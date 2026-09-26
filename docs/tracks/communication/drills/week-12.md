---
title: "Week 12 drills — Cohesion, review and executive summaries"
track: communication
week: 12
last_reviewed: 2026-09-25
---

# Week 12 — Cohesion, review and executive summaries

!!! abstract "This week"
    **Grammar:** Linking words and cohesion · **Vocabulary:** Review, spaced repetition round · **Idioms & phrasal verbs:** Idiom review round · **Speaking:** Shadowing practice 2 · **Writing:** Executive summaries · **Soft skill:** Cross-cultural communication
    **Light week (20 min per day).** Exercises are shortened to about 6 items and 3 new words. **Checkpoint comm-3:** at the end of the week, re-read your error log from Weeks 7-11, pick your three most frequent errors, and write one correct sentence for each in `docs/log/`. Then record a 2-minute talk (Day 6) and compare your rubric score with Week 8.

## Day 1 — Grammar: Linking words and cohesion {#day-1}
**⏱ 20 min · Mon** Cohesion is what makes a paragraph read as one argument rather than a list of sentences.

### Rule in 60 seconds

Linking words belong to three grammatical classes, and each has its own punctuation and structure.

| Class | Examples | What follows | Punctuation |
|---|---|---|---|
| Conjunctions | although, whereas, because, since, so, but, while | a clause (subject + verb) | comma before `but/so`; comma after a fronted clause: `Although it worked, we rolled back.` |
| Conjunctive adverbs | however, therefore, moreover, nevertheless, consequently, in addition | start a new sentence or follow a semicolon | `...; however, ...` or `. However, ...` with a comma after |
| Prepositions | despite, in spite of, because of, due to, owing to, in addition to | a noun phrase or `-ing` | no special punctuation |

**Function map**

- **Contrast:** but, although / even though, whereas / while, however, nevertheless, that said, despite / in spite of.
- **Cause:** because, since, as; because of, due to, owing to; **result:** so, therefore, consequently, as a result, hence.
- **Addition:** and, moreover, furthermore, in addition, besides; in addition to + noun/-ing.
- **Sequence:** first, then, subsequently, finally; **example:** for instance, such as, in particular.

**Rules and the errors fluent speakers make**

- **Two contrast words in one clause:** `Although it was slow, but we shipped it` is wrong. Use one: `Although it was slow, we shipped it` or `It was slow, but we shipped it.` The same goes for `Because ... so ...`.
- **`Despite` takes no `of`:** `Despite the delay` or `In spite of the delay`. `Despite of` is wrong. `Despite the fact that + clause` works.
- **`Because` needs a clause; `because of` needs a noun:** `because the vendor was late` / `because of the vendor's delay`. `Due to` follows `be` in careful usage (`The delay was due to a bug`), but is common as a sentence opener in business writing.
- **Comma splice:** `The pilot succeeded, however we cannot scale it` is wrong. Use `The pilot succeeded; however, we cannot scale it` or `. However, ...`.
- **`In addition to`** takes a noun or `-ing`: `In addition to fixing the bug, we added a test`; the `to` is a preposition, not part of an infinitive.
- **Overusing connectors:** a sentence starting with `Moreover` or `Furthermore` every time reads mechanical. Use them only when adding a stronger point.

**Cohesion beyond connectors**

- **Old before new:** start with what the reader already knows, end with the new point: `We migrated the database. The migration exposed a stale index.`
- **`This` + noun beats bare `This`:** `This delay`, `This change`. A bare `This caused the outage` after three actions is ambiguous.
- **Repeat key terms** rather than switching synonyms in technical writing (`the cache`... `the cache`, not `the buffer`).

### Exercise

Correct or complete (6).

1. Although the migration was successful, but we found several defects.
2. Despite of the delay, we shipped on 14 March.
3. We slipped ___ the vendor's delay. (because / because of)
4. The pilot succeeded, however we cannot scale it yet.
5. ___ fixing the bug, we added a regression test. (In addition to / In addition)
6. `We changed the schema, migrated the data and updated the clients. This caused the outage.` What is the problem, and how would you fix it?

??? success "Answers and explanations"
    1. `Although the migration was successful, we found several defects.` Only one contrast marker per clause.
    2. `**Despite** the delay...` (or `In spite of`). `Despite` never takes `of`.
    3. **because of**: followed by a noun phrase (`the vendor's delay`).
    4. `The pilot succeeded; **however,** we cannot scale it yet.` (or `. However,`). `However` is an adverb, so a comma alone makes a comma splice.
    5. **In addition to**: a preposition plus `-ing`.
    6. `This` is ambiguous: it could refer to the schema change, the migration or the client update. Fix: `The schema change caused the outage.` (choose the actual cause, or say `Two of these steps caused the outage`). *Note:* the model fix depends on the facts; the point is that `this` needs a clear referent.

### Use it
Write a 3-sentence paragraph about a real trade-off in your project with one contrast connector, one cause connector and one `this + noun`. Check punctuation.

## Day 2 — Vocabulary: Review, spaced repetition round {#day-2}
**⏱ 20 min · Tue** Three new words, then a round of review from Weeks 7-11.

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| nuanced | adjective | Showing subtle distinctions rather than a simple, all-or-nothing view. | The board wanted a nuanced assessment of the vendor, not a simple recommendation. |
| contingent | adjective | Depending on something that may or may not happen; (`contingent on`). | The go-live date is contingent on the regulator's approval. |
| reconcile | verb | To make two conflicting things consistent, or to check that two sets of records agree. | Finance needs us to reconcile the billing totals with the ledger by month end. |

### Collocations and word family

- **nuanced:** a nuanced view / understanding / position / discussion; noun `nuance` (a subtle difference); `nuanced` is a positive word for careful thinking.
- **contingent:** contingent on / upon; noun `contingency` (a plan for a possible problem: `a contingency plan`); do not confuse with `continuous`.
- **reconcile:** reconcile A with B / reconcile A and B / reconcile differences / reconcile accounts; noun `reconciliation`; `be reconciled to` (accept) is a different sense.

### Exercise

Cloze (6). Words from earlier weeks: **corroborate, leverage, materially, negligible, candid, scrutiny, expedite**.

1. Please ______ the two ledgers before the audit.
2. The launch is ______ on legal approval.
3. Give me a ______ view: is the new model better in every segment?
4. Independent tests ______ the vendor's benchmark.
5. The change did not ______ affect revenue; the impact was ______.
6. If we ______ the vendor's existing connectors and ______ the approval, we can still meet the date. (two different words)

??? success "Answers and explanations"
    1. **reconcile**: make the records agree.
    2. **contingent**: depends on approval.
    3. **nuanced**: not a yes/no answer (the phrase `in every segment` asks for detail, not a yes/no).
    4. **corroborated** (Week 8).
    5. **materially**, **negligible** (Week 9).
    6. **leverage** (Week 10) and **expedite** (Week 11).

### Use it
Write three sentences: one with `contingent on`, one with `nuanced`, one with `reconcile`. Say them aloud as if in a steering meeting.

## Day 3 — Speaking: Shadowing practice 2 {#day-3}
**⏱ 20 min · Wed**

**Prompt:** Shadow a 90-second clip of a fluent professional speaker (for example, a segment of a BBC Learning English or 6 Minute English episode, or a TED talk). Do not analyze content; imitate the rhythm.

**Structure of a shadowing session**

1. **Listen** once for meaning (30 s).
2. **Read** the transcript and mark stressed words (30 s).
3. **Shadow** three passes: speak 0.5 seconds behind the speaker, first with the transcript, then without.
4. **Record** your last pass and compare it with the original.

**Pronunciation micro-drill: weak forms.** In connected speech, function words (`to`, `for`, `of`, `and`, `the`, `a`, `can`, `have`) are usually unstressed and reduced to a schwa /ə/. Content words carry stress.

| Written | Spoken | Say it |
|---|---|---|
| a lot of it | a LOT_a it | `a LOT-uv-it` |
| ready for the release | READy fer the reLEASE | weak `for` /fə/ |
| we have to decide | we HAFta deCIDE | `have to` becomes `hafta` |
| roll it out and test it | ROLL_it OUT_n TEST it | `and` becomes /n/ |
| the cost of the delay | the COST_uv the deLAY | `of` becomes /əv/ |

Common error: stressing every word equally, which sounds flat and tiring for listeners. Stress the content words and let the rest shrink.

**Self-check**

- [ ] I matched the speaker's pauses within about half a second.
- [ ] I reduced function words instead of stressing them.
- [ ] I stressed the content words (nouns, verbs, numbers).
- [ ] My last pass sounded closer to the speaker than my first.

## Day 4 — Idioms & phrasal verbs: Idiom review round {#day-4}
**⏱ 20 min · Thu** Five expressions from Weeks 1-6 that turn up on almost every project call.

| Expression | Meaning | Example |
|---|---|---|
| on the same wavelength | Thinking in a similar way and understanding each other easily; informal, US and UK. | The two leads are on the same wavelength about the rollout order, which speeds up every review. |
| fall behind | To make less progress than planned, or than others; neutral, common phrasal verb. | The integration team is starting to fall behind because of the vendor's delays. |
| on the horizon | Likely to happen soon; neutral, common in both US and UK business writing. | Three new carrier integrations are on the horizon for next quarter. |
| a tangled web | A complicated, interconnected situation that is hard to unpick; neutral to literary in register, common in business writing. | The billing logic had become a tangled web of special cases for individual customers. |
| check in (with) | To make brief contact to get an update; informal to neutral, common in US and UK business. | I'll check in with the vendor on Monday to see where things stand. |

### Exercise

Choose or complete (6).

1. Rewrite plainly: `We need to get on the same wavelength about the release scope.`
2. Fix: `The project is falling behind of schedule.`
3. `The permissions logic in this migration has become ______: three teams, two clouds and one deadline of overlapping rules.` (a tangled web / big picture)
4. `A redesign of the feature is ______ for next quarter.` (on the horizon / on the same wavelength)
5. Rewrite: `I will contact them again on Friday to check.` with `check in`.
6. Which idiom would you avoid in a formal letter to a regulator?

??? success "Answers and explanations"
    1. `We need to agree on the release scope.`
    2. `The project is **falling behind** schedule.` No `of`.
    3. **a tangled web**: a complicated, interconnected set of rules.
    4. **on the horizon**.
    5. `I will **check in** with them on Friday.`
    6. Any of them; `on the same wavelength` and `a tangled web` are the most informal or figurative. Use `agreed` and `a complicated set of rules`.

!!! warning "When NOT to use them"
    Use idioms to speed up internal conversation, not to explain a serious issue to a regulator, customer executive or non-native reader. If a listener looks confused, restate in plain language rather than repeating the idiom louder.

## Day 5 — Writing: Executive summaries {#day-5}
**⏱ 20 min · Fri**

**Bad draft:**

> This document provides an overview of the various considerations associated with the potential migration of the tracking platform to a new cloud provider. There are several factors, including cost, risk, and timeline, and the team has done a lot of analysis. Overall, the migration has both advantages and disadvantages. More details are in the following pages.

**Task:** Rewrite as an executive summary of 80-110 words that lets a reader make a decision without reading further. Include: the recommendation, the reason with a number, the main risk, the cost or time, and the decision needed with a date.

??? success "Model answer and what changed"
    > **Recommendation.** Migrate the tracking platform to Provider B in two phases, starting in January.
    >
    > **Why.** Provider B reduces run cost by about 28 percent (1.4 million dollars a year) and removes the regional capacity limit that caused three outages this year.
    >
    > **Risk.** The data migration is the main risk; we will mitigate it with a four-week parallel run. Total cost is 900,000 dollars over nine months.
    >
    > **Decision needed.** Approval by 15 November, so the vendor contract can be signed before year-end pricing expires.

    - **Recommendation first**, not an overview of considerations.
    - **Numbers** replace `several factors` and `a lot of analysis`.
    - **Risk and cost stated honestly,** each in one line.
    - **A decision and a date** replace `more details are in the following pages`.
    - **Labeled sections** let a busy reader skim; the whole page fits one screen.

## Day 6 — Speaking record: Shadowing practice 2 {#day-6}
**⏱ 20 min · Sat**

**Record a 2-minute talk:** Summarize, as if for an executive, the most important project in your area: recommendation, reason with a number, main risk and the decision you need. Use at least two linking words from Day 1 (one contrast, one cause) and one word from Day 2. Then listen back for reduced function words.

**Rubric (score 1-4)**

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Clarity | Message unclear | Recommendation buried | Clear recommendation | Recommendation and decision unmistakable |
| Structure | No order | Order weak | Recommendation, reason, risk, ask present | All present with clear linking |
| Fluency | Frequent stops | Several long pauses | Occasional hesitation | Smooth and steady |
| Grammar accuracy | Errors block meaning | Frequent connector errors | Few errors | Connectors and punctuation-in-speech correct |
| Vocabulary range | Repetitive | Basic | Some precise words | Precise and varied |
| Pronunciation | Flat, every word stressed | Some reduction | Mostly natural rhythm | Natural stress and weak forms |

**Shadowing task:** Choose a different clip from Day 3 (another 90 seconds from a TED talk or a BBC Learning English episode). Do one pass with the transcript and one without. Log which phrases you reduced correctly.

**Log your score (comm-3):** total out of 24, and compare with your Week 8 presentation score in `docs/log/`.

## Day 7 — Soft skills + weekly review: Cross-cultural communication {#day-7}
**⏱ 20 min · Sun**

**Scenario.** You lead a global project with engineers in Bangalore, Copenhagen and Houston. In review meetings, the Copenhagen team disagrees openly and briefly, the Bangalore team says "we will try" when a request is unrealistic, and the Houston team expects a decision at the end of every meeting. A Danish engineer told you, "Your Bangalore team never says no." You suspect the issue is culture, not competence.

**Task:** Write 120-150 words (or script your talk) to the team, proposing two working agreements that reduce misunderstandings without blaming any group.

??? success "Model response and techniques"
    > Thanks, everyone. I want to suggest two working agreements, because we communicate in different styles and that is normal. First, when we make a request, we will state the level of confidence: for example, "high confidence, fully doable," "medium, contingent on the API," or "low, I see a risk." That way, "we will try" always comes with a number, and nobody has to guess whether it means yes or maybe. Second, disagreement is welcome, and we will separate the idea from the person by saying, "I see it differently, and here is why." Finally, every meeting will end with a one-line summary of decisions and owners. Please tell me if you want to change any of this; we can review it in a month.

    **Techniques used**

    - **Normalize differences** (`different styles, and that is normal`) instead of naming a culture as a problem.
    - **Make implicit signals explicit:** a shared confidence scale converts `we will try` into a comparable message.
    - **Give a safe script for disagreement** to lower the cost of directness.
    - **Close with decisions and owners,** which serves the Houston expectation.
    - **Invite revision** (a one-month review) to share ownership.
    - Cross-cultural principle: shift from `who is right` to `how do we make our signals clear`; high-context speakers rely on tone and context, low-context speakers on explicit words. Both need to adapt.

### Weekly recap (20 items)

1. Correct: `Although it was slow, but we shipped it.`
2. Correct: `Despite of the delay...`
3. Which is right: `because the delay` or `because of the delay`?
4. Which class is `however`?
5. Fix the comma splice: `It worked, however it was slow.`
6. What follows `in addition to`?
7. Why is a bare `This` risky?
8. What is `old before new`?
9. Define `nuanced`.
10. Define `contingent`; preposition?
11. Define `reconcile` (two senses).
12. Idiom: having the same understanding, easily.
13. Fix: `The project is falling behind of schedule.`
14. `a tangled web` meaning.
15. What does `on the horizon` mean?
16. What happens to `to` and `of` in fast speech?
17. Why shadow at 0.5 seconds behind?
18. What goes first in an executive summary?
19. What is a shared confidence scale?
20. Which two things does a good executive summary end with?

??? success "Answers and explanations"
    1. `Although it was slow, we shipped it.`
    2. `Despite the delay...`
    3. `because of the delay` (noun); `because the delay was long` (clause).
    4. Conjunctive adverb.
    5. `It worked; however, it was slow.`
    6. A noun or `-ing` form.
    7. It can refer to several things; use `this + noun`.
    8. Start a sentence with known information, end with the new point.
    9. Showing subtle distinctions.
    10. Depending on something uncertain; `contingent on`.
    11. Make two conflicting things consistent; check that records agree.
    12. on the same wavelength.
    13. `The project is falling behind schedule.`
    14. A complicated, interconnected situation that is hard to unpick.
    15. Likely to happen soon.
    16. They reduce to weak forms: /tə/ and /əv/.
    17. It forces you to copy rhythm as you hear it, not after.
    18. The recommendation.
    19. Speakers label each commitment `high/medium/low` to make implicit signals explicit.
    20. The decision needed and the date.

**Self-score**

- [ ] I use one contrast marker per clause and avoid comma splices.
- [ ] I used nuanced, contingent, reconcile in real sentences.
- [ ] I reduced function words when shadowing.
- [ ] I can write a decision-ready executive summary.
- [ ] I can propose working agreements across cultures without blame.
- [ ] I completed the comm-3 checkpoint log.

**Error log (comm-3):** write your top 3 recurring mistakes from Weeks 7-11 (for example, passive of intransitive verbs, article errors, comma splices) and one correct model sentence for each. Note how each differs from your Week 8 list.
