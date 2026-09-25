---
title: Week 22 — Write-ups + STAR bank II
week: 22
generated: true
---

# Week 22 — Write-ups + STAR bank II

!!! abstract "At a glance"
    **Phase 6:** Capstone + Interview Loop · **Starts:** Mon 22 Feb 2027 · **Planned:** 13h 15m

    **Build:** Capstone: README, demo video, blog post #1 (eval-driven agent development)

## By day

### Monday 22 Feb · 1h 30m

- [ ] **System Design** · 45 min · Timed SD mock: chat system (redo) — focus on deep dives and trade-off articulation → [Chat / messaging system](../../tracks/system-design/case-studies/chat-system.md) <small>`w22-sd-1`</small>
- [ ] **DSA** · 25 min · LLD: parking lot with OOP + extensibility discussion → [Concurrency & low-level design problems (LRU, rate limiter, parking lot)](../../tracks/dsa/concurrency-lld.md) <small>`w22-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: implement LRU with OrderedDict and with dict+linked list; compare → [Python data model & dunder protocols](../../tracks/python/data-model.md) <small>`w22-py-1`</small>

### Tuesday 23 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Write blog post #1: eval-driven development of the Ops Copilot (error analysis → judges → CI gates) with real numbers → [Evals I: error analysis, LLM-as-judge, eval-driven development](../../tracks/agentic-ai/evals-error-analysis.md) · [resource](https://hamel.dev/blog/posts/evals-faq/) <small>`w22-ai-1`</small>
- [ ] **DSA** · 30 min · LLD: in-memory pub/sub with concurrent subscribers → [Concurrency & low-level design problems (LRU, rate limiter, parking lot)](../../tracks/dsa/concurrency-lld.md) <small>`w22-dsa-2`</small>

### Wednesday 24 Feb · 1h 30m

- [ ] **DSA** · 25 min · Revision: Coin Change + Word Break (DP weak spot) → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w22-dsa-3`</small>
- [ ] **Architecture** · 45 min · Architecture review of the capstone using your ADR set: find stale decisions, write superseding notes → [The architect role & trade-off thinking](../../tracks/architecture/architect-role-tradeoffs.md) <small>`w22-arch-1`</small>
- [ ] **Python** · 20 min · Rep: asyncio interview questions — explain event loop, cancellation, TaskGroup semantics → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w22-py-2`</small>

### Thursday 25 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Multi-agent retrospective: where a second agent helped/hurt; document failure modes observed → [Multi-agent systems: when, how, and failure modes](../../tracks/agentic-ai/multi-agent-systems.md) <small>`w22-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI RAG + MCP demo polish; record Java side of the demo → [RAG with Spring AI & pgvector](../../tracks/java-spring-ai/spring-ai-rag.md) <small>`w22-java-1`</small>

### Friday 26 Feb · 1h 30m

- [ ] **System Design** · 45 min · Replication + partitioning L3 drill (10 questions out loud) → [Partitioning & sharding, consistent hashing](../../tracks/system-design/partitioning-sharding.md) <small>`w22-sd-2`</small>
- [ ] **DSA** · 25 min · Revision: Course Schedule II + Redundant Connection → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w22-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: Pydantic v2 interview questions — validation modes, performance, serialization → [Pydantic v2 in depth](../../tracks/python/pydantic-v2.md) <small>`w22-py-3`</small>

### Saturday 27 Feb · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: README (architecture, run locally, evals, costs), 5-min demo recording, tag v1.0 → [LLM observability: Langfuse, Phoenix, OTel GenAI semconv](../../tracks/agentic-ai/llm-observability.md) <small>`w22-ai-3`</small>
- [ ] **DSA** · 30 min · Revision: Minimum Window Substring + Trapping Rain Water → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w22-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Java concurrency interview drill: virtual threads, structured concurrency, CompletableFuture → [Virtual threads, structured concurrency & scoped values](../../tracks/java-spring-ai/virtual-threads-structured-concurrency.md) <small>`w22-java-2`</small>

### Sunday 28 Feb · 2h 45m

- [ ] **System Design** · 45 min · Written design (timed): multi-tenant LLM gateway redo in 45 min → [Design a multi-tenant LLM gateway](../../tracks/ai-system-design/llm-gateway.md) <small>`w22-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 022 for capstone: tenant isolation model for a multi-team rollout (pool with row-level security) → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) · [resource](https://adr.github.io) <small>`w22-arch-2`</small>
- [ ] **Staff+** · 30 min · STAR bank part 2: 6 Staff-level stories (strategy, cross-org alignment, tech debt, incident, hiring bar, AI adoption) with metrics → [Behavioral & Staff interviews: STAR stories bank](../../tracks/staff-skills/behavioral-interviews.md) <small>`w22-staff-1`</small>
- [ ] **Review** · 60 min · Retro + flashcards: all P0 AI topics; explain-it-back guardrails and routing → [Guardrails & security: OWASP LLM/Agentic Top 10, prompt injection](../../tracks/agentic-ai/guardrails-security.md) <small>`w22-rev-1`</small>

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
