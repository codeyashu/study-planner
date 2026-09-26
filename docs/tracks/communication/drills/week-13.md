---
title: "Week 13 drills — Strong verbs, executive language and briefings"
track: communication
week: 13
last_reviewed: 2026-09-25
---

# Week 13 — Strong verbs, executive language and briefings

!!! abstract "This week"
    **Grammar:** Nominalisation vs strong verbs (clear writing) · **Vocabulary:** Executive vocabulary: mandate, remit, accountable · **Idioms & phrasal verbs:** Money talk: bottom line, cost a fortune, break even · **Speaking:** The 3-minute executive briefing · **Writing:** Executive updates · **Soft skill:** Stakeholder mapping and framing

## Day 1 — Grammar: Nominalisation vs strong verbs (clear writing) {#day-1}
**⏱ 30 min · Mon** A nominalization turns a verb or adjective into a noun: `decide` becomes `decision`, `implement` becomes `implementation`, `fail` becomes `failure`, `available` becomes `availability`. Engineers write with heavy nominalization because it sounds serious. Readers pay for it.

### Rule in 60 seconds

**The pattern to fix:** a weak verb (`make, take, have, give, conduct, perform, carry out, undertake, provide, is/are`) plus an abstract noun that hides the real action.

| Weak | Strong |
|---|---|
| conduct an evaluation of the vendors | evaluate the vendors |
| make a decision to postpone | decide to postpone |
| is in agreement | agree |
| perform an analysis of the logs | analyze the logs |
| the implementation of the migration of the service | we migrated the service |
| give consideration to | consider |

**Why it matters:** strong verbs make the doer and the action visible, shorten the sentence, and speed comprehension. Helen Sword calls the heavy abstract nouns `zombie nouns` (*Stylish Academic Writing*, and later essays): they take over a sentence and drain its life. Typical zombie nouns end in `-tion, -ment, -ance, -ity, -ness`.

**Fix method:** (1) find the abstract noun, (2) ask `who does what?`, (3) make the doer the subject and the action the verb, (4) delete the light verb and stacked `of` phrases.

**When nominalization is correct, not a flaw**

1. **Cohesion:** a noun can summarize the previous sentence and start the next: `Latency doubled after the release. This increase triggered the alert.`
2. **Naming things:** `the migration`, `a review`, `a request`, `an outage`, `a decision log` are the natural terms.
3. **Formal or hedged register:** `There is a possibility of failure` can be intentionally cautious (compare Week 4), and `approval is required` suits policy.
4. **Unknown or irrelevant agent:** `Approval of the budget is pending.`
5. **Conciseness:** `The cache's failure to invalidate` may still be shorter than a clause when the subject is long.

**Errors fluent speakers make**

- **Stacked `of` phrases:** `the implementation of the migration of the billing service` (three nouns, no one acting).
- **`Utilization`, `facilitate`, `leverage` for `use`, `help`:** `utilize` is only better than `use` in rare technical cases.
- **`is in agreement/ is in a position to` and `there is / it is` fillers:** `There is a need for us to...` becomes `We need to...`.
- **Choosing a verb that is stronger but wrong in register:** `We nixed the plan` for `We cancelled the plan` in a formal report.

### Exercise

Rewrite each sentence with strong verbs, or explain (10).

1. We conducted an evaluation of three vendors.
2. The team made a decision to postpone the release.
3. There was a failure of the cache to invalidate stale entries.
4. The implementation of the migration of the billing service was completed by the team.
5. Our recommendation is for the adoption of a feature-flag system.
6. The reduction of latency was achieved by the introduction of caching.
7. Explain why `This increase` is good here: `Latency doubled after the release. This increase triggered the alert.`
8. Management's approval of the budget is required.
9. The team is in agreement that the plan is viable.
10. The utilization of automation facilitates the optimization of deployment.

??? success "Answers and explanations"
    1. `We **evaluated** three vendors.`
    2. `The team **decided** to postpone the release.`
    3. `The cache **failed** to invalidate stale entries.`
    4. `The team **migrated** the billing service.` (Three stacked nouns collapse to one verb.)
    5. `We **recommend adopting** a feature-flag system.`
    6. `**Caching reduced** latency.` (Or `We reduced latency by introducing caching`.)
    7. `This increase` is a **deliberate nominalization** that summarizes the previous sentence and starts the next (cohesion). The alternative, `Latency doubled after the release. The fact that it doubled triggered the alert`, is longer and clumsier.
    8. `Management **must approve** the budget.` Or keep the original if the agent is irrelevant and the rule is formal (`Approval is required`); the rewrite is preferable when accountability matters.
    9. `The team **agrees** that the plan is viable.`
    10. `**Automation speeds up** deployment.` or `We use automation to deploy faster.` (Zombie nouns: utilization, facilitates, optimization.)

### Use it
Take one paragraph from your last design doc or email, circle every `-tion/-ment/-ity` word and every `make/conduct/perform/provide`, and rewrite three sentences with strong verbs. Say the before and after aloud; the second should be easier to say in one breath.

## Day 2 — Vocabulary: Executive vocabulary: mandate, remit, accountable {#day-2}
**⏱ 30 min · Tue**

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| mandate | noun / verb | Noun: official authority or instruction to act. Verb: to require officially (stress: MAN-date). | The steering group gave the platform team a clear mandate to consolidate the three ticketing tools. |
| remit | noun | The area of responsibility given to a person or group (mostly UK; stress REE-mit as a noun); as a verb it means `send money`. | Vendor selection is outside the remit of the architecture board. |
| accountable | adjective | Required to explain or justify actions, and to accept the consequences; different from `responsible`. | One named director is accountable for the outcome, even though three teams do the work. |
| purview | noun | The range or scope of authority or concern; formal. | Data retention falls within the purview of the compliance office. |
| stewardship | noun | Careful, responsible management of something entrusted to you, such as data or budget. | Good stewardship of the cloud budget means reviewing idle resources every quarter. |

**Responsible vs accountable (RACI):** the *responsible* person does the work; the *accountable* person answers for the result, and there is one accountable person per item.

### Collocations and word family

- **mandate:** a clear / strong / executive mandate; give / receive a mandate; mandate a change; adjective `mandatory` (required), noun `mandate` in politics (an election win).
- **remit:** within / outside / beyond the remit; narrow / broad remit; `fall within the remit`; US usage often prefers `scope` or `charter`.
- **accountable:** be held accountable; accountable to (a person) for (an outcome); noun `accountability`; verb: `hold to account`. Not `accountable` for a person's salary; `accounting` is a different word.
- **purview:** within / outside / beyond the purview of; formal, mostly written.
- **stewardship:** data / financial / environmental stewardship; noun `steward`, verb `steward` (to manage carefully).

### Exercise

Fill each gap (8). Review words: **contingent, reiterate, trajectory**.

1. The CEO gave the platform team a ______ to cut cloud costs by 20 percent.
2. Security policy is outside the ______ of the delivery team.
3. Who is ______ if the migration misses the regulatory deadline? One name, please.
4. Approving new vendors falls within the ______ of procurement.
5. Responsible use of customer data is part of our data ______.
6. The budget is ______ on board approval.
7. I want to ______ that accountability sits with the sponsor, not the team.
8. On this ______, we will reach our cost target by Q3.

??? success "Answers and explanations"
    1. **mandate**: an official authority to act.
    2. **remit** (or `purview`): the area of responsibility.
    3. **accountable**: the one answerable for the result.
    4. **purview** (or `remit`): the scope of authority.
    5. **stewardship**: careful management of something entrusted.
    6. **contingent** (Week 12).
    7. **reiterate** (Week 11).
    8. **trajectory** (Week 10).

### Use it
Write three sentences about your organization: who has the mandate for something, what is outside your team's remit, and who is accountable for one project outcome. Say them aloud as a two-sentence introduction to a new stakeholder.

## Day 3 — Speaking: The 3-minute executive briefing {#day-3}
**⏱ 30 min · Wed**

**Prompt (3 minutes, practice today, record on Saturday):** Brief a VP who has 3 minutes between meetings on the status of your most important project. Assume they will interrupt.

**Structure: Bottom line, Why, Risk, Ask (BWRA)**

1. **Bottom line (20 s):** `Bottom line: we are on track for 14 March, at 2 percent over budget.`
2. **Why (90 s):** three short points with one number each: progress, milestones, evidence.
3. **Risk (40 s):** the single most important risk, the probability, the impact and the mitigation.
4. **Ask (30 s):** the decision or support needed, with a date. `I need your approval on the extra vendor budget by Friday.`
5. **Buffer (20 s):** leave space for interruptions; if they interrupt, answer briefly and return to your structure (`Let me finish this point, and then come back to that`).

Phrases: `Bottom line...`, `In short...`, `The main thing to know is...`, `The one risk I want to flag is...`, `What I need from you is...`, `I can go deeper on any of these.`

**Pronunciation micro-drill: compound-noun stress.** English compound nouns are stressed on the first element; adjective plus noun is stressed on the second.

| Compound (first stress) | Adjective + noun (second stress) |
|---|---|
| BLACKboard | a black BOARD |
| GREENhouse | a green HOUSE |
| BOTtom line | a bottom LINE (the line at the bottom of a page) |
| ROADmap | a rough MAP |
| DEADline | a dead LINE (a phone with no signal) |

Note: apply the rule to business compounds: `BOTtom line`, `ROADmap`, `DEADline`, `DEcision log`, `RISK register`, `SERvice desk`. Longer noun phrases vary; when in doubt, stress the word carrying the new information. Say each business compound three times, then in a sentence: `The BOTtom line is on the ROADmap.`

**Self-check**

- [ ] I stated the bottom line in the first 20 seconds.
- [ ] I gave exactly one risk and one ask, each with a number or date.
- [ ] I spoke in short, strong-verb sentences.
- [ ] I finished in 3 minutes or less, with a short buffer.
- [ ] I stressed compound nouns on the first element.

## Day 4 — Idioms & phrasal verbs: Money talk: bottom line, cost a fortune, break even {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| bottom line | The final result or the most important point; from the last line of a financial statement. Neutral, common in US and UK. | The bottom line is that this migration saves 1.4 million dollars a year. |
| cost a fortune | To be very expensive; informal (also `cost an arm and a leg`, informal, mostly US). | Running two data centers in parallel will cost a fortune. |
| break even | Reach the point where revenue equals costs, with no profit or loss; neutral, financial. | At current volumes, the new service will break even in month 14. |
| in the red | Losing money or overdrawn; informal, from accounting practice of writing losses in red; opposite `in the black`. | The division has been in the red for three quarters. |
| write off | Treat as a loss or accept that something has no value; accounting and general use; noun `write-off`. Neutral to informal. | Finance will write off the unused licenses this quarter. |

**Grammar note:** `break even` is intransitive (`we broke even`), and the noun is `break-even point`. `Write off` is separable: `write the debt off` / `write off the debt`.

### Exercise

Choose or complete (8).

1. Rewrite plainly: `Duplicate licenses cost us a fortune.`
2. The new product must ______ within 18 months. (break even / write off)
3. `The bottom line is that we are over budget.` Does `bottom line` here mean the details or the conclusion?
4. What is the opposite of `in the red`?
5. Fix: `We wrote off it last quarter.`
6. Choose the more formal expression for a board report: `it costs a fortune` or `it is very expensive`.
7. `The team's rewrite was a ______: we never used it.` (write-off / break-even)
8. Rewrite with `bottom line`: `The most important point is that we need a second region.`

??? success "Answers and explanations"
    1. `Duplicate licenses cost us **a great deal of money**.` / `are very expensive.`
    2. **break even**: revenue equals costs.
    3. **The conclusion** or the most important result, not the detail.
    4. `In the black` (profitable).
    5. `We **wrote it off** last quarter.` Pronoun in the middle.
    6. **it is very expensive** (or `it is costly`): `cost a fortune` is informal.
    7. **write-off**: a complete loss (noun).
    8. `**The bottom line** is that we need a second region.`

!!! warning "When NOT to use them"
    Use `in the red`, `write off` and `break even` with finance colleagues only when you know the accounting meaning; they have precise definitions there. Avoid `cost a fortune` and `cost an arm and a leg` in formal proposals and vendor negotiations (they signal emotion, not numbers). Say `what does it cost?` with a figure instead. `Bottom line` can sound abrupt if you use it to end a discussion; soften with `To sum up`.

## Day 5 — Writing: Executive updates {#day-5}
**⏱ 30 min · Fri**

**Bad draft:**

> Hi all, quick update on the project. The team has been working hard and we made a lot of progress on multiple workstreams. There were some challenges with the vendor but we are dealing with them. Testing is ongoing and we are hoping to be in a good position soon. Let me know if you have any questions or concerns and I will get back to you.

**Task:** Rewrite as a weekly executive update in 90-130 words: a subject line with a status colour (RAG: Red, Amber, Green), a bottom-line first line, three bullets (progress with numbers, risk, help needed) and a deadline for the ask. Use strong verbs, not nominalizations; use at least one of `mandate`, `accountable`, `contingent`.

??? success "Model answer and what changed"
    > **Subject: Tracking migration: AMBER, go-live 14 March at risk (decision needed by Friday)**
    >
    > Bottom line: we are on track except for one vendor dependency that could move go-live by two weeks.
    >
    > - **Progress:** 42 of 60 services migrated (70 percent); load tests passed at 2x peak.
    > - **Risk:** the vendor's API sandbox is three weeks late. Go-live is contingent on delivery by 22 February; I rate this a 40 percent chance of slipping.
    > - **Help needed:** I ask the sponsor, who is accountable for vendor escalation, to call the vendor's executive by Friday.
    >
    > Next update: Thursday.

    - **Status colour and bottom line first**: a busy reader needs one line to know whether to worry.
    - **Numbers replace `a lot of progress`** and `hoping to be in a good position`.
    - **Risk is specific,** with a date and a probability.
    - **The ask names an accountable person and a deadline** rather than `let me know if you have questions`.
    - **Strong verbs** (`migrated`, `passed`, `ask`, `rate`) replace `been working hard` and `dealing with`.
    - **A next update date** builds trust.

## Day 6 — Speaking record: The 3-minute executive briefing {#day-6}
**⏱ 30 min · Sat** This is the one talk this week that runs 3 minutes instead of 2, because the focus is the executive briefing format.

**Record a 3-minute talk:** Give the BWRA briefing from Day 3 for your most important current project. Include one number in each section, at least two words from Day 2 (`mandate`, `remit`, `accountable`, `purview`, `stewardship`) and one money idiom from Day 4. Play a colleague interrupting once if possible (you can pause the recording and resume).

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Bottom line unclear | Bottom line late | Clear bottom line | Bottom line, risk and ask unmistakable |
| Structure | No order | Order weak | BWRA present | BWRA complete, within 3 minutes |
| Fluency | Frequent stops | Long pauses, rushed end | Mostly steady | Steady, controlled, with a buffer |
| Grammar accuracy | Errors block meaning | Frequent nominalization-heavy sentences | Few errors; mostly strong verbs | Strong verbs, correct articles and tenses |
| Vocabulary range | Repetitive | Basic terms | Executive terms used correctly | Precise, natural, not jargon-heavy |
| Pronunciation | Hard to follow | Stress errors frequent | Clear; compound stress mostly right | Clear stress, numbers and compounds |

**Shadowing task:** Choose a short executive-style talk (for example, a TED talk by a business leader, or an earnings-style briefing from a public company's investor presentation, if you can find a clean one). Shadow 90 seconds, focusing on how the speaker states the headline and pauses before numbers. Three passes.

**Log your score:** total out of 24 in `docs/log/`, along with your time (target 2:45 to 3:00).

## Day 7 — Soft skills + weekly review: Stakeholder mapping and framing {#day-7}
**⏱ 30 min · Sun**

**Scenario.** You are about to announce the deprecation of a legacy reporting service in six months. Stakeholders: the CFO (worried about cost and audit), the Head of Customer Support (worried about tickets and customer anger), a Staff engineer who built the service (proud, may feel undervalued), and a strategic customer using it heavily. You have limited time and must decide how to approach each one.

**Task:** (1) Sketch a stakeholder map with two axes (power and interest) and place the four people; (2) write a 150-word framing message for the CFO and the Head of Support, using a different angle for each.

??? success "Model response and techniques"
    **Map:** high power and high interest (manage closely): CFO, Head of Support. High power, lower interest (keep informed, consult later): none here. Lower power, high interest (keep involved and respected): the Staff engineer, the strategic customer (high influence on revenue, so treat as key).

    **CFO framing:** `The legacy reporting service costs 320,000 dollars a year and has failed two audits. Retiring it in six months saves that cost and closes the audit finding. The decision I need is your agreement to fund the replacement, contingent on your sign-off next month.`

    **Head of Support framing:** `In six months, customers will move to the new reports, which are faster and self-service. I expect a rise in tickets during the change, so I propose a migration guide, a two-week hypercare window and a weekly check-in with your team. You will be accountable for the customer messaging and I will own the technical fixes.`

    **Techniques used**

    - **Map before you message:** power, interest and stance decide the sequence (engineer and strategic customer are told before the general announcement).
    - **Frame by the listener's interest:** the same fact becomes cost and risk for the CFO, workload and customer experience for Support.
    - **Concrete ask and role clarity** in each message (`accountable`, `own`).
    - **Bottom line first** in each version.
    - **Respect for the builder:** speak to the Staff engineer first and describe the service's history as an achievement, not as failure.
    - **Consistency:** the facts stay the same across audiences; only emphasis changes.

### Weekly recap (20 items)

1. Define nominalization with one example.
2. Rewrite: `We conducted an evaluation of the tool.`
3. Rewrite: `The team made a decision to proceed.`
4. Name two zombie-noun endings.
5. When is a nominalization better than a verb?
6. Rewrite: `There is a need for us to escalate.`
7. Define `mandate` (noun).
8. What does `remit` mean and where is it common?
9. Difference between responsible and accountable.
10. Which word means `range of authority`?
11. Define `stewardship`.
12. What does `bottom line` mean?
13. `break even` meaning.
14. Opposite of `in the red`.
15. Fix: `We wrote off it.`
16. What does BWRA stand for?
17. Stress: `BOTtom line` or `bottom LINE` as a compound?
18. What goes in the subject line of an executive update?
19. What are the two axes of a stakeholder map?
20. Why frame the same fact differently for different stakeholders?

??? success "Answers and explanations"
    1. Turning a verb or adjective into a noun: decide to decision.
    2. `We evaluated the tool.`
    3. `The team decided to proceed.`
    4. `-tion`, `-ment`, `-ance`, `-ity`, `-ness` (any two).
    5. For cohesion (`This increase...`), naming things, formal or hedged tone, unknown agent.
    6. `We need to escalate.`
    7. Official authority to act.
    8. The area of responsibility given to a person or group; mostly UK.
    9. Responsible does the work; accountable answers for the result (one per item).
    10. purview.
    11. Careful management of something entrusted to you.
    12. The final result or most important point.
    13. Reach the point where revenue equals costs.
    14. in the black.
    15. `We wrote it off.`
    16. Bottom line, Why, Risk, Ask.
    17. `BOTtom line` (first element stressed).
    18. Status colour (RAG), the headline and the decision needed with a date.
    19. Power (or influence) and interest.
    20. Each listener cares about different consequences; emphasis changes but facts stay consistent.

**Self-score**

- [ ] I replaced weak verb plus abstract noun with a strong verb in my writing.
- [ ] I used mandate, remit, accountable, purview, stewardship in real sentences.
- [ ] I used bottom line, break even, write off, in the red correctly.
- [ ] I delivered a 3-minute executive briefing within time.
- [ ] I wrote an executive update with a bottom line, a number and a dated ask.
- [ ] I can map stakeholders and frame one message for two audiences.

**Error log:** write down your top 3 recurring mistakes this week (for example, stacked `of` phrases, `-tion` overuse, pronoun placement with phrasal verbs) and one correct model sentence for each.
