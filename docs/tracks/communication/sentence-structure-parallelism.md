---
title: "Sentence structure & parallelism"
track: communication
slug: sentence-structure-parallelism
priority: P0
complexity: 3
est_hours: 2
phase: 2
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Sentence structure & parallelism

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 2 · **Prereqs:** [tenses & aspect](tenses-aspect.md) · **Pairs with:** [clauses & cohesion](clauses-and-cohesion.md), [concise writing & editing](concise-writing-editing.md)
    **You're done when:** you can diagnose and fix run-ons, fragments, dangling modifiers, misplaced modifiers and faulty parallelism in a 300-word draft, and you can restructure a sentence so its most important information lands at the end.

## Why it matters
Clear technical prose is mostly *sentence architecture*. Readers parse sentences left to right; every wrong turn (an ambiguous modifier, a list whose items do not match, a subject buried 25 words from its verb) costs attention. For a Staff engineer, whose documents are read by busy people across languages, structure is the difference between "I have to reread this" and "I got it in one pass". Fluent speakers' typical failures are not basic grammar but: very long sentences that follow spoken thought order, mismatched list items, and modifiers attached to the wrong noun.

## Core concepts

### The four sentence types
| Type | Structure | Example |
|---|---|---|
| Simple | one independent clause | "The cache expired." |
| Compound | two independent clauses joined by coordinating conjunction (FANBOYS: for, and, nor, but, or, yet, so), a semicolon, or a colon | "The cache expired, and the database saturated." |
| Complex | independent + dependent clause (because, although, when, if, which, who, that...) | "The database saturated because the cache expired." |
| Compound-complex | both | "The cache expired, and the database saturated because retries amplified the load." |

Variety matters: a run of simple sentences reads choppy; a run of compound-complex sentences reads dense. Mix; use the short sentence for the point you want remembered.

### Errors to fix

#### 1. Run-on and comma splice
A comma cannot join two independent clauses on its own.
- **Comma splice:** "The deploy failed, we rolled back." 
- **Fixes:** period ("The deploy failed. We rolled back."); semicolon ("...failed; we rolled back."); comma + conjunction ("...failed, so we rolled back."); subordinate ("Because the deploy failed, we rolled back."); dash/colon if the second explains the first.
- **Trap:** *however, therefore, moreover, consequently, thus, then* are adverbs, not conjunctions: "The fix worked, however it was slow" is a splice. Use "; however," or a period.

#### 2. Fragment
A group of words lacking a subject or finite verb, or a dependent clause standing alone: "Because the queue backed up." Fragments are acceptable in slides, bullet lists, headings and deliberate emphasis ("Result: 40% faster."), but not in the body of a formal document.

#### 3. Dangling modifier
An introductory participle or infinitive phrase must describe the **subject of the main clause**.
- **Wrong:** "After deploying the patch, the errors stopped." (Who deployed? The errors?)
- **Right:** "After we deployed the patch, the errors stopped." / "After deploying the patch, we saw the errors stop."
- **Wrong:** "To improve performance, the queries were rewritten." (Passive hides the agent; the infinitive implies *someone* wants to improve performance.) Better: "To improve performance, we rewrote the queries."
- **Test:** ask "Who is doing the action in the first phrase?" That noun must be the grammatical subject next.

#### 4. Misplaced modifier
Put modifiers next to what they modify. *Only, almost, just, even, nearly* are the classic ones.
- "We **only** support two regions" (only two? only support?): "We support only two regions."
- "The report **nearly** took three hours" (nearly took?) → "The report took nearly three hours."
- "The server with the bug that crashed": which crashed, the server or the bug? Rewrite: "The server that crashed had a bug."

#### 5. Ambiguous pronoun reference
"When the service calls the gateway, it times out." (it = service or gateway?) Repeat the noun or restructure: "When the service calls the gateway, the gateway times out."
- *This/that/which* referring to a whole previous clause is vague: "The build failed. This caused delays." Add a noun: "This failure caused delays."

#### 6. Subject-verb agreement
- Match the verb to the head noun, not the nearest noun: "**The list of dependencies** *is* long."
- *A number of* + plural verb; *the number of* + singular verb.
- *Data:* accepted both ways; choose one and stay consistent.
- *Each/every/one of* + singular verb: "Each of the services *has* a dashboard." 
- Compound subject with *and* = plural; with *or/nor* verb agrees with the nearer noun: "Neither the client nor the servers *were* ready."
- Collective nouns (*team, staff, committee*): US usually singular ("The team is"), UK often plural ("The team are"). Stay consistent.
- *Either/neither of* + plural noun; verb singular in formal writing.

### Parallelism: the core principle
Items in a list, a comparison or a series of clauses must have the **same grammatical form**.

**Faulty:** "The role involves designing systems, to mentor engineers, and stakeholder management."
**Parallel:** "The role involves designing systems, mentoring engineers, and managing stakeholders." (all *-ing*)

Where parallelism is required:

| Context | Broken | Fixed |
|---|---|---|
| Lists after a verb | "She is responsible for planning, deploy, and monitoring." | "...planning, deploying and monitoring." |
| Bullets under one heading | "- Reduce latency / - Improvement of reliability / - We will cut cost" | "- Reduce latency / - Improve reliability / - Cut cost" (all imperative) |
| Correlative pairs (both...and, either...or, neither...nor, not only...but also, whether...or) | "We can either optimise the query or to add an index." | "We can either optimise the query or add an index." (same form after *either* and *or*) |
| Comparisons | "Reading logs is slower than to query metrics." | "Reading logs is slower than querying metrics." |
| Repeated clauses | "The design is scalable, has good resilience, and cheap." | "The design is scalable, resilient and cheap." |
| Headings and table cells | "Rollout plan / Risks that exist / Timeline" | "Rollout plan / Risks / Timeline" |

**Correlatives:** the word after each half must be the same part of speech: "not only **reduces** cost but also **improves** reliability" (verb / verb), not "not only reduces cost but also reliability".

**Parallelism for rhetoric:** the triad ("faster, cheaper, safer"), antithesis ("It is not a tool problem; it is a trust problem"), and anaphora ("We will... We will...") depend on parallelism. See [rhetorical devices](storytelling-and-persuasion.md).

**Parallel bullets checklist:** same grammar (all verbs or all noun phrases), same length band (approx.), same level of detail, punctuation consistent (full stops on all or none).

### Word order and emphasis in English

English is SVO with fixed placement rules.

- **Adverbs of frequency** go before the main verb, after *be*: "We *rarely* deploy on Fridays" / "It is *often* slow." Not "We deploy rarely on Fridays" (acceptable but marked).
- **Adverbs of manner/place/time** normally end-of-sentence, in order manner-place-time: "We shipped it *carefully in Rotterdam last week*." Never between verb and its direct object: "We finished *quickly* the migration" → "We finished the migration quickly."
- **Object placement:** "explain *it* to me", "send *him* the report", "give the report *to the client*".
- **Questions:** inversion or auxiliary do: "Why did you choose Kafka?" (not "Why you chose"). **Indirect questions** use statement order: "I wonder why *we chose* Kafka." "Can you tell me *what the risk is*?" (not "what is the risk").
- **Time and place at the front for framing:** "In Q3, we will migrate..." (comma after introductory phrase longer than a few words).

### End-weight and information structure
- **Given before new:** start with what the reader already knows (the topic); end with the new information. "The migration is complete. **It cut latency by 40%.**"
- **End-weight principle:** English places heavy, important information at the end of a sentence (the *stress position*). Compare "Latency dropped 40% because of the cache" vs "Because of the cache, latency dropped 40%": the second ends on the result, the first on the cause. Choose by what you want remembered.
- **Front-load the subject and verb:** the reader needs the action early. Avoid long introductory clauses (the "front-loaded sentence").
- **Subject-verb distance:** keep it under ~10 words. "The service, which was created three years ago by a team that has since been reorganised and which nobody fully understands, fails" - move the interruption: "The service fails. It was created three years ago by a team that has since been reorganised, and nobody fully understands it."
- **Old-to-new chain:** the end of sentence 1 becomes the subject of sentence 2 ("...a new **cache**. **The cache** reduces..."): the most powerful cohesion device (see [clauses and cohesion](clauses-and-cohesion.md)).

### Sentence length
- Median: 15-20 words for technical prose; anything over 30 needs a reason.
- Long sentences are fine if the structure is transparent (list, parallelism, stepwise).
- Spoken thought order is *not* good written order. In writing, put the conclusion first (BLUF: bottom line up front).

### Cleft sentences and fronting (for emphasis; see also [active/passive & emphasis](active-passive-emphasis.md))
- **It-cleft:** "It was the retry storm that caused the outage."
- **Wh-cleft:** "What we need is a clear owner."
- **Fronting:** "Rarely have I seen a cleaner design." (inversion)

### Quick diagnostic for a messy sentence
1. Find the **subject** and **main verb**. Are they close? Is the subject a real actor?
2. Circle each **modifier**. Is it next to what it modifies?
3. Find **lists**. Are the items parallel?
4. Check the **end**: is the most important information there?
5. If the sentence has more than one idea, **split it**.

## Reference table: fixes at a glance

| Problem | Symptom | Fix |
|---|---|---|
| Run-on/comma splice | two full clauses joined by a comma | period, semicolon, conjunction, subordinate |
| Fragment | no finite verb, or stray "because..." | attach or complete |
| Dangling modifier | opening -ing/to phrase with wrong subject | rename subject or rewrite phrase |
| Misplaced modifier | *only/almost* in wrong place | move next to target |
| Faulty parallelism | mixed forms in list/correlative | force one form |
| Pronoun ambiguity | *it/this/they* with two candidates | repeat noun |
| Buried point | conclusion at the end of a long build-up | BLUF, split |
| Subject-verb distance | long interruption | move or split |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| Joseph Williams & Joseph Bizup, *Style: Lessons in Clarity and Grace* | book | The best book on sentence structure for expository writing; explains "old before new" and "end weight". | advanced | paid |
| Steven Pinker, *The Sense of Style* | book | Cognitive-science view of clear prose, parsing and the "curse of knowledge". | advanced | paid |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Parallelism, modifiers, fragments and run-ons pages with exercises. | intermediate | free |
| [Google developer documentation style guide](https://developers.google.com/style) | style guide | Sentence-level guidance for technical documentation (short sentences, parallel lists). | intermediate | free |
| [Plain Language guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/) | guide | Practical rules on sentence length, active voice, front-loading. | intermediate | free |
| [Grammarly blog](https://www.grammarly.com/blog/) | articles | Accessible explanations of dangling modifiers and comma splices. | beginner-intermediate | free |
| Strunk & White, *The Elements of Style* | book | Short, opinionated; use as a prompt, not as gospel (some rules are dated). | intermediate | paid |
| [Cambridge Dictionary grammar](https://dictionary.cambridge.org/) | reference | Word-order and inversion entries for learners. | intermediate | free |
| The *Economist* Style Guide :gem: | book | Compact rules for short, direct sentences in business writing. | intermediate-advanced | paid |

## Hands-on lab (60 min)
1. Take 500 words of your own doc. Highlight the five longest sentences. Split or restructure each; compute average sentence length before and after.
2. Find every list (inline and bulleted). Check parallel form and make each list uniform.
3. Search for *-ing* sentence openers and *to* openers; check each subject with the "Who?" test.
4. Search for *it/this/they/which* at sentence start; make each reference explicit.
5. Rewrite one paragraph in given-before-new order and end-weight the key facts.
6. Read the result aloud; where you breathe unnaturally, the sentence is too long.

## Questions

### L1 - Recall

??? question "Q1. What is a comma splice, and name three ways to fix one."
    ??? success "Answer"
        Two independent clauses joined by only a comma ("The test failed, we rolled back"). Fixes: full stop; semicolon; comma + coordinating conjunction ("..., so we rolled back"); subordinate clause ("Because the test failed, we rolled back"); colon/dash for explanation.

??? question "Q2. What is a dangling modifier? Give an example and a fix."
    ??? success "Answer"
        An opening modifier whose implied subject differs from the main clause's subject: "After deploying the patch, the errors stopped." Fix: "After we deployed the patch, the errors stopped."

??? question "Q3. State the rule of parallelism in one sentence."
    ??? success "Answer"
        Elements that serve the same function in a list, comparison or correlative pair must have the same grammatical form.

??? question "Q4. Where do frequency adverbs (always, rarely, often) go?"
    ??? success "Answer"
        Before the main verb and after *be* or the first auxiliary: "We rarely deploy", "It is often slow", "We have never seen this."

### L2 - Apply

??? question "Q5. Fix the parallelism: \"Our goals: improving latency, to reduce cost, and reliability should be higher.\""
    ??? success "Answer"
        "Our goals: improve latency, reduce cost, and increase reliability." All three are imperative verb phrases. (Alternative: "improving latency, reducing cost and increasing reliability".)

??? question "Q6. Fix: \"The service can not only scale horizontally but also it is cheap to run.\""
    ??? success "Answer"
        "The service can not only scale horizontally but also run cheaply." (or "is not only scalable but also cheap"). After *not only* and *but also* the same form is needed (verb phrase / verb phrase).

??? question "Q7. Repair the dangling modifier and comma splice: \"Reviewing the logs, the root cause was found, it was a stale certificate.\""
    ??? success "Answer"
        "Reviewing the logs, we found the root cause: a stale certificate." (Subject *we* now matches the participle; the splice becomes a colon.)

??? question "Q8. Make unambiguous: \"When the client calls the proxy, it fails.\" (Assume the proxy fails.)"
    ??? success "Answer"
        "When the client calls the proxy, the proxy fails." Repeat the noun when a pronoun has two possible referents. If the client fails, say "the client fails".

### L3 - Judge and choose

??? question "Q9. \"Latency dropped 40% because of the cache\" vs \"Because of the cache, latency dropped 40%\": which do you use for an exec update where the win is the cache design, and which where the win is the number?"
    ??? success "Answer"
        End-weight: what you want remembered goes last. If the key message is the cache decision, end on it: "Latency dropped 40% because of the new cache." If the number is the headline, front the cause and end on the number: "Thanks to the new cache, latency dropped 40%." Both grammatical; choose by emphasis.

??? question "Q10. A colleague uses a 45-word sentence in an RFC with a nested relative clause. Split it or keep it? Explain your criteria."
    ??? success "Answer"
        Split unless the structure is a simple parallel list. Criteria: subject-verb distance under ~10 words, one idea per sentence, readers with different first languages, and consequential claims that must not be misread. A long parallel list of requirements can stay in one sentence but might be better as bullets.

??? question "Q11. Are sentence fragments always wrong? Where are they appropriate?"
    ??? success "Answer"
        No. They are appropriate in bullets, headings, slide text, emphasis ("Big win: fewer pages."), Slack and ticket titles. They are inappropriate in the body of a formal document because readers may not know what the missing subject/verb is. Deliberate fragments should be rare and obviously intentional.

??? question "Q12. \"The team are\" vs \"The team is\": which do you choose?"
    ??? success "Answer"
        In American English *team* takes a singular verb by default (the group as a unit); British English allows plural (the members as individuals). Both are grammatical; the rule is consistency with your audience and within one document. Use plural if the sentence focuses on individuals ("The team are divided"), singular otherwise.

### L4 - Real-world decisions

??? question "Q13. You must edit a peer's 4-page design doc in 30 minutes. What sentence-level issues do you prioritise?"
    ??? success "Answer"
        (1) The summary and headline sentences: ensure conclusion first, short sentences. (2) Parallelism in requirement lists and headings, since these are scanned. (3) Ambiguous pronouns and dangling modifiers in critical claims (decisions, risks). (4) Long sentences with buried subjects in the decision section. Skip cosmetic fixes that do not change readability. Provide 3 patterns and 2 examples rather than marking every sentence.

??? question "Q14. A director complains that your updates are \"hard to follow\" though the grammar is correct. Diagnose likely structure issues."
    ??? success "Answer"
        Likely: spoken thought order (context first, conclusion last), long sentences with front-loaded subordinate clauses, key numbers buried mid-sentence, unparallel bullets, and vague *this/it* references. Fix: BLUF (conclusion first), one idea per sentence, key facts in end position, parallel bullets, explicit nouns.

??? question "Q15. You are writing acceptance criteria for a ticket that non-native engineers in three countries will implement. What sentence structure rules apply?"
    ??? success "Answer"
        Short sentences, one requirement per sentence, subject-first, active voice, parallel bullets, explicit nouns rather than pronouns, one modal only (*must* for requirements, *should* for recommendations, *may* for options, defined once), no idioms or ambiguous modifiers ("only", "almost"), and examples with inputs and outputs. This maximises unambiguous parsing for all readers.

## Real-world use cases
- **RFC summaries.** One-sentence problem, one-sentence proposal, one-sentence ask, each parallel in structure.
- **Runbooks.** Imperative, parallel steps ("Check the queue depth. Restart the consumer. Verify lag drops below 100.").
- **Interview answers.** Spoken sentences should be *shorter* and more parallel than written ones: triads and contrasts are easy to follow by ear.
- **Slack incident updates.** Fragment-style headings with full-sentence details.
- **Contracts and SLAs.** Precision about *only/at least/no later than* positions (misplaced modifiers become disputes).

## Pitfalls & anti-patterns
- Comma before *however* used as a conjunction.
- Opening every sentence with *-ing* phrases or "By doing X, ..." (dangling risk).
- Long, mixed-form bullet lists.
- Using *this* without a noun.
- Hiding the actor behind nominalisations (see [active vs passive](active-passive-emphasis.md)).
- Over-splitting into staccato sentences, or over-joining with semicolons.
- Placing *only* by habit at the start instead of before the word it modifies.
- Front-loading with a 20-word subordinate clause.

## Checklist
- [ ] I can identify and fix comma splices, fragments, dangling and misplaced modifiers.
- [ ] I can produce parallel lists, bullets and correlative pairs without hesitation.
- [ ] I apply given-before-new and end-weight to my summaries.
- [ ] I audited five long sentences in my own document and split or restructured them.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
