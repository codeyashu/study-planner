---
title: "Iterators, generators & context managers"
track: python
slug: generators-context-managers
priority: P1
complexity: 2
est_hours: 2
phase: 1
tags: [python, P1]
last_reviewed: 2026-09-25
---

# Iterators, generators & context managers

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 2/5 · **Est. time:** 2 h · **Phase:** 1 · **Prereqs:** [Data model](data-model.md)
    **You're done when:** you can build lazy, memory-bounded streaming pipelines with (async) generators, write correct `@contextmanager`/`@asynccontextmanager` resources with exception semantics, and explain how `await` is built on generators.

## Why it matters

Streaming is the native shape of LLM workloads: token streams, SSE, chunked document ingestion, paginated APIs, log tails. Generators give you lazy, backpressured pipelines with O(1) memory. Context managers make resource lifetimes (HTTP streams, DB transactions, spans, locks, timeouts) deterministic. Async generators plus `aclosing` are how you avoid paying for tokens nobody reads ([asyncio](asyncio-deep.md)). Understanding generators is also the key to understanding coroutines: `async/await` is generator machinery with a different name (see Beazley, tenthousandmeters #12).

## Core concepts

### Iterator protocol

- Iterable: has `__iter__` returning an iterator. Iterator: has `__next__` (raises `StopIteration`) and `__iter__` returning itself.
- `for` calls `iter(x)` once, then `next()` until `StopIteration`. Iterators are **single-pass**: a consumed generator yields nothing the second time.

```python
g = (x * x for x in range(3))
print(list(g), list(g))     # [0, 1, 4] []
```

- `iter(callable, sentinel)` is underrated: `for chunk in iter(lambda: f.read(8192), b"")`.
- Classic bug: returning an iterator from a method that is expected to be re-iterable (like a `Sequence`). Return a new iterator each call, or a list.

### Generators as coroutines

```python
def gen():
    x = yield 1          # yield is an expression
    print("got", x)
    yield 2

g = gen()
print(next(g), g.send("hi"))   # got hi  ->  1 2
```

- `send(v)`, `throw(exc)`, `close()` (raises `GeneratorExit` at the yield point; the generator must not yield again). `finally` blocks run on close, which happens on garbage collection, but relying on that timing is fragile.
- `yield from sub()` delegates, forwards `send/throw`, and evaluates to the sub-generator's `return` value:

```python
def inner():
    yield "a"; return 42
def outer():
    r = yield from inner()
    print("inner returned", r)
print(list(outer()))     # inner returned 42  ->  ['a']
```

`await` is essentially `yield from` for awaitables. An event loop drives coroutines by calling `send(None)` and receiving futures.

### Lazy pipelines

```python
from collections.abc import Iterable, Iterator
from itertools import batched, islice

def read_lines(path: str) -> Iterator[str]:
    with open(path, encoding="utf-8") as f:       # file closed when the generator finishes/closes
        yield from f

def clean(lines: Iterable[str]) -> Iterator[str]:
    return (l.strip() for l in lines if l.strip())

def chunk_docs(lines: Iterable[str], n: int = 64) -> Iterator[tuple[str, ...]]:
    return batched(lines, n)                       # 3.12+, stdlib; strict=True in 3.13

for batch in islice(chunk_docs(clean(read_lines("corpus.txt"))), 3):
    embed(batch)
```

Memory stays flat regardless of file size, and pulling stops the whole chain (backpressure by construction: nothing runs until the consumer pulls). `itertools` (`islice`, `chain.from_iterable`, `groupby` (needs sorted input!), `tee` (buffers, memory hazard), `batched`, `pairwise`, `accumulate`) is the toolbox.

### Async generators and streaming

```python
from contextlib import aclosing
from collections.abc import AsyncIterator

async def tokens(client, prompt: str) -> AsyncIterator[str]:
    async with client.stream("POST", "/v1/stream", json={"prompt": prompt}) as r:
        async for line in r.aiter_lines():
            if line.startswith("data: "):
                yield line[6:]

async def first_n(prompt: str, n: int) -> list[str]:
    out = []
    async with aclosing(tokens(client, prompt)) as ts:    # deterministic close on early exit
        async for t in ts:
            out.append(t)
            if len(out) == n:
                break                                     # without aclosing, the HTTP stream stays open until GC
    return out
```

Async generators are finalised by the event loop's asyncgen hooks *eventually*, not deterministically. Always wrap in `aclosing()` (or an explicit `async with`) when you may stop early. Also: you cannot `yield` inside a `TaskGroup`/`timeout` block that spans yields without care, because cancellation scope and generator lifetime interact (a known footgun in structured concurrency, see PEP 789 discussion).

### Context managers

```python
from contextlib import contextmanager, asynccontextmanager, ExitStack, suppress
import time, logging

@contextmanager
def timed(label: str):
    t = time.perf_counter()
    try:
        yield
    finally:                                     # runs on success AND exception
        logging.info("%s took %.1f ms", label, (time.perf_counter() - t) * 1e3)

@asynccontextmanager
async def span(tracer, name: str):
    s = tracer.start(name)
    try:
        yield s
    except Exception as e:
        s.record(e); raise                       # re-raise: swallowing changes program behaviour
    finally:
        s.end()
```

Semantics:

- `with` calls `__exit__(exc_type, exc, tb)`. Returning **truthy suppresses** the exception. `@contextmanager` suppresses only if the generator catches the exception and does not re-raise.
- **Forgetting `try/finally` around `yield`** means cleanup is skipped on exceptions:

```python
@contextmanager
def res():
    print("open"); yield; print("close")     # BUG: "close" never prints if the body raises
```

- `ExitStack` / `AsyncExitStack` manage a dynamic number of resources (open N files, enter optional contexts, transfer ownership with `pop_all()`). `suppress`, `closing`, `aclosing`, `nullcontext`, `redirect_stdout`, and `chdir` (3.11) cover common cases.
- 3.13+ / 3.14: parenthesised multi-item `with` is standard, and `except` without brackets (PEP 758) reads better in cleanup code.
- Reentrancy and reuse: generator-based context managers are **single-use**. Class-based managers may be reusable. Check `ContextDecorator` (`@contextmanager` objects can double as decorators, but each call creates a fresh generator).

### contextvars and generators

`contextvars.ContextVar` values follow the task or thread context. Setting a var inside an async generator that's iterated from different tasks can leak or vanish surprisingly. Use `token = var.set(x)` / `var.reset(token)` in `try/finally`, and set request IDs at task entry, not inside long-lived generators.

### Senior nuance

- A generator that holds a resource (file, DB cursor) and is abandoned mid-iteration leaks it until GC. Prefer context managers for resource lifetime and generators for data flow. Combine: `with open(...) as f: for l in f: yield ...` inside a generator.
- `return value` inside a generator is `StopIteration(value)`. Inside an async generator, `return value` is a SyntaxError.
- `yield` inside `try/finally` inside a `contextmanager` when the body does `break` on a generator loop: cleanup runs on close, not at `break`.
- Generator expressions evaluate the *outermost iterable* eagerly, and the rest lazily. Late-binding closure gotcha: `[lambda: i for i in range(3)]` all return 2 (comprehension variable shared).
- `sum(x for x in xs)` vs `sum([x for x in xs])`: the list version is often *faster* for small inputs due to lower overhead, but uses memory. Choose by size.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Python HOWTO: Functional programming (iterators, generators)](https://docs.python.org/3/howto/functional.html) | docs | Clear treatment of the protocols | intermediate | free |
| [contextlib docs](https://docs.python.org/3/library/contextlib.html) | docs | ExitStack, aclosing, suppress semantics | intermediate | free |
| [itertools docs and recipes](https://docs.python.org/3/library/itertools.html) | docs | The recipes section is a masterclass | intermediate | free |
| [David Beazley: Python Concurrency From the Ground Up (PyCon 2015)](https://www.youtube.com/watch?v=MCs5OvhV9S4) :gem: | video | Generators to event loop, live | advanced | free |
| [Beazley: tutorials index](https://www.dabeaz.com/tutorials.html) :gem: | site | Links to his classic generator/coroutine tutorials | advanced | free |
| [Python behind the scenes #12: async/await](https://tenthousandmeters.com/blog/python-behind-the-scenes-12-how-asyncawait-works-in-python/) :gem: | article | Generators, coroutines and the loop, implemented | advanced | free |
| [PEP 789: Preventing task-cancellation bugs by limiting yield in async generators](https://peps.python.org/pep-0789/) | spec | Why yield inside cancel scopes is dangerous | advanced | free |
| [Fluent Python 2e, Part IV](https://www.fluentpython.com/) | book | Iterators, generators, context managers, coroutines | advanced | paid |
| [mCoding (YouTube)](https://www.youtube.com/@mCoding) :gem: | video | Short explainers on generators/itertools gotchas | intermediate | free |

## Hands-on lab

**Goal (45-60 min):** a memory-flat streaming ingest pipeline plus a cancel-safe token stream.

1. Generate a 1 GB text file (or 5M lines). Write `read_lines -> clean -> batched(64) -> fake_embed` as lazy generators. Track peak RSS with `/usr/bin/time -l` (macOS) or `-v` (Linux). **Expected:** peak RSS stays flat (tens of MB) vs `readlines()` loading GBs.
2. Implement `timed()` and an `asynccontextmanager` `span()`. Prove cleanup runs on exception, then delete the `try/finally` and observe skipped cleanup.
3. Async: a fake provider async generator yielding a token every 50 ms and setting a flag in `finally`. Consume 3 tokens with `break`: (a) without `aclosing`, check the flag *immediately* (expected: not yet set, or set only at GC), (b) with `aclosing`, expected: set immediately.
4. Predict then run: `[f() for f in [lambda: i for i in range(3)]]` (expected `[2, 2, 2]`).
5. Write `ExitStack` code that opens a variable list of files and closes all even if the third open fails.

## Questions

### L1 - Recall

??? question "Q1. What does this print?"
    ```python
    g = (x*x for x in range(3))
    print(list(g), list(g))
    ```
    ??? success "Answer"
        `[0, 1, 4] []`. Generators are single-pass iterators. The second `list` finds it exhausted.

??? question "Q2. What is the value of `yield from sub()` as an expression?"
    ??? success "Answer"
        The `return` value of the sub-generator (carried in `StopIteration.value`). It also forwards `send`, `throw` and `close` to the sub-generator.

??? question "Q3. When does a `@contextmanager` generator suppress an exception raised in the `with` body?"
    ??? success "Answer"
        Only if the exception is thrown into the generator at `yield`, the generator catches it, and finishes without re-raising. Otherwise it propagates. Bare `try/finally` around `yield` runs cleanup but doesn't suppress.

??? question "Q4. Why prefer `aclosing()` for async generators?"
    ??? success "Answer"
        Async generator finalisation is scheduled by the event loop hooks and isn't deterministic. On early exit (`break`, exception, cancellation) the generator's `finally` (closing the HTTP stream) might not run promptly. `aclosing` awaits `aclose()` deterministically.

### L2 - Apply

??? question "Q5. What does this print, and why is it a bug?"
    ```python
    @contextmanager
    def res():
        print("open"); yield; print("close")
    try:
        with res(): raise RuntimeError
    except RuntimeError: pass
    ```
    ??? success "Answer"
        Prints only `open`. The exception is thrown into the generator at `yield`, no `try/finally`, so `print("close")` is skipped. Fix: `try: yield` / `finally: print("close")`.

??? question "Q6. Predict the output."
    ```python
    print([f() for f in [lambda: i for i in range(3)]])
    ```
    ??? success "Answer"
        `[2, 2, 2]`. The lambdas close over the variable `i`, not its value, so all see the final value. Fix: `lambda i=i: i` or `functools.partial`.

??? question "Q7. Process a 40 GB JSONL file, calling an LLM per record with 32 concurrent requests, resuming after crashes. Outline the generator/async design."
    ??? success "Answer"
        Sync generator reads lines lazily (with byte-offset checkpoints), `batched()` groups records, an async worker pool (Queue with `maxsize`, 32 workers) consumes batches with a Semaphore, results are appended to an output file with the input offset committed only after results are durably written (at-least-once, idempotent by record ID). Memory is bounded by queue size, and the producer blocks when the queue is full (backpressure).

??? question "Q8. `itertools.groupby` returns groups that look wrong on unsorted input. Explain."
    ??? success "Answer"
        `groupby` groups only **consecutive** equal keys, like Unix `uniq`. Sort by the key first (or use a dict/`defaultdict`). Also, each group iterator is invalidated when you advance the outer iterator, so materialise with `list(g)` if you keep it.

### L3 - Design & trade-offs

??? question "Q9. Generator pipeline vs async queue pipeline vs materialising lists for a 3-stage embed pipeline."
    ??? success "Answer"
        Lists: simplest, fine up to memory limits, no overlap between stages. Sync generators: lazy, O(1) memory, single-threaded flow control, but no parallelism between stages (the slowest stage serialises). Async queues (bounded): stages run concurrently, with explicit backpressure and parallel workers per stage, at the cost of complexity and error/cancellation handling. Choose lists for small data, generators for streaming CPU/IO-light chains, and queues for I/O-heavy stages with different speeds (parse -> embed API -> upsert).

??? question "Q10. Should a repository return `list[T]`, `Iterator[T]`, or `AsyncIterator[T]` for a large query?"
    ??? success "Answer"
        Returning a live cursor iterator ties resource lifetime (connection, transaction) to consumer behaviour, leaking if not exhausted. Safer API: pagination returning `Page[T]`, or an async context-manager that yields the iterator (`async with repo.stream(q) as rows:`), making lifetime explicit. Use lists for bounded results. Document that iterators are single-use. This is a data-model/API design decision that also affects testing (fakes are trivial with lists).

??? question "Q11. Yielding inside `async with asyncio.timeout(...)` in an async generator: what's the risk?"
    ??? success "Answer"
        The generator suspends while the timeout scope is active. The consumer's time then counts against the timeout, and cancellation can be delivered to unrelated code between yields, mis-attributing `CancelledError`/`TimeoutError`. This is why PEP 789 was proposed. Prefer to yield outside cancel scopes (wrap each upstream await in its own scope), or restructure with a Queue between a producer task and the consumer.

### L4 - Staff-level ambiguity

??? question "Q12. A team's streaming endpoint leaks upstream connections during deploys and client aborts. How do you find and fix systematically?"
    ??? success "Answer"
        Reproduce with a test that disconnects mid-stream and asserts the upstream mock saw close. Audit all async generators for `aclosing`/`async with` around upstream streams, and forbid detached `create_task` consumers. Add metrics: open upstream streams gauge, streams closed by reason, and tokens billed but not delivered. Add a lint/review checklist and a shared `stream_relay` utility implementing the right pattern once. Verify in load tests with random client aborts.

??? question "Q13. You're designing a shared library API for streaming LLM responses (text deltas, tool calls, usage). Iterator design decisions?"
    ??? success "Answer"
        Expose an async context manager returning a typed event stream (`async with model.stream(...) as s: async for ev in s`), so lifetime and cleanup are explicit, plus helpers (`await s.get_final()`, `s.text_deltas()`). Events form a discriminated union (text delta, tool call delta, usage, finish) validated by Pydantic. Guarantee cancellation-safety and single-consumption (raise on second iteration with a clear error). Provide a sync facade only if needed, with tests for early-exit, error mid-stream and retry-before-first-token semantics. Document idempotency: retries after partial output are the caller's decision.

## Real-world use cases

- **Token streaming gateways:** async generator relays with `aclosing` cut wasted generation after disconnects.
- **Bulk ingestion:** generator pipelines over JSONL/Parquet row groups keep memory flat for 100M-row backfills.
- **Tracing:** `span()` context managers wrap model/tool calls so exceptions are recorded and spans always end.
- **Transaction scopes (unit of work):** context managers commit/rollback deterministically ([architecture patterns](architecture-patterns-python.md)).

## Pitfalls & anti-patterns

- `@contextmanager` without `try/finally`.
- Consuming an iterator twice.
- Abandoning generators that hold resources; relying on GC timing.
- `groupby` on unsorted data; `tee` buffering unbounded data.
- Materialising with `list()` in the middle of a lazy pipeline.
- Swallowing exceptions in `__exit__` by returning truthy accidentally.
- Yielding inside cancel scopes in async generators.

## Checklist

- [ ] I can explain `send/throw/close`, `yield from`, and how `await` relates to generators
- [ ] I measured flat memory for a lazy pipeline vs a list-based one
- [ ] I demonstrated `aclosing` vs no `aclosing` on an early break
- [ ] I answered all L3 questions out loud in < 3 min each
