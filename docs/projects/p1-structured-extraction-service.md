---
title: "P1: Structured extraction service"
tags: [projects, phase-1, agentic-ai, python]
last_reviewed: 2026-09-25
---

# P1: Structured extraction service

!!! abstract "At a glance"
    **Phase:** 1 · **Weeks:** 3–4 (~8 h build over two weekends) · **Feeds:** capstone M2
    **Goal:** A FastAPI service that turns messy operational documents (bill of lading, commercial invoice, SLA/contract clause) into validated Pydantic models with per-field confidence, backed by an eval harness that reports field-level precision/recall/F1.
    **Done when:** `make eval` prints a per-field F1 table, overall F1 >= 0.85 with a local model, and the write-up compares at least 2 models and 2 extraction strategies.

## Why this project

Structured extraction is the most common "boring but valuable" LLM workload in enterprises, and it is the gateway to agents: every tool call is structured output. It forces you to get the fundamentals right early: typed schemas, validation-and-retry, a golden set, and a metric you trust. Interviewers love it because it exposes whether you measure or vibe-check.

## Skills practised

- [Pydantic v2](../tracks/python/pydantic-v2.md): discriminated unions, validators, `Annotated` constraints, JSON Schema generation
- [FastAPI in production](../tracks/python/fastapi-production.md): lifespan, dependency injection, background tasks, error model
- [Prompting and structured outputs](../tracks/agentic-ai/prompting-structured-outputs.md): native JSON-schema mode vs tool-call mode vs prompted JSON; retries on validation errors
- [Pydantic AI](../tracks/agentic-ai/pydantic-ai.md): typed agents, `output_type`, deps, `pydantic_evals`
- [Evals and error analysis](../tracks/agentic-ai/evals-error-analysis.md): golden set design, field-level metrics
- [asyncio](../tracks/python/asyncio-deep.md): bounded concurrency with `TaskGroup` + semaphore for batch extraction
- [Testing with pytest](../tracks/python/testing-pytest.md), [modern tooling](../tracks/python/modern-tooling.md)

## Spec

### API

| Endpoint | Behaviour |
|---|---|
| `POST /v1/extract` | Multipart file or text + `doc_type` (optional; auto-classify if absent). Returns `ExtractionResult{doc_type, data, field_confidence, warnings, model, prompt_version, latency_ms, cost_usd}` |
| `POST /v1/extract/batch` | Up to 50 docs; returns job id; processes with bounded concurrency |
| `GET /v1/jobs/{id}` | Status + results |
| `GET /v1/schemas/{doc_type}` | JSON Schema of the target model |
| `GET /healthz`, `/readyz` | Liveness / model reachability |

### Target schemas (example domain)

```python
from datetime import date
from decimal import Decimal
from typing import Annotated, Literal
from pydantic import BaseModel, Field

ContainerNo = Annotated[str, Field(pattern=r"^[A-Z]{4}\d{7}$")]  # ISO 6346 shape (check digit validated separately)

class Party(BaseModel):
    name: str
    address: str | None = None
    country_code: Annotated[str, Field(min_length=2, max_length=2)] | None = None

class BillOfLading(BaseModel):
    doc_type: Literal["bill_of_lading"] = "bill_of_lading"
    bl_number: str
    shipper: Party
    consignee: Party
    port_of_loading: str
    port_of_discharge: str
    containers: list[ContainerNo]
    gross_weight_kg: Decimal | None = None
    issue_date: date | None = None

class InvoiceLine(BaseModel):
    description: str
    quantity: Decimal
    unit_price: Decimal
    hs_code: str | None = None

class CommercialInvoice(BaseModel):
    doc_type: Literal["commercial_invoice"] = "commercial_invoice"
    invoice_number: str
    currency: Annotated[str, Field(min_length=3, max_length=3)]
    lines: list[InvoiceLine]
    total: Decimal
    # model_validator: sum(lines) == total within tolerance -> else warning, not failure

class SlaClause(BaseModel):
    doc_type: Literal["sla_clause"] = "sla_clause"
    metric: Literal["transit_time", "on_time_delivery", "free_time_days", "other"]
    threshold: str
    penalty: str | None = None
    source_quote: str  # verbatim span, used for grounding checks
```

### Non-functional

- Validation failure → one repair retry with the validation error fed back → then return partial result with `warnings`.
- Works fully offline with Ollama; cloud models behind the same interface via LiteLLM or Pydantic AI model strings.
- Every call emits an OTel span with model, tokens, latency, prompt version.
- No real customer documents: use synthetic docs you generate plus public sample templates.

## Step-by-step plan

| Step | When | What | Output |
|---|---|---|---|
| 1 | Wk 3 Sat (1 h) | Scaffold with uv; FastAPI app; schemas above; `/v1/schemas` | Service boots, schemas render |
| 2 | Wk 3 Sat (1 h) | **Build the golden set first**: 30 docs (10 per type). Generate varied synthetic docs (different layouts, OCR noise, missing fields, two currencies) and hand-label JSON. Store in `evals/golden/extraction/` | `*.pdf` + `*.expected.json` |
| 3 | Wk 3 Sat (1 h) | Baseline extractor: Pydantic AI agent with `output_type=Union[...]` using a local model | First end-to-end result |
| 4 | Wk 3 Sun (1.5 h) | Eval harness: field-level comparison with normalisers (dates, decimals, whitespace, case), list matching (set-based for containers, Hungarian or order-based for invoice lines); per-field P/R/F1 and schema-valid rate | `make eval` table |
| 5 | Wk 4 weekday | Error analysis: read every failure, tag it (OCR, wrong field, hallucinated value, missing, format), count | Failure taxonomy table |
| 6 | Wk 4 Sat (1.5 h) | Improve: (a) classify-then-extract vs single union; (b) native structured output vs tool-call mode; (c) repair retry; (d) few-shot examples; measure each | Ablation table |
| 7 | Wk 4 Sat (1.5 h) | Add batch endpoint with `asyncio.TaskGroup` + semaphore; confidence scoring (logprob-based if available, else self-reported + validator-based heuristics) | Batch works; confidence per field |
| 8 | Wk 4 Sun (1.5 h) | Run 2 models (one local, one cloud cheap tier) × best strategy; write README, 2 ADRs, write-up | Deliverables |

## Acceptance criteria

- [ ] `make eval` reproduces the headline table from a clean clone
- [ ] Overall field F1 >= 0.85 (local model) and schema-valid rate >= 98%
- [ ] Per-field F1 reported; the 3 worst fields have a documented cause
- [ ] Hallucination check: for `SlaClause`, `source_quote` is a verbatim substring of the input in >= 95% of cases
- [ ] Batch of 50 docs completes with concurrency cap respected (test proves max in-flight <= N)
- [ ] p95 latency and cost per document reported per model
- [ ] 2 ADRs: extraction strategy; model choice for cost/quality
- [ ] Unit tests for normalisers and matchers (these are where eval bugs hide)

## Stretch

- Vision path: send page images to a multimodal model vs text-extraction + LLM; compare F1 and cost.
- Port the extractor to Spring AI 2.0 structured output (`entity()` mapping to a Java record) and compare. See [Spring AI fundamentals](../tracks/java-spring-ai/spring-ai-fundamentals.md).
- DSPy signature for the extractor; compare with hand prompt (preview of P5).
- Active-learning loop: low-confidence fields go to a review queue; corrections append to the golden set.

## Deliverables

1. `experiments/p1-extraction/` (or `apps/extractor/` in the capstone repo) with code, tests, eval harness
2. README with architecture diagram and how to run
3. Write-up: *"Measuring structured extraction: what actually moved F1"* with the ablation table
4. ADRs 2 (strategy, model)
5. Rubric self-score in `docs/scorecard.md`

## Rubric

Score with the [generic rubric](rubric.md) plus these project-specific criteria:

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Golden set | < 15 docs or unlabelled | 30 docs, one layout per type | 30+ docs, varied layouts and noise, edge cases | Plus documented labelling guide and inter-annotator check (label twice, a week apart) |
| Metric design | "Looks right" | Exact-match whole doc | Field-level P/R/F1 with normalisers | Plus list-matching, confidence calibration plot, per-field error taxonomy |
| Robustness | Crashes on bad output | Retries blindly | Validation-error-guided repair; partial results | Plus grounding checks and fallbacks by field criticality |
| Experimentation | One config | Two configs, no table | Ablation table with cost + latency | Plus statistical caution (confidence intervals / variance across 3 runs) |
| Service quality | Script only | FastAPI, no tests | Typed, tested, traced, batch with backpressure | Plus load-tested and documented SLOs |

## Resources

| Resource | Why |
|---|---|
| [Pydantic AI docs](https://ai.pydantic.dev/) | Typed agents, output types, evals |
| [Pydantic docs](https://docs.pydantic.dev/) | Validators, JSON Schema |
| [FastAPI docs](https://fastapi.tiangolo.com/) | Lifespan, dependencies, background tasks |
| [Hamel Husain: evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | How to do error analysis before metrics |
| [applied-llms.org](https://applied-llms.org/) | Practical lessons on structured output and evals |
| [LiteLLM docs](https://docs.litellm.ai/) | Swap local/cloud models behind one API |
| [Ollama](https://ollama.com) | Local models |
