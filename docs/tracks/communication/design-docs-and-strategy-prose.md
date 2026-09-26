---
title: "Prose for design docs, RFCs & strategy"
track: communication
slug: design-docs-and-strategy-prose
priority: P0
complexity: 4
est_hours: 3
phase: 2
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Prose for design docs, RFCs & strategy

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 4/5 · **Est. time:** 3 h · **Phase:** 2 · **Prereqs:** [Concise writing & editing](concise-writing-editing.md), [Sentence structure & parallelism](sentence-structure-parallelism.md)
    **You're done when:** you have written an RFC introduction and a one-page strategy summary where a reader who stops after the first 200 words knows the problem, the proposal, the main trade-off and the decision needed, and a reviewer can argue with your claims because they are specific and falsifiable.

Drilled in [Week 5](drills/week-05.md) (design-doc summary), [Week 8](drills/week-08.md) (RFC introduction), [Week 10](drills/week-10.md) (engineering strategy) and [Week 15](drills/week-15.md) (tech-debt proposal).

## Why it matters

At Staff/Principal level, **writing is the primary way you scale**. A good design doc gets you alignment across teams without ten meetings, survives you leaving the room, and becomes the institutional memory. Amazon's narrative memos, Google's design docs, Rust and Python's RFC/PEP processes and Stripe-style strategy docs all rest on one idea: *writing forces clear thinking and makes disagreement productive*.

The prose problems at this level are different from email:

- **Burying the decision** under background.
- **Describing the design instead of arguing for it**: reviewers need to know *why this, not that*.
- **Vague claims** ("scalable", "robust", "better") that cannot be tested.
- **Missing non-goals and alternatives**, so reviewers reopen settled questions.
- **Heavy, abstract prose** with nominalisations ("the utilisation of a caching layer for the facilitation of...").
- **Wrong register** for strategy: either a list of tasks or a vision poster.

## Core concepts

### 1. Anatomy of a design doc / RFC

Adapt to your organisation's template; the order below works for most:

| Section | Purpose | Prose guidance |
|---|---|---|
| **Title, authors, status, date, reviewers** | Metadata | Status: Draft / In review / Accepted / Superseded |
| **TL;DR / Summary** | The whole doc in 100-200 words | Problem, proposal, main trade-off, decision needed |
| **Context / Problem** | Why now, who is affected, what is broken | Numbers; user or business impact; the cost of doing nothing |
| **Goals** | What success looks like | Measurable: "p95 < 300 ms at 2x peak" |
| **Non-goals** | What you are deliberately not solving | Stops scope creep; a sign of senior thinking |
| **Proposal / Design** | The solution | Diagram first, then prose; walk through one request end-to-end |
| **Alternatives considered** | Why not X | One paragraph each: what it is, why rejected, under what condition it would win |
| **Trade-offs and risks** | Costs and failure modes | Honest; include rollback and blast radius |
| **Rollout / migration plan** | Steps, order, and checkpoints | Owners and dates |
| **Open questions** | What you do not know | Assign an owner and date |
| **Decision requested** | What reviewers must do | "Approve option B by 10 Oct" |
| **Appendix** | Details, benchmarks, links | Keeps the main body short |

**Length norm:** a decision document is 2-6 pages; a strategy doc 3-8; deep technical detail goes to an appendix or linked docs.

### 2. The RFC introduction: a template

The first paragraph does five things: problem, scale/impact, proposal, key trade-off, ask.

```text
## Summary

Booking-status updates from carriers reach customers up to 15 minutes late,
because we poll 40 carrier APIs on a schedule and fan out through a single
shared queue (about 2.3M updates/day; p95 delay 14 min; 3 escalations in Q2).
This RFC proposes replacing polling with a push-first, event-driven ingestion
layer built on Kafka, with polling retained as a fallback for the 12 carriers
that offer no webhooks. We expect p95 delay under 60 seconds for 70% of volume
at roughly EUR 9k/month additional infrastructure cost. The main trade-off is
operational: two ingestion paths to run. We ask reviewers to approve the
approach and the phase-1 scope (5 carriers) by 10 October.
```

Why it works: quantified problem, one-sentence proposal, explicit benefit and cost, the one trade-off that matters, and a dated ask.

**Weak version:** "In this document we discuss some challenges with the current status polling and present a possible new approach that may improve things." Nothing testable; nothing to decide.

### 3. Prose for arguing a design

**Make claims specific and falsifiable.**

| Vague | Specific |
|---|---|
| The new design is more scalable. | The new design handles 10x current write volume by sharding on shipment ID; the old one saturates at about 3x. |
| This reduces complexity. | This removes two services and one queue, and cuts the on-call runbook from 14 to 6 steps. |
| We should consider caching. | Caching carrier rate lookups (hit rate est. 85%) removes 60% of outbound calls; the cost is up to 5 minutes of stale prices. |
| It is more reliable. | The design has no single point of failure at the ingestion layer; the failure mode moves to consumer lag, which we can alarm on. |

**The claim-evidence-implication pattern** for each paragraph:

1. **Claim** (topic sentence): "Polling cannot meet a 60-second freshness target."
2. **Evidence:** "Each poll cycle across 40 carriers takes 11 minutes at the current rate limits."
3. **Implication:** "Reducing latency requires push, not faster polling."

**Trade-off language:** "X at the cost of Y", "in exchange for", "the price of this is", "this optimises for A over B", "we accept B because...". Signal your own weakness first: "The main weakness of this design is..."

**Alternatives section pattern:**

> **Alternative: increase polling frequency.** Simplest change (one config), but violates carrier rate limits for 9 of 40 carriers and cannot reach a 60-second target. Would be preferred if the freshness target were relaxed to 5 minutes.

Format: what it is, why rejected, the condition under which it would be right. This shows you considered it fairly and helps reviewers who prefer it.

**Hedging in design docs.** Separate what you know from what you assume: "We measured...", "We estimate... (based on the March traffic sample)", "We assume... If wrong, then...", "We have not tested...". Avoid decorative hedges ("might possibly perhaps").

### 4. Strategy prose: the kernel

Rumelt's *Good Strategy / Bad Strategy* gives a useful structure, the **kernel**: (1) a **diagnosis** of the challenge, (2) a **guiding policy** (the approach), and (3) **coherent actions**. Bad strategy is a list of goals or aspirations. Will Larson's engineering strategy writing (see Resources) adds: explore, diagnose, refine policy, operationalise.

| Element | Prose test | Example |
|---|---|---|
| **Diagnosis** | Names the specific obstacle; ideally a surprising insight | "We have 14 ways of deploying and no one owns any; 40% of incidents follow a deploy." |
| **Guiding policy** | A choice that rules things out | "We will consolidate on one paved deployment path and stop supporting the others by Q3." |
| **Coherent actions** | Concrete, sequenced, owned | "Q1 migrate the top 20 services; Q2 sunset the oldest pipeline; Q3 remove exceptions" |
| **Trade-offs** | What you give up | "Teams lose custom hooks; we will provide extension points for the top five use cases." |

**Tone for strategy:** confident but explicit about uncertainty; decisions in active voice ("We will..."); avoid "leverage synergies", "best-in-class", "holistic" and other filler. Say who does what.

### 5. Sentence-level style for technical prose

- **Subject first, verb early.** "The scheduler assigns each job to a worker" beats "Assignment of jobs to workers is performed by the scheduler."
- **One idea per sentence; average 15-20 words.** Break long chains.
- **Concrete nouns, precise verbs:** "the API returns 429 when the quota is exceeded" not "there are certain limits that may result in errors".
- **Define terms once**, then use them consistently. Do not vary "shipment", "consignment" and "booking" for elegance.
- **Parallel structure in lists** (see [Sentence structure & parallelism](sentence-structure-parallelism.md)).
- **Tense:** present tense for the design ("the service validates..."), future for plans ("we will migrate..."), past for evidence ("we measured...").
- **Active voice** for design and decisions; passive is fine when the actor is irrelevant ("the request is retried three times").
- **Signposting:** "This section covers...", "The remainder of this document..." only in long docs.
- **Avoid empty intensifiers:** "very", "extremely", "significant" (give the number).
- **"We" vs "I":** "We propose" in team docs; "I recommend" when it is your judgement and you own the risk.
- **Diagrams:** every diagram needs a caption stating the point ("Figure 2: Events flow through the ingestion layer; polling is used only as a fallback").
- **Avoid the curse of knowledge:** expand acronyms once; state assumptions about the reader.

### 6. Before / after: a design paragraph

**Before**

> We have been thinking about the fact that the current system has some scalability challenges and it would probably be a good idea to consider possibly introducing some kind of a caching layer, which could potentially help with a number of the performance issues that have been noticed by various teams recently.

**After**

> The rate service handles 9,000 requests/second at peak, and p95 latency has risen from 180 ms to 720 ms since March because every request calls the carrier API. We propose a read-through cache with a 5-minute TTL, which we estimate will remove about 60% of outbound calls. The trade-off is that prices may be up to five minutes stale; Sales has confirmed this is acceptable for quotes but not for confirmed bookings, which will bypass the cache.

**What changed:** specific numbers replace "some scalability challenges", one hedge ("estimate") in the right place, trade-off named, a stakeholder check included, and the confirmed-booking exception shows depth.

### 7. Review and feedback etiquette in docs

- Author: ask specific questions ("Is the migration order safe?"), set a review deadline, respond to every comment (resolve, reply or defer with a reason).
- Reviewer: classify comments (blocking / suggestion / question / nit); give reasons; propose alternatives; praise what is strong.
- Comment prose: "Could we..?", "What happens if...?", "I'm worried about X because Y", not "This is wrong". See [Feedback, disagreement & conflict](feedback-and-conflict.md).
- Decision log: record what was decided, who decided, and why; update the doc's status.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Design Docs at Google (Malte Ubl)](https://www.industrialempathy.com/posts/design-docs-at-google/) | article | Concise account of what a design doc is for, its sections and its "trade-off" focus | intermediate | free |
| [Python Enhancement Proposals](https://peps.python.org/) :gem: | docs | Real RFC prose at scale: read PEP 1 for the process and a few accepted PEPs for structure, rationale and rejected ideas | intermediate-advanced | free |
| [Rust RFCs](https://github.com/rust-lang/rfcs) | docs | A template with "Motivation", "Drawbacks", "Alternatives", "Unresolved questions" you can borrow directly | intermediate-advanced | free |
| [Will Larson, lethain.com](https://lethain.com/) | blog | Engineering strategy writing: diagnosis, policy, and actions; many worked examples | advanced | free |
| [StaffEng](https://staffeng.com/) | site | Staff-level writing and influence stories from real engineers | intermediate | free |
| [Google developer documentation style guide](https://developers.google.com/style) | guide | Sentence-level rules for technical prose | intermediate | free |
| [Write the Docs](https://www.writethedocs.org/) | community | Documentation writing practice, guides and talks | intermediate | free |
| Rumelt, *Good Strategy / Bad Strategy* | book | The diagnosis, guiding policy, coherent actions kernel | advanced | paid |
| Williams, *Style: Lessons in Clarity and Grace* | book | Cure for heavy abstract prose in technical writing | advanced | paid |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Paragraph structure, cohesion and argument basics | intermediate | free |

## Hands-on lab (2 h)

1. **Read (30 min).** Read the summary and rationale of two PEPs or RFCs. Highlight the sentences that state the problem, the trade-off and the rejected alternatives. Note how they hedge.
2. **Write the summary (30 min).** Choose a real decision you face. Write a 150-word RFC summary using the template: problem with numbers, proposal, benefit and cost, main trade-off, dated ask.
3. **Write an alternatives section (20 min).** Two alternatives: what, why not, and when they would win.
4. **Strategy kernel (20 min).** Write a diagnosis, a guiding policy and three coherent actions for a real problem (for example "deployment sprawl") in under 200 words.
5. **Edit (20 min).** Apply the vague-to-specific table to your text; replace every vague claim with a number or delete it. Read aloud once.

**Expected output:** a 150-word RFC summary, an alternatives section, a strategy kernel, a list of the vague words you replaced.

## Questions

### L1 — Recall

??? question "Q1. List the sections of a typical design doc in order."

    ??? success "Answer"
        Metadata, summary/TL;DR, context/problem, goals, non-goals, proposal/design, alternatives, trade-offs and risks, rollout plan, open questions, decision requested, appendix.

??? question "Q2. What five things should an RFC summary contain?"

    ??? success "Answer"
        The problem (with scale), the proposal, the benefit and cost, the main trade-off, and the ask (decision and date).

??? question "Q3. What are the three parts of Rumelt's strategy kernel?"

    ??? success "Answer"
        Diagnosis, guiding policy, coherent actions.

??? question "Q4. Why include non-goals?"

    ??? success "Answer"
        They limit scope, prevent reviewers from reopening settled questions and show that you made deliberate choices.

### L2 — Apply

??? question "Q5. Replace the vague claim: "The new approach is more robust.""

    ??? success "Answer"
        "The new approach keeps working when one region fails: in the March test, the system stayed available with a 40 s failover, whereas the old approach lost 12 minutes of writes." Specific, testable, comparative. If you have no data, say what you expect and how you will test it.

??? question "Q6. Rewrite in the claim-evidence-implication pattern: "We think Kafka is better because our team knows it and there are more tools and lots of people use it.""

    ??? success "Answer"
        "Kafka is the lower-risk choice for this project (claim). Three of five engineers have run it in production, its connector ecosystem covers all four of our sources, and hiring for Kafka skills is easier than for the alternatives (evidence). This reduces delivery risk by roughly a quarter of the estimated schedule, at the cost of higher operational overhead than a managed queue (implication)." (Numbers illustrative; use your own.)

??? question "Q7. Write an alternatives paragraph for "keep polling".""

    ??? success "Answer"
        "Alternative: keep polling and increase frequency. This is the smallest change, but 9 of 40 carriers' rate limits forbid it, and the best achievable p95 would be about 5 minutes. It would be the right choice if the freshness requirement were relaxed to 10 minutes." What/why not/when it wins.

??? question "Q8. Convert to active voice and strong verbs: "The implementation of retries is performed by the client library, and a determination of failure is made after three attempts.""

    ??? success "Answer"
        "The client library retries a request up to three times, then reports failure." Fewer words, clear actor, verbs instead of nominalisations.

### L3 — Judge and choose

??? question "Q9. Should a design doc argue for your preferred option, or present options neutrally?"

    ??? success "Answer"
        Argue, but fairly. Reviewers need a recommendation to react to. A neutral option list pushes the work back to the reader. Present the alternatives at full strength, say when each would win, and state the recommendation and your confidence. If the decision genuinely depends on someone else's judgement (cost tolerance), say so and ask.

??? question "Q10. A reviewer says your doc is "too long", another says "not enough detail". How do you resolve this?"

    ??? success "Answer"
        Use layers: a 200-word summary, a 3-5 page body containing decisions, and an appendix with details, benchmarks and diagrams. Ask each reviewer what decision they need to make. Detail without decision relevance goes to the appendix. Track questions that recur: they belong in the body.

??? question "Q11. Is it acceptable to write "I" in a design doc?"

    ??? success "Answer"
        Yes, where it clarifies ownership of judgement ("I recommend", "I am not confident about..."). Use "we" for team decisions and for the design itself ("we propose"). Consistency and the organisation's norm matter more than the rule.

??? question "Q12. "We should improve developer productivity" is a goal. Why is it bad strategy, and what would a better version look like?"

    ??? success "Answer"
        It states an aspiration but no diagnosis or choice. Better: diagnosis ("median build takes 42 minutes; 60% of engineers cite it as their top blocker"), policy ("we will cut CI time before adding any new tooling"), actions ("shard tests; cache dependencies; remove 30% flaky tests by Q2"). It says what you will and will not do.

### L4 — Staff-level

??? question "Q13. Three teams have three competing designs. You are asked to write the reconciling RFC. How do you write it so no team feels defeated?"

    ??? success "Answer"
        Start with shared goals and constraints, accepted by all three; describe each design fairly (in its authors' terms and with their review); use criteria stated before the analysis (cost, latency, migration effort, ownership); show a comparison with evidence; recommend a path that adopts strong ideas from each and credit them by name; name the trade-off honestly; state who decides and by when. Pre-wire each team lead in 1:1 before circulation. See [Storytelling & persuasion](storytelling-and-persuasion.md).

??? question "Q14. Your RFC was rejected in review because "the problem isn't clear". What do you change?"

    ??? success "Answer"
        Rewrite the context first: who is affected, how many, what it costs (numbers), a concrete example incident, and what happens if we do nothing. Ask a reviewer to paraphrase the problem before you fix the solution. Often the proposal is fine and the problem statement was assumed. Add a "why now" sentence.

??? question "Q15. You need to write a 2-year engineering strategy for 60 engineers when you have partial data. How do you handle uncertainty in the prose?"

    ??? success "Answer"
        State the diagnosis with the evidence you have and the confidence level; separate facts, estimates and assumptions; give decision points with triggers ("if adoption is below 50% by Q2, we will..."); avoid false precision; commit to the policy that is robust across scenarios; commit to a review date. Certainty of language should match certainty of evidence.

## Real-world use cases

- **Cross-team platform RFC** (event ingestion, deployment, auth) with a decision deadline.
- **Build-vs-buy memo** for a vendor tool with cost, risk and exit strategy.
- **Tech-debt proposal** framed as risk and velocity cost to leadership (see [Week 15](drills/week-15.md)).
- **Architecture decision records (ADRs)**: short, dated, and honest about context and consequences.
- **AI platform strategy:** diagnosis of current agent sprawl, guiding policy (a shared evaluation and guardrail layer), and phased actions.

## Pitfalls & anti-patterns

- Describing the design with no argument for why.
- Vague, unfalsifiable adjectives (scalable, robust, flexible).
- Hiding the ask on page five.
- Alternatives as straw men.
- No non-goals, so the scope expands in review.
- Diagrams with no caption or no walk-through.
- Strategy docs that are lists of initiatives without diagnosis.
- Writing only after the decision is made, to justify it.
- Over-hedging everything so the reviewer cannot tell what you believe.

## Checklist

- [ ] My RFC summary is 100-200 words and includes problem, proposal, trade-off and ask.
- [ ] Every claim in the body has a number, source or explicit assumption.
- [ ] I list non-goals and at least two alternatives with "when it would win".
- [ ] I wrote one strategy kernel: diagnosis, guiding policy and coherent actions.
- [ ] I edited for active voice, strong verbs and consistent terminology.
- [ ] I answered all L3 questions out loud in < 3 min each.
