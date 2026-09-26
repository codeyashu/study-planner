---
title: "Week 15 drills — data storytelling and precise comparisons"
track: communication
week: 15
last_reviewed: 2026-09-25
---

# Week 15 — Data storytelling and precise comparisons

!!! abstract "This week"
    **Grammar:** comparatives, quantifiers and precise comparisons · **Vocabulary:** data storytelling (anomaly, granular, attest, outlier, cohort) · **Idioms & phrasal verbs:** tip of the iceberg, moving target, cherry-pick, drill down, move the goalposts · **Speaking:** narrating a demo · **Writing:** tech-debt proposal · **Soft skill:** difficult conversations

    Theme: numbers persuade only when the comparison is exact. "Much faster" and "200 percent more" are where senior engineers lose credibility.

## Day 1 — Grammar: comparatives, quantifiers and precise comparisons {#day-1}
**⏱ 30 min · Mon**

### Rule in 60 seconds

- **Form:** one syllable and many two-syllable words take `-er` (faster, larger); longer adjectives take `more` (more reliable, more resilient). `Two-syllable words ending in -y` change to `-ier` (easier, noisier).
- **Modifying a comparative:** use `much, far, considerably, slightly, a bit, significantly`. Never `very`: "very faster" is an error; say "much faster".
- **Double comparatives:** "the + comparative, the + comparative": "The more data we collect, the more accurate the model becomes."
- **Equal and multiple comparisons:** `as ... as`, and `twice / three times as fast as`. "Three times faster than" is widely used but ambiguous to some readers; `three times as fast as` is unambiguous and preferred in specifications.
- **Percentages:** "increased by 200 percent" means it tripled (100 to 300). "Increased to 200 percent of the baseline" means it doubled. State the baseline and the result to be safe.
- **Fewer vs less:** `fewer` with countable plurals (fewer incidents), `less` with uncountable nouns (less latency, less downtime). Exception: measurements and sums are treated as a single amount ("less than 5 minutes", "less than $100").
- **A few / few, a little / little:** `a few` is positive (some, enough); `few` is negative (hardly any). Same for `a little` vs `little`.
- **Number agreement:** `A number of` + plural verb ("A number of teams have"); `The number of` + singular verb ("The number of failures has"). `The amount of` goes with uncountable nouns.
- **Two things vs three or more:** comparative for two ("the faster of the two"), superlative for three or more ("the fastest of the three").
- **Illogical comparison (the fluent-speaker error):** compare like with like. "Latency here is lower than the old region" compares latency with a region. Say "lower than in the old region" or "lower than that of the old region."

### Exercise

1. Correct: "The new index is very faster than the old one."
2. Fill in fewer or less: "We had ______ incidents this quarter and ______ downtime."
3. Correct the illogical comparison: "Latency in the new region is lower than the old region."
4. Choose: "The number of failed jobs (has / have) doubled since March."
5. Choose: "A number of customers (has / have) reported delays."
6. Transform: "Version B takes 2 minutes; version A takes 6." Use `times as ... as`.
7. Correct: "The more data we collect, the model is more accurate."
8. Choose and explain the meaning: "We have (few / a few) engineers with Rust experience, so hiring is a real risk."
9. Correct: "Of the two designs, B is the most resilient."
10. Baseline throughput was 100 requests per second; it is now 300. Write two accurate sentences, one with "by ... percent" and one with "times".

??? success "Answers and explanations"
    1. **much (or far) faster.** `Very` cannot modify a comparative.
    2. **fewer incidents, less downtime.** Incidents are countable; downtime is uncountable.
    3. **"...lower than in the old region"** or "than that of the old region." The comparison must be between the same kinds of thing.
    4. **has.** `The number of` takes a singular verb.
    5. **have.** `A number of` means "several" and takes a plural verb.
    6. **"Version B is three times as fast as version A"** (or "A takes three times as long as B").
    7. **"The more data we collect, the more accurate the model is/becomes."** Both halves need a comparative; the second clause uses subject-verb order after the comparative phrase.
    8. **few.** `Few` means hardly any, so hiring is a risk; `a few` would mean there are some, contradicting "risk".
    9. **more resilient.** Two items require the comparative.
    10. "Throughput increased by 200 percent" and "Throughput is three times what it was" (or "tripled"). An increase of 200 percent means the increase is twice the original; the result is three times the original.

### Use it
Write three comparison sentences about a system you own, each with a baseline and a result: one using `times as ... as`, one using `fewer`, and one using `the more ..., the ...`. Check that each compares like with like.

## Day 2 — Vocabulary: data storytelling vocabulary (anomaly, granular, attest, outlier, cohort) {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| anomaly | noun | Something that deviates from what is normal or expected | "The dashboard flagged an anomaly in container dwell time at the Rotterdam terminal." |
| granular | adjective | Detailed; broken down to small units | "We need more granular data than monthly averages to see which routes are failing." |
| attest (to) | verb | To provide clear evidence that something is true, or to state formally that it is (used as `attest to something` or `attest that`) | "The logs attest to the customer's account that the events arrived out of order." |
| outlier | noun | A data point far from the others in a set | "Two outliers skewed the mean; the median tells the real story." |
| cohort | noun | A group sharing a characteristic, analyzed over time | "The cohort of customers onboarded after the redesign has a 15 percent lower churn rate." |

### Collocations and word family

- **anomaly:** detect / flag / investigate / explain an anomaly; a statistical anomaly; anomaly detection. Adjective: **anomalous**. Plural: anomalies.
- **granular:** granular data / control / permissions; more / finer granularity (noun). Not the same as "detailed report": granular describes level of breakdown.
- **attest:** attest to a fact / claim / account; attest that + clause; noun **attestation** (formal, often legal). Do not confuse with the near-synonym `corroborate` (confirm with a second, independent source).
- **outlier:** remove / exclude / investigate an outlier; statistical outlier. Verb phrase: "lie outside the interquartile range".
- **cohort:** a cohort of users; cohort analysis; a cohort of graduates. Do not confuse with "colleague".
- Pronunciation: a-NOM-a-ly, GRAN-yoo-lar, co-ROB-o-rate, OUT-ly-er, CO-hort.

### Exercise
Cloze. Word bank (each once): anomaly, granular, attest, outlier, cohort, trajectory, headwinds, materially.

1. The first ______ of users who adopted the new API shows twice the retention of the control group.
2. One ______ (a 45-second request) inflated the average; the 95th percentile was unaffected.
3. The spike in error rates was an ______ that nobody had predicted.
4. Can you ______ that number with the finance team's export before we present it?
5. We need to break this down at a more ______ level: per route, not per region.
6. The cost curve's ______ is downward, but rising energy prices are ______ we can't ignore.
7. The change did not ______ affect throughput; the difference is within noise.
8. Which word means "a data point far from the rest"?

??? success "Answers and explanations"
    1. **cohort**: a group tracked over time.
    2. **outlier**: a single extreme value.
    3. **anomaly**: a deviation from expected behavior.
    4. **attest**: provide clear evidence for a claim.
    5. **granular**: fine-level breakdown.
    6. **trajectory / headwinds** (week 10 review words). "Trajectory" is the direction; "headwinds" are external forces working against you.
    7. **materially** (week 9 review word): to a significant degree.
    8. **outlier.**

### Use it
Explain one real metric aloud in three sentences using `anomaly`, `granular` and `attest`. Example: "This anomaly only appears at a granular level; the aggregate hides it. The raw event log attests to it."

## Day 3 — Speaking: narrating a demo {#day-3}
**⏱ 30 min · Wed**

**Prompt (60-90 seconds).** Screen-share a dashboard or tool of your choice (or imagine one) and narrate a 90-second demo to a non-technical director: a new shipment-delay prediction view. Do not read from a script; use the structure below.

**Structure: S-S-M-N (Set the scene, Show, Meaning, Next)**

1. **Set the scene:** "What you're about to see is how we predict late shipments 48 hours ahead."
2. **Show** with signposts: "First, you'll see... Now I'll filter by... Notice that..."
3. **Meaning:** "What this tells us is that 70 percent of the delays start at two ports."
4. **Next:** "The next step is to route around those ports; I'll show that on Thursday."

Signposting phrases: "Let me draw your attention to...", "If you look at the top right...", "As you can see...", "Let me zoom in on...". While the screen changes, narrate what the audience should notice; never leave silence over a loading screen ("While that loads, the key point is...").

**Pronunciation micro-drill: sentence stress and numbers**

Stress content words, weaken function words: "The FIRST thing to NOtice is the SPIKE at NINE." Practice these pairs where numbers are often misheard (stress on the second syllable for -teen, first for -ty):

| -teen | -ty |
|---|---|
| thir-TEEN | THIR-ty |
| four-TEEN | FOR-ty |
| fif-TEEN | FIF-ty |
| six-TEEN | SIX-ty |

Say: "Fifteen ports, fifty vessels; thirteen delays, thirty cancellations." Stress the number and pause slightly before it.

**Self-check**
- [ ] I used at least three signposts ("First...", "Notice that...", "What this means...").
- [ ] I said what the audience should conclude, not only what is on screen.
- [ ] Numbers (teen/ty) were clearly distinguishable.
- [ ] I covered any "dead air" with a bridging sentence.
- [ ] I ended with a next step.

## Day 4 — Idioms & phrasal verbs: data idioms {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| the tip of the iceberg | A small visible part of a much larger problem. Common in all registers. | "Those 12 failed deployments are just the tip of the iceberg; the audit found 200 silent retries." |
| a moving target | Something whose requirements or position keep changing, making it hard to hit. Neutral. | "The compliance requirements are a moving target, so we can't fix the scope." |
| cherry-pick | To select only the data or examples that support your argument (negative when about evidence). Informal; neutral when about choosing commits ("cherry-pick a commit"). | "Don't cherry-pick the best quarter; show the full year." |
| drill down (into) | To examine data in progressively more detail. Phrasal verb; neutral, very common in analytics. | "Let's drill down into the latency numbers by endpoint." |
| move the goalposts | To change the criteria for success after the work is done, unfairly. Informal; accusatory when said of others, so use carefully. | "Every time we hit the target, they move the goalposts." |

### Exercise (8 items)

1. Choose the best expression: "Requirements keep changing, so the design is aiming at ______." (a moving target / the tip of the iceberg)
2. Choose: "We found one corrupt record, but I suspect it's ______." 
3. Fill in: "Instead of showing all regions, he ______ the two best ones."
4. Fill in: "Can you ______ into the data by customer segment?"
5. Which expression would be inappropriate to say directly to your VP in a review, and why? (move the goalposts / drill down)
6. Rewrite more idiomatically: "This visible issue is only a small part of a much bigger problem."
7. Rewrite more diplomatically: "You keep moving the goalposts."
8. Is "cherry-pick a commit" positive, negative or neutral?

??? success "Answers and explanations"
    1. **a moving target**: requirements changing.
    2. **the tip of the iceberg**: a small visible part of a larger issue.
    3. **cherry-picked** (past form).
    4. **drill down** (phrasal verb, "into" follows).
    5. **move the goalposts**: it accuses the VP of acting unfairly. Say instead: "Help me understand how the success criteria have changed."
    6. "This is the tip of the iceberg."
    7. "It feels like the success criteria have changed since we agreed the plan; can we align on them again?"
    8. **Neutral**: in Git contexts it is a technical term; only negative for evidence selection.

**When NOT to use them:** avoid *cherry-pick* and *move the goalposts* as accusations in escalations; they trigger defensiveness. *Tip of the iceberg* can sound dramatic in status reports; reserve it for genuine surprises, and back it up with a number.

## Day 5 — Writing: tech-debt proposal {#day-5}
**⏱ 30 min · Fri**

**Bad draft**:

> Team, our codebase has a lot of tech debt and it is getting worse. Lots of bugs come from the old parts and engineers hate working there. We should really do something about it soon or it might become a big problem. I suggest we stop feature work for a while and clean everything up. Thanks.

**Task.** Rewrite it as a 150-200 word proposal to a product director, who cares about delivery dates. Constraints: quantify the cost of the debt (invent numbers), scope it to one component, propose a time-boxed approach that keeps 70 percent of capacity on features, name the outcome measurably, and use at least two comparisons with baselines (for example "40 percent fewer", "twice as fast").

??? success "Model answer"
    **Subject: Proposal: 6-week time-boxed refactor of the rating engine (30 percent capacity)**

    The rating engine is our largest source of delivery drag, and I propose a six-week refactor that uses 30 percent of team capacity while features continue at 70 percent.

    **Cost today.** The rating engine caused 41 percent of production defects last quarter and takes three times as long to modify as our other services (median 9 days per change against 3). Two of the last three delayed features were blocked here.

    **Scope.** One component only: extract the tariff calculation module and add contract tests. We will not touch the booking flow.

    **Expected outcome.** Median change time down from 9 days to 4 or fewer; defects from this component down at least 40 percent by the end of the following quarter. We will report both metrics in the monthly review.

    **Trade-off.** Feature throughput drops roughly 30 percent for six weeks, so the Q4 partner integration could slip by one sprint. I would rather agree that trade-off now than face an unplanned slip in November.

    **Decision requested:** approval of the six-week window from 3 November.

    What changed and why:
    - The debt is quantified with baselines (41 percent, three times as long), so the director can compare cost against benefit.
    - Scope is narrowed to one component; "clean everything up" is unfundable.
    - The proposal keeps feature capacity at 70 percent, addressing the director's actual concern.
    - Outcomes are measurable and dated; "engineers hate working there" is replaced by change-time and defect metrics.
    - The trade-off is stated openly, which builds trust.

## Day 6 — Speaking record: explaining a trend from data {#day-6}
**⏱ 30 min · Sat**

**Record a 2-minute talk.** You have a chart in front of you (real or imagined): weekly incident counts fell from 22 to 9 over two quarters, but the number of severity-1 incidents stayed flat at 3. Explain to your director what happened, what you believe the cause is, how confident you are, and what you recommend.

**Structure:** headline (the trend in one sentence, 15 s) - the comparison with baseline (25 s) - the anomaly or outlier that complicates the story (25 s) - your interpretation with calibrated certainty (25 s) - what would attest to it (15 s) - recommendation (15 s).

**Scoring rubric** (1 to 4)

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Message unclear | Point emerges late | Clear main point | Point is unmistakable and memorable |
| Structure | No visible order | Some order, jumps | Clear sequence | Signposted and easy to follow |
| Fluency | Frequent stops/fillers | Occasional long pauses | Mostly smooth | Smooth with deliberate pauses |
| Grammar accuracy | Errors block meaning | Frequent errors | Few errors, no confusion | Comparisons and quantifiers precise |
| Vocabulary range | Repeats basic words | Some C1 words | Good range, some data terms | Precise, varied, natural |
| Pronunciation | Hard to follow | Stress errors distract | Generally clear | Numbers and stress clear |

**Shadowing task.** Shadow two minutes of a Hans Rosling TED talk (he narrates charts with excellent pacing and signposting), or a BBC 6 Minute English episode about statistics or data. Copy his pauses before the key number.

**Log your score:** total out of 24 and your weakest criterion; note whether your comparisons were precise (baseline and result).

## Day 7 — Soft skills + weekly review: difficult conversations {#day-7}
**⏱ 30 min · Sun**

**Scenario.** A strong senior engineer on your team, Priya, has repeatedly merged large changes without review in the last month, saying that reviews slow her down. Two incidents traced back to these merges. She is respected and defensive when challenged. You have a one-to-one tomorrow.

**Task.** Write a 150-word script of how you open and run the first two minutes of the conversation. Include: intent, facts, an open question, and listening.

??? success "Model response"
    "Priya, thanks for making time. I want to talk about something that matters to both of us: how we keep the quality of the main branch high while keeping you fast. I'm raising it because I value your work, and I'd like to solve this together.

    Here's what I've seen. In the last month, five of your merges went in without review, and two of them were connected to the incidents on the 3rd and 17th. I'm not assuming intent; I'd like to understand what's happening from your side. What's making reviews hard to work with right now?

    [Listen; do not interrupt.] So the review queue is taking two days, and that blocks you. That's a real problem, and I can help fix it. What I need is a review on every change to the payments module; can we agree on a same-day review target and try it for two weeks?"

    **Techniques used:** (1) Intent first: signals shared goal, reduces defensiveness. (2) Facts, not labels: numbers and dates, not "you're careless". (3) Explicit statement of no assumed intent. (4) Open question inviting her view. (5) Reflective listening ("So the review queue is taking two days"). (6) A specific request and a time-boxed experiment. (7) Offers help on the underlying cause.

### Weekly recap (20 items)

1. Correct: "very faster".
2. Fewer or less: "___ bugs", "___ latency".
3. "The number of errors" takes has or have?
4. "A number of errors" takes has or have?
5. Convert: "Increased by 200 percent" equals how many times the original?
6. "Twice as fast as" versus "twice faster than": which is unambiguous?
7. What is the difference between "few" and "a few"?
8. Fix: "Throughput is higher than the old cluster."
9. Define **anomaly**.
10. Which word means to provide clear evidence that something is true?
11. What is an **outlier**?
12. Meaning of **granular**?
13. What is a **cohort**?
14. Where is the stress in **attest**?
15. "Tip of the iceberg" means...?
16. What does **cherry-pick** imply about evidence?
17. What does **drill down** mean?
18. Why is "move the goalposts" risky to say directly?
19. In S-S-M-N, what does M stand for?
20. Which week 10 word means external forces against progress?

??? success "Answers"
    1. "much faster". 2. fewer bugs, less latency. 3. has. 4. have. 5. Three times. 6. "Twice as fast as". 7. Few = hardly any (negative); a few = some (positive). 8. "...higher than on the old cluster / than the old cluster's." 9. A deviation from what is expected. 10. attest. 11. A data point far from the others. 12. Detailed, at a fine level. 13. A group sharing a trait, tracked over time. 14. a-TEST. 15. A small visible part of a bigger problem. 16. Choosing only supporting data, unfairly. 17. Examine in more detail. 18. It accuses the other party of acting unfairly. 19. Meaning (what it tells us). 20. headwinds.

**Self-score (tick what you can do without notes)**
- [ ] I compare like with like and give baseline plus result.
- [ ] I use fewer/less, a few/few and number agreement correctly.
- [ ] I used at least three of the five new words in speech or writing.
- [ ] I can narrate a demo with signposts and a meaning statement.
- [ ] I can open a difficult conversation with intent, facts and a question.

**Error log.** Write down your top 3 recurring mistakes from this week. Review before Week 16, which is a checkpoint week: your error log is the input for Monday's grammar review.
