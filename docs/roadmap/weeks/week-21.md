---
title: Week 21 — Capstone polish + STAR bank I
week: 21
generated: true
---

# Week 21 — Capstone polish + STAR bank I

!!! abstract "At a glance"
    **Phase 6:** Capstone + Interview Loop · **Starts:** Mon 15 Feb 2027 · **Planned:** 13h 15m

    **Build:** Capstone: deploy to Azure Container Apps + Foundry; end-to-end demo script

## By day

### Monday 15 Feb · 1h 30m

- [ ] **System Design** · 45 min · Timed AI SD mock: enterprise RAG system (redo, compare with week 6 write-up) → [Design an enterprise RAG system](../../tracks/ai-system-design/rag-system.md) <small>`w21-sd-1`</small>
- [ ] **DSA** · 25 min · Reverse Bits + Missing Number + Sum of Two Integers → [Math, geometry & bit manipulation](../../tracks/dsa/math-bits.md) · [resource](https://neetcode.io) <small>`w21-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: clean up typing across the capstone (ty strict on core package) → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) <small>`w21-py-1`</small>

### Tuesday 16 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Deployment architecture for Azure: Container Apps, Foundry models, Key Vault, managed identity, Postgres Flexible Server + pgvector → [Managed platforms: Microsoft Foundry, Bedrock AgentCore](../../tracks/agentic-ai/managed-agent-platforms.md) · [resource](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) <small>`w21-ai-1`</small>
- [ ] **DSA** · 30 min · Pow(x, n) + Multiply Strings → [Math, geometry & bit manipulation](../../tracks/dsa/math-bits.md) · [resource](https://neetcode.io) <small>`w21-dsa-2`</small>

### Wednesday 17 Feb · 1h 30m

- [ ] **DSA** · 25 min · LLD: LRU cache + TTL cache, thread-safe (threading.Lock) → [Concurrency & low-level design problems (LRU, rate limiter, parking lot)](../../tracks/dsa/concurrency-lld.md) · [resource](https://www.techinterviewhandbook.org) <small>`w21-dsa-3`</small>
- [ ] **Architecture** · 45 min · arc42 full doc for capstone (sections 1-12, trimmed) + C4 diagrams updated → [C4, arc42 & diagrams as code](../../tracks/architecture/documenting-architecture.md) · [resource](https://arc42.org) <small>`w21-arch-1`</small>
- [ ] **Python** · 20 min · Rep: raise coverage on domain layer to 90% with property tests → [Testing: pytest, fixtures, Hypothesis, testcontainers](../../tracks/python/testing-pytest.md) <small>`w21-py-2`</small>

### Thursday 18 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Production checklist pass 2: close every red item (rollback, cost caps, retention, runbook) → [Shipping LLM features to production: the checklist](../../tracks/agentic-ai/production-checklist.md) <small>`w21-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Deploy the Spring AI MCP server to Azure Container Apps with managed identity → [Tool calling & MCP servers in Spring AI](../../tracks/java-spring-ai/spring-ai-tools-mcp.md) <small>`w21-java-1`</small>

### Friday 19 Feb · 1h 30m

- [ ] **System Design** · 45 min · Caching + consistency deep-dive questions drill (10 L3 questions out loud) → [Caching strategies](../../tracks/system-design/caching.md) <small>`w21-sd-2`</small>
- [ ] **DSA** · 25 min · LLD: rate limiter (token bucket) with concurrency tests → [Concurrency & low-level design problems (LRU, rate limiter, parking lot)](../../tracks/dsa/concurrency-lld.md) <small>`w21-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: FastAPI production config: workers, timeouts, graceful shutdown → [FastAPI for production](../../tracks/python/fastapi-production.md) <small>`w21-py-3`</small>

### Saturday 20 Feb · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: deploy orchestrator + MCP servers to Azure Container Apps via IaC (Bicep/Terraform); smoke evals against the deployed stack → [Shipping LLM features to production: the checklist](../../tracks/agentic-ai/production-checklist.md) · [resource](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) <small>`w21-ai-3`</small>
- [ ] **DSA** · 30 min · LLD: bounded blocking queue / producer-consumer (Condition) → [Concurrency & low-level design problems (LRU, rate limiter, parking lot)](../../tracks/dsa/concurrency-lld.md) <small>`w21-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Java README + architecture notes for the MCP server → [Spring AI 2.0 fundamentals: ChatClient, advisors, structured output](../../tracks/java-spring-ai/spring-ai-fundamentals.md) <small>`w21-java-2`</small>

### Sunday 21 Feb · 2h 45m

- [ ] **System Design** · 45 min · Written design: capstone architecture as an interview answer — 2-page 'design a multi-agent ops platform' doc → [Design a multi-agent platform](../../tracks/ai-system-design/agent-platform.md) <small>`w21-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 021 for capstone: Azure deployment topology (Container Apps + Foundry + managed identity) → [C4, arc42 & diagrams as code](../../tracks/architecture/documenting-architecture.md) · [resource](https://adr.github.io) <small>`w21-arch-2`</small>
- [ ] **Staff+** · 30 min · STAR bank part 1: 6 stories (conflict, influence, failure, ambiguity, technical leadership, mentoring) in docs/interviews/star-bank.md → [Behavioral & Staff interviews: STAR stories bank](../../tracks/staff-skills/behavioral-interviews.md) <small>`w21-staff-1`</small>
- [ ] **Review** · 60 min · Explain-it-back: your capstone architecture in 5 min to a 'VP' audience; flashcards on LLD patterns → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) <small>`w21-rev-1`</small>

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
