---
title: "Week 07 drills — Explaining and influencing"
track: communication
week: 7
last_reviewed: 2026-09-25
---

# Week 07 — Explaining and influencing

!!! abstract "This week"
    **Grammar:** Relative clauses and reported speech · **Vocabulary:** Persuasion words: compelling, tangible, rationale · **Idioms & phrasal verbs:** Teamwork: pull your weight, have each other's back · **Speaking:** Explaining technical ideas to non-technical people · **Writing:** Technical explanations with analogies · **Soft skill:** Influencing without authority

## Day 1 — Grammar: Relative clauses and reported speech {#day-1}
**⏱ 30 min · Mon** Relative clauses let you pack a definition or a qualification into one sentence. Reported speech is how you relay what a vendor, a VP or an incident channel said, and you do it all day in status calls.

### Rule in 60 seconds

**Defining vs non-defining relative clauses**

| | Defining (essential) | Non-defining (extra) |
|---|---|---|
| Commas | none | commas around the clause |
| Pronouns | who / that (people); that / which (things); whose; zero pronoun allowed for objects | who / which / whose only; never `that`, never zero |
| Example | The engineers **who were on call** got a day off. (only some) | The engineers, **who were on call**, got a day off. (all of them) |

- **Zero pronoun:** you may drop the pronoun when it is the *object* of the clause: `The vendor (that) we chose is late.` You cannot drop it when it is the *subject*: `The vendor that missed the deadline...`.
- **Prepositions:** formal style puts the preposition before `which/whom` (`the framework on which we rely`); normal style leaves it at the end (`the framework we rely on`). Both are correct; do not force the formal one in speech.
- **whose** works for things too: `a service whose owner has left`.
- **Reduced clauses:** `the team responsible for ingestion` = `the team that is responsible for ingestion`.
- **Fluent-speaker error 1: the resumptive pronoun.** `The service which it handles payments` is wrong: the relative pronoun already *is* the subject or object. Do not repeat it with `it/he/they`.
- **Fluent-speaker error 2:** `that` after a comma (`Our API, that was rewritten...`) and `what` after a noun (`everything what we shipped`). Use `which` after a comma; use `that` (or nothing) after `everything/all/something`.

**Reported speech**

- Reporting in the past normally **backshifts** the tense: `"We are migrating"` becomes `He said they were migrating.` Present simple to past simple, present perfect and past simple to past perfect, `will` to `would`, `can` to `could`, `must` to `had to` (obligation).
- **Backshift is optional** when the statement is still true or still in the future: `The vendor said they *will* deliver on the 14th.` Use it when you want to signal "I am not vouching for this" or when the fact has changed.
- **Time and place words shift** with the viewpoint: `next week` becomes `the following week`; `yesterday` becomes `the day before`; `here` becomes `there`; `this` becomes `that`.
- `say` does not take a person object; `tell` requires one: `She told us that...` / `She said that...` (never `said us`).
- **Reported questions have statement word order, no `do`, no question mark:** `She asked what the root cause was`, `He asked if we had rolled back`.
- **Reporting verbs with patterns:** `suggest that + subject + base form / should` (`He suggested that I roll back`, or `suggested rolling back`), never `suggested me to roll back`. `Recommend` works the same way. `Advise/ask/tell/persuade` take a person plus `to`-infinitive: `She advised us to freeze the release.`
- Error fluent speakers make: keeping question order (`He asked me what was the root cause`) and `explain me / suggest me`.

### Exercise

Correct or complete each item (10).

1. The service which it processes the invoices was migrated last quarter.
2. Combine into one sentence using a relative clause: `We hired an engineer. Her team now owns the routing engine.`
3. Our billing service, that was written in 2012, is our biggest risk.
4. Report this: `"We are migrating next week," the vendor said on Monday.` (Assume it is now the following Friday and the migration has not happened.)
5. She asked me what was the root cause.
6. He suggested me to roll back the release.
7. Fill in: `The director ___ us that the audit would slip.` (said / told)
8. Which meaning is correct for `The engineers, who were on call, got a day off.`? (a) only the on-call engineers got a day off; (b) all the engineers were on call and all got a day off.
9. Fill in: `Everything ___ the vendor promised turned out to be untrue.` (what / that)
10. Reduce the clause: `The team that is responsible for the ingestion pipeline is under-staffed.`

??? success "Answers and explanations"
    1. `The service **that processes** the invoices was migrated last quarter.` `Which/that` already acts as the subject, so `it` is a duplicate. (`which` is also fine; `that` is more natural for defining clauses in speech.)
    2. `We hired an engineer **whose team** now owns the routing engine.` `Whose` replaces the possessive `her`.
    3. `Our billing service, **which** was written in 2012, is our biggest risk.` A comma-separated (non-defining) clause cannot use `that`.
    4. `The vendor said on Monday that they **were migrating** the following week.` Since the migration is now overdue, backshift is the natural choice; it also distances you from the promise. `Time shift: next week to the following week.` (Keeping `are migrating` would sound as if it were still pending.)
    5. `She asked me **what the root cause was**.` Reported questions take statement word order.
    6. `He suggested **that I roll back** the release` or `He suggested **rolling back** the release.` `Suggest` does not take `person + to`-infinitive. (In US English `that I roll back`; UK often `that I should roll back`.)
    7. `The director **told** us that...` Tell needs an object; `said us` is ungrammatical (`said to us` is possible, but `told us` is simpler).
    8. **(b).** Commas make the clause non-defining: it adds information about *all* the engineers. Without commas (`The engineers who were on call got a day off`) only some engineers are identified.
    9. `Everything **that** the vendor promised...` (or no pronoun). `What` cannot follow a noun/pronoun antecedent such as `everything`; `what` itself means "the thing that".
    10. `The team **responsible for the ingestion pipeline** is under-staffed.` Relative pronoun plus `be` can be dropped before an adjective or prepositional phrase.

### Use it
Write or say three sentences about your work: one defining clause (`the service that...`), one non-defining clause with commas, and one reported statement from a real meeting (`She told us that... / He asked whether...`). Check: no `it` copied after the pronoun, `which` (not `that`) after commas, and statement word order in the reported question.

## Day 2 — Vocabulary: Persuasion words: compelling, tangible, rationale {#day-2}
**⏱ 30 min · Tue** These five words carry the weight of a business case: they describe what makes an argument land.

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| compelling | adjective | Convincing or forcing you to agree because it is so strong; a compelling case leaves little room for doubt. | The latency data made a compelling case for moving the routing service off the shared cluster. |
| tangible | adjective | Real and measurable; something you can point to, as opposed to vague or theoretical. | Leadership wants tangible results, such as a 20 percent drop in failed bookings, before funding phase two. |
| rationale | noun | The set of reasons behind a decision or plan (stress: ra-tion-ALE; plural: rationales). | The design doc should state the rationale for choosing an event log over polling. |
| buttress | verb | To strengthen an argument or position by adding supporting evidence (formal; originally an architectural support). | You will need production traces to buttress the claim that the cache is the bottleneck. |
| resonate | verb | To strike a chord; to be received as relevant or meaningful by an audience. | The cost argument did not resonate with the platform team; reliability was what they cared about. |

### Collocations and word family

- **compelling:** compelling evidence / reason / case / argument / need; `compelling` (adj), `compel` (verb), `compulsion` (noun, not the same register). Do not confuse with `compulsory` (required by rule).
- **tangible:** tangible benefit / outcome / results / progress; opposite `intangible` (culture, brand, goodwill). Adverb: tangibly.
- **rationale:** the rationale behind / for; a clear / sound / underlying rationale. Not `rationalization` (which implies inventing reasons after the fact).
- **buttress:** buttress an argument / a case / a claim (with data); also a noun (`a buttress`, the physical support of a wall). Pronounced BUT-ress. Do not confuse with `butt` or with `bolster` (a near-synonym, more general).
- **resonate:** resonate with the audience / stakeholders / customers; adjective `resonant`; noun `resonance`. Pattern: `X resonates with Y` (not `resonates to`).

### Exercise

Fill each gap (8). Two review words appear from earlier weeks: **mitigate** and **prioritize**.

1. The steering group will not approve the migration budget without a ______ reason to act this quarter.
2. The ______ for splitting the monolith was documented in the first two pages of the RFC.
3. We need ______ progress by the end of Q3, not another roadmap slide.
4. Can you ______ that argument with a load test, not a hunch?
5. The story about the two-hour outage really ______ with the finance directors.
6. To ______ the risk of data loss, we replicate to a second region.
7. We had to ______ the customer-facing fixes over internal tooling.
8. Which is stronger in a business case: a `______ benefit` or an `intangible benefit`? Justify in one clause.

??? success "Answers and explanations"
    1. **compelling**: a reason strong enough to convince; `tangible reason` is not a standard collocation.
    2. **rationale**: reasons behind a decision.
    3. **tangible**: measurable, visible progress, contrasted with slideware.
    4. **buttress**: strengthen the argument with supporting evidence.
    5. **resonated** (past tense; `with` the directors).
    6. **mitigate** (review, Week 1): reduce the severity of.
    7. **prioritize** (review, Week 1): treat as more important than something else.
    8. **tangible**: it can be measured and defended in a budget conversation; intangible benefits are real but harder to defend.

### Use it
Say aloud, then write: (1) a compelling reason to pay down a specific piece of tech debt in your team, (2) one tangible result you delivered last year, (3) the rationale for a design choice you made. Aim for full sentences of 15-25 words.

## Day 3 — Speaking: Explaining technical ideas to non-technical people {#day-3}
**⏱ 30 min · Wed**

**Prompt (60-90 seconds):** Explain to a warehouse operations manager, who has no software background, why the system occasionally shows a container as "in two places". You can use one analogy. Do not use jargon without defining it.

**Structure: Point, Picture, Proof, Payoff (PPPP)**

1. **Point** (one sentence, no jargon): `In short, two of our systems briefly disagree about where a container is.`
2. **Picture** (the analogy): `Think of two clerks keeping separate ledgers for the same yard...`
3. **Proof** (one concrete example with a number): `Last Tuesday it happened for about 40 containers, for roughly 90 seconds.`
4. **Payoff** (what it means for them, and what they should do): `For you, that means... and we are fixing it by...`

Useful phrases: `Put simply...`, `The easiest way to think about it is...`, `It works a bit like...`, `The catch is...`, `What that means for you is...`, `Does that make sense, or shall I try another angle?`

**Pronunciation micro-drill: technical words people mishear** (capitals mark the stressed syllable)

| Word | Say it | Common error |
|---|---|---|
| latency | LAY-ten-see | LA-ten-see |
| cache | KASH (same as "cash") | "ka-SHAY" |
| hierarchy | HY-er-ar-kee | hi-ER-ar-kee |
| schema | SKEE-muh | SHAY-ma |
| queue | KYOO | "kway-oo" |
| daemon | DEE-mon | DAY-mon |
| Kubernetes | koo-ber-NET-eez | koo-BER-netis |
| analogy / analogous | a-NAL-o-gee / a-NAL-o-gus | stress shifted to the last syllable |
| architecture / architectural | AR-ki-tek-chur / ar-ki-TEK-chur-al | stress does not shift in the noun |

Say each word three times, then in the frame: `The ______ is the reason for the delay.` Listen for the stressed syllable being longer and higher, not just louder.

**Self-check**

- [ ] I stated the point in one jargon-free sentence before explaining.
- [ ] The analogy maps to something the listener already knows and I said where it breaks down.
- [ ] I gave one number or example, not five.
- [ ] I finished with what it means for them.
- [ ] I checked understanding at least once (`Does that make sense?`).

## Day 4 — Idioms & phrasal verbs: Teamwork: pull your weight, have each other's back {#day-4}
**⏱ 30 min · Thu**

| Expression | Meaning | Example |
|---|---|---|
| pull your weight | Do your fair share of the work; often used in the negative (`not pulling his weight`). Neutral, common in both US and UK; can sound critical. | Everyone on the rota needs to pull their weight during the migration weekend. |
| have each other's back(s) | Support and protect one another; informal, positive, common in US and UK. | On a good on-call rotation, people have each other's backs at 3 a.m. |
| throw someone under the bus | Blame or sacrifice someone to protect yourself. Informal, US origin, now international; clearly negative. | The postmortem should not throw the junior engineer under the bus for a process failure. |
| roll up your sleeves | Get ready to work hard; informal, encouraging. | When the outage began, the leads rolled up their sleeves and joined the debugging call. |
| wear many hats | Perform several different roles; neutral and common. | In a small platform team you wear many hats: architect, on-call engineer, and recruiter. |

### Exercise

Choose or complete (8).

1. A colleague repeatedly skips code reviews and leaves others to do them. He is not ______. (pulling his weight / rolling his sleeves)
2. Rewrite plainly: `Our team really has each other's backs.`
3. During the release, the CTO called me at midnight to ask what went wrong, and my manager blamed me in front of the executives. He threw me under the ______. (bus / train)
4. Replace with an idiom: `We all need to start working hard on this backlog now.`
5. Which is more formal in a performance review: `not pulling his weight` or `not meeting expectations for contribution`?
6. `As a staff engineer I write code, mentor and manage vendors.` Rewrite using an idiom.
7. True or false: `have each other's back` is offensive in a formal client letter. Explain.
8. Fix: `She pulled her own weights on the project.`

??? success "Answers and explanations"
    1. **pulling his weight**. `Roll up your sleeves` describes starting hard work, not the ongoing fair share.
    2. `Team members support and protect one another.` (or `We can rely on each other`).
    3. **bus**. Fixed phrase.
    4. `Let's roll up our sleeves and get through this backlog.`
    5. `Not meeting expectations for contribution` is the formal option; `pulling his weight` is a spoken idiom and a little blunt in writing.
    6. `As a staff engineer I wear many hats: I code, mentor and manage vendors.`
    7. **Not offensive, but too informal**: `have each other's back` is friendly. Use `support one another` in formal letters.
    8. `She pulled **her weight**` (singular, fixed).

!!! warning "When NOT to use them"
    Do not use idiom clusters with people from other cultures or on a call where you suspect low comfort in English: `throw under the bus` and `have each other's back` are harder for non-native speakers than `blame` and `support`. In performance feedback, avoid `not pulling their weight`: it is a judgment about a person, not behavior. Use SBI (Week 2) instead.

## Day 5 — Writing: Technical explanations with analogies {#day-5}
**⏱ 30 min · Fri**

**Bad draft** (from a design doc going to finance):

> The event bus implements an asynchronous publish-subscribe pattern wherein producers emit messages to topics without knowledge of consumers, which allows eventual consistency between microservices but that can lead to out of order delivery and idempotency issues which we mitigate by using a dead letter queue.

**Task:** Rewrite in 90-120 words for a finance director. Constraints: one analogy, at most one technical term (defined), no sentence longer than 25 words, and a sentence stating why it matters for cost or risk.

??? success "Model answer and what changed"
    > Our systems talk to each other through a shared **message board**. When a booking is created, the booking system pins a note on the board; the billing and notification systems each pick up the notes they care about, in their own time. The booking system never needs to know who is reading. The benefit is that one slow system cannot hold up the others. The trade-off is that a note can occasionally arrive late or twice, like a duplicate post-it, so billing checks each note before acting on it. Notes that cannot be processed go to a "returns pile" for a person to review. That design is the reason a billing outage does not stop customers from booking.

    - **Analogy up front and consistent** (message board, notes, returns pile) rather than three technical patterns in one sentence.
    - **Jargon defined or dropped:** `idempotency` became "checks each note before acting"; `dead letter queue` became "returns pile".
    - **Split one 45-word sentence** into short sentences of 12-20 words.
    - **Trade-off stated honestly:** the analogy also explains the downside (late or duplicate notes).
    - **Closing sentence ties to the reader's concern** (risk and continuity).
    - Note the relative clauses: `the notes they care about` (zero pronoun) and `notes that cannot be processed` (defining `that`).

## Day 6 — Speaking record: Explaining technical ideas to non-technical people {#day-6}
**⏱ 30 min · Sat**

**Record a 2-minute talk:** Explain one technical concept from your current project (for example, idempotency, caching, an ML model's confidence score, or a rollback) to a senior business stakeholder with no engineering background. Use PPPP from Day 3, one analogy, and one relative clause with `whose` or `which` (commas). Play back once; do not re-record more than twice.

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Jargon dominates | Some undefined terms | Mostly plain, one slip | Fully plain; analogy lands |
| Structure | No clear order | Point unclear until the end | Point, picture, payoff present | Clear PPPP with signposts |
| Fluency | Frequent stops | Several long pauses | Occasional hesitation | Smooth, deliberate pauses |
| Grammar accuracy | Errors block meaning | Frequent errors | Few errors; none block meaning | Rare slips; relative clauses correct |
| Vocabulary range | Repetitive | Limited to basic words | Some precise words (tangible, rationale) | Precise, varied, natural |
| Pronunciation | Hard to follow | Word stress often wrong | Mostly clear; a few stress errors | Clear stress and rhythm |

**Shadowing task:** Choose a 3-minute clip from a TED talk in which a scientist or engineer explains a complex idea with an analogy (for example, search TED for a talk on how a technology works). Listen once, then read the transcript, then shadow: speak 0.5 seconds behind the speaker, matching stress and pauses. Do three passes of one minute. BBC Learning English's 6 Minute English is a good alternative for slower speech.

**Log your score:** total out of 24 in your learning log (`docs/log/`) with one sentence: "Biggest improvement / biggest issue this week."

## Day 7 — Soft skills + weekly review: Influencing without authority {#day-7}
**⏱ 30 min · Sun**

**Scenario.** You lead the payments integration team. You want the security team (a separate department reporting to a different VP) to prioritize a review of your new tokenization service within two weeks, ahead of a customer launch. Their queue is full, and their lead, Marta, told you last month, "We are not a service desk." You have no authority over her.

**Task.** Write a 150-word message to Marta, or script the conversation, that asks for the review and could realistically succeed.

??? success "Model response and techniques"
    > Hi Marta, I understand your queue is heavy, and I do not want to jump it without a good reason. Here is the reason: our tokenization service goes live for a major customer on the 14th, and it handles card data, so I would rather have your team's eyes on it than ship it unreviewed. I have already done the threat model and attached it, so the review should take roughly two days rather than two weeks. In return, I can put two engineers with you for a week to help build the checklist automation you mentioned, which would reduce your future load. Could we spend 15 minutes on Thursday to agree scope? If the 14th is not realistic for you, I would like to know what would be, so I can plan an honest date with the customer.

    **Techniques used**

    - **Acknowledge her constraint first** (`I understand your queue is heavy`) to avoid triggering the "service desk" reaction.
    - **Shared goal and concrete stakes** (card data, customer, date) rather than "it is urgent".
    - **Reduce her cost:** threat model already done, review scoped to two days.
    - **Reciprocity:** offer help she values, not just a favor request.
    - **Small next step** (15 minutes) and **an exit** (`what would be realistic`), preserving her autonomy.
    - Language: relative clauses `a major customer`, `what would be`; reported speech avoided; hedging with `would rather`, `roughly`.

### Weekly recap (20 items)

1. Which pronoun is not allowed in a non-defining clause: `that`, `which`, `who`?
2. Correct: `The API what we built last year is stable.`
3. When can a relative pronoun be omitted?
4. Report: `"I will send the report tomorrow," she said.` (said on Monday, now Wednesday)
5. Report the question: `"Have you deployed the fix?" he asked.`
6. `suggest` pattern: correct `She suggested me to wait.`
7. Difference between `said` and `told`?
8. Define `whose` in one sentence and give a work example.
9. Synonym for `convincing` from this week.
10. Opposite of `tangible`.
11. Which word: `the ______ behind the decision` (rationale / rationalization)?
12. Preposition: `The pitch resonated ___ the CFO.`
13. Meaning of `buttress` (verb, as used this week).
14. Idiom: works fairly and does their share.
15. Idiom: blames a colleague to save yourself (US).
16. Which two idioms mean `support` and `work hard`?
17. What are the four steps of PPPP?
18. Stress: where is the stress in `rationale`?
19. What three moves make influence without authority work in the model response?
20. Give a one-sentence analogy for a message queue.

??? success "Answers"
    1. `that` (non-defining clauses need `which/who/whose`).
    2. `The API **that** we built last year is stable` (or no pronoun).
    3. When it is the object of the clause (not the subject) in a defining clause.
    4. `She said she would send the report **the next day**` (or `on Tuesday`; backshift plus time shift).
    5. `He asked **if/whether we had deployed** the fix.`
    6. `She suggested **that I wait** / suggested waiting.`
    7. `Tell` requires a person object; `say` does not (`told us` vs `said that`).
    8. `Whose` marks possession: `a service whose owner has left`.
    9. compelling.
    10. intangible.
    11. rationale.
    12. `with`.
    13. To strengthen an argument by adding supporting evidence.
    14. pull your weight.
    15. throw someone under the bus.
    16. have each other's back (support); roll up your sleeves (work hard).
    17. Point, Picture, Proof, Payoff.
    18. ra-tion-**ALE** (last syllable).
    19. Acknowledge constraint, reduce her cost, offer reciprocity (plus a small next step and exit).
    20. `A message queue works like a post office box: senders drop letters in, and the receiver collects them when ready.`

**Self-score**

- [ ] I can use `who/that/which/whose` without a duplicate pronoun.
- [ ] I can report speech with correct backshift and word order.
- [ ] I used compelling, tangible, rationale, buttress, resonate in real sentences.
- [ ] I explained a technical idea with one analogy in under 90 seconds.
- [ ] I wrote a request that acknowledges the other person's constraint.

**Error log:** write down your top 3 recurring mistakes this week (for example, `told/said`, `that` after commas, statement order in reported questions) and one correct model sentence for each.
