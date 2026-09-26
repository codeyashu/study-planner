---
title: "Week 07 — Evals I — error analysis, LLM-as-judge"
week: 7
generated: true
---

# Week 07 — Evals I — error analysis, LLM-as-judge

!!! abstract "At a glance"
    **Phase 2:** RAG + Evals · **Starts:** Mon 09 Nov 2026 · **Planned:** 16h 45m

    **Build:** Capstone: eval harness — error analysis on 100 traces, failure taxonomy, LLM-as-judge aligned to labels

## By day

### Monday 09 Nov · 2h 00m

- [ ] **System Design** · 45 min · Partitioning: key-range vs hash, consistent hashing with vnodes, hot keys and rebalancing → [Partitioning & sharding, consistent hashing](../../tracks/system-design/partitioning-sharding.md) <small>`w07-sd-1`</small>
- [ ] **DSA** · 25 min · Copy List with Random Pointer → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w07-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: descriptors — build a validated field descriptor; how properties are descriptors → [Decorators, descriptors & metaclasses](../../tracks/python/decorators-descriptors-metaclasses.md) · [resource](https://www.fluentpython.com/) <small>`w07-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Relative clauses and reported speech → [Week 07 drills · day 1](../../tracks/communication/drills/week-07.md#day-1) <small>`w07-comm-1`</small>

### Tuesday 10 Nov · 2h 00m

- [ ] **Agentic AI** · 60 min · Read Hamel & Shreya evals FAQ: error analysis → open/axial coding → failure taxonomy; apply to 50 capstone traces → [Evals I: error analysis, LLM-as-judge, eval-driven development](../../tracks/agentic-ai/evals-error-analysis.md) · [resource](https://hamel.dev/blog/posts/evals-faq/) <small>`w07-ai-1`</small>
- [ ] **DSA** · 30 min · Add Two Numbers + Find the Duplicate Number → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w07-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Persuasion words: compelling, tangible, rationale → [Week 07 drills · day 2](../../tracks/communication/drills/week-07.md#day-2) <small>`w07-comm-2`</small>

### Wednesday 11 Nov · 2h 00m

- [ ] **DSA** · 25 min · LRU Cache (hash map + doubly linked list) → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w07-dsa-3`</small>
- [ ] **Architecture** · 45 min · DDD tactical: aggregates, invariants, value objects, domain events — model the Incident aggregate → [DDD tactical: aggregates, entities, value objects, domain events](../../tracks/architecture/ddd-tactical.md) <small>`w07-arch-1`</small>
- [ ] **Python** · 20 min · Rep: message bus dispatching domain events to handlers (Cosmic Python ch8) → [Architecture patterns in Python (repository, UoW, message bus)](../../tracks/python/architecture-patterns-python.md) · [resource](https://www.cosmicpython.com/) <small>`w07-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Explaining technical ideas to non-technical people → [Week 07 drills · day 3](../../tracks/communication/drills/week-07.md#day-3) <small>`w07-comm-3`</small>

### Thursday 12 Nov · 2h 00m

- [ ] **Agentic AI** · 60 min · LLM-as-judge: binary pass/fail judges, measure judge TPR/TNR against 40 hand labels; iterate judge prompt → [Evals I: error analysis, LLM-as-judge, eval-driven development](../../tracks/agentic-ai/evals-error-analysis.md) · [resource](https://hamel.dev/blog/posts/evals-faq/) <small>`w07-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI evaluation: RelevancyEvaluator / FactCheckingEvaluator on the Java RAG path → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w07-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Teamwork: pull your weight, have each other's back → [Week 07 drills · day 4](../../tracks/communication/drills/week-07.md#day-4) <small>`w07-comm-4`</small>

### Friday 13 Nov · 2h 00m

- [ ] **System Design** · 45 min · Consistency models map: linearisable, sequential, causal, eventual; CAP vs PACELC — use Jepsen consistency pages → [Consistency models, CAP & PACELC](../../tracks/system-design/consistency-models.md) · [resource](https://jepsen.io/analyses) <small>`w07-sd-2`</small>
- [ ] **DSA** · 25 min · Merge K Sorted Lists → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w07-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: testcontainers-python spinning pgvector for integration tests → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w07-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Technical explanations with analogies → [Week 07 drills · day 5](../../tracks/communication/drills/week-07.md#day-5) <small>`w07-comm-5`</small>

### Saturday 14 Nov · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: eval harness (pytest-style) with golden set, retrieval metrics (recall@k, MRR) + generation judge; run on RAG v0 vs hybrid → [Evals I: error analysis, LLM-as-judge, eval-driven development](../../tracks/agentic-ai/evals-error-analysis.md) · [resource](https://applied-llms.org/) <small>`w07-ai-3`</small>
- [ ] **DSA** · 30 min · Reverse Nodes in k-Group → [Linked list](../../tracks/dsa/linked-list.md) · [resource](https://neetcode.io) <small>`w07-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Testcontainers (pgvector) integration test for the Spring AI RAG endpoint with a fixed 10-query assertion set → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w07-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Explaining technical ideas to non-technical people → [Week 07 drills · day 6](../../tracks/communication/drills/week-07.md#day-6) <small>`w07-comm-6`</small>

### Sunday 15 Nov · 3h 15m

- [ ] **System Design** · 45 min · Written design: news feed / timeline — fan-out on write vs read, celebrity problem, ranking, cache layers → [News feed / timeline](../../tracks/system-design/case-studies/news-feed.md) <small>`w07-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 007 for capstone: Incident aggregate boundaries and domain events (IncidentTriaged, TicketCreated) → [DDD tactical: aggregates, entities, value objects, domain events](../../tracks/architecture/ddd-tactical.md) · [resource](https://adr.github.io) <small>`w07-arch-2`</small>
- [ ] **Staff+** · 30 min · Write a 1-page exec summary of RAG v0 vs hybrid results (decision, numbers, risk, ask) for a non-technical stakeholder → [Communicating with executives & stakeholders](../../tracks/staff-skills/communication-stakeholders.md) <small>`w07-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Influencing without authority → [Week 07 drills · day 7](../../tracks/communication/drills/week-07.md#day-7) <small>`w07-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back: consistent hashing + consistency models in 3 min each; flashcards on eval terms (TPR/TNR, axial coding) → [Consistency models, CAP & PACELC](../../tracks/system-design/consistency-models.md) <small>`w07-rev-1`</small>

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
