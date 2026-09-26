---
title: Week 09 — LangGraph orchestrator
week: 9
generated: true
---

# Week 09 — LangGraph orchestrator

!!! abstract "At a glance"
    **Phase 3:** Agents + Protocols · **Starts:** Mon 23 Nov 2026 · **Planned:** 16h 45m

    **Build:** Capstone: LangGraph orchestrator (state, nodes, conditional edges, Postgres checkpointer)

## By day

### Monday 23 Nov · 2h 00m

- [ ] **System Design** · 45 min · Kafka internals: log, partitions, consumer groups, offsets, ordering guarantees → [Message queues & streaming (Kafka)](../../tracks/system-design/messaging-streaming.md) <small>`w09-sd-1`</small>
- [ ] **DSA** · 25 min · Count Good Nodes in Binary Tree + Validate Binary Search Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w09-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: async generators to stream LangGraph events through FastAPI → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w09-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Active vs passive voice, and when to use each → [Week 09 drills · day 1](../../tracks/communication/drills/week-09.md#day-1) <small>`w09-comm-1`</small>

### Tuesday 24 Nov · 2h 00m

- [ ] **Agentic AI** · 60 min · LangChain Academy 'Intro to LangGraph' modules 1-2: StateGraph, reducers, conditional edges, checkpointers → [LangGraph: graphs, state, checkpoints](../../tracks/agentic-ai/langgraph.md) · [resource](https://academy.langchain.com/courses/intro-to-langgraph) <small>`w09-ai-1`</small>
- [ ] **DSA** · 30 min · Kth Smallest Element in a BST → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w09-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Precision with numbers: roughly, approximately, marginally, materially → [Week 09 drills · day 2](../../tracks/communication/drills/week-09.md#day-2) <small>`w09-comm-2`</small>

### Wednesday 25 Nov · 2h 00m

- [ ] **DSA** · 25 min · Construct Binary Tree from Preorder and Inorder Traversal → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w09-dsa-3`</small>
- [ ] **Architecture** · 45 min · Sagas (orchestration vs choreography) + transactional outbox — microservices.io patterns → [Sagas, outbox & distributed transactions](../../tracks/architecture/sagas-outbox.md) · [resource](https://microservices.io) <small>`w09-arch-1`</small>
- [ ] **Python** · 20 min · Rep: Pydantic TypeAdapter + model_validate_json performance on large tool payloads → [Pydantic v2 in depth](../../tracks/python/pydantic-v2.md) <small>`w09-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Question intonation and turn-taking → [Week 09 drills · day 3](../../tracks/communication/drills/week-09.md#day-3) <small>`w09-comm-3`</small>

### Thursday 26 Nov · 2h 00m

- [ ] **Agentic AI** · 60 min · LangGraph 1.x deep dive: persistence, threads, time travel, streaming modes; rebuild the triage router as a graph → [LangGraph: graphs, state, checkpoints](../../tracks/agentic-ai/langgraph.md) · [resource](https://academy.langchain.com/courses/intro-to-langgraph) <small>`w09-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI tool calling: @Tool methods, ToolCallback, returnDirect — expose service-status as a tool → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) · [resource](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) <small>`w09-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Project phrasal verbs: roll out, scale up, sign off → [Week 09 drills · day 4](../../tracks/communication/drills/week-09.md#day-4) <small>`w09-comm-4`</small>

### Friday 27 Nov · 2h 00m

- [ ] **System Design** · 45 min · Delivery semantics: at-least-once + idempotent consumers, transactional/exactly-once in Kafka and its limits → [Message queues & streaming (Kafka)](../../tracks/system-design/messaging-streaming.md) <small>`w09-sd-2`</small>
- [ ] **DSA** · 25 min · Binary Tree Maximum Path Sum → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w09-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: generator send()/close() and yield from — build a lazy trace reader → [Iterators, generators & context managers](../../tracks/python/generators-context-managers.md) <small>`w09-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Blameless postmortem prose → [Week 09 drills · day 5](../../tracks/communication/drills/week-09.md#day-5) <small>`w09-comm-5`</small>

### Saturday 28 Nov · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: LangGraph orchestrator (classify → retrieve → act → draft) with PostgresSaver checkpointer and streaming to FastAPI SSE → [LangGraph: graphs, state, checkpoints](../../tracks/agentic-ai/langgraph.md) · [resource](https://academy.langchain.com/courses/intro-to-langgraph) <small>`w09-ai-3`</small>
- [ ] **DSA** · 30 min · Serialize and Deserialize Binary Tree → [Trees: DFS, BFS, BST](../../tracks/dsa/trees.md) · [resource](https://neetcode.io) <small>`w09-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI MCP client: connect a ChatClient to an existing MCP server (filesystem) over stdio → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) <small>`w09-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Question intonation and turn-taking → [Week 09 drills · day 6](../../tracks/communication/drills/week-09.md#day-6) <small>`w09-comm-6`</small>

### Sunday 29 Nov · 3h 15m

- [ ] **System Design** · 45 min · Written design: notification system — channels, templating, preferences, rate limiting, retries, dedupe → [Notification system](../../tracks/system-design/case-studies/notification-system.md) <small>`w09-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 009 for capstone: outbox for ticket-creation side effects triggered by the agent graph → [Sagas, outbox & distributed transactions](../../tracks/architecture/sagas-outbox.md) · [resource](https://adr.github.io) <small>`w09-arch-2`</small>
- [ ] **Staff+** · 30 min · Read lethain on influence/alignment; list stakeholders for adopting the capstone at work and what each cares about → [Influence without authority & alignment](../../tracks/staff-skills/influence-without-authority.md) · [resource](https://lethain.com) <small>`w09-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: De-escalating conflict → [Week 09 drills · day 7](../../tracks/communication/drills/week-09.md#day-7) <small>`w09-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back: LangGraph state + reducers + checkpoints; flashcards on Kafka semantics and sagas → [LangGraph: graphs, state, checkpoints](../../tracks/agentic-ai/langgraph.md) <small>`w09-rev-1`</small>

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
