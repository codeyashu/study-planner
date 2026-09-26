---
title: "Week 08 drills — Fluent-speaker errors, presentations and the RFC intro"
track: communication
week: 8
last_reviewed: 2026-09-25
---

# Week 08 — Fluent-speaker errors, presentations and the RFC intro

!!! abstract "This week"
    **Grammar:** Common errors of fluent speakers: uncountables, word order, false friends · **Vocabulary:** Review and 100-word check · **Idioms & phrasal verbs:** Idiom review and usage in speech · **Speaking:** Deliver a 5-minute presentation · **Writing:** Writing an RFC introduction · **Soft skill:** Handling tough questions
    **Checkpoint comm-2 (end of this week):** record your 5-minute presentation (Day 6), score it with the rubric, take the 100-word check (Day 2), and compare with your Week 0 baseline in `docs/log/comm-baseline.md`. Note which three error patterns still recur.

## Day 1 — Grammar: Common errors of fluent speakers: uncountables, word order, false friends {#day-1}
**⏱ 30 min · Mon** Fluent speakers rarely make beginner errors. They make *stable* errors: patterns that survive years because they never block communication. This day targets three of them.

### Rule in 60 seconds

**1. Uncountable nouns.** These have no plural and no `a/an`, and take `much / a little / less`, not `many / a few / fewer`. Work nouns are the trap: `advice, information, feedback, equipment, software, hardware, knowledge, research, progress, evidence, infrastructure, traffic, luggage, news, furniture, work (= labor)`.

- Quantify with a unit: `a piece of advice`, `an item of feedback`, `a piece of software`, `a body of research`.
- Wrong: `informations, an advice, feedbacks, softwares, an equipment, researches (noun)`. `Research` as a verb is fine (`She researches the topic`).
- `Data`: both `The data is / are` are accepted; in business and US usage `The data is` is the norm. Pick one and be consistent.
- `Staff` and `team` are collective nouns: `The staff is/are` (US/UK differ; either is fine, be consistent).
- `A good knowledge of` and `a working knowledge of` are established fixed phrases; do not generalize them to `a knowledge`.
- `Less` with uncountables, `fewer` with countable plurals: `less latency`, `fewer incidents`.

**2. Word order.**

- **Frequency adverbs** go before the main verb and after `be`: `We always review`, `He is usually late`, `We have never seen this`. Not: `We review always`, `Always we review` (unless for emphasis).
- **Do not put an adverb between verb and direct object:** `I like this design very much`, not `I like very much this design`.
- **Manner, place, time order** for endings: `We deployed the fix carefully to production yesterday.`
- **Indirect questions use statement order:** `Can you tell me where the log is?`, `I wonder why it failed.` (Direct: `Where is the log?`).
- **`Explain / suggest / describe / mention / say`** take `to` before the person: `explain it to me`, never `explain me`.
- **`enough`** goes after an adjective/adverb but before a noun: `fast enough`, `enough time`.
- **`only`** goes directly before what it limits: `I only sent him the draft` (nothing else was done) vs `I sent only him the draft` (nobody else received it).

**3. False friends and near-synonyms.** Two families:

- **English-internal confusables:** `actually` (in fact; does not mean "currently"), `eventually` (in the end, after a long time; not "possibly"), `sensible` (practical, rational) vs `sensitive` (easily affected; confidential data), `economic` (relating to the economy) vs `economical` (saves money), `historic` (important in history) vs `historical` (related to the past), `continual` (repeated) vs `continuous` (without break).
- **L1 transfer false friends** depend on your first language. Common examples: `control` (French/Spanish/Italian `controler`, meaning "check": say `verify` or `check`), `assist` (meaning "attend": use `attend`), `resume` (`résumé` is a CV), `pretend` (Spanish `pretender`, meaning "intend").
- **Indian English (if relevant to you):** `prepone`, `revert back`, `do the needful`, `out of station` are fully normal within India but are unclear to many international readers. Use `move earlier / bring forward`, `reply`, `please take the necessary action / please do X`, `out of town`. `Revert` means "go back to a previous state" to most global readers; a code `revert` is a rollback.

**The error fluent speakers make** is to trust "it sounds right". For these three families, the fix is a checklist, not intuition: scan every draft for `informations/feedbacks/softwares`, for adverbs after the verb, and for suspicious cognates.

### Exercise

Correct each sentence (10).

1. Thanks for the informations and the feedbacks.
2. She gave me an advice about the retry policy.
3. Can you tell me where is the deployment log?
4. I explained him the trade-offs.
5. We have got less bugs this sprint.
6. I like very much this architecture.
7. Customer data is very sensible, so we encrypt it.
8. Choose: The cheaper cloud tier is more (economic / economical) in the long run.
9. We deploy on Fridays never.
10. The equipment are outdated and the software need updating.

??? success "Answers and explanations"
    1. `Thanks for the **information and feedback**.` Both are uncountable; no plural.
    2. `She gave me **a piece of advice**` / `some advice`. `Advice` is uncountable.
    3. `Can you tell me **where the deployment log is**?` Embedded questions use statement order.
    4. `I explained **the trade-offs to him**.` `Explain` needs `to` before the person.
    5. `We have **fewer bugs** this sprint.` `Bug` is countable, so `fewer`.
    6. `I like this architecture **very much**.` Adverb cannot sit between verb and object.
    7. `Customer data is very **sensitive**.` `Sensible` means reasonable.
    8. **economical.** It means good value; `economic` relates to the economy.
    9. `We **never deploy** on Fridays.` Frequency adverb precedes the main verb.
    10. `The equipment **is** outdated and the software **needs** updating.` Both are uncountable and take singular verbs.

### Use it
Look at your last three Slack or email messages. Find any uncountable noun, any adverb placement, and any suspicious cognate. Rewrite one sentence correctly, then say it aloud.

## Day 2 — Vocabulary: Review and 100-word check {#day-2}
**⏱ 30 min · Tue** Five new words to close out Weeks 1-8, then a 100-word self-audit.

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| corroborate | verb | To confirm a claim with a second, independent source of evidence. | The vendor's benchmark was corroborated by our own load test. |
| pragmatic | adjective | Focused on what works in practice rather than on theory or ideals. | Given the deadline, the pragmatic option is to ship a read-only mode first. |
| contentious | adjective | Likely to cause disagreement; controversial. | Ownership of the shared schema is a contentious issue between the two teams. |
| salient | adjective | Most noticeable or important; stands out. | The most salient point in the postmortem is that no alert fired for 40 minutes. |
| scrutiny | noun | Close, critical examination; usually uncountable (under scrutiny, face scrutiny). | The proposal will face scrutiny from the architecture board. |

### Collocations and word family

- **corroborate:** corroborate a claim / account / finding / evidence; noun `corroboration`, adjective `corroborating` (corroborating evidence). Stronger than `confirm` because the source is independent.
- **pragmatic:** a pragmatic approach / solution / choice / view; adverb `pragmatically`; noun `pragmatism`. Not the same as `practical` (usable): `pragmatic` describes a person's or plan's attitude.
- **contentious:** a contentious issue / decision / point / debate; noun `contention` (a point of contention). `Controversial` is the everyday synonym.
- **salient:** a salient point / feature / fact; noun `salience`. Often followed by `feature` in product and design talk.
- **scrutiny:** careful / close / intense / public scrutiny; under scrutiny; verb `scrutinize`; adjective `scrutable` is rare.

### Exercise

Fill each gap with the right word (8). Review words from earlier weeks are included: **tangible, substantiate, mitigate, rationale**.

1. Two independent audits ______ the vendor's claim about uptime.
2. Sharing production access with contractors is a ______ topic in the security council.
3. The ______ feature of the outage was that customers noticed before we did.
4. Each line of the budget will come under ______ before the CFO signs it.
5. A ______ compromise is to cache stale data for five minutes, rather than build a perfect invalidation system.
6. The steering group asked for ______ savings, not projections.
7. Please ______ your claim that the new index cut latency by half.
8. What is the ______ for delaying the migration, and how do we ______ the customer impact?

??? success "Answers and explanations"
    1. **corroborated** (confirmed by a second source).
    2. **contentious**: it causes disagreement.
    3. **salient**: the most noticeable feature.
    4. **scrutiny**: examination; uncountable, no article.
    5. **pragmatic**: what works in practice.
    6. **tangible** (review): measurable, real.
    7. **substantiate** (review): support with evidence.
    8. **rationale** (review) and **mitigate** (review).

### The 100-word check

Rate each word: **1** = I can use it correctly in a spoken sentence right now; **0.5** = I recognize it but would hesitate to use it; **0** = not sure. Do not look anything up. Time yourself: 10 minutes.

**Band A (Weeks 1-3):** assess, mitigate, prioritize, affect, impact, influence, ensure, assure, insure, champion, unblock, de-risk, validate, allocate, anticipate, accommodate, clarify, constrain, defer, delegate.

**Band B (Weeks 4-5):** presumably, ostensibly, conceivably, seemingly, consequently, whereas, hinge on, thereby, albeit, conversely, subsequently, predominantly, inherent, viable, feasible, redundant, ambiguous, coherent, concise, verbose.

**Band C (Weeks 6-7):** make a case, raise a concern, draw a conclusion, reach a consensus, address an issue, set a precedent, meet a deadline, take ownership, weigh the options, strike a balance, compelling, tangible, rationale, substantiate, resonate, intangible, plausible, credible, pertinent, incremental.

**Band D (Week 8 and general):** corroborate, pragmatic, contentious, salient, scrutiny, ubiquitous, obsolete, resilient, deprecate, fragile, opaque, granular, seamless, cumbersome, robust, latent, arbitrary, deliberate, trivial, imminent.

**Band E (idioms and phrasals, Weeks 1-7):** touch base, ballpark, on the same page, behind schedule, move the needle, in the pipeline, up in the air, meet halfway, off the table, low-hanging fruit, moving parts, bring up, follow up, wrap up, pull your weight, have each other's back, throw under the bus, roll up your sleeves, wear many hats, get buy-in.

**Scoring (out of 100):** 0-54 revisit each band's earlier drill tables; 55-74 solid B2+, with words to activate; 75-89 strong C1 range for this set; 90+ you can rely on these words under pressure. Record your total and your weakest band in `docs/log/comm-baseline.md` as the comm-2 checkpoint. Re-drill every `0` and `0.5` word by writing a workplace sentence for each.

### Use it
Pick the five lowest-confidence words from your check. Write one sentence for each about your own project and say each aloud twice.

## Day 3 — Speaking: Deliver a 5-minute presentation {#day-3}
**⏱ 30 min · Wed** Today you plan and rehearse; Saturday you record.

**Prompt:** Give a 5-minute presentation to your director on one technical decision you would make for your platform in the next quarter (for example, adopting a message broker, consolidating two services, or introducing an evaluation harness for an LLM feature). No slides needed: use five index-card notes.

**Structure: Hook, Roadmap, Three points, Recap, Ask**

1. **Hook (20 s):** a fact, a customer story or a question. `Last quarter, we spent 120 engineering hours on incidents that had the same cause.`
2. **Roadmap (15 s):** `I will cover three things: the problem, the option I recommend, and what I need from you.`
3. **Three points (about 3 min):** one card each, each with a claim, one piece of evidence and a transition (`That brings me to...`).
4. **Recap (30 s):** `To summarize...`
5. **Ask (30 s):** a specific decision with a date. `I am asking for approval to start in Q1.`

Signposting phrases: `First / Second / Finally`, `Let me turn to...`, `The key point here is...`, `Before I go on, does this raise any questions?`

**Pronunciation micro-drill: past-tense -ed endings** Three sounds, decided by the last sound of the verb.

| Sound | Rule | Words |
|---|---|---|
| /t/ | after voiceless sounds (p, k, f, s, sh, ch) | launched, worked, stopped, pushed, fixed, patched |
| /d/ | after voiced sounds and vowels | deployed, logged, moved, scaled, configured, failed |
| /ɪd/ | after /t/ or /d/ | needed, tested, migrated, escalated, updated, decided |

Correct sets to say aloud (three repetitions each): **/t/:** launched, worked, stopped, pushed, fixed, patched. **/d/:** deployed, logged, moved, scaled, configured, failed. **/ɪd/:** tested, migrated, escalated, needed, updated, decided.

Common error: adding an extra syllable to /t/ and /d/ verbs (`work-ED`, `deploy-ED`) or dropping it from /ɪd/ verbs (`tes'`, `escalate'`). Say the sentence: `We tested, patched and deployed it, then escalated when it failed.` Only *tested* and *escalated* get an extra syllable.

**Self-check**

- [ ] I opened with a hook, not "Today I will talk about...".
- [ ] I gave a roadmap of exactly three items and followed it.
- [ ] Each point had a claim, evidence and a transition.
- [ ] I ended with a specific ask and a date.
- [ ] My past-tense endings were clear, with no extra syllables.

## Day 4 — Idioms & phrasal verbs: Idiom review and usage in speech {#day-4}
**⏱ 30 min · Thu** Five fresh expressions that extend the idioms of Weeks 1-7, for the moments when people forget to reach for an idiom at all.

| Expression | Meaning | Example |
|---|---|---|
| keep (someone) in the loop | Keep someone regularly informed about progress or decisions; neutral, common in US and UK business. | Please keep the port operations team in the loop on the cutover plan. |
| a game changer | Something that fundamentally changes a situation or market; informal, common in US and UK business, sometimes hype. | Event-driven tracking was a game changer for our exception handling. |
| in limbo | Stuck in an uncertain state, waiting for a decision or outcome; neutral in US and UK. | The second-phase budget has been in limbo since the reorganization. |
| split the difference | Compromise by settling on a point midway between two positions; informal, common in negotiation in US and UK English. | Let's split the difference: a four-week freeze instead of two or six. |
| a quick win | A small, easy action that gives a visible benefit fast; neutral in US and UK business English. | Deleting unused dashboards is a quick win that saves 15 percent of the bill. |

### Exercise

Choose the best expression or rewrite (8).

1. Rewrite plainly: `The launch date has been in limbo since the reorg.`
2. `Automating the weekly report will be a real ______ (game changer / keep in the loop) for team productivity.` Is that plausible? Explain.
3. Fill: `Please ______ on the cutover so the carriers are not surprised.` (keep us in the loop / split the difference)
4. Rewrite idiomatically: `We each need to compromise on the rollout scope, ending up in the middle.`
5. Choose the best: `Renaming the variables is ______.` (a quick win / a game changer) as a description of an easy fix with modest value.
6. A colleague writes `I will keep you in the loop` in a formal letter to a client's board. Better alternative?
7. Which idiom describes a development that fundamentally changes the whole situation (informal, sometimes hype)?
8. `We agreed to split the differences on the freeze length.` Fix.

??? success "Answers and explanations"
    1. `The launch date has not been decided.` / `We are not sure of the launch date yet.`
    2. **Not plausible.** Automating a weekly report saves minutes; `game changer` implies a fundamental shift, not a small saving.
    3. **keep us in the loop**: keep informed; `split the difference` is about compromise, not information.
    4. `We could **split the difference** on the rollout scope.`
    5. **a quick win** describes an easy, fast benefit; `a game changer` would overstate a rename. Note: the idiom implies *fast and easy*, not necessarily *high value*. If you mean low value, say `a cosmetic change`.
    6. `I would welcome the opportunity to discuss progress` or `to update you`.
    7. **a game changer**.
    8. `We agreed to **split the difference** on the freeze length.` The phrase is fixed and singular; `differences` is a common slip.

!!! warning "When NOT to use them"
    Idioms compress meaning for people who share the reference and hurt clarity for those who do not. Avoid clusters (`Let's keep everyone in the loop on the quick wins so this can be a game changer`), formal letters, contracts, and calls with mixed-fluency audiences. In writing for a global audience, prefer the plain version. Also check the register: `game changer` can sound like hype if it is not backed by numbers.

## Day 5 — Writing: Writing an RFC introduction {#day-5}
**⏱ 30 min · Fri**

**Bad draft:**

> Hi all, this RFC is about the thing where our onboarding takes too long. Currently, customer onboarding is slow, and many customers are complaining, and there has been a lot of confusion about who owns what. We propose to think about maybe changing the architecture, which includes a lot of stuff, in order that things can be improved. Please give feedbacks.

**Task:** Rewrite as an RFC introduction (120-160 words) with four labeled parts: **Summary**, **Problem**, **Goals and non-goals**, **Request**. Constraints: at least one number (invent a plausible one), no uncountable-noun errors, no vague words (`thing`, `stuff`), and a specific deadline for feedback.

??? success "Model answer and what changed"
    > **Summary.** This RFC proposes replacing the manual, ticket-driven customer onboarding flow with an automated workflow owned by the Platform team.
    >
    > **Problem.** Onboarding a new shipping customer currently takes a median of 19 days, against a target of 5. Most of the delay is hand-offs between three teams, and no single team is accountable for the outcome. Support handled 140 onboarding complaints last quarter.
    >
    > **Goals.** Cut median onboarding time to 5 days; assign one accountable owner. **Non-goals.** Redesigning billing or the customer portal.
    >
    > **Request.** Please review the design in section 3 and send feedback by 10 October. I am especially interested in comments on the ownership model.

    - **Structure is explicit:** labeled sections let readers skim and comment on the right part.
    - **Vague words replaced with facts:** `the thing`, `a lot of stuff` became a proposal, a number, and an owner.
    - **Specific ask and deadline** replaced `Please give feedbacks` (also fixes the uncountable: `feedback`).
    - **Active, decisive verbs:** `proposes replacing` rather than `propose to think about maybe changing`.
    - **Scope boundaries** (non-goals) prevent scope creep and focus the debate.
    - `in order that things can be improved` became a measurable goal.

## Day 6 — Speaking record: Deliver a 5-minute presentation {#day-6}
**⏱ 30 min · Sat** This is the one week where the recorded talk runs 5 minutes rather than 2: it is the comm-2 checkpoint recording.

**Record:** your 5-minute presentation from Day 3, using the Hook, Roadmap, Three points, Recap, Ask structure. Stand up, use your index cards, and time yourself. Record once as a real attempt; play it back; re-record once if you want. Save the best take.

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Message unclear | Point emerges late | Clear with minor drifts | Every section serves one message |
| Structure | No visible order | Roadmap missing or ignored | Roadmap followed, weak transitions | Roadmap, signposts, recap and ask all present |
| Fluency | Frequent stops and fillers | Noticeable pauses | Mostly smooth, few fillers | Deliberate pauses, no fillers |
| Grammar accuracy | Errors block meaning | Frequent errors | Few errors, uncountables mostly right | Rare slips |
| Vocabulary range | Repetitive | Some variety | Precise business words | Precise, varied, natural |
| Pronunciation | Hard to follow | Frequent stress errors | Clear; some -ed or stress slips | Clear stress, rhythm and endings |

**Shadowing task:** Choose a talk of 5-8 minutes from TED or a conference talk where the speaker signposts clearly (for example, a talk recorded at a developer conference). Shadow the first 60 seconds three times, copying the signposts and pauses. Then write down five signposting phrases you heard.

**Log your score:** total out of 24, plus duration, plus the number of filler words you counted (um, like, you know) in `docs/log/comm-baseline.md` for comm-2.

## Day 7 — Soft skills + weekly review: Handling tough questions {#day-7}
**⏱ 30 min · Sun**

**Scenario.** In a quarterly review, the VP of Operations, Anders, interrupts your presentation: "You told us six months. It took nine and cost 40 percent more. Why should we trust the next estimate?" The room goes quiet. You are the program lead and you have actual reasons, including two scope changes he approved.

**Task.** Script your 150-word answer.

??? success "Model response and techniques"
    > That is a fair question, and you are right about both numbers. I underestimated the integration work, and I should have flagged the slip earlier than I did. Three things drove the overrun: the carrier API change in March, the two scope additions we agreed in April, and my estimate not including a buffer for either. What I have changed: estimates now carry an explicit contingency, and any change over two weeks comes to you with a cost before we accept it. For the next phase, I can give you a range, eight to ten months, with the assumptions listed, and a checkpoint at month three where we confirm or reset. If it would help, I will share the variance breakdown after this meeting.

    **Techniques used**

    - **Pause, then concede the fair part** (`you are right about both numbers`) instead of defending immediately.
    - **Own your share** without self-flagellation, then **state causes briefly**, including the scope changes, without blaming him.
    - **Bridge from past to future:** what has changed and how the next estimate is different.
    - **Give a range with assumptions** rather than a false promise.
    - **Offer evidence and a next step.**
    - Tone: calm, short sentences, no filler; the loaded premise (`why should we trust`) is answered by actions, not reassurance.

    Other tough-question tactics: for a hostile question, restate it neutrally first; for a vague one, ask `Which part concerns you most?`; for one outside your remit, say `I don't know, and I will find out by Friday`.

### Weekly recap (20 items)

1. Give two examples of uncountable nouns that are often made plural by mistake.
2. Correct: `Can you tell me where is the log?`
3. Where does `always` go in `We review always`?
4. Correct: `She suggested me a fix.`
5. Difference between `sensible` and `sensitive`.
6. Difference between `economic` and `economical`.
7. What does `eventually` mean?
8. Fewer or less: `___ incidents`, `___ latency`.
9. Definition: `corroborate`.
10. Which adjective: `Ownership is a ______ issue` (causing disagreement)?
11. Which noun: `The plan faces ______`?
12. `Salient` means?
13. Idiom meaning `stuck in an uncertain state, waiting for a decision`.
14. Idiom meaning `something that fundamentally changes the situation` (informal).
15. `split the difference` means?
16. Correct: `We deployed yesterday to production the fix.`
17. Pronounce the -ed ending in `launched`, `needed`, `deployed`.
18. What are the five parts of the presentation structure?
19. What does an RFC `non-goal` do?
20. What is the first move when answering a hostile question?

??? success "Answers"
    1. `information`, `feedback`, `advice`, `equipment`, `software` (any two).
    2. `Can you tell me where the log is?`
    3. Before the verb: `We always review`.
    4. `She suggested a fix to me` / `She suggested that I try X.`
    5. `Sensible` = reasonable; `sensitive` = easily affected or confidential.
    6. `Economic` = of the economy; `economical` = saves money.
    7. In the end, after a delay or long process.
    8. `fewer incidents`, `less latency`.
    9. Confirm with independent evidence.
    10. contentious.
    11. scrutiny.
    12. Most noticeable or important.
    13. in limbo.
    14. a game changer.
    15. Compromise; each side gives something.
    16. `We deployed the fix to production yesterday.`
    17. launched /t/, needed /ɪd/, deployed /d/.
    18. Hook, Roadmap, Three points, Recap, Ask.
    19. It sets scope boundaries to keep the debate focused.
    20. Pause and concede what is fair or restate the question neutrally.

**Self-score**

- [ ] I avoid plural forms of uncountable nouns in writing.
- [ ] I put adverbs in the right place without thinking.
- [ ] I scored the 100-word check and logged it.
- [ ] I delivered and recorded a 5-minute presentation with a clear structure.
- [ ] I can answer a tough question without defensiveness.
- [ ] I completed the comm-2 checkpoint and compared with my baseline.

**Error log:** write down your top 3 recurring mistakes from Weeks 1-8 (for example, uncountable plurals, indirect-question order, -ed syllables) and one correct model sentence for each.
