---
title: Week 11 — Durable execution, HITL, multi-agent
week: 11
generated: true
---

# Week 11 — Durable execution, HITL, multi-agent

!!! abstract "At a glance"
    **Phase 3:** Agents + Protocols · **Starts:** Mon 07 Dec 2026 · **Planned:** 16h 45m

    **Build:** Capstone: human-in-the-loop approval (interrupt/resume) + Spring AI MCP server wired in

## By day

### Monday 07 Dec · 2h 00m

- [ ] **System Design** · 45 min · Circuit breakers, bulkheads, load shedding, timeouts hierarchy — apply to tool calls and LLM providers → [Reliability: retries, backoff, circuit breakers, bulkheads](../../tracks/system-design/reliability-patterns.md) <small>`w11-sd-1`</small>
- [ ] **DSA** · 25 min · Kth Largest Element in an Array (quickselect vs heap) → [Heap / priority queue](../../tracks/dsa/heap.md) · [resource](https://neetcode.io) <small>`w11-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: uv workspaces monorepo — orchestrator, mcp-server, evals as members → [Packaging, project layout & monorepos](../../tracks/python/packaging-project-structure.md) · [resource](https://docs.astral.sh/uv/) <small>`w11-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Advanced articles and the zero article with abstract nouns → [Week 11 drills · day 1](../../tracks/communication/drills/week-11.md#day-1) <small>`w11-comm-1`</small>

### Tuesday 08 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · Durable execution & HITL: LangGraph interrupt/Command resume, idempotent side effects, timeouts; compare with Temporal-style durable workflows → [Durable execution & human-in-the-loop](../../tracks/agentic-ai/durable-execution-hitl.md) · [resource](https://academy.langchain.com/courses/intro-to-langgraph) <small>`w11-ai-1`</small>
- [ ] **DSA** · 30 min · Task Scheduler → [Heap / priority queue](../../tracks/dsa/heap.md) · [resource](https://neetcode.io) <small>`w11-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Register: formal vs informal, and switching → [Week 11 drills · day 2](../../tracks/communication/drills/week-11.md#day-2) <small>`w11-comm-2`</small>

### Wednesday 09 Dec · 2h 00m

- [ ] **DSA** · 25 min · Design Twitter + Find Median from Data Stream → [Heap / priority queue](../../tracks/dsa/heap.md) · [resource](https://neetcode.io) <small>`w11-dsa-3`</small>
- [ ] **Architecture** · 45 min · Enterprise integration patterns: channels, content-based router, aggregator, idempotent receiver — relate to MCP/A2A → [Enterprise integration patterns](../../tracks/architecture/integration-patterns.md) <small>`w11-arch-1`</small>
- [ ] **Python** · 20 min · Rep: anyio/pytest-asyncio tests for the interrupt/resume flow → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w11-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Clarity on calls and video: pacing, signposting → [Week 11 drills · day 3](../../tracks/communication/drills/week-11.md#day-3) <small>`w11-comm-3`</small>

### Thursday 10 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · Multi-agent systems: supervisor vs swarm vs hierarchical; failure modes (loops, context loss, cost blow-up) — decide if capstone needs >1 agent → [Multi-agent systems: when, how, and failure modes](../../tracks/agentic-ai/multi-agent-systems.md) · [resource](https://www.anthropic.com/engineering/building-effective-agents) <small>`w11-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Finish Spring AI MCP server: OAuth-ready config, tool schemas, integration test from the Python LangGraph client → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) <small>`w11-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Escalation phrasal verbs: flag up, push back, loop in → [Week 11 drills · day 4](../../tracks/communication/drills/week-11.md#day-4) <small>`w11-comm-4`</small>

### Friday 11 Dec · 2h 00m

- [ ] **System Design** · 45 min · Distributed job scheduler: leases, at-least-once execution, cron fan-out, dedupe — sketch + read notes → [Distributed job scheduler](../../tracks/system-design/case-studies/job-scheduler.md) <small>`w11-sd-2`</small>
- [ ] **DSA** · 25 min · Subsets → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w11-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: DuckDB over Langfuse trace exports to find slowest nodes → [Data tooling: Polars, DuckDB, Arrow](../../tracks/python/data-tooling.md) <small>`w11-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Escalation emails → [Week 11 drills · day 5](../../tracks/communication/drills/week-11.md#day-5) <small>`w11-comm-5`</small>

### Saturday 12 Dec · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: HITL approval node before create_ticket (interrupt → approve via API → resume from checkpoint) calling the Spring AI MCP server; kill/restart mid-run to prove durability → [Durable execution & human-in-the-loop](../../tracks/agentic-ai/durable-execution-hitl.md) <small>`w11-ai-3`</small>
- [ ] **DSA** · 30 min · Combination Sum → [Backtracking](../../tracks/dsa/backtracking.md) · [resource](https://neetcode.io) <small>`w11-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI agentic patterns: chain, routing, orchestrator-workers examples — port one to the Java service → [Agentic patterns with Spring AI](../../tracks/java-spring-ai/spring-ai-agents.md) · [resource](https://github.com/spring-ai-community/awesome-spring-ai) <small>`w11-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Clarity on calls and video: pacing, signposting → [Week 11 drills · day 6](../../tracks/communication/drills/week-11.md#day-6) <small>`w11-comm-6`</small>

### Sunday 13 Dec · 3h 15m

- [ ] **System Design** · 45 min · Written design: multi-agent platform — agent registry, tool gateway (MCP), memory, orchestration, evals, tenancy, cost controls → [Design a multi-agent platform](../../tracks/ai-system-design/agent-platform.md) <small>`w11-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 011 for capstone: MCP as integration boundary for tools (vs direct SDK clients) → [Enterprise integration patterns](../../tracks/architecture/integration-patterns.md) · [resource](https://adr.github.io) <small>`w11-arch-2`</small>
- [ ] **Staff+** · 30 min · Draft an exec update for your manager's manager on the capstone/AI initiative: 5 bullets, 1 chart, 1 ask → [Communicating with executives & stakeholders](../../tracks/staff-skills/communication-stakeholders.md) <small>`w11-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Saying no without burning bridges → [Week 11 drills · day 7](../../tracks/communication/drills/week-11.md#day-7) <small>`w11-comm-7`</small>
- [ ] **Review** · 60 min · Retro + explain-it-back: interrupt/resume guarantees and when multi-agent is worth it; flashcards on circuit breakers → [Multi-agent systems: when, how, and failure modes](../../tracks/agentic-ai/multi-agent-systems.md) <small>`w11-rev-1`</small>

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
