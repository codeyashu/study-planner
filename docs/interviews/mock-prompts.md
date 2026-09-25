---
title: Mock prompt bank
tags: [interviews, system-design, ai-system-design, behavioral]
last_reviewed: 2026-09-25
---

# Mock prompt bank

!!! abstract "How to use"
    105 prompts: **40 system design**, **25 AI system design**, **15 low-level design**, **25 behavioral/Staff**. Each is tagged with difficulty and links to prep pages where they exist.
    **Difficulty:** :material-circle-outline: **M** = Senior-bar standard · :material-circle-half-full: **H** = Senior-hard / Staff standard · :material-circle: **XH** = Staff/Principal (ambiguous, multi-team, migration or deep distributed theory).
    **Staff twist:** for any prompt, add one of: *"How would you roll this out across 100 teams?"*, *"Cut the cost by 50%"*, *"Now make it multi-region active-active"*, *"You have 2 engineers and 3 months — what do you build first?"*
    Use them with a peer, a paid mock, or the [AI mock interviewer](ai-mock-interviewer.md); score with the [rubric](rubric.md).

## System design (40)

### Classic web-scale

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| SD1 | URL shortener with custom aliases, expiry and near-real-time click analytics | M | hashing, KV, analytics | [case study](../tracks/system-design/case-studies/url-shortener.md) |
| SD2 | Pastebin with 10 GB/day uploads and expiring pastes | M | blob storage, TTL | [storage and CDN](../tracks/system-design/storage-cdn.md) |
| SD3 | News feed / timeline for 300M DAU | H | fan-out, ranking, caching | [case study](../tracks/system-design/case-studies/news-feed.md) |
| SD4 | Chat system (1:1 + groups up to 500, presence, read receipts) | H | websockets, ordering | [case study](../tracks/system-design/case-studies/chat-system.md) |
| SD5 | Notification system (push/email/SMS, 1B/day, preferences) | M | queues, retries, dedupe | [case study](../tracks/system-design/case-studies/notification-system.md) |
| SD6 | Typeahead / search autocomplete for 50k QPS | M | tries, caching | [search systems](../tracks/system-design/search-systems.md) |
| SD7 | Web crawler for 1B pages/month with politeness | H | frontier, dedupe, scheduling | [data pipelines](../tracks/system-design/data-pipelines.md) |
| SD8 | Video upload and streaming platform (YouTube-lite) | H | transcoding, CDN, adaptive bitrate | [storage and CDN](../tracks/system-design/storage-cdn.md) |
| SD9 | Photo sharing with feed and likes (Instagram-lite) | M | blob, feed, counters | [caching](../tracks/system-design/caching.md) |
| SD10 | Google Docs-style collaborative editor | XH | OT/CRDT, presence, consistency | [consistency models](../tracks/system-design/consistency-models.md) |

### Infrastructure and platform

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| SD11 | Distributed rate limiter across 3 regions for 2,000 services | H | token bucket, consistency | [rate limiting](../tracks/system-design/rate-limiting.md) |
| SD12 | Distributed key-value store with tunable consistency | XH | replication, quorums, gossip | [case study](../tracks/system-design/case-studies/distributed-kv-store.md) |
| SD13 | Distributed job scheduler (cron at scale, exactly-once execution semantics) | H | leases, idempotency | [case study](../tracks/system-design/case-studies/job-scheduler.md) |
| SD14 | Metrics and monitoring system (1M series/s ingest, 13-month retention) | H | TSDB, downsampling | [case study](../tracks/system-design/case-studies/metrics-monitoring.md) |
| SD15 | Distributed message queue / Kafka-lite | XH | log, partitions, ISR | [messaging and streaming](../tracks/system-design/messaging-streaming.md) |
| SD16 | Distributed cache (Redis-cluster-like) with hot-key handling | H | consistent hashing, eviction | [partitioning](../tracks/system-design/partitioning-sharding.md) |
| SD17 | Centralised logging platform for 5 TB/day | H | ingestion, indexing, tiering | [observability and SLOs](../tracks/system-design/observability-slos.md) |
| SD18 | Feature flag / config service with < 1 s propagation | M | push vs pull, consistency | [reliability patterns](../tracks/system-design/reliability-patterns.md) |
| SD19 | API gateway for a microservices estate (auth, routing, quotas) | H | proxies, authN/Z | [load balancing](../tracks/system-design/load-balancing.md) |
| SD20 | Distributed lock service (Chubby/ZooKeeper-like) | XH | consensus, fencing tokens | [consensus and Raft](../tracks/system-design/consensus-raft.md) |
| SD21 | Blob storage service (S3-lite) with erasure coding | XH | durability, metadata | [storage and CDN](../tracks/system-design/storage-cdn.md) |
| SD22 | Unique ID generator (Snowflake-like) for 1M IDs/s | M | clocks, coordination-free | [scalability fundamentals](../tracks/system-design/scalability-fundamentals.md) |
| SD23 | Multi-region active-active user-profile service with DR (RPO 0, RTO 5 min) | XH | replication, failover | [multi-region and DR](../tracks/system-design/multi-region-dr.md) |
| SD24 | Change-data-capture pipeline from 200 Postgres DBs to a lakehouse | H | CDC, schemas, ordering | [data pipelines](../tracks/system-design/data-pipelines.md) |

### Transactions, money and marketplaces

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| SD25 | Payment system for a marketplace with multiple PSPs, ledger, reconciliation | XH | idempotency, double-entry | [case study](../tracks/system-design/case-studies/payment-system.md) |
| SD26 | Ride hailing / proximity matching (Uber-lite) | H | geo-index, matching | [case study](../tracks/system-design/case-studies/ride-hailing-proximity.md) |
| SD27 | Ticket booking (concerts) with 1M users at on-sale | H | contention, queues, holds | [consistency models](../tracks/system-design/consistency-models.md) |
| SD28 | Hotel/flight reservation system with overbooking rules | H | inventory, sagas | [sagas and outbox](../tracks/architecture/sagas-outbox.md) |
| SD29 | E-commerce order management (cart → order → fulfilment) | M | sagas, events | [messaging and streaming](../tracks/system-design/messaging-streaming.md) |
| SD30 | Digital wallet with P2P transfers and fraud checks | XH | ledger, consistency, risk | [payment system](../tracks/system-design/case-studies/payment-system.md) |
| SD31 | Stock exchange order matching engine (low latency) | XH | single-writer, sequencing | [reliability patterns](../tracks/system-design/reliability-patterns.md) |
| SD32 | Ad click aggregation with exactly-once counts for billing | H | stream processing, dedupe | [data pipelines](../tracks/system-design/data-pipelines.md) |

### Domain / enterprise (logistics flavoured)

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| SD33 | Real-time container/shipment tracking for 10M active shipments with ETA updates | H | events, geo, fan-out | [messaging and streaming](../tracks/system-design/messaging-streaming.md) |
| SD34 | Global booking platform for a shipping line (capacity, pricing, allocations) | XH | inventory, consistency, multi-region | [data architecture](../tracks/architecture/data-architecture.md) |
| SD35 | Event-driven integration hub between 300 partner systems (EDI, APIs, files) | H | integration patterns, schemas | [integration patterns](../tracks/architecture/integration-patterns.md) |
| SD36 | Multi-tenant SaaS platform with tenant isolation and noisy-neighbour control | H | tenancy, quotas | [security and multi-tenancy](../tracks/system-design/security-authn-authz.md) |
| SD37 | Document management with search, versioning and retention for regulated data | M | storage, search, compliance | [search systems](../tracks/system-design/search-systems.md) |

### Staff / Principal (ambiguous, organisational)

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| SD38 | Migrate a 15-year-old monolith (order management) to services without downtime; 12 teams involved | XH | strangler fig, data migration | [legacy modernization](../tracks/architecture/legacy-modernization.md) |
| SD39 | Company has 3 incompatible event platforms after acquisitions; design the convergence | XH | platform strategy, migration | [team topologies](../tracks/architecture/team-topologies.md) |
| SD40 | Define API standards and versioning for 400 internal APIs; how do you enforce without blocking teams? | XH | governance, contracts | [API contracts and versioning](../tracks/architecture/api-contracts-versioning.md) |

## AI system design (25)

### RAG and search

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| AI1 | Enterprise RAG assistant over 2M documents with document-level ACLs and citations | H | hybrid retrieval, ACL, evals | [rag system](../tracks/ai-system-design/rag-system.md) |
| AI2 | Semantic product search for an e-commerce catalogue of 50M items | H | embeddings, hybrid, ranking | [AI search](../tracks/ai-system-design/ai-search.md) |
| AI3 | Customer-support RAG bot that must never give wrong policy answers | M | grounding, refusal, HITL | [rag system](../tracks/ai-system-design/rag-system.md) |
| AI4 | Multi-tenant RAG platform offered to 500 B2B customers | XH | isolation, cost, noisy neighbour | [advanced RAG](../tracks/agentic-ai/advanced-rag.md) |
| AI5 | Q&A over contracts requiring multi-hop reasoning ("which customers are affected if port X closes?") | XH | GraphRAG, structured + unstructured | [advanced RAG](../tracks/agentic-ai/advanced-rag.md) |

### Assistants and agents

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| AI6 | ChatGPT-style assistant for 10M users: conversations, memory, file uploads | H | streaming, memory, safety | [chat assistant](../tracks/ai-system-design/chat-assistant.md) |
| AI7 | Multi-agent platform for 50 internal teams calling internal APIs | XH | tool registry, identity, HITL | [agent platform](../tracks/ai-system-design/agent-platform.md) |
| AI8 | Operations copilot that triages exceptions and takes approved actions (capstone) | XH | orchestration, evals, guardrails | [capstone](../projects/capstone.md) |
| AI9 | Coding agent / automated code-review bot for 2,000 repositories | H | sandboxing, context, evals | [coding agent](../tracks/ai-system-design/coding-agent.md) |
| AI10 | Email/inbox agent that drafts and sends replies on a user's behalf | H | lethal trifecta, approvals | [guardrails and security](../tracks/agentic-ai/guardrails-security.md) |
| AI11 | Voice agent for a call centre (sub-second turn latency) | XH | streaming ASR/TTS, latency budget | [cost and latency](../tracks/agentic-ai/cost-latency-optimization.md) |
| AI12 | Deep-research agent that produces cited reports in 10 minutes | H | planning, parallel tools, verification | [multi-agent systems](../tracks/agentic-ai/multi-agent-systems.md) |
| AI13 | Agent memory service shared across products (preferences, facts, episodes) | H | memory, privacy, provenance | [memory systems](../tracks/agentic-ai/memory-systems.md) |
| AI14 | Long-running procurement agent that waits days for approvals and supplier replies | H | durable execution, HITL | [durable execution](../tracks/agentic-ai/durable-execution-hitl.md) |

### Platform, gateway, evaluation

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| AI15 | Multi-tenant LLM gateway for 40 teams and 5 providers with budgets and chargeback | H | routing, quotas, observability | [LLM gateway](../tracks/ai-system-design/llm-gateway.md) |
| AI16 | LLM evaluation and observability platform for the whole company | XH | offline/online evals, judges, tracing | [evaluation platform](../tracks/ai-system-design/evaluation-platform.md) |
| AI17 | Prompt management and experimentation platform (versioning, A/B, rollback) | M | config, experimentation | [LLM observability](../tracks/agentic-ai/llm-observability.md) |
| AI18 | Guardrails service used by every AI product (input/output/tool policies) | H | classifiers, latency, policy | [guardrails and security](../tracks/agentic-ai/guardrails-security.md) |
| AI19 | MCP server registry and gateway for an enterprise (discovery, auth, audit) | XH | MCP, OAuth, governance | [MCP](../tracks/agentic-ai/mcp.md) |

### Serving, documents, cost

| # | Prompt | Diff | Tags | Prep |
|---|---|---|---|---|
| AI20 | LLM inference platform for 3 open-weight models at 5k req/min | XH | GPUs, batching, autoscaling | [LLM serving platform](../tracks/ai-system-design/llm-serving-platform.md) |
| AI21 | Intelligent document processing for 1M trade documents/month | H | OCR, extraction, HITL review | [document processing](../tracks/ai-system-design/document-processing.md) |
| AI22 | Cut LLM spend of an existing product by 60% without quality loss | H | routing, caching, distillation | [capacity and cost planning](../tracks/ai-system-design/capacity-cost-planning.md) |
| AI23 | Fine-tuning platform for internal teams (data, training, eval, deploy) | XH | LoRA, eval gates, registry | [fine-tuning](../tracks/agentic-ai/fine-tuning.md) |
| AI24 | Recommendation system for a marketplace home feed (classic ML + LLM features) | H | two-tower, ranking, features | [recsys basics](../tracks/ai-system-design/recsys-ml-basics.md) |
| AI25 | Your company wants "AI in every product" in 12 months: design the shared platform and operating model | XH | strategy, platform, governance | [AI-native architecture](../tracks/architecture/ai-native-architecture.md) |

## Low-level design (15)

| # | Prompt | Diff | Focus | Prep |
|---|---|---|---|---|
| LLD1 | Parking lot (spots by size, tickets, pricing) + change request: EV charging with reservations | M | modelling, strategy pattern | [design patterns](../tracks/architecture/design-patterns.md) |
| LLD2 | LRU cache with TTL, thread-safe | M | data structures, locking | [concurrency and LLD](../tracks/dsa/concurrency-lld.md) |
| LLD3 | Rate limiter library (token bucket, sliding window) pluggable per key | M | strategy, concurrency | [rate limiting](../tracks/system-design/rate-limiting.md) |
| LLD4 | Elevator control system for a 40-floor building with 6 elevators | H | state machines, scheduling | [design patterns](../tracks/architecture/design-patterns.md) |
| LLD5 | In-memory pub/sub message broker with topics, consumer groups, at-least-once | H | concurrency, queues | [concurrency and LLD](../tracks/dsa/concurrency-lld.md) |
| LLD6 | Splitwise-style expense sharing with debt simplification | M | modelling, graph | [SOLID and refactoring](../tracks/architecture/solid-refactoring.md) |
| LLD7 | Library management / book lending system | M | modelling, invariants | [DDD tactical](../tracks/architecture/ddd-tactical.md) |
| LLD8 | Shipment lifecycle state machine with guards, side effects and audit | H | state pattern, events | [DDD tactical](../tracks/architecture/ddd-tactical.md) |
| LLD9 | Thread pool / bounded executor with graceful shutdown | H | concurrency primitives | [concurrency models](../tracks/python/concurrency-models.md) |
| LLD10 | Job scheduler (cron expressions, retries, priorities) in-process | H | heaps, time, concurrency | [heap](../tracks/dsa/heap.md) |
| LLD11 | Logging framework with levels, appenders, async flushing | M | chain of responsibility, observer | [design patterns](../tracks/architecture/design-patterns.md) |
| LLD12 | Chess or tic-tac-toe game engine with undo | M | command pattern, validation | [design patterns](../tracks/architecture/design-patterns.md) |
| LLD13 | Tool-calling agent runtime: tool registry, schema validation, retries, budgets | H | interfaces, typing | [tool calling](../tracks/agentic-ai/tool-calling.md) |
| LLD14 | Circuit breaker + retry with backoff library | H | state machine, concurrency | [reliability patterns](../tracks/system-design/reliability-patterns.md) |
| LLD15 | Vending machine / payment kiosk with multiple payment methods | M | state pattern | [design patterns](../tracks/architecture/design-patterns.md) |

## Behavioral / Staff (25)

Prep: [behavioral interviews](../tracks/staff-skills/behavioral-interviews.md). Answer in STAR(L): Situation (< 45 s), Task, Actions (with "I"), Result (numbers), Learning.

### Scope and impact

| # | Prompt | Diff | Signal tested | Related |
|---|---|---|---|---|
| B1 | Tell me about your highest-impact work in the last 3 years. | H | scope, impact | [Staff archetypes](../tracks/staff-skills/staff-archetypes.md) |
| B2 | Describe the most technically complex project you led end-to-end. | M | technical depth, ownership | |
| B3 | Tell me about a technical strategy or vision you created for multiple teams. | XH | strategy, alignment | [technical strategy](../tracks/staff-skills/technical-strategy.md) |
| B4 | Tell me about a time you identified a problem nobody had asked you to solve. | H | ownership, ambiguity | |
| B5 | Describe a time you reduced cost, latency or incidents significantly. How did you measure it? | M | impact, data | |

### Influence and conflict

| # | Prompt | Diff | Signal tested | Related |
|---|---|---|---|---|
| B6 | Tell me about a conflict with a peer or another team over a technical decision. | M | conflict, collaboration | [influence without authority](../tracks/staff-skills/influence-without-authority.md) |
| B7 | Tell me about a time you influenced a decision outside your team without authority. | H | influence | [influence without authority](../tracks/staff-skills/influence-without-authority.md) |
| B8 | Tell me about a time you disagreed with your manager or a senior leader. | H | courage, judgement | [communication](../tracks/staff-skills/communication-stakeholders.md) |
| B9 | Describe a time you had to get several teams to adopt a standard or platform. | XH | coalition-building | [architecture reviews](../tracks/staff-skills/architecture-reviews.md) |
| B10 | Tell me about a decision you made that was unpopular. | H | conviction, empathy | [decision making](../tracks/staff-skills/decision-making.md) |

### Ambiguity, judgement and failure

| # | Prompt | Diff | Signal tested | Related |
|---|---|---|---|---|
| B11 | Tell me about a project that failed or missed its goals. | M | self-awareness | |
| B12 | Tell me about a time you were wrong about a technical decision. | H | humility, learning | |
| B13 | Tell me about a time you made a decision with incomplete data. | H | judgement, reversibility | [decision making](../tracks/staff-skills/decision-making.md) |
| B14 | Tell me about a time you killed or significantly changed a project. | XH | prioritisation | |
| B15 | How did you handle significant technical debt competing with feature work? | H | trade-offs, business framing | [technical debt](../tracks/staff-skills/technical-debt.md) |
| B16 | Describe a time you balanced speed against quality under a hard deadline. | M | pragmatism | |

### Growing others and org health

| # | Prompt | Diff | Signal tested | Related |
|---|---|---|---|---|
| B17 | Tell me about someone you mentored or sponsored into a bigger role. | H | growing others | [mentoring and sponsorship](../tracks/staff-skills/mentoring-sponsorship.md) |
| B18 | How have you raised the engineering bar beyond your own team? | XH | mechanisms | [architecture reviews](../tracks/staff-skills/architecture-reviews.md) |
| B19 | Tell me about a time you gave difficult feedback to a senior engineer. | H | candour | |
| B20 | Describe how you onboarded into a new, complex domain quickly. | M | learning | |

### Operations, AI era and motivation

| # | Prompt | Diff | Signal tested | Related |
|---|---|---|---|---|
| B21 | Describe an incident you led. What changed afterwards? | H | incident leadership | [incident leadership](../tracks/staff-skills/incident-leadership.md) |
| B22 | How have you introduced AI tools or AI features into a team responsibly? What went wrong? | H | AI-era leadership | [AI-era leadership](../tracks/staff-skills/ai-era-leadership.md) |
| B23 | Tell me about a design doc or RFC you wrote that changed direction after review. | M | written communication | [design docs and RFCs](../tracks/staff-skills/design-docs-rfcs.md) |
| B24 | What kind of Staff engineer are you (archetype), and what work do you avoid? | H | self-knowledge | [Staff archetypes](../tracks/staff-skills/staff-archetypes.md) |
| B25 | Why this role, and what would you do in your first 90 days? | M | motivation, planning | |

!!! tip "Story bank coverage"
    Map your 8–10 strongest stories against B1–B25. Each story should cover 3+ prompts. Any prompt with no story → write one before the next checkpoint.
