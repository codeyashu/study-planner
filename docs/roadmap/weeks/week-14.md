---
title: Week 14 — Cost, latency, routing
week: 14
generated: true
---

# Week 14 — Cost, latency, routing

!!! abstract "At a glance"
    **Phase 4:** Production & AI Architecture · **Starts:** Mon 28 Dec 2026 · **Planned:** 16h 45m

    **Build:** Capstone: LiteLLM routing (cheap → strong escalation), semantic + prompt caching, streaming latency budget

## By day

### Monday 28 Dec · 2h 00m

- [ ] **System Design** · 45 min · SLOs, SLIs, error budgets, burn-rate alerting — define SLOs for the capstone (latency, success, eval-quality SLO) → [Observability, SLOs & error budgets](../../tracks/system-design/observability-slos.md) <small>`w14-sd-1`</small>
- [ ] **DSA** · 25 min · Redundant Connection (union-find) → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w14-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: OTel metrics (histograms for token usage, latency) exported to Langfuse/Prometheus → [Observability in Python: structlog, OpenTelemetry](../../tracks/python/observability-python.md) <small>`w14-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Degrees of certainty: modals and adverbs → [Week 14 drills · day 1](../../tracks/communication/drills/week-14.md#day-1) <small>`w14-comm-1`</small>

### Tuesday 29 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · Cost & latency levers: prompt caching, semantic caching, batching, streaming, speculative/parallel calls — build a latency budget per node → [Cost & latency optimization: caching, batching, streaming](../../tracks/agentic-ai/cost-latency-optimization.md) · [resource](https://applied-llms.org/) <small>`w14-ai-1`</small>
- [ ] **DSA** · 30 min · Word Ladder → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w14-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Negotiation vocabulary: concession, leverage, deadlock → [Week 14 drills · day 2](../../tracks/communication/drills/week-14.md#day-2) <small>`w14-comm-2`</small>

### Wednesday 30 Dec · 2h 00m

- [ ] **DSA** · 25 min · Network Delay Time (Dijkstra) → [Advanced graphs: Dijkstra, MST, Bellman-Ford](../../tracks/dsa/advanced-graphs.md) · [resource](https://neetcode.io) <small>`w14-dsa-3`</small>
- [ ] **Architecture** · 45 min · C4 model + arc42: draw capstone context, container, component diagrams as code (Structurizr DSL or Mermaid) → [C4, arc42 & diagrams as code](../../tracks/architecture/documenting-architecture.md) · [resource](https://c4model.com) <small>`w14-arch-1`</small>
- [ ] **Python** · 20 min · Rep: async token-bucket rate limiter for provider calls → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w14-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Handling pushback live → [Week 14 drills · day 3](../../tracks/communication/drills/week-14.md#day-3) <small>`w14-comm-3`</small>

### Thursday 31 Dec · 2h 00m

- [ ] **Agentic AI** · 60 min · Model selection & routing: cascades, classifier routers, fallbacks; LiteLLM router config with budgets → [Model selection, routing & gateways (LiteLLM)](../../tracks/agentic-ai/model-routing-gateways.md) · [resource](https://docs.litellm.ai/) <small>`w14-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Export Spring AI OTel traces to Langfuse; align attributes with GenAI semconv → [Observability & testing: Micrometer, OTel, Testcontainers](../../tracks/java-spring-ai/observability-testing.md) · [resource](https://langfuse.com/docs) <small>`w14-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Negotiation phrasal verbs: hold out, give in, back down → [Week 14 drills · day 4](../../tracks/communication/drills/week-14.md#day-4) <small>`w14-comm-4`</small>

### Friday 01 Jan · 2h 00m

- [ ] **System Design** · 45 min · LLM capacity & cost planning: tokens/s, TTFT, concurrency, $ per resolved incident — spreadsheet model → [LLM capacity, latency & cost planning](../../tracks/ai-system-design/capacity-cost-planning.md) <small>`w14-sd-2`</small>
- [ ] **DSA** · 25 min · Min Cost to Connect All Points (Prim/Kruskal) → [Advanced graphs: Dijkstra, MST, Bellman-Ford](../../tracks/dsa/advanced-graphs.md) · [resource](https://neetcode.io) <small>`w14-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: snapshot tests for prompts + cost assertions in pytest → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w14-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Writing a proposal → [Week 14 drills · day 5](../../tracks/communication/drills/week-14.md#day-5) <small>`w14-comm-5`</small>

### Saturday 02 Jan · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: LiteLLM proxy in docker-compose (Ollama + 2 hosted models), cascade routing with eval-guarded escalation, prompt caching; report cost/latency before vs after → [Model selection, routing & gateways (LiteLLM)](../../tracks/agentic-ai/model-routing-gateways.md) · [resource](https://docs.litellm.ai/) <small>`w14-ai-3`</small>
- [ ] **DSA** · 30 min · Cheapest Flights Within K Stops (Bellman-Ford / BFS with stops) → [Advanced graphs: Dijkstra, MST, Bellman-Ford](../../tracks/dsa/advanced-graphs.md) · [resource](https://neetcode.io) <small>`w14-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring AI guardrail advisor (input/output check) in the Java service → [Agentic patterns with Spring AI](../../tracks/java-spring-ai/spring-ai-agents.md) <small>`w14-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Handling pushback live → [Week 14 drills · day 6](../../tracks/communication/drills/week-14.md#day-6) <small>`w14-comm-6`</small>

### Sunday 03 Jan · 3h 15m

- [ ] **System Design** · 45 min · Written design: payment system — idempotency, ledger (double-entry), exactly-once illusions, reconciliation, PSP integration → [Payment system](../../tracks/system-design/case-studies/payment-system.md) <small>`w14-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 014 for capstone: LiteLLM as model gateway (vs custom router vs managed gateway) → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) · [resource](https://adr.github.io) <small>`w14-arch-2`</small>
- [ ] **Staff+** · 30 min · Artifact: technical strategy doc (2-3 pages) — 'AI agents for operations: diagnosis, guiding policies, coherent actions' → [Writing engineering strategy & vision](../../tracks/staff-skills/technical-strategy.md) · [resource](https://lethain.com) <small>`w14-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Negotiation practice → [Week 14 drills · day 7](../../tracks/communication/drills/week-14.md#day-7) <small>`w14-comm-7`</small>
- [ ] **Review** · 60 min · Run a mock architecture review of the capstone C4 docs + ADRs with a peer/AI reviewer: checklist, risks, decision log; flashcards on SLOs and graph algorithms → [Running architecture reviews & guilds](../../tracks/staff-skills/architecture-reviews.md) <small>`w14-rev-1`</small>

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
