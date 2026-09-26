---
title: Week 02 — Tool calling, API design, two pointers
week: 2
generated: true
---

# Week 02 — Tool calling, API design, two pointers

!!! abstract "At a glance"
    **Phase 1:** Foundations · **Starts:** Mon 05 Oct 2026 · **Planned:** 16h 45m

    **Build:** Capstone: typed tool calling loop (runbook search, service status, ticket create)

## By day

### Monday 05 Oct · 2h 00m

- [ ] **System Design** · 45 min · API design: idempotency keys, cursor pagination, REST vs gRPC vs GraphQL trade-offs — decide for capstone's external API → [API design: REST, gRPC, GraphQL, idempotency, pagination](../../tracks/system-design/api-design.md) <small>`w02-sd-1`</small>
- [ ] **DSA** · 25 min · Valid Sudoku (row/col/box sets) → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w02-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: typing.Protocol for an LLMClient port; structural vs nominal typing, runtime_checkable caveats → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) · [resource](https://typing.python.org) <small>`w02-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Prepositions and collocations → [Week 02 drills · day 1](../../tracks/communication/drills/week-02.md#day-1) <small>`w02-comm-1`</small>

### Tuesday 06 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · Structured outputs deep dive: constrained decoding vs tool-forcing vs validate-and-retry; measure failure rate on 50 synthetic incident texts → [Prompting & structured outputs](../../tracks/agentic-ai/prompting-structured-outputs.md) <small>`w02-ai-1`</small>
- [ ] **DSA** · 30 min · Valid Palindrome + Two Sum II - Input Array Is Sorted → [Two pointers](../../tracks/dsa/two-pointers.md) · [resource](https://neetcode.io) <small>`w02-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Word nuance: affect/impact/influence, ensure/assure/insure → [Week 02 drills · day 2](../../tracks/communication/drills/week-02.md#day-2) <small>`w02-comm-2`</small>

### Wednesday 07 Oct · 2h 00m

- [ ] **DSA** · 25 min · 3Sum (sort + two pointers, skip duplicates) → [Two pointers](../../tracks/dsa/two-pointers.md) · [resource](https://neetcode.io) <small>`w02-dsa-3`</small>
- [ ] **Architecture** · 45 min · Architecture styles: modular monolith vs microservices vs event-driven — score each against the capstone's characteristics → [Architecture styles: modular monolith → microservices → event-driven → serverless](../../tracks/architecture/architecture-styles.md) · [resource](https://microservices.io) <small>`w02-arch-1`</small>
- [ ] **Python** · 20 min · Rep: data model — __eq__/__hash__/__repr__ on a value object; why dataclass(frozen=True) vs Pydantic here → [Python data model & dunder protocols](../../tracks/python/data-model.md) · [resource](https://www.fluentpython.com/) <small>`w02-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Word stress and sentence rhythm → [Week 02 drills · day 3](../../tracks/communication/drills/week-02.md#day-3) <small>`w02-comm-3`</small>

### Thursday 08 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · LLM internals for engineers: KV cache, context window cost, prefill vs decode latency — estimate p50/p95 latency and cost per /triage call → [LLM fundamentals: tokens, transformers, sampling, reasoning models](../../tracks/agentic-ai/llm-fundamentals.md) · [resource](https://github.com/chiphuyen/aie-book) <small>`w02-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI 2.0 ChatClient fluent API: system/user prompts, options, streaming — hello-world against Ollama → [Spring AI 2.0 fundamentals: ChatClient, advisors, structured output](../../tracks/java-spring-ai/spring-ai-fundamentals.md) · [resource](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) <small>`w02-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Progress and delay: behind schedule, move the needle → [Week 02 drills · day 4](../../tracks/communication/drills/week-02.md#day-4) <small>`w02-comm-4`</small>

### Friday 09 Oct · 2h 00m

- [ ] **System Design** · 45 min · Load balancing: L4 vs L7, algorithms, health checks — work through Sam Who's interactive essay → [Load balancing & proxies](../../tracks/system-design/load-balancing.md) · [resource](https://samwho.dev/load-balancing/) <small>`w02-sd-2`</small>
- [ ] **DSA** · 25 min · Container With Most Water (greedy pointer move proof) → [Two pointers](../../tracks/dsa/two-pointers.md) · [resource](https://neetcode.io) <small>`w02-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: Pydantic discriminated unions for tool results (Success | ToolError) with Field(discriminator=...) → [Pydantic v2 in depth](../../tracks/python/pydantic-v2.md) <small>`w02-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Clear status updates → [Week 02 drills · day 5](../../tracks/communication/drills/week-02.md#day-5) <small>`w02-comm-5`</small>

### Saturday 10 Oct · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: 3 typed tools (search_runbooks stub, get_service_status, create_ticket) with Pydantic arg schemas, error-as-result returns and a hand-rolled tool loop with max-steps → [Tool calling & function design](../../tracks/agentic-ai/tool-calling.md) <small>`w02-ai-3`</small>
- [ ] **DSA** · 30 min · Trapping Rain Water (two pointers with left/right max) → [Two pointers](../../tracks/dsa/two-pointers.md) · [resource](https://neetcode.io) <small>`w02-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI structured output: .entity(IncidentTriage.class) with a Java record; compare failure behaviour to Python → [Spring AI 2.0 fundamentals: ChatClient, advisors, structured output](../../tracks/java-spring-ai/spring-ai-fundamentals.md) <small>`w02-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Word stress and sentence rhythm → [Week 02 drills · day 6](../../tracks/communication/drills/week-02.md#day-6) <small>`w02-comm-6`</small>

### Sunday 11 Oct · 3h 15m

- [ ] **System Design** · 45 min · Written design: estimation write-up — size the capstone for 50 teams, 2k incidents/day, 10 tool calls each (tokens, $/month, QPS, storage) → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) <small>`w02-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 002 for capstone: modular monolith (Python) + separate Spring AI MCP service → [Architecture styles: modular monolith → microservices → event-driven → serverless](../../tracks/architecture/architecture-styles.md) · [resource](https://adr.github.io) <small>`w02-arch-2`</small>
- [ ] **Staff+** · 30 min · Artifact: archetype self-assessment — which archetype you target, evidence you have, 3 gaps (docs/log/staff/archetype.md) → [Staff archetypes & operating at Staff+](../../tracks/staff-skills/staff-archetypes.md) · [resource](https://staffeng.com/guides/staff-archetypes/) <small>`w02-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Giving feedback with SBI (situation-behaviour-impact) → [Week 02 drills · day 7](../../tracks/communication/drills/week-02.md#day-7) <small>`w02-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back (record 5 min): tool-calling loop design and why tool errors are returned as results; 15 flashcards on API design → [Tool calling & function design](../../tracks/agentic-ai/tool-calling.md) <small>`w02-rev-1`</small>

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
