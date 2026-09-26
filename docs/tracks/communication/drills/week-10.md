---
title: "Week 10 drills — Emphasis, strategy and data stories"
track: communication
week: 10
last_reviewed: 2026-09-25
---

# Week 10 — Emphasis, strategy and data stories

!!! abstract "This week"
    **Grammar:** Inversion and emphasis structures · **Vocabulary:** Strategy vocabulary: leverage, trajectory, headwinds · **Idioms & phrasal verbs:** Vision: north star, the big picture · **Speaking:** Storytelling with data · **Writing:** Writing engineering strategy · **Soft skill:** Negotiating trade-offs

## Day 1 — Grammar: Inversion and emphasis structures {#day-1}
**⏱ 30 min · Mon** Inversion (auxiliary before subject) and clefts are how you put weight on one part of a sentence. They belong in strategy documents, keynotes and high-stakes emails, and they backfire when used in every sentence.

### Rule in 60 seconds

**1. Negative and restrictive adverbials at the start of the clause trigger inversion.** Word order: adverbial + auxiliary + subject + main verb. If there is no auxiliary, add `do/does/did`.

| Trigger | Example |
|---|---|
| never, rarely, seldom | `Rarely do we see this failure mode in production.` |
| hardly / scarcely / barely ... when | `Hardly had the call started when the connection dropped.` |
| no sooner ... than | `No sooner had we deployed than the alerts fired.` |
| not only ... (but also) | `Not only was the API slow, but the database was too.` |
| not until | `Not until Friday did we learn the cause.` |
| only after / only when / only if | `Only when we saw the trace did we understand the delay.` |
| under no circumstances / at no time / in no way | `Under no circumstances should production credentials be shared.` |
| little | `Little did we know that the cache was stale.` |

**2. Conditional inversion (formal).** Drop `if` and invert: `Should you need more capacity, contact us` (= `If you should need`); `Had we known about the dependency, we would have delayed the launch` (= `If we had known`); `Were we to change the schema, all consumers would break` (= `If we were to change`).

**3. Other emphasis structures**

- `So + adjective + be + subject + that`: `So severe was the outage that we froze all releases.` `Such was the severity of the outage that...`
- **Cleft sentences** (no inversion): `What we need is a decision`, `It was the cache that failed`, `The reason we missed the date is that...`
- `Do/does/did` for emphasis: `I did tell you about the risk.`
- **Fronting** with inversion after `here/there/next`: `Here comes the hard part.`

**Rules and errors**

- Inversion happens **in the main clause**, right after the fronted phrase: `Only when we saw the trace **did we** understand` (not in the `when` clause).
- After `not only ... but also`, invert only the first clause: `Not only did the migration fail, but it also corrupted data.` Fluent-speaker error: `but also did it corrupt data`.
- `Hardly/scarcely ... when` is standard; `no sooner ... than` is standard. `Hardly ... than` is often heard but is nonstandard.
- **Do not invert** when the negative word is the subject: `Nobody expected the failure` and `Only the CTO can approve this` (subject, not adverbial).
- **Register:** inversion is formal or rhetorical. Once per page is enough; in casual Slack messages it sounds pompous.

### Exercise

Correct or transform (10).

1. Rarely we see this error in production.
2. Not only the API was slow, but the database was too.
3. No sooner had we deployed ___ the alerts fired. (than / when)
4. Hardly had the call started ___ the connection dropped. (when / than)
5. Rewrite with inversion: `If we had known about the dependency, we would have delayed the launch.`
6. Rewrite with inversion: `If you should need more capacity, contact the platform team.`
7. Under no circumstances ___ (production access should be shared / should production access be shared) with contractors.
8. Only after the audit ___ we discover the gap. (did / had)
9. Choose: `___ was the outage that we froze all releases.` (So severe / Such severe)
10. Correct: `Not only did the migration fail, but also did it corrupt data.`

??? success "Answers and explanations"
    1. `Rarely **do we see** this error in production.` Negative adverbial triggers inversion with `do`.
    2. `Not only **was the API** slow, but the database was too.` The verb `be` moves before the subject.
    3. **than**: `no sooner ... than`.
    4. **when**: `hardly/scarcely ... when`.
    5. `**Had we known** about the dependency, we would have delayed the launch.`
    6. `**Should you need** more capacity, contact the platform team.`
    7. **should production access be shared**: inversion after `under no circumstances`.
    8. **did**: `Only after the audit did we discover the gap.` (`Had` would need a past perfect: `had we discovered` is not idiomatic here.)
    9. **So severe**: `So + adjective` triggers inversion; `such` needs a noun (`Such was the severity...`).
    10. `Not only did the migration fail, **but it also corrupted** data.` No inversion in the second clause.

### Use it
Write three sentences about your work: one with `Rarely/Never do...`, one with `Had we...` and one with a cleft (`What we need is...`). Check the auxiliary comes before the subject. Then decide which sentence you would actually use in a strategy document and which you would leave out.

## Day 2 — Vocabulary: Strategy vocabulary: leverage, trajectory, headwinds {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| leverage | verb | To use something you already have to gain maximum advantage (also a noun: influence or advantage). | We can leverage the existing event bus instead of building a new messaging layer. |
| trajectory | noun | The path something is following over time, usually with an implied direction. | At the current trajectory, our cloud spend will double by next March. |
| headwind | noun | A force or condition that slows progress (plural often used; the opposite is `tailwind`). | Rising fuel costs are a headwind for every carrier we serve. |
| differentiator | noun | A feature or capability that sets you apart from competitors. | Our real-time tracking accuracy is the main differentiator in the enterprise segment. |
| foothold | noun | An initial position from which you can expand. | The pilot with one port gave us a foothold in the Asian market. |

**Note on `leverage`:** the verb is standard in strategy writing, but overused. Prefer `use` when there is no sense of multiplying advantage. Stress: LEV-er-age (US) or LEE-ver-age (UK, both heard).

### Collocations and word family

- **leverage:** leverage existing infrastructure / expertise / data / relationships; leverage X to do Y; noun: `have leverage over` (in negotiation, see Week 14). `Leveraged` also means `financed with debt`.
- **trajectory:** an upward / downward / growth / career trajectory; on a trajectory; change / alter trajectory. Plural `trajectories`.
- **headwind:** face / encounter / strong headwinds; macroeconomic headwinds; against the headwinds; opposite `tailwind` (a favorable force).
- **differentiator:** key / main / competitive differentiator; verb `differentiate from`, noun `differentiation`; adjective `distinctive`.
- **foothold:** gain / establish / secure a foothold in; adjective form none. Do not confuse with `foot in the door` (idiom, first opportunity).

### Exercise

Fill each gap (8). Review words: **rationale, materially, scrutiny**.

1. If we ______ the vendor's existing integrations, we can go live in half the time.
2. On the current ______, we will exhaust our storage budget by August.
3. The strategy must acknowledge the regulatory ______ in Europe.
4. Our low latency is not a ______: three competitors offer the same.
5. The pilot in Rotterdam gave us a ______ in the European market.
6. What is the ______ for entering the market now rather than next year?
7. The new pricing did not ______ change the revenue forecast.
8. Any strategy of this size will face intense ______ from the board.

??? success "Answers and explanations"
    1. **leverage**: use an existing asset for advantage.
    2. **trajectory**: the path of spend over time.
    3. **headwinds** (or `headwind`): a slowing external force.
    4. **differentiator**: something that sets you apart; the sentence says it does not.
    5. **foothold**: a start from which to expand.
    6. **rationale** (review, Week 7).
    7. **materially** (review, Week 9).
    8. **scrutiny** (review, Week 8).

### Use it
Write three sentences about your product or platform: one with `trajectory` (with a number or date), one with `headwinds` or `tailwinds`, one with `leverage` as a verb. Say them aloud as if in a strategy review.

## Day 3 — Speaking: Storytelling with data {#day-3}
**⏱ 30 min · Wed**

**Prompt (60-90 seconds):** Present one metric from your work as a story to a director: for example, on-time delivery rate, incident count, model accuracy or cloud cost. Tell what happened, why it matters and what should be done. No slides; imagine one chart.

**Structure: Context, Change, Cause, Consequence, Call to action (5 Cs)**

1. **Context:** `Over the last six months, our booking success rate has been our headline metric.`
2. **Change:** the surprise. `In June it dropped from 99.2 to 96.8 percent.`
3. **Cause:** `The drop traces to one carrier API that began timing out.`
4. **Consequence:** `That is roughly 1,800 failed bookings a week.`
5. **Call to action:** `I recommend we add a fallback route by the end of the quarter.`

Language: `What stands out is...`, `The story here is...`, `If you look at the trend...`, `That is a drop of...`, `Put differently...`, `So what does this mean?`

**Pronunciation micro-drill: numbers in English** Stress and clarity matter.

| Pair | Say it | Trap |
|---|---|---|
| 13 vs 30 | thir-TEEN (stress on -TEEN, ends long) vs THIR-ty (stress first) | `-teen` numbers have end stress; `-ty` numbers have first-syllable stress |
| 15 vs 50 | fif-TEEN vs FIF-ty | same pattern |
| 0.5 | "zero point five" or "point five" | say each digit after the decimal: 0.25 is "zero point two five" |
| 1.2M | "one point two million" | never "one comma two" |
| 99.95% | "ninety-nine point nine five percent" | |
| p99 | "p ninety-nine" or "p nine nine" | |
| 1,250 | "one thousand two hundred fifty" or "twelve fifty" in casual speech | US: no `and` (`one thousand two hundred and fifty` is UK/formal) |
| 2024 | "twenty twenty-four" | |

In speech, emphasize the number that carries the story: `It dropped to NINETY-six point EIGHT percent`, with a short pause before it. Say each row of the table three times, in a sentence.

**Self-check**

- [ ] I stated the change (the surprise) within the first 20 seconds.
- [ ] I gave one number for each of change, cause and consequence.
- [ ] My `-teen` and `-ty` numbers were distinguishable.
- [ ] I paused before the important number.
- [ ] I ended with a specific call to action.

## Day 4 — Idioms & phrasal verbs: Vision: north star, the big picture {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| north star | A single guiding goal or metric that aligns decisions; common in product and strategy, informal to neutral. | Our north star for this year is on-time delivery, and every project should be able to justify itself against it. |
| the big picture | The overall situation or goal, as opposed to details; neutral, common in US and UK. | Let's zoom out and look at the big picture before choosing a vendor. |
| boil the ocean | Try to do something impossibly large or attempt to fix everything at once; informal, mostly US, negative. | We do not need to boil the ocean: migrate one service first. |
| double down | Increase commitment to a strategy or bet, often after it has been challenged; informal, US origin, neutral in tone. | After the pilot succeeded, leadership doubled down on the platform approach. |
| connect the dots | See how separate facts or events relate to form a whole picture; neutral to informal. | The incident review connected the dots between three unrelated alerts. |

### Exercise

Choose or complete (8).

1. Replace `overall aim`: `Every roadmap item should serve our ______.` (north star / big picture)
2. Rewrite: `The team tries to fix all legacy problems at once.`
3. What does it mean to `double down` on a strategy? Is it always positive?
4. Choose: `Let's step back and see ______ before debating the details.` (the big picture / the north star)
5. Rewrite plainly: `No one connected the dots between the two vendors.`
6. True or false: `boil the ocean` is used for something ambitious that you encourage.
7. Choose the register: `north star` in a board paper. Is it acceptable?
8. Fix: `We need a north stars.`

??? success "Answers and explanations"
    1. **north star**: a specific guiding goal.
    2. `The team is trying to **boil the ocean**.`
    3. To increase commitment to a choice, often when it is under doubt. **Not always positive**: it can be praised as conviction or criticized as stubbornness (sunk cost).
    4. **the big picture**: the overall situation.
    5. `No one noticed how the two vendor issues were related.`
    6. **False**: it is a warning against attempting too much.
    7. **Acceptable** in many strategy papers, but some boards see it as jargon; consider `guiding goal` for formal or non-native audiences.
    8. `We need **a north star**.` Singular; pick one metric.

!!! warning "When NOT to use them"
    `North star` is jargon-heavy in mixed-culture audiences and is often misused for a list of goals (a north star is one). `Double down` can suggest recklessness in risk-averse organizations. `Boil the ocean` criticizes an idea; do not aim it at a person's proposal in a public forum. In contracts and official reports, use the plain equivalent.

## Day 5 — Writing: Writing engineering strategy {#day-5}
**⏱ 30 min · Fri**

**Bad draft:**

> Our engineering strategy is to become best in class by leveraging AI everywhere and moving fast while maintaining quality. We will double down on innovation, break down silos, and deliver value to customers. All teams should adopt the strategy and prioritize accordingly.

**Task:** Rewrite as a 130-170 word engineering strategy in the **diagnosis, guiding policy, coherent actions** structure (from Richard Rumelt's *Good Strategy, Bad Strategy*). Include a real challenge (invented), one clear choice and a trade-off you accept, and three actions with owners or dates. Use at least one of `trajectory`, `headwinds`, `leverage`.

??? success "Model answer and what changed"
    > **Diagnosis.** Our deployment lead time is 11 days, against 2 days at our closest competitor. On the current trajectory, we cannot ship the compliance features customers have requested before the next renewal cycle. The main cause is not developer speed but a manual, three-team release approval.
    >
    > **Guiding policy.** We will make deployment a self-service platform capability. We will leverage the existing CI system rather than buy a new one, and we accept that the platform team will pause new-feature work for two quarters.
    >
    > **Actions.** (1) By 31 October, the platform team automates the approval checks currently done by hand. (2) By 15 December, two pilot teams deploy without a ticket. (3) By Q1 review, security signs off on the automated gates. Progress is measured by lead time, targeting 3 days.

    - **Diagnosis before solution:** it names the actual problem with a number instead of aspirations.
    - **One guiding policy with a stated trade-off:** the original had none (`everything, faster and better`); a strategy chooses and gives something up.
    - **Coherent actions with dates and owners:** the original told everyone to `prioritize accordingly`.
    - **Buzzwords removed:** `best in class`, `break down silos`, `deliver value`. `Leverage` survives because it has a concrete object.
    - **A measure of success** (lead time) closes the loop.

## Day 6 — Speaking record: Storytelling with data {#day-6}
**⏱ 30 min · Sat**

**Record a 2-minute talk:** Tell the story of one metric from your work using the 5 Cs (Context, Change, Cause, Consequence, Call to action). Include at least three numbers, one inversion structure (`Rarely...`, `Not only...`, `Had we...`), and one of `trajectory`, `headwinds`, `foothold`. Keep the tone that of a director briefing.

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Numbers unclear or missing | Story hard to follow | Story clear, one number unexplained | Every number serves the story |
| Structure | No arc | Arc partial | Context, change, cause, consequence present | All five Cs with a clear call to action |
| Fluency | Frequent stops | Long pauses before numbers | Mostly smooth | Deliberate pauses for emphasis |
| Grammar accuracy | Errors block meaning | Frequent errors | Few errors; inversion attempted | Inversion correct and natural |
| Vocabulary range | Repetitive | Basic terms | Strategy words used correctly | Precise, varied, not jargon-heavy |
| Pronunciation | Numbers ambiguous | `-teen`/`-ty` often confused | Mostly clear | Numbers, stress and rhythm clear |

**Shadowing task:** Choose a data-driven talk (for example, a TED talk by a data visualization speaker, or a conference talk on a production metric or incident). Shadow the section where the speaker moves from data to insight. Note how they pause before key numbers. Three passes, one minute each.

**Log your score:** total out of 24 in `docs/log/`, plus note whether your numbers were clear on playback.

## Day 7 — Soft skills + weekly review: Negotiating trade-offs {#day-7}
**⏱ 30 min · Sun**

**Scenario.** The VP of Product, Clara, wants a new self-service tracking feature live by the end of Q3. Your team estimates it can deliver a complete, reliable version by mid-Q4, or an end-of-Q3 version with no retry handling and manual monitoring. Clara says: "I need it in Q3. Just make it work." You have a good relationship but different incentives.

**Task:** Script your 150-word response.

??? success "Model response and techniques"
    > I want to hit Q3 too, so let me lay out what is possible. The constraint is that we cannot have all three: the full scope, high reliability and end of Q3. Option A: the full version in mid-Q4, with retries and monitoring. Option B: a Q3 launch to a limited group of ten customers, with the core tracking working but manual monitoring by my team, and the full rollout in Q4. Option C: a Q3 launch to everyone, with a higher chance of failed updates, which I do not recommend. What matters most to you: the date, the scope, or the customer experience? If it is the date, I recommend Option B. It gives you a Q3 announcement without exposing all customers to the unreliable parts. I need your decision by Friday to stay on that path.

    **Techniques used**

    - **Shared goal first** (`I want to hit Q3 too`).
    - **Make the trade-off visible:** the triangle of scope, reliability and date; three concrete options.
    - **Offer a recommendation** with a reason, not just a menu.
    - **Ask for her priority** (`What matters most to you`) to convert `make it work` into a real decision.
    - **Preserve her win** (a Q3 announcement) while protecting the customer.
    - **Close with a decision deadline.**

### Weekly recap (20 items)

1. Which auxiliary appears in `Rarely ___ we see this error`?
2. Complete: `No sooner had we deployed ___ the alerts fired.`
3. Complete: `Hardly had the call started ___ it dropped.`
4. Rewrite `If we had known` as inversion.
5. Rewrite `If you should need` as inversion.
6. Correct: `Not only did it fail, but also did it corrupt data.`
7. Which is correct: `So severe was the outage` or `Such severe was the outage`?
8. Inversion or not: `Only the CTO can approve this.`
9. What is a cleft sentence? Give one example.
10. Define `leverage` (verb).
11. Meaning of `trajectory`.
12. Opposite of `headwind`.
13. What is a `differentiator`?
14. `Foothold` meaning.
15. What does a north star do?
16. `boil the ocean` meaning and tone.
17. `double down` meaning; when is it risky?
18. Say: 13, 30, 15, 50 and mark the stress.
19. What are the three parts of a Rumelt strategy?
20. Which three options structure the trade-off response?

??? success "Answers and explanations"
    1. `do`.
    2. than.
    3. when.
    4. `Had we known`.
    5. `Should you need`.
    6. `Not only did it fail, but it also corrupted data.`
    7. `So severe was the outage`.
    8. No inversion; `only the CTO` is the subject.
    9. A sentence that puts focus on one element, e.g. `What we need is a decision` or `It was the cache that failed.`
    10. Use an existing asset to gain maximum advantage.
    11. The path over time, with a direction.
    12. tailwind.
    13. A feature or capability that sets you apart from competitors.
    14. An initial position from which to expand.
    15. Aligns decisions through one guiding goal or metric.
    16. Try to do something impossibly large; negative and informal.
    17. Increase commitment to a bet; risky when facts have changed (sunk cost).
    18. thir-TEEN, THIR-ty, fif-TEEN, FIF-ty.
    19. Diagnosis, guiding policy, coherent actions.
    20. A full version later, a limited earlier launch, a full early launch with high risk; plus asking for her priority.

**Self-score**

- [ ] I can use never/rarely/not only/only when inversions correctly.
- [ ] I used leverage, trajectory, headwind, differentiator, foothold in context.
- [ ] I told a data story with the 5 Cs and clear numbers.
- [ ] I wrote a strategy with a diagnosis and a trade-off.
- [ ] I can present trade-off options and ask for a decision.

**Error log:** write down your top 3 recurring mistakes this week (for example, wrong `than/when`, inversion in the wrong clause, `-teen`/`-ty` confusion) and one correct model sentence for each.
