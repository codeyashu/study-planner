---
title: "Week 17 drills — participle clauses, nuance and mentoring"
track: communication
week: 17
last_reviewed: 2026-09-25
---

# Week 17 — Participle clauses, intensifiers and mentoring

!!! abstract "This week"
    **Grammar:** participle clauses and concise modification · **Vocabulary:** intensifiers and nuance (considerably, notably, arguably, inherently, markedly) · **Idioms & phrasal verbs:** raise the bar, stretch goal, punch above your weight, step up, play to your strengths · **Speaking:** rhythm and stress in long sentences · **Writing:** blog post outline · **Soft skill:** mentoring conversations

    Theme: senior writing is dense but readable. Participle clauses cut words; nuance adverbs cut over-claiming; both need control.

## Day 1 — Grammar: participle clauses and concise modification {#day-1}
**⏱ 30 min · Mon**

### Rule in 60 seconds

A participle clause replaces a full clause with `-ing`, `-ed/past participle`, or `having + past participle`, giving a compact way to express time, cause, result or description.

| Form | Meaning | Example |
|---|---|---|
| Present participle (`-ing`) | Active; simultaneous or sequential action, or reason | "Running the migration overnight, we avoided peak traffic." |
| Past participle (`-ed`) | Passive meaning | "Written in Go, the service starts in milliseconds." |
| Perfect participle (`having + pp`) | Action completed before the main action | "Having reviewed the RFC, I have three concerns." |
| `Being + pp` / `Having been + pp` | Passive with cause or time (often dropped) | "Deprecated two years ago, the API still has users." |
| Negative | `not` before the participle | "Not knowing the root cause, we rolled back." |

**Reduced relative clauses** (the same idea after a noun): "engineers working on the migration" (who are working), "the report submitted yesterday" (that was submitted), "a service designed for scale".

**After conjunctions and prepositions:** "When deploying to production, check the flag"; "before making a change"; "while reviewing the design".

**The rule that catches everyone:** the implied subject of the participle clause must be the same as the subject of the main clause. Otherwise you have a **dangling participle**: "Looking at the dashboard, the spike is obvious" (the spike is not looking).

**Exceptions:** fixed expressions do not need a matching subject: *judging by, considering, given, generally speaking, providing/provided that, assuming, taking everything into account*. Formal *absolute constructions* have their own subject: "The deadline having passed, we escalated"; "Weather permitting, we deploy Friday".

**The error fluent speakers make:** dangling participles, especially at the start of a sentence in emails ("Having finished the deploy, the alerts started"), and using a participle for an action that is not the same subject's ("Being late, the report..."). Also mixing tense meaning: `-ing` for a prior completed action instead of `having + pp` where sequence matters: "Reviewing the code, I merged it" suggests simultaneous; "Having reviewed the code, I merged it" is clearer.

### Exercise

1. Combine with a participle clause: "We reviewed the logs. We found the root cause."
2. Correct the dangling participle: "Looking at the dashboard, the spike is clear."
3. Reduce the relative clause: "Engineers who are working on the migration should attend."
4. Reduce: "The report that was submitted yesterday contains errors."
5. Rewrite with a perfect participle: "After we had signed the contract, we discovered a hidden fee."
6. Correct: "Having finished the deploy, the alerts started firing."
7. Rewrite with a negative participle: "Because we did not know the cause, we rolled back."
8. Choose: "(Writing / Written) in Rust, the tool is memory-safe."
9. Correct: "Being tired, the code review was rushed."
10. Is this correct, and why? "Judging by the metrics, the rollout is healthy."

??? success "Answers and explanations"
    1. **"Reviewing the logs, we found the root cause"** or **"Having reviewed the logs, we found the root cause."** (The perfect form emphasizes completion before.)
    2. **"Looking at the dashboard, we can see the spike clearly."** The subject after the comma must be the one looking.
    3. **"Engineers working on the migration should attend."**
    4. **"The report submitted yesterday contains errors."**
    5. **"Having signed the contract, we discovered a hidden fee."**
    6. **"Having finished the deploy, we saw the alerts start firing."** The person finished the deploy, not the alerts.
    7. **"Not knowing the cause, we rolled back."** `Not` precedes the participle.
    8. **Written.** The tool was written (passive meaning), so past participle.
    9. **"Being tired, I rushed the code review"** (or "Because I was tired, the code review was rushed"). Dangling: the review is not tired.
    10. **Correct.** *Judging by* is a fixed expression exempt from the same-subject rule.

### Use it
Write three sentences about a recent project: one with `having + pp`, one with a reduced relative clause, one starting with `not + -ing`. Check that each subject matches.

## Day 2 — Vocabulary: intensifiers and nuance (considerably, notably, arguably, inherently, markedly) {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| considerably | adverb | To a large degree (modifies verbs, comparatives) | "Latency dropped considerably after we added the cache." |
| notably | adverb | In particular; especially worth mentioning | "Several regions improved, notably Asia-Pacific, where errors halved." |
| arguably | adverb | It can be argued (but not everyone agrees); often with superlatives | "Kafka is arguably the most mature option, but it is not the simplest." |
| inherently | adverb | By its very nature; as a built-in characteristic | "Distributed systems are inherently harder to debug." |
| markedly | adverb | Noticeably; clearly different (formal) | "Performance was markedly better for the smaller payloads." |

### Collocations and word family

- **considerably** + comparative or verb: considerably faster / higher; differ considerably; improve considerably. Adjective: **considerable** (a considerable effort). Do not confuse with **considerate** (thoughtful) or **considerately**.
- **notably**: "notably X" introduces the most important example. Adjective: **notable** (a notable exception); noun: **notability**.
- **arguably**: signals contestable claims. "Arguably the most important" is safer than "the most important". Do not use it to mean "obviously" or "clearly"; it weakens the claim. Adjective form: **arguable** (also "an arguable case").
- **inherently**: inherently risky / complex / unstable / flawed; opposite: **extrinsically** (rare). Adjective: **inherent** (an inherent risk).
- **markedly**: markedly different / better / worse / lower. Adjective: **marked** (a marked improvement).
- Pronunciation: con-SID-er-a-bly, NO-ta-bly, AR-gyoo-a-bly, in-HAIR-ent-ly (also in-HEER-), MARK-id-ly.
- **Register:** *markedly* is formal (reports, papers); in speech use "clearly" or "noticeably". *Very* and *really* are weak intensifiers; the words above replace them precisely.

### Exercise
Cloze. Word bank: considerably, notably, arguably, inherently, markedly, ostensibly, tenable, granular.

1. Batch jobs are ______ less responsive than streaming pipelines; that is a design property.
2. Costs fell ______ in the second quarter, from 90k to 55k dollars a month.
3. Several teams adopted the tool, ______ the payments team, which cut deployment time by half.
4. It is ______ our best architecture, although the operations team disagrees.
5. The two proposals differ ______: one is centralized, the other fully federated.
6. The team's proposal was ______ about cost, but its main aim was headcount.
7. A single-region deployment is no longer a ______ position for a global service.
8. We need ______ data (per route) to explain the difference.

??? success "Answers and explanations"
    1. **inherently**: property built into the design.
    2. **considerably** (or markedly): a large, measurable fall. Both fit; the sentence lists figures, so "considerably" is more neutral.
    3. **notably**: singles out the main example.
    4. **arguably**: claim open to dispute (the second half signals disagreement).
    5. **markedly** (or considerably): "differ markedly" is a common collocation.
    6. **ostensibly** (week 16 review): apparently about cost.
    7. **tenable** (week 16 review): defensible.
    8. **granular** (week 15 review): fine-level breakdown.

### Use it
Replace "very" in three sentences from your last status update with a precise word from this list. Say the new versions aloud.

## Day 3 — Speaking: rhythm and stress in long sentences {#day-3}
**⏱ 30 min · Wed**

**Prompt (60-90 seconds).** Explain, in three or four long-ish sentences, why your team chose one architecture over another. Aim for smooth, controlled sentences rather than lots of short ones, using at least two participle clauses ("Having compared...", "Written in...").

**Structure for long sentences: chunk, stress, pause**

1. **Chunk** into thought groups of 4-8 words. Breathe and pause (a short beat) at chunk boundaries.
2. **Stress** the last important content word in each chunk (the "nuclear" stress).
3. **Weaken** function words: to /tə/, and /ən/, of /əv/, for /fə/, can /kən/.

Example, with `/` for pauses and capitals for the nuclear stress:

"Having evaluated three OPtions, / we chose the event-driven DEsign, / which, although harder to OPerate, / scales considerably better under PEAK load."

**Pronunciation micro-drill: can vs can't, and weak forms**

- "I can DEploy on Friday" (weak /kən/, stress on deploy) versus "I CAN'T deploy on Friday" (full vowel /kænt/, stressed). Say both; a listener must hear the difference.
- Linking: "hav-ing re-VIEWED the RFC" runs together; do not chop each word.
- Read this aloud twice, marking the chunks first: "Written in Go and deployed on Kubernetes, the service, which handles roughly twelve thousand requests per second, has remained stable since the last release."

**Self-check**
- [ ] I paused at chunk boundaries, not mid-phrase.
- [ ] I stressed one key word per chunk, not every word.
- [ ] "Can" and "can't" were audibly different.
- [ ] My participle clauses had the right subject.
- [ ] I did not speed up toward the end of long sentences.

## Day 4 — Idioms & phrasal verbs: growth idioms {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| raise the bar | To increase the standard expected. Neutral; common in performance and quality contexts. | "The new platform team raised the bar for reliability across the company." |
| a stretch goal | An ambitious target beyond what is likely, meant to push effort. US business term; used in OKRs; note that failing a stretch goal is often acceptable by design. | "Zero-downtime deploys are a stretch goal for this year." |
| punch above your weight | To perform better than your size or experience suggests. Positive; British origin (boxing) but widely used in the US. | "For a five-person team, they punch well above their weight." |
| step up | To take on more responsibility or make a greater effort, especially when needed. Neutral, positive tone. | "When the lead left, two senior engineers stepped up." |
| play to your strengths | To use your best abilities, rather than working on weaknesses. Neutral; advice tone. | "Let's play to our strengths and give the data work to Mia." |

### Exercise (8 items)

1. Choose: "The new review standard has ______ for everyone." (raised the bar / stepped up)
2. Fill in: "Shipping in one week is a ______; we'll be happy with two."
3. Fill in: "When the outage hit, the junior engineers ______ and led the response."
4. Fill in: "A team that small is ______ its weight."
5. Rewrite more idiomatically: "We should give tasks to people according to what they are best at."
6. Rewrite more idiomatically: "Our company has increased the quality expectations for launches."
7. Choose the situation where "stretch goal" is inappropriate: (a) OKR for the year (b) a contractual delivery date (c) a hackathon target.
8. Which of these expressions is positive praise: "punch above your weight" or "cut corners"?

??? success "Answers and explanations"
    1. **raised the bar.**
    2. **stretch goal.**
    3. **stepped up.**
    4. **punching above** ("punching above its weight"; the subject "a team" takes "its").
    5. "We should **play to our strengths** / play to people's strengths."
    6. "Our company has **raised the bar** for launches."
    7. **(b).** A contractual date is a commitment; a stretch goal is by definition one you may miss.
    8. **punch above your weight** (a compliment). *Cut corners* is negative (week 16).

**When NOT to use them:** *stretch goal* misleads when leadership treats it as a commitment; label targets clearly ("commit" versus "stretch"). *Raise the bar* said to a team can sound like a threat; pair it with support. *Punch above your weight* can sound patronizing if it implies the team should be small; use it as praise in retrospect, not as a justification for under-staffing.

## Day 5 — Writing: blog post outline {#day-5}
**⏱ 30 min · Fri**

**Bad "outline"**:

> Blog post about our migration
> - Intro: we migrated
> - What we did
> - Problems
> - What we learned
> - Conclusion

**Task.** Create a proper outline for a 1,200-word technical blog post about migrating a batch pipeline to streaming. Include: a working title that promises a specific takeaway; a one-sentence hook; four to five section headings, each with a one-line key point and the evidence (metric, diagram or code) you will use; and a closing takeaway with a call to action. The audience: engineers at other companies considering the same move. Use at least two participle-clause phrases in the key points.

??? success "Model answer"
    **Working title:** How we cut freight-event latency from 40 minutes to 90 seconds by moving from batch to streaming (and the three things we would do differently)

    **Hook:** "Every morning, 200,000 container events reached customers 40 minutes late, and nobody could explain why the fix always took a quarter."

    **1. Why batch stopped working.** Key point: designed for nightly volumes, the pipeline could not absorb intraday peaks. *Evidence:* graph of lag versus volume.

    **2. The design we chose (and the one we rejected).** Key point: having compared a lambda architecture with a pure streaming approach, we picked streaming with replay for auditability. *Evidence:* architecture diagram.

    **3. Migrating without a big bang.** Key point: running both pipelines in parallel and comparing outputs let us catch 14 discrepancies before cutover. *Evidence:* table of discrepancies by category.

    **4. What went wrong.** Key point: underestimating state size, we hit memory limits in week three. *Evidence:* the incident timeline and the fix (10-line config change).

    **5. Results and trade-offs.** Key point: latency fell 96 percent, but operational complexity is arguably higher. *Evidence:* before/after metrics; on-call load.

    **Takeaway and call to action:** "Start with one high-value stream, run in parallel, and measure the discrepancy rate; share your own numbers in the comments."

    What changed and why:
    - The title states a measurable outcome plus a promise ("three things"), which helps readers decide to click.
    - The hook is a concrete moment, not "we migrated".
    - Each section has a *claim*, not a topic label, so the argument can be judged from the outline alone.
    - Evidence is attached to each section, which prevents an unsupported draft.
    - Participle phrases ("designed for...", "having compared...", "underestimating...") compress the key points without losing the causal link.

## Day 6 — Speaking record: a lightning talk on a lesson learned {#day-6}
**⏱ 30 min · Sat**

**Record a 2-minute talk.** Give a lightning talk titled "One thing I would do differently in our last big project". Tell it as a short story: context, the decision, what happened, the lesson.

**Structure:** context in one sentence (15 s) - the decision and why (30 s) - what happened, with a number (30 s) - the lesson (30 s) - one-sentence takeaway (15 s). Use at least three participle clauses and two nuance adverbs (arguably, considerably, notably).

**Scoring rubric** (1 to 4)

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Message unclear | Point emerges late | Clear main point | Point is unmistakable and memorable |
| Structure | No visible order | Some order, jumps | Clear sequence | Signposted, story arc clear |
| Fluency | Frequent stops/fillers | Occasional long pauses | Mostly smooth | Smooth with deliberate pauses |
| Grammar accuracy | Errors block meaning | Frequent errors | Few errors | Participle clauses accurate |
| Vocabulary range | Repeats basic words | Some C1 words | Good range, nuance adverbs | Precise, varied, natural |
| Pronunciation | Hard to follow | Stress errors distract | Generally clear | Chunking and stress control long sentences |

**Shadowing task.** Shadow two minutes of a conference talk by an experienced engineering speaker (for example, a QCon or GOTO talk on YouTube). Note where they pause; copy the chunking of long sentences, not just the words.

**Log your score:** total out of 24, and how many participle clauses you used correctly (aim for at least 3).

## Day 7 — Soft skills + weekly review: mentoring conversations {#day-7}
**⏱ 30 min · Sun**

**Scenario.** You mentor Tomasz, a strong mid-level engineer who has just been passed over for promotion to senior. He says: "It's political. They promote whoever is loudest." He is frustrated and thinking of leaving. You have 30 minutes tomorrow.

**Task.** Write a 150-word script of how you would open and steer the first part of the conversation as a mentor, using coaching questions (Goal, Reality, Options, Way forward) rather than advice.

??? success "Model response"
    "Tomasz, I'm sorry it didn't go the way you hoped; I know how much you put into this year. Before we talk about what to do, I'd like to understand what you're seeing. What did the feedback actually say?

    [Listen.] So the gap they named is influence beyond your team. What would getting there look like for you, in twelve months? [Goal]

    And where are you today against that? For example, which decisions outside your team have you shaped? [Reality]

    There are a few ways forward. You could lead a cross-team design review, write the RFC for the routing change, or mentor a new joiner. Which of those interests you, and which would you rather avoid? [Options]

    What's one step you could take in the next two weeks, and how can I help? [Way forward]"

    **Techniques used:** (1) Empathy first, without endorsing the "political" framing. (2) Open questions in GROW order. (3) Reflecting the feedback back, in his words. (4) Options offered as a menu, letting him choose (ownership). (5) A small, dated next step. (6) Offer of specific help. Avoid arguing about whether it is political; explore what he can influence.

### Weekly recap (20 items)

1. What is the same-subject rule for participle clauses?
2. Correct: "Looking at the logs, the error is obvious."
3. Which participle expresses a prior completed action?
4. Reduce: "The engineers who are attending the review..."
5. Negative form: "Not ___ the cause, we rolled back." (know form)
6. Is "Judging by the numbers, ..." dangling?
7. Define **considerably** and give a collocate.
8. When do you use **arguably**?
9. Meaning of **inherently**?
10. Which adverb is formal for "noticeably"?
11. **Notably** introduces...?
12. Where is the stress in **arguably**?
13. "Raise the bar" means...?
14. Why is a "stretch goal" not a commitment?
15. "Punch above your weight" is praise or criticism?
16. What does "step up" mean?
17. Which is preferred in speech, chunking sentences or racing through them?
18. Which vowel does "can't" have in a stressed position: weak /ə/ or full /æ/?
19. What does GROW stand for?
20. In a mentoring conversation, should you first offer advice or ask questions?

??? success "Answers and explanations"
    1. The implied subject of the participle must be the subject of the main clause. 2. "Looking at the logs, we can see the error." 3. having + past participle. 4. "The engineers attending the review..." 5. knowing. 6. No; it is a fixed expression. 7. To a large degree; considerably higher/improve considerably. 8. For contestable claims, often before a superlative. 9. By its nature; built in. 10. markedly. 11. The most important example. 12. AR-gyoo-a-bly, first syllable. 13. Raise the standard expected. 14. It is a target you may miss by design. 15. Praise. 16. Take on more responsibility or effort. 17. Chunking. 18. Full /æ/. 19. Goal, Reality, Options, Way forward. 20. Ask questions first.

**Self-score**
- [ ] I can use `having + pp` and reduced relative clauses without dangling.
- [ ] I can replace "very" with a precise nuance adverb.
- [ ] I used at least three of the five new words.
- [ ] I chunk and stress long sentences deliberately.
- [ ] I drafted a blog outline where each heading is a claim.

**Error log.** Write your top 3 recurring mistakes this week (grammar, word choice, pronunciation). Week 18 is a light week: use this list as its grammar input.
