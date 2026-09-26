---
title: "Week 05 drills — Parallelism, analytical connectors, PREP"
track: communication
week: 5
last_reviewed: 2026-09-25
---

# Week 05 — Parallelism, analytical connectors, PREP

!!! abstract "This week"
    **Grammar:** Sentence structure and parallelism · **Vocabulary:** Analytical words (consequently, whereas, hinge on, albeit, thereby) · **Idioms & phrasal verbs:** Strategy metaphors: low-hanging fruit, moving parts, silver bullet, bite off more than you can chew, table stakes · **Speaking:** PREP and pyramid structure for answers · **Writing:** Writing a design-doc summary · **Soft skill:** Facilitating a meeting

    Note: the plan lists *mitigate* for this week, but it is taught in Week 1, so *albeit* and *thereby* replace it here.

## Day 1 — Grammar: Sentence structure and parallelism {#day-1}
**⏱ 30 min · Mon**

### Rule in 60 seconds
- **Parallelism:** items in a list, a comparison, or a correlative pair must share the same grammatical form. "Fast, reliable, **and inexpensive**" (adjectives), not "fast, reliable, and has low cost". "To design, to build and to operate" or "designing, building and operating" (do not mix *to* and *-ing*).
- **Correlatives** (*not only... but also, either... or, both... and, neither... nor, whether... or*): put the same structure after each half. "The migration **not only cut** costs **but also improved** performance." If you invert (*Not only did the migration cut costs, but it also improved...*), keep the second clause complete.
- **Compare like with like:** "Latency this quarter is lower than **it was** last quarter" (not "than last quarter" alone, which compares latency with a quarter).
- **One main idea per sentence; put the main clause early.** English readers expect subject + verb within the first 8-10 words.
- **Run-ons and comma splices:** two independent clauses cannot be joined by a comma alone. Use a full stop, a semicolon, or a conjunction. "The deploy failed, so we rolled back."
- **Dangling participles:** the implied subject of an *-ing* clause must be the subject of the main clause. "Running the tests, **we found** the bug" (not "the bug was found").
- **The error fluent speakers make:** mixing forms in lists ("to reduce latency, improving reliability"), splicing with commas, and starting long sentences with three subordinate clauses before the main point.

### Exercise
Fix each sentence.

1. The service is fast, reliable and has low cost.
2. We want to reduce latency, improving reliability, and to cut cost.
3. Not only did the migration cut costs but also improved performance.
4. She is responsible for reviewing designs and to mentor junior engineers.
5. Our latency this quarter is lower than last quarter.
6. The deploy failed, we rolled back.
7. The dashboard was slow. Because the cache was cold.
8. Running the tests, the bug was found.
9. We can either extend the deadline or to cut scope.
10. Rewrite to put the main point first: "Although several options were considered, including a full rewrite, a partial migration and buying a vendor product, after reviewing the cost, risk and timeline data collected by three teams over the past month, we recommend the partial migration."

??? success "Answers and explanations"
    1. "...fast, reliable and **inexpensive**." (three adjectives.) 2. "...reduce latency, **improve** reliability, and **cut** cost." 3. "The migration **not only cut** costs **but also improved** performance." (or: "Not only did the migration cut costs, **but it also improved** performance.") 4. "...for **reviewing** designs and **mentoring** junior engineers." 5. "...lower than **it was** last quarter." (or "than last quarter's".) 6. "The deploy failed, **so** we rolled back." (or a semicolon or full stop.) 7. "The dashboard was slow **because** the cache was cold." (a *because* clause alone is a fragment.) 8. "Running the tests, **we found** the bug." 9. "We can either extend the deadline or **cut** scope." 10. Model: "We recommend the partial migration. We compared a full rewrite, a partial migration and a vendor product on cost, risk and timeline, using data from three teams over the past month." (Front-loaded recommendation; the long sentence is split.)

### Use it
Write one list of three parallel items about your project goals, one *not only... but also* sentence, and one main-point-first summary sentence. Check parallel forms.

## Day 2 — Vocabulary: Analytical words (consequently, whereas, hinge on) {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| consequently | adverb | as a result; introduces an effect of what was just said (more formal than *so*) | The vendor missed the deadline; consequently, we moved go-live by two weeks. |
| whereas | conjunction | contrasts two facts, "while on the other hand" (formal) | Option A optimizes for cost, whereas option B optimizes for resilience. |
| hinge on | phrasal verb | to depend entirely on a single factor | The decision hinges on whether the regulator accepts the audit trail. |
| albeit | conjunction | although (usually followed by an adjective, adverb or phrase, not a full clause); formal | The pilot succeeded, albeit on a small dataset. |
| thereby | adverb | by that means; introduces the result of an action, followed by -ing | We cache lookups locally, thereby reducing calls to the pricing service. |

### Collocations and word family
- **consequently** placed at the start (with a comma) or after a semicolon; near synonyms *therefore, as a result, hence*. *Consequence*: *a consequence of, serious consequences, face the consequences*. *Consequential* means important, not "resulting".
- **whereas** joins clauses: "A is X, whereas B is Y." Do not use it to mean *because*. Punctuation: comma before it. *While* is the more casual equivalent (ambiguity: *while* can also mean time).
- **hinge on / hinge upon** + noun or wh-clause: "hinges on the outcome", "hinges on whether...". Synonyms: *turn on, depend on*.
- **albeit** + adjective/phrase: "albeit slowly", "albeit imperfect". Wrong: "albeit we had no data".
- **thereby** + -ing: "thereby reducing", "thereby avoiding". *Thus* and *hence* are alternatives.

### Exercise
Choose or fill (use earlier words as review).

1. Latency dropped 30 percent; ___, conversion rose.
2. The old system is stateful, ___ the new one is stateless.
3. The launch date ___ legal approval.
4. The prototype worked, ___ with hard-coded data.
5. We batch writes, ___ cutting database load by half.
6. True or false: "albeit we lacked data" is correct.
7. Review: the manager asked us to ___ (evaluate) the feasibility before we commit. (Week 1)
8. Review: we ___ the migration by starting with one low-risk service. (Week 3)

??? success "Answers and explanations"
    1. consequently. 2. whereas (contrast). 3. hinges on. 4. albeit (concessive, followed by a phrase). 5. thereby. 6. False: *albeit* needs a phrase or adjective; use "although we lacked data". 7. assess. 8. de-risked.

### Use it
Write three sentences about your architecture or team: one contrast with *whereas*, one result with *consequently*, one dependency with *hinge on*.

## Day 3 — Speaking: PREP and pyramid structure for answers {#day-3}
**⏱ 30 min · Wed**

### Prompt (60-90 seconds)
"Should we build or buy a workflow engine for our booking platform? Give your recommendation."

### Structure
- **PREP:** **P**oint (your answer), **R**eason (why), **E**xample (evidence or story), **P**oint (restate). "I'd buy. Reason: workflow engines are commodity and our differentiator is elsewhere. For example, our last in-house engine cost three engineers a year. So my recommendation is to buy."
- **Pyramid:** answer first; then three supports; detail only if asked. Good for executives: they can stop listening after the answer and still have what they need.
- Signposts: "The short answer is...", "There are three reasons...", "First..., second..., third...", "To sum up...".

### Pronunciation micro-drill
- **Signpost stress:** put the stress on the number/ordinal and the key noun: "There are **THREE** **REA**sons." "**FIRST**, **COST**."
- **Linking:** "The_short_answer_is_yes", "in_fact", "a lot_of".
- **Final consonant clarity:** *cost* /kɒst/ (UK) or /kɔːst/ (US); do not drop the /t/: "cos(t) of delay". Practice: cost-benefit, next steps, first step, last-minute.
- **Word stress:** **al-TER-na-tive, RE-com-men-DA-tion, CRI-te-ri-a, TRADE-off, dif-fer-en-TI-ate**.
- Drill: answer three random questions in PREP, 45 seconds each.

### Self-check
- [ ] My first sentence was the answer.
- [ ] I gave a reason and a concrete example.
- [ ] I closed by restating the point.
- [ ] I used at least two signposts.
- [ ] I did not add a fourth point.

## Day 4 — Idioms & phrasal verbs: Strategy metaphors: low-hanging fruit, moving parts {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| low-hanging fruit | easy wins; things that give benefit for little effort; common business idiom (informal to neutral) | Fixing the slow queries is low-hanging fruit; we can cut load by 20 percent this week. |
| moving parts | the individual components or dependencies that can change or fail; neutral | The migration has too many moving parts to hand off in one sprint. |
| silver bullet | a single simple solution to a complex problem, usually said sceptically | There is no silver bullet for legacy code; we need incremental refactoring. |
| bite off more than you can chew | take on more than you can handle; informal | We bit off more than we could chew by launching in six regions at once. |
| table stakes | the minimum requirement to compete or take part; US business, informal | Single sign-on is table stakes for enterprise customers. |

### Exercise
1. "Automated retries are ___ ___; we should do them first." (low-hanging fruit)
2. "The rollout plan is risky because of the number of ___ ___."
3. Which idiom is used skeptically about a claimed cure-all?
4. "If we add three new features this sprint, we'll ___ off more than we can ___."
5. Rewrite plainly: "Observability is table stakes."
6. Rewrite idiomatically: "It's an easy improvement that gives a lot of value."
7. True or false: *silver bullet* is normally used positively ("we found the perfect silver bullet").
8. Which two idioms warn about complexity or overload?

??? success "Answers and explanations"
    1. low-hanging fruit. 2. moving parts. 3. silver bullet. 4. bite, chew. 5. "Observability is the minimum requirement." 6. "It's low-hanging fruit." 7. False: it is usually negative or sceptical ("there is no silver bullet"). 8. moving parts, bite off more than you can chew.

!!! warning "When NOT to use them"
    Metaphors can hide vagueness. "Low-hanging fruit" needs an estimate, or your audience will assume everything is easy. *Table stakes* may confuse non-US colleagues; give the meaning if unsure. Do not mix metaphors in one sentence ("we'll pick the low-hanging fruit and bite the bullet...").

## Day 5 — Writing: Writing a design-doc summary {#day-5}
**⏱ 30 min · Fri**

A summary should let a director decide in 60 seconds: **Context (one sentence), Proposal, Why, Alternatives considered, Impact/cost, Ask.**

### Bad draft
> This document describes a proposal for the redesign of the tracking service. Currently there are many issues with the tracking service and it is slow and hard to maintain and the team spends a lot of time fixing things. There are a lot of ways we could fix this and we looked into several of them. In this document we go through the details of the different options and then finally at the end there is a recommendation about which one we think is best.

### Task
Write a summary of at most 100 words for a tracking-service redesign. Invent plausible facts: p95 latency 2.4 s, 40 percent of on-call pages, recommendation: move to event-driven read models over 2 quarters, alternatives: patch or vendor.

??? success "Model answer and what changed"
    > **Recommendation:** rebuild the tracking read path as event-driven read models over two quarters.
    >
    > **Problem:** tracking has a p95 latency of 2.4 s and causes 40 percent of on-call pages.
    >
    > **Why this option:** it removes the shared-database bottleneck, thereby cutting latency and pages; a vendor product would add cost, whereas patching only delays the problem.
    >
    > **Alternatives:** patch the current service (cheap, short-lived); buy a vendor platform (fast, costly, lock-in).
    >
    > **Impact:** two engineers for two quarters; no customer-facing downtime.
    >
    > **Ask:** approve staffing by 15 Oct.

    - Recommendation first (BLUF, pyramid).
    - Vague "many issues" became two numbers.
    - Alternatives are named and compared with parallel structure.
    - The ask has a date.
    - Removed the table of contents disguised as a summary ("in this document we go through...").

## Day 6 — Speaking record: PREP and pyramid structure (2-minute recording) {#day-6}
**⏱ 30 min · Sat**

### Task
Record 2 minutes. **Prompt:** "Recommend whether your team should adopt a new technology or process. Use pyramid structure: answer, three reasons, one risk."

### Structure
Answer (10 s) -> Reason 1, 2, 3 (25 s each, each with a PREP mini-example) -> Risk (20 s) -> Close (15 s).

### Scoring rubric (1-4)

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | hard to follow | main idea recoverable | clear | effortless |
| Structure | no order | partial | clear start and end | answer first, signposted |
| Fluency | frequent long pauses | noticeable hesitations | occasional | smooth |
| Grammar accuracy | blocks meaning | frequent errors | occasional | rare |
| Vocabulary range | basic | some variety | good | precise, varied |
| Pronunciation | unintelligible in places | needs effort | mostly clear | clear stress and rhythm |

### Shadowing task
Shadow a structured talk: a TED talk with clear signposting (ted.com) or a BBC Learning English "6 Minute English" episode (bbc.co.uk/learningenglish). Note the signposts the speaker uses and copy them.

**Log your score:** date, total /24, whether the answer came first (yes/no).

## Day 7 — Soft skills + weekly review: Facilitating a meeting {#day-7}
**⏱ 30 min · Sun**

### Scenario
You chair a 45-minute cross-team meeting (8 people) to decide on a service ownership handover. Two senior engineers dominate, one director keeps returning to an old budget dispute, and two quieter engineers have said nothing. The decision is due today.

### Task
Script (about 150 words) your opening, one redirect for the off-topic director, and one way to draw in a quiet participant.

??? success "Model response and techniques"
    > **Opening:** "Thanks all. We have 45 minutes and one decision: who owns the notification service from 1 November. I'll take options for 15 minutes, then we decide. Ana will take notes."
    >
    > **Redirect:** "Tomás, the budget history matters, and I'd like to give it proper time. Can we park it and take it up with finance on Thursday? I want to use this meeting for ownership."
    >
    > **Draw in:** "Wei, you've run this service on-call. What's the risk we haven't discussed?"
    >
    > **Close:** "Let me confirm the decision: ..."

    Techniques: **timebox and stated outcome**; a **parking lot** for off-topic points that validates the concern; **directed questions** by name and experience for quiet people; **recap decisions and owners** at the end.

### Weekly recap (20 items)
1. Fix: "fast, reliable and has low cost." 2. Fix: "either extend or to cut." 3. What are correlatives? 4. What is a comma splice? 5. Fix a dangling participle: "Testing the code, the error appeared." 6. Compare like with like: "Latency is lower than last year." 7. Where should the main point go? 8. *Consequently*: register and punctuation? 9. *Whereas* means? 10. *Hinge on* means? 11. What follows *albeit*? 12. What follows *thereby*? 13. Meaning of *low-hanging fruit*. 14. *Moving parts*. 15. *Silver bullet* tone. 16. *Bite off more than you can chew*. 17. *Table stakes*. 18. PREP stands for? 19. What is the pyramid principle? 20. What is a parking lot in a meeting?

??? success "Answers"
    1. "fast, reliable and inexpensive". 2. "either extend or cut". 3. Paired conjunctions (*not only... but also*). 4. Two independent clauses joined by a comma alone. 5. "Testing the code, we saw the error." 6. "...than it was last year." 7. First. 8. Formal; comma after it or a semicolon before it. 9. Contrast ("while on the other hand"). 10. Depend entirely on. 11. An adjective, adverb or phrase. 12. An -ing form. 13. Easy wins. 14. Components that can change or fail. 15. Sceptical, usually negative. 16. Take on too much. 17. Minimum requirement. 18. Point, Reason, Example, Point. 19. Answer first, then supports, then detail. 20. A list of off-topic items to handle later.

### Self-score
- [ ] I fixed at least 8 of 10 structure errors.
- [ ] I used *consequently, whereas, hinge on, albeit, thereby* correctly.
- [ ] My spoken answer started with the point.
- [ ] My design-doc summary had a recommendation and an ask.
- [ ] I timeboxed or parked a topic in a real meeting.

**Error log:** write your top 3 recurring mistakes (lists that break parallelism are typical).
