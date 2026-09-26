---
title: Week 12 — Protocols, memory, vendor SDKs (light) — interview-3
week: 12
generated: true
---

# Week 12 — Protocols, memory, vendor SDKs (light) — interview-3

!!! abstract "At a glance"
    **Phase 3:** Agents + Protocols · **Starts:** Mon 14 Dec 2026 · **Planned:** 11h 00m · **Light week**

    **Build:** Capstone: A2A/AG-UI spike + Mem0 memory prototype + vendor SDK comparison notes

!!! warning "Interview checkpoint: interview-3"
    Run the full mock loop and score it with the [rubric](../../tracks/staff-skills/interview-prep/rubric.md).

## By day

### Monday 14 Dec · 1h 20m

- [ ] **System Design** · 30 min · Distributed job scheduler write-up review; data pipeline for trace → eval dataset → [Batch & stream data pipelines](../../tracks/system-design/data-pipelines.md) <small>`w12-sd-1`</small>
- [ ] **DSA** · 15 min · Permutations + Subsets II → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w12-dsa-1`</small>
- [ ] **Python** · 15 min · Rep: Protocol + generics for a typed Memory store interface → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) · [resource](https://typing.python.org) <small>`w12-py-1`</small>
- [ ] **Communication** · 20 min · Grammar: Linking words and cohesion → [Week 12 drills · day 1](../../tracks/communication/drills/week-12.md#day-1) <small>`w12-comm-1`</small>

### Tuesday 15 Dec · 1h 20m

- [ ] **Agentic AI** · 40 min · A2A v1.0 (signed Agent Cards, JSON-RPC/gRPC/REST) + AG-UI event stream — where each fits next to MCP → [A2A & AG-UI protocols](../../tracks/agentic-ai/a2a-ag-ui.md) · [resource](https://a2a-protocol.org/) <small>`w12-ai-1`</small>
- [ ] **DSA** · 20 min · Combination Sum II → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w12-dsa-2`</small>
- [ ] **Communication** · 20 min · Vocabulary: Review, spaced repetition round → [Week 12 drills · day 2](../../tracks/communication/drills/week-12.md#day-2) <small>`w12-comm-2`</small>

### Wednesday 16 Dec · 1h 20m

- [ ] **DSA** · 15 min · Word Search → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w12-dsa-3`</small>
- [ ] **Architecture** · 30 min · API contracts & schema evolution: backward/forward compatibility, consumer-driven contracts, versioning MCP tool schemas → [API contracts, versioning & schema evolution](../../tracks/architecture/api-contracts-versioning.md) <small>`w12-arch-1`</small>
- [ ] **Python** · 15 min · Rep: __getattr__/__slots__ trade-offs on high-volume event objects → [Python data model & dunder protocols](../../tracks/python/data-model.md) <small>`w12-py-2`</small>
- [ ] **Communication** · 20 min · Speaking drill: Shadowing practice 2 → [Week 12 drills · day 3](../../tracks/communication/drills/week-12.md#day-3) <small>`w12-comm-3`</small>

### Thursday 17 Dec · 1h 20m

- [ ] **Agentic AI** · 40 min · Vendor SDK tour: Claude Agent SDK, OpenAI Agents SDK, Google ADK 2.0, MS Agent Framework 1.0 — same toy task in 2 of them, compare → [Vendor agent SDKs: Claude Agent SDK, OpenAI Agents SDK, Google ADK, MS Agent Framework](../../tracks/agentic-ai/vendor-agent-sdks.md) · [resource](https://code.claude.com/docs/en/agent-sdk/overview) <small>`w12-ai-2`</small>
- [ ] **Java/Spring AI** · 20 min · Spring AI agent with ChatMemory + tool calling + MCP client end-to-end → [Agentic patterns with Spring AI](../../tracks/java-spring-ai/spring-ai-agents.md) <small>`w12-java-1`</small>
- [ ] **Communication** · 20 min · Idioms & phrasal verbs: Idiom review round → [Week 12 drills · day 4](../../tracks/communication/drills/week-12.md#day-4) <small>`w12-comm-4`</small>

### Friday 18 Dec · 1h 15m

- [ ] **System Design** · 30 min · Kafka vs Pulsar vs SQS/Service Bus decision table → [Message queues & streaming (Kafka)](../../tracks/system-design/messaging-streaming.md) <small>`w12-sd-2`</small>
- [ ] **DSA** · 15 min · Palindrome Partitioning → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w12-dsa-4`</small>
- [ ] **Python** · 10 min · Rep: functools.wraps, cache, singledispatch in a tool registry → [Decorators, descriptors & metaclasses](../../tracks/python/decorators-descriptors-metaclasses.md) <small>`w12-py-3`</small>
- [ ] **Communication** · 20 min · Writing: Executive summaries → [Week 12 drills · day 5](../../tracks/communication/drills/week-12.md#day-5) <small>`w12-comm-5`</small>

### Saturday 19 Dec · 2h 15m

- [ ] **Agentic AI** · 75 min · Capstone build: add Mem0 (or Letta) long-term memory for per-team preferences; expose the orchestrator via AG-UI events to a minimal UI → [Agent memory systems (Mem0, Letta, Zep)](../../tracks/agentic-ai/memory-systems.md) · [resource](https://docs.mem0.ai/) <small>`w12-ai-3`</small>
- [ ] **DSA** · 20 min · Timed coding mock (interview-3): Number of Islands + Clone Graph in 30 min → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w12-dsa-5`</small>
- [ ] **Java/Spring AI** · 20 min · Evaluate where Spring AI agent patterns are enough vs needing LangGraph → [Agentic patterns with Spring AI](../../tracks/java-spring-ai/spring-ai-agents.md) <small>`w12-java-2`</small>
- [ ] **Communication** · 20 min · Record & shadow: Shadowing practice 2 → [Week 12 drills · day 6](../../tracks/communication/drills/week-12.md#day-6) <small>`w12-comm-6`</small>

### Sunday 20 Dec · 2h 10m

- [ ] **System Design** · 30 min · Timed 45-min AI SD mock (interview-3): design a ChatGPT-style assistant (sessions, memory, tools, streaming, safety, cost) → [Design a ChatGPT-style assistant](../../tracks/ai-system-design/chat-assistant.md) <small>`w12-sd-3`</small>
- [ ] **Architecture** · 20 min · Write ADR 012 for capstone: tool schema versioning policy (additive changes, deprecation window) → [API contracts, versioning & schema evolution](../../tracks/architecture/api-contracts-versioning.md) · [resource](https://adr.github.io) <small>`w12-arch-2`</small>
- [ ] **Staff+** · 20 min · Read an incident-command model; note how you'd lead a Sev-1 involving an AI agent misbehaving → [Incident leadership & blameless postmortems](../../tracks/staff-skills/incident-leadership.md) <small>`w12-staff-1`</small>
- [ ] **Communication** · 20 min · Soft skills + weekly review: Cross-cultural communication — checkpoint comm-3: re-record and compare against the baseline rubric → [Week 12 drills · day 7](../../tracks/communication/drills/week-12.md#day-7) <small>`w12-comm-7`</small>
- [ ] **Review** · 40 min · interview-3: full mock — SD + coding + AI SD + behavioral, score with the unified interview rubric and log gaps into next week's plan → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) <small>`w12-rev-1`</small>

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
