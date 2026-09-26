---
title: "Week 05 — RAG fundamentals, caching, hexagonal"
week: 5
generated: true
---

# Week 05 — RAG fundamentals, caching, hexagonal

!!! abstract "At a glance"
    **Phase 2:** RAG + Evals · **Starts:** Mon 26 Oct 2026 · **Planned:** 16h 45m

    **Build:** Capstone: RAG v0 — ingest runbooks/postmortems into pgvector, naive dense retrieval behind a Retriever port

## By day

### Monday 26 Oct · 2h 00m

- [ ] **System Design** · 45 min · Caching strategies: cache-aside, write-through, write-behind, TTL + stampede protection (request coalescing, probabilistic early expiry) → [Caching strategies](../../tracks/system-design/caching.md) <small>`w05-sd-1`</small>
- [ ] **DSA** · 25 min · Generate Parentheses (stack + backtracking warm-up) → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w05-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: pytest fixtures with scopes + factories; parametrize retrieval tests → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w05-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Sentence structure and parallelism → [Week 05 drills · day 1](../../tracks/communication/drills/week-05.md#day-1) <small>`w05-comm-1`</small>

### Tuesday 27 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · RAG fundamentals: chunking strategies (fixed, recursive, semantic, structure-aware), embedding model choice, top-k — write a comparison table for runbooks/postmortems → [RAG fundamentals: chunking, embeddings, retrieval](../../tracks/agentic-ai/rag-fundamentals.md) · [resource](https://eugeneyan.com/writing/llm-patterns/) <small>`w05-ai-1`</small>
- [ ] **DSA** · 30 min · Binary Search + Search a 2D Matrix → [Binary search (incl. on answer)](../../tracks/dsa/binary-search.md) · [resource](https://neetcode.io) <small>`w05-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Analytical words: consequently, whereas, mitigate, hinge on → [Week 05 drills · day 2](../../tracks/communication/drills/week-05.md#day-2) <small>`w05-comm-2`</small>

### Wednesday 28 Oct · 2h 00m

- [ ] **DSA** · 25 min · Koko Eating Bananas (binary search on answer) → [Binary search (incl. on answer)](../../tracks/dsa/binary-search.md) · [resource](https://neetcode.io) <small>`w05-dsa-3`</small>
- [ ] **Architecture** · 45 min · Cosmic Python ch1-3 / hexagonal architecture: domain model, repository, ports & adapters — sketch capstone layers → [Hexagonal / clean architecture, ports & adapters](../../tracks/architecture/hexagonal-clean.md) · [resource](https://www.cosmicpython.com/) <small>`w05-arch-1`</small>
- [ ] **Python** · 20 min · Rep: Repository pattern for chunks (abstract base vs Protocol), in-memory fake for tests → [Architecture patterns in Python (repository, UoW, message bus)](../../tracks/python/architecture-patterns-python.md) · [resource](https://www.cosmicpython.com/) <small>`w05-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: PREP and pyramid structure for answers → [Week 05 drills · day 3](../../tracks/communication/drills/week-05.md#day-3) <small>`w05-comm-3`</small>

### Thursday 29 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · Vector databases: pgvector HNSW vs IVFFlat parameters (m, ef_construction, ef_search, lists) — build an index on 50k chunks and measure recall@10 vs latency → [Vector databases: pgvector, Qdrant & friends](../../tracks/agentic-ai/vector-databases.md) · [resource](https://github.com/pgvector/pgvector) <small>`w05-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI VectorStore with PgVectorStore: configure dimensions, index type, metadata filters → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) · [resource](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) <small>`w05-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Strategy metaphors: low-hanging fruit, moving parts → [Week 05 drills · day 4](../../tracks/communication/drills/week-05.md#day-4) <small>`w05-comm-4`</small>

### Friday 30 Oct · 2h 00m

- [ ] **System Design** · 45 min · Storage engines: B-tree vs LSM-tree, write/read amplification (DDIA 2e storage chapter) → [Databases: SQL vs NoSQL, storage engines](../../tracks/system-design/databases-sql-nosql.md) · [resource](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) <small>`w05-sd-2`</small>
- [ ] **DSA** · 25 min · Find Minimum in Rotated Sorted Array → [Binary search (incl. on answer)](../../tracks/dsa/binary-search.md) · [resource](https://neetcode.io) <small>`w05-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: __iter__/__len__/__getitem__ on a ChunkCollection; sequence protocol vs subclassing list → [Python data model & dunder protocols](../../tracks/python/data-model.md) · [resource](https://www.fluentpython.com/) <small>`w05-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Writing a design-doc summary → [Week 05 drills · day 5](../../tracks/communication/drills/week-05.md#day-5) <small>`w05-comm-5`</small>

### Saturday 31 Oct · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: ingestion pipeline (Markdown/PDF → chunks → embeddings → pgvector via docker-compose) + Retriever port with dense adapter; answer with citations → [RAG fundamentals: chunking, embeddings, retrieval](../../tracks/agentic-ai/rag-fundamentals.md) <small>`w05-ai-3`</small>
- [ ] **DSA** · 30 min · Search in Rotated Sorted Array + Time Based Key-Value Store → [Binary search (incl. on answer)](../../tracks/dsa/binary-search.md) · [resource](https://neetcode.io) <small>`w05-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI ETL: DocumentReader → TokenTextSplitter → VectorStore for the same runbook corpus → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w05-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: PREP and pyramid structure for answers → [Week 05 drills · day 6](../../tracks/communication/drills/week-05.md#day-6) <small>`w05-comm-6`</small>

### Sunday 01 Nov · 3h 15m

- [ ] **System Design** · 45 min · Written design: apply your AI system design framework to 'design an internal support chatbot' — requirements, data, model choice, eval plan, risks → [AI system design interview framework](../../tracks/ai-system-design/framework.md) · [resource](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) <small>`w05-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 005 for capstone: hexagonal layout with retrieval, LLM and ticketing as ports → [Hexagonal / clean architecture, ports & adapters](../../tracks/architecture/hexagonal-clean.md) · [resource](https://adr.github.io) <small>`w05-arch-2`</small>
- [ ] **Staff+** · 30 min · Outline the capstone design doc (context, goals/non-goals, architecture, alternatives, risks, rollout) → [Design docs & RFCs that get approved](../../tracks/staff-skills/design-docs-rfcs.md) <small>`w05-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Facilitating a meeting → [Week 05 drills · day 7](../../tracks/communication/drills/week-05.md#day-7) <small>`w05-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back: caching stampede mitigations + LSM vs B-tree in 3 min each; 20 flashcards on RAG vocabulary → [Caching strategies](../../tracks/system-design/caching.md) <small>`w05-rev-1`</small>

## By track

| Track | Tasks | Time |
|---|---|---|
| Agentic AI | 3 | 4h 00m |
| System Design | 3 | 2h 15m |
| DSA | 5 | 2h 15m |
| Architecture | 2 | 1h 15m |
| Python | 3 | 1h 00m |
| Java/Spring AI | 2 | 1h 00m |
| Staff+ | 1 | 30m |
| Communication | 7 | 3h 30m |
| Review | 1 | 1h 00m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
