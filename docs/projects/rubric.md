---
title: Project rubric
tags: [projects, rubric]
last_reviewed: 2026-09-25
---

# Project rubric

!!! abstract "How to use"
    Score every project (capstone at each milestone, each mini-project at the end) on these **7 dimensions, 1–4**. Record scores and one-line evidence in the capstone repo `docs/scorecard.md`.
    **Phase gate:** average >= 3.0 and no dimension below 2. **Week-24 bar:** capstone average >= 3.5 with Evals and Security at 4.
    Score against *evidence you could show an interviewer*, not intentions. When torn between two levels, pick the lower one.

## Scale meaning

| Score | Label | Meaning |
|---|---|---|
| 1 | Prototype | Works on your machine for the demo path. Would not survive review. |
| 2 | Solid Senior | Clean and working; gaps in rigour (measurement, failure handling, docs). |
| 3 | Strong Senior / emerging Staff | Production-credible: measured, tested, observable, documented decisions. |
| 4 | Staff+ | Could be adopted by another team; trade-offs made explicit; teaches others; anticipates the next scale step. |

## Dimensions

### 1. Code quality

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Scripts/notebooks; no types or tests; secrets in code | Modules, some type hints, happy-path tests, linter configured | `ruff` + `ty`/`mypy` clean, meaningful unit + integration tests (> 70% on core logic), CI green, clear module boundaries, dependency pins via `uv.lock` | Plus property-based or contract tests where valuable, test data builders, fast feedback (< 3 min CI), code a newcomer extends without asking you |

### 2. Architecture

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Everything in one file; LLM calls scattered | Layers exist but leak (framework types in domain, prompts inline) | Hexagonal/ports-and-adapters: domain independent of LLM/vendor SDKs; model aliases; C4 context + container diagrams current | Plus explicit extension points (domain packs, tool manifests), documented quality-attribute trade-offs, a credible "what changes at 10× / 100×" section |

See [hexagonal and clean architecture](../tracks/architecture/hexagonal-clean.md), [documenting architecture](../tracks/architecture/documenting-architecture.md), [AI-native architecture](../tracks/architecture/ai-native-architecture.md).

### 3. Evals

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Manual spot checks ("looks good") | Golden set exists; one aggregate metric; run by hand | Golden set with coverage of failure categories; component-level metrics (retrieval, generation, tools); LLM judges calibrated against own labels; CI gate on regressions | Plus error-analysis-driven taxonomy, online evals from production traces, feedback loop into dataset, variance/CI reporting, eval cost tracked |

See [evals and error analysis](../tracks/agentic-ai/evals-error-analysis.md), [eval tooling](../tracks/agentic-ai/eval-tooling.md).

### 4. Observability

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Print statements | Structured logs; some LLM call logging | End-to-end traces (OTel + Langfuse) across services, tokens/cost/latency per span, prompt versions tagged, PII redacted | Plus SLOs with error budgets, dashboards that answer "why is it slow/expensive/wrong?", alerting, trace-to-eval workflow |

See [LLM observability](../tracks/agentic-ai/llm-observability.md), [observability and SLOs](../tracks/system-design/observability-slos.md), [observability in Python](../tracks/python/observability-python.md).

### 5. Security and safety

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| No auth; tools can do anything; secrets in env files committed | Auth on API; secrets outside repo; basic input validation | Threat model (OWASP LLM + agentic); least-privilege tools; HITL on writes; tenant isolation; red-team suite with results | Plus red-team in CI with tracked ASR, lethal-trifecta analysis, audit trail, accepted-risk register, supply-chain hygiene (pinned images, SBOM/scan) |

See [guardrails and security](../tracks/agentic-ai/guardrails-security.md), [security: authN/Z](../tracks/system-design/security-authn-authz.md).

### 6. Documentation and ADRs

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| No README beyond a title | README with run steps; decisions undocumented | README (problem, diagram, run, evaluate, limits, cost); ADRs for every significant decision with alternatives and consequences; runbook | Plus ADRs cite evidence (eval/benchmark links), superseded ADRs tracked, docs a reviewer can use to onboard in < 30 min |

See [ADRs](../tracks/architecture/adrs.md).

### 7. Write-up clarity

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Diary of what you did | Explains what was built; results without context | Question → method → results table → decision → next steps; readable by a senior peer in 10 min | Publishable: crisp thesis, honest limitations, visuals, one insight a reader could not get elsewhere; you could present it as a 15-min talk |

See [communication with stakeholders](../tracks/staff-skills/communication-stakeholders.md), [design docs and RFCs](../tracks/staff-skills/design-docs-rfcs.md).

## Scorecard template

Copy into `docs/scorecard.md` in the capstone repo.

| Project / milestone | Date | Code | Arch | Evals | Obs | Security | Docs/ADRs | Write-up | Avg | Lowest → action |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 Skeleton | | | | | | | | | | |
| P1 Extraction | | | | | | | | | | |
| M3 Hybrid RAG / P2 | | | | | | | | | | |
| M4 Agent / P3 | | | | | | | | | | |
| M5 Hardening / P4 | | | | | | | | | | |
| P5 Optimise & serve | | | | | | | | | | |
| P6 Distributed lab | | | | | | | | | | |
| M8 Final | | | | | | | | | | |

## Getting an honest score

- **Self-score, then get one external score.** Ask a peer, or use an AI reviewer with the prompt below; take the lower of the two when they differ by more than 1.
- **Evidence column is mandatory.** "Evals = 3 because CI run #142 blocked a 5-point faithfulness drop" beats "Evals = 3".
- **Trend matters more than level.** Seeing 2 → 3 → 3.5 across phases is the goal.

??? example "AI reviewer prompt"
    ```text
    You are a Staff engineer reviewing a portfolio project for a Staff/AI-architect candidate.
    Score it strictly on this rubric (1-4 per dimension): code quality, architecture, evals,
    observability, security & safety, documentation & ADRs, write-up clarity.
    <paste rubric tables>
    For each dimension: give the score, quote the specific evidence from the materials below,
    and name the single change that would raise it by one level. If evidence is missing,
    score as if it does not exist. Do not be encouraging; be accurate.
    Materials: <README, ADR list, eval report, CI summary, write-up>
    ```
