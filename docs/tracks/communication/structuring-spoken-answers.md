---
title: "Structuring spoken answers: PREP, pyramid, STAR"
track: communication
slug: structuring-spoken-answers
priority: P0
complexity: 3
est_hours: 2
phase: 2
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Structuring spoken answers: PREP, pyramid, STAR

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 2 · **Prereqs:** [Pace, pauses, filler words & clarity](pace-fillers-clarity.md)
    **You're done when:** you can answer any unseen work question in 60-90 seconds using a named structure, with the answer first, three or fewer supporting points, and a clear stop, and you can pick PREP, pyramid, STAR or SBI without thinking.

Drilled in [Week 5](drills/week-05.md) (PREP and pyramid), [Week 7](drills/week-07.md) (explaining to non-technical people) and [Week 21](drills/week-21.md) (STAR).

## Why it matters

The most common spoken-answer failure at senior level is the **chronological tour**: "So first we started with X, then we found Y, then..." The listener waits 90 seconds to learn the point. Executives interrupt, engineers think you have not decided, interviewers score you low on structure and impact.

A structure fixes three problems at once: it removes the planning pressure (which drives fillers), gives the listener a map (signposts), and forces a conclusion. You will use four: **PREP** for opinions and recommendations, **Pyramid** for complex answers and updates, **STAR** for behavioural stories and **SBI** for feedback. In Staff/Principal interviews, structure is a proxy for seniority: you are judged on how you think as much as on what you say.

## Core concepts

### 1. The principle: answer first, then support

Minto's **Pyramid Principle**: state the governing thought (answer) first, then group your supporting arguments (usually 2-4), each with its evidence. In speech, the top of the pyramid is the first sentence; the groups are your signposted points.

Spoken differences from writing: the listener cannot re-read, so (a) tell them how many points, (b) repeat the answer at the end, (c) keep each point to one to three sentences.

### 2. PREP: Point, Reason, Example, Point

Best for: "What do you think?", "Should we...?", "Why did you choose...?", 30-60 second answers.

| Step | Purpose | Example (Should we adopt a service mesh?) |
|---|---|---|
| **P**oint | Answer + stance | "Not yet. I'd wait until we have more than about 20 services." |
| **R**eason | The main why | "Right now the operational cost exceeds the benefit: we would add a control plane to run, upgrade and debug." |
| **E**xample | Concrete evidence | "In the last migration, the team spent six weeks on sidecar upgrades alone for four services." |
| **P**oint | Restate, with the next step | "So my recommendation is to keep mTLS in the gateway and revisit at 20 services." |

Variants: **PREP-with-trade-off** ("The cost is..."); **Point-Reason-Reason-Point** when no example exists.

### 3. The pyramid for longer answers (60-120 s)

1. **Answer** (1 sentence).
2. **Number of points** ("three reasons").
3. **Each point**: claim, then one proof.
4. **Close**: restate answer + ask or next step.

Pattern: "**Short answer:** X. **Three reasons.** First..., second..., third.... **So** X, and I need Y from you."

**Grouping rule:** points at one level must be the same *kind* of thing (all risks, all options, all reasons) and ideally MECE (mutually exclusive, collectively exhaustive). Common groupings: time (past, present, future), structure (people, process, technology), priority (must, should, could), trade-offs (cost, risk, speed).

### 4. STAR for behavioural stories

Best for interviews and stories about your past: "Tell me about a time you...". Target: 90-120 seconds.

| Step | Share of time | What to include |
|---|---|---|
| **S**ituation | ~15% | Context in 1-2 sentences: company, scale, stakes |
| **T**ask | ~10% | Your specific responsibility or the goal |
| **A**ction | ~50% | What *you* did (use "I", not "we"), 3 concrete actions incl. decisions and trade-offs |
| **R**esult | ~25% | Quantified outcome + what you learned or would change |

**STAR-L** adds a Learning. **CAR** (Context, Action, Result) is the compact variant. Senior candidates commonly fail by over-explaining Situation and under-explaining Action.

Example (compressed): "At our carrier-booking platform, p95 latency doubled after a migration (S). I owned the fix, with three days before peak season (T). I profiled the traffic, found N+1 queries in the rate lookup, added a cache with a five-minute TTL and a circuit breaker, and got the carrier-API team to batch requests (A). p95 fell from 2.1 s to 400 ms, we handled peak with no incidents, and I added a latency SLO to the release checklist (R)."

### 5. Other structures worth having

| Structure | Use | Skeleton |
|---|---|---|
| **SBI** | Giving feedback | Situation, Behaviour, Impact (see [Feedback, disagreement & conflict](feedback-and-conflict.md)) |
| **Past-Present-Future** | Status, intros | "Where we were, where we are, where we're going" |
| **Problem-Options-Recommendation** | Decisions | 2-3 options with one line of trade-off each, then a pick |
| **What-So what-Now what** | Updates, reflections | Facts, meaning, action |
| **Situation-Complication-Question-Answer (SCQA)** | Framing in a narrative | Minto's narrative opener |
| **Rule of three** | Anything unstructured | Three points beat two (thin) and five (forgettable) |

### 6. Phrase bank

| Function | Phrases |
|---|---|
| Open with the answer | "The short answer is..." · "My recommendation is..." · "I'd go with X, for three reasons." |
| Signpost | "First..., second..., third..." · "There are two dimensions to this." · "On the technical side... On the organisational side..." |
| Transition | "That brings me to..." · "Turning to risk..." · "The second reason is more subtle." |
| Give the example | "For instance..." · "A concrete case: last quarter..." · "To make that tangible..." |
| Trade-off | "The trade-off is X against Y." · "What we give up is..." · "The main downside is..." |
| Close | "So, to sum up..." · "The decision I need from you is..." · "In one line: X because Y." |
| Clarify the question first | "Just to make sure I'm answering the right question: are you asking about cost or risk?" |
| Handle a multi-part question | "There are two parts. Let me take the first one." |
| Admit not knowing | "I don't have the number to hand; my estimate is X, and I'll confirm by end of day." |

### 7. Picking the structure fast (10-second decision)

- Opinion, recommendation or "why did you...": **PREP**
- Complex analysis, options or a status: **Pyramid** or **Problem-Options-Recommendation**
- "Tell me about a time...": **STAR**
- Feedback: **SBI**
- Blank mind: **Past-Present-Future** or "three points"

### 8. Handling the hard cases

- **You do not know the answer.** Use structure anyway: "I don't know the exact figure. What I do know is A and B; I'd find out by C." An honest structured non-answer scores better than a guess.
- **Rambling recovery.** "Let me bring that back to the main point:..." then restate the answer.
- **Interrupted mid-answer.** Answer the interruption briefly, then: "Coming back to the second reason..."
- **Answering with the audience in mind.** For executives: answer, impact, ask (BLUF). For engineers: answer, mechanism, trade-off. For a non-technical partner: answer, analogy, consequence. See [Executive updates, summaries & escalations](executive-updates.md).
- **Numbers.** Give one number with context ("about 40 minutes, versus 4 hours in the last incident").

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| Barbara Minto, *The Pyramid Principle* | book | The origin of answer-first structure and MECE grouping; dense but the foundation | intermediate-advanced | paid |
| [Toastmasters International](https://www.toastmasters.org/) | community | "Table Topics" is exactly this skill: impromptu 1-2 minute structured answers with feedback | all | freemium |
| [TED](https://www.ted.com/) | video | Watch 5 talks and mark where the speaker states the point, the reasons and the close | intermediate | free |
| [Plain Language guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/) | guide | Organise by the reader's need, lead with the conclusion: the same logic as answer-first | intermediate | free |
| [BBC Learning English](https://www.bbc.co.uk/learningenglish/) | audio | Listen to how presenters signpost in 6 Minute English | intermediate | free |
| Talk Like TED (Carmine Gallo) | book | Practical patterns for stories, rule of three and structure | intermediate | paid |
| *Crucial Conversations* (Patterson et al.) | book | Structure for high-stakes conversations: facts first, story second | intermediate | paid |
| [YouGlish](https://youglish.com/) :gem: | interactive | Search "the short answer is", "the trade-off is", "for three reasons" to hear real signposts | all | free |

## Hands-on lab (60 min)

1. **Question bank (10 min).** Write 8 questions you may face: 3 opinion ("Should we build or buy?"), 3 behavioural ("Tell me about a conflict"), 2 status ("Where are we on migration?").
2. **Skeletons (15 min).** For each, write only the skeleton: Point/Reasons/Example or S/T/A/R with 5-word bullets.
3. **Deliver (20 min).** Record each answer in 60-90 s using only your skeleton. Transcribe two.
4. **Score (10 min).** Check: answer in the first 10 seconds? Number of points announced? Example concrete? Stop clearly?
5. **Re-do the worst (5 min).**

**Expected output:** 8 reusable skeletons in your notes, one reworked answer, and your average time per answer under 90 s.

## Questions

### L1 — Recall

??? question "Q1. What do the letters in PREP and STAR stand for?"

    ??? success "Answer"
        PREP: Point, Reason, Example, Point. STAR: Situation, Task, Action, Result.

??? question "Q2. What is the governing principle of the Pyramid Principle?"

    ??? success "Answer"
        Lead with the answer (governing thought), then support it with 2-4 grouped arguments, each backed by evidence. Groups should be of the same kind and MECE.

??? question "Q3. Which STAR step should take the most time?"

    ??? success "Answer"
        Action (about half), with Result about a quarter. Situation and Task are context, kept short.

??? question "Q4. Why announce the number of points ("three reasons")?"

    ??? success "Answer"
        Listeners cannot re-read. A count creates a map, shows you have structure, and lets the listener stop you or check they are still following.

### L2 — Apply

??? question "Q5. Give a PREP answer (under 60 words) to: "Should we rewrite the legacy booking service?""

    ??? success "Answer"
        Example: "No, not as a full rewrite. The service carries 60% of revenue, and a rewrite means two to three years of parallel running. Last time we rewrote the tariff engine, it took 18 months and lost the edge cases we hadn't documented. I'd strangle it: extract the three highest-churn modules first." Point, reason, example, point with a next step.

??? question "Q6. This STAR answer is weak: "We had a problem with the database and we all worked together and eventually it worked out." Identify three problems."

    ??? success "Answer"
        (1) No Situation detail or stakes. (2) "We" hides your contribution: state your own actions. (3) No result with numbers and no learning. Also no tension or decision.

??? question "Q7. Reorder into pyramid form: "We evaluated three brokers. Latency was similar. Kafka has best throughput. Our team knows Kafka. Cost is higher with managed Kafka. We recommend Kafka.""

    ??? success "Answer"
        "We recommend Kafka, for three reasons: it has the highest throughput, our team already knows it, and although the managed version costs more, latency was similar across all three, so cost is the only real trade-off." Recommendation first; grouped reasons; the trade-off named.

??? question "Q8. Choose the best structure: (a) an interviewer asks for a time you missed a deadline; (b) a VP asks for status; (c) a peer asks whether to use gRPC or REST."

    ??? success "Answer"
        (a) STAR (with a Learning). (b) Pyramid or Past-Present-Future with the status colour first. (c) PREP, or Problem-Options-Recommendation if there are several options with trade-offs.

### L3 — Judge and choose

??? question "Q9. In a design review, someone asks "why not use Redis?". Two answers: (A) a 3-minute history of the caching decision; (B) "Two reasons: durability and cost. Redis would need persistence, adding complexity; and at our volume, DynamoDB is cheaper." Which is better and when might A be right?"

    ??? success "Answer"
        B: answer first, two reasons. A is right only if the questioner asked for history or the decision is contested and context is missing; even then, lead with "Short answer: durability and cost; here's the background if useful."

??? question "Q10. Is it ever right to start with the story instead of the answer?"

    ??? success "Answer"
        Yes: with hostile or sceptical audiences, or when the answer is surprising and needs context to be believed, or in narrative talks (see [Storytelling & persuasion](storytelling-and-persuasion.md)). In status updates and interviews, answer-first is the default. If you delay the answer, say so: "I'll give you the answer in a moment; the context matters."

??? question "Q11. You have two strong examples for a behavioural question. Use both or one?"

    ??? success "Answer"
        One, in depth, unless the interviewer asks for more. Two shallow examples score lower than one with clear actions and quantified results. Mention the second as an offer: "I have another example with a different context if useful."

### L4 — Staff-level

??? question "Q12. A director asks in a group meeting "Why is this project late?" and two peers are partly at fault. Structure the answer."

    ??? success "Answer"
        Facts, not blame; answer, causes, recovery. "It is three weeks late. Two causes: the vendor API changed in week 4, and we underestimated the data migration. Neither was flagged early enough, which is on us as a program. The recovery plan: cut scope X, add two engineers for four weeks, new date is 15 November. I'd like your decision on scope today." Name systemic causes rather than people; take collective ownership; end with the ask.

??? question "Q13. In a panel interview, one panelist keeps interrupting your STAR answer. Adapt live."

    ??? success "Answer"
        Treat interruptions as signal: they want the point sooner. Restate the headline: "In short, I reduced p95 by 80%. Let me tell you how." Then give Action and Result compressed. Answer the actual interrupting question first, then return: "Coming back to the result..."

??? question "Q14. You coach an engineer who answers every question with 4 minutes of context. What is your plan?"

    ??? success "Answer"
        (1) Diagnose: they are safe-guarding. (2) Teach the "headline first" rule with a fixed one-sentence answer. (3) Set a timer of 90 s; practise 5 questions a week. (4) Use a "then stop" cue: after the closing line, stop speaking; silence invites follow-up. (5) Give feedback with SBI and celebrate measurable progress.

## Real-world use cases

- **Design review**: PREP for "why X over Y" and a trade-off close.
- **Steering committee**: Pyramid: recommendation, three reasons, decision ask.
- **Staff-level interview**: STAR with quantified results; PREP for design justifications.
- **Retro or postmortem call**: what, so what, now what.
- **1:1 with skip-level**: past-present-future for "what is your team working on".

## Pitfalls & anti-patterns

- Chronological storytelling with the answer at minute two.
- Announcing "three points" and delivering five.
- STAR answers that say "we" throughout and give no numbers.
- Answering a different question because you did not clarify.
- Overusing frameworks aloud ("Using the PREP method...") instead of just doing it.
- Not stopping: adding "and, yeah" after the conclusion.
- One-size-fits-all: giving an executive the mechanism first.

## Checklist

- [ ] I can state PREP, pyramid, STAR and SBI skeletons from memory.
- [ ] I have 6 STAR stories with numbers, ready to adapt.
- [ ] I open with the answer in my last 5 meetings and stop cleanly.
- [ ] I recorded 8 timed answers and compared them to the checklist.
- [ ] I can choose a structure in under 10 seconds.
- [ ] I answered all L3 questions out loud in < 3 min each.
