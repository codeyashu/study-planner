---
title: "Week 03 — Context engineering, workflows, sliding window"
week: 3
generated: true
---

# Week 03 — Context engineering, workflows, sliding window

!!! abstract "At a glance"
    **Phase 1:** Foundations · **Starts:** Mon 12 Oct 2026 · **Planned:** 16h 45m

    **Build:** Capstone: routing + prompt-chaining workflow with history compaction

## By day

### Monday 12 Oct · 2h 00m

- [ ] **System Design** · 45 min · DDIA 2e ch1-2: reliability, scalability, maintainability — describe load parameters + percentiles for the capstone → [Scalability fundamentals & latency numbers](../../tracks/system-design/scalability-fundamentals.md) · [resource](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) <small>`w03-sd-1`</small>
- [ ] **DSA** · 25 min · Best Time to Buy and Sell Stock + Longest Substring Without Repeating Characters → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w03-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: asyncio.TaskGroup to fan out 5 tool calls; exception propagation via ExceptionGroup/except* → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w03-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Present perfect vs past simple, and time expressions → [Week 03 drills · day 1](../../tracks/communication/drills/week-03.md#day-1) <small>`w03-comm-1`</small>

### Tuesday 13 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · Read Anthropic 'Effective context engineering for AI agents'; write a context budget for the triage agent (system, tools, retrieved docs, history, scratchpad) → [Context engineering](../../tracks/agentic-ai/context-engineering.md) · [resource](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) <small>`w03-ai-1`</small>
- [ ] **DSA** · 30 min · Longest Repeating Character Replacement (window validity = len - maxfreq <= k) → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w03-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Tech-leadership verbs: champion, unblock, de-risk → [Week 03 drills · day 2](../../tracks/communication/drills/week-03.md#day-2) <small>`w03-comm-2`</small>

### Wednesday 14 Oct · 2h 00m

- [ ] **DSA** · 25 min · Permutation in String (fixed window counts) → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w03-dsa-3`</small>
- [ ] **Architecture** · 45 min · Design patterns that still matter: strategy, adapter, decorator, chain of responsibility — map each to LLM provider / middleware code → [Design patterns that still matter (GoF, modern)](../../tracks/architecture/design-patterns.md) · [resource](https://refactoring.guru) <small>`w03-arch-1`</small>
- [ ] **Python** · 20 min · Rep: asyncio cancellation + asyncio.timeout(); make a tool call cancel-safe (cleanup in finally) → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w03-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Intonation for emphasis and questions → [Week 03 drills · day 3](../../tracks/communication/drills/week-03.md#day-3) <small>`w03-comm-3`</small>

### Thursday 15 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · Reasoning models: when extended thinking helps vs hurts; compare a reasoning and a fast model on 20 triage cases (accuracy, latency, cost) → [LLM fundamentals: tokens, transformers, sampling, reasoning models](../../tracks/agentic-ai/llm-fundamentals.md) <small>`w03-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring Boot 4 highlights: API versioning, built-in retry/concurrency limits, JSpecify null-safety — apply @Retryable to an LLM call → [Spring Boot 4 & Spring Framework 7](../../tracks/java-spring-ai/spring-boot-4.md) <small>`w03-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Risk and uncertainty: in the pipeline, up in the air → [Week 03 drills · day 4](../../tracks/communication/drills/week-03.md#day-4) <small>`w03-comm-4`</small>

### Friday 16 Oct · 2h 00m

- [ ] **System Design** · 45 min · Proxies & gateways: reverse proxy, API gateway, service mesh — where each sits in front of an LLM service → [Load balancing & proxies](../../tracks/system-design/load-balancing.md) <small>`w03-sd-2`</small>
- [ ] **DSA** · 25 min · Minimum Window Substring (need/have counters) → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w03-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: ParamSpec + Concatenate to type a @retry decorator that preserves signatures → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) · [resource](https://typing.python.org) <small>`w03-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Meeting notes and action items → [Week 03 drills · day 5](../../tracks/communication/drills/week-03.md#day-5) <small>`w03-comm-5`</small>

### Saturday 17 Oct · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: routing workflow — classify incident type then dispatch to specialised prompt chains; add history compaction when context > budget → [Agent & workflow patterns (Building Effective Agents)](../../tracks/agentic-ai/agent-patterns.md) · [resource](https://www.anthropic.com/engineering/building-effective-agents) <small>`w03-ai-3`</small>
- [ ] **DSA** · 30 min · Sliding Window Maximum (monotonic deque) → [Sliding window](../../tracks/dsa/sliding-window.md) · [resource](https://neetcode.io) <small>`w03-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI advisors: SimpleLoggerAdvisor + MessageChatMemoryAdvisor; write a custom advisor that redacts emails from prompts → [Spring AI 2.0 fundamentals: ChatClient, advisors, structured output](../../tracks/java-spring-ai/spring-ai-fundamentals.md) · [resource](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) <small>`w03-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Intonation for emphasis and questions → [Week 03 drills · day 6](../../tracks/communication/drills/week-03.md#day-6) <small>`w03-comm-6`</small>

### Sunday 18 Oct · 3h 15m

- [ ] **System Design** · 45 min · Written design: public API for the capstone — REST + SSE streaming, idempotent ticket creation, cursor pagination, versioning, error model → [API design: REST, gRPC, GraphQL, idempotency, pagination](../../tracks/system-design/api-design.md) <small>`w03-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 003 for capstone: LLM provider abstraction via Protocol-based adapter (vs LiteLLM-only)  → [Design patterns that still matter (GoF, modern)](../../tracks/architecture/design-patterns.md) · [resource](https://adr.github.io) <small>`w03-arch-2`</small>
- [ ] **Staff+** · 30 min · Read a good design doc structure (context, goals/non-goals, alternatives, risks) and draft a template for docs/log/design-doc-template.md → [Design docs & RFCs that get approved](../../tracks/staff-skills/design-docs-rfcs.md) · [resource](https://lethain.com) <small>`w03-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Receiving feedback without defensiveness → [Week 03 drills · day 7](../../tracks/communication/drills/week-03.md#day-7) <small>`w03-comm-7`</small>
- [ ] **Review** · 60 min · Retro week 1-3 + flashcards: context engineering vocabulary (compaction, JIT retrieval, tool budget); explain-it-back sliding window invariant → [Context engineering](../../tracks/agentic-ai/context-engineering.md) <small>`w03-rev-1`</small>

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
