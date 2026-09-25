---
title: "Evolutionary architecture & fitness functions"
track: architecture
slug: evolutionary-architecture
priority: P1
complexity: 3
est_hours: 2
phase: 4
tags: [architecture, P1]
last_reviewed: 2026-09-25
---

# Evolutionary architecture & fitness functions

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 4 · **Prereqs:** [Coupling & modularity](coupling-modularity.md), [ADRs](adrs.md)
    **You're done when:** you can define fitness functions for at least five architectural characteristics (structural, performance, security, data, AI-quality), wire two into CI, and explain how they turn architectural principles into governance without a review board.

## Why it matters

Architectures are never finished: business, load, regulation, teams and (now) AI models change continuously. Ford, Parsons and Kua's *Building Evolutionary Architectures* defines an evolutionary architecture as one that "supports guided, incremental change across multiple dimensions". The mechanism for *guiding* is the **fitness function**: an objective, automated (ideally) measure of how close a system is to an architectural goal. It's the architecture equivalent of a unit test.

For Staff/Principal architects this is the answer to "how do you keep 30 teams aligned without a gatekeeping architecture board?": encode principles as executable checks. It also solves an AI-era problem: coding agents produce lots of code quickly; fitness functions give them (and reviewers) immediate, objective feedback on boundary violations, latency regressions and quality drift.

## Core concepts

### Definitions

- **Architectural characteristic** (-ility): what you want to preserve (modularity, performance, security, evaluability...).
- **Fitness function**: any mechanism that provides an objective integrity assessment of a characteristic — a unit test, a metric with threshold, a monitor, a chaos experiment, a manual review with a checklist.
- **Guided evolution**: changes are steered by fitness functions rather than by prohibition or hope.
- **Incremental change**: small, frequently deployable changes are cheaper to validate (continuous delivery is a prerequisite).
- **Appropriate coupling**: few, well-defined integration points (see [balanced coupling](coupling-modularity.md)).

### Taxonomy of fitness functions

| Dimension | Options | Example |
|---|---|---|
| Scope | **Atomic** (one characteristic, isolated) vs **holistic** (interaction of several) | Atomic: no cyclic dependencies. Holistic: latency remains under SLO *while* encryption enabled and under 3x load |
| Trigger | **Triggered** (on commit/PR/deploy) vs **continual** (running in production: monitors, chaos) | Triggered: ArchUnit test. Continual: p99 latency alert, Chaos Monkey |
| Result | **Static** (pass/fail, fixed threshold) vs **dynamic** (threshold depends on context) | Dynamic: allowed latency scales with request size |
| Proactivity | **Intentional** (designed up front) vs **emergent** (discovered later) | Emergent: found after incident that cold starts break SLO |
| Coverage | **Automated** vs **manual** | Manual: quarterly security architecture review (still a fitness function) |
| Audience | **Domain-specific** | Regulatory compliance checks, data residency verification |

### Examples by characteristic

| Characteristic | Fitness function | Implementation |
|---|---|---|
| Modularity | No cycles between modules; domain doesn't import adapters | import-linter contracts / ArchUnit / jMolecules in CI |
| Encapsulation | Only `module.api` may be imported by other modules | import-linter `forbidden` contract |
| Dependency hygiene | No dependency older than N months; no banned licences | Dependabot/Renovate + SBOM checks |
| Performance | p95 of `/quote` < 300 ms in staging at 500 rps | k6/Locust job in the pipeline; SLO monitors in prod |
| Scalability/elasticity | Service scales from 2 → 20 pods with < 5% error during ramp | Load test + autoscaler assertions |
| Resilience | Booking API remains available when Payment is down (degraded mode) | Chaos test / fault injection in pre-prod, game days |
| Security | No secrets in repo; no public buckets; deps without critical CVEs | gitleaks, policy-as-code (OPA/Conftest), trivy |
| Data | Every table has an owner; PII columns encrypted; schema changes backward-compatible | Schema lint, migration checks (expand/contract) |
| API compatibility | No breaking OpenAPI/proto changes without version bump | oasdiff/buf breaking in CI |
| Cost | Cost per booking < $0.02; LLM cost per task within budget | Cost dashboards with alert thresholds |
| Team cognitive load | Services per team ≤ N; on-call load within threshold | Catalogue metadata + reports |
| **AI quality** | Eval score ≥ baseline on golden set; no regression on safety set; hallucination rate below X | Eval suite in CI (promptfoo/DeepEval/Inspect); production sampling with LLM-judge |
| **AI cost/latency** | p95 time-to-first-token < 1.2 s; cost per task < $0.05 | Trace-based metrics with alerts |

### Structural fitness functions in code

Python (import-linter):

```ini
[importlinter]
root_packages = booking, invoicing, tracking

[importlinter:contract:layers]
name = Layered architecture inside each module
type = layers
layers =
    booking.entrypoints
    booking.application
    booking.domain

[importlinter:contract:domain-purity]
name = Domain must not import frameworks or SDKs
type = forbidden
source_modules = booking.domain
forbidden_modules = sqlalchemy, fastapi, openai, pydantic_ai

[importlinter:contract:module-boundaries]
name = Modules only talk through their api package
type = forbidden
source_modules = invoicing, tracking
forbidden_modules = booking.domain, booking.adapters, booking.application
```

Java (ArchUnit):

```java
@ArchTest
static final ArchRule domain_is_framework_free =
    noClasses().that().resideInAPackage("..domain..")
        .should().dependOnClassesThat().resideInAnyPackage(
            "org.springframework..", "jakarta.persistence..", "org.springframework.ai..");

@ArchTest
static final ArchRule no_cycles = slices().matching("com.acme.(*)..").should().beFreeOfCycles();
```

Behavioural, holistic example (pytest + k6-style check):

```python
def test_quote_latency_under_slo(load_env):
    result = run_load(endpoint="/quote", rps=500, duration_s=120)
    assert result.p95_ms < 300
    assert result.error_rate < 0.001
```

### AI-quality fitness functions

LLM systems drift silently (model updates, prompt edits, data drift). Encode expectations:

```yaml
# promptfoo-style CI gate (conceptual)
tests:
  - description: Delay explanations mention cause and new ETA
    vars: { events: file://fixtures/delay_1.json }
    assert:
      - type: contains-any
        value: ["port congestion", "weather"]
      - type: llm-rubric
        value: "States a new ETA and does not invent vessel names"
      - type: cost
        threshold: 0.01
      - type: latency
        threshold: 3000
```

Gate merges on eval regressions vs baseline; run a sample of production traces nightly through an LLM-judge and alert on trend breaks. See [eval tooling](../agentic-ai/eval-tooling.md).

### Making evolution possible: enablers

- **Continuous delivery** with fast pipelines; feature flags; trunk-based development.
- **Expand/contract (parallel change)** for schemas and APIs: add new, migrate consumers, remove old — see [API contracts](api-contracts-versioning.md).
- **Testing pyramid** with contract tests between services.
- **Observability** to power continual fitness functions.
- **Small, independently deployable units** — connects to architecture style.
- **Last responsible moment** decisions with reversible options (ports/adapters).
- **Data evolution**: migrations as code; schema compatibility checks; event upcasting.

### Governance with fitness functions

Traditional governance: review board approves designs (slow, subjective, scaled poorly). Fitness-function governance: architects define *the rules as code and metrics*; teams get immediate feedback; humans review only the exceptions. Keep an **inventory** mapping each architecture principle/ADR → its fitness function(s) → owner → status (automated/manual). Principles without any check are wishes.

| Principle (from ADR) | Fitness function | Trigger | Owner |
|---|---|---|---|
| Domain layer is framework-free | import-linter `domain-purity` | PR | Each team |
| Events published via outbox only | Test: no producer client used outside outbox relay; outbox table exists | PR | Platform |
| p95 latency SLO | k6 in staging + prod SLO alert | Nightly + continual | Service owner |
| No unapproved LLM provider egress | Egress policy test / network policy | Deploy | Security |
| AI answers grounded | Eval faithfulness ≥ 0.9 on golden set | PR (prompt/model change) | AI feature team |

### Senior-level nuance

- **Start with 3–5 fitness functions that guard your top characteristics**; don't boil the ocean. Each one should relate to an ADR or quality scenario.
- **Fitness functions must be fast and reliable** or people will disable them. Flaky performance tests are worse than none — use ratchets/trends instead of hard thresholds when noisy.
- **Ratchet pattern**: fail if the metric worsens (e.g. cycle count, error count) relative to the baseline; makes legacy cleanup incremental.
- **Holistic functions** catch the conflicts atomic ones miss (security vs performance).
- **Review the fitness functions**: business goals shift; retire obsolete checks.
- **Make failures actionable**: a message stating the rule, why it exists (ADR link) and how to fix or request an exception.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Building Evolutionary Architectures, 2nd ed. (Ford, Parsons, Kua, Sadalage)](https://evolutionaryarchitecture.com/) | book | The origin of fitness functions, with a catalogue and case studies | intermediate | paid |
| [Fitness function-driven development (Thoughtworks)](https://www.thoughtworks.com/insights/articles/fitness-function-driven-development) | article | Short applied introduction including sample functions | intermediate | free |
| [ArchUnit](https://www.archunit.org/) | docs | Java architecture tests: layers, cycles, naming, annotations | intermediate | free |
| [import-linter](https://import-linter.readthedocs.io/) :gem: | docs | Python contract-based dependency rules; layers, forbidden, independence | intermediate | free |
| [jMolecules](https://www.jmolecules.org/) | docs | Annotations to express architecture concepts and verify them automatically | intermediate | free |
| [Spring Modulith](https://docs.spring.io/spring-modulith/reference/) | docs | Module verification tests as fitness functions for modular monoliths | intermediate | free |
| [Continuous Architecture](https://continuousarchitecture.com/) :gem: | article/book | Complementary view on architecture in continuous delivery contexts | intermediate | mixed |
| [Parallel Change (Fowler)](https://martinfowler.com/bliki/ParallelChange.html) | article | Expand/contract technique enabling safe evolution of interfaces | intermediate | free |
| [Refactoring Databases / Evolutionary DB Design (Fowler)](https://martinfowler.com/articles/evodb.html) | article | Evolving schemas safely with migrations | intermediate | free |
| [promptfoo docs](https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/) | docs | Eval/red-team assertions as CI gates for AI features | intermediate | free |

## Hands-on lab

**Goal:** stand up an architecture-governance pipeline with 5 fitness functions. 90 min.

1. In the capstone repo, list 5 principles (from ADRs or your own): domain purity, module boundaries, API compatibility, latency SLO, AI eval gate.
2. Implement structural functions via import-linter (two contracts) and confirm a deliberate violation fails CI with a helpful message linking the ADR.
3. Add API-compat check: generate OpenAPI in CI and diff vs main using `oasdiff` (or a simple JSON-schema diff script); fail on breaking changes.
4. Add a small load test (Locust/k6) asserting p95 under a threshold on a local stack; store the trend and use a ratchet for noise.
5. Add an eval gate: 15 golden examples run via promptfoo/DeepEval with pass rate ≥ baseline − 2%.
6. Create `docs/architecture/fitness-functions.md` inventory (principle → function → trigger → owner).
7. Ask a coding agent to make a change crossing a boundary; observe the check catching it and the agent's correction.

**Expected output:** CI pipeline with 5 gates, an inventory table, and a screenshot/log of a caught violation.

## Questions

### L1 — Recall

??? question "Q1. Define an architectural fitness function and give two examples of different kinds."
    ??? success "Answer"
        An objective, ideally automated assessment of how well the system meets an architectural characteristic. Examples: an ArchUnit/import-linter test asserting no dependency cycles (atomic, triggered, structural); a production SLO monitor on p99 latency (continual); a chaos experiment verifying graceful degradation (holistic, continual); an eval gate for LLM output quality (domain-specific).

??? question "Q2. Distinguish atomic vs holistic and triggered vs continual fitness functions."
    ??? success "Answer"
        Atomic checks one characteristic in isolation; holistic checks combinations (e.g. latency under load *with* encryption on). Triggered runs on an event (commit, PR, deploy); continual runs constantly in production (monitors, synthetic checks, chaos engineering).

??? question "Q3. What does 'incremental change' require of the delivery pipeline?"
    ??? success "Answer"
        Continuous integration/delivery with fast, automated build and test, deployment automation and rollbacks, feature flags, trunk-based development and safe database/API change patterns (expand/contract). Without it, changes batch up, risk grows and fitness feedback comes too late.

??? question "Q4. What is the ratchet pattern?"
    ??? success "Answer"
        A fitness function that permits the current level of a violation metric but fails if it gets worse (e.g. count of forbidden imports must not increase). It enables incremental improvement of legacy code without a big-bang cleanup and reduces noise from strict absolute thresholds.

### L2 — Apply

??? question "Q5. Write fitness functions for: 'The Booking module must not depend on Invoicing internals' and 'Response p95 < 300 ms'."
    ??? success "Answer"
        Structural: import-linter `forbidden` contract with `source_modules = booking` and `forbidden_modules = invoicing.domain, invoicing.adapters` (or ArchUnit rule `noClasses().that().resideInAPackage("..booking..").should().dependOnClassesThat().resideInAPackage("..invoicing.internal..")`). Performance: a load test in the pipeline (k6/Locust) asserting p95 < 300 ms at target RPS in staging, with a production SLO monitor/alert as continual counterpart; use a rolling baseline for noise tolerance.

??? question "Q6. Your team migrates from OpenAI model A to model B. Which fitness functions protect quality, cost and latency?"
    ??? success "Answer"
        Quality: golden-set eval with task metrics and LLM-judge rubric, safety/refusal set, regression threshold vs model A baseline; Cost: cost-per-task metric from traces with a budget assertion; Latency: p95 TTFT and total latency measured on representative prompts; Behavioural: structured-output validity rate (% parseable), tool-call correctness; Production: shadow/A-B traffic comparison and continual sampling with alerts. Gate the switch behind these thresholds and keep a rollback via the LLM gateway.

??? question "Q7. How would you detect that an 'API compatibility' principle is being violated automatically?"
    ??? success "Answer"
        Generate the OpenAPI spec (or use proto/AsyncAPI) from code in CI and diff against the version on main using a breaking-change detector (oasdiff, buf breaking, Confluent schema registry compatibility check). Fail on breaking changes unless version bump/deprecation process is followed; add consumer-driven contract tests (Pact) to detect breakage of actual consumers' expectations that specs don't capture.

### L3 — Design & trade-offs

??? question "Q8. Fitness functions vs an architecture review board: compare and design a hybrid."
    ??? success "Answer"
        ARB: flexible, handles novelty and judgement, but slow, subjective, a bottleneck, and reviews design not implementation. Fitness functions: scalable, objective, immediate, continuous, but limited to what is measurable and needs upfront effort. Hybrid: automate everything measurable (structural rules, SLOs, compat, security policies); reserve human review for decisions crossing team boundaries or with high risk (advice process + ADRs), and have the review examine exceptions and propose new fitness functions where recurring issues appear. Success metric: fewer meetings, fewer violations, faster lead time.

??? question "Q9. Performance fitness functions in CI are flaky. How do you keep them useful?"
    ??? success "Answer"
        Use dedicated, stable environments; measure relative changes vs baseline on the same infra rather than absolute numbers; run multiple iterations and compare distributions (e.g. median of p95 across 3 runs); use ratchets/trend alerts instead of hard gates on noisy metrics; separate micro-benchmarks (deterministic operation counts, allocations) from load tests; run heavy tests nightly and gate on *significant* regressions; complement with production SLO monitoring as the truth source.

??? question "Q10. Design the set of fitness functions for a multi-tenant LLM gateway."
    ??? success "Answer"
        Security: tenant isolation tests (one tenant can't read another's cache/logs/keys), prompt/response logging redaction verified with seeded PII; Reliability: provider failover test (kill provider A → traffic routes to B within X s with < Y% errors); Performance: gateway overhead p99 < 30 ms; Cost governance: quota enforcement tests and budget alerts, cost attribution completeness (100% requests tagged with tenant/team); Compatibility: OpenAI-compatible API contract tests with recorded fixtures; Observability: every request has a trace with model, tokens, cost; Structural: no provider SDK imports outside adapters. Mix of triggered (CI) and continual (canaries, synthetic probes).

### L4 — Staff-level ambiguity

??? question "Q11. You are asked to roll out fitness functions to 25 teams with different stacks. How do you get adoption without becoming the bottleneck?"
    ??? success "Answer"
        Start with the *why*: pick 3 high-value org-level characteristics tied to pain (e.g. lost events, breaking API changes, cost). Provide paved-road implementations per stack (Python import-linter template, Java ArchUnit library, CI reusable workflows) so adoption is "add a line". Publish the inventory with owners; make checks warn-only first, then ratchet to fail; give exceptions a lightweight process with expiry. Recruit champions in 3 pilot teams, share measurable wins (incidents avoided, review time saved), and support via a guild/office hours. Avoid mandating uniform tools; standardise the *characteristics* and reporting format. Revisit quarterly to retire unhelpful checks.

??? question "Q12. A fitness function blocks a critical release at 5 pm on a Friday; the VP asks you to disable it. What do you do and what do you change afterwards?"
    ??? success "Answer"
        In the moment: assess the actual risk — what does the failing check protect (e.g. breaking API change affecting partners?). If the risk is acceptable and time-critical, grant a *time-boxed, recorded exception* (owner, expiry, follow-up ticket) rather than deleting the check; involve the decider named in the ADR. Afterwards: run a retro — was the check right but the timing poor (should run earlier in the pipeline, e.g. on PRs)? Was it flaky or too strict? Adjust: move earlier, add an exception mechanism with SLA, add a dashboard of exceptions. The principle: exceptions are explicit and expiring; silent disabling destroys trust in governance.

## Real-world use cases

- **Netflix-style chaos engineering**: resilience as a continual fitness function.
- **Modular monoliths (Shopify Packwerk, Spring Modulith)**: automated boundary verification.
- **Fintech**: compliance-as-code (policy checks for data residency, encryption) gating deployments.
- **API platforms**: breaking-change detection (buf, oasdiff) as merge gates.
- **LLM products**: eval suites as regression gates for prompts and model upgrades; cost/latency budgets on traces.

## Pitfalls & anti-patterns

- Fitness functions without an owner or link to a principle/ADR.
- Flaky tests that teams learn to ignore or disable.
- Only structural checks, ignoring runtime characteristics and data.
- Exceptions granted informally, never expiring.
- Metrics theatre: dashboards nobody acts on.
- Using fitness functions to enforce taste rather than characteristics.
- No CI/CD maturity, so "continuous" checks run monthly.

## Checklist

- [ ] I can define fitness functions and classify them (atomic/holistic, triggered/continual)
- [ ] I wired structural, API-compat, performance and AI-eval checks into CI
- [ ] I maintain an inventory mapping principles/ADRs to fitness functions
- [ ] I can explain fitness-function governance vs review boards
- [ ] I answered all L3 questions out loud in < 3 min each
