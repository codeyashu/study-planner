---
title: "Clauses, participles & cohesion (linking words)"
track: communication
slug: clauses-and-cohesion
priority: P1
complexity: 4
est_hours: 2
phase: 3
tags: [communication, P1]
last_reviewed: 2026-09-25
---

# Clauses, participles & cohesion (linking words)

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 4/5 · **Est. time:** 2 h · **Phase:** 3 · **Prereqs:** [sentence structure & parallelism](sentence-structure-parallelism.md)
    **You're done when:** you can choose the right linker for cause, contrast, concession, addition, sequence and result; write defining and non-defining relative clauses with correct commas; and compress two sentences into one with a participle clause without creating a dangling modifier.

## Why it matters
Cohesion is what turns correct sentences into an argument. Design docs and strategy memos live on relations between ideas: *because, although, whereas, consequently, provided that*. Writers at B2 tend to over-rely on *and, but, so, also, however*, which flattens reasoning. Staff-level prose uses a wider, precise set: it signals *why* something matters, *what trades off against what*, and *what follows*. Participle clauses and reduced relative clauses let you pack information densely; used well they read like an expert, used badly they produce dangling modifiers and ambiguity.

## Core concepts

### Clauses in one page
- **Independent (main) clause:** can stand alone.
- **Dependent clauses:**
  - **Adverbial** (time, reason, condition, contrast, purpose, result): *when, because, if, although, so that, whereas*.
  - **Relative** (adjectival): *who, whom, whose, which, that, where, when, why*.
  - **Nominal (noun clauses):** *that, whether, if, wh-words*: "What matters is that we ship."
- **Non-finite clauses:** *-ing*, *-ed* participle, *to*-infinitive: "Having reviewed the design, we approved it."

### Relative clauses

| Type | Comma? | Pronoun | Example |
|---|---|---|---|
| **Defining** (identifies which one) | no commas | who/that (people), which/that (things), can drop *that* when object | "The engineers **who own the pipeline** are on call." / "The bug (that) we found was critical." |
| **Non-defining** (extra info) | commas | who/which only, never *that*; the pronoun cannot be dropped | "Our billing service, **which was written in 2015**, is being retired." |

**Traps**
- *That* is impossible in non-defining clauses: "The API, that we built, ..." is wrong.
- Comma change = meaning change: "The teams **who use Kafka** need training" (only those that use it) vs "The teams, **who use Kafka**, need training" (all the teams use it: usually a mistake).
- *Whose* for possession, including things: "a service whose owner left".
- *Whom* is formal; "the person I reported to" or "to whom I reported" both fine. Avoid overusing *whom*: "the person who I asked" is common in speech.
- **Sentential *which*:** "The build passed, **which** surprised everyone." refers to the whole clause; keep it close and unambiguous.
- **Preposition placement:** "the tool we rely on" (informal, natural) vs "the tool on which we rely" (formal).
- **Where/when/why:** "the day when it failed", "the reason why we chose it" (*why* can be dropped: "the reason we chose it"). "The reason is because" is redundant: "The reason is that..."
- **Reduced relative clauses:** "The engineers *working on the migration*" (= who are working), "the data *collected last week*" (= that was collected).

### Participle clauses (concise modification)

| Type | Meaning | Example |
|---|---|---|
| Present participle (-ing), active, simultaneous or cause | "Working from home, she..." | "Running the tests locally, I noticed the memory leak." |
| Perfect participle (having + p.p.), earlier action | "Having reviewed the RFC, we approved it." | Emphasises sequence. |
| Past participle (-ed), passive | "Written in Go, the service..." | "Built for scale, the platform..." |
| Being + p.p. (passive, ongoing) | "Being new to the team, he asked..." | Often reason. |
| After conjunctions/prepositions | "before leaving", "while reviewing", "on completing", "after being informed" | |

**The golden rule:** the implied subject of the participle clause = the subject of the main clause (see dangling modifiers in [sentence structure](sentence-structure-parallelism.md)).
- Wrong: "Having reviewed the RFC, the design was approved."
- Right: "Having reviewed the RFC, we approved the design."
- Exception (fixed, absolute constructions): "Generally speaking, ..." "Given the constraints, ..." "Weather permitting..." "All things considered, ..." "Judging by the metrics, ..."

**Use participle clauses to:**
- Compress sequence: "The pod crashed, restarting three times before stabilising."
- Show reason: "Not knowing the root cause, we escalated."
- Add a result: "The change doubled traffic, overwhelming the cache."
- Reduce wordiness: "We ran a load test, which showed..." → "We ran a load test showing..."

**Avoid:** more than one participle clause per sentence; using them for main ideas.

### Noun clauses and reporting
- *That*-clauses: "It is clear **that** we need an owner." *That* can be dropped after common verbs (*think, say, believe, know*), but keep it in formal text and after nouns (*the fact that, the risk that*).
- *Whether/if*: *whether* is standard after prepositions and before *or not* and in formal text: "We need to decide whether to build or buy." "The question of whether..." ("if" is not possible after a preposition or before an infinitive).
- *Wh*-clauses: statement word order: "I don't know **why the job failed**" (not "why did the job fail").
- *The fact that*: use to nominalise a clause after a preposition: "Despite the fact that..." (or *although*).

### Linking words (discourse markers) by function
A **connector** must be used with the right grammar: conjunctions join clauses, prepositions take nouns/-ing, and adverbs need a full stop or semicolon.

#### Addition
| Linker | Type/position | Example |
|---|---|---|
| and, also | conj/adv | "The API is slow and it lacks tests." |
| in addition (to) | prep/adv | "In addition to latency, cost is a concern." |
| furthermore, moreover, what's more | adverb, formal | "Moreover, the vendor does not support X." |
| as well as | prep | "as well as fixing the bug, we..." |
| besides | adv/prep | informal-ish |
| not only ... but also | correlative | see parallelism |

#### Contrast and concession
| Linker | Grammar | Example |
|---|---|---|
| but | conj (informal) | "It works, but it's slow." |
| however | adverb (semicolon/period before, comma after) | "The design is elegant. However, it is expensive." |
| although / even though / though | subordinating conj + clause | "Although the design is elegant, it is expensive." |
| despite / in spite of | preposition + noun/-ing (never + clause) | "Despite the risk, we proceeded." / "Despite being expensive, ..." / "Despite the fact that it is expensive..." |
| whereas / while | contrast between two things | "Kafka is log-based, whereas RabbitMQ is queue-based." |
| yet | conj / adv (more formal than *but*) | "It is simple, yet powerful." |
| nevertheless / nonetheless / even so | adverb, formal | "The risk is high. Nevertheless, we recommend proceeding." |
| on the other hand / by contrast / in contrast | adverb | "On the one hand... on the other hand..." |
| whatever / regardless of | | |
| still | adverb | "It's flawed; still, it works." |

**Trap:** "Despite of", "although ... but" (double), "in spite the risk". Use one connector: "Although it is slow, it is reliable." (not "Although it is slow, but reliable").

#### Cause and reason
| Linker | Grammar | Example |
|---|---|---|
| because | conj + clause | "We rolled back because latency spiked." |
| because of / due to / owing to / thanks to (positive) | prep + noun | "Because of the outage" / "due to" (adjective use) |
| since / as | conj (reason known to reader) | "Since the cache is stale, ..." (*since* = known reason) |
| given that / seeing that / in view of the fact that | | "Given that budgets are frozen, ..." |
| for | conj, formal/literary | avoid |
| the reason is that; this is why | | |

#### Result and consequence
| Linker | Example |
|---|---|
| so | informal; "so we rolled back" |
| therefore / thus / hence / consequently / as a result | formal; adverbs |
| accordingly | "We adjusted the plan accordingly." |
| so ... that / such ... that | "It was so slow that users left." "such a slow service that..." |
| which means / meaning | "..., which means we can't launch in Q2." |
| leading to / resulting in / giving rise to | participle-style |

#### Purpose
| Linker | Example |
|---|---|
| to / in order to / so as to | "in order to reduce cost" (formal) |
| so that / in order that | "so that the team can..." |
| with a view to (+ -ing) | formal |
| for (+ -ing/noun) | "used for monitoring" |
| lest, for fear that | rare; avoid |

#### Sequence, time
*First(ly), second(ly), next, then, after that, subsequently, finally, meanwhile, in the meantime, at the same time, previously, prior to, following, ahead of, until, once, as soon as, by the time, whenever*.
- "In the end/eventually" - eventually a result; "at last" - relief.
- *Afterwards* = adverb; *after* = preposition/conjunction.

#### Condition
*if, unless, provided (that), as long as, in case, assuming, on condition that, otherwise, or else, failing that* (see [conditionals](conditionals-modals-hedging.md)).

#### Exemplification and clarification
*for example, for instance, such as, e.g., in particular, namely, specifically, that is (i.e.), in other words, put differently, to put it simply, that is to say*.
- *Such as* introduces examples in a sentence (no colon); *namely* introduces an exhaustive specification.
- *e.g.* = for example (not exhaustive); *i.e.* = in other words.

#### Summary and emphasis
*in short, in summary, to sum up, overall, all in all, in conclusion, above all, most importantly, indeed, in fact, crucially*.
- *In fact* adds a stronger or contrasting fact; *actually* corrects expectations.

### Punctuation of connectors
- **Adverbs mid-sentence:** "This, however, is not the whole picture."
- **Sentence start:** "However, ..." comma after.
- **Two clauses:** "...; however, ..." semicolon before.
- **Subordinators** at the start of a sentence: comma after the clause ("Although X, Y"), no comma when the clause follows ("Y although X" often no comma, or with for contrast).

### Cohesion beyond connectors
Connectors are only 10-20% of cohesion. The bigger levers:

1. **Old-to-new chain (given-new):** end a sentence with the new item, begin the next with it. "We introduced a **circuit breaker**. **The breaker** trips when..."
2. **Consistent terms** (elegant variation is harmful in technical writing: call it "the queue" every time, not "the buffer", "the channel").
3. **Reference:** *this + noun* ("this approach"), *such*, *the latter/former*, *the same*, *these*.
4. **Ellipsis and substitution:** "We tried caching, and it worked." / "Some agreed; others didn't." *do so*: "We must migrate, and doing so requires..."
5. **Lexical chains:** related terms across a paragraph (*latency, slow, delay, response time*).
6. **Topic sentences and signposting:** "There are three reasons. First, ..." "The second concern is..." "To summarise, ..."
7. **Parallel structure** repeated across paragraphs.
8. **Paragraph-level:** one claim per paragraph; first sentence = claim; last sentence = implication.

**Over-connecting:** a "However/Moreover/Furthermore" opening every sentence sounds mechanical; the logic should be visible without them. Delete a connector; if the meaning holds, leave it out.

## Reference table: quick chooser

| You want to say... | Formal | Neutral | Informal |
|---|---|---|---|
| but | nevertheless / nonetheless | however / although | but / still |
| so | consequently / therefore | as a result / so | so |
| because | owing to / in view of | because of / due to / since | because / as |
| also | moreover / furthermore | in addition / also | plus / on top of that |
| for example | for instance / namely | such as / e.g. | like |
| in conclusion | in conclusion | overall | in short / bottom line |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| Hewings, *Advanced Grammar in Use* | book | Relative clauses, participle clauses, linking words with practice keys. | intermediate-advanced | paid |
| Michael Swan, *Practical English Usage* | book | Authoritative on *despite/although*, relative clause punctuation. | advanced | paid |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Transitions and cohesion in professional and academic writing. | intermediate | free |
| [BBC Learning English](https://www.bbc.co.uk/learningenglish) | site | Lessons on linkers and relative clauses. | intermediate | free |
| Joseph Williams & Bizup, *Style: Lessons in Clarity and Grace* | book | Cohesion via old-to-new information; better than any connector list. | advanced | paid |
| [Cambridge Dictionary grammar](https://dictionary.cambridge.org/) | reference | Short pages on *although/though/even though/despite* and non-defining clauses. | intermediate | free |
| [Google developer documentation style guide](https://developers.google.com/style) | style guide | Model of plain, well-linked technical prose. | intermediate | free |
| [English-Corpora.org (COCA)](https://www.english-corpora.org/coca/) :gem: | tool | Check how often *moreover* vs *also* occur in spoken vs academic text to calibrate register. | advanced | freemium |

## Hands-on lab (60 min)
1. **Connector census.** In a 500-word doc, list every connector and count. Which appear more than three times? Replace at least half of the *however/also/so* with more precise alternatives or with structure.
2. **Old-to-new rewrite.** Choose a paragraph whose sentences feel disconnected; rearrange so each sentence starts with what the previous sentence ended with.
3. **Relative-clause check.** Find every *which/that/who*; classify defining or non-defining; check commas and the *that/which* choice.
4. **Participle compression.** Take three pairs of short sentences and combine each with a participle clause; check the subject match. Then decide whether the combined version reads better.
5. **Speak it.** Explain a design decision aloud using *although, whereas, consequently, provided that* at least once each; record and check the grammar.

## Questions

### L1 - Recall

??? question "Q1. Which is correct: \"Despite of the delay\", \"Despite the delay\", \"In spite the delay\"?"
    ??? success "Answer"
        "Despite the delay" (or "In spite of the delay"). *Despite* takes no *of*; *in spite* needs *of*.

??? question "Q2. What is the difference between a defining and a non-defining relative clause? Which can use *that*?"
    ??? success "Answer"
        Defining clauses identify which noun is meant, take no commas, and can use *that* (or drop it for objects). Non-defining clauses add extra information, are set off by commas, and use *which/who* but never *that*.

??? question "Q3. Which linkers take a clause and which take a noun? although, despite, because, because of, whereas, due to."
    ??? success "Answer"
        Clause: although, because, whereas. Noun/-ing: despite, because of, due to.

??? question "Q4. Why is \"Having reviewed the RFC, the design was approved\" wrong?"
    ??? success "Answer"
        Dangling participle: the design did not review the RFC. Fix: "Having reviewed the RFC, we approved the design."

### L2 - Apply

??? question "Q5. Correct: \"Although the API is fast, but it is unreliable. Despite it is popular, we don't use it.\""
    ??? success "Answer"
        "Although the API is fast, it is unreliable." (no *but*); "Despite being popular, we don't use it" or "Although it is popular, we don't use it" (*despite* requires a noun/-ing, not a clause, unless "the fact that").

??? question "Q6. Punctuate and choose *that/which*: \"Our payment service ___ we built in 2015 ___ is being replaced. The tool ___ we need is not available.\""
    ??? success "Answer"
        "Our payment service, which we built in 2015, is being replaced." (non-defining: commas, *which*). "The tool (that) we need is not available." (defining: no commas, *that* or nothing).

??? question "Q7. Combine using a participle clause: \"We analysed the traces. We found the bottleneck.\" (a) with earlier action emphasis, (b) with simultaneous action."
    ??? success "Answer"
        (a) "Having analysed the traces, we found the bottleneck." (b) "Analysing the traces, we found the bottleneck." (The perfect form stresses that analysis was complete first.)

??? question "Q8. Choose the best connector: \"The vendor promised delivery in May. ___, it slipped to July.\" (however / therefore / moreover) and \"Kafka retains messages, ___ RabbitMQ deletes them after acknowledgment.\" (whereas / because / despite)."
    ??? success "Answer"
        However (contrast); whereas (comparison between two things).

### L3 - Judge and choose

??? question "Q9. \"Although it is expensive\" / \"Despite its cost\" / \"Even though it is expensive\" / \"Expensive though it is\": choose for an exec memo and defend."
    ??? success "Answer"
        For clarity and register: "Although it is expensive, we recommend..." or "Despite its cost, we recommend..." (more compact). *Even though* adds emphasis on the factual contrast; *Expensive though it is* is a rhetorical, slightly literary fronting. In a memo prefer the first two; keep the fronted form for speeches.

??? question "Q10. \"Since\" vs \"because\": what nuance and risk?"
    ??? success "Answer"
        *Because* introduces new/important information about cause; *since/as* present a reason the reader already knows. *Since* can be ambiguous (time vs reason): "Since we upgraded, latency has increased" (time or cause?). In technical causal claims, use *because* to avoid ambiguity.

??? question "Q11. A paragraph uses \"Moreover\", \"Furthermore\", \"In addition\" in consecutive sentences. Keep or cut?"
    ??? success "Answer"
        Cut most. Additive connectors in a row signal a list without structure. Restructure: "There are three benefits. First..., second..., third..." or combine with parallel structure. Keep at most one additive connector per paragraph unless it marks an important shift.

??? question "Q12. \"The reason is because...\" - error or acceptable?"
    ??? success "Answer"
        Common in speech but prescriptively redundant (*reason* and *because* both mean cause). Use "The reason is that..." or "This is because...". In a formal document, edit it.

### L4 - Real-world decisions

??? question "Q13. You must write a 3-sentence trade-off summary for a VP: microservices vs modular monolith. Use one concession, one contrast, one result connector, no filler."
    ??? success "Answer"
        "Although microservices allow teams to deploy independently, they add operational overhead that our five-person platform team cannot absorb. A modular monolith, by contrast, keeps deployment simple while still enforcing boundaries. Consequently, we recommend starting with the monolith and extracting services only when a boundary shows sustained deployment friction." Concession (*although*), contrast (*by contrast*), result (*consequently*); each connector encodes a logical relation the VP can follow.

??? question "Q14. A colleague's doc is correct but 'feels choppy'. What do you check first: connectors or something else?"
    ??? success "Answer"
        Old-to-new flow and consistent terminology first: check whether each sentence begins with something the previous one established. Connectors patch a lack of structure; fix the structure and then add the few connectors that mark real logical turns (contrast, cause, consequence).

??? question "Q15. In spoken English (interview, call), which linkers should you favour over the formal written ones?"
    ??? success "Answer"
        Simple, audible signposts: *so, but, because, though, anyway, that said, on top of that, the thing is, which means*. Formal *furthermore, nevertheless, consequently* sound stilted in speech. Signposts like "There are two reasons. First..." work better than dense subordination for listeners.

## Real-world use cases
- **Design-doc trade-offs:** *whereas, although, provided that*.
- **Postmortem causality:** *because, as a result, which meant*, careful about *since*.
- **Strategy memos:** *consequently, given that, nevertheless*.
- **RFC risks:** *unless, in case, failing that*.
- **Interviews:** *that said, on the other hand* for balanced answers.

## Pitfalls & anti-patterns
- *Despite/in spite* + clause, *despite of*.
- *Although ... but*, *because ... so*.
- Comma splice before *however/therefore*.
- *Which* referring vaguely to a whole sentence.
- Non-defining clause with *that*.
- Elegant variation of technical terms.
- Connector overload; every sentence starting with *However/Moreover*.
- Dangling participles.
- Using formal connectors in speech.

## Checklist
- [ ] I can pick the right linker for cause, contrast, concession, result and purpose, and I know each one's grammar.
- [ ] I can punctuate defining and non-defining relative clauses correctly.
- [ ] I can compress with participle clauses without dangling.
- [ ] I audited a document's connectors and improved cohesion via old-to-new order.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
