---
title: "Week 22 drills — Thinking aloud: system design and ambiguity"
track: communication
week: 22
last_reviewed: 2026-09-25
---

# Week 22 — Thinking aloud: system design and ambiguity

!!! abstract "This week"
    **Grammar:** Precision under time pressure: fewer errors while thinking aloud · **Vocabulary:** Design-interview vocabulary (bottleneck, trade-off, blast radius) · **Idioms & phrasal verbs:** Thinking-aloud phrases (let me walk through, to step back) · **Speaking:** Narrating a system design out loud · **Writing:** Summary sections and profile · **Soft skill:** Handling ambiguity out loud

    Difficulty: high (C1+), timed. The target is not perfect English but *recoverable* English: finish your sentences, keep subjects and verbs in agreement across long clauses, and fix a slip once, cleanly, without a restart cascade.

## Day 1 — Grammar: Precision under time pressure: fewer errors while thinking aloud {#day-1}
**⏱ 30 min · Mon** · 5 min rule, 15 min exercise (timer), 5 min check, 5 min use it.

### Rule in 60 seconds

Under time pressure, fluent non-native speakers do not make *new* mistakes; their known patterns come back. The five that appear most in design discussions:

| Pressure error | Cause | Fix |
|---|---|---|
| Dropped third-person -s / wrong *have/do*: "the service don't scale" | Speed; the -s is unstressed | Slow the *verb*, not the whole sentence; keep subjects short so the verb is near the subject |
| Agreement across a long subject: "One of the bottlenecks *are* the database" | The plural noun nearest the verb captures it | Agree with the *head*: *one* (singular). "The number of requests *is* growing"; "a number of requests *are* failing" |
| Wrong pattern after a verb: "suggest to use", "explain you", "discuss about" | Transfer from other languages | *suggest using / suggest that we use*; *explain X to you*; *discuss X* (no preposition) |
| Tense switching mid-explanation: "The client sends a request and then the server returned..." | Losing track of the frame | Pick present simple for "how the system works" and stay there; use past only for events that happened |
| Sentence restarts: "So the, the service will, we will have the service calls..." | Starting a sentence before you know its end | Pause, then produce a *short* complete sentence. A silent second beats a restarted sentence |

**Exceptions and detail**

- **The number of** takes a singular verb; **a number of** takes plural. Similarly *a variety of, a range of* take plural; *the range of* is singular.
- **If-clauses:** no *will* in the *if* part of a real conditional: "If we add a cache, latency will drop." (Exception: *if you will* meaning "please", not relevant here.)
- **Between... and:** "between Kafka and SQS", never "between Kafka or SQS". **Parallel structure** under pressure: "using Kafka or using SQS" or "Kafka or SQS", not "using Kafka or to use SQS".
- **Uncountables:** *information, advice, feedback, latency* (as a general quality), *throughput* have no plural: "some information", "a piece of advice". (*A latency* is possible in technical speech for a specific measurement, but "informations" and "advices" are always wrong.)

**Recovery technique (self-correction).** If you make an error, correct it once, at the phrase level, and keep going: "The service *scale*... scales horizontally." Do not restart the whole sentence.

### Exercise

Timer: 12 minutes. Each item is a transcribed slip from a design discussion. Correct it. Item 9 is a restart to clean up.

1. *The service don't scale because it have a single writer.*
2. *One of the bottlenecks are the database.*
3. *The number of requests are growing every quarter.*
4. *If we will add a cache, the latency will drop.*
5. *We need to decide between using Kafka or to use SQS.*
6. *Depending of the load, we can scale horizontal.*
7. *I would suggest to use a queue here.*
8. *Let me explain you the flow. The message is stored and then it is get processed by the worker.* (two errors)
9. *So the, the service will, we will have the service, it calls the cache first.* (rewrite as one clean sentence)
10. *I need some informations about the traffic, and any advices you have on the data model.*

??? success "Answers and explanations"
    1. *The service **doesn't** scale because it **has** a single writer.* Third-person -s on *do* and *have*.
    2. *One of the bottlenecks **is** the database.* The subject is *one*, not *bottlenecks*.
    3. *The number of requests **is** growing.* "The number of" = singular. (*A number of requests are growing* would also be correct, with different meaning: several.)
    4. *If we **add** a cache, the latency will drop.* No *will* in the *if*-clause.
    5. *We need to decide between **Kafka and SQS**.* (or: *between using Kafka and using SQS.*) *Between* pairs with *and*; the two options must be parallel.
    6. *Depending **on** the load, we can scale **horizontally**.* Preposition (*depend on*) and adverb (modifies the verb *scale*).
    7. *I would suggest **using** a queue here.* (or: *suggest that we use a queue.*) *Suggest* takes a gerund or a *that*-clause, not *to* + infinitive.
    8. *Let me explain **the flow to you**. The message is stored and then **it gets processed** / **is processed** by the worker.* *Explain* takes its object first (explain X to Y); *is get processed* mixes two passive forms. (Note: *explain me / explain you* is a very common transfer error.)
    9. *The service calls the cache first.* The restart came from starting the subject before choosing it.
    10. *I need some **information** about the traffic, and any **advice** you have on the data model.* Both are uncountable.

### Use it
Explain the architecture of one system you work on in 4 sentences, in present simple, without a single restart. Record it and count the restarts. Goal: zero. Then write down the one pressure error that hit you.

## Day 2 — Vocabulary: Design-interview vocabulary (bottleneck, trade-off, blast radius) {#day-2}
**⏱ 30 min · Tue** · 10 min table, 5 min collocations, 10 min cloze, 5 min use it.

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| bottleneck | noun | The point in a system where capacity is lowest and limits overall throughput. | At peak, the single-writer database was the bottleneck, not the API tier. |
| trade-off | noun | A situation where gaining one benefit means accepting a cost elsewhere; also the decision balancing them. | The trade-off is consistency versus availability: strong consistency costs us latency across regions. |
| blast radius | noun phrase | The extent of damage or impact if a component, change or deployment fails. | We shipped the config change to one region first to limit the blast radius. |
| throttle | verb | To deliberately limit the rate of requests or processing to protect a system. | The gateway throttles each partner to 500 requests per second. |
| degrade gracefully | verb phrase | For a system to lose non-essential features under stress while keeping the core function working. | If the recommendation service fails, the page should degrade gracefully and still show shipment status. |

### Collocations and word family

- **bottleneck**: *identify / remove / alleviate / become a bottleneck*; *the bottleneck in / at*; *a network / CPU / I/O bottleneck*. Verb use ("to bottleneck") is informal.
- **trade-off**: *make / weigh / accept a trade-off*; *a trade-off between X and Y*; *trade-offs of / involved in*. The verb is *trade off*, two words; the noun is hyphenated (US also "tradeoff").
- **blast radius**: *limit / reduce / contain / minimize the blast radius*; *a large / small blast radius*. Common in SRE and security.
- **throttle**: *throttle requests / traffic / a client*; noun *throttling*; *rate limiting* is the close synonym (throttling is often the softer version: slow, not reject).
- **degrade / degradation**: *graceful degradation*; *degrade gracefully*; *performance degradation*; *degraded mode*. Verb *degrade* is intransitive here; you *degrade* a service in the transitive sense only when you deliberately reduce quality.

### Exercise
Timer: 10 minutes.

1. Adding a read replica reduces read latency but introduces replication lag: that is the ______ we need to explain.
2. The nightly job saturates the disk and slows everything down; it is the main ______.
3. To ______ a noisy client, we cap it at 100 requests per second with a 429 response.
4. A staged rollout, region by region, keeps the ______ small if the release is faulty.
5. If the search index is unavailable, the app should ______ and fall back to a cached list.
6. Review (Week 21): the team ______ the entire cutover across six services and two vendors. (spearheaded / orchestrated)
7. Review (Week 21): we ______ the deployment process by removing three manual gates. (streamlined / galvanized)
8. Write one sentence using *trade-off* and *between*, about a decision you made this year.

??? success "Answers and explanations"
    1. **trade-off.** A benefit with a cost.
    2. **bottleneck.** The point limiting overall performance.
    3. **throttle.** Limit the rate, per client.
    4. **blast radius.** Extent of impact of a failure.
    5. **degrade gracefully.** Keep the core, drop the extras.
    6. **orchestrated** (coordination of many parties); *spearheaded* also possible if you led it from the front. Here "coordinated across six services and two vendors" favours orchestrated.
    7. **streamlined.** Removing steps.
    8. Model: *"The trade-off between build time and test coverage led us to run the slow integration suite only on merge."* Check: *trade-off between X and Y*, not *trade-off from*.

### Use it
Take a system you know. Say aloud: its bottleneck, one trade-off in its design, and its blast radius if it fails. Three sentences, each with one of the words.

## Day 3 — Speaking: Narrating a system design out loud {#day-3}
**⏱ 30 min · Wed** · 5 min structure, 5 min notes (four bullets max), 3 x 90 s, 5 min self-check.

**Prompt.** Timer 90 seconds each; record. Speak as if a design interviewer were listening.

1. "Design a service that tells customers where their container is, in near real time."
2. "Design a rate limiter for a partner-facing shipment API."
3. "How would you migrate a batch reconciliation job to a streaming pipeline with no downtime?"

**Structure: the spoken design loop.** Narrate the *process*, not just the answer.

| Step | Sentence stems | Time |
|---|---|---|
| 1. Clarify | "Before I start: who are the users, and what's the scale?" | 10 s |
| 2. State assumptions | "I'll assume ten million events a day and five-minute freshness is acceptable." | 10 s |
| 3. High-level design | "At a high level there are three components: ingest, store, serve." | 25 s |
| 4. Deep dive on one part | "Let me zoom in on the ingest layer, since it's the likely bottleneck." | 25 s |
| 5. Trade-offs and risks | "The trade-off here is X against Y. I'd choose X because... The blast radius of a failure here is..." | 15 s |
| 6. Check in | "Does that match what you had in mind, or should I go deeper somewhere?" | 5 s |

**Pronunciation micro-drill: noun/verb stress and technical terms.**

- Two-syllable noun/verb pairs: noun stress on the **first** syllable, verb on the **second**. *INcrease* (n) / *inCREASE* (v); *REcord* / *reCORD*; *PROject* / *proJECT*; *UPgrade* / *upGRADE*; *CONflict* / *conFLICT*. Say: *"We expect an INcrease in load, so we must inCREASE capacity."*
- Technical words: *LA-ten-cy* (LAY-tən-see), *AR-chi-tec-ture* (stress on first syllable), *AL-go-rith-m*, *cache* = "cash", *queue* = "kyoo", *idempotent* = *eye-DEM-po-tent* (some say *ID-em-...*), *Kubernetes* = *koo-ber-NET-eez*, *SQL* = "ess-cue-el" (or "sequel", both accepted), *bottleneck* = *BOT-tl-neck*, *trade-off* = *TRADE-off* (stress first).
- Linking: *"blast radius"* runs together: *blas-RAY-dee-us*. *"Trade-off between"* : *trade-off-BEtween* (the /f/ links to the next word).

**Self-check**

- [ ] I clarified and stated at least one assumption before designing.
- [ ] I used present simple to describe how the system works, without tense flips.
- [ ] I said one trade-off and one risk with the correct words (*trade-off between... and...*, *blast radius*).
- [ ] I ended sentences; I did not restart more than twice.
- [ ] I checked in with the listener at the end.

## Day 4 — Idioms & phrasal verbs: Thinking-aloud phrases (let me walk through, to step back) {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| walk (someone) through | (phrasal) To explain a process step by step. Neutral; very common in interviews and reviews. | Let me walk you through the request path, from the gateway to the database. |
| step back | To pause and view the problem from a wider perspective. Neutral/informal, common in meetings. | Let me step back for a second: what problem are we actually solving? |
| zoom in / zoom out | (phrasal) To focus on a detail / to view the whole picture. Informal-neutral, metaphor from cameras. | Let me zoom in on the write path, then zoom out and look at failure modes. |
| bear with me | Please be patient while I think or explain. Polite, slightly formal, works well for pauses. | Bear with me, I'm working out the failure modes as I go. |
| think out loud | To speak your reasoning as you form it, so others can follow and correct. Neutral; UK also "think aloud". | I'm going to think out loud here, so stop me if I go down the wrong path. |

### Exercise
Timer: 10 minutes.

1. Choose the best: *"Before we go into details, let me (step back / step up / step in) and restate the goal."*
2. Fill: *"I'll ______ you ______ the deployment pipeline."*
3. Fill: *"Sorry, ______ with me while I check the numbers."*
4. Rewrite more idiomatically: *"Please let me say my thoughts while I am thinking so you can correct me."*
5. Rewrite more idiomatically: *"Let me examine the smaller part now, the write path."*
6. Match the intent to the phrase: (a) buy thinking time politely; (b) signal that you are about to explain a process step by step; (c) invite correction on unfinished reasoning.
7. Which is wrong: *walk me through / walk through me / walk us through*? Explain.
8. When do you *zoom out* and when *zoom in* in a design discussion? One sentence each.

??? success "Answers and explanations"
    1. **step back.** *Step up* = take responsibility; *step in* = intervene.
    2. **walk / through.** *Walk someone through something.*
    3. **bear.**
    4. *"I'm going to think out loud so you can correct me."*
    5. *"Let me zoom in on the write path."*
    6. (a) *bear with me*; (b) *let me walk you through*; (c) *let me think out loud*.
    7. *Walk through me* is wrong. The person takes the object position after *walk*: *walk me / us through*.
    8. Zoom out to check the overall goal, dependencies, failure modes before committing; zoom in on the component that is the likely bottleneck or the riskiest assumption.

!!! warning "When NOT to use them"
    These are meta-phrases: they help when you need structure, but repeated they become filler ("let me step back" three times in five minutes signals that you are lost). Use one per minute at most. Avoid *bear with me* in writing (it sounds oral). *Think out loud* is a request; never use it to excuse an unfinished answer at the end.

## Day 5 — Writing: Summary sections and profile {#day-5}
**⏱ 30 min · Fri** · 5 min read, 15 min rewrite, 10 min compare.

**Bad draft (a "profile" section of a Staff Engineer resume):**

*Highly motivated and results-driven software engineer with more than 15 years of experience in the IT industry. Passionate about technology and always eager to learn new things. Good team player with excellent communication skills. Worked on many different projects in various domains, including logistics and e-commerce. Looking for a challenging position in a dynamic organization where I can utilize my skills and grow.*

**Task.** Rewrite as a 60-80-word profile that: (a) opens with your level and specialism; (b) contains two proof points with numbers (invent plausible ones for the exercise); (c) names the kind of problem you want next; (d) contains no cliché (*motivated, passionate, team player, dynamic*), no "I", and no "utilize".

??? success "Model answer and what changed"
    *Staff-level backend and platform engineer with 15 years' experience building high-volume logistics systems. Led the redesign of a shipment-event platform handling 40 million events a day, cutting status latency from twelve minutes to under one. Introduced blameless postmortems and staged rollouts across five teams, reducing Sev-1 incidents by 45%. Looking to lead architecture for large-scale data and AI-enabled platforms where reliability and delivery speed both matter.* (66 words)

    **What changed and why**

    - **Level and specialism first.** "Staff-level backend and platform engineer" tells the reader where to file you in one line; "results-driven" tells them nothing.
    - **Proof, not adjectives.** "40 million events", "twelve minutes to under one" and "45%" can be checked; "excellent communication skills" cannot.
    - **Noun-phrase style, no pronouns.** Profiles conventionally omit "I" and use fragments starting with a noun or participle. The style is compressed but grammatical.
    - **A direction, not a wish.** "Where reliability and delivery speed both matter" names the trade-off you like to work on; "challenging position" is filler.
    - **Plain verbs.** *Led, cut, introduced,* not *utilize*. Note "15 years' experience" (apostrophe after the plural noun) is correct.

## Day 6 — Speaking record: Design narration, 2-minute talk {#day-6}
**⏱ 30 min · Sat** · 5 min prep, 2 min record, 5 min replay and score, 15 min shadowing, 3 min log.

**Prompt.** Record a two-minute spoken design walk-through: *"Design a system that tracks the location and status of 10 million shipping containers and alerts customers when an ETA changes by more than two hours."* Use the spoken design loop from Day 3. Include one deliberate self-correction (say a slip and fix it cleanly), and at least three of this week's words.

**Structure.** 0:00 clarify + assumptions; 0:20 high-level (three components); 0:50 deep dive on the riskiest one; 1:25 trade-off and blast radius; 1:45 what you would monitor; 1:55 check-in question.

**Rubric** (score each 1-4; total /24)

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Listener cannot follow the design | Follows with effort; components unclear | Clear components and flow | Immediately clear; easy to draw from |
| Structure | Random order | Some order; no trade-offs | Clarify > design > deep dive > trade-off | Full loop, proportional timing, check-in |
| Fluency | Long pauses, many restarts | Frequent restarts | Few restarts; recovers | Smooth; deliberate pauses; clean self-correction |
| Grammar accuracy | Errors block meaning | Frequent agreement and tense errors | Few errors; consistent present tense | Almost error-free under load |
| Vocabulary range | Vague ("thing", "stuff") | Some technical terms | Precise terms, mostly correct | Precise and varied; uses trade-off/bottleneck naturally |
| Pronunciation | Hard to follow | Term stress errors distract | Mostly clear | Clear stress on technical terms and noun/verb pairs |

**Shadowing task (15 min).** Pick a recorded conference talk on system design or architecture (for example a QCon or a company engineering talk on video; choose one with clear speaker and a transcript or auto-captions). Shadow 60 seconds where the speaker explains a component: copy the rhythm, the pauses and how they signpost ("what this means is...", "the reason is..."). Do it three times, then record it without looking.

**Log your score:** `Week 22 record: __/24 · restarts counted: __ · weakest criterion: ______` in your log.

## Day 7 — Soft skills + weekly review: Handling ambiguity out loud {#day-7}
**⏱ 30 min · Sun** · 10 min scenario, 10 min recap, 10 min self-score and error log.

**Scenario.** In a final-round interview, or in a real planning meeting with a VP, you get a vague request: *"We need to make the tracking experience much better for our top customers. What would you do?"* No metrics, no constraints. The VP watches how you handle it, and will judge you as much for the process as for the answer.

**Task.** Script your first 150 words of response: ask two or three clarifying questions, state assumptions explicitly, offer a small set of options with a trade-off, and propose how you will decide. Do not start designing before you have framed the problem.

??? success "Model response and annotation"
    *Good question. Let me make sure I'm solving the right problem. Two quick questions: when you say "better", is that faster status updates, more accurate ETAs, or fewer support calls? And who counts as top customers, the top fifty accounts or a segment? While you think, I'll state my assumptions: I'll assume that accuracy of the ETA is the pain point, and that we have three months and no new headcount. Given that, I see two options. One: improve ETA accuracy with a better model, which is high impact but a longer feedback loop. Two: add proactive delay alerts, which is quicker, lower risk, and visible to customers, but does not fix the root cause. I'd lean toward the alerts first, then the model, because they let us learn faster. Does that direction fit your priorities, or should I weight it differently?*

    **Techniques used:** (1) *Name the process* ("let me make sure I'm solving the right problem") buys time and shows method. (2) *Questions with options* (faster / more accurate / fewer calls) are easier to answer than open ones. (3) *Explicit assumptions* make you correctable without looking wrong. (4) *Two options and a trade-off* prove structure; more than three overloads the listener. (5) *A recommendation with a reason* shows you can decide under uncertainty. (6) *Check-in question* returns control and invites correction.

### Weekly recap (20 items)

1. Correct: *The service don't scale.*
2. Which verb is right: *"One of the bottlenecks (is/are) the database"*? Why?
3. *The number of requests* takes singular or plural? And *a number of requests*?
4. Correct: *If we will add a cache...*
5. Correct: *I suggest to use a queue.*
6. Correct: *Let me explain you the design.*
7. Correct: *We need to decide between Kafka or SQS.*
8. Which tense should you use to describe how a system works?
9. Give the two-step recovery for a slip in speech.
10. Define *bottleneck*.
11. What does *trade-off* connect with, *between... and* or *between... or*?
12. Define *blast radius* and one way to limit it.
13. Difference between *throttle* and *rate limit* in everyday use?
14. What does it mean for a system to *degrade gracefully*?
15. Stress: *INcrease* or *inCREASE* for the noun?
16. *Walk me through*: what does it ask for?
17. *Step back*: when do you use it?
18. Why is repeating *let me step back* risky?
19. Name two techniques for handling ambiguity out loud.
20. Which Week 21 verb means to make a practice permanent?

??? success "Answers"
    1. *The service **doesn't** scale.*
    2. **is**: the subject is *one*.
    3. *The number of* = singular (is); *a number of* = plural (are).
    4. *If we **add** a cache...*
    5. *I suggest **using** a queue* / *suggest that we use a queue*.
    6. *Let me explain **the design to you**.*
    7. *between Kafka **and** SQS.*
    8. Present simple.
    9. Correct at the phrase level once and keep going; do not restart the sentence.
    10. The point of lowest capacity that limits overall throughput.
    11. *Between... and...*
    12. The extent of damage from a failure; limit with staged rollouts or isolation.
    13. Throttling slows traffic; rate limiting often rejects excess (for example with a 429). In practice used loosely, but the distinction is real.
    14. Lose non-essential features under stress while keeping the core function.
    15. **INcrease** (noun); *inCREASE* is the verb.
    16. To explain a process step by step, to the person.
    17. To reconsider the goal or the bigger picture before more detail.
    18. It sounds like you are lost, or stalling.
    19. Ask clarifying questions with options; state assumptions explicitly; offer two options with trade-offs; check in.
    20. **Institutionalize.**

### Self-score
- [ ] I can narrate a design for two minutes with fewer than three restarts.
- [ ] I can use *trade-off between... and...* correctly without thinking.
- [ ] I framed ambiguity by asking questions and stating assumptions, before answering.
- [ ] My Day 6 recording scored 18/24 or above.
- [ ] My profile has no cliché and two numbers.

**Error log prompt.** Write down your top 3 recurring mistakes from this week (for example: dropped -s, "suggest to", tense flip), each with a corrected sentence. Week 23 uses this list.
