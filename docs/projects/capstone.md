---
title: "Capstone: Agentic Ops Copilot"
tags: [projects, capstone, agentic-ai, architecture]
last_reviewed: 2026-09-25
---

# Capstone: Agentic Ops Copilot

!!! abstract "At a glance"
    **What:** A production-grade, domain-agnostic operations copilot. It triages operational exceptions, answers questions over documents and policies, calls tools in systems of record, and proposes (never silently executes) risky actions.
    **Example domain:** logistics shipment exceptions and trade documents. Swappable via a *domain pack* (IT incident ops, insurance claims, procurement).
    **Duration:** weeks 1–24, milestones M1–M8. **Repo:** `agentic-ops-copilot` (you create it). **Budget:** ~$30–50/month, local-first.
    **Done when:** all M8 acceptance criteria pass, eval gates are enforced in CI, it runs locally with `docker compose up` and on Azure, and 15 ADRs + 2 public write-ups exist.

## 1. Problem

Operations teams (control towers, service desks, claims handlers) spend most of their time on **exception handling**: something deviates from plan, someone has to work out what happened, find the relevant contract/SOP clause, check three systems, decide, and notify people. The knowledge is spread across PDFs, tickets, emails, and people's heads.

In the example domain: a container misses its vessel cut-off; the handler must check the booking, the carrier's schedule, the customer's SLA and the demurrage/detention clause in the contract, then choose between rebooking, notifying the customer, or escalating. That takes 15–40 minutes of swivel-chair work per exception.

**Copilot goal:** cut time-to-decision per exception by more than 50%, with every recommendation grounded in cited sources and every side-effecting action approved by a human.

## 2. Users and jobs-to-be-done

| Persona | Job | What they need from the copilot |
|---|---|---|
| **Ops handler** (primary) | Resolve exceptions quickly and correctly | Triage summary, root-cause hypothesis, cited SOP/contract clauses, a drafted action plan, one-click approve/edit/reject |
| **Team lead** | Keep SLA, spot patterns | Queue view, escalations, weekly pattern report ("30% of delays are from port X") |
| **Knowledge owner** | Keep SOPs and policies current | Ingestion status, stale-document alerts, "questions we couldn't answer" report |
| **Platform/AI engineer** (you) | Run it safely and cheaply | Traces, eval dashboards, cost per request, model routing config, kill switches |
| **Auditor/compliance** | Prove decisions were sound | Immutable audit trail: inputs, retrieved sources, model, prompt version, approver |

## 3. Requirements

### 3.1 Functional

| ID | Requirement |
|---|---|
| F1 | **Ingest** documents (PDF, DOCX, email/EML, HTML) into a hybrid index with metadata (tenant, doc type, effective date, ACL). Incremental re-ingest on change. |
| F2 | **Extract** structured records from documents (e.g. bill of lading, commercial invoice, SLA clauses) into typed Pydantic models, with per-field confidence. |
| F3 | **Ask**: grounded Q&A over the corpus with inline citations; refuses when evidence is insufficient. |
| F4 | **Triage** an exception event: classify, gather context via tools, retrieve policy, produce a structured triage report (severity, hypothesis, evidence, recommended actions). |
| F5 | **Act** via tools (MCP): read-only tools run freely; write tools (rebook, notify customer, open ticket) require **human approval** with a diff/preview. |
| F6 | **Resume**: long-running cases survive restarts; a human can approve hours later and the graph resumes from checkpoint. |
| F7 | **Memory**: per-case working memory, per-user preferences, per-tenant learned facts (with provenance and TTL). |
| F8 | **Feedback**: thumbs up/down + correction on every answer; corrections flow into the eval set after review. |
| F9 | **Multi-tenant**: tenant isolation in retrieval, memory, budgets, and traces. |
| F10 | **Domain packs**: swapping domain = new tools, schemas, prompts, golden set; no orchestrator code changes. |

### 3.2 Non-functional

| Area | Target (M8) | How measured |
|---|---|---|
| Latency: Ask | p50 < 2.5 s to first token, p95 < 6 s full answer | Langfuse/OTel spans, k6 or Locust load test |
| Latency: Triage (no approval wait) | p95 < 20 s end-to-end | Trace duration from event to report |
| Throughput | 5 concurrent triage runs + 20 RPS Ask on a single Container Apps replica set | Load test |
| Cost | <= $0.01 median per Ask, <= $0.05 median per triage (cloud models); $0 local mode | Gateway cost logs per request |
| Monthly spend | <= $50 total (cloud LLM + Azure infra) | Budget alerts in LiteLLM + Azure Cost Management |
| Retrieval quality | recall@10 >= 0.85, MRR@10 >= 0.6 on golden set | Eval suite |
| Answer quality | faithfulness >= 0.90, answer relevancy >= 0.85, citation precision >= 0.9 | DeepEval/Ragas + LLM judge calibrated to your labels (>= 0.8 agreement) |
| Extraction | field-level F1 >= 0.92 on labelled docs | P1 harness |
| Agent quality | task success >= 80%, tool-call correctness >= 95%, zero unapproved write actions | Trajectory evals |
| Safety | 0 critical findings in promptfoo OWASP LLM + agentic red-team; prompt-injection attack success < 2% | Red-team suite in CI |
| Security | OAuth2/OIDC for users and MCP servers; secrets in Key Vault; per-tenant row-level security; PII redaction in traces | Checklist + tests |
| Availability | 99.5% monthly for Ask (portfolio target); graceful degradation to "retrieval-only" if LLM provider down | Synthetic probe |
| Observability | 100% of requests traced with OTel GenAI attributes; prompt versions tagged | Langfuse |
| Reproducibility | `docker compose up` from clean clone < 10 min; all evals runnable offline with Ollama | README check |

## 4. Architecture

### 4.1 C4 context

```mermaid
flowchart TB
    handler([Ops handler])
    lead([Team lead])
    eng([AI/platform engineer])
    subgraph copilot[Agentic Ops Copilot]
        sys[Copilot system]
    end
    tms[(Shipment/TMS API<br/>system of record)]
    ticket[(Ticketing system)]
    mail[(Email / notification service)]
    docs[(Document stores<br/>SharePoint, S3, file drops)]
    llm[[LLM providers<br/>Microsoft Foundry, Anthropic/OpenAI, Ollama]]
    idp[[Identity provider<br/>Entra ID / OIDC]]

    handler -->|asks, approves actions| sys
    lead -->|reviews queue, reports| sys
    eng -->|configures, observes| sys
    sys -->|read/write via MCP tools| tms
    sys -->|create/update tickets| ticket
    sys -->|send approved notifications| mail
    sys -->|ingest| docs
    sys -->|completions, embeddings| llm
    sys -->|authN/Z| idp
```

### 4.2 C4 container

```mermaid
flowchart TB
    ui[Web UI<br/>minimal chat + approval inbox<br/>later AG-UI]
    gw[API gateway service<br/>FastAPI: auth, tenancy, rate limits, SSE streaming]
    orch[Orchestrator<br/>LangGraph: triage/ask graphs,<br/>checkpoints, HITL interrupts]
    subs[Sub-agents<br/>Pydantic AI: extractor, retriever-QA,<br/>planner, notifier-drafter]
    guard[Guardrails layer<br/>input/output filters, PII redaction,<br/>tool-permission policy]
    llmgw[LLM gateway<br/>LiteLLM proxy: routing, fallbacks,<br/>caching, budgets]
    mcpPy[MCP server: ops-tools<br/>Python, FastMCP SDK]
    mcpJ[MCP server: shipment-tools<br/>Spring AI 2.0, @McpTool]
    ingest[Ingestion worker<br/>parse, chunk, embed, extract]
    pg[(PostgreSQL 16+ with pgvector<br/>chunks, BM25/FTS, checkpoints,<br/>memory, audit log)]
    obs[Langfuse + OTel Collector<br/>traces, scores, prompt versions]
    evals[Eval suite<br/>promptfoo + DeepEval in CI]
    models[[Ollama local / Foundry / other providers]]

    ui --> gw --> orch
    orch --> subs
    orch --> guard
    subs --> guard
    guard --> llmgw --> models
    orch -->|MCP Streamable HTTP| mcpPy
    orch -->|MCP Streamable HTTP| mcpJ
    subs --> pg
    orch --> pg
    ingest --> pg
    ingest --> llmgw
    gw -.-> obs
    orch -.-> obs
    llmgw -.-> obs
    evals --> gw
```

### 4.3 Triage flow (LangGraph)

```mermaid
stateDiagram-v2
    [*] --> classify
    classify --> gather_context: known exception type
    classify --> ask_human: low confidence
    gather_context --> retrieve_policy
    retrieve_policy --> plan_actions
    plan_actions --> guard_check
    guard_check --> await_approval: write actions present
    guard_check --> report: read-only plan
    await_approval --> execute: approved
    await_approval --> plan_actions: edited / rejected with reason
    execute --> verify
    verify --> report
    ask_human --> gather_context
    report --> [*]
```

Every node transition is checkpointed to Postgres, so `await_approval` can sit for hours and survive redeploys (see [durable execution and HITL](../tracks/agentic-ai/durable-execution-hitl.md)).

## 5. Components

| Component | Tech (as of Sept 2026) | Responsibilities | Key design notes | Learn |
|---|---|---|---|---|
| **API gateway** | FastAPI, Pydantic v2, uvicorn, SSE | AuthN (OIDC JWT), tenant resolution, request validation, per-tenant rate limits, streaming, idempotency keys on action endpoints | Hexagonal: routes call application services; no LLM code here | [FastAPI in production](../tracks/python/fastapi-production.md), [API design](../tracks/system-design/api-design.md) |
| **Orchestrator** | LangGraph 1.x, Postgres checkpointer | Ask and Triage graphs; state schema; interrupts for HITL; retries per node; time-travel debugging | Keep graphs small and explicit (workflow > autonomous agent where possible); node = pure-ish function over typed state | [LangGraph](../tracks/agentic-ai/langgraph.md), [agent patterns](../tracks/agentic-ai/agent-patterns.md) |
| **Sub-agents** | Pydantic AI (typed outputs, deps injection, `pydantic_evals`) | Extractor, Retriever-QA, Planner, Notification drafter | Each returns a Pydantic model; no free text crosses agent boundaries | [Pydantic AI](../tracks/agentic-ai/pydantic-ai.md), [structured outputs](../tracks/agentic-ai/prompting-structured-outputs.md) |
| **MCP server: ops-tools (Python)** | MCP Python SDK (FastMCP), Streamable HTTP | `search_documents`, `get_sop`, `create_ticket`, `draft_email` | Tools declare read/write; write tools return a *proposal* id, execution is a separate approved call | [MCP](../tracks/agentic-ai/mcp.md), [tool calling](../tracks/agentic-ai/tool-calling.md) |
| **MCP server: shipment-tools (Java)** | Spring Boot 4 + Spring AI 2.0 `@McpTool`, MCP Java SDK 2.0 | `get_shipment`, `get_vessel_schedule`, `propose_rebooking` against a mock TMS | Demonstrates polyglot agents; OAuth2 resource server | [Spring AI tools and MCP](../tracks/java-spring-ai/spring-ai-tools-mcp.md), [polyglot AI architecture](../tracks/java-spring-ai/polyglot-ai-architecture.md) |
| **Hybrid RAG** | Postgres + pgvector (HNSW) + Postgres FTS (or ParadeDB/pg_search BM25), reciprocal rank fusion, cross-encoder reranker (bge-reranker local / Cohere or Foundry-hosted) | Retrieve top-k with tenant + ACL + effective-date filters; rerank; cite | Chunking chosen by P2 ablation, not by gut | [hybrid search and reranking](../tracks/agentic-ai/hybrid-search-reranking.md), [vector databases](../tracks/agentic-ai/vector-databases.md), [advanced RAG](../tracks/agentic-ai/advanced-rag.md) |
| **Ingestion worker** | Python async worker, Docling/unstructured-style parsers, queue table (`SKIP LOCKED`) or Redis Streams | Parse, chunk, embed, extract, upsert; outbox events | Idempotent by content hash; re-embed on model change via versioned embedding column | [data pipelines](../tracks/system-design/data-pipelines.md), [sagas and outbox](../tracks/architecture/sagas-outbox.md) |
| **Observability** | Langfuse (self-hosted in compose), OpenTelemetry SDK + Collector, GenAI semantic conventions (Development status as of Jul 2026) | Traces across gateway → graph → tools → LLM; token/cost; prompt versions; user feedback scores | Redact PII before export; sample 100% in dev, tail-sample errors + 10% in prod | [LLM observability](../tracks/agentic-ai/llm-observability.md), [observability and SLOs](../tracks/system-design/observability-slos.md) |
| **Eval suite** | promptfoo (assertions + red-team), DeepEval (RAG + agent metrics), Ragas (optional), pytest | Offline regression on golden sets; CI gate; nightly larger run; online scores from sampled traces | Judges are calibrated against your own labels before trusted | [eval tooling](../tracks/agentic-ai/eval-tooling.md), [evals and error analysis](../tracks/agentic-ai/evals-error-analysis.md) |
| **Guardrails** | Input: prompt-injection classifier + allow-listed tools per graph; output: schema validation, citation check, PII (Presidio); policy: tool permission matrix | Block, redact, or route to human | Design against the lethal trifecta: never combine untrusted content + private data + exfiltration channel without a human gate | [guardrails and security](../tracks/agentic-ai/guardrails-security.md) |
| **LLM gateway** | LiteLLM proxy | Model aliases (`fast`, `smart`, `embed`), fallbacks, retries, per-tenant/per-key budgets, caching, cost logging | App code references aliases only; model swap = config change | [model routing and gateways](../tracks/agentic-ai/model-routing-gateways.md), [cost and latency](../tracks/agentic-ai/cost-latency-optimization.md) |
| **Memory** | Postgres tables (episodic per case, semantic per tenant) first; evaluate Mem0/Letta in M6 | Case scratchpad, user prefs, tenant facts with provenance + TTL | Memory writes go through the same guardrails (memory poisoning is an OWASP agentic risk) | [memory systems](../tracks/agentic-ai/memory-systems.md), [context engineering](../tracks/agentic-ai/context-engineering.md) |

## 6. Repo layout

```text
agentic-ops-copilot/
  pyproject.toml              # uv workspace root
  uv.lock
  Makefile                    # up, down, test, eval, redteam, lint, seed
  docker-compose.yml          # local stack (below)
  .github/workflows/
    ci.yml                    # lint, type-check, unit tests, eval gate (Ollama or cheap model)
    nightly-evals.yml         # full golden set + red-team, posts scores
    deploy.yml                # build images, deploy to Azure Container Apps
  apps/
    gateway/                  # FastAPI service
    orchestrator/             # LangGraph graphs + Pydantic AI sub-agents
    ingest/                   # ingestion worker
    mcp-ops-py/               # Python MCP server
    mcp-shipment-java/        # Spring Boot 4 + Spring AI 2.0 MCP server (Gradle or Maven)
    mock-tms/                 # fake system of record (FastAPI + seed data)
    ui/                       # minimal web UI (later AG-UI client)
  packages/
    domain/                   # Pydantic models, domain-pack interface
    rag/                      # chunkers, retrievers, rerankers, fusion
    guardrails/
    telemetry/                # OTel setup, redaction processors
  domain-packs/
    logistics/                # schemas, tools manifest, prompts, golden sets, seed docs
    it-ops/                   # second pack (M8) proves domain-agnosticism
  evals/
    golden/                   # ask.jsonl, triage.jsonl, extraction/, retrieval.jsonl
    promptfooconfig.yaml
    redteam.yaml
    deepeval/                 # test_rag.py, test_agent.py
  experiments/                # p1..p5 notebooks, scripts, reports
  infra/
    azure/                    # Bicep or Terraform: ACA env, Postgres Flexible Server, Key Vault, Log Analytics
    litellm/config.yaml
    otel/collector.yaml
  docs/
    adr/                      # 0001-record-architecture-decisions.md ...
    writeups/
    scorecard.md              # rubric scores per phase
    runbook.md
```

## 7. Local stack (docker compose)

| Service | Image / build | Purpose |
|---|---|---|
| `postgres` | `pgvector/pgvector:pg17` | Chunks, vectors, FTS, checkpoints, memory, audit |
| `ollama` | `ollama/ollama` | Local chat model (e.g. a 7–8B instruct model) + embedding model; GPU optional |
| `litellm` | LiteLLM proxy image + `infra/litellm/config.yaml` | Aliases `fast`/`smart`/`embed` mapped to Ollama locally, cloud when keys present |
| `langfuse` (+ its deps) | Langfuse self-host compose (web, worker, ClickHouse, Redis, MinIO as per Langfuse docs) | Tracing UI |
| `otel-collector` | `otel/opentelemetry-collector-contrib` | Receives OTLP, redacts, forwards to Langfuse |
| `gateway`, `orchestrator`, `ingest`, `mcp-ops-py`, `mock-tms` | local builds | App services |
| `mcp-shipment-java` | local build (Spring Boot buildpack or Dockerfile) | Java MCP server |

```yaml
# docker-compose.yml (sketch, not complete)
services:
  postgres:
    image: pgvector/pgvector:pg17
    environment: {POSTGRES_PASSWORD: dev, POSTGRES_DB: copilot}
    ports: ["5432:5432"]
    healthcheck: {test: ["CMD", "pg_isready", "-U", "postgres"], interval: 5s}
  ollama:
    image: ollama/ollama
    volumes: [ollama:/root/.ollama]
  litellm:
    image: ghcr.io/berriai/litellm:main-stable
    command: ["--config", "/app/config.yaml"]
    volumes: ["./infra/litellm/config.yaml:/app/config.yaml:ro"]
    depends_on: [ollama]
  orchestrator:
    build: ./apps/orchestrator
    environment:
      LLM_BASE_URL: http://litellm:4000
      DATABASE_URL: postgresql://postgres:dev@postgres:5432/copilot
      OTEL_EXPORTER_OTLP_ENDPOINT: http://otel-collector:4318
    depends_on: {postgres: {condition: service_healthy}}
volumes: {ollama: {}}
```

!!! warning "Verify image tags"
    Image names and tags change; check the pgvector, Ollama, LiteLLM and Langfuse docs for the current self-hosting instructions when you build M1.

## 8. Azure deployment

| Concern | Azure service | Notes |
|---|---|---|
| Compute | **Azure Container Apps** (one environment, one app per service; scale-to-zero for MCP servers, ingest as a Container Apps Job) | Consumption plan keeps idle cost near zero |
| Models | **Microsoft Foundry** (renamed from Azure AI Foundry in 2026) model deployments behind LiteLLM; optionally compare Foundry Agent Service for one flow | Assistants API retired 2026-08-26; Foundry Agent Service is on the Responses API |
| Database | **Azure Database for PostgreSQL – Flexible Server** with the `vector` extension enabled | Burstable tier for portfolio; stop when idle |
| Secrets | Key Vault + managed identity | No keys in env files in cloud |
| Identity | Entra ID app registration (OIDC) for UI + gateway; client-credentials for MCP servers | |
| Observability | Langfuse Cloud free tier or self-host on ACA; Azure Monitor / Application Insights for infra | Keep one trace ID across both |
| IaC + CI/CD | Bicep or Terraform in `infra/azure`; GitHub Actions with OIDC federated credentials | No long-lived Azure secrets in GitHub |

**Cost control:** deploy only in M7–M8, tear down with one command, keep the default demo on local Ollama. See [managed agent platforms](../tracks/agentic-ai/managed-agent-platforms.md) and [capacity and cost planning](../tracks/ai-system-design/capacity-cost-planning.md).

## 9. Milestones (weeks 1–24)

| Milestone | Weeks | Scope | Acceptance criteria | Feeds from |
|---|---|---|---|---|
| **M1 Skeleton** | 1–2 | uv workspace, FastAPI gateway with `/healthz` and `/ask` (plain LLM call via LiteLLM → Ollama), docker compose (Postgres, Ollama, LiteLLM), CI (ruff, ty, pytest), ADR 0001–0002, mock TMS with seed data | `make up` works from clean clone; CI green; one OTel trace visible per request; ADRs merged | — |
| **M2 Extraction** | 3–4 | Pydantic AI extractor for 3 doc types; ingestion worker stores docs + extracted records; first golden set (30 docs) | Field-level F1 >= 0.85 locally; eval runs with `make eval`; failure cases documented | [P1](p1-structured-extraction-service.md) |
| **M3 Hybrid RAG** | 5–8 | Chunking, pgvector HNSW + FTS, RRF fusion, reranker, citations; Langfuse tracing; DeepEval/promptfoo in CI with gates | recall@10 >= 0.80, faithfulness >= 0.85 on 100-question golden set; CI fails on >3-point regression; Langfuse shows retrieval spans | [P2](p2-hybrid-rag-with-ablation.md) |
| **M4 Agent + tools** | 9–12 | LangGraph Triage graph with Postgres checkpointer; HITL approval interrupt; both MCP servers (Python + Spring AI 2.0); Pydantic AI sub-agents; trajectory evals | 40 triage scenarios: task success >= 70%, tool-call correctness >= 90%, 0 unapproved writes; kill the orchestrator mid-run and resume without duplicate side effects | [P3](p3-mcp-agent-and-failure-analysis.md) |
| **M5 Production hardening** | 13–16 | Guardrails layer, LiteLLM routing/fallbacks/budgets/caching, OAuth on MCP servers, tenancy + RLS, promptfoo red-team in CI, cost dashboard | 0 critical red-team findings; injection ASR < 5%; per-tenant budget enforced (test proves 429 after cap); median cost/Ask <= $0.01 | [P4](p4-llm-gateway-and-guardrails.md) |
| **M6 Optimise + memory** | 17–20 | DSPy/GEPA-optimised classifier/planner prompts; local serving benchmark; memory (episodic + semantic) with provenance; optional LoRA router | Optimised module beats baseline by a measured margin on held-out set; memory evals (recall of prior-case facts) >= 80%; go/no-go memo merged | [P5](p5-optimize-and-serve.md), [P6](p6-distributed-systems-lab.md) (idempotency, retries) |
| **M7 Cloud deploy** | 21–22 | Azure Container Apps + Foundry + Postgres Flexible Server via IaC; GitHub OIDC deploy; load test; runbook | One-command deploy + teardown; NFR latency targets met at stated load; monthly cost projection <= $50 | — |
| **M8 Polish + second domain** | 23–24 | IT-ops domain pack (proves domain-agnosticism); README, C4 docs, demo video, 2 blog posts, all ADRs; final rubric scoring | All NFR targets in §3.2 met or deviations documented in an ADR; second domain works with zero orchestrator code changes; rubric avg >= 3.5 | Interview [checkpoint 6](../interviews/checkpoints.md) |

## 10. ADR backlog (15 decisions to record)

| # | Decision | Options to compare | Record by |
|---|---|---|---|
| 0001 | Record architecture decisions (MADR template) | MADR vs Nygard vs Y-statements | wk 1 |
| 0002 | Monorepo with uv workspace | Monorepo vs polyrepo; uv vs Poetry | wk 1 |
| 0003 | Postgres + pgvector as the single datastore | pgvector vs Qdrant vs Azure AI Search | wk 5 |
| 0004 | Chunking strategy | Fixed vs recursive vs structure-aware vs late chunking (from P2 data) | wk 7 |
| 0005 | Hybrid retrieval with RRF + cross-encoder rerank | Dense only vs hybrid; RRF vs weighted; reranker vs none | wk 8 |
| 0006 | Eval gating policy in CI | Absolute thresholds vs regression deltas; judge model choice | wk 8 |
| 0007 | LangGraph for orchestration, Pydantic AI for sub-agents | LangGraph vs Pydantic AI graphs vs MS Agent Framework vs plain code | wk 9 |
| 0008 | HITL approval model for write actions | Approve-each vs policy-based auto-approve vs two-person rule | wk 10 |
| 0009 | MCP transport and auth | Streamable HTTP vs stdio; OAuth 2.1 vs mTLS vs API key | wk 11 |
| 0010 | Polyglot: Java MCP server via Spring AI 2.0 | Python everywhere vs Spring AI for JVM systems of record | wk 12 |
| 0011 | Guardrail architecture | In-process vs sidecar vs gateway-level; classifier choice | wk 14 |
| 0012 | Model routing and fallback policy | Static alias vs cost/latency-aware router vs learned router | wk 15 |
| 0013 | Multi-tenancy isolation | RLS vs schema-per-tenant vs DB-per-tenant | wk 16 |
| 0014 | Memory design | Postgres tables vs Mem0 vs Letta; TTL + provenance policy | wk 19 |
| 0015 | Hosting: Azure Container Apps + Foundry | ACA vs AKS vs App Service; Foundry Agent Service vs self-orchestrated | wk 21 |

Use [ADRs](../tracks/architecture/adrs.md) and [documenting architecture](../tracks/architecture/documenting-architecture.md). Each ADR must cite the eval or benchmark that justified it where one exists.

## 11. Evaluation plan

| Layer | Dataset | Metrics | Tool | Gate |
|---|---|---|---|---|
| Extraction | 60 labelled docs across 3 types (synthetic + public samples, no real customer data) | Field precision/recall/F1, schema-valid rate | `pydantic_evals` / pytest | F1 >= 0.92 (M8) |
| Retrieval | 150 question → relevant-chunk-id pairs | recall@k (5, 10), MRR@10, nDCG@10 | custom + Ragas context metrics | recall@10 >= 0.85 |
| Generation | Same questions + reference answers; 20 unanswerable | Faithfulness, answer relevancy, citation precision, correct-refusal rate | DeepEval / promptfoo `llm-rubric` | faithfulness >= 0.90, refusal >= 0.9 |
| Agent | 60 triage scenarios with expected tool sequence + final decision | Task success, tool-call accuracy, steps, cost, unapproved-write count | DeepEval agent metrics + custom trajectory checks | success >= 80%, unapproved writes = 0 |
| Safety | promptfoo red-team: OWASP LLM Top 10 + OWASP agentic presets; indirect injection via poisoned documents | Attack success rate by plugin | promptfoo | 0 critical, ASR < 2% |
| Online | 10% sampled production traces + all thumbs-down | Judge scores, user feedback, latency, cost | Langfuse scores | Weekly review; add failures to golden set |

**Process:** start with error analysis (read 50–100 traces, open-code failures, cluster into a taxonomy), then write evals for the top failure modes; do not start with generic metrics. Calibrate every LLM judge against ~50 of your own binary labels before trusting it.

## 12. Cost budget (~$30–50/month)

| Item | Local-first phase (wk 1–20) | Cloud phase (wk 21–24) |
|---|---|---|
| LLM calls for dev + CI evals | $5–15 (cheap model in CI, Ollama for inner loop) | $10–20 |
| Embeddings | ~$0 (local embedding model) | < $2 |
| Azure Container Apps | $0 | $5–10 (scale-to-zero) |
| Azure Postgres Flexible Server (burstable, stopped when idle) | $0 | $10–15 |
| Langfuse | $0 (self-host) | $0 (free tier / self-host) |
| **Total** | **$5–15** | **$30–50** |

Rules: hard budget in LiteLLM (monthly cap per key), Azure budget alert at 50/80/100%, nightly evals capped by dataset size, teardown script tested.

## 13. Stretch goals

- **A2A:** expose the triage agent via an A2A v1.0 Agent Card and call a second, independent agent (e.g. a "carrier-liaison" agent) over A2A. See [A2A and AG-UI](../tracks/agentic-ai/a2a-ag-ui.md).
- **AG-UI front end:** replace the minimal UI with an AG-UI client (streaming state, tool-call rendering, approval widgets).
- **DSPy optimisation at scale:** GEPA over the full triage planner with trajectory-level metric. See [DSPy](../tracks/agentic-ai/dspy.md).
- **Fine-tuned small routing model:** LoRA-tune a 1–3B model to classify exception type / route requests; compare against prompt-only on cost, latency, accuracy. See [fine-tuning](../tracks/agentic-ai/fine-tuning.md).
- **vLLM serving:** serve the open model with vLLM (cloud GPU for a day) and compare to Ollama for throughput and p95. See [inference serving](../tracks/agentic-ai/inference-serving.md).
- **GraphRAG:** entity graph over contracts for multi-hop questions ("which customers with SLA tier A ship via port X?").
- **Event-driven triggers:** exceptions arrive via Kafka/Event Hubs; outbox pattern for action execution. See [messaging and streaming](../tracks/system-design/messaging-streaming.md).

## 14. Related interview practice

The capstone is designed to double as your answer to these prompts: [enterprise RAG](../tracks/ai-system-design/rag-system.md), [multi-agent platform](../tracks/ai-system-design/agent-platform.md), [LLM gateway](../tracks/ai-system-design/llm-gateway.md), [evaluation platform](../tracks/ai-system-design/evaluation-platform.md), [document processing](../tracks/ai-system-design/document-processing.md). In a Staff behavioral round, use its ADRs as "a decision I made with incomplete information" stories.

## Resources

| Resource | Why |
|---|---|
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflow-vs-agent framing behind the triage graph |
| [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context budget and memory design |
| [LangChain Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) | Checkpoints, interrupts, HITL |
| [Pydantic AI docs](https://ai.pydantic.dev/) | Sub-agents, evals, Logfire/OTel |
| [MCP specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28) | Transport, auth, tasks |
| [Spring AI 2.0 GA announcement](https://spring.io/blog/2026/06/12/spring-ai-2-0-0-GA-available-now/) | `@McpTool`, MCP Java SDK 2.0 |
| [pgvector](https://github.com/pgvector/pgvector) | HNSW/IVFFlat, operators |
| [Langfuse docs](https://langfuse.com/docs) | Self-hosting, tracing, scores |
| [OTel GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) | Span attributes |
| [Hamel Husain: evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | Error-analysis-first evals |
| [promptfoo OWASP agentic red-team](https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/) | Red-team preset |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Threat model |
| [Simon Willison: the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | Guardrail design principle |
| [LiteLLM docs](https://docs.litellm.ai/) | Proxy, routing, budgets |
| [Microsoft Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | Azure agent hosting option |
| [Azure Container Apps docs](https://learn.microsoft.com/en-us/azure/container-apps/) | Deployment target |
| [C4 model](https://c4model.com) | Diagrams in §4 |
