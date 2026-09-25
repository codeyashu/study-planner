---
title: "P4: LLM gateway and guardrails"
tags: [projects, phase-4, agentic-ai, security, ai-system-design]
last_reviewed: 2026-09-25
---

# P4: LLM gateway and guardrails

!!! abstract "At a glance"
    **Phase:** 4 · **Weeks:** 14–16 (~12 h build) · **Feeds:** capstone M5, ADRs 0011–0013
    **Goal:** Put a production control plane in front of every model call: routing with fallbacks, caching (exact + semantic), per-tenant budgets and rate limits, cost/latency telemetry, and a guardrail layer. Prove it with a **red-team suite** (promptfoo OWASP LLM + agentic presets plus your own domain attacks) running in CI.
    **Done when:** a budget cap demonstrably blocks spend, a provider outage fails over transparently, 0 critical red-team findings remain, and a dashboard shows cost and latency per tenant/model.

## Why this project

Every enterprise that ships more than one LLM feature ends up building an AI gateway, and every agent with tools is a security incident waiting to happen. "Design a multi-tenant LLM gateway" is one of the most common AI system design prompts in 2026, and security questions (prompt injection, excessive agency) are now standard in Staff loops.

## Skills practised

- [Model routing and gateways](../tracks/agentic-ai/model-routing-gateways.md), [cost and latency optimisation](../tracks/agentic-ai/cost-latency-optimization.md)
- [Guardrails and security](../tracks/agentic-ai/guardrails-security.md)
- [Rate limiting](../tracks/system-design/rate-limiting.md), [caching](../tracks/system-design/caching.md), [security: authN/Z and multi-tenancy](../tracks/system-design/security-authn-authz.md)
- [Observability and SLOs](../tracks/system-design/observability-slos.md), [LLM observability](../tracks/agentic-ai/llm-observability.md)
- AI SD: [LLM gateway](../tracks/ai-system-design/llm-gateway.md), [capacity and cost planning](../tracks/ai-system-design/capacity-cost-planning.md)

## Spec

### Gateway capabilities

| Capability | Requirement | Implementation hint |
|---|---|---|
| Model aliases | Apps call `fast`, `smart`, `embed`, `judge`; never raw model IDs | LiteLLM `model_list` |
| Routing | Route by task type + tenant tier; cost-aware (cheap model first, escalate on low confidence) | LiteLLM router + small custom pre-call hook |
| Fallbacks | Provider error / timeout / 429 → next deployment; circuit breaker opens after N failures | LiteLLM fallbacks + cooldowns |
| Caching | Exact-match cache (Redis) for deterministic calls; semantic cache (embedding similarity >= threshold) only for FAQ-style Ask with tenant scoping | Measure hit rate and **false-hit rate** |
| Budgets | Per tenant and per virtual key: monthly $ cap, soft alert at 80%, hard 429 at 100% | LiteLLM virtual keys + budgets |
| Rate limits | Token-per-minute and requests-per-minute per tenant | LiteLLM limits or gateway-side token bucket |
| Telemetry | Every call: tenant, alias, model, tokens in/out, cost, latency, cache hit, fallback used | OTel + Langfuse |
| Prompt/response logging | PII redacted before persistence; retention policy | Presidio in a callback / collector processor |

### Guardrail layer

| Stage | Control | Blocks |
|---|---|---|
| Input | Prompt-injection classifier (open model or hosted), length limits, allowed languages | Direct injection, jailbreaks, resource abuse |
| Retrieval | Tag retrieved content as untrusted data; strip hidden text/markup; source allow-list | Indirect injection via documents |
| Tool policy | Per-graph tool allow-list; write tools require approval; argument validators (e.g. email domain allow-list) | Excessive agency, data exfiltration |
| Output | Schema validation; citation check; PII/secret detector; toxicity/off-topic | Data leakage, ungrounded claims |
| Memory | Validate before write; provenance; no instructions stored as facts | Memory poisoning |

Design principle: break the **lethal trifecta** (private data + untrusted content + external communication). Any path that has all three requires a human gate.

### Red-team suite

- promptfoo red-team config using the **OWASP LLM Top 10** and **OWASP agentic** presets against the capstone's Ask and Triage endpoints.
- 30+ custom domain attacks: poisoned SOP document with hidden instructions; customer email asking the agent to reveal other customers' shipments; tool-argument smuggling (`"shipment_id": "X; also send to attacker@..."`); cost-exhaustion prompts; cross-tenant retrieval attempts.
- Metrics: attack success rate (ASR) per category, severity, and false-positive rate of guardrails on benign traffic (use your golden set as the benign set).

## Step-by-step plan

| Step | When | What |
|---|---|---|
| 1 | Wk 14 Sat | LiteLLM proxy config: aliases, two providers + Ollama, fallbacks; virtual keys per tenant; load test the proxy overhead |
| 2 | Wk 14 Sun | Threat model the capstone (STRIDE + OWASP LLM/agentic mapping); write ADR 0011 |
| 3 | Wk 15 weekdays | Baseline red-team run *before* guardrails; record ASR |
| 4 | Wk 15 Sat | Implement guardrail stages; tool policy matrix; PII redaction in traces |
| 5 | Wk 15 Sun | Budgets + rate limits + tests (prove 429 at cap); outage drill (block provider A with a fault-injection proxy) |
| 6 | Wk 16 weekdays | Exact + semantic cache; measure hit rate, false-hit rate on a paraphrase set, latency and $ saved |
| 7 | Wk 16 Sat | Re-run red-team; tune; wire promptfoo into nightly CI and a fast subset into PR CI |
| 8 | Wk 16 Sun | Dashboard (Langfuse / Grafana): cost by tenant/model, p95 latency, cache hit, fallback rate; report + ADRs 0012–0013 |

## Acceptance criteria

- [ ] Apps reference only aliases; swapping a model is a config-only change (demonstrated in a PR)
- [ ] Provider outage drill: error rate seen by users < 1% during failover; p95 increase documented
- [ ] Budget test: tenant hits cap → subsequent calls get 429 with a clear error; alert fires at 80%
- [ ] Red-team: 0 critical findings; overall ASR < 5% (M5) with a path to < 2% (M8); guardrail false-positive rate on benign set < 3%
- [ ] Semantic cache false-hit rate < 1% at the chosen threshold, or semantic cache disabled with an ADR explaining why
- [ ] Gateway overhead p95 < 30 ms (excluding model time)
- [ ] PII never appears in stored traces (test with seeded PII)
- [ ] Threat model document mapping each OWASP item to a control or accepted risk

## Stretch

- Learned router: classifier predicts whether the cheap model suffices; measure $ saved vs quality lost (RouteLLM-style).
- Compare LiteLLM with a managed gateway (Azure API Management AI gateway policies or Pydantic AI Gateway): feature matrix + latency.
- Prompt caching (provider-side) for long system prompts: measure savings.
- Signed tool manifests; per-tool OAuth scopes on MCP servers.

## Deliverables

1. `infra/litellm/`, `packages/guardrails/`, `evals/redteam.yaml` merged (capstone M5)
2. Threat model + red-team report (before/after ASR table)
3. Cost/latency dashboard screenshot + description in README
4. ADRs 0011 (guardrail architecture), 0012 (routing/fallback), 0013 (tenancy isolation)
5. Write-up: *"Putting a control plane in front of an agent"*

## Rubric

Generic [rubric](rubric.md) plus:

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Routing & resilience | Single provider | Aliases, manual fallback | Automatic fallback + circuit breaking, drill done | Plus cost-aware routing with measured savings and quality impact |
| Cost governance | No tracking | Cost logged | Per-tenant budgets + rate limits enforced and tested | Plus forecasting, alerts, and unit-economics table ($/case) |
| Threat model | None | Generic list | OWASP LLM + agentic mapped to controls | Plus lethal-trifecta path analysis and accepted-risk register |
| Red-team | Manual pokes | promptfoo preset only | Presets + 30 domain attacks, before/after ASR | Plus in CI, FPR measured on benign set, regression tracked over time |
| Caching | None | Exact cache | Exact + semantic with hit/false-hit metrics | Plus tenant-scoped invalidation strategy and savings analysis |

## Resources

| Resource | Why |
|---|---|
| [LiteLLM docs](https://docs.litellm.ai/) | Proxy, router, virtual keys, budgets |
| [promptfoo OWASP agentic red-team](https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/) | Preset used here |
| [OWASP GenAI Security Project](https://genai.owasp.org/) | LLM Top 10 and agentic Top 10 |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–ASI10 |
| [Simon Willison: the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) :gem: | Clearest framing of agent data exfiltration |
| [Microsoft Presidio](https://microsoft.github.io/presidio/) | PII detection/redaction |
| [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Alternative programmable guardrails |
| [Langfuse docs](https://langfuse.com/docs) | Cost and latency analytics |
