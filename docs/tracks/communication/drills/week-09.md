---
title: "Week 09 drills — Passive voice, numbers and postmortems"
track: communication
week: 9
last_reviewed: 2026-09-25
---

# Week 09 — Passive voice, numbers and postmortems

!!! abstract "This week"
    **Grammar:** Active vs passive voice, and when to use each · **Vocabulary:** Precision with numbers: roughly, approximately, marginally, materially · **Idioms & phrasal verbs:** Project phrasal verbs: roll out, scale up, sign off · **Speaking:** Question intonation and turn-taking · **Writing:** Blameless postmortem prose · **Soft skill:** De-escalating conflict

## Day 1 — Grammar: Active vs passive voice, and when to use each {#day-1}
**⏱ 30 min · Mon** Passive voice is neither good nor bad. It is a tool for controlling what comes first in the sentence. Engineers overuse it to sound formal and underuse it where it is the right choice, such as blameless writing.

### Rule in 60 seconds

**Form:** `be` + past participle: `The fix was deployed`, `is being investigated`, `has been suppressed`, `will be reviewed`, `must be approved`. The tense is carried by `be`.

**Use the passive when:**

1. **The doer is unknown or irrelevant:** `The cluster was upgraded last night.`
2. **The doer is obvious:** `The suspect was arrested` (police).
3. **You want the topic to stay in first position** (given-before-new): `We migrated the database. It was validated against last month's data.`
4. **You are writing blameless prose:** focus on systems and conditions, not people (`The config was changed without a review gate`).
5. **Formal or scientific writing** where the process matters more than the agent (`Samples were collected hourly`).

**Use the active when:**

1. **You want clarity and energy:** `We rolled back the release` beats `The release was rolled back` in a status update.
2. **Accountability matters:** `Legal missed the deadline` versus `The deadline was missed` (who?). In performance or contracts, hidden agents cause confusion.
3. **The doer is new or important information:** put it at the end with `by`, or make it the subject.

**Rules and exceptions**

- Only **transitive verbs** (verbs that take an object) can be made passive. **Intransitive verbs cannot**: `happen, occur, arise, fail, exist, appear, disappear, remain, consist, die, seem`. Error fluent speakers make: `The outage was happened at 2 a.m.`, `The deploy has been failed`, `It was occurred yesterday`. Correct: `The outage happened`, `The deploy failed`, `It occurred yesterday`.
- **Participle mistakes:** the passive needs the third form: `is being investigated` (not `investigate`), `has been suppressed` (not `suppress`).
- **Dangling modifiers:** `By adding an index, the latency was reduced` is wrong because the phrase `By adding an index` needs a doer that is missing from the main clause. Write `By adding an index, we reduced the latency` or `Adding an index reduced the latency.`
- **Verbs with two objects:** prefer the person as subject: `We were given read-only access` rather than `Read-only access was given to us`.
- **Get-passive** (`The queue got flooded`) is informal; use `was` in formal writing.
- **Stative passive:** `The port is closed` describes a state, not an action.
- **Overuse trap:** `It was decided that mistakes were made` is grammatical but evasive. Fluent speakers often default to this in writing because it sounds formal.

### Exercise

Correct or transform (10).

1. The incident was happened at 02:10 UTC.
2. The deploy has been failed twice this week.
3. Rewrite in a blameless style: `The engineer deleted the wrong table.`
4. By adding an index, the latency was reduced from 800 ms to 90 ms.
5. Someone approved the budget on Monday. (Rewrite so the emphasis is on the budget; the approver is irrelevant.)
6. An external researcher found the vulnerability. (Passive, keeping the agent.)
7. It was decided that the release would be delayed and mistakes were made. (Make it accountable.)
8. Rewrite with the person as subject: `Production access was given to the contractors.`
9. Which is more appropriate in a postmortem: `The queue got flooded` or `The queue was flooded`?
10. The alerts have been suppress since Monday.

??? success "Answers and explanations"
    1. `The incident **happened** at 02:10 UTC.` `Happen` is intransitive and has no passive.
    2. `The deploy **failed** twice this week.` (or `has failed`). `Fail` is intransitive here.
    3. `The wrong table was deleted during a manual cleanup, and the tooling did not require a review.` The passive removes the person and the extra clause names the system condition that allowed the mistake. This is a legitimate use; a blameless postmortem still needs the *cause* (not a passive that hides it entirely).
    4. `By adding an index, **we reduced** the latency...` Dangling modifier: the subject of the main clause must be the doer of `adding`.
    5. `The budget **was approved** on Monday.` The topic is first; the agent is irrelevant.
    6. `The vulnerability **was found by** an external researcher.` Keep `by` when the agent is new information.
    7. `**We decided** to delay the release, and **we made** mistakes.` Active voice restores accountability, which reads more credible in a review.
    8. `**The contractors were given** production access.` Person as subject is more natural.
    9. `was flooded`. `Get` passives are informal and can sound casual in an incident record.
    10. `The alerts have been **suppressed** since Monday.` Third form.

### Use it
Take three sentences from your last incident update or design doc. Change one from active to passive because the agent is irrelevant, one from passive to active because accountability matters, and one where you delete a dangling modifier. Say all three aloud.

## Day 2 — Vocabulary: Precision with numbers: roughly, approximately, marginally, materially {#day-2}
**⏱ 30 min · Tue** Executives interrupt vague numbers. These words give exactly the amount of precision you intend.

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| approximately | adverb | Close to, but not exactly; more formal than `about` or `roughly`. | The migration will take approximately six weeks, subject to vendor availability. |
| marginally | adverb | By a very small amount; barely. | The new index improved query time only marginally, from 92 ms to 88 ms. |
| materially | adverb | In a way that is significant enough to matter for a decision; common in finance and legal English. | The outage did not materially affect quarterly revenue. |
| negligible | adjective | So small that it can be ignored. | The cost of the extra replica is negligible compared with an outage. |
| appreciably | adverb | By a large enough amount to be noticed or measured. | Latency has not improved appreciably since the upgrade. |

**Note:** `roughly` is the informal equivalent of `approximately` (`roughly 40 servers`). `Around` and `about` are also fine in speech.

### Collocations and word family

- **approximately:** approximately + number/quantity only; adjective `approximate` (an approximate figure); noun `approximation`; verb `approximate`. Never with an exact figure: not `approximately 40.3 percent` (say `about 40 percent`).
- **marginally:** marginally better / slower / higher / lower; adjective `marginal` (marginal gain, marginal cost); noun `margin`. Often used in the negative: `not marginally, but dramatically`.
- **materially:** materially affect / impact / misleading / different; the term `material` (adj) appears in `material change`, `material risk`. Do not confuse with `material` (noun = matter, fabric).
- **negligible:** negligible risk / impact / effect / difference / cost / amount; noun `negligibility` is rare. Not `neglectful` (careless).
- **appreciably:** improve / change / differ appreciably; usually with a negative or comparison: `not appreciably different`.

**A precision scale (increasing effect):** negligible < marginal < modest < appreciable < material < substantial < dramatic.

### Exercise

Fill each gap (8). Review words: **substantiate, salient, pragmatic**.

1. Our p99 latency is ______ 300 ms, give or take ten.
2. Adding a second cache shard improved throughput only ______ from 10,200 to 10,350 requests per second.
3. The cost of storing an extra week of logs is ______ next to the licence fee.
4. The finding did not ______ affect our audit result.
5. Response times did not change ______ after the patch; users could not tell the difference.
6. Please ______ your claim that the outage cost 2 million dollars.
7. The most ______ number in this chart is the 14 percent growth in failed pickups.
8. A ______ approach is to ship the read-only view first.

??? success "Answers and explanations"
    1. **approximately** (or `roughly`, `about`); the `give or take ten` shows an approximate figure.
    2. **marginally**: a 1.5 percent change is barely anything.
    3. **negligible**: small enough to ignore.
    4. **materially**: significant enough to change the audit outcome.
    5. **appreciably**: not noticeably.
    6. **substantiate** (review, Week 7).
    7. **salient** (review, Week 8).
    8. **pragmatic** (review, Week 8).

### Use it
Report three real numbers from your work with the right precision word: one `approximately`, one `marginally` or `negligible`, one `materially`. Say each aloud as a complete sentence, with the number in the middle.

## Day 3 — Speaking: Question intonation and turn-taking {#day-3}
**⏱ 30 min · Wed**

**Prompt (60-90 seconds):** You are chairing a design review of a new event pipeline. Open the discussion, ask two questions of different types, politely interrupt a colleague who is talking too long, and invite a quiet participant to speak. Say it aloud as one continuous piece.

**Structure: Open, Ask, Manage the floor, Invite**

1. **Open:** `Thanks, everyone. We have 30 minutes and I want to focus on the failure modes.`
2. **Ask:** one yes/no question and one wh- question, with correct intonation.
3. **Manage the floor:** `Can I jump in for a second?`, `Let me stop you there, and we can come back to this`, `To build on that...`
4. **Invite:** `Priya, we have not heard from you yet. What is your view?`

**Turn-taking phrases:**

| Move | Phrases |
|---|---|
| Take a turn | `Can I add something?` / `If I may...` / `Just to build on that...` |
| Hold the turn | `Let me finish this point, and then I'll take your question.` |
| Interrupt politely | `Sorry to cut in, but...` / `Let me stop you there.` |
| Yield | `That's all from me.` / `Over to you, Priya.` |
| Redirect | `Let's park that and come back to it.` |

**Pronunciation micro-drill: question intonation** (↗ = rising, ↘ = falling)

| Type | Pattern | Example |
|---|---|---|
| Yes/no | ends rising ↗ | `Did the rollback complete?` ↗ |
| Wh- question | ends falling ↘ | `What caused the delay?` ↘ |
| Tag: real question | rising ↗ | `You've tested it, haven't you?` ↗ (I'm not sure) |
| Tag: confirming | falling ↘ | `That was a bad idea, wasn't it?` ↘ (I expect agreement) |
| List | rise, rise, fall | `We checked logs ↗, metrics ↗, and traces ↘.` |
| Alternative | rise on first, fall on last | `Do you want to roll back ↗ or roll forward?` ↘ |

Drill: say each pair twice, changing only the ending. The word-stress is on the last important word (`the DELAY`), and the pitch movement begins there. Rising on a wh- question can sound uncertain or challenging; falling on a yes/no question can sound like an accusation or a boredom.

**Self-check**

- [ ] My yes/no questions rose and my wh- questions fell.
- [ ] I interrupted politely and did not just talk over the person.
- [ ] I used at least three phrases from the turn-taking table.
- [ ] I invited a quiet participant by name.
- [ ] I did not answer my own questions.

## Day 4 — Idioms & phrasal verbs: Project phrasal verbs: roll out, scale up, sign off {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| roll out | Release or introduce something gradually or widely; noun `rollout`. Neutral. | We will roll out the new routing engine to three regions first. |
| scale up | Increase in size or capacity; opposite `scale down`. Neutral. | If the pilot succeeds, we can scale up to all carriers in Q2. |
| sign off (on) | Give formal approval; noun `sign-off`. Neutral, common in US and UK. | Legal has not yet signed off on the data-sharing clause. |
| phase out | Withdraw gradually in stages. Neutral. | We will phase out the legacy SOAP endpoint over two quarters. |
| ramp up | Increase gradually to a higher level of activity or output; opposite `ramp down`. Neutral to informal. | The team will ramp up on the integration once the vendor delivers the sandbox. |

**Grammar note:** `roll out`, `scale up`, `phase out`, `ramp up` are separable or inseparable depending on the verb: `roll out the feature` / `roll the feature out` (both fine); `sign off on the design` (inseparable, needs `on`); `scale up the cluster` / `scale it up`; `phase out the service` / `phase it out`. Pronouns go in the middle: `roll it out`, not `roll out it`.

### Exercise

Choose or complete (8).

1. The security team has not ______ on the design. (signed off / rolled out)
2. Rewrite: `We will introduce the feature gradually to all customers.`
3. Fix: `We will roll out it next month.`
4. `We are retiring the old API in stages.` Which phrasal verb? 
5. `______ the staffing before the peak season.` (Ramp up / Phase out)
6. Rewrite with `scale up`: `If the pilot works, we will expand it to every port.`
7. True or false: `Sign-off` is a noun and `sign off` is a verb.
8. What is the difference between `roll out` and `scale up`?

??? success "Answers and explanations"
    1. **signed off**: gives formal approval (`signed off on the design`).
    2. `We will **roll out** the feature to all customers.`
    3. `We will **roll it out** next month.` Pronoun in the middle.
    4. **phase out** (gradual withdrawal).
    5. **Ramp up**: increase gradually before peak season.
    6. `If the pilot works, we will **scale it up** to every port.`
    7. **True**: `sign-off` (noun, hyphenated) and `sign off` (verb).
    8. `Roll out` = release/deploy (breadth and timing); `scale up` = increase capacity or size (volume). You can roll out a feature without scaling anything up.

!!! warning "When NOT to use them"
    Phrasal verbs sound natural in speech and internal notes, but they can confuse readers who learned English formally. In contracts, formal reports and documentation for non-native readers, prefer single-word verbs: `approve`, `deploy`, `withdraw`, `increase`. Also watch for `ramp up` in HR contexts, where it may mean `training` and be misread. Do not use `roll out` for a one-off change (say `release` or `ship`).

## Day 5 — Writing: Blameless postmortem prose {#day-5}
**⏱ 30 min · Fri**

**Bad draft:**

> On Tuesday Ravi pushed a bad config to prod without asking anyone and it broke the booking API. The on-call guy was asleep and did not answer his page for 25 minutes, which was really bad. Then the team finally rolled it back, but customers were already really angry. It should never have happened and people need to be more careful.

**Task:** Rewrite as the **Summary and Timeline** section of a blameless postmortem in 130-170 words. Constraints: no names or blame words (`careless`, `bad`, `asleep`); use passive where it removes blame and active where a system or team acts; include three timestamps (invent them); end with one contributing-factor sentence about the system, not a person.

??? success "Model answer and what changed"
    > **Summary.** On Tuesday, a configuration change was deployed to production that caused the booking API to return errors for 48 minutes. Approximately 3,200 bookings failed.
    >
    > **Timeline (UTC).**
    > - 09:12: A configuration change was applied to the routing service.
    > - 09:14: Error rates rose above 20 percent; an alert was sent to the primary on-call.
    > - 09:39: The page was escalated to the secondary on-call after no acknowledgment.
    > - 10:00: The change was rolled back and service was restored.
    >
    > **Contributing factors.** The deployment pipeline allowed configuration changes to reach production without a review gate or a staged rollout, and the alert threshold did not distinguish a paging failure from a delay in acknowledgment.

    - **Names removed, systems named:** `Ravi` and `the on-call guy` became roles and system components.
    - **Passive used deliberately** for actions where the person is irrelevant (`was applied`, `was rolled back`), and **active for systems** (`rates rose`, `the pipeline allowed`).
    - **Value words removed:** `bad`, `really angry`, `should never have happened`, `be more careful`. Facts replaced them (`48 minutes`, `3,200 bookings`).
    - **Timestamps** make the sequence checkable; `approximately` conveys an estimate honestly.
    - **Ends with a system-level cause,** which points to a fix (a review gate) rather than a person.

## Day 6 — Speaking record: Question intonation and turn-taking {#day-6}
**⏱ 30 min · Sat**

**Record a 2-minute talk:** Play both roles in a role-play. First, chair a 1-minute mini-discussion of a real technical proposal in your team: ask one yes/no question, one wh- question, interrupt yourself politely, and invite a named person. Then, for the second minute, answer your own question as a colleague, using `approximately`, `marginally` or `materially` with a number. Listen for intonation on your questions.

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Unclear which role is speaking | Some confusion | Clear roles, minor drift | Roles and questions clearly signposted |
| Structure | No order | Order weak | Open, ask, manage, invite present | All four moves, smoothly linked |
| Fluency | Frequent stops | Several long pauses | Occasional hesitation | Smooth and controlled |
| Grammar accuracy | Errors block meaning | Frequent errors, incl. passive errors | Few errors | Passive and active used correctly |
| Vocabulary range | Repetitive | Basic words only | Precision words used correctly | Precise, varied, natural |
| Pronunciation | Flat pitch | Pitch patterns often wrong | Rising and falling mostly correct | Natural intonation throughout |

**Shadowing task:** Shadow 2 minutes of a live Q&A or panel discussion from a conference talk (for example, a recorded developer-conference panel or a BBC Learning English interview episode). Focus on how the moderator asks questions and interrupts. Do it three times: first listening, then shadowing with the transcript, then without it.

**Log your score:** total out of 24 in `docs/log/`, plus one line on which question type (yes/no or wh-) you got wrong.

## Day 7 — Soft skills + weekly review: De-escalating conflict {#day-7}
**⏱ 30 min · Sun**

**Scenario.** In a cross-team sync, Dev lead Ben and QA lead Isabel are arguing. Ben says: "We shipped exactly what the spec said. If QA missed the bug, that's on them." Isabel replies: "The spec was incomplete, and you never asked us." Voices are rising, six other people are watching, and you are the facilitator with no line authority over either.

**Task.** Script what you say to lower the temperature, in about 150 words.

??? success "Model response and techniques"
    > Let me pause us for a moment. I can hear that you both care about getting this right, and I do not think either of you wants to spend the next ten minutes on who is at fault. Ben, what I am hearing is that the team built to the spec you had. Isabel, what I am hearing is that the spec left gaps that nobody caught before testing. Is that a fair summary? [pause] Both can be true. The gap is in our process, not in either team. So let us do two things: first, agree what the customer impact is right now, and second, decide who owns closing the spec gap before the next release. Ben, could you take the first fifteen minutes on impact, and Isabel, could you draft the missing acceptance criteria? We can review in tomorrow's stand-up.

    **Techniques used**

    - **Interrupt with a pause request**, calmly and without blame (`Let me pause us`).
    - **Label the shared intent** (`you both care about getting this right`).
    - **Paraphrase each side neutrally** and check accuracy (`Is that a fair summary?`), which reduces defensiveness.
    - **Reframe the problem as process**, not person, and use `both can be true`.
    - **Move to actions:** two small tasks with owners and a time, redirecting energy.
    - **Voice:** lower pitch and pace; falling intonation on statements; short sentences. Use question intonation for the check (`fair summary?` rising).

### Weekly recap (20 items)

1. Which verbs cannot be passive: `happen`, `deploy`, `fail`, `review`?
2. Correct: `The outage was occurred at 3 a.m.`
3. Correct: `The alerts have been suppress.`
4. What is a dangling modifier? Correct: `By adding a cache, latency was reduced.`
5. Two situations when the passive is the better choice.
6. Why is `It was decided that mistakes were made` weak?
7. Preferred structure: `Read-only access was given to us.`
8. `Approximately` is used with what kind of figure?
9. Which word means `barely`?
10. Which word means `significant enough to matter to a decision`?
11. Which word means `so small it can be ignored`?
12. Order: negligible, appreciable, marginal, material (smallest to largest).
13. Meaning and one example of `roll out`.
14. `sign off` meaning; and correct: `Legal signed off the plan` (which preposition?).
15. Opposite of `scale up`.
16. Correct: `We will phase out it.`
17. Intonation of a wh- question.
18. Intonation of a yes/no question.
19. One polite way to interrupt.
20. Name three moves in the de-escalation model response.

??? success "Answers and explanations"
    1. `happen`, `fail` (intransitive).
    2. `The outage occurred at 3 a.m.`
    3. `have been suppressed`.
    4. A modifier with no logical subject in the main clause. `By adding a cache, we reduced latency.`
    5. Agent unknown or irrelevant; blameless writing; topic continuity.
    6. It hides who decided and who erred, so it reads evasive.
    7. `We were given read-only access.`
    8. An approximate, rounded figure (not an exact number).
    9. marginally.
    10. materially.
    11. negligible.
    12. negligible, marginal, appreciable, material.
    13. Release or introduce gradually or widely: `We will roll out the feature to three regions.`
    14. Formal approval; `signed off on the plan`.
    15. scale down.
    16. `We will phase it out.`
    17. Falling.
    18. Rising.
    19. `Sorry to cut in, but...` or `Let me stop you there.`
    20. Pause, label shared intent, paraphrase and check, reframe to process, assign actions (any three).

**Self-score**

- [ ] I can choose passive or active deliberately and can spot dangling modifiers.
- [ ] I used approximately, marginally, materially, negligible, appreciably correctly.
- [ ] I used roll out, scale up, sign off, phase out, ramp up in real sentences.
- [ ] My yes/no questions rise and my wh- questions fall.
- [ ] I can write a blameless timeline.
- [ ] I can de-escalate a heated exchange in three or four sentences.

**Error log:** write down your top 3 recurring mistakes this week (for example, passive of intransitive verbs, missing participle endings, pitch on questions) and a correct model sentence for each.
