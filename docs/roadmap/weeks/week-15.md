---
title: Week 15 — Managed platforms & production checklist
week: 15
generated: true
---

# Week 15 — Managed platforms & production checklist

!!! abstract "At a glance"
    **Phase 4:** Production & AI Architecture · **Starts:** Mon 04 Jan 2027 · **Planned:** 13h 15m

    **Build:** Capstone: Microsoft Foundry Agent Service spike + production-readiness checklist pass

## By day

### Monday 04 Jan · 1h 30m

- [ ] **System Design** · 45 min · Zero trust + agent identity: workload identity, per-tool scopes, tenant isolation patterns (silo/pool/bridge) → [Security: authN/Z, OAuth2/OIDC, zero trust, multi-tenancy](../../tracks/system-design/security-authn-authz.md) <small>`w15-sd-1`</small>
- [ ] **DSA** · 25 min · Swim in Rising Water (Dijkstra / binary search + BFS) → [Advanced graphs: Dijkstra, MST, Bellman-Ford](../../tracks/dsa/advanced-graphs.md) · [resource](https://neetcode.io) <small>`w15-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: py-spy / cProfile flame graph of the ingestion pipeline → [Performance & profiling](../../tracks/python/performance-profiling.md) <small>`w15-py-1`</small>

### Tuesday 05 Jan · 1h 30m

- [ ] **Agentic AI** · 60 min · Managed agent platforms: Microsoft Foundry Agent Service (Responses API) vs Bedrock AgentCore — map capstone components to each → [Managed platforms: Microsoft Foundry, Bedrock AgentCore](../../tracks/agentic-ai/managed-agent-platforms.md) · [resource](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) <small>`w15-ai-1`</small>
- [ ] **DSA** · 30 min · Reconstruct Itinerary (Hierholzer) → [Advanced graphs: Dijkstra, MST, Bellman-Ford](../../tracks/dsa/advanced-graphs.md) · [resource](https://neetcode.io) <small>`w15-dsa-2`</small>

### Wednesday 06 Jan · 1h 30m

- [ ] **DSA** · 25 min · Climbing Stairs + Min Cost Climbing Stairs → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w15-dsa-3`</small>
- [ ] **Architecture** · 45 min · Evolutionary architecture: fitness functions — turn eval thresholds, latency budgets and dependency rules into CI checks → [Evolutionary architecture & fitness functions](../../tracks/architecture/evolutionary-architecture.md) <small>`w15-arch-1`</small>
- [ ] **Python** · 20 min · Rep: memray/scalene memory profile of embedding batch job → [Performance & profiling](../../tracks/python/performance-profiling.md) <small>`w15-py-2`</small>

### Thursday 07 Jan · 1h 30m

- [ ] **Agentic AI** · 60 min · Production checklist: evals gate, observability, guardrails, cost caps, fallbacks, rollback, data retention, incident runbook — audit the capstone → [Shipping LLM features to production: the checklist](../../tracks/agentic-ai/production-checklist.md) · [resource](https://applied-llms.org/) <small>`w15-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Secure the Spring AI MCP server with OAuth2 resource server (Spring Security) per MCP authorization spec → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) · [resource](https://modelcontextprotocol.io/specification/2026-07-28) <small>`w15-java-1`</small>

### Friday 08 Jan · 1h 30m

- [ ] **System Design** · 45 min · Quotas for LLM platforms: token-based rate limits per tenant, fairness, burst handling → [Rate limiting & quotas](../../tracks/system-design/rate-limiting.md) <small>`w15-sd-2`</small>
- [ ] **DSA** · 25 min · House Robber + House Robber II → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w15-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: refactor a service layer to use the message bus for side effects → [Architecture patterns in Python (repository, UoW, message bus)](../../tracks/python/architecture-patterns-python.md) · [resource](https://www.cosmicpython.com/) <small>`w15-py-3`</small>

### Saturday 09 Jan · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: run the triage agent on Foundry Agent Service (or MS Agent Framework) against the same eval set; compare quality, latency, cost, ops burden → [Managed platforms: Microsoft Foundry, Bedrock AgentCore](../../tracks/agentic-ai/managed-agent-platforms.md) · [resource](https://learn.microsoft.com/en-us/agent-framework/overview/) <small>`w15-ai-3`</small>
- [ ] **DSA** · 30 min · Longest Palindromic Substring → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w15-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Spring Boot 4 production settings: graceful shutdown, virtual threads flag, actuator probes for Container Apps → [Spring Boot 4 & Spring Framework 7](../../tracks/java-spring-ai/spring-boot-4.md) <small>`w15-java-2`</small>

### Sunday 10 Jan · 2h 45m

- [ ] **System Design** · 45 min · Written design: LLM evaluation & observability platform — trace ingestion, datasets, judges, online evals, dashboards → [Design an LLM evaluation & observability platform](../../tracks/ai-system-design/evaluation-platform.md) · [resource](https://arize.com/docs/phoenix) <small>`w15-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 015 for capstone: architectural fitness functions in CI (eval score, p95, import-linter rules) → [Evolutionary architecture & fitness functions](../../tracks/architecture/evolutionary-architecture.md) · [resource](https://adr.github.io) <small>`w15-arch-2`</small>
- [ ] **Staff+** · 30 min · Artifact: tech-debt proposal — inventory, cost of delay, prioritised paydown plan, how you'd get it funded → [Managing technical debt & quality](../../tracks/staff-skills/technical-debt.md) <small>`w15-staff-1`</small>
- [ ] **Review** · 60 min · Explain-it-back: managed vs self-built agent platform trade-offs; flashcards on production checklist items → [Shipping LLM features to production: the checklist](../../tracks/agentic-ai/production-checklist.md) <small>`w15-rev-1`</small>

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
