---
title: "Week 01 drills — Articles, precision verbs, BLUF"
track: communication
week: 1
last_reviewed: 2026-09-25
---

# Week 01 — Articles, precision verbs, BLUF

!!! abstract "This week"
    **Grammar:** Articles and determiners: a/the/zero · **Vocabulary:** Precision verbs for business (assess, mitigate, prioritize, quantify, substantiate) · **Idioms & phrasal verbs:** Workplace basics: touch base, ballpark, on the same page, circle back, heads-up · **Speaking:** Pace and deliberate pausing · **Writing:** Concise emails and subject lines (BLUF) · **Soft skill:** Active listening and clarifying questions

## Day 1 — Grammar: Articles and determiners: a/the/zero {#day-1}
**⏱ 30 min · Mon**

### Rule in 60 seconds
- **a / an** + singular countable noun that is *new* or *non-specific*: "We hit **a** bottleneck." (Use *an* before a vowel *sound*: **an** hour, **an** API, **an** SLA, **a** user, **a** URL, **a** European vendor.)
- **the** when the listener can identify the noun: already mentioned, unique ("the CTO", "the internet"), made specific by a modifier ("**the** service that failed"), or obvious from context ("**the** dashboard" in a team with one dashboard). Also with superlatives and ordinals ("**the** second option", "**the** most critical path").
- **zero article** with plural or uncountable nouns used in a general sense: "**Latency** hurts conversion." "**Engineers** dislike ambiguity." Also with most fixed expressions: *in production, on call, by email, at scale, in progress, on schedule*.
- Exceptions to watch: *in the cloud, on the network, in the pipeline, at the moment, on the phone*. Learn them as chunks.
- **The error fluent speakers make:** (1) dropping the article before a singular countable noun ("We need to update database"); (2) over-using *the* with general abstract or plural nouns ("**The** reliability is important"); (3) treating uncountables as countable ("an advice", "informations"). Speakers whose first language has no articles (Russian, Hindi in many registers, Chinese, Japanese) tend to drop them; Romance-language speakers tend to add *the* before abstractions.
- Shortcut question: **Singular countable? Then you need a determiner (a/the/my/this...). No exception.**

### Exercise
Each sentence contains one or two article errors. Rewrite it correctly.

1. We need to update database schema before Friday's release.
2. The scalability is a key challenge for us.
3. He is engineer with ten years of experience.
4. Can we have a meeting on the Friday?
5. It was a most difficult migration we have ever done.
6. We use the Kubernetes in a production.
7. I need an advice from senior architect.
8. The engineers should not make the assumptions about the users' data.
9. It took us a hour to find the root cause.
10. We sent the notification to the all customers by the email.

??? success "Answers and explanations"
    1. We need to update **the** database schema... (a specific schema both people know; singular countable needs a determiner.)
    2. Scalability is a key challenge... (general abstract noun: zero article.)
    3. He is **an** engineer... (job/role: singular countable, non-specific.)
    4. ...on Friday? (Days of the week take no article.)
    5. ...**the** most difficult migration we have ever done. (Superlative takes *the*.)
    6. We use Kubernetes in production. (Product names: zero; *in production* is a fixed phrase.)
    7. I need advice from **a** senior architect. (*Advice* is uncountable; *architect* is singular countable.)
    8. ...should not make assumptions about users' data. (General plurals: zero. Also acceptable in careful writing: "the users'" if you mean specific users, but here it is general.)
    9. ...**an** hour... (silent *h*, vowel sound.)
    10. ...to all customers by email. ("To all the customers" is also correct if you mean a specific group; "by email" always zero.)

### Use it
Write three sentences about your current project using: one *a/an* for a new thing, one *the* for something both of you know, one general plural or uncountable noun with no article. Read them aloud.

## Day 2 — Vocabulary: Precision verbs for business (assess, mitigate, prioritize) {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| assess | verb | to evaluate the nature, quality or size of something, usually with a defined method | We need to assess the impact of the schema change on downstream consumers before approving it. |
| mitigate | verb | to reduce the severity or likelihood of harm (not to remove it entirely) | Regional failover mitigates the risk of a single-datacenter outage. |
| prioritize | verb | to decide what is most important and handle it first (US spelling; UK also *prioritise*) | With two engineers out, we prioritized the customs-clearance fixes over the dashboard redesign. |
| quantify | verb | to express or measure something as a number | Can you quantify how much latency the new proxy adds at peak load? |
| substantiate | verb | to support a claim with evidence | The vendor could not substantiate its claim of 99.99 percent availability. |

### Collocations and word family
- **assess** a risk / the impact / the feasibility / performance; noun *assessment* (a risk assessment); *reassess*.
- **mitigate** a risk / the impact / the effects / exposure; noun *mitigation* (a mitigation plan). Note: *mitigate* is not the same as *militate*, and it is not a synonym of *eliminate*.
- **prioritize** tasks / requirements / bugs; noun *priority* (top priority, competing priorities); *prioritization*. Not "prioritize the priority".
- **quantify** the risk / the benefit / the cost / the savings; adjective *quantifiable*; opposite *intangible*.
- **substantiate** a claim / an allegation / a forecast; adjective *substantiated*, *unsubstantiated*; noun *substantiation*.

### Exercise
Fill each gap with the best word from this week (change the form if needed).

1. Before we commit to the vendor, we should ___ their security posture with an independent audit.
2. The team ___ the backlog by customer impact.
3. Retries with exponential backoff ___ the effect of transient network failures.
4. Your proposal says the new cache will "significantly" reduce load. Can you ___ that? A percentage would help.
5. The claim that the outage cost us millions was ___; nobody had produced the calculation.
6. We need a ___ plan in case the migration window overruns.
7. It is hard to ___ the value of better documentation, but we can measure onboarding time.
8. The postmortem should ___ every cause it names with logs or metrics.

??? success "Answers and explanations"
    1. assess (evaluate with a method). 2. prioritized (ordered by importance). 3. mitigate (reduce, not eliminate; retries do not remove failures). 4. quantify ("a percentage would help" = express as a number). 5. unsubstantiated (a claim without evidence). 6. mitigation (noun modifier). 7. quantify (turning value into a number; "measure" is the follow-up). 8. substantiate (support with evidence).

### Use it
Say aloud, then write, three sentences about a current risk at your company using *assess*, *mitigate* and *quantify*.

## Day 3 — Speaking: Pace and deliberate pausing {#day-3}
**⏱ 30 min · Wed**

### Prompt (60-90 seconds)
"Give a status update on the most important project you own, as if speaking to a director who has two minutes: where we are, the main risk, and what you need."

### Structure
1. Headline (one sentence): "The migration is 70 percent complete and on track for November."
2. One risk: "The main risk is vendor delivery."
3. The ask: "I need a decision by Friday."

**Pausing rules.** Speak in **thought groups** of 4-8 words. Pause (about 0.5 s) at the end of each group. Add a longer **spotlight pause** (about 1 s) just *before* the key number or the ask; the pause tells the listener "this matters". Target speed: about 130-150 words per minute. Non-native speakers often speed up under pressure; pausing is the fix.

### Pronunciation micro-drill
Mark the thought groups with slashes and read aloud:

- "The migration is seventy percent done, / but the cutover window / has moved to Saturday."
- "The main risk is the vendor, / not the code."
- "I need one decision from you: / whether we extend the deadline."

Number stress (very common source of misunderstanding on calls): **thir-TEEN** vs **THIR-ty**, **four-TEEN** vs **FOR-ty**, **fif-TEEN** vs **FIF-ty**. In the -teen numbers the stress is on the second syllable (or equal), and the final /n/ is clear; in -ty numbers stress falls on the first syllable and the ending is short. Practice: 13/30, 14/40, 15/50, 16/60, 17/70, 18/80, 19/90.

### Self-check
- [ ] I paused at the end of each thought group, not in the middle of one.
- [ ] I paused before the key number or the ask.
- [ ] My number stress is distinguishable (thirteen vs thirty).
- [ ] I finished sentences with falling intonation instead of trailing off.
- [ ] Playback: I sound calmer than I felt.

## Day 4 — Idioms & phrasal verbs: Workplace basics: touch base, ballpark, on the same page {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| touch base (with someone) | make brief contact to update or check in; informal, common in US and UK business | Let's touch base on Thursday to see where the vendor integration stands. |
| a ballpark figure / ballpark estimate | a rough estimate, good enough for planning; informal, US baseball origin, widely used in UK too | Can you give me a ballpark for the migration cost? |
| be on the same page | share the same understanding of a plan or situation; informal | Before we brief the client, let's make sure we are all on the same page about scope. |
| circle back (to) | return to a topic later; informal, corporate US (some find it jargon) | I don't have the numbers now; I'll circle back to you tomorrow. |
| a heads-up | advance warning; informal, neutral in most workplaces | Just a heads-up: the deploy window moved to 10 p.m. |

### Exercise
Choose the best expression or fill the gap.

1. You don't have exact costs but want to give a rough number. Say: "My ___ is 200,000 euros."
2. After a meeting you realize the two teams understood the scope differently. You want to check: "Are we really ___?"
3. You need to postpone a question until you have data. "Can I ___ on that after the weekend?"
4. You want to warn a colleague about a change before it hits: "Quick ___: the API is deprecated next week."
5. Rewrite plainly: "Let's touch base after the demo."
6. Rewrite idiomatically: "We should check that everybody has the same understanding."
7. Which is too informal for a formal contract email to a customer's legal team: a) touch base b) ballpark c) contact d) all of a and b?
8. Correct the misuse: "I'll ballpark you tomorrow."

??? success "Answers and explanations"
    1. ballpark (figure/estimate). 2. on the same page. 3. circle back. 4. heads-up. 5. "Let's have a short check-in after the demo." 6. "We should make sure we're all on the same page." 7. d (idioms are unsuitable in formal legal correspondence). 8. "I'll give you a ballpark tomorrow." (*ballpark* is a noun here, not a verb; the verb form "ballpark it" exists informally but "ballpark you" is wrong.)

!!! warning "When NOT to use them"
    Avoid stacking idioms ("Let's touch base and circle back so we're on the same page"): it sounds like jargon. Skip them in formal writing, with people who may not share the idiom (many non-native colleagues), and when precision matters: say the date, not "touch base soon".

## Day 5 — Writing: Concise emails and subject lines (BLUF) {#day-5}
**⏱ 30 min · Fri**

**BLUF = Bottom Line Up Front.** The first two lines state the conclusion, the decision needed and the deadline. Details follow for those who want them. The subject line should carry the message: *Action required by Fri: approve 3-week extension for booking migration*, not *Update*.

### Bad draft
> **Subject:** Update
>
> Hi Priya, I hope you are doing well. So as you know we have been working on the booking migration for some time now and there have been a few things that came up. First, the vendor connector arrived late, actually about three weeks later than the date that we had all agreed on, and then when we tested it there was a problem with throughput at high load. Because of this I was thinking that maybe we might need some more time. Let me know your thoughts when you get a chance. Thanks, Rahul

### Task
Rewrite in under 90 words. Constraints: an informative subject line; the decision needed in the first two lines; one date; one recommendation; a fixed deadline for the reply.

??? success "Model answer and what changed"
    > **Subject:** Decision needed by Fri 3 Oct: extend booking migration to 27 Nov?
    >
    > Priya, I recommend extending the booking-service migration from 30 Oct to 27 Nov. Please confirm by Friday.
    >
    > Why: the vendor's connector arrived three weeks late, and testing shows it cannot sustain peak load. Launching on 30 Oct would risk the December peak. The extension adds minimal cost.
    >
    > If you prefer to keep 30 Oct, we can launch with reduced features; I can outline that option today.
    >
    > Rahul

    - **Subject line carries the ask, deadline and topic.**
    - **Conclusion first:** recommendation and deadline in lines 1-2.
    - **Cut the filler** ("I hope you are doing well", "as you know", "for some time now").
    - **Replaced vague hedges** ("maybe we might need some more time") with a concrete recommendation.
    - **Offered the alternative** briefly so the reader can decide fast.

## Day 6 — Speaking record: Pace and deliberate pausing (2-minute recording) {#day-6}
**⏱ 30 min · Sat**

### Task
Record a **2-minute** talk (plan 5 min, record 2, score 13, shadow 10). **Prompt:** "Explain the current architecture of a system you know well, and the one thing you would change." Use thought groups and spotlight pauses. Aim for 130-150 wpm.

### Structure
Overview (20 s) -> Two key components (50 s) -> Problem (25 s) -> Change and expected benefit (25 s).

### Scoring rubric (1-4)

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | hard to follow | main idea recoverable | clear, minor confusion | effortless |
| Structure | no order | partial order | clear start and end | signposted throughout |
| Fluency | frequent long pauses | noticeable hesitations | occasional | smooth, deliberate pauses |
| Grammar accuracy | errors block meaning | frequent errors | occasional | rare |
| Vocabulary range | basic, repetitive | some variety | good range | precise and varied |
| Pronunciation | unintelligible in places | needs effort | mostly clear | clear stress and rhythm |

### Shadowing task
Pick a 90-second segment of a clear, moderately paced speaker (a TED talk at ted.com, or a BBC Learning English "6 Minute English" episode). Listen once, then speak along with it sentence by sentence, matching pauses and stress. Note where you rush.

**Log your score:** date, total /24, lowest criterion, words per minute.

## Day 7 — Soft skills + weekly review: Active listening and clarifying questions {#day-7}
**⏱ 30 min · Sun**

### Scenario
In an architecture review, a senior product director, Marcus, says: "This platform needs to be faster. Customers are complaining, and I need it fixed before the peak." He is visibly frustrated. Your team has three candidate causes but no proof.

### Task
Write a 150-word response (or script the dialogue) that: (1) paraphrases what you heard, (2) asks two clarifying questions (open, specific), and (3) commits to a next step with a time.

??? success "Model response and techniques"
    > "Marcus, let me check I've understood. The customer complaints are about speed, and you need improvement before the peak season starts in November. Is that right?
    >
    > Two questions so we fix the right thing. Which customer actions feel slow: searching for rates, booking, or tracking? And do you have examples or a rough time when it happens, so we can match them to our metrics?
    >
    > Here is what I'll do: by Wednesday I'll bring you a one-page view of which of the three suspected causes the data supports, and a proposed plan for the biggest one. Would that work?"

    Techniques: **paraphrase and confirm** ("let me check I've understood... Is that right?"); **open, specific questions** (which actions, when); a **named commitment** with a date; emotion acknowledged by staying calm rather than defending.

### Weekly recap (20 items)
1. Which article: "___ CTO approved the plan"? 2. Article: "___ hour later"? 3. Correct: "We need an advice." 4. General plural nouns take which article? 5. "in production": article? 6. Define *mitigate*. 7. Difference between *assess* and *quantify*? 8. Noun form of *prioritize*? 9. What does *substantiate* require? 10. Correct: "We discussed about the risk." 11. What is BLUF? 12. What belongs in the subject line? 13. Thought group: typical length? 14. What is a spotlight pause? 15. Stress: thirteen or thirty? 16. Meaning of "ballpark figure". 17. "Touch base": register? 18. "On the same page" means? 19. Give one clarifying question stem. 20. Why paraphrase before answering?

??? success "Answers"
    1. the (unique role). 2. an. 3. "We need advice" / "a piece of advice". 4. none (zero). 5. none. 6. Reduce the severity or likelihood of harm. 7. Assess = evaluate; quantify = express as a number. 8. priority / prioritization. 9. Evidence. 10. "We discussed the risk." 11. Bottom Line Up Front. 12. The topic, the action and the deadline. 13. 4-8 words. 14. A ~1 s pause before the key point. 15. thir-TEEN has late stress; THIR-ty has first-syllable stress. 16. A rough estimate. 17. Informal business. 18. Share the same understanding. 19. "Could you give me an example of..." 20. Confirms understanding and lowers tension.

### Self-score
- [ ] I corrected 8 of 10 article errors on Day 1.
- [ ] I can use *assess, mitigate, prioritize, quantify, substantiate* in speech.
- [ ] I paused at thought-group boundaries in my recording.
- [ ] My email led with the ask.
- [ ] I paraphrased before responding in a real conversation this week.

**Error log:** write down your top 3 recurring mistakes this week (article or preposition slips, filler words, buried asks).
