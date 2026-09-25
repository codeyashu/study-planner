---
title: Week 08 — Evals II in CI + observability — interview-2
week: 8
generated: true
---

# Week 08 — Evals II in CI + observability — interview-2

!!! abstract "At a glance"
    **Phase 2:** RAG + Evals · **Starts:** Mon 16 Nov 2026 · **Planned:** 13h 15m

    **Build:** Capstone: promptfoo/DeepEval/Ragas in CI with thresholds + Langfuse tracing

!!! warning "Interview checkpoint: interview-2"
    Run the full mock loop and score it with the [rubric](../../interviews/rubric.md).

## By day

### Monday 16 Nov · 1h 30m

- [ ] **System Design** · 45 min · Search systems: inverted index, BM25, sharding an index, near-real-time refresh → [Search systems & inverted indexes](../../tracks/system-design/search-systems.md) <small>`w08-sd-1`</small>
- [ ] **DSA** · 25 min · Invert Binary Tree + Maximum Depth of Binary Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w08-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: Polars/DuckDB to aggregate eval results (per failure category, per model) → [Data tooling: Polars, DuckDB, Arrow](../../tracks/python/data-tooling.md) <small>`w08-py-1`</small>

### Tuesday 17 Nov · 1h 30m

- [ ] **Agentic AI** · 60 min · Eval tooling survey: promptfoo vs DeepEval vs Ragas vs Inspect — pick per use case (regression, RAG metrics, agent tasks) → [Evals II: promptfoo, DeepEval, Ragas, Inspect in CI](../../tracks/agentic-ai/eval-tooling.md) · [resource](https://docs.ragas.io/) <small>`w08-ai-1`</small>
- [ ] **DSA** · 30 min · Diameter of Binary Tree + Balanced Binary Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w08-dsa-2`</small>

### Wednesday 18 Nov · 1h 30m

- [ ] **DSA** · 25 min · Same Tree + Subtree of Another Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w08-dsa-3`</small>
- [ ] **Architecture** · 45 min · Balancing Coupling in Software Design: strength, distance, volatility — score couplings in the capstone → [Coupling, cohesion & modularity (balanced coupling)](../../tracks/architecture/coupling-modularity.md) <small>`w08-arch-1`</small>
- [ ] **Python** · 20 min · Rep: class decorators vs metaclass vs __init_subclass__ for a tool registry → [Decorators, descriptors & metaclasses](../../tracks/python/decorators-descriptors-metaclasses.md) <small>`w08-py-2`</small>

### Thursday 19 Nov · 1h 30m

- [ ] **Agentic AI** · 60 min · LLM observability: Langfuse traces/spans/scores + OTel GenAI semantic conventions (still Development status) — instrument one request end to end → [LLM observability: Langfuse, Phoenix, OTel GenAI semconv](../../tracks/agentic-ai/llm-observability.md) · [resource](https://langfuse.com/docs) <small>`w08-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Compare Spring AI vs Python RAG on the same 30-query set; note differences in retrieval defaults → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w08-java-1`</small>

### Friday 20 Nov · 1h 30m

- [ ] **System Design** · 45 min · Blob storage + CDN: presigned URLs, cache keys, invalidation, edge compute — for storing ingested documents → [Blob storage, CDN & edge](../../tracks/system-design/storage-cdn.md) <small>`w08-sd-2`</small>
- [ ] **DSA** · 25 min · Lowest Common Ancestor of a Binary Search Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w08-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: PEP 695 generics (class Result[T]) + TypedDict for eval records → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) · [resource](https://typing.python.org) <small>`w08-py-3`</small>

### Saturday 21 Nov · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: GitHub Actions eval job (promptfoo or DeepEval) failing the build under thresholds; Ragas faithfulness/context-precision report on the golden set → [Evals II: promptfoo, DeepEval, Ragas, Inspect in CI](../../tracks/agentic-ai/eval-tooling.md) · [resource](https://deepeval.com/) <small>`w08-ai-3`</small>
- [ ] **DSA** · 30 min · Timed coding mock (interview-2): Binary Tree Level Order Traversal + Binary Tree Right Side View in 30 min → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w08-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Records + sealed types for eval results in Java; pattern-matching switch over outcomes → [Modern Java 21→25: records, sealed types, patterns](../../tracks/java-spring-ai/modern-java.md) <small>`w08-java-2`</small>

### Sunday 22 Nov · 2h 45m

- [ ] **System Design** · 45 min · Timed 45-min AI SD mock (interview-2): design AI-powered semantic search for a 10M-document corpus → [Design AI-powered semantic search](../../tracks/ai-system-design/ai-search.md) · [resource](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) <small>`w08-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 008 for capstone: pgvector over Qdrant for v1 (coupling, ops cost, scale ceiling, exit path) → [Coupling, cohesion & modularity (balanced coupling)](../../tracks/architecture/coupling-modularity.md) · [resource](https://qdrant.tech/documentation/) <small>`w08-arch-2`</small>
- [ ] **Staff+** · 30 min · Write a stakeholder update on eval-in-CI: what it catches, cost, what you need from other teams → [Communicating with executives & stakeholders](../../tracks/staff-skills/communication-stakeholders.md) <small>`w08-staff-1`</small>
- [ ] **Review** · 60 min · interview-2: full mock — SD + coding + AI SD + behavioral, score with docs/interviews/rubric.md and log gaps into next week's plan → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) <small>`w08-rev-1`</small>

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
| Review | 1 | 1h 00m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
