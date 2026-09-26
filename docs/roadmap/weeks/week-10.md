---
title: Week 10 — MCP + Pydantic AI sub-agents
week: 10
generated: true
---

# Week 10 — MCP + Pydantic AI sub-agents

!!! abstract "At a glance"
    **Phase 3:** Agents + Protocols · **Starts:** Mon 30 Nov 2026 · **Planned:** 16h 45m

    **Build:** Capstone: Python MCP server (runbooks, service status) + Pydantic AI sub-agents inside LangGraph nodes

## By day

### Monday 30 Nov · 2h 00m

- [ ] **System Design** · 45 min · Retries, exponential backoff with jitter, retry budgets — Marc Brooker on retries and timeouts → [Reliability: retries, backoff, circuit breakers, bulkheads](../../tracks/system-design/reliability-patterns.md) · [resource](https://brooker.co.za/blog/) <small>`w10-sd-1`</small>
- [ ] **DSA** · 25 min · Implement Trie (Prefix Tree) → [Tries](../../tracks/dsa/tries.md) · [resource](https://neetcode.io) <small>`w10-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: repository + UoW for agent run records; keep LangGraph state separate from domain state → [Architecture patterns in Python (repository, UoW, message bus)](../../tracks/python/architecture-patterns-python.md) · [resource](https://www.cosmicpython.com/) <small>`w10-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Inversion and emphasis structures → [Week 10 drills · day 1](../../tracks/communication/drills/week-10.md#day-1) <small>`w10-comm-1`</small>

### Tuesday 01 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · MCP spec 2026-07-28: tools/resources/prompts, Streamable HTTP, stateless core, Tasks, OAuth/OIDC hardening — HF MCP course unit 1-2 → [Model Context Protocol (MCP)](../../tracks/agentic-ai/mcp.md) · [resource](https://modelcontextprotocol.io/specification/2026-07-28) <small>`w10-ai-1`</small>
- [ ] **DSA** · 30 min · Design Add and Search Words Data Structure → [Tries](../../tracks/dsa/tries.md) · [resource](https://neetcode.io) <small>`w10-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Strategy vocabulary: leverage, trajectory, headwinds → [Week 10 drills · day 2](../../tracks/communication/drills/week-10.md#day-2) <small>`w10-comm-2`</small>

### Wednesday 02 Dec · 2h 00m

- [ ] **DSA** · 25 min · Word Search II (trie + DFS pruning) → [Tries](../../tracks/dsa/tries.md) · [resource](https://neetcode.io) <small>`w10-dsa-3`</small>
- [ ] **Architecture** · 45 min · CQRS & event sourcing: when it pays off, projections, snapshotting, pitfalls → [CQRS & event sourcing](../../tracks/architecture/cqrs-event-sourcing.md) <small>`w10-arch-1`</small>
- [ ] **Python** · 20 min · Rep: TaskGroup error handling with except* when parallel sub-agents fail → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w10-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Storytelling with data → [Week 10 drills · day 3](../../tracks/communication/drills/week-10.md#day-3) <small>`w10-comm-3`</small>

### Thursday 03 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · Pydantic AI: Agent, deps injection, typed outputs, tools, retries — build the 'root-cause analyst' sub-agent → [Pydantic AI](../../tracks/agentic-ai/pydantic-ai.md) · [resource](https://ai.pydantic.dev/) <small>`w10-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI MCP server: @McpTool / @McpResource annotations, Streamable HTTP transport (SSE deprecated) → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) · [resource](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) <small>`w10-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Vision: north star, the big picture → [Week 10 drills · day 4](../../tracks/communication/drills/week-10.md#day-4) <small>`w10-comm-4`</small>

### Friday 04 Dec · 2h 00m

- [ ] **System Design** · 45 min · Batch vs stream pipelines: Lambda vs Kappa, windowing, late data — for ingesting incident streams into the RAG index → [Batch & stream data pipelines](../../tracks/system-design/data-pipelines.md) <small>`w10-sd-2`</small>
- [ ] **DSA** · 25 min · Kth Largest Element in a Stream + Last Stone Weight → [Heap / priority queue](../../tracks/dsa/heap.md) · [resource](https://neetcode.io) <small>`w10-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: FastAPI BackgroundTasks vs a real queue for long agent runs — implement 202 + status polling → [FastAPI for production](../../tracks/python/fastapi-production.md) <small>`w10-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Writing engineering strategy → [Week 10 drills · day 5](../../tracks/communication/drills/week-10.md#day-5) <small>`w10-comm-5`</small>

### Saturday 05 Dec · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: Python MCP server exposing search_runbooks + get_service_status over Streamable HTTP; LangGraph nodes call it via MCP client; Pydantic AI sub-agent in the analyse node → [Model Context Protocol (MCP)](../../tracks/agentic-ai/mcp.md) · [resource](https://huggingface.co/learn/mcp-course) <small>`w10-ai-3`</small>
- [ ] **DSA** · 30 min · K Closest Points to Origin → [Heap / priority queue](../../tracks/dsa/heap.md) · [resource](https://neetcode.io) <small>`w10-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Start the Spring AI MCP server 'ticketing' (create_ticket, get_ticket) with MCP Java SDK 2.0 → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) <small>`w10-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Storytelling with data → [Week 10 drills · day 6](../../tracks/communication/drills/week-10.md#day-6) <small>`w10-comm-6`</small>

### Sunday 06 Dec · 3h 15m

- [ ] **System Design** · 45 min · Written design: chat/messaging system — delivery guarantees, ordering, presence, fan-out, storage (cf. Discord's message store) → [Chat / messaging system](../../tracks/system-design/case-studies/chat-system.md) <small>`w10-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 010 for capstone: incident timeline as append-only event log with read projection (vs CRUD) → [CQRS & event sourcing](../../tracks/architecture/cqrs-event-sourcing.md) · [resource](https://adr.github.io) <small>`w10-arch-2`</small>
- [ ] **Staff+** · 30 min · Artifact: influence plan — adoption path for an agentic ops tool at work: allies, skeptics, pre-wiring, pilot, success metric → [Influence without authority & alignment](../../tracks/staff-skills/influence-without-authority.md) · [resource](https://noidea.dog/staff-resources) <small>`w10-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Negotiating trade-offs → [Week 10 drills · day 7](../../tracks/communication/drills/week-10.md#day-7) <small>`w10-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back: MCP transports + auth model; flashcards on retries/backoff and tries → [Model Context Protocol (MCP)](../../tracks/agentic-ai/mcp.md) <small>`w10-rev-1`</small>

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
