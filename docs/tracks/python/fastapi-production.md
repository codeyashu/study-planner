---
title: "FastAPI for production"
track: python
slug: fastapi-production
priority: P0
complexity: 2
est_hours: 3
phase: 1
tags: [python, P0]
last_reviewed: 2026-09-25
---

# FastAPI for production

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 2/5 · **Est. time:** 3 h · **Phase:** 1 · **Prereqs:** [asyncio in depth](asyncio-deep.md), [Pydantic v2](pydantic-v2.md)
    **You're done when:** you can ship a FastAPI LLM gateway with lifespan-managed clients, dependency injection, streaming (SSE), timeouts, load shedding, health checks, tests with dependency overrides, and a container that shuts down gracefully.

## Why it matters

FastAPI (0.14x on Starlette 1.x as of Sept 2026) is the default HTTP layer for Python AI services: agent backends, RAG APIs, MCP servers over HTTP, tool servers, eval dashboards. Tutorial-level FastAPI is easy. Production FastAPI is about **event-loop hygiene, resource lifecycle, streaming and cancellation, backpressure, and operability**, which is where incidents come from.

## Core concepts

### Request path

```mermaid
flowchart LR
  C[Client] --> U[uvicorn / granian workers]
  U --> M[ASGI middleware stack]
  M --> R[Router: path/query/body validation - Pydantic]
  R --> D[Dependencies - DI graph]
  D --> H["handler: async def (event loop) or def (threadpool)"]
  H --> S[Response model serialisation]
```

- `async def` handlers run **on the event loop**: never block. Plain `def` handlers run in AnyIO's threadpool (default 40 threads), so sync SDKs are fine there, but the pool is a bottleneck resource.
- Pydantic validates inputs and, if `response_model`/return annotation is set, filters and serialises outputs. That costs CPU on big payloads.

### Lifespan: own your long-lived resources

```python
from contextlib import asynccontextmanager
from typing import Annotated
import asyncio, httpx
from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel

class AppState:
    http: httpx.AsyncClient
    llm_sem: asyncio.Semaphore

@asynccontextmanager
async def lifespan(app: FastAPI):
    state = AppState()
    state.http = httpx.AsyncClient(base_url="https://llm.internal", timeout=httpx.Timeout(60, connect=5))
    state.llm_sem = asyncio.Semaphore(32)
    app.state.s = state
    try:
        yield
    finally:
        await state.http.aclose()          # runs on graceful shutdown

app = FastAPI(lifespan=lifespan)

def get_state(request: Request) -> AppState:
    return request.app.state.s

StateDep = Annotated[AppState, Depends(get_state)]

class Ask(BaseModel):
    prompt: str

@app.post("/v1/ask")
async def ask(body: Ask, s: StateDep) -> dict[str, str]:
    async with s.llm_sem, asyncio.timeout(45):
        r = await s.http.post("/complete", json={"prompt": body.prompt})
    r.raise_for_status()
    return {"text": r.json()["text"]}
```

`on_event("startup")` is deprecated. Use lifespan. Create clients, DB pools, and model handles once per process.

### Dependency injection (the good parts)

- `Annotated[T, Depends(fn)]` is the modern style. Dependencies can be async or sync, nest, are cached per request, and accept `yield` for setup/teardown (a DB session per request).
- Dependencies are the seam for **testing**: `app.dependency_overrides[get_state] = lambda: fake_state`.
- Auth, tenancy, rate limits, and request-scoped context (trace IDs) belong in dependencies or middleware, not in every handler.
- Nuance: yield-dependencies' exit code runs *after the response is sent* in current versions, so don't rely on it to alter the response, and remember cleanup runs even when the client disconnects.

### Streaming LLM output (SSE)

```python
from collections.abc import AsyncIterator
from contextlib import aclosing
from fastapi.responses import StreamingResponse

async def sse(upstream: AsyncIterator[str]) -> AsyncIterator[bytes]:
    async with aclosing(upstream) as stream:
        async for tok in stream:
            yield f"data: {tok}\n\n".encode()
        yield b"data: [DONE]\n\n"

@app.post("/v1/stream")
async def stream(body: Ask, s: StateDep) -> StreamingResponse:
    return StreamingResponse(sse(call_provider_stream(s, body.prompt)),
                             media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
```

Production concerns: disable proxy buffering (nginx `X-Accel-Buffering: no`), send periodic comment heartbeats (`: ping\n\n`) to survive idle timeouts, handle disconnect via cancellation (`aclosing`), set an overall deadline, and put errors *in-band* as an SSE event because HTTP status is already 200 once streaming starts.

### Serving: workers, graceful shutdown, limits

- Process model: one asyncio loop per process. Scale cores with multiple workers or, in Kubernetes, more single-worker pods (preferred, simpler memory/metrics). `fastapi run` wraps uvicorn. `uvicorn --workers N`, or gunicorn with `uvicorn.workers`/granian for process management.
- `--timeout-graceful-shutdown` must be **shorter than the pod's `terminationGracePeriodSeconds`**, and long streams need a plan (drain via readiness fail first, then wait).
- Load shedding: `--limit-concurrency N` returns 503 when saturated instead of queueing unboundedly. Better than letting latency explode.
- Separate **liveness** (`/healthz`, process alive) from **readiness** (`/readyz`, dependencies OK, not draining).
- Trust proxy headers correctly (`--proxy-headers`, `--forwarded-allow-ips`) or client IPs and https redirects break.
- Behind a load balancer, keep-alive timeout of uvicorn (default 5 s) must be **higher** than the LB idle timeout, or you get sporadic 502s.

### Response and payload hygiene

- `response_model_exclude_none`, dedicated response models (never return ORM/DB rows or internal models with secrets).
- Big JSON: return `Response(content=bytes, media_type="application/json")` from pre-serialised data, or use `ORJSONResponse`-style faster encoders after measuring.
- Pagination, idempotency keys for POSTs that trigger LLM/agent work (see [API design](../system-design/api-design.md)), and request size limits at the proxy.
- Background work: `BackgroundTasks` are in-process and lost on crash. Use a queue/worker (Celery/ARQ/Temporal/Kafka) for anything that must complete ([durable execution](../agentic-ai/durable-execution-hitl.md)).

### Testing

```python
import pytest
from httpx import ASGITransport, AsyncClient

@pytest.fixture
async def client(fake_state):
    app.dependency_overrides[get_state] = lambda: fake_state
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://t") as c:
        yield c
    app.dependency_overrides.clear()

async def test_ask(client):
    r = await client.post("/v1/ask", json={"prompt": "hi"})
    assert r.status_code == 200
```

Note: `ASGITransport` does not run lifespan. Use `asgi-lifespan`'s `LifespanManager` or `TestClient(app)` as a context manager when you need startup/shutdown.

### Senior nuance

- `async def` + sync DB driver = the loop freezes. `def` + async lib = error/awkward. Match colour to library.
- Middleware with `BaseHTTPMiddleware` breaks streaming/contextvars in subtle ways and adds overhead. Prefer pure ASGI middleware for hot paths.
- `Depends` with expensive setup per request (creating clients) is an anti-pattern. Do it in lifespan.
- Request cancellation: when clients disconnect, Starlette cancels the handler task. Your `finally`/`aclosing` blocks run. Never swallow `CancelledError` ([asyncio](asyncio-deep.md)).
- Contextvars (trace ID, tenant) set in middleware flow into handlers and tasks, but not into `BackgroundTasks` run after the response in some patterns. Test it.
- OpenAPI is a product: stable `operation_id`s, response models and examples let you generate typed clients (including for the Java side) and drive contract tests.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [FastAPI docs](https://fastapi.tiangolo.com/) | docs | Excellent and current, including the async explainer | beginner-advanced | free |
| [Concurrency and async/await](https://fastapi.tiangolo.com/async/) | docs | The def vs async def rules in one page | intermediate | free |
| [Lifespan events](https://fastapi.tiangolo.com/advanced/events/) | docs | Correct startup/shutdown pattern | intermediate | free |
| [Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/) | docs | Exit-code timing semantics | intermediate | free |
| [Testing dependencies with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) | docs | The DI testing seam | intermediate | free |
| [Server workers / deployment](https://fastapi.tiangolo.com/deployment/server-workers/) and [Docker](https://fastapi.tiangolo.com/deployment/docker/) | docs | Process model, one-process-per-container guidance | intermediate | free |
| [Starlette](https://starlette.dev/) and [Uvicorn](https://uvicorn.dev/) | docs | The layers underneath: middleware, lifespan, settings | advanced | free |
| [zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) :gem: | repo | Opinionated project structure and pitfalls from real projects | intermediate | free |
| [HTTPX docs](https://www.python-httpx.org/) | docs | Timeouts, limits, transports, ASGITransport for tests | intermediate | free |

## Hands-on lab

**Goal (90 min):** a production-shaped LLM gateway (capstone edge).

1. `uv init --package gw`, `uv add fastapi httpx structlog`, `uv add --dev pytest pytest-asyncio`.
2. Build the lifespan app above with a **fake upstream** (`/complete` sleeps 0.2-1 s, sometimes returns 503) served by a second tiny FastAPI app on port 9001.
3. Add `/v1/stream` with SSE and heartbeat; verify with `curl -N -X POST localhost:8000/v1/stream -H 'content-type: application/json' -d '{"prompt":"hi"}'`. **Expected:** tokens appear incrementally, not at the end.
4. Kill `curl` mid-stream (Ctrl-C). **Expected:** upstream mock logs its stream closed (no orphaned generation).
5. Load-test: `uvx --from locust locust` or `hey -z 20s -c 200`. Run once without limits and once with `uvicorn --limit-concurrency 64`. Compare p99 and 503 rate.
6. Add `/readyz` that flips to 503 on SIGTERM, then verify graceful drain: send SIGTERM during a load run, and check in-flight requests finish.
7. Write two tests using `dependency_overrides` (success and upstream 503 mapped to your error schema).

## Questions

### L1 - Recall

??? question "Q1. Where does an `async def` handler run vs a plain `def` handler?"
    ??? success "Answer"
        `async def` runs directly on the event loop (must never block). Plain `def` runs in the AnyIO worker threadpool (default 40 threads), so blocking calls are OK but consume a limited pool.

??? question "Q2. Why lifespan instead of creating an `httpx.AsyncClient` per request?"
    ??? success "Answer"
        A shared client reuses pooled keep-alive connections and TLS sessions (saving tens to ~150 ms per call) and centralises timeouts/limits. Per-request clients re-handshake and can exhaust sockets. Lifespan gives deterministic close on shutdown.

??? question "Q3. Difference between liveness and readiness probes?"
    ??? success "Answer"
        Liveness: is the process healthy enough to keep running (failure = restart). Readiness: can it accept traffic now (failure = removed from load balancing). Readiness should fail while draining or when critical dependencies are down. Don't put dependency checks in liveness or you cause restart storms.

??? question "Q4. How do you swap a real LLM client for a fake in tests?"
    ??? success "Answer"
        `app.dependency_overrides[real_dep] = fake_dep`, with clean-up afterwards. That is why external resources should be exposed through `Depends`, not module globals.

### L2 - Apply

??? question "Q5. p99 spikes to 3 s whenever one endpoint runs. The endpoint is `async def` and calls `requests.post(...)`. Diagnose and fix."
    ??? success "Answer"
        `requests` is synchronous, so it blocks the event loop and stalls every concurrent request. Fix: use `httpx.AsyncClient` (shared, from lifespan), or make the handler plain `def`, or `await asyncio.to_thread(...)`. Catch it in CI with ruff `ASYNC210` and monitor loop lag.

??? question "Q6. Users report intermittent 502s from the load balancer under low traffic. Your uvicorn keep-alive is default. What's likely?"
    ??? success "Answer"
        The LB's idle timeout (e.g. 60 s) exceeds uvicorn's `--timeout-keep-alive` (5 s default), so uvicorn closes an idle connection just as the LB reuses it. Set uvicorn's keep-alive higher than the LB idle timeout.

??? question "Q7. An SSE endpoint works locally but tokens arrive in one burst in production behind nginx. Fix?"
    ??? success "Answer"
        Proxy buffering. Set `X-Accel-Buffering: no` in the response (or `proxy_buffering off` for that location), keep `Cache-Control: no-cache`, avoid gzip middleware for the stream, and add heartbeats to keep idle timeouts from closing it.

??? question "Q8. Your handler starts a background LLM task with `BackgroundTasks` and jobs vanish during deploys. Options?"
    ??? success "Answer"
        BackgroundTasks live in the worker process, so they die with it. Enqueue work to a durable queue/worker (Celery/ARQ/Kafka consumer/Temporal), return 202 with a job ID, and make the job idempotent. For short, non-critical work accept the loss but drain gracefully on SIGTERM.

### L3 - Design & trade-offs

??? question "Q9. Multiple uvicorn workers per pod vs one worker per pod with more replicas?"
    ??? success "Answer"
        One-per-pod: simple resource limits, per-process metrics, K8s handles restarts and scaling, no shared-memory tricks needed. More replicas cost more baseline memory (each loads models/clients). Multi-worker per pod: shares the image and page cache, fewer pods, but noisy in-pod contention, harder autoscaling/metrics, and a supervisor to manage. Default: single worker per pod sized to a CPU limit, and multiple workers only when memory duplication is costly and you can measure a benefit.

??? question "Q10. Where should rate limiting, auth and idempotency live: FastAPI middleware, dependencies, or the gateway?"
    ??? success "Answer"
        Coarse, cross-service concerns (global rate limits, WAF, authN, TLS) belong at the gateway/mesh, uniform and offloaded. Route-specific policy (per-tenant quotas, authZ on resources, idempotency keys tied to business logic) belongs in dependencies close to domain code. Middleware only for cross-cutting request/response mechanics (trace IDs, timing). Avoid duplicating enforcement in two layers without a clear source of truth ([rate limiting](../system-design/rate-limiting.md)).

??? question "Q11. Return Pydantic models directly, or pre-serialise JSON, for a 5 MB list response at 200 RPS?"
    ??? success "Answer"
        Validation plus serialisation of large nested models is CPU on the event loop and blocks other requests. Options: pre-serialise once (cache the bytes and return `Response`), use `response_model=None` for trusted internal data, paginate, or stream NDJSON. Measure with py-spy first. If it remains CPU-heavy, run in threadpool (`def` handler) or move to a separate service. Don't optimise before measuring, and keep contract tests to guard against schema drift when bypassing `response_model`.

### L4 - Staff-level ambiguity

??? question "Q12. Six teams each built their own FastAPI service scaffold. Propose a platform approach."
    ??? success "Answer"
        Publish a versioned template/library ("paved road"): lifespan wiring, structured logging + OTel, health/readiness, error model (RFC 9457 problem+json), auth dependency, settings via pydantic-settings, Dockerfile/CI/pre-commit ([tooling](modern-tooling.md)). Ship it as a copier/cookiecutter template plus a small shared library for the runtime parts (so fixes propagate). Avoid a heavy framework-on-framework. Adoption via new services first, then opt-in migration for existing ones with a compatibility checklist. Metrics: time to first deploy, % services on template, incident classes eliminated (loop blocking, missing timeouts).

??? question "Q13. A product team wants their FastAPI agent endpoint to run 10-minute tasks synchronously with streaming updates. What do you advise?"
    ??? success "Answer"
        Long-lived HTTP requests fight LB timeouts, deploys and retries. Recommend a job model: POST returns a job ID (202), work runs in a durable executor (queue/workflow engine with checkpoints), progress via SSE/WebSocket reconnectable with `Last-Event-ID` or polling, results persisted. Keep streaming for the short interactive path (model tokens), and make the endpoint resumable. If they insist on long connections: heartbeats, deadline, graceful drain, client reconnection, and idempotent resumption.

## Real-world use cases

- **LLM gateway/proxy:** lifespan-managed client, semaphore and token bucket, SSE relay, request/response logging with redaction.
- **RAG API:** endpoint fan-outs to retrievers under a deadline, returns citations, streams the answer.
- **Tool server for agents:** typed endpoints double as tool schemas (OpenAPI to tool definitions).
- **Booking-status API for a logistics platform:** read-heavy, cache-aside with Redis, ETag support, strict response models to avoid leaking internal fields.

## Pitfalls & anti-patterns

- Blocking calls inside `async def`.
- Creating clients or DB pools per request.
- No timeouts anywhere (httpx default is 5 s per phase, but SDKs vary).
- Unbounded concurrency and queueing (no load shedding).
- `BaseHTTPMiddleware` on streaming routes.
- Returning internal/ORM models; missing `response_model`.
- Relying on `BackgroundTasks` for must-run work.
- Health checks that call the LLM provider on every probe.

## Checklist

- [ ] I can explain async vs sync handlers and where each runs
- [ ] I built the lab gateway with lifespan, SSE, limits and graceful drain
- [ ] I verified disconnect closes the upstream stream
- [ ] I answered all L3 questions out loud in < 3 min each
