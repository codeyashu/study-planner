---
title: "Week 06 — Hybrid search + reranking (light week)"
week: 6
generated: true
---

# Week 06 — Hybrid search + reranking (light week)

!!! abstract "At a glance"
    **Phase 2:** RAG + Evals · **Starts:** Mon 02 Nov 2026 · **Planned:** 11h 00m · **Light week**

    **Build:** Capstone: hybrid retrieval (BM25 + dense + metadata filters) with cross-encoder reranking

## By day

### Monday 02 Nov · 1h 20m

- [ ] **System Design** · 30 min · SQL vs NoSQL choice matrix: access patterns, transactions, secondary indexes — for 3 capstone entities → [Databases: SQL vs NoSQL, storage engines](../../tracks/system-design/databases-sql-nosql.md) <small>`w06-sd-1`</small>
- [ ] **DSA** · 15 min · Median of Two Sorted Arrays (binary search on partition) → [Binary search (incl. on answer)](../../tracks/dsa/binary-search.md) · [resource](https://neetcode.io) <small>`w06-dsa-1`</small>
- [ ] **Python** · 15 min · Rep: Hypothesis property test for the chunker (no text lost, chunk size bounds) → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w06-py-1`</small>
- [ ] **Communication** · 20 min · Grammar: Punctuation and style: commas, dashes, semicolons → [Week 06 drills · day 1](../../tracks/communication/drills/week-06.md#day-1) <small>`w06-comm-1`</small>

### Tuesday 03 Nov · 1h 20m

- [ ] **Agentic AI** · 40 min · Hybrid search: BM25 + dense fusion (RRF vs weighted), metadata pre/post-filtering trade-offs → [Hybrid search & reranking](../../tracks/agentic-ai/hybrid-search-reranking.md) <small>`w06-ai-1`</small>
- [ ] **DSA** · 20 min · Reverse Linked List + Merge Two Sorted Lists → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w06-dsa-2`</small>
- [ ] **Communication** · 20 min · Vocabulary: Verb-noun collocations (make a case, raise a concern) → [Week 06 drills · day 2](../../tracks/communication/drills/week-06.md#day-2) <small>`w06-comm-2`</small>

### Wednesday 04 Nov · 1h 20m

- [ ] **DSA** · 15 min · Linked List Cycle (Floyd) → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w06-dsa-3`</small>
- [ ] **Architecture** · 30 min · DDD strategic: subdomains (core/supporting/generic), bounded contexts, context map for the ops domain (Learning DDD, Khononov) → [DDD strategic: subdomains, bounded contexts, context maps](../../tracks/architecture/ddd-strategic.md) <small>`w06-arch-1`</small>
- [ ] **Python** · 15 min · Rep: Unit of Work context manager wrapping a Postgres transaction → [Architecture patterns in Python (repository, UoW, message bus)](../../tracks/python/architecture-patterns-python.md) · [resource](https://www.cosmicpython.com/) <small>`w06-py-2`</small>
- [ ] **Communication** · 20 min · Speaking drill: Shadowing practice 1 → [Week 06 drills · day 3](../../tracks/communication/drills/week-06.md#day-3) <small>`w06-comm-3`</small>

### Thursday 05 Nov · 1h 20m

- [ ] **Agentic AI** · 40 min · Rerankers: bi-encoder vs cross-encoder vs LLM reranking — read Pinecone series and pick one for the capstone → [Hybrid search & reranking](../../tracks/agentic-ai/hybrid-search-reranking.md) · [resource](https://www.pinecone.io/learn/series/rag/rerankers/) <small>`w06-ai-2`</small>
- [ ] **Java/Spring AI** · 20 min · Spring AI RetrievalAugmentationAdvisor / QuestionAnswerAdvisor with filter expressions → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w06-java-1`</small>
- [ ] **Communication** · 20 min · Idioms & phrasal verbs: Phrasal verbs in meetings: bring up, follow up, wrap up → [Week 06 drills · day 4](../../tracks/communication/drills/week-06.md#day-4) <small>`w06-comm-4`</small>

### Friday 06 Nov · 1h 15m

- [ ] **System Design** · 30 min · Replication: single-leader, multi-leader, leaderless; replication lag anomalies (read-your-writes, monotonic reads) → [Replication](../../tracks/system-design/replication.md) · [resource](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) <small>`w06-sd-2`</small>
- [ ] **DSA** · 15 min · Reorder List → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w06-dsa-4`</small>
- [ ] **Python** · 10 min · Rep: src layout + pyproject entry points; build a wheel with uv build → [Packaging, project layout & monorepos](../../tracks/python/packaging-project-structure.md) · [resource](https://docs.astral.sh/uv/) <small>`w06-py-3`</small>
- [ ] **Communication** · 20 min · Writing: Tightening paragraphs → [Week 06 drills · day 5](../../tracks/communication/drills/week-06.md#day-5) <small>`w06-comm-5`</small>

### Saturday 07 Nov · 2h 15m

- [ ] **Agentic AI** · 75 min · Capstone build: add Postgres full-text (or pg_search) BM25 leg + RRF fusion + cross-encoder rerank; compare hit rate@5 vs dense-only on 30 queries → [Hybrid search & reranking](../../tracks/agentic-ai/hybrid-search-reranking.md) <small>`w06-ai-3`</small>
- [ ] **DSA** · 20 min · Remove Nth Node From End of List → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w06-dsa-5`</small>
- [ ] **Java/Spring AI** · 20 min · Spring Boot 4 + Testcontainers dev services for pgvector in local runs → [Spring Boot 4 & Spring Framework 7](../../tracks/java-spring-ai/spring-boot-4.md) <small>`w06-java-2`</small>
- [ ] **Communication** · 20 min · Record & shadow: Shadowing practice 1 → [Week 06 drills · day 6](../../tracks/communication/drills/week-06.md#day-6) <small>`w06-comm-6`</small>

### Sunday 08 Nov · 2h 10m

- [ ] **System Design** · 30 min · Written design: enterprise RAG system — ingestion, ACL-aware retrieval, hybrid search, reranking, eval, freshness (short 2-page version) → [Design an enterprise RAG system](../../tracks/ai-system-design/rag-system.md) <small>`w06-sd-3`</small>
- [ ] **Architecture** · 20 min · Write ADR 006 for capstone: bounded contexts — Incident, Knowledge, Ticketing — and their integration style → [DDD strategic: subdomains, bounded contexts, context maps](../../tracks/architecture/ddd-strategic.md) · [resource](https://adr.github.io) <small>`w06-arch-2`</small>
- [ ] **Staff+** · 20 min · Artifact: capstone design doc v1 (docs/log/design-doc-capstone.md) — send to one peer/AI reviewer for critique → [Design docs & RFCs that get approved](../../tracks/staff-skills/design-docs-rfcs.md) <small>`w06-staff-1`</small>
- [ ] **Communication** · 20 min · Soft skills + weekly review: Storytelling basics: context, conflict, resolution → [Week 06 drills · day 7](../../tracks/communication/drills/week-06.md#day-7) <small>`w06-comm-7`</small>
- [ ] **Review** · 40 min · Light-week retro + flashcards: hybrid search, RRF, rerankers, replication anomalies → [Hybrid search & reranking](../../tracks/agentic-ai/hybrid-search-reranking.md) <small>`w06-rev-1`</small>

## By track

| Track | Tasks | Time |
|---|---|---|
| Agentic AI | 3 | 2h 35m |
| System Design | 3 | 1h 30m |
| DSA | 5 | 1h 25m |
| Architecture | 2 | 50m |
| Python | 3 | 40m |
| Java/Spring AI | 2 | 40m |
| Staff+ | 1 | 20m |
| Communication | 7 | 2h 20m |
| Review | 1 | 40m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
