---
title: Advanced Python question bank
track: python
last_reviewed: 2026-09-25
tags: [python, questions]
---

# Advanced Python: question bank

Cross-topic graded questions, production scenarios and rapid-fire drills. Per-topic questions live at the bottom of each topic page (see the [track index](index.md)). Answer aloud first, then open the model answer. Python behaviour below was checked on 3.14 unless noted.

Levels: **L1** recall, **L2** apply (including "what does this print" and "fix this bug"), **L3** design and trade-offs, **L4** Staff-level ambiguity.

## Graded questions

### L1 - Recall

??? question "G1. What is the difference between `uv sync --locked` and `uv sync --frozen`?"
    ??? success "Answer"
        `--locked` verifies that `uv.lock` is up to date with `pyproject.toml` and errors if not (use in CI to catch forgotten lock updates). `--frozen` uses the lockfile as-is without checking that it matches `pyproject.toml`. Prefer `--locked` in CI, and `--frozen` only when you deliberately skip the check.

??? question "G2. What does `__hash__` become when a class defines `__eq__` but not `__hash__`?"
    ??? success "Answer"
        `None`, so instances are unhashable (`TypeError: unhashable type`). Define `__hash__` over immutable fields, or use `@dataclass(frozen=True)`.

??? question "G3. Which is looked up first for `obj.x`: a data descriptor on the class or `obj.__dict__['x']`?"
    ??? success "Answer"
        The data descriptor (has `__set__`/`__delete__`). A non-data descriptor (only `__get__`, such as a plain function or `cached_property`) loses to the instance dict.

??? question "G4. Which PEP gave the `def f[T](x: T)` syntax, and what else came with it?"
    ??? success "Answer"
        PEP 695 (3.12): inline type parameters for functions and classes, the `type X = ...` alias statement (lazily evaluated), and inferred variance for class type parameters. PEP 696 (3.13) added defaults such as `class Box[T = str]`.

??? question "G5. What does `model_validate_json` do that `model_validate(json.loads(s))` doesn't?"
    ??? success "Answer"
        Parses and validates in one pass inside Rust (jiter + pydantic-core) without building an intermediate Python object graph. It is faster and also gives JSON-specific error locations and handling (for example strict-mode behaviour for JSON types).

??? question "G6. Name three differences between `asyncio.gather` and `asyncio.TaskGroup`."
    ??? success "Answer"
        (1) On first failure TaskGroup cancels siblings and waits, gather doesn't cancel the others. (2) TaskGroup raises an `ExceptionGroup` (catch with `except*`), gather raises the first exception. (3) TaskGroup guarantees no child outlives the `async with` block (structured concurrency), gather can leave orphans. Also: `return_exceptions=True` exists only on gather.

??? question "G7. Why is `CancelledError` a `BaseException`?"
    ??? success "Answer"
        So that `except Exception` blocks don't accidentally swallow cancellation. Catch it only to clean up and re-raise.

??? question "G8. Free-threaded build: what does `sys._is_gil_enabled()` return, and can it change at runtime?"
    ??? success "Answer"
        `False` when the GIL is off. On a free-threaded build the GIL can be re-enabled at runtime if an imported C extension doesn't declare support (with a warning), and `PYTHON_GIL=0`/`-X gil=0` forces it off. On a normal build it always returns True.

??? question "G9. What is a Protocol's advantage over an ABC for ports?"
    ??? success "Answer"
        Structural typing: implementations and test fakes needn't inherit from or import the port, which keeps dependencies pointing inward and lets you wrap third-party classes. Cost: no runtime enforcement of behaviour, so use contract tests.

??? question "G10. What does `@functools.wraps` copy, and why do frameworks care?"
    ??? success "Answer"
        `__name__`, `__qualname__`, `__doc__`, `__module__`, `__dict__` and sets `__wrapped__`, so `inspect.signature` follows through to the original signature. FastAPI DI, Pydantic AI tool schemas and pytest introspect signatures.

??? question "G11. What are `TypeIs` and `TypeGuard`, and which do you prefer?"
    ??? success "Answer"
        Both are return annotations for user-defined narrowing functions. `TypeIs` (3.13) narrows in both branches and requires consistency with the input type, `TypeGuard` narrows only when True and is looser. Prefer `TypeIs`.

??? question "G12. When does `__init_subclass__` run?"
    ??? success "Answer"
        On the parent class whenever a subclass is created (at class definition/import time), for direct and indirect subclasses. It replaces most metaclass uses for registries and contract validation.

??? question "G13. What are the standard signals of observability and the key correlation field?"
    ??? success "Answer"
        Traces, metrics, logs. Correlate through `trace_id`/`span_id` injected into log records, and exemplars linking metrics to traces.

??? question "G14. Why does Polars prefer `scan_parquet` over `read_parquet` for big data?"
    ??? success "Answer"
        `scan_*` builds a lazy plan, so the optimiser pushes filters and column selection into the file scan, and the streaming engine can process larger-than-memory data. `read_*` loads everything eagerly.

### L2 - Apply

??? question "G15. What does this print?"
    ```python
    print([f() for f in [lambda: i for i in range(3)]])
    ```
    ??? success "Answer"
        `[2, 2, 2]`. The lambdas share the variable `i` and see its final value. Bind it with `lambda i=i: i`.

??? question "G16. What does this print?"
    ```python
    class B:
        def __bool__(self): return False
        def __len__(self): return 5
    print(bool(B()))
    ```
    ??? success "Answer"
        `False`. `__bool__` takes precedence over `__len__`.

??? question "G17. What does this print, and what's the practical lesson?"
    ```python
    class A:
        def __init__(self, d): self.d = d
        def __len__(self): return len(self.d)
        def __getitem__(self, i): return self.d[-1 - i]
    a = A([1, 2, 3])
    print(list(a), 2 in a)
    ```
    ??? success "Answer"
        `[3, 2, 1] True`. Without `__iter__`, `iter()` falls back to the legacy sequence protocol: `__getitem__` with 0, 1, 2, ... until `IndexError`. `in` falls back to iteration too. Lesson: define `__iter__` explicitly, or inherit `collections.abc.Sequence`.

??? question "G18. What does this print?"
    ```python
    from pydantic import BaseModel
    class M(BaseModel):
        x: int
    m = M(x=1)
    m2 = m.model_copy(update={"x": "oops"})
    print(repr(m2.x), M.model_construct(x="bad").x)
    ```
    ??? success "Answer"
        `'oops' bad`. `model_copy(update=...)` and `model_construct` skip validation. Re-validate with `M.model_validate({**m.model_dump(), "x": "oops"})` for untrusted changes.

??? question "G19. What does this print (Python 3.14)?"
    ```python
    async def stubborn():
        try:
            await asyncio.sleep(10)
        except asyncio.CancelledError:
            print("swallowed")
        return "done"
    async def main():
        t = asyncio.create_task(stubborn())
        await asyncio.sleep(0)
        t.cancel()
        print(await t)
    asyncio.run(main())
    ```
    ??? success "Answer"
        `swallowed` then `done`. The task swallowed the cancellation and finished normally, so awaiting it returns a value instead of raising. Re-raise `CancelledError` after cleanup.

??? question "G20. What does this print?"
    ```python
    async def tick():
        for _ in range(3):
            print("tick", round(time.perf_counter() - t0, 1)); await asyncio.sleep(0.1)
    async def blocker(): time.sleep(0.5)
    t0 = time.perf_counter()
    await asyncio.gather(tick(), blocker())
    ```
    ??? success "Answer"
        `tick 0.0`, `tick 0.5`, `tick 0.6`. The blocking `time.sleep(0.5)` freezes the loop, so the second tick is delayed until the sleep finishes. Fix with `await asyncio.sleep` or `asyncio.to_thread`.

??? question "G21. Fix this dataclass."
    ```python
    @dataclass
    class Conversation:
        messages: list[str] = []
    ```
    ??? success "Answer"
        Raises `ValueError: mutable default <class 'list'> for field messages is not allowed: use default_factory`. Use `messages: list[str] = field(default_factory=list)`.

??? question "G22. What does this print?"
    ```python
    from contextlib import contextmanager
    @contextmanager
    def res():
        print("open"); yield; print("close")
    try:
        with res(): raise RuntimeError
    except RuntimeError: pass
    ```
    ??? success "Answer"
        Only `open`. Without `try/finally` around `yield`, the exception thrown into the generator skips the cleanup. Wrap `yield` in `try/finally`.

??? question "G23. What does this print?"
    ```python
    def inner():
        yield "a"; return 42
    def outer():
        r = yield from inner()
        print("inner returned", r)
    print(list(outer()))
    ```
    ??? success "Answer"
        `inner returned 42` then `['a']`. `yield from` evaluates to the sub-generator's return value.

??? question "G24. Why does this raise, and how do you fix it?"
    ```python
    class P:
        __slots__ = ("a",)
    P().b = 1
    ```
    ??? success "Answer"
        `AttributeError: 'P' object has no attribute 'b' and no __dict__ for setting new attributes`. Slotted classes have no instance dict. Add the name to `__slots__` (or include `"__dict__"` if dynamic attributes are required).

??? question "G25. In what order are `M.__call__`, `Q.__new__`, `Q.__init__` invoked for `Q()` when `Q` uses metaclass `M`?"
    ??? success "Answer"
        `M.__call__` first (via `Q()`), which calls `Q.__new__`, then `Q.__init__` if `__new__` returns a `Q` instance. Verified output: `meta call`, `new`, `init`.

??? question "G26. A Dockerfile re-installs all dependencies on every code change. Give the fix in three lines of intent."
    ??? success "Answer"
        Bind-mount `pyproject.toml` and `uv.lock` and run `uv sync --locked --no-install-project --no-dev` first (dependency layer). Then `COPY` the source and run `uv sync --locked --no-dev`. Add a cache mount for `/root/.cache/uv`.

??? question "G27. A `TaskGroup` is used with 10,000 items and `Semaphore(20)`; memory spikes. Why?"
    ??? success "Answer"
        10,000 tasks are created immediately (each with a coroutine frame and captured payload) even though only 20 run. Bound the *task creation* too: a fixed worker pool pulling from a bounded `Queue`, or process in chunks. A semaphore alone limits concurrency, not memory.

??? question "G28. `lru_cache` on an `async def` raises `RuntimeError: cannot reuse already awaited coroutine` on the second call. Explain and fix."
    ??? success "Answer"
        The cache stores the coroutine object, which can be awaited only once. Cache the result (async-aware cache library) or cache a `Task` per key (`tasks.setdefault(key, asyncio.create_task(fn(key)))`) so concurrent callers share one in-flight call.

??? question "G29. Which of these is safe on the free-threaded build without a lock: `counter += 1`, `lst.append(x)`, `if k not in d: d[k] = v`?"
    ??? success "Answer"
        Only `lst.append(x)` is safe as a single operation (built-in containers are internally locked to avoid crashes). `counter += 1` is read-modify-write and races. The check-then-set on the dict is a race (duplicate work or lost updates). Use a lock, or `dict.setdefault`, or per-thread aggregation.

??? question "G30. Your FastAPI service gets sporadic 502s from the load balancer under low traffic. First hypothesis?"
    ??? success "Answer"
        Keep-alive mismatch: uvicorn's idle keep-alive (default 5 s) shorter than the LB idle timeout, so uvicorn closes a connection the LB is about to reuse. Set `--timeout-keep-alive` above the LB's idle timeout.

### L3 - Design & trade-offs

??? question "G31. Choose asyncio, threads, processes, or 3.14t threads for: (a) 5,000 concurrent LLM calls, (b) parsing 2M PDFs, (c) in-process reranker with a 3 GB model shared by workers."
    ??? success "Answer"
        (a) asyncio: cheapest per connection, supports cancellation and backpressure. (b) Processes (or a worker fleet), since parsing is CPU-heavy and isolates crashes and memory leaks in native libs. (c) Free-threaded threads if all dependencies support 3.14t (share the model without pickling), otherwise a separate model-serving process with batched requests. Support with benchmarks and a canary.

??? question "G32. Strict vs lax Pydantic validation at three boundaries: public API input, LLM tool arguments, internal service events."
    ??? success "Answer"
        Public API: lax parsing is friendlier for clients (`"3"` for ints in query/JSON) but constrain values tightly. LLM tool args: lax plus tight constraints reduces retries, strict for side-effecting tools. Internal events: strict, `extra="forbid"`, frozen, since both sides are code you control and silent coercion hides bugs.

??? question "G33. When would you use `TypedDict` vs dataclass vs Pydantic model?"
    ??? success "Answer"
        TypedDict for JSON-shaped dicts you pass through or `**kwargs` typing (no runtime cost, no validation). Dataclass (frozen, slots) for internal domain values. Pydantic for untrusted input, LLM structured output, and anywhere you need validation plus JSON Schema.

??? question "G34. Where do timeouts belong in an agent turn: per call, per step or per turn?"
    ??? success "Answer"
        All three, with a deadline model. A turn-level deadline (contextvar) bounds worst-case latency, each step uses the remaining budget (`asyncio.timeout_at`), and per-call timeouts (connect/read) protect against hung sockets. Otherwise N sequential steps x per-call timeouts blow the SLO.

??? question "G35. `BackgroundTasks` vs a durable queue vs `asyncio.create_task` for post-response work such as audit logging and embedding a new document."
    ??? success "Answer"
        Audit logging that must not be lost: durable queue/outbox. Embedding a new document: durable job (queue plus worker) with retries and idempotency, since it is slow and must survive deploys. `BackgroundTasks` for small, best-effort work. Bare `create_task` needs a held reference and graceful-shutdown draining, and still dies with the process.

??? question "G36. Monorepo with a uv workspace vs polyrepo for shared Pydantic contracts."
    ??? success "Answer"
        Monorepo gives atomic contract changes, one lock, easy refactors. Cost: CI scaling (affected-only builds), ownership granularity, coupled upgrades. Polyrepo isolates cadence but drifts and makes contract changes painful. With fast-moving shared contracts, choose the monorepo plus CODEOWNERS and import-linter boundaries, and publish versioned schemas for non-Python consumers.

??? question "G37. Repository/UoW/message bus: when is it over-engineering?"
    ??? success "Answer"
        For CRUD services with little domain logic, one entrypoint and no need to fake infrastructure. Introduce a service layer and ports when logic is duplicated, multiple entrypoints share it, tests are slow due to DB coupling, or infra needs swapping. Add the message bus only when handlers multiply or side effects must be decoupled.

??? question "G38. Compare mypy, pyright and ty as the org CI gate."
    ??? success "Answer"
        mypy: reference behaviour and plugin ecosystem (Django, SQLAlchemy). pyright: fast, strong inference, mature. ty: fastest, strong diagnostics and editor integration, but beta (0.0.x as of Sept 2026), so pin and run advisory first. Choose one CI gate with a pinned version and a ratchet, allow others in editors.

??? question "G39. Pydantic models everywhere (API, DB, LLM schema) vs separate models per layer."
    ??? success "Answer"
        One model couples three change rates: public API contract, persistence, and LLM-facing schema (description tuning, flattening). Separate models with explicit mappers are more code but let each evolve independently. For small internal tools, one model is fine, but design so the split is cheap.

??? question "G40. Head vs tail sampling for LLM traces."
    ??? success "Answer"
        Head sampling is cheap but drops rare failures and slow/high-cost runs. Tail sampling in the Collector keeps errors, slow, high-token, and flagged traces plus a baseline percentage, at the cost of stateful infrastructure. For agent traces (large and costly) tail sampling is usually worth it.

??? question "G41. `to_thread` vs `ProcessPoolExecutor` vs a separate service for CPU-heavy work called from an async API."
    ??? success "Answer"
        `to_thread` helps only if the work releases the GIL (NumPy, Polars, tokenizers-rs) or the build is free-threaded. `ProcessPoolExecutor` gives true parallelism for pure Python at the cost of pickling and startup, good for medium tasks. A separate service is right when the workload is heavy, needs different scaling/hardware (GPU), or isolation. Decide by payload size, task duration, and scaling needs.

??? question "G42. Design the error contract for an LLM extraction endpoint that must return validated JSON."
    ??? success "Answer"
        Success returns the validated Pydantic model and metadata (model, attempts, tokens). Failure classes: input invalid (4xx), model output invalid after N retries (422 or a domain error with the validation errors summarised and a job ID for review), provider unavailable/rate limited (503 with `Retry-After`), timeout (504). Never leak raw prompts or provider errors. Emit metrics per class, and send terminal failures to a dead-letter queue.

??? question "G43. Explain when Hypothesis beats example-based tests, with two concrete targets in an LLM service."
    ??? success "Answer"
        When the input space is large and invariants are clear: parsers of LLM output (round-trips, idempotence, never-crash on arbitrary text), chunkers (lossless, bounded size), reducers/state machines (stateful testing). It finds edge cases (empty strings, unicode, boundaries) that hand-written examples miss and shrinks to a minimal repro.

??? question "G44. What would make you avoid `functools.cache`/`lru_cache` on a method?"
    ??? success "Answer"
        The cache key includes `self`, so it holds strong references to every instance seen (a memory leak for long-lived caches). Use `cached_property` for per-instance values, an instance-level cache, or a module-level pure function.

??? question "G45. Choose a log/trace content policy for prompts and completions in production."
    ??? success "Answer"
        Default: metadata only (model, token counts, latency, finish reason, tool names, hashes). Content captured only in a sampled, access-controlled, TTL'd store (errors, low eval scores, opted-in tenants), redacted at the SDK processor level. Document retention and legal basis. Gives debuggability without blanket PII exposure.

??? question "G46. Explain trade-offs of uvloop and multiple uvicorn workers for an LLM gateway."
    ??? success "Answer"
        uvloop reduces loop overhead (2-4x on raw loop microbenchmarks) but matters little when each request waits seconds on the LLM. Multiple workers use more cores but multiply memory and split in-process semaphores/caches, so effective global limits scale with worker count. In Kubernetes prefer one worker per pod plus more replicas, and use a shared limiter (gateway or Redis) for provider quotas.

### L4 - Staff-level ambiguity

??? question "G47. Three teams use poetry, pip-tools and conda. Propose convergence."
    ??? success "Answer"
        ADR with goals (reproducibility, CI time, security scanning). Pilot uv on one repo and publish before/after numbers. Golden-path template (uv + ruff + chosen type checker + Docker + pre-commit). Keep conda/pixi where native binaries demand it. Migrate opportunistically with a deprecation date and support channel. Metrics: % repos on template, CI p50, time to patch a CVE across repos.

??? question "G48. Leadership proposes rewriting the Python agent platform in Go/Java for performance. Respond."
    ??? success "Answer"
        Reframe to bottlenecks with data. Agent latency is dominated by model and tool I/O, and asyncio overhead per await is microseconds. Typical culprits (blocking calls, no backpressure, CPU-bound serialisation) are fixable in Python (to_thread, process pools, 3.14t, native libs). The AI ecosystem is Python-first. Extract a CPU-heavy component only if profiling proves a ceiling. Document criteria and revisit in an ADR.

??? question "G49. 25 services on Pydantic v1 need Python 3.14. Plan the migration."
    ??? success "Answer"
        The `pydantic.v1` shim is unsupported on 3.14+, so v2 migration gates the Python upgrade. Inventory usage, order by risk/traffic (shared libs first), snapshot JSON Schema and dump outputs before migrating for diffing, run the codemod plus manual validator review, and track progress. Timebox with office hours and a compatibility matrix.

??? question "G50. Design a shared, typed SDK for defining agent tools that 12 teams use."
    ??? success "Answer"
        Tools are typed functions. Schemas derive from signatures, `Annotated[..., Field(description=...)]` and docstrings (single source of truth). Restrict to JSON-representable params with clear registration errors. A typed `RunContext[Deps]` injected via `Concatenate` stays out of the LLM-visible schema. Snapshot-test generated schemas, version them, and fail CI on breaking changes. Explicit toolset composition instead of import-time global registries.

??? question "G51. Your org has recurring 'event loop blocked' incidents. Build the prevention and detection system."
    ??? success "Answer"
        Prevention: ruff `ASYNC` rules in the template and CI, shared async adapters wrapping sync SDKs with sized executors. Detection: loop-lag histogram per service with alerts (p99 > 100 ms), debug mode in staging, py-spy runbook. Enablement: guidance that sync `def` endpoints run in the threadpool. Metrics: incident count and loop-lag p99 per service over time.

??? question "G52. You must adopt free-threaded Python across a 40-service estate. What is your rollout and stop condition?"
    ??? success "Answer"
        Inventory dependency support for `cp314t`, add a 3.14t CI job failing if the GIL re-enables, pilot 2-3 CPU-bound thread-heavy services, canary with p99, RSS and error-rate guards, keep GIL builds as rollback. Stop condition: dependency gaps in your critical path, unacceptable memory growth, or no measured cost/latency win for the workload class.

??? question "G53. Telemetry cost is 30% of the bill after adding agent traces. What now?"
    ??? success "Answer"
        Attribute by signal and service. Tail sample (keep errors, slow, expensive, plus 1-5% baseline), drop health-check and noisy internal spans, enforce metric cardinality budgets, move verbose content to cheap TTL'd storage, shorten debug-log retention, and give teams budgets and dashboards. Run fire drills to confirm on-call can still debug.

??? question "G54. Define a testing standard for 12 teams shipping LLM features."
    ??? success "Answer"
        Ports and fakes for models/tools, table tests for parsers and prompt assembly, Hypothesis for serialisation/reducers, one real-dependency integration suite (testcontainers), recorded provider contract tests refreshed weekly, and a golden eval set run nightly with regression gates. Ship a shared `testkit` package so compliance is cheap, and review via checklist rather than coverage thresholds.

??? question "G55. CI takes 25 minutes and 4% of runs flake, so people rerun until green. Fix the system."
    ??? success "Answer"
        Measure durations and flake rates from CI history, parallelise (xdist, sharding), remove sleeps/network, session-scope containers, split fast and slow suites, cache uv. Quarantine flakes with owner/ticket/SLA, root-cause top offenders (order dependence, time, ports, shared state), enforce `pytest-randomly`. SLOs: PR feedback under 8 minutes, flake rate under 0.5%.

??? question "G56. Define a 'metaprogramming budget' for a 200-engineer Python org."
    ??? success "Answer"
        Ladder of least power: functions and composition, decorators, `__init_subclass__`/descriptors, then metaclasses (design review required). Any magic must preserve signatures and types (`ParamSpec`, `dataclass_transform`), have no import-time I/O or hidden global mutation, be testable, debuggable, and documented with failure modes.

## Scenario questions

Each scenario gives inputs, constraints, and asks for a decision. State assumptions, then answer.

??? question "S1. Your FastAPI service calls an LLM and p99 spikes from 3 s to 25 s every few minutes, while p50 is unchanged and CPU is low. Diagnose."
    ??? success "Answer"
        Look for queueing and tail causes, not average latency. Check: (1) provider 429/5xx with retries and backoff inflating tail (metrics on retry counts, `Retry-After`), (2) semaphore/connection-pool exhaustion (wait time before the call; httpx pool timeout), (3) event-loop blocking (loop-lag metric, py-spy dump) if other endpoints also spike, (4) a slow tenant sending huge prompts (token histogram by tenant), (5) missing timeouts, so a hung provider connection holds slots until the 60-120 s default. Fixes: per-turn deadline, jittered capped retries honouring `Retry-After`, separate bulkheads per tenant/priority, load shedding (`--limit-concurrency`) and fallback model. Verify with traces showing where the 25 s goes (span for semaphore wait vs provider call).

??? question "S2. A nightly job embeds 3M chunks using a provider limited to 300 RPM and 1M TPM. It takes 30 hours and sometimes dies at hour 20. Redesign."
    ??? success "Answer"
        Batch inputs (embedding APIs accept arrays), so RPM stops being the constraint and TPM becomes the limit: 3M chunks x ~400 tokens = 1.2B tokens, at 1M TPM that is 1,200 minutes (20 hours) at best, so negotiate quotas or use multiple deployments/regions. Design: a bounded async pipeline (producer to batch builder to N workers under a token-bucket for TPM/RPM), idempotent writes keyed by content hash so restarts skip done work, checkpointing by shard, retries with jittered backoff, and a dead-letter output for poison chunks. Report progress and ETA. Consider a batch/offline API tier if available at lower cost.

??? question "S3. Memory of your agent worker grows 1 GB per day and is OOM-killed weekly. Find and fix."
    ??? success "Answer"
        Compare RSS with `tracemalloc` to distinguish Python heap growth from native or fragmentation, then `tracemalloc` snapshot diffs or memray over a soak test. Likely suspects: unbounded caches (prompt/response dicts, `lru_cache(maxsize=None)`), conversation histories in globals, stored exceptions retaining tracebacks and big locals, per-request `AsyncClient`s or unclosed streams, `functools.cache` on methods. Fix with bounded TTL/LRU caches, storing formatted error strings, lifespan-scoped clients, `aclosing`. Add an RSS alert and a soak test in CI. If it's fragmentation, recycle workers (`max_requests`) as mitigation.

??? question "S4. Users see tokens arrive in one burst instead of streaming in production, but local dev streams fine. Diagnose."
    ??? success "Answer"
        Buffering between app and client: nginx/ingress proxy buffering (`X-Accel-Buffering: no`, `proxy_buffering off`), gzip middleware buffering the stream, a CDN or APM agent buffering, or `BaseHTTPMiddleware` wrapping the streaming route. Verify with `curl -N` directly against the pod, then through each hop. Fix at the offending hop and add SSE heartbeats to keep idle timeouts from cutting streams.

??? question "S5. Clients disconnect mid-stream, yet your provider bill shows full completions. Quantify and fix."
    ??? success "Answer"
        Upstream generation continues because the provider stream isn't closed on cancellation. Instrument tokens billed vs tokens delivered to estimate waste. Fix by consuming the provider stream inside the response generator with `aclosing`/`async with client.stream`, avoiding detached consumer tasks, and testing disconnect behaviour (fake provider asserting `aclose()`). Also set `max_tokens` and per-request deadlines. Track the waste ratio as a metric.

??? question "S6. An LLM extraction step returns invalid JSON 6% of the time. Product wants under 0.5%. What do you try, in order?"
    ??? success "Answer"
        1) Use provider structured-output/constrained decoding with the Pydantic-derived schema (adjusted to the supported subset). 2) Simplify the schema (flatter, `Literal` enums, fewer optionals) and improve field descriptions. 3) Validation retry with error feedback (max 1-2), measuring first-pass vs post-retry validity. 4) Repair pass for known failure classes (fence stripping, trailing commas) before re-calling the model. 5) Escalate hard cases to a stronger model. 6) Dead-letter plus human review for the residue. Measure on a labelled set. Validity is not accuracy, so track field-level accuracy too.

??? question "S7. Your 3.14t pilot shows no speedup for a chunking service. Why?"
    ??? success "Answer"
        Check: `sys._is_gil_enabled()` (an incompatible extension may have re-enabled the GIL), the workload isn't CPU-bound (I/O or lock contention), a global lock or shared mutable structure serialises threads, the threadpool size is capped (AnyIO default 40 tokens, executor `max_workers`), dependencies release the GIL anyway (so the GIL build was already parallel), or task granularity is too small. Profile with `py-spy --gil`/`--native`, and compare to a process pool baseline.

??? question "S8. A junior's PR adds `requests` calls inside `async def` handlers and passes all tests. Which controls should have caught it?"
    ??? success "Answer"
        Static: ruff `ASYNC210`/`ASYNC` rules in CI. Dynamic: a load test with a loop-lag gate, and asyncio debug mode in staging. Review: PR checklist and the golden-path template using a shared async HTTP client. Tests pass because functional tests don't measure concurrency, so add a concurrency smoke test asserting other requests aren't delayed.

??? question "S9. Your team's Pydantic model for tool arguments works locally but the provider rejects the JSON Schema in strict mode. What now?"
    ??? success "Answer"
        Strict structured-output modes support a subset (all fields required, `additionalProperties: false`, limited formats/patterns, restricted recursion, no `oneOf` variants in some providers). Use the SDK's schema transformation helper or post-process `model_json_schema()` (inline `$defs`, set `additionalProperties`, convert optionals to nullable required). Keep the full-constraint Pydantic model for server-side validation. Snapshot-test the transformed schema per provider and re-validate outputs.

??? question "S10. Two engineers propose different ways to share a 2 GB embedding index between 8 worker processes. Compare."
    ??? success "Answer"
        Fork/COW: simple but refcount writes and GC dirty pages, and `forkserver` is the 3.14 default on Linux so fork inheritance can't be assumed. Memory-mapped file (NumPy `memmap`/Arrow IPC/FAISS mmap): shared page cache, no copies, best for read-only. `multiprocessing.shared_memory`: explicit, works with NumPy arrays. Threads on 3.14t: one copy, no IPC, requires dependency support. A dedicated search service: isolates memory, scales independently, adds a network hop. For read-only vector data, mmap plus a single-process-per-pod service is usually simplest.

??? question "S11. Your `pytest` suite passes locally and fails in CI with 'attached to a different event loop'. What changed?"
    ??? success "Answer"
        Async fixture/test loop scope mismatch (for example a session-scoped async client used from function-scoped test loops), or a different `pytest-asyncio` mode/default in CI config. Align `loop_scope` for fixtures and tests (or set `asyncio_default_fixture_loop_scope`/`asyncio_default_test_loop_scope`), or create loop-bound resources per test. Pin plugin versions.

??? question "S12. You inherit a service using `@lru_cache` on instance methods and `BackgroundTasks` for billing events. Prioritise your fixes."
    ??? success "Answer"
        Billing events first: `BackgroundTasks` lose work on restart, which is a correctness/revenue risk. Move to a transactional outbox or durable queue with idempotent consumers. Then the `lru_cache`-on-methods memory leak (and stale-data risk): replace with per-instance or bounded TTL caches keyed by hashable inputs. Add tests for both (crash-and-recover for billing, RSS soak for caches).

??? question "S13. You need per-tenant fairness in an LLM gateway so one tenant can't starve others. Design."
    ??? success "Answer"
        Bulkheads and weighted fair queuing: per-tenant concurrency limits (semaphores) plus a global limit, a token-bucket per tenant for RPM/TPM, and a scheduler picking from per-tenant queues round-robin or weighted by tier. Shed load with 429 plus `Retry-After` when a tenant's queue exceeds bounds. Track per-tenant queue wait and rejects as metrics (bounded label: tier, not tenant ID, plus per-tenant logs/traces). Global limits across replicas need shared state (Redis) or a gateway.

??? question "S14. The p99 of your `model_validate` step is 40 ms for a 5 MB payload at 200 RPS, blocking the loop. Options?"
    ??? success "Answer"
        Confirm with py-spy. Options in order: validate less (trusted internal data, only needed fields), `model_validate_json` from bytes, remove Python-level validators, move to a `def` handler (threadpool) or `to_thread` so the loop stays responsive (on 3.14t it can also use multiple cores), paginate/stream the payload (NDJSON), or use a leaner parser (msgspec) for that path. Keep contract tests when bypassing validation.

??? question "S15. A Python 3.14.0 fleet shows RSS regressions after upgrade. Where do you look?"
    ??? success "Answer"
        Known: 3.14.0-3.14.4 shipped an incremental GC, reverted in 3.14.5 due to memory-pressure reports in production. Check the exact patch version, upgrade to 3.14.5+, compare RSS and GC stats (`gc.get_stats`) before and after. Also check dependency changes and free-threaded/mimalloc differences if on 3.14t. Verify with a canary before fleet rollout.

??? question "S16. Design the local-dev-to-prod path for a Python LLM service so 'works on my machine' disappears."
    ??? success "Answer"
        `pyproject.toml` + `uv.lock` (universal), `.python-version` pinned, `uv sync --locked` in dev/CI/Docker, pre-commit (ruff, uv-lock), the same multi-stage Dockerfile for CI and prod, config via pydantic-settings, `docker compose` (or testcontainers) for Postgres/Redis, recorded provider cassettes for offline tests, a wheel-install smoke test job, and identical base image digests. A `make dev` or `just` entrypoint documents it.

## Rapid-fire (30)

Answer in one or two sentences. Aim for under 20 seconds each.

??? question "R1. `python -m venv` replacement in the uv world?"
    ??? success "Answer"
        `uv venv`, or just `uv sync`/`uv run` (creates `.venv` implicitly).

??? question "R2. Which file records exact resolved versions for a uv project?"
    ??? success "Answer"
        `uv.lock` (export to `pylock.toml` or requirements for interoperability).

??? question "R3. What does `hash(-1)` return in CPython?"
    ??? success "Answer"
        `-2`. `-1` is reserved as the C-level error sentinel.

??? question "R4. `__repr__` vs `__str__` audience?"
    ??? success "Answer"
        `__repr__` for developers (unambiguous, used in logs and debugging), `__str__` for end users. `repr` is the fallback when `__str__` is missing.

??? question "R5. What does returning `NotImplemented` from `__add__` trigger?"
    ??? success "Answer"
        Python tries the reflected `other.__radd__(self)`, then raises `TypeError` if that also declines.

??? question "R6. Covariant, contravariant, invariant: which is `list[T]`?"
    ??? success "Answer"
        Invariant.

??? question "R7. What replaces `Optional[int]` in modern typing?"
    ??? success "Answer"
        `int | None`.

??? question "R8. What does `@override` (3.12) catch?"
    ??? success "Answer"
        A method that claims to override but doesn't match any base method (for example after a rename in the base class).

??? question "R9. `Annotated[int, Field(ge=0)]`: who reads the metadata?"
    ??? success "Answer"
        Runtime libraries such as Pydantic and FastAPI. Type checkers ignore it and treat it as `int`.

??? question "R10. Which Pydantic API validates a non-model type such as `list[int]`?"
    ??? success "Answer"
        `TypeAdapter(list[int])`. Create it once at module level.

??? question "R11. What does `M(x=True)` give for `x: int` in lax mode?"
    ??? success "Answer"
        `x=1`. In strict mode it fails.

??? question "R12. Pydantic `SecretStr`: what does it protect?"
    ??? success "Answer"
        Repr and default dumps show `**********`, so secrets don't leak in logs. Use `.get_secret_value()` at the point of use.

??? question "R13. `asyncio.timeout` raises what on expiry?"
    ??? success "Answer"
        The builtin `TimeoutError` (`asyncio.TimeoutError` is an alias since 3.11).

??? question "R14. What does `Queue.shutdown()` (3.13) do?"
    ??? success "Answer"
        Marks the queue closed: `put` raises `QueueShutDown` immediately, and consumers drain remaining items and then get `QueueShutDown`. It ends worker pools without sentinels.

??? question "R15. Which asyncio tool bounds in-flight operations, and which bounds buffered items?"
    ??? success "Answer"
        `Semaphore` bounds in-flight operations. `Queue(maxsize=n)` bounds buffered items (and makes `put` wait, which gives backpressure).

??? question "R16. Why keep a reference to `create_task()` results?"
    ??? success "Answer"
        The loop holds only weak references, so an un-referenced task can be garbage-collected mid-flight.

??? question "R17. What replaced `on_event('startup')` in FastAPI?"
    ??? success "Answer"
        The `lifespan` async context manager passed to `FastAPI(lifespan=...)`.

??? question "R18. Where do plain `def` FastAPI endpoints run?"
    ??? success "Answer"
        In AnyIO's worker threadpool (default 40 tokens).

??? question "R19. Which start method is the Linux default for `multiprocessing` in 3.14?"
    ??? success "Answer"
        `forkserver`.

??? question "R20. Which module gives an `InterpreterPoolExecutor` in 3.14?"
    ??? success "Answer"
        `concurrent.futures` (with `concurrent.interpreters` from PEP 734).

??? question "R21. What flag enables an extension-safe check for the GIL being off in CI?"
    ??? success "Answer"
        Assert `sys._is_gil_enabled()` is False on the 3.14t job (or run with `PYTHON_GIL=0`/`-X gil=0` to force and surface incompatibilities).

??? question "R22. pytest: how do you run only fast tests?"
    ??? success "Answer"
        Mark slow ones (`@pytest.mark.integration`) and run `pytest -m "not integration"` with `--strict-markers` registered.

??? question "R23. Hypothesis: what does shrinking do?"
    ??? success "Answer"
        Reduces a failing input to a minimal counterexample, and stores it in the example database for replay.

??? question "R24. `itertools.batched` first appeared in which version?"
    ??? success "Answer"
        3.12 (with `strict=` added in 3.13).

??? question "R25. Why wrap async generators in `aclosing`?"
    ??? success "Answer"
        Deterministic `aclose()` on early exit, so upstream streams and `finally` blocks run promptly instead of at GC/loop finalisation.

??? question "R26. `cached_property` on a class with `__slots__`?"
    ??? success "Answer"
        Doesn't work (needs an instance `__dict__`), unless you include `__dict__` in slots or use another caching approach.

??? question "R27. Which tool would you reach for to see what a live production Python process is doing without code changes?"
    ??? success "Answer"
        `py-spy dump`/`top`/`record` (needs ptrace permission), or in 3.14 `python -m asyncio ps/pstree PID` for asyncio task trees.

??? question "R28. What is Arrow's role between Polars and DuckDB?"
    ??? success "Answer"
        The shared columnar memory format that lets them exchange tables zero-copy.

??? question "R29. Why is `time.sleep` in `async def` a bug, and which ruff rule flags it?"
    ??? success "Answer"
        It blocks the event loop for all tasks. Ruff `ASYNC251` (blocking sleep in async function), part of the `ASYNC` family.

??? question "R30. Metrics label you must never use?"
    ??? success "Answer"
        Unbounded/high-cardinality values (user ID, prompt hash, raw URL with IDs). Use bounded labels and keep identifiers in traces/logs.
