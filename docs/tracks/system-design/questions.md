---
title: System design question bank
track: system-design
tags: [system-design, questions]
last_reviewed: 2026-09-25
---

# System design question bank

Cross-topic interview bank for the system design track: **62 graded questions (L1–L4)**, **16 use-case scenarios**, and **30 rapid-fire one-liners** for spaced review. Every item has a collapsible model answer. Say your answer out loud before you open it.

!!! tip "How to use this page"
    - **Weekdays:** 5 rapid-fire + 2 graded questions (≈ 15 min).
    - **Saturday:** 2 scenarios, whiteboarded end to end with a timer (25 min each).
    - **Checkpoint weeks (4/8/12/16/20/24):** a random L3 + L4 pair out loud, recorded; grade against the model answer.
    - Levels: L1 recall · L2 apply · L3 design & trade-offs · L4 Staff ambiguity.

Case-study walkthroughs: [URL shortener](case-studies/url-shortener.md) · [News feed](case-studies/news-feed.md) · [Chat](case-studies/chat-system.md) · [Notifications](case-studies/notification-system.md) · [Payments](case-studies/payment-system.md) · [KV store](case-studies/distributed-kv-store.md) · [Metrics](case-studies/metrics-monitoring.md) · [Ride hailing](case-studies/ride-hailing-proximity.md) · [Job scheduler](case-studies/job-scheduler.md)

## L1 — Recall

??? question "Q1. What does a write-ahead log guarantee, and what does it not?"
    ??? success "Answer"
        Durability and atomicity of committed changes: a change is appended (and fsynced) to the log before it's applied to data pages, so after a crash the system replays the log to reach a consistent state. It does **not** guarantee replication/availability (a disk loss loses the WAL unless it's shipped) and, if fsync is disabled or batched (group commit windows), the last few ms of commits can be lost. Related: [databases](databases-sql-nosql.md).

??? question "Q2. State CAP precisely and explain why PACELC is more useful."
    ??? success "Answer"
        CAP: during a network **partition**, a system must choose between linearizable consistency and availability (every non-failed node responds). It says nothing about normal operation. PACELC adds: **Else** (no partition), choose between **Latency** and **Consistency** — the trade-off you pay every day (e.g. synchronous cross-AZ replication adds ms to every write). See [consistency models](consistency-models.md).

??? question "Q3. Define linearizability, sequential consistency, and causal consistency in one line each."
    ??? success "Answer"
        Linearizable: every operation appears to take effect atomically at a single point between its invocation and response, respecting real time. Sequential: all nodes see operations in the same total order consistent with each client's program order, but not necessarily real time. Causal: operations that are causally related are seen in the same order by everyone; concurrent ones may be seen in different orders.

??? question "Q4. What is consistent hashing and why do virtual nodes help?"
    ??? success "Answer"
        Keys and nodes are hashed onto a ring; each key belongs to the next node clockwise, so adding/removing a node moves only ~1/N of keys. With one token per node, load is uneven and a failed node's entire range lands on one neighbour; virtual nodes (many tokens per node) even out the distribution and spread rebuild load across many nodes. See [partitioning](partitioning-sharding.md).

??? question "Q5. Name the four cache write strategies and one risk of each."
    ??? success "Answer"
        Cache-aside (lazy load): stale data / stampede on miss. Read-through: same staleness, ties cache to loader. Write-through: write latency and caching data never read. Write-back (write-behind): data loss if cache dies before flush. Plus write-around: first read after write misses. See [caching](caching.md).

??? question "Q6. What is the difference between L4 and L7 load balancing?"
    ??? success "Answer"
        L4 balances TCP/UDP connections by IP/port without inspecting payloads — fast, protocol-agnostic, but can't route by path/header and balances connections not requests (bad for long-lived HTTP/2 or gRPC). L7 terminates HTTP, routes by host/path/header, does retries, per-request balancing, TLS termination, auth — at higher CPU cost. See [load balancing](load-balancing.md).

??? question "Q7. What does an idempotency key do, and who generates it?"
    ??? success "Answer"
        It lets the server recognise retries of the same logical request and return the original result instead of executing twice. The **client** generates it (UUID per logical operation) so retries after timeouts carry the same key; the server stores key → (request hash, response) with a TTL. See [API design](api-design.md) and the [payment case study](case-studies/payment-system.md).

??? question "Q8. Token bucket vs leaky bucket vs sliding window counter?"
    ??? success "Answer"
        Token bucket: tokens refill at rate r up to capacity b; allows bursts up to b. Leaky bucket: requests drain at a constant rate; smooths output, no bursts. Sliding window counter: approximates a rolling window by weighting the previous fixed window's count; cheap and avoids boundary spikes of fixed windows. See [rate limiting](rate-limiting.md).

??? question "Q9. What is a quorum and what does R + W > N give you?"
    ??? success "Answer"
        With N replicas, a write waits for W acks and a read queries R replicas. If R + W > N, every read set overlaps every write set, so a read sees at least one replica with the latest acknowledged write (assuming no sloppy quorums and a way to pick the newest version). It does not by itself give linearizability under concurrent writes or failures.

??? question "Q10. What problem do fencing tokens solve?"
    ??? success "Answer"
        A lock/lease holder can pause (GC, VM stall) past lease expiry while another node acquires the lease; when the first wakes, it believes it still holds the lock. A fencing token is a monotonically increasing number issued with each lease; the protected resource rejects writes with a token lower than the highest seen. See [consensus](consensus-raft.md).

??? question "Q11. What is the difference between a message queue and a log (Kafka)?"
    ??? success "Answer"
        Queue (SQS, RabbitMQ): messages are consumed and deleted, per-message acks, competing consumers, no replay. Log: append-only, retained by time/size, consumers track offsets, multiple independent consumer groups, replayable, ordered per partition. Logs suit event streaming and rebuilding state; queues suit task distribution with per-message retries. See [messaging](messaging-streaming.md).

??? question "Q12. What are the four golden signals?"
    ??? success "Answer"
        Latency (distinguish successful vs failed requests), traffic, errors, saturation (Google SRE book). RED (rate, errors, duration) for services and USE (utilisation, saturation, errors) for resources are complementary. See [observability & SLOs](observability-slos.md).

??? question "Q13. What is an inverted index?"
    ??? success "Answer"
        A map from term → posting list of document IDs (often with positions and frequencies), enabling fast full-text lookups; ranking uses BM25 over term statistics. Posting lists are compressed (delta + variable-byte/PFOR) and merged across immutable segments. See [search systems](search-systems.md).

??? question "Q14. RPO vs RTO?"
    ??? success "Answer"
        RPO (recovery point objective): maximum acceptable data loss measured in time (e.g. 5 min of writes). RTO (recovery time objective): maximum acceptable downtime until service is restored. Async replication → RPO > 0; synchronous → RPO ≈ 0 at the cost of write latency. See [multi-region & DR](multi-region-dr.md).

??? question "Q15. What is the outbox pattern?"
    ??? success "Answer"
        Write the business change and an event row into an `outbox` table in the **same local transaction**; a relay (poller or CDC like Debezium) publishes outbox rows to the broker and marks them sent. Guarantees the event is published if and only if the transaction commits (at-least-once publishing; consumers dedupe). Avoids dual-write inconsistency.

## L2 — Apply

??? question "Q16. Size a Redis cluster for 50 k QPS, 1 KB values, 20 M keys, p99 < 5 ms."
    ??? success "Answer"
        Memory: 20 M × (1 KB + ~100 B overhead) ≈ 22 GB; with 30–50% headroom for fragmentation and failover ≈ 30–35 GB. Throughput: one Redis shard handles ~100 k simple ops/s, but keep < 50% CPU for tail latency → 50 k QPS fits on 1–2 shards; for memory and HA, 3 shards × ~12 GB with 1 replica each. Bandwidth: 50 k × 1 KB = 50 MB/s — fine. p99 < 5 ms is achievable if you avoid big keys/slow commands (KEYS, large ZRANGE).

??? question "Q17. You have 10 k writes/s to Postgres and it's at 85% CPU. List five things you check before sharding."
    ??? success "Answer"
        (1) Query plans and missing/unused indexes (write amplification from too many indexes). (2) Batch writes / COPY instead of row-by-row, fewer round trips. (3) Connection pooling (PgBouncer) — thousands of connections burn CPU. (4) Hot rows / lock contention (counters) → redesign. (5) Move reads to replicas and cache; vacuum/autovacuum tuning; partition large tables by time. Then vertical scaling. Shard only when a single primary's write capacity is truly exhausted.

??? question "Q18. Estimate: 100 M DAU, each uploads 2 photos/day at 2 MB. Storage per year and upload bandwidth?"
    ??? success "Answer"
        200 M photos/day × 2 MB = 400 TB/day → ~146 PB/year raw; with thumbnails/variants (+20%) and replication/erasure coding (~1.4x) ≈ 245 PB/yr. Upload: 400 TB/86,400 s ≈ 4.6 GB/s avg ≈ 37 Gbps, peak ×3 ≈ 110 Gbps. Conclusion: direct-to-object-storage uploads via pre-signed URLs; app servers never proxy bytes. See [storage & CDN](storage-cdn.md).

??? question "Q19. Design cursor pagination for `GET /orders?status=open` sorted by created_at."
    ??? success "Answer"
        Sort by `(created_at DESC, id DESC)` for a total order; cursor = base64 of the last row's `(created_at, id)`; next page query `WHERE status='open' AND (created_at, id) < (:c_ts, :c_id) ORDER BY created_at DESC, id DESC LIMIT 50` with an index on `(status, created_at DESC, id DESC)`. Stable under inserts, O(page) cost regardless of depth, unlike OFFSET.

??? question "Q20. A service calls 3 dependencies in sequence with 99.9% availability each. What's the composite availability and how do you improve it?"
    ??? success "Answer"
        0.999³ ≈ 99.7% (≈ 26 h downtime/yr vs 8.8 h for one). Improve: make calls parallel where possible (doesn't change availability, improves latency), make non-critical dependencies optional with fallbacks/defaults, cache responses, add redundancy (active-active dependency instances), and use timeouts + circuit breakers so a slow dependency doesn't consume all threads. See [reliability patterns](reliability-patterns.md).

??? question "Q21. Configure retries for a client calling an API with p99 = 200 ms."
    ??? success "Answer"
        Timeout slightly above p99 (e.g. 300 ms), max 2–3 attempts, exponential backoff with full jitter (e.g. base 50 ms, cap 1 s), retry only idempotent operations or those with idempotency keys, respect `Retry-After`/429, and a **retry budget** (e.g. retries ≤ 10% of requests) to avoid retry storms. Only retry at one layer of the stack.

??? question "Q22. Kafka topic for order events: 20 k msgs/s peak, 1 KB each, 7-day retention. Partitions and storage?"
    ??? success "Answer"
        Throughput 20 MB/s; a partition comfortably handles ~5–10 MB/s writes, but consumer parallelism usually drives the count: if a consumer instance processes 1 k msgs/s, need ≥ 20 partitions → choose 48 for growth (partitions are hard to change without reordering keys). Storage: 20 MB/s × 604,800 s ≈ 12 TB × RF 3 ≈ 36 TB (peak-based upper bound; avg lower). Key by `order_id` for per-order ordering.

??? question "Q23. How would you implement a distributed rate limiter at 200 k req/s across 50 gateway nodes?"
    ??? success "Answer"
        Options: (a) central Redis with Lua token bucket per key — accurate, adds ~1 ms and a dependency; shard Redis by key. (b) Local token buckets per node with limit/N — no network hop, inaccurate with uneven LB. (c) Hybrid: local buckets that periodically sync counts with Redis (e.g. every 100 ms). For 200 k req/s, (c) or (a) with pipelining. Fail open for availability-critical APIs, fail closed for abuse-protection endpoints.

??? question "Q24. Choose a shard key for a multi-tenant SaaS orders table (10 k tenants, top tenant = 15% of data)."
    ??? success "Answer"
        `tenant_id` keeps tenant queries single-shard and eases isolation/residency, but the 15% tenant becomes a hot shard. Solution: tenant_id as the key with a directory (tenant → shard) so big tenants get dedicated shards, and for the largest, a compound key `(tenant_id, hash(order_id))` spanning multiple shards. Avoid pure `hash(order_id)` — every tenant query becomes scatter-gather.

??? question "Q25. Estimate the number of servers for 30 k RPS where each request needs 20 ms CPU."
    ??? success "Answer"
        CPU demand = 30 k × 0.02 s = 600 cores busy. Target 50–60% utilisation for tail latency → ~1,100 cores. On 32-core instances ≈ 35 servers; add N+1 per AZ across 3 AZs (each AZ able to lose one) → ~40–45. I/O wait doesn't count toward CPU but affects concurrency (Little's law for connection pools).

??? question "Q26. A read replica lags 30 s during peak; users don't see their own edits. Fixes?"
    ??? success "Answer"
        Read-your-writes: route a user's reads to the primary for N seconds after their write (session flag/cookie), or read from a replica only if its replayed LSN ≥ the user's last write LSN (causal token). Reduce lag: fix long-running replica queries/conflicts, bigger replica instances, reduce write bursts. See [replication](replication.md).

??? question "Q27. Plan capacity for a Black Friday event that historically brings 8x normal traffic."
    ??? success "Answer"
        Load test at 10x in a prod-like environment; identify the first bottleneck (usually DB or a third party). Pre-scale (autoscaling reacts too slowly for step changes), warm caches, raise provider quotas, freeze deploys, prepare load-shedding and feature flags to turn off non-essential features (recommendations), queue-based checkout for surges, and staff a war room with dashboards tied to SLOs.

??? question "Q28. Compute the error budget for a 99.95% SLO over 30 days and how many 10-minute incidents it allows."
    ??? success "Answer"
        30 days = 43,200 min; 0.05% = 21.6 min of full downtime. So two 10-minute full outages consume ~93% of the budget. Partial outages count proportionally (e.g. 10% of requests failing for 60 min = 6 min of budget).

??? question "Q29. You need search over 50 M product listings with filters and typo tolerance. What do you use and how do you keep it in sync?"
    ??? success "Answer"
        Elasticsearch/OpenSearch (or a managed search) with BM25 + fuzzy matching, facets for filters; ~50 M docs × 2 KB ≈ 100 GB → a few shards with replicas. Sync from the source DB via CDC (Debezium → Kafka → indexer) with idempotent upserts keyed by product ID and version; periodic full reindex into a new index + alias swap for mapping changes. Accept seconds of lag. For semantic queries, add vector search in a hybrid setup.

??? question "Q30. How many WebSocket connections per server and what limits it?"
    ??? success "Answer"
        Hundreds of thousands to ~1 M idle connections on a tuned Linux box: limits are file descriptors (ulimit), memory per connection (kernel buffers + TLS state + app state ≈ 10–50 KB), ephemeral ports at proxies, and CPU for TLS handshakes during reconnect storms and for message fan-out. Practically, plan 100–250 k per node for headroom and faster draining.

??? question "Q31. Write the sequence for safely deploying a DB schema change that renames a column."
    ??? success "Answer"
        Expand/contract: (1) add the new column; (2) deploy code writing both columns; (3) backfill new column in batches; (4) deploy code reading new column (still writing both); (5) stop writing old column; (6) drop old column after a safe period. Each step is backward compatible, so any deploy can roll back. Never rename in place on a live system.

## L3 — Design & trade-offs

??? question "Q32. Cache invalidation for a product catalog read at 100 k QPS with price updates every few minutes. Design it."
    ??? success "Answer"
        Cache-aside with TTL (e.g. 5 min) as a safety net plus event-driven invalidation: price change → outbox → Kafka → invalidator deletes (not updates) cache keys, avoiding race-induced stale sets; use versioned keys or delete-after-write with a short delay to handle replica lag. Protect against stampede via request coalescing and probabilistic early refresh. Prices shown at checkout re-read from the source of truth — the cache is never authoritative for money.

??? question "Q33. Synchronous REST calls between microservices vs async events — how do you decide per interaction?"
    ??? success "Answer"
        Sync when the caller needs the answer to proceed (query, validation) and the dependency's availability is acceptable to inherit. Async events when the caller only needs to announce a fact (order placed) and consumers can act later — decouples availability and scaling but adds eventual consistency, ordering and debugging cost. Commands that must be reliable but not immediate → queue. Rule: sync for queries, async for side effects; avoid synchronous chains > 2–3 deep.

??? question "Q34. Strong vs eventual consistency for a shopping cart, inventory, and product reviews."
    ??? success "Answer"
        Cart: eventual/causal is fine, merge conflicts (union of items) — availability matters (Dynamo's motivating example). Inventory: strong for the decrement at purchase (or reservation with escrow), eventual for displayed stock levels ("only 3 left" can be approximate). Reviews: eventual; read-your-writes for the author. Pick per operation, not per system.

??? question "Q35. Single-leader, multi-leader, or leaderless replication for a global user-profile service?"
    ??? success "Answer"
        Profile writes are infrequent and per-user; users mostly write from one region. Single-leader per user (home region) with async replicas elsewhere gives simple consistency and local reads; failover moves the home. Multi-leader lets writes happen anywhere but needs conflict resolution (LWW on fields, CRDTs) — justified only if users write from multiple regions concurrently. Leaderless adds operational complexity without clear benefit here.

??? question "Q36. Kafka vs a managed queue (SQS/Service Bus) for a task-processing system with per-task retries."
    ??? success "Answer"
        Managed queue: per-message visibility timeout, retries, delay, DLQ built in; horizontal consumers with no partition planning — ideal for independent tasks. Kafka: ordered partitions, replay, high throughput, multiple consumer groups — but a failing message blocks its partition unless you build retry topics. Choose queue for tasks, Kafka for event streams; many systems use both.

??? question "Q37. Active-active multi-region vs active-passive for an e-commerce platform. Decide."
    ??? success "Answer"
        Active-passive: simpler consistency (single write region), RPO = replication lag, RTO = minutes (failover automation, DNS), wasted standby capacity. Active-active: lower latency globally and near-zero RTO, but needs conflict handling or data partitioned by home region, and doubles operational complexity. Common answer: active-active for stateless and read paths, per-user/tenant homing for writes, and strong single-region for payments/inventory. Decide by the cost of downtime vs engineering cost. See [multi-region](multi-region-dr.md).

??? question "Q38. How do you prevent a cache stampede on a hot key that expires?"
    ??? success "Answer"
        Request coalescing (single-flight: one miss fetches, others wait), locks/leases on regeneration (memcache leases), serve-stale-while-revalidate, probabilistic early expiration (XFetch), and jittered TTLs so many keys don't expire together. For extremely hot keys, local in-process caches with short TTL.

??? question "Q39. Circuit breaker vs retry vs bulkhead — how do they compose?"
    ??? success "Answer"
        Retries handle transient failures; circuit breakers stop calling a dependency that is failing persistently (fail fast, give it room to recover); bulkheads isolate resources (thread/connection pools per dependency) so one slow dependency can't exhaust everything. Compose: timeout → retry (bounded, jittered, budgeted) inside a circuit breaker, each dependency in its own bulkhead, with a fallback when the breaker is open.

??? question "Q40. gRPC vs REST vs GraphQL for (a) internal service mesh, (b) public partner API, (c) mobile app BFF."
    ??? success "Answer"
        (a) gRPC: typed contracts, HTTP/2 streaming, efficient; needs L7 LB aware of HTTP/2. (b) REST+JSON with OpenAPI: universal tooling, caching, easy for partners; version carefully. (c) GraphQL or a REST BFF: GraphQL lets clients fetch exactly what screens need, but needs query cost limits, persisted queries, and careful caching; a purpose-built BFF is simpler for a single app team.

??? question "Q41. Event sourcing for an order management system — worth it?"
    ??? success "Answer"
        Pros: full audit history, temporal queries, rebuilding projections, natural fit for event-driven integration. Cons: schema evolution of events forever, eventual consistency of read models, complexity for simple CRUD, GDPR deletion (crypto-shredding). Worth it where history is the domain (ledgers, shipments with many state changes, compliance); otherwise use CRUD + outbox events. See [architecture: CQRS & event sourcing](../architecture/cqrs-event-sourcing.md).

??? question "Q42. How do you design idempotent consumers for an at-least-once event stream?"
    ??? success "Answer"
        Dedupe by event ID in a processed-events table written in the same transaction as the side effect (or unique constraints on natural keys), make operations naturally idempotent (upsert, set-state rather than increment), use versions to ignore out-of-order older events, and bound the dedupe store by TTL aligned with max redelivery window.

??? question "Q43. Hybrid logical clocks vs vector clocks vs wall clocks for ordering events."
    ??? success "Answer"
        Wall clocks: simple, wrong under skew (LWW data loss). Vector clocks: detect concurrency precisely but grow with the number of nodes/clients. HLC: combine physical time with a logical counter — monotonic, close to wall time, capture causality within bounded skew, constant size; used by CockroachDB/YugabyteDB. Use HLC for timestamps, vector clocks where you must detect concurrent writes for merging.

??? question "Q44. Autoscaling on CPU vs queue depth vs request latency."
    ??? success "Answer"
        CPU works for CPU-bound stateless services but lags for I/O-bound ones. Queue depth (or lag) is the best signal for workers — scale to drain within SLO (desired = backlog / (per-worker rate × target drain time)). Latency is the user-facing signal but noisy and can reflect downstream problems where scaling hurts (more load on a struggling DB). Combine with scheduled scaling for known peaks and floors to avoid cold starts.

??? question "Q45. A multi-tenant API has noisy neighbours. Design isolation."
    ??? success "Answer"
        Per-tenant rate limits and concurrency limits at the gateway, weighted fair queuing in shared workers, separate pools (cells) for large tenants, per-tenant resource quotas in the DB (connection limits, statement timeouts), and cell-based architecture where tenants are assigned to independent stacks so blast radius is bounded. Measure per-tenant resource usage for chargeback and placement decisions.

??? question "Q46. Blob storage + CDN for user uploads: public URLs, signed URLs, or proxying?"
    ??? success "Answer"
        Proxying through app servers wastes bandwidth and CPU. Public URLs are fine for truly public, immutable assets (content-hashed names, long cache TTLs). Private content: signed URLs/cookies with short expiry issued after authz, CDN configured to validate signatures, so the CDN caches private objects without exposing them. Uploads via pre-signed PUT/multipart directly to storage, with async virus scanning and processing.

??? question "Q47. Choosing between Postgres, DynamoDB, and Cassandra for a new service with 20 k writes/s and simple access patterns."
    ??? success "Answer"
        Postgres: rich queries, transactions; 20 k writes/s is achievable on a large primary but near its comfort limit; scaling beyond requires sharding (Citus). DynamoDB: managed, scales writes horizontally, predictable latency, pay per use; constrained query model (design for access patterns). Cassandra: similar model, self-managed or managed, multi-region friendly; ops heavy. With simple access patterns and growth expected, DynamoDB (or Cassandra if multi-cloud/self-hosted is required); Postgres if you need relational queries and growth is bounded.

??? question "Q48. How do you roll out a risky change to a system serving 50 M users?"
    ??? success "Answer"
        Feature flags decoupling deploy from release, canary (1% → 5% → 25% → 100%) with automated analysis against SLO metrics, cell-by-cell or region-by-region rollout, dark launches/shadow traffic for backend changes, fast rollback (flag off), and a defined bake time per stage. Changes to data (migrations) follow expand/contract so rollback remains possible.

## L4 — Staff-level ambiguity

??? question "Q49. Three teams built three different event buses (Kafka, RabbitMQ, a homegrown Redis queue). Propose a convergence plan."
    ??? success "Answer"
        Inventory use cases (streaming vs task queues vs pub/sub), volumes, pain points and incidents. Define a paved road: e.g. Kafka for event streams, a managed queue for tasks — two tools, not one, because the semantics differ. Provide platform capabilities (schema registry, client libraries, observability, ACLs). Migrate by value (highest-incident system first), use bridges during transition, set a deprecation date for the homegrown queue. Write an ADR, socialise with tech leads, measure incidents and on-call load before/after.

??? question "Q50. Your monolith's database is at 80% capacity and growing 5% monthly. Leadership asks for microservices. What do you recommend?"
    ??? success "Answer"
        Separate the capacity problem (months of runway: ~4–5 months to 100%) from the architecture question. Immediate: query optimisation, read replicas, caching, archiving cold data, vertical scale — buys 12+ months. Then identify the domains driving load and extract them where boundaries are clear (strangler fig), or shard the monolith DB by tenant. Microservices are an organisational scaling tool; recommend a modular monolith first if the team count doesn't justify many services. Present options with cost, risk, timeline.

??? question "Q51. A critical system has no SLOs; every incident is a debate about severity. How do you introduce SLOs?"
    ??? success "Answer"
        Start with user journeys (checkout, search), pick SLIs measurable today (availability, latency from load balancer logs), set initial SLOs from historical performance (not aspiration), publish error budgets, and agree an error-budget policy with product (e.g. budget exhausted → reliability work prioritised). Iterate quarterly. Win buy-in by using SLOs to reduce pager noise (burn-rate alerts replace threshold alerts).

??? question "Q52. You're asked to cut cloud spend 30% in two quarters without hurting reliability. Approach?"
    ??? success "Answer"
        Attribute costs (tagging, per-team showback). Quick wins: rightsizing, idle resources, storage tiering, reserved/savings plans, spot for batch. Architectural: cache to reduce DB size, reduce cross-AZ/egress traffic, observability data retention, move chatty services together. Guardrails: SLO dashboards reviewed with every change. Organisational: cost as a non-functional requirement in design reviews, per-team budgets. Report monthly with realised savings.

??? question "Q53. A new VP wants to move everything to multi-region active-active within a year. How do you respond?"
    ??? success "Answer"
        Clarify the driver (regulatory, latency, availability target, customer contracts). Quantify: current availability and RTO/RPO, cost of downtime vs 1.5–2x infra and significant engineering cost. Propose tiering: tier-0 services (checkout, auth) get active-active or fast failover; others get backup region with RTO hours. Show a roadmap with milestones (DR drills first, data replication, stateless services, then stateful). Disagree-and-commit style: present data, align on outcomes rather than a technology mandate.

??? question "Q54. Two senior engineers disagree strongly: one wants event sourcing for the new logistics tracking platform, the other CRUD + CDC. How do you resolve it?"
    ??? success "Answer"
        Make the decision criteria explicit (audit needs, query patterns, team experience, time to market, reversibility). Timebox a spike of the riskiest part of each approach, write an ADR with both options' consequences, and seek the smallest reversible decision (e.g. append-only shipment events table + CRUD projections without full event-sourcing framework). Decide, document dissent, and set a review point. The goal is a good decision and preserved relationships.

??? question "Q55. Your platform team's internal API gateway is a single point of failure for 200 services. Plan to de-risk."
    ??? success "Answer"
        Short term: redundancy across AZs, capacity headroom, config change safety (validation, canary, fast rollback — most gateway outages are bad configs). Medium: cell-based deployment (gateway instances per cell/domain so a failure affects a subset), static fallback routes, remove non-essential plugins from the hot path. Long: move east-west traffic off the gateway to a service mesh or direct calls with shared libraries. Track gateway-caused incidents and blast radius.

??? question "Q56. A product team wants to store all customer events forever 'for AI later'. Respond."
    ??? success "Answer"
        Balance optionality with cost and compliance: GDPR/retention obligations, PII minimisation, and storage/processing costs. Propose a data strategy: define candidate use cases, keep raw events in cheap object storage with a table format (Iceberg/Delta) and a retention policy by data class, pseudonymise identifiers, document consent basis, and review annually. Store what you can justify, and make deletion possible (crypto-shredding).

??? question "Q57. Leadership asks whether to adopt a vendor's managed agent platform or build on open-source frameworks. How do you frame the decision?"
    ??? success "Answer"
        Frame with criteria: time to value, control over data/residency, integration with identity and existing systems, evaluation/observability support, lock-in and exit cost, pricing at projected scale, team skills. Separate layers: model access (use a gateway for portability), orchestration (framework vs managed), tools (MCP for portability), data. Recommend a thin internal platform with open protocols, and use managed components where they are commodity. Pilot with one use case, measure, revisit in 6 months.

??? question "Q58. After a major outage, an exec asks 'who is responsible?'. How do you lead the postmortem?"
    ??? success "Answer"
        Reframe to systems thinking: blameless postmortem focused on contributing factors (missing safeguards, alerting gaps, unclear ownership, risky processes) not individuals. Produce a timeline, impact, root causes, and prioritised actions with owners and dates; distinguish quick fixes from systemic ones. Communicate to the exec in business terms (impact, what changes, how recurrence risk falls), and follow up on action completion.

??? question "Q59. You own a platform used by 40 teams. A proposed breaking API change would save the platform team 3 months but cost each consumer team 1 week. Decide."
    ??? success "Answer"
        Consumer cost is 40 team-weeks ≈ 10 months > 3 months saved — globally negative unless the change unlocks significant future value. Options: provide a compatibility layer, automated codemods, or migrate consumers yourselves; version the API and support both for a deprecation window. Make the trade-off visible to leadership with numbers; this is the classic local vs global optimisation Staff engineers must surface.

??? question "Q60. You are designing the architecture for a new logistics visibility product with unclear requirements. How do you avoid both over- and under-engineering?"
    ??? success "Answer"
        Identify the few decisions that are expensive to reverse (data model for shipments/events, tenant isolation, identity, event backbone) and invest there; keep everything else simple and replaceable (modular monolith, managed services). Define fitness functions (latency, cost per shipment tracked), build a thin vertical slice with a design partner customer, and write ADRs with explicit review triggers (e.g. "revisit when > 1 M events/day").

??? question "Q61. How would you evaluate whether your organisation's system design interviews predict on-the-job success?"
    ??? success "Answer"
        Define on-the-job signals (design doc quality, incident performance, peer feedback at 12 months), correlate with interview scores (acknowledge small samples and survivorship bias), check inter-rater reliability via calibration sessions and paired interviews, review rubric for bias toward memorised patterns vs reasoning, and pilot changes (e.g. realistic scenarios from your domain). This is a Staff-level influence task spanning engineering and recruiting.

??? question "Q62. A team's service meets its SLO but users still complain about slowness. What's going on and what do you do?"
    ??? success "Answer"
        The SLI measures the wrong thing: server-side latency vs end-to-end (client, network, CDN), average vs tail, or only one endpoint of a multi-call journey; or the SLO is too loose. Add real user monitoring and journey-level SLIs, measure p99 at the client, and revisit targets with product. SLOs must reflect user happiness, not what's easy to measure.

## Use-case scenarios

Each scenario gives inputs, scale and constraints and asks for a decision. Aim for a 3–5 minute spoken answer with a clear recommendation.

??? question "S1. Container tracking events: 40 carriers push 25 M EDI/API milestone events/day (bursty, 10x after vessel arrival). Customers query shipment status (5 k QPS) and subscribe to webhooks. Design the ingestion and serving path."
    ??? success "Answer"
        Ingestion: carrier adapters normalise EDI/API into a canonical event schema → Kafka (partitioned by container/shipment ID for ordering) → idempotent processor (dedupe by carrier event ID, handle out-of-order milestones with event time, not arrival time) → shipment state store (Postgres/DynamoDB) + event history (append-only). Serving: status reads from a cache-fronted read model (5 k QPS trivial). Webhooks via the [notification pattern](case-studies/notification-system.md): per-customer queues, retries with backoff, signatures. Bursts absorbed by Kafka; autoscale consumers on lag. Decision: event-driven with CQRS read models; keep raw events for reprocessing when mapping bugs are found.

??? question "S2. A B2B SaaS with 3 k tenants must offer EU data residency within 6 months. Currently single US region, shared Postgres. Decide the approach."
    ??? success "Answer"
        Deploy an EU cell (full stack: app, DB, storage, logs) and route EU tenants by tenant directory at the edge; migrate EU tenants tenant-by-tenant (logical replication/export-import with a short write freeze). Global services (billing, auth) must avoid storing EU personal data or get EU instances. Also audit sub-processors, logs, backups, analytics pipelines — residency violations often hide there. Cells are also a blast-radius win. Decision: cell-based regional deployment with tenant routing, not active-active replication.

??? question "S3. An internal RAG assistant serves 20 k employees; p95 latency is 9 s and cost is $60 k/month. Leadership wants < 4 s and half the cost. What do you change?"
    ??? success "Answer"
        Profile the pipeline: retrieval, reranking, LLM time-to-first-token, output length. Latency: stream responses, parallelise retrieval, smaller reranker, cap context size, semantic cache for frequent questions. Cost: route easy queries to a smaller model, prompt caching for system prompts, shorter outputs, fewer retrieved chunks via better reranking. Validate with an eval set so quality doesn't regress. Decision: routing + caching + context trimming, gated by evals. (See the AI system design track.)

??? question "S4. Flash sale: 1 M users will attempt to buy 10 k units at 12:00. Design to avoid overselling and meltdown."
    ??? success "Answer"
        Virtual waiting room at the edge (admit users at a controlled rate with signed tokens), inventory as pre-allocated tokens in Redis (atomic DECR/Lua; reservation with TTL, e.g. 10 min to pay), orders written asynchronously via a queue, payment with idempotency keys, and reservation expiry returning stock. Static pages cached at CDN; all non-essential features off. Decision: admission control + atomic reservation, never letting 1 M users hit the DB.

??? question "S5. A fintech needs audit logs for every admin action, immutable for 7 years, queryable by auditors in minutes. 50 M events/month."
    ??? success "Answer"
        Append-only pipeline: services emit audit events via outbox → Kafka → writer to object storage with object lock (WORM, compliance mode) in Parquet partitioned by date/tenant, plus a hash chain or periodic Merkle root anchored externally for tamper evidence. Queries via a query engine (Athena/Trino/DuckDB) over the table format; recent 90 days also in a search index for fast investigations. 50 M/month × 1 KB = 50 GB/month — small. Decision: WORM object storage + table format + hash chain.

??? question "S6. Your API has a public free tier abused by scrapers: 70% of 300 k req/s is bot traffic. Design mitigation without hurting paying customers."
    ??? success "Answer"
        Tiered identity: require API keys (even free), per-key and per-IP/ASN token buckets at the edge, stricter limits and quotas for free tier, bot detection (behavioural signals, TLS fingerprints) at the CDN/WAF, cache public responses at the edge, separate capacity pools for paid tenants so bots can't exhaust them. Monitor false positives on paid customers as a guardrail metric. Decision: edge rate limiting with tiered quotas + paid-tier isolation.

??? question "S7. A 12-year-old monolith (Java, Oracle) processes bookings for 400 enterprise customers. Management wants 'cloud-native' in 18 months with no big-bang. Plan."
    ??? success "Answer"
        Strangler fig: put a routing facade in front; identify seams via domain analysis (event storming) and change frequency; extract first a domain with high change rate and low coupling (e.g. notifications, document generation); use CDC from Oracle to feed new services' read models; keep Oracle as system of record for core booking until late. Lift-and-shift the monolith to the cloud early for infra benefits. Measure deployment frequency and lead time. Decision: incremental extraction with CDC, not a rewrite.

??? question "S8. 500 IoT reefer containers per vessel send temperature every minute over expensive satellite links; alerts must trigger within 5 min of out-of-range temperatures. Design."
    ??? success "Answer"
        Edge processing on the vessel gateway: aggregate and compress readings, send only deltas/threshold breaches immediately and summaries in batches; store-and-forward during connectivity loss. Shore side: MQTT/HTTPS ingestion → stream processing (windowed rules per container/cargo profile) → alerting via notification platform; time-series store for history. Handle out-of-order and late data by event time. Decision: edge filtering + event-time stream processing; cost driven by satellite bytes.

??? question "S9. Search latency spiked from 80 ms to 900 ms after catalogue grew from 5 M to 60 M docs. Elasticsearch cluster: 3 nodes, 1 index, 5 shards."
    ??? success "Answer"
        Shards are now ~12 M docs each and likely exceed memory for hot data; heap pressure and GC. Actions: reindex into more shards (target 10–50 GB per shard) across more nodes, review mappings (disable unnecessary fields, keyword vs text), filter context caching, avoid deep pagination and expensive aggregations, separate hot/warm data. Use an alias swap for zero-downtime reindex. Decision: scale out with a reshard + query optimisation, measured with load tests.

??? question "S10. A product needs 'collaborative editing' of shipment documents by up to 20 users at once. Decide between locking, OT, and CRDTs."
    ??? success "Answer"
        Pessimistic locking per field/section: simplest, fine if edits rarely collide and documents are structured forms. OT: server-centric, proven (Google Docs), complex to implement. CRDTs (Yjs/Automerge): offline-friendly, peer merges, good libraries now; metadata overhead. For structured shipping documents with sections, section-level locks or field-level LWW with presence indicators may suffice; for free-text rich editing, use a CRDT library with a sync server. Decision driven by document structure and offline needs.

??? question "S11. Your company runs 300 microservices; a single request touches 25 services and p99 latency is 2.5 s. Diagnose and reduce."
    ??? success "Answer"
        Distributed tracing to find the critical path and fan-out; common culprits: sequential calls that could be parallel, N+1 calls, chatty services that should be merged, missing caches, retries amplifying latency, tail latency compounding (p99 of 25 hops). Fixes: aggregate APIs/BFF, parallelise, hedged requests for idempotent reads, caches, and consolidate overly fine-grained services. Decision: trace-driven critical-path optimisation plus selective service consolidation.

??? question "S12. A partner requires exactly-once delivery of invoices over webhooks. Your system is at-least-once. What do you offer?"
    ??? success "Answer"
        Explain the impossibility over unreliable networks; offer effectively-once: each webhook carries a stable event ID and sequence per invoice, retries until acked, partner dedupes by ID (document it, provide SDK helpers), plus a reconciliation API (list invoices since cursor) so the partner can verify completeness. Signed payloads and replay protection via timestamp. Decision: at-least-once + idempotency contract + reconciliation endpoint.

??? question "S13. A mobile app with 30 M users needs offline-first support for field agents recording inspections; sync conflicts are common."
    ??? success "Answer"
        Local database on device (SQLite), operation log with client IDs and HLC timestamps, sync protocol with per-entity versions; conflict policy per field type (LWW for simple fields, merge for lists, manual resolution for critical ones). Server stores canonical state and change feed; clients pull changes since cursor. Attachments uploaded separately with resumable uploads. Decision: op-log sync with typed conflict policies; consider CRDTs for collaborative fields.

??? question "S14. You must build a pricing engine that recomputes 200 M freight rates nightly from tariffs, surcharges, and FX, and serves quotes at 2 k QPS with p99 < 100 ms."
    ??? success "Answer"
        Split batch precompute from online serving: nightly distributed job (Spark/Beam) computes base rates into a KV store keyed by lane/equipment/date; online quote service reads base rates + applies dynamic components (FX, spot surcharges) cached in memory; versioned rate tables for auditability and rollback. Validation checks before publishing a new version (diff vs previous, bounds). Decision: batch + KV serving with versioned snapshots.

??? question "S15. A startup's single Postgres (2 TB) handles OLTP and analytics dashboards; dashboards slow down checkout. Fix within a sprint."
    ??? success "Answer"
        Immediately move dashboards to a read replica with statement timeouts, add connection pools per workload. Next: CDC or scheduled exports into a warehouse/OLAP (BigQuery, Snowflake, ClickHouse, or DuckDB over Parquet for small teams) for analytics. Decision: workload isolation now (replica), analytical store next quarter.

??? question "S16. An AI agent platform lets agents call internal tools; one agent looped and made 400 k API calls in an hour. Design controls."
    ??? success "Answer"
        Per-agent and per-run budgets (tool calls, tokens, wall time, cost), rate limits at the tool gateway keyed by agent identity, loop detection (repeated identical calls), circuit breakers per tool, human approval for high-impact tools, and kill switches. Observability: traces per run with tool-call spans. Decision: a tool gateway enforcing identity, budgets and policies — the same multi-tenant rate-limiting patterns, applied to agents.

## Rapid-fire (spaced review)

One-liners: answer in one breath, then check.

??? question "RF1. Latency: L1 cache vs main memory vs same-DC round trip vs cross-continent round trip?"
    ??? success "Answer"
        ~1 ns, ~100 ns, ~0.5 ms, ~150 ms.

??? question "RF2. Seconds in a day (for QPS math)?"
    ??? success "Answer"
        86,400 ≈ 10^5 — so 1 M/day ≈ 12 /s.

??? question "RF3. 99.99% availability = how much downtime per year?"
    ??? success "Answer"
        ~52.6 minutes (99.9% ≈ 8.8 h; 99.999% ≈ 5.3 min).

??? question "RF4. Base62 with 7 characters gives how many IDs?"
    ??? success "Answer"
        62^7 ≈ 3.5 trillion.

??? question "RF5. Default max Kafka ordering guarantee?"
    ??? success "Answer"
        Order is guaranteed only within a partition.

??? question "RF6. What does `SKIP LOCKED` do?"
    ??? success "Answer"
        Skips rows locked by other transactions, so concurrent workers claim disjoint rows without blocking.

??? question "RF7. Primary cause of Redis latency spikes?"
    ??? success "Answer"
        Slow O(N) commands or big keys blocking the single-threaded event loop (and fork for persistence).

??? question "RF8. Little's law?"
    ??? success "Answer"
        L = λ × W (concurrency = arrival rate × time in system).

??? question "RF9. HyperLogLog is used for?"
    ??? success "Answer"
        Approximate distinct counts with ~12 KB per counter and ~1% error.

??? question "RF10. Bloom filter false positives or false negatives?"
    ??? success "Answer"
        False positives only; never false negatives.

??? question "RF11. What is a hot partition?"
    ??? success "Answer"
        A shard receiving disproportionate load due to skewed keys; fix with better keys, splitting, or salting.

??? question "RF12. 301 vs 302?"
    ??? success "Answer"
        301 permanent (browser caches it); 302 temporary (each request returns to the server).

??? question "RF13. What does a CDN's `s-maxage` control?"
    ??? success "Answer"
        TTL in shared caches (CDN/proxies), overriding `max-age` for them.

??? question "RF14. Why jitter in backoff?"
    ??? success "Answer"
        To desynchronise clients and avoid retry thundering herds.

??? question "RF15. Leader lease purpose?"
    ??? success "Answer"
        Lets a leader serve linearizable reads locally for the lease duration without a quorum round trip.

??? question "RF16. Raft needs how many nodes to tolerate 2 failures?"
    ??? success "Answer"
        5 (2f + 1).

??? question "RF17. What is read repair?"
    ??? success "Answer"
        On read, the coordinator updates stale replicas it detected with the newest version.

??? question "RF18. What is tail-based sampling?"
    ??? success "Answer"
        Deciding to keep a trace after it completes (e.g. keep errors/slow ones), rather than at the start.

??? question "RF19. What is a dead letter queue?"
    ??? success "Answer"
        Where messages go after exceeding retry attempts, for inspection and replay.

??? question "RF20. Geohash neighbour problem?"
    ??? success "Answer"
        Nearby points can have different prefixes at cell edges — query the 8 neighbours too.

??? question "RF21. Write amplification in LSM trees comes from?"
    ??? success "Answer"
        Compaction rewriting data multiple times across levels.

??? question "RF22. Snowflake ID layout?"
    ??? success "Answer"
        41-bit timestamp (ms) + 10-bit machine ID + 12-bit sequence (+1 sign bit).

??? question "RF23. What is head-of-line blocking?"
    ??? success "Answer"
        One slow item blocks all items queued behind it on the same connection/partition/queue.

??? question "RF24. Strong reason for cell-based architecture?"
    ??? success "Answer"
        Bounded blast radius — a failure or bad deploy affects only one cell's customers.

??? question "RF25. CDC stands for, and a common tool?"
    ??? success "Answer"
        Change data capture; Debezium reading the DB's WAL/binlog.

??? question "RF26. Burn rate of 14.4 on a 30-day SLO means?"
    ??? success "Answer"
        Consuming budget 14.4x faster than allowed — 2% of the monthly budget per hour; page-worthy.

??? question "RF27. When is 2PC acceptable?"
    ??? success "Answer"
        Within a single database/tightly coupled system with a reliable coordinator; avoid across services (blocking, availability).

??? question "RF28. What does idempotent PUT mean?"
    ??? success "Answer"
        Repeating the same request yields the same state as doing it once.

??? question "RF29. Pre-signed URL?"
    ??? success "Answer"
        A time-limited URL granting direct access to an object in blob storage without proxying via your servers.

??? question "RF30. First question in any system design interview?"
    ??? success "Answer"
        Clarify requirements and scale — who uses it, for what, how much, and which non-functional requirements matter most.
