---
title: "Design patterns that still matter (GoF, modern)"
track: architecture
slug: design-patterns
priority: P1
complexity: 2
est_hours: 3
phase: 1
tags: [architecture, P1]
last_reviewed: 2026-09-25
---

# Design patterns that still matter (GoF, modern)

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 2/5 · **Est. time:** 3 h · **Phase:** 1 · **Prereqs:** [SOLID & refactoring](solid-refactoring.md), [Advanced typing](../python/typing-advanced.md)
    **You're done when:** you can name the ~10 patterns that actually recur in production code, show idiomatic Python and Java forms (including where the language makes the pattern disappear), and pick the right one for a forces-based problem, including AI-era cases (strategy for model routing, decorator for LLM middleware).

## Why it matters

The 23 GoF patterns are 30 years old, but the *forces* behind them (vary this without touching that) are permanent. In 2026 the value is in three skills: recognising patterns in frameworks you didn't write (FastAPI dependencies, Spring AOP, LangGraph nodes), knowing which patterns your language has already absorbed (first-class functions replace Strategy/Command/Observer in Python), and avoiding pattern-fever. Interviews for Staff roles use patterns as a shared language for low-level design and code review.

Patterns also map cleanly onto LLM application code: strategy (model selection), decorator/chain-of-responsibility (middleware for retry, cache, guardrails), adapter (provider SDKs), template method (agent loops), observer (event streaming to UI), state (conversation/workflow phase).

## Core concepts

### Pattern = problem + forces + consequences

A pattern is not code to copy; it is a named solution to a recurring tension with known trade-offs. Always state: *what varies?* *what must stay stable?* *what does this cost?* (indirection, more types, harder debugging).

### The ones that recur (and their modern shape)

| Pattern | Forces | Python form | Java form | Watch-out |
|---|---|---|---|---|
| **Strategy** | Swap an algorithm at runtime | A callable / `Protocol` | Interface + lambdas | Over-abstracting a single implementation |
| **Adapter** | Make an incompatible interface fit | Small class wrapping SDK behind a `Protocol` | Class implementing your interface | Leaky adapters that mirror the vendor API |
| **Decorator** | Add behaviour without changing the class; stackable | `@decorator` functions, wrapper classes | Wrapper classes, Spring AOP | Order of stacking matters (cache before retry?) |
| **Factory / Abstract factory** | Choose concrete type from config | Function returning instance, registry dict | Static factory, `ServiceLoader`, Spring `@Bean` | Reflection-heavy factories hide dependencies |
| **Builder** | Many optional parameters, staged construction | `dataclass` with defaults, Pydantic, keyword args | Records + builder, Lombok/Immutables | Unneeded in Python; use kwargs |
| **Observer / pub-sub** | Notify many of a change, decoupled | Callbacks, `asyncio.Queue`, signals, event bus | `ApplicationEventPublisher`, `Flow` | Hidden control flow, memory leaks (unregistered listeners) |
| **Command** | Encapsulate a request (queue, undo, log) | Dataclass + handler function | Record + handler | Prefer plain functions unless serialising |
| **State** | Behaviour varies by state machine | Enum + `match`, or state classes | Sealed interface + pattern matching | Ad hoc `if status ==` sprawl |
| **Template method** | Fixed skeleton, variable steps | Base class hooks *or* pass functions | Abstract class | Inheritance coupling; prefer strategy composition |
| **Chain of responsibility / middleware** | Pipeline of handlers each may act/stop | List of callables (ASGI middleware) | Filter chain, interceptors | Debugging order and short-circuiting |
| **Facade** | Simple API over a complex subsystem | Module with a few functions | Service class | Becoming a god class |
| **Proxy** | Control access (lazy, caching, auth, remote) | `__getattr__`, wrapper classes | Dynamic proxies (Spring) | Surprising behaviour, hard debugging |
| **Composite** | Treat tree of objects uniformly | Recursive classes | Interface + composite | Rare; useful for rule trees, UI, ASTs |
| **Iterator / generator** | Traverse lazily | Generators | Streams | Built into languages |
| **Singleton** | One instance | Module-level object | DI container scope | Global state, testability nightmare — prefer DI |

### Patterns the language has already absorbed

- **Python**: Strategy, Command, Observer, Iterator, Template Method (as passing functions), Singleton (modules) collapse into first-class functions, generators and modules. Writing a `PaymentStrategy` ABC with one method where a function would do is a Java accent in Python.
- **Java 21–25**: records, sealed interfaces and pattern-matching `switch` make **Visitor** largely obsolete for closed hierarchies, and give **State**/algebraic data types a native form; lambdas absorb Strategy/Command.

```python
# Strategy as a function type — model routing
from typing import Callable, Protocol
from dataclasses import dataclass

@dataclass(frozen=True)
class Request:
    prompt: str
    needs_reasoning: bool
    max_cost_usd: float

RouteFn = Callable[[Request], str]           # returns a model id

def cheapest(_: Request) -> str: return "small-model"
def by_complexity(r: Request) -> str:
    return "reasoning-model" if r.needs_reasoning else "small-model"

class Router:
    def __init__(self, strategy: RouteFn): self.strategy = strategy
    def route(self, r: Request) -> str: return self.strategy(r)
```

```java
// Java 21+: sealed types + pattern matching replace Visitor / State classes
sealed interface BookingState permits Draft, Confirmed, Shipped, Cancelled {}
record Draft() implements BookingState {}
record Confirmed(Instant at) implements BookingState {}
record Shipped(String vessel) implements BookingState {}
record Cancelled(String reason) implements BookingState {}

static String describe(BookingState s) {
    return switch (s) {                 // compiler checks exhaustiveness
        case Draft d -> "Not yet confirmed";
        case Confirmed c -> "Confirmed at " + c.at();
        case Shipped sh -> "On " + sh.vessel();
        case Cancelled x -> "Cancelled: " + x.reason();
    };
}
```

### Decorator/middleware for LLM calls

A pipeline of decorators is the cleanest way to add cross-cutting behaviour to LLM calls without polluting business code:

```python
import time, hashlib
from typing import Protocol

class LLM(Protocol):
    def complete(self, prompt: str) -> str: ...

class Retrying:
    def __init__(self, inner: LLM, attempts=3): self.inner, self.attempts = inner, attempts
    def complete(self, prompt):
        for i in range(self.attempts):
            try: return self.inner.complete(prompt)
            except TimeoutError:
                if i == self.attempts - 1: raise
                time.sleep(2 ** i)

class Cached:
    def __init__(self, inner: LLM, store: dict): self.inner, self.store = inner, store
    def complete(self, prompt):
        k = hashlib.sha256(prompt.encode()).hexdigest()
        return self.store.setdefault(k, self.inner.complete(prompt))

class Guarded:                                # output guardrail
    def __init__(self, inner: LLM, check): self.inner, self.check = inner, check
    def complete(self, prompt):
        out = self.inner.complete(prompt)
        if not self.check(out): raise ValueError("guardrail violation")
        return out

llm: LLM = Guarded(Cached(Retrying(RealLLM()), {}), check=no_pii)   # order is a design decision
```

Order: cache before retry (don't cache errors, don't retry cache hits); guardrails outermost so they see final output. Same idea as ASGI/Starlette middleware, Spring interceptors and LiteLLM callbacks.

### Patterns in the frameworks you use (recognition skill)

| Framework | Pattern |
|---|---|
| FastAPI `Depends` | Dependency injection + factory; scoped lifetimes |
| Starlette/ASGI middleware | Chain of responsibility / decorator |
| SQLAlchemy Session | Unit of Work + Identity Map |
| Spring AOP (`@Transactional`, `@Retryable`) | Proxy + decorator |
| Spring AI advisors | Chain of responsibility around chat calls |
| LangGraph | State machine (graph) + reducers; nodes are commands |
| Pydantic AI tools | Command/registry, dependency injection via `RunContext` |
| Kafka consumers | Observer/competing consumers |
| Pytest fixtures | Dependency injection, template method |

### Choosing: a decision guide

| Symptom | Consider |
|---|---|
| `if/elif` on a type/flag in many places | Polymorphism / Strategy / State (or sealed types + match) |
| Constructor with 10 optional args | Builder (Java) / kwargs + dataclass (Python) |
| Cross-cutting behaviour repeated at call sites | Decorator / middleware / AOP |
| Third-party API shape leaking into your code | Adapter behind a port |
| Need to undo/queue/log actions | Command |
| Many things must react to one event | Observer / event bus |
| Complex subsystem, callers need 3 operations | Facade |

### Senior-level nuance

- **Patterns are vocabulary for reviews, not a design method.** Start from forces; a pattern name is a shortcut for communicating the result.
- **Indirection has a cost** — each pattern adds names, files and stack frames. Add it at the second real variation, not the first (rule of three; YAGNI).
- **Prefer composition over inheritance**; template method via inheritance is fragile.
- **Anti-patterns are patterns too**: God object, Service Locator, Singleton-as-global, Anemic domain in a core context, Golden hammer.
- **Beyond GoF**: enterprise patterns (Fowler's PoEAA: Repository, Unit of Work, Identity Map, Data Mapper), concurrency patterns (producer-consumer, actor), resilience patterns (circuit breaker, bulkhead) and cloud patterns are more relevant day to day for architects than Flyweight or Memento.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Refactoring.Guru — Design Patterns](https://refactoring.guru/design-patterns) | docs | Best-illustrated catalogue with Python and Java examples and pros/cons | intermediate | free/freemium |
| [The Python Patterns Guide (Brandon Rhodes)](https://python-patterns.guide/) :gem: | docs | Which GoF patterns survive in Python and how they change; rare, thoughtful | advanced | free |
| [Composition over Inheritance (Rhodes)](https://python-patterns.guide/gang-of-four/composition-over-inheritance/) :gem: | article | Sharp argument with concrete Python examples | intermediate | free |
| [Game Programming Patterns (Robert Nystrom)](https://gameprogrammingpatterns.com/) :gem: | book | The clearest patterns writing anywhere; free online; applies well beyond games | intermediate | free |
| [Design Patterns (GoF)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) | book | The source; read for forces and consequences, skip the C++ | advanced | paid |
| [Patterns of Enterprise Application Architecture (Fowler catalog)](https://martinfowler.com/eaaCatalog/) | docs | Repository, Unit of Work, Data Mapper and friends | intermediate | free |
| [Cosmic Python](https://www.cosmicpython.com/) | book | Repository/UoW/service layer/message bus patterns in idiomatic Python | intermediate | free |
| [Azure Architecture Center — cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) | docs | Resilience, messaging and data patterns with when-not-to-use | intermediate | free |
| [Refactoring catalog (Fowler)](https://refactoring.com/catalog/) | docs | Move from smell to pattern via small refactorings | intermediate | free |

## Hands-on lab

**Goal:** refactor a messy LLM call site into patterns. 60–90 min.

1. Start with a function that builds a prompt, calls a provider SDK, retries in a loop, caches in a global dict and logs — 120 lines.
2. Extract an **Adapter** (`LLM` protocol + provider class).
3. Turn retry, cache, logging and guardrail into **Decorators**; compose them in a factory.
4. Replace an `if provider == ...` chain with a **Strategy** registry.
5. Model conversation phases (`Collecting`, `Confirming`, `Done`) as **State** using an enum + `match`, then as sealed types in a Java snippet.
6. Add tests: fake LLM, assert decorator order behaviour (cache hit skips retry; guardrail sees final output).
7. Write down what you did *not* abstract and why.

**Expected output:** a small package with tests, and a table mapping each refactoring to the force it resolves.

## Questions

### L1 — Recall

??? question "Q1. Which GoF patterns are mostly absorbed by first-class functions in Python?"
    ??? success "Answer"
        Strategy, Command, Template Method (via passed callables), Observer (callbacks), and often Factory (functions returning objects). Iterator is absorbed by generators, Singleton by modules. A class hierarchy for a single-method strategy is usually unnecessary.

??? question "Q2. What is the difference between Decorator and Proxy?"
    ??? success "Answer"
        Both wrap an object with the same interface. Decorator adds behaviour/responsibilities (logging, retry, caching) and is typically stackable by the client. Proxy controls access to the object (lazy loading, remote call, access control, caching as access control) and usually manages the subject's lifecycle itself. Intent differs more than structure.

??? question "Q3. State two problems with Singleton in modern code."
    ??? success "Answer"
        Hidden global state makes testing hard (shared mutable state across tests, impossible to substitute) and couples code to a concrete instance; concurrency issues in initialisation and access. Prefer dependency injection with a scoped lifetime (singleton scope in the container) so consumers depend on an interface.

### L2 — Apply

??? question "Q4. Implement a middleware chain for LLM calls with retry, cache and guardrail; where does each go and why?"
    ??? success "Answer"
        Outermost: guardrail (must validate the final output, whether from cache or model, and block unsafe content). Next: cache (avoid model calls and cost; cached responses never trigger retries). Innermost: retry (only for calls hitting the model; transient errors). Add timeout at the innermost layer and observability (tracing) outermost to time the whole. Rationale: caching failures or retrying cached hits are bugs; guardrails after cache protect against poisoned entries.

??? question "Q5. A `NotificationService` has `if channel == 'email' ... elif 'sms' ... elif 'slack'` repeated in four methods. Refactor."
    ??? success "Answer"
        Introduce a `Channel` protocol with `send(recipient, message)`, implementations per channel, and a registry/factory keyed by channel name (config-driven). The service depends on the protocol; adding WhatsApp = one new class + registration (Open/Closed). If the variation is only a function (no state), use a dict of callables. Add a test per channel and a contract test for the protocol. Don't add a Factory class in Python if a dict suffices.

??? question "Q6. Model an order lifecycle (Draft → Paid → Shipped → Delivered/Cancelled) in Python so illegal transitions are impossible to code by accident."
    ??? success "Answer"
        Option 1: Enum + transition table `{Draft: {Paid, Cancelled}, ...}` and a `transition(order, to)` method that raises on invalid moves; simple and inspectable. Option 2: separate immutable state objects (`Draft`, `Paid(paid_at)`, ...) with methods only valid for that state (`Paid.ship()`), typed with `Union` so type checkers flag misuse. Option 3: `match` over the state in the aggregate methods. Emit domain events on transitions. In Java, sealed interface + records + exhaustive switch.

### L3 — Design & trade-offs

??? question "Q7. Inheritance-based Template Method vs Strategy for an agent loop (plan → act → observe → evaluate). Choose."
    ??? success "Answer"
        Strategy/composition. The skeleton (loop with budget, tracing, error handling, stop conditions) is stable; the varying parts (planner, tool executor, evaluator) become injected collaborators. Template method via inheritance couples subclasses to the base's internal order, makes testing require subclassing, and complicates mixing variations (e.g. reflective evaluator + parallel tools). With composition you can test each piece, swap them per tenant, and wrap the loop with decorators. Use inheritance only if variation is tiny and the base class is stable and owned by you.

??? question "Q8. Your team wants an abstract factory + builder + strategy for a component that has exactly one implementation today. Respond."
    ??? success "Answer"
        Ask what force justifies each abstraction now. With one implementation and no known second, abstractions are speculative generality: they add files, indirection and cognitive load and often guess the wrong seam. Recommend the simplest code, isolate the volatile dependency (if any, e.g. vendor SDK) behind one thin port, and introduce the second abstraction when a second implementation appears (rule of three). Keep the code refactorable through tests. Exception: public library APIs or boundaries expected to be extended by others.

??? question "Q9. Observer/event bus vs direct calls between modules in a modular monolith: decide."
    ??? success "Answer"
        Use direct calls (module APIs) for queries and commands needing immediate results; use in-process domain events for reactions where the publisher shouldn't know consumers (e.g. `BookingConfirmed` → invoicing, notifications). Costs of events: hidden control flow, ordering, error handling (what if a handler fails?), transaction semantics. Mitigate: handlers after commit, persisted event publication (outbox-like, e.g. Spring Modulith registry), naming in past tense, tests for handlers, and observability. Balanced coupling: events reduce strength between modules that don't need coordination.

### L4 — Staff-level ambiguity

??? question "Q10. A new hire's PRs apply GoF patterns everywhere; reviews are turning into pattern debates. How do you coach and set guidelines?"
    ??? success "Answer"
        Reframe from patterns to forces: in reviews ask "what varies here, and what evidence do we have it will?" Provide a short team guideline: prefer functions and composition; add abstraction at the second real variation; isolate volatile external dependencies with ports; patterns must be named in the PR description with the force resolved. Pair on a refactoring to show removing an unnecessary abstraction is valued. Provide reading (Nystrom, Rhodes) and examples of code in the repo that's good (simple) and bad (over-engineered). Recognise the learner's enthusiasm; steer, don't shame.

??? question "Q11. How would you build an internal 'LLM middleware' standard so 20 teams get retries, caching, PII redaction and tracing consistently without a mandated framework?"
    ??? success "Answer"
        Provide the cross-cutting concerns at the *gateway* (server-side) where possible: an LLM gateway offering auth, quotas, caching, PII policies, tracing and provider failover — language-agnostic, one place to enforce. For client-side patterns, publish a small library per language implementing decorators around a minimal `LLM` protocol, plus reference templates. Standardise the contract (OpenAI-compatible API or a thin internal one), trace/attribute conventions (OTel GenAI) and the eval harness, not the agent framework. Track adoption and incidents; deprecate duplicated implementations gradually. Guilds maintain the library with clear ownership and semantic versioning.

## Real-world use cases

- **Web frameworks**: middleware chains (ASGI, servlet filters) as chain of responsibility/decorator.
- **Payments**: strategy/adapter per PSP behind a `PaymentGateway`; state pattern for payment status.
- **ORMs**: unit of work, identity map, proxies for lazy loading.
- **LLM platforms**: strategy for routing, decorator for cache/retry/guardrails, adapter for providers, observer for streaming tokens to UI.
- **Workflow engines**: command + state + saga orchestration.

## Pitfalls & anti-patterns

- Pattern-first design; abstractions with a single implementation.
- Java-style class hierarchies in Python where functions suffice.
- Singletons and service locators as hidden globals.
- Inheritance for reuse; deep hierarchies and template methods with many hooks.
- Decorator stacks with unclear order semantics.
- Facades that grow into god classes.
- Event buses that hide critical control flow.

## Checklist

- [ ] I can name ~12 recurring patterns with the force each resolves, without notes
- [ ] I can show which patterns Python and modern Java absorb natively
- [ ] I built an LLM call pipeline with adapter, decorators and strategy
- [ ] I can justify *not* introducing a pattern
- [ ] I answered all L3 questions out loud in < 3 min each
