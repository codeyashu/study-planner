---
title: Week 13 — Guardrails & security
week: 13
generated: true
---

# Week 13 — Guardrails & security

!!! abstract "At a glance"
    **Phase 4:** Production & AI Architecture · **Starts:** Mon 21 Dec 2026 · **Planned:** 13h 15m

    **Build:** Capstone: guardrails layer (input/output/tool), prompt-injection red-team suite in CI

## By day

### Monday 21 Dec · 1h 30m

- [ ] **System Design** · 45 min · Rate limiting: token bucket, leaky bucket, sliding window log/counter; distributed limits with Redis + Lua → [Rate limiting & quotas](../../tracks/system-design/rate-limiting.md) <small>`w13-sd-1`</small>
- [ ] **DSA** · 25 min · Max Area of Island + Clone Graph → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w13-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: structlog JSON logging with contextvars (request_id, tenant, run_id) → [Observability in Python: structlog, OpenTelemetry](../../tracks/python/observability-python.md) <small>`w13-py-1`</small>

### Tuesday 22 Dec · 1h 30m

- [ ] **Agentic AI** · 60 min · OWASP Top 10 for LLM Apps + OWASP Agentic Top 10 2026 (ASI01-ASI10) — threat-model the capstone per item → [Guardrails & security: OWASP LLM/Agentic Top 10, prompt injection](../../tracks/agentic-ai/guardrails-security.md) · [resource](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) <small>`w13-ai-1`</small>
- [ ] **DSA** · 30 min · Pacific Atlantic Water Flow → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w13-dsa-2`</small>

### Wednesday 23 Dec · 1h 30m

- [ ] **DSA** · 25 min · Surrounded Regions + Rotting Oranges (multi-source BFS) → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w13-dsa-3`</small>
- [ ] **Architecture** · 45 min · AI-native architecture: LLMs as non-deterministic components — deterministic shells, eval gates, fallbacks, human override (FoSA 2e GenAI chapters) → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) <small>`w13-arch-1`</small>
- [ ] **Python** · 20 min · Rep: OpenTelemetry manual spans around tool calls with GenAI attributes → [Observability in Python: structlog, OpenTelemetry](../../tracks/python/observability-python.md) · [resource](https://github.com/open-telemetry/semantic-conventions-genai) <small>`w13-py-2`</small>

### Thursday 24 Dec · 1h 30m

- [ ] **Agentic AI** · 60 min · Lethal trifecta (private data + untrusted content + exfiltration): find every trifecta path in the capstone and design mitigations → [Guardrails & security: OWASP LLM/Agentic Top 10, prompt injection](../../tracks/agentic-ai/guardrails-security.md) · [resource](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) <small>`w13-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Micrometer observations for Spring AI ChatClient/VectorStore; view token metrics → [Observability & testing: Micrometer, OTel, Testcontainers](../../tracks/java-spring-ai/observability-testing.md) <small>`w13-java-1`</small>

### Friday 25 Dec · 1h 30m

- [ ] **System Design** · 45 min · AuthN/Z: OAuth2/OIDC flows, token exchange, multi-tenant isolation, zero trust — how MCP OAuth fits → [Security: authN/Z, OAuth2/OIDC, zero trust, multi-tenancy](../../tracks/system-design/security-authn-authz.md) <small>`w13-sd-2`</small>
- [ ] **DSA** · 25 min · Course Schedule + Course Schedule II (topological sort) → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w13-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: FastAPI middleware for OIDC JWT validation + tenant resolution → [FastAPI for production](../../tracks/python/fastapi-production.md) <small>`w13-py-3`</small>

### Saturday 26 Dec · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: guardrails (input classification, tool allow-lists + arg validation, output PII redaction) + promptfoo OWASP agentic red-team preset in CI → [Guardrails & security: OWASP LLM/Agentic Top 10, prompt injection](../../tracks/agentic-ai/guardrails-security.md) · [resource](https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/) <small>`w13-ai-3`</small>
- [ ] **DSA** · 30 min · Number of Connected Components (union-find) + Graph Valid Tree → [Graphs: BFS, DFS, topological sort, union-find](../../tracks/dsa/graphs.md) · [resource](https://neetcode.io) <small>`w13-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Write the polyglot rationale: which capstone parts belong in Java vs Python and why → [Java vs Python for AI: polyglot architecture decisions](../../tracks/java-spring-ai/polyglot-ai-architecture.md) <small>`w13-java-2`</small>

### Sunday 27 Dec · 2h 45m

- [ ] **System Design** · 45 min · Written design: multi-tenant LLM gateway — auth, quotas by tokens, routing, caching, fallbacks, audit, cost attribution → [Design a multi-tenant LLM gateway](../../tracks/ai-system-design/llm-gateway.md) · [resource](https://docs.litellm.ai/) <small>`w13-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 013 for capstone: guardrail placement (gateway vs in-graph vs tool server) and fail-closed policy → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) · [resource](https://adr.github.io) <small>`w13-arch-2`</small>
- [ ] **Staff+** · 30 min · Read lethain on writing engineering strategy (diagnosis, policy, actions); pick a strategy topic from work → [Writing engineering strategy & vision](../../tracks/staff-skills/technical-strategy.md) · [resource](https://lethain.com) <small>`w13-staff-1`</small>
- [ ] **Review** · 60 min · Explain-it-back: OWASP agentic top risks + lethal trifecta; flashcards on rate limiting algorithms → [Guardrails & security: OWASP LLM/Agentic Top 10, prompt injection](../../tracks/agentic-ai/guardrails-security.md) <small>`w13-rev-1`</small>

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
