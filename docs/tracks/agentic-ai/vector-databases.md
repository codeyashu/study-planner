---
title: "Vector databases: pgvector, Qdrant & friends"
track: agentic-ai
slug: vector-databases
priority: P0
complexity: 3
est_hours: 3
phase: 2
tags: [agentic-ai, P0]
last_reviewed: 2026-09-25
---

# Vector databases: pgvector, Qdrant & friends

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 3 h · **Phase:** 2 · **Prereqs:** [RAG fundamentals](rag-fundamentals.md), [Hybrid search & reranking](hybrid-search-reranking.md)
    **You're done when:** you can size, index, tune and benchmark a pgvector deployment (recall vs latency vs memory), explain HNSW vs IVF vs quantization trade-offs, and justify pgvector vs a dedicated vector DB for a given scale and filter pattern.

## Why it matters

Every RAG, memory and semantic-search system needs approximate nearest neighbour (ANN) search over embeddings. Choosing the store is an architecture decision with lasting cost: operational complexity, filter behaviour, consistency with your source-of-truth data, re-indexing pain, and cloud bill. For a senior engineer the default question is not "which vector DB is best" but **"do I need a separate system at all?"** For most enterprise workloads under ~50M vectors, Postgres + pgvector is the boring, correct answer; beyond that or with special needs (heavy filtered search, multi-tenancy at scale, quantization, sparse+dense native fusion) a dedicated engine such as Qdrant earns its keep.

## Core concepts

### Exact vs approximate search

Exact (brute-force) kNN is O(N·d) per query: fine up to ~100k vectors (a few ms with SIMD), untenable at millions. ANN trades a little recall for orders-of-magnitude speed. Two families dominate:

| Index | Idea | Build cost | Memory | Query | Recall knob | Notes |
|---|---|---|---|---|---|---|
| **HNSW** | Multi-layer proximity graph; greedy descent from sparse top layers to dense bottom layer | High (minutes-hours at 10M+) | High (vectors + graph, ~1.5-2x raw) | ~1-10 ms | `ef_search` | Best recall/latency; default choice; supports incremental inserts well |
| **IVF (IVFFlat)** | k-means clusters; search only the `nprobe` closest lists | Lower; needs data to train centroids | Low (~raw) | Depends on `nprobe` | `probes` | Must build after data loaded; recall drops when data drifts; good for memory-tight, batch loads |
| **DiskANN / Vamana** | Graph optimised for SSD | High | Low RAM | Higher latency | search list size | pgvectorscale (StreamingDiskANN), some managed engines |
| **Flat** | Brute force | None | Raw | O(N) | none | Baseline for measuring ANN recall |

HNSW parameters: `m` (edges per node, default 16; higher = better recall, more memory), `ef_construction` (build-time candidate list, default 64; 100-200 for higher quality), `ef_search` (query-time, default 40 in pgvector; raise for recall, e.g. 100-200). Rule of thumb: tune `ef_search` to hit recall@10 >= 0.95-0.98 against a flat baseline, then look at latency.

### Distance metrics

Use **cosine** (or inner product on L2-normalised vectors — identical ranking and slightly cheaper) for text embeddings unless the model card says otherwise. pgvector operators: `<=>` cosine distance, `<->` L2, `<#>` negative inner product, `<+>` L1. The operator class on the index must match the operator in your query or the index isn't used.

### Quantization and compression

Memory is the dominant cost. Options, from safest to most aggressive:

- **float16 (`halfvec`)**: 2x smaller, negligible recall loss. pgvector supports `halfvec` up to 4,000 dims indexed (vs 2,000 for `vector`).
- **Scalar quantization (int8)**: 4x smaller (Qdrant, others), small loss, often with rescoring on originals.
- **Binary quantization**: 32x smaller, hamming distance; works best with high-dim (>=768/1024) models trained for it, then **rescore the top-N with full vectors**. pgvector supports `bit` with hamming/jaccard.
- **Product quantization (PQ)**: 8-64x, larger recall loss, common in IVF-PQ / FAISS.
- **Matryoshka truncation**: use fewer dimensions from models trained for it (e.g. 256 of 1024).

Pattern: quantized index for the candidate set (fast, small) + full-precision rerank of top 100 -> top-k. Always measure recall on your golden set.

### The filter problem (the thing that bites in production)

Real queries are "nearest neighbours **where** tenant = X and service = Y and acl contains G." Graph indexes and filters interact badly:

- **Post-filtering**: ANN top-k first, then filter -> returns fewer than k (or zero) when the filter is selective. pgvector's HNSW historically did this: with `ef_search=40` and a filter matching 1% of rows you get ~0 results.
- **Pre-filtering** (filter, then exact search over the subset): correct and fast when the subset is small (< ~10-50k rows), where a B-tree or partial index narrows candidates first — Postgres's planner may choose this automatically.
- **Iterative index scans** (pgvector >= 0.8): `SET hnsw.iterative_scan = relaxed_order;` keeps scanning the graph until enough filtered rows are found (bounded by `hnsw.max_scan_tuples`). Big practical fix; `strict_order` preserves exact distance ordering at more cost.
- **Filterable HNSW** (Qdrant): payload indexes, and the graph is built with extra links so filtered traversal stays connected; query planner switches between graph and payload-index scan by filter cardinality.
- **Partitioning** by tenant (Postgres declarative partitions with a per-partition HNSW, or Qdrant collections/tenant payload with `is_tenant`) — the cleanest multi-tenant answer at scale.

Test with your *worst* filter (most selective) before choosing.

### pgvector in practice

```sql
CREATE EXTENSION vector;
CREATE TABLE chunks (
  id bigserial PRIMARY KEY, tenant_id int NOT NULL, service text,
  content text NOT NULL, embedding halfvec(1024) NOT NULL
);
-- build AFTER bulk load; give it memory
SET maintenance_work_mem = '4GB'; SET max_parallel_maintenance_workers = 7;
CREATE INDEX chunks_hnsw ON chunks USING hnsw (embedding halfvec_cosine_ops)
  WITH (m = 16, ef_construction = 128);
CREATE INDEX ON chunks (tenant_id, service);

-- query
SET hnsw.ef_search = 100; SET hnsw.iterative_scan = relaxed_order;
SELECT id, embedding <=> $1 AS dist FROM chunks
WHERE tenant_id = $2 AND service = $3
ORDER BY embedding <=> $1 LIMIT 20;
```

Operational facts: the HNSW index should fit in `shared_buffers`/OS cache or latency spikes (check with `pg_buffercache`/`EXPLAIN (ANALYZE, BUFFERS)`); index build for 10M x 1024-dim can take hours; `VACUUM` behaves normally but heavy update/delete churn degrades graph quality (REINDEX CONCURRENTLY occasionally); WAL volume from inserts is large; replicas work like any table (huge operational win: backups, PITR, HA, transactions with your metadata). **pgvectorscale** adds StreamingDiskANN and label-filtered search; **VectorChord** and **ParadeDB** are other Postgres-native options; managed: Azure Database for PostgreSQL (pgvector + DiskANN option), AWS RDS/Aurora, Cloud SQL, Supabase, Neon.

### Landscape (as of September 2026)

| Option | Sweet spot | Watch out |
|---|---|---|
| **pgvector (+scale)** | < ~50M vectors, need SQL joins/transactions/ACLs in same DB, small team | Memory-bound HNSW, filtering tuning, single-node write limits |
| **Qdrant** | Heavy filtering, multi-tenancy, quantization, sparse+dense hybrid, Rust performance, self-host or cloud | Another system to run; eventual consistency with your source of truth |
| **Weaviate / Milvus** | Large scale (100M-billions), built-in modules / distributed architecture | Operational heft (Milvus), learning curve |
| **Elasticsearch/OpenSearch** | Already the search platform; rich lexical + kNN | Heavier per vector; cost |
| **Azure AI Search / Vertex / OpenSearch Serverless / Pinecone** | Managed, low ops, integrated hybrid + semantic ranking | Cost at scale, lock-in, less control |
| **Redis / Mongo Atlas / Cosmos DB** | Vectors alongside existing data, modest scale | Feature depth varies |
| **FAISS / hnswlib / Lucene libs** | Embedded, in-process, offline batch | You build persistence, filters, HA |

Decision heuristics: (1) < 5M vectors and already on Postgres -> pgvector, done; (2) 5-50M with mostly tenant/ACL filters -> pgvector with partitioning/iterative scans or Qdrant; (3) > 100M or > 1,000 QPS with tight p99 -> dedicated engine with sharding; (4) need consistency between metadata and vectors in one transaction -> Postgres.

### Sizing worksheet

Raw bytes = N x dims x bytes/dim. Index overhead HNSW ~ N x m x 2 x 4-8 B. Example: 10M x 1,024 x 2 B (halfvec) = 20 GB + graph ~ 10 GB -> ~30 GB RAM-resident for good latency. Throughput: HNSW at ef=100 is ~1-5 ms/query single-threaded on warm cache; QPS scales with cores. Recall must be measured: build a flat ground truth on 1k-10k queries and compute recall@10 of the ANN result.

### Consistency and lifecycle

- **Dual-write problem** with a separate DB: ingest via an outbox/CDC pipeline keyed by document ID + content hash; make upserts idempotent; reconcile periodically.
- **Deletes and GDPR erasure** need to hit the vector store too (tombstones, then compaction).
- **Embedding versioning**: separate collection/column per model version; dual-read during migration; cut over after golden-set validation.
- **Backups**: pgvector inherits PITR; dedicated stores need snapshot procedures you have tested.

### What juniors miss

- Never comparing ANN to a flat baseline, so recall is unknown.
- Building HNSW before loading data (slow) or with tiny `maintenance_work_mem`.
- Selective filters returning empty results.
- Index bigger than RAM -> latency cliffs.
- Using `<->` in the query but a cosine index -> sequential scan.
- Storing full-precision vectors "just in case" of 3072 dims when 512 Matryoshka dims would pass evals.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [pgvector README](https://github.com/pgvector/pgvector) | docs | Authoritative on types, HNSW/IVFFlat params, iterative scans, filtering | intermediate | free |
| [pgvectorscale](https://github.com/timescale/pgvectorscale) :gem: | docs | StreamingDiskANN + label filtering for Postgres; benchmarks and tuning | advanced | free |
| [Qdrant documentation](https://qdrant.tech/documentation/) | docs | Filterable HNSW, quantization, multitenancy, hybrid queries | intermediate | free |
| [Pinecone - Hierarchical Navigable Small Worlds](https://www.pinecone.io/learn/series/faiss/hnsw/) | article | Best visual explanation of how HNSW search actually works | intermediate | free |
| [ANN-Benchmarks](https://ann-benchmarks.com/) :gem: | interactive | Recall vs QPS curves across algorithms; learn to read the trade-off frontier | advanced | free |
| [Jonathan Katz - blog](https://jkatz05.com/) :gem: | article | pgvector committer's deep dives on performance, quantization, filtering | advanced | free |
| [Supabase - hybrid search](https://supabase.com/docs/guides/ai/hybrid-search) | docs | Practical Postgres FTS + vector patterns | intermediate | free |
| [Chip Huyen - AI Engineering](https://github.com/chiphuyen/aie-book) | book | Systems view of retrieval infrastructure trade-offs | advanced | paid |

## Hands-on lab

**Goal:** benchmark pgvector for the capstone and produce a recall/latency/memory table plus a Qdrant comparison. (2 h)

1. Generate 1M synthetic-but-realistic vectors: embed 20k real chunks and add 980k perturbed copies (or use a public embedding dataset such as a 1M-vector slice; do not invent results). Use 768 dims (Ollama `nomic-embed-text`) with a `tenant_id` (100 tenants, Zipf-distributed) and `service` column.
2. Load into `halfvec(768)` with COPY; **then** create HNSW indexes with (m, ef_construction) in {(16,64), (16,128), (32,128)}. Record build time and `pg_relation_size`.
3. Ground truth: brute-force top-10 for 1,000 queries via `SET enable_indexscan=off` (or a numpy flat pass).
4. For `ef_search` in {40, 100, 200, 400}: measure recall@10, p50/p95 latency, with (a) no filter, (b) `tenant_id = large tenant`, (c) `tenant_id = tiny tenant (0.1% of rows)` with and without `hnsw.iterative_scan = relaxed_order`.
5. Repeat (a)-(c) on Qdrant (docker compose service, payload index on `tenant_id`, `is_tenant=true`).
6. Write `docs/adr/vector-store.md` with the table, the worst-filter result, and your decision for the capstone.

*Expected shape:* no-filter recall@10 ~0.97+ at ef=100; the tiny-tenant filter without iterative scan returns << 10 rows (the classic failure); with iterative scan or partial/partitioned indexes it recovers. Qdrant handles the tiny-tenant filter natively. Numbers depend on hardware; record yours.

## Questions

### L1 — Recall

??? question "Q1. How does HNSW search work and what do m, ef_construction and ef_search control?"
    ??? success "Answer"
        HNSW is a layered proximity graph. Search enters at the sparse top layer, greedily moves to the closest neighbour until no improvement, then descends a layer and repeats, finishing at the dense base layer where it explores a candidate list of size `ef_search`. `m` = max edges per node (connectivity; more = higher recall and memory), `ef_construction` = candidate list size while inserting (better graph quality, slower build), `ef_search` = query-time breadth (recall vs latency knob).

??? question "Q2. Why must the query operator match the index operator class in pgvector?"
    ??? success "Answer"
        The index is built for one distance function (e.g. `vector_cosine_ops` supports `<=>`). If the query orders by `<->` (L2) the planner can't use the index and falls back to a sequential scan (exact but slow). Always verify with `EXPLAIN` that an Index Scan on the HNSW index is used.

??? question "Q3. What is the trade-off between HNSW and IVFFlat?"
    ??? success "Answer"
        HNSW: better recall/latency and handles inserts incrementally, but slower to build and uses more memory. IVFFlat: faster to build and smaller, but requires training on existing data (build after loading), recall depends on `probes` and degrades as data distribution drifts, and it typically needs a rebuild after big changes.

### L2 — Apply

??? question "Q4. Size a pgvector deployment for 20M chunks, 1,024-dim embeddings, target p95 < 50 ms."
    ??? success "Answer"
        With `halfvec(1024)`: 20M x 2 KB = ~41 GB raw. HNSW m=16 adds ~ 20M x 32 links x ~6-8 B ~ 4-5 GB (plus per-node overhead), so ~45-50 GB index; plus text/metadata heap (a separate few tens of GB not required in RAM). Provision a node with >= 64-96 GB RAM so the index stays cached (shared_buffers ~ 25%, rest OS cache), NVMe storage, and 8+ cores. Build with high `maintenance_work_mem` and parallel workers (expect hours). Consider Matryoshka 512 dims or binary quantization + rescoring to halve or shrink further; validate recall@10 >= 0.95 vs flat on 1k queries. If filters are selective, use partitioning or iterative scans; add read replicas for QPS.

??? question "Q5. A query with `WHERE tenant_id = 42 ORDER BY embedding <=> $1 LIMIT 10` returns 2 rows for a tenant with 5,000 chunks. Diagnose and fix."
    ??? success "Answer"
        HNSW returns the global top `ef_search` (40) candidates and Postgres filters them afterwards; only 2 belong to tenant 42. Fixes: enable iterative scans (`SET hnsw.iterative_scan = relaxed_order`, raise `hnsw.max_scan_tuples` if needed); create a B-tree on `tenant_id` so the planner can pre-filter and run exact search for small tenants; partition the table by tenant (or tenant hash) with per-partition HNSW; or raise `ef_search`. Verify with the golden set that filtered recall is restored.

??? question "Q6. How do you measure ANN recall for your index?"
    ??? success "Answer"
        Take a representative sample of ~1,000 real queries, compute exact top-k with brute force (disable index scan or a flat pass) as ground truth, run the same queries via the ANN index at the chosen parameters, and compute recall@k = |ANN ∩ exact| / k averaged over queries. Repeat per filter slice. Plot recall against p95 latency while varying `ef_search` to choose the operating point. This measures index quality; end-to-end retrieval quality still needs the labelled golden set.

### L3 — Design & trade-offs

??? question "Q7. pgvector vs Qdrant for a multi-tenant SaaS with 5,000 tenants (skewed sizes, total 80M vectors) and per-tenant ACLs. Decide."
    ??? success "Answer"
        At 80M vectors with highly selective per-tenant filters, dedicated filterable HNSW and native multitenancy (Qdrant `is_tenant` payload indexes, or sharded collections) is attractive: filtered traversal stays connected, quantization reduces RAM, and horizontal scaling exists. pgvector can work with partitioning by tenant hash and iterative scans but 80M x 1024 dims strains a single node (memory, build time) and a partition per tenant at 5,000 tenants is heavy. Trade-off: Qdrant adds a system and an ingestion pipeline (outbox/CDC, reconciliation) and ACL/metadata consistency concerns; Postgres offers transactional consistency and simpler ops. I'd prototype both on the worst-case tenant filter and pick Qdrant if pgvector needs > 1 large node or fails the p95 for tiny tenants — otherwise stay on Postgres. Record in an ADR with the re-evaluation trigger (e.g. > 100M vectors).

??? question "Q8. When is quantization worth the recall loss, and how do you deploy it safely?"
    ??? success "Answer"
        When memory (hence cost) dominates and evals show negligible task impact: halfvec is almost free; int8 scalar is usually safe; binary works for high-dim models with rescoring. Deploy as two-stage: quantized index retrieves e.g. 200 candidates, then rescore with full-precision vectors to top-20, then rerank. Validate recall@k and end-to-end answer metrics on the golden set, canary in shadow mode, and keep originals (on disk) so you can re-quantize. Avoid PQ unless you need extreme compression and can accept recall loss.

??? question "Q9. Should the vector index live in the same database as the source-of-truth business data?"
    ??? success "Answer"
        Same DB (pgvector) gives transactional consistency (a deleted document disappears atomically), joins for metadata/ACLs, single backup/HA story, fewer moving parts — great at moderate scale. Separate DB gives independent scaling, specialised features and isolation of heavy ANN workloads from OLTP. Middle path: Postgres replica/dedicated instance for retrieval fed via logical replication or CDC, retaining Postgres semantics. Decide by scale, workload interference (index builds and vector scans are memory/IO hungry), and team ops capacity.

### L4 — Staff-level ambiguity

??? question "Q10. Your org has Pinecone, Elasticsearch kNN, and three pgvector instances across teams. The CFO wants consolidation. What is your plan?"
    ??? success "Answer"
        Inventory: vectors count, dims, QPS, filters, latency SLOs, cost, data classification, owners. Build a shared benchmark harness and golden sets per workload class. Define 2 supported tiers: (1) Postgres+pgvector as the default (<= ~50M vectors), (2) one dedicated engine for large or filter-heavy workloads (chosen by bake-off). Provide a retrieval SDK/service abstracting store specifics (hybrid, filters, embedding versioning) so migrations are mechanical. Migrate the costliest workloads first with dual-write/dual-read and golden-set parity gates; decommission on a timeline. Avoid forced migration where the business value is low; use showback to make cost visible.

??? question "Q11. Six months in, recall regressed 8 points after a model upgrade nobody flagged. How do you make vector infra safe against this class of failure?"
    ??? success "Answer"
        Treat the embedding model + chunker + index params as a versioned artifact: store `embedding_model/version` per row, require a new collection/column for changes, and gate cutover on the golden-set eval in CI (recall@k slices, per-service). Monitor online proxies (empty-result rate, mean top-1 score, click/thumb rates, reranker score distributions) and alert on drift. Add a canary index with shadow traffic before promotion, and document the runbook for rollback (keep the old index until stable). Ownership: a named retrieval platform owner with a change process (RFC + eval evidence).

## Real-world use cases

- **Ops copilot knowledge base:** pgvector alongside incident metadata in the same Postgres; ACL/service filters in SQL.
- **Multi-tenant document Q&A SaaS:** Qdrant with tenant payload index and scalar quantization.
- **Semantic dedup of support tickets:** offline FAISS/hnswlib batch job writing cluster IDs back to the warehouse.
- **Product/parts search for logistics equipment:** hybrid in OpenSearch because catalogue search already lives there.

## Pitfalls & anti-patterns

- Adopting a dedicated vector DB "because RAG" at 200k vectors.
- Unknown recall (no flat baseline).
- Unindexed or highly selective filters with post-filtering.
- Index larger than RAM.
- No embedding version column; no re-index plan.
- Ignoring delete/erasure propagation.
- Benchmarks on random vectors instead of your embeddings and queries.

## Checklist

- [ ] I can explain HNSW, IVF, quantization and the filter problem
- [ ] I benchmarked recall/latency/memory on pgvector including worst-case filters
- [ ] I compared against Qdrant and wrote an ADR
- [ ] I can size an index from N, dims and bytes per dim
- [ ] I answered all L3 questions out loud in < 3 min each
