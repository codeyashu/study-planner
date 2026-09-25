---
title: Unified interview rubric
tags: [interviews, rubric]
last_reviewed: 2026-09-25
---

# Unified interview rubric

!!! abstract "How to use"
    Five round types, each with 5–6 dimensions scored **1–4**. Descriptors are written for two bars: **Senior** and **Staff**. Score the level you *demonstrated*, against the bar you are targeting.
    - **1** = clear no-hire signal · **2** = lean no-hire · **3** = hire · **4** = strong hire.
    - A "3 at Staff bar" means a Staff interviewer would be comfortable. A 4 at Senior bar is roughly a 2–3 at Staff bar.
    - Use the same rubric at every [checkpoint](checkpoints.md); only the targets change.

## Scale and hiring signal

| Score | Signal | Rule of thumb |
|---|---|---|
| 1 | Strong no | Missing fundamentals or could not make progress without heavy help |
| 2 | Lean no | Got somewhere, but gaps an interviewer would write up as concerns |
| 3 | Hire | Solid, independent, few hints; minor gaps |
| 4 | Strong hire | Drove the conversation, surfaced things the interviewer did not ask about, crisp trade-offs |

A round's **overall** is not the arithmetic mean: any dimension at 1 caps the round at 2; the Staff bar needs no dimension below 3 in SD, AI SD and Staff behavioral.

---

## 1. Coding (DSA)

| Dimension | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **Problem understanding** | Starts coding immediately; misreads problem | Asks some questions; misses key edge cases | Clarifies inputs/outputs/constraints; writes 2–3 examples incl. edge cases | Plus spots the hidden constraint that determines the approach (e.g. value range → counting sort) |
| **Approach & pattern** | No viable approach | Brute force only, or optimal only after hints | Identifies the pattern; states brute force → optimal with complexity before coding | Plus compares two optimal approaches and picks based on constraints |
| **Implementation** | Does not compile / major bugs | Works with notable bugs fixed after hints | Clean, idiomatic Python, correct on first full run or self-corrected | Plus well-named helpers, no dead code, handles edge cases up front |
| **Testing & debugging** | Does not test | Tests only the given example | Dry-runs own edge cases; finds and fixes own bug | Plus systematically picks tests that exercise each branch |
| **Complexity analysis** | Wrong or absent | Correct time, vague space | Correct time and space incl. recursion stack | Plus discusses amortised/average vs worst and practical constants |
| **Communication** | Silent | Narrates sporadically | Thinks aloud continuously; checks in at decision points | Interviewer never has to ask "what are you doing now?" |

**Senior vs Staff bar:** coding bar is largely the same (medium in ~20 min, hard with a hint in ~40). At Staff, communication and trade-off discussion carry more weight; raw speed slightly less.

**Timing targets:** medium: approach in <= 5 min, code in <= 15, test in <= 5. Hard: approach in <= 10, working code in <= 35.

---

## 2. System design

| Dimension | Senior bar (3) | Staff bar (3) | Staff 4 looks like |
|---|---|---|---|
| **Requirements & scope** | Lists functional + non-functional; asks about scale | Negotiates scope; identifies the *one or two* requirements that drive the design; states explicit non-goals | Reframes the problem (e.g. "this is really a write-heavy fan-out problem") and gets buy-in |
| **Estimation** | QPS, storage, bandwidth roughly right | Uses numbers to *make decisions* (e.g. "20 TB/yr → single Postgres is fine for 3 years") | Includes cost ($) and headroom; revisits numbers when design changes |
| **High-level design** | Correct components and data flow; clear API and data model | Clean decomposition with ownership boundaries; picks storage per access pattern with reasons | Evolutionary path: v1 simple, v2 at 10×, what triggers the change |
| **Deep dive** | Goes deep on one component when asked | Proactively picks the riskiest component and goes deep (consistency, hot keys, backpressure) | Quantifies failure modes; discusses exact algorithms/configs (e.g. quorum sizes, TTL, partition key) |
| **Trade-offs** | Mentions pros/cons | Every major choice has named alternatives and a reasoned decision tied to requirements | Frames trade-offs in business terms (cost, time-to-market, team skills, operability) |
| **Reliability & operations** | Mentions replication, retries | Failure modes, degradation, idempotency, observability/SLOs, deployment/migration | Operational story: on-call, runbooks, blast radius, rollout plan |
| **Communication & drive** | Structured; responds well to hints | Drives the whole session; manages time; checks alignment | Interviewer feels like they were in a design review with a peer |

**1 and 2 descriptors (all dimensions):** 1 = absent, wrong, or only after being told; 2 = present but shallow, generic ("add a cache"), or needed prompting.

---

## 3. AI system design

| Dimension | Senior bar (3) | Staff bar (3) | Staff 4 looks like |
|---|---|---|---|
| **Problem framing** | Clarifies users, task, success criteria | Asks "does this need an LLM / an agent at all?"; picks workflow vs agent; defines measurable quality targets | Frames risk and value: what errors cost, where humans stay in the loop |
| **Data & retrieval** | Reasonable RAG pipeline (chunk, embed, retrieve) | Hybrid retrieval, reranking, metadata/ACL filters, freshness, ingestion pipeline, multi-tenancy | Justifies choices with how they would *measure* them; handles versioned/conflicting docs |
| **Model & orchestration** | Chooses a model; basic prompt design | Model routing (cheap/strong), structured outputs, tool design, state/memory, durable execution + HITL | Explains when to optimise prompts (DSPy), fine-tune, or self-host, with break-even reasoning |
| **Evaluation** | Mentions evals | Offline golden sets per component, LLM-as-judge with calibration, online metrics, CI gates, error analysis loop | Eval strategy is the backbone of the design; describes how failures become tests |
| **Safety & security** | Mentions guardrails | Prompt injection (direct/indirect), excessive agency, data leakage, PII; least-privilege tools; OWASP LLM/agentic awareness | Lethal-trifecta analysis of the design; red-team plan; audit trail |
| **Cost, latency, scale** | Mentions token cost | Token/cost estimate per request and per month; latency budget per stage; caching, batching, streaming | Capacity plan (TPM limits, GPU if self-hosting), cost guardrails and budgets per tenant |
| **Observability & operations** | Logging | Tracing (OTel GenAI / Langfuse), prompt versioning, feedback capture, model/provider fallback | Rollout plan (shadow, canary, A/B), drift detection, incident playbook for model regressions |

---

## 4. Low-level design (LLD / OOD / concurrency)

| Dimension | 1 | 2 | 3 (Senior) | 4 (Staff) |
|---|---|---|---|---|
| **Requirements & use cases** | Starts drawing classes | Some use cases | Clear use cases, actors, constraints, out-of-scope | Plus identifies extension points likely to change |
| **Modelling** | God classes | Reasonable nouns → classes | Cohesive classes, clear responsibilities, correct relationships | Plus domain language (DDD-style), value objects, invariants enforced in types |
| **Design principles & patterns** | None | Patterns name-dropped | SOLID applied; appropriate patterns (strategy, state, observer) with reasons | Plus explains when *not* to use a pattern; favours composition, small interfaces |
| **Concurrency & correctness** | Ignores | Mentions locks | Correct synchronisation; identifies races; thread-safe data structures | Plus lock granularity trade-offs, deadlock avoidance, async vs threads choice |
| **Code** | Pseudo-code only | Partial code | Working core classes and key methods in Python (or Java) | Plus tests or testable seams; clean API |
| **Extensibility** | Rigid | Changes require edits everywhere | New variant = new class | Walks through a change request live and shows minimal diff |

---

## 5. Behavioral / Staff leadership

| Dimension | Senior bar (3) | Staff bar (3) | Staff 4 looks like |
|---|---|---|---|
| **Scope & impact** | Team-level project with clear outcome | Multi-team / org-level problem; impact quantified (revenue, cost, latency, reliability, velocity) | Changed how the org works (standards, platforms, strategy) with lasting effect |
| **Ownership & ambiguity** | Owned a well-defined project end-to-end | Found or defined the problem; created clarity where none existed | Chose *not* to do things; killed or reshaped projects with data |
| **Influence & collaboration** | Worked well with peers and manager | Aligned multiple teams/leaders without authority; handled disagreement constructively | Changed a senior leader's mind; built coalitions; resolved conflict leaving relationships stronger |
| **Technical judgement** | Sound technical decisions | Decisions balanced tech, business, people; explicit trade-offs and reversibility | Anticipated second-order effects; set technical direction others adopted |
| **Growing others** | Helped teammates | Mentored/sponsored engineers to promotion or new scope; raised team bar | Built mechanisms (reviews, guilds, docs) that scale beyond self |
| **Self-awareness & learning** | Mentions a mistake | Owns failures specifically, what changed afterwards | Shows pattern-level learning; how feedback changed their leadership style |
| **Story structure** | STAR, some rambling | Concise STAR(L): situation in < 45 s; "I" not "we"; numbers; handles follow-ups at depth | Every follow-up reveals more substance; no rehearsed feel |

---

## Scoring sheet

Copy for each round. Fill **during** the round (notes) and **immediately after** (scores).

```text
Checkpoint: CP__   Date: ____   Round type: Coding | SD | AI SD | LLD | Behavioral
Prompt: ______________________________   Interviewer: self | peer | paid | AI
Target bar: Senior | Staff     Time-box: __ min   Actual: __ min

| Dimension                    | Self | Interviewer | Evidence (1 line) |
|------------------------------|------|-------------|-------------------|
|                              |      |             |                   |
|                              |      |             |                   |
|                              |      |             |                   |
|                              |      |             |                   |
|                              |      |             |                   |
|                              |      |             |                   |

Round overall (apply caps): ___    Hire signal: strong no | lean no | hire | strong hire
Hints needed: 0 | 1 | 2 | 3+     Went silent > 20 s: __ times
Biggest strength:
Biggest gap:
One drill for next week:
```

### Aggregation per checkpoint

| Round | Weight (CP1–CP3) | Weight (CP4–CP6, Staff loop) |
|---|---|---|
| Coding | 30% | 20% |
| System design | 30% | 25% |
| AI system design | 20% | 25% |
| LLD | 5% | 10% |
| Behavioral / Staff | 15% | 20% |

Report both the weighted overall and the minimum round score; hiring committees look at the weakest round.

## Related

- [Checkpoints](checkpoints.md) · [Mock prompts](mock-prompts.md) · [AI mock interviewer](ai-mock-interviewer.md)
- [System design framework](../tracks/system-design/framework-and-estimation.md) · [AI SD framework](../tracks/ai-system-design/framework.md) · [Behavioral interviews](../tracks/staff-skills/behavioral-interviews.md)
