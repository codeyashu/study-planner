---
title: "Business & tech-leadership vocabulary"
track: communication
slug: business-tech-vocabulary
priority: P0
complexity: 3
est_hours: 3
phase: 1
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Business & tech-leadership vocabulary

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 3 h · **Phase:** 1 · **Prereqs:** none (pairs with [word nuance & register](word-nuance-register.md), [collocations & precision](collocations-precision.md))
    **You're done when:** you can use 40 of the 70 words below accurately in your own sentences about your work (not just recognise them), and you know the collocations and register of each.

## Why it matters
Vocabulary range is what separates "clear" from "authoritative". A Staff engineer is expected to name things precisely: *bottleneck* vs *constraint*, *mitigate* vs *resolve*, *mandate* vs *remit*, *dependency* vs *blocker*. The words below are the working vocabulary of design reviews, exec updates, strategy documents and interviews. They are grouped by **function** (what you want to *do* with language), not alphabetically, because you retrieve words by intent ("I want to say we reduced the risk"). Learn each word with its **collocations** and one example sentence from your own work; recognition is not enough.

## Core concepts

### How to learn a word properly (5 layers)
1. **Meaning** (in your own words, in English).
2. **Grammar** (verb pattern, countable/uncountable, prepositions: *mitigate the risk of*, *a mandate to*).
3. **Collocations** (what it goes with: *mitigate risk, mitigate impact*, not *mitigate a problem* as often).
4. **Register** (formal, neutral, informal; jargon; overused buzzword).
5. **Own sentence** about your current work; say it aloud.

**Buzzword warning.** Some words here (*leverage, synergy, ecosystem, disrupt, paradigm*) are so overused that many readers roll their eyes. Where a word carries that risk, the table says so and gives a plain alternative.

### A. Assessing and analysing (understanding a situation)

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| assess | verb | evaluate the quality, size or importance of something; more formal than *check* | "We assessed the blast radius before changing the schema." |
| evaluate | verb | judge the value of options against criteria | "We evaluated three vendors against six criteria." |
| scrutinise (US: scrutinize) | verb | examine very carefully | "The auditors scrutinised every access log." |
| diagnose | verb | identify the cause of a problem | "It took two days to diagnose the memory leak." |
| corroborate | verb | confirm with independent evidence | "The traces corroborate the customer's report." |
| substantiate | verb | provide evidence to support a claim | "You need data to substantiate that claim." |
| infer | verb | conclude from evidence (not stated directly) | "From the error pattern, we infer a race condition." (Note: *imply* = the speaker suggests; *infer* = the listener concludes.) |
| discern | verb | notice or recognise something subtle | "We couldn't discern a clear pattern in the failures." |
| ascertain | verb (formal) | find out for certain | "We must ascertain whether personal data was exposed." |
| baseline | noun/verb | a reference measurement for comparison | "Take a baseline before optimising." |
| root cause | noun | the fundamental reason a problem occurs | "The root cause was an expired certificate." |
| bottleneck | noun | the point that limits throughput | "The database is the bottleneck." |
| constraint | noun | a limiting condition (time, budget, technical) | "Regulatory constraints rule out that option." |
| trade-off | noun | a balance where gaining one thing costs another | "The trade-off is latency for consistency." |
| nuance | noun | a subtle difference | "The proposal misses a key nuance about data residency." |

### B. Acting and delivering (verbs of leadership)

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| champion | verb/noun | actively support and promote an idea | "She championed the move to trunk-based development." |
| spearhead | verb | lead an initiative from the front | "He spearheaded the migration." (mild cliché on CVs; fine) |
| orchestrate | verb | coordinate many moving parts | "We orchestrated a cutover across six teams." |
| streamline | verb | make more efficient by removing steps | "We streamlined the release checklist." |
| consolidate | verb | combine into one, strengthen | "We consolidated five log pipelines into one." |
| unblock | verb | remove an obstacle stopping work | "I unblocked the team by getting the access approved." |
| de-risk | verb | reduce the risk of a project | "A prototype de-risks the integration." |
| mitigate | verb | reduce the severity or likelihood of harm | "We mitigated the risk with a feature flag." (Mitigate *reduces*; it doesn't eliminate.) |
| remediate | verb (formal) | fix something wrong, esp. security/compliance | "We remediated all critical vulnerabilities." |
| escalate | verb | raise to a higher level of authority | "I escalated the vendor issue to the VP." |
| triage | verb/noun | prioritise problems by urgency | "We triage incoming bugs daily." |
| prioritise (US: prioritize) | verb | decide what is most important and do it first | "We prioritised reliability over new features." |
| sunset | verb | gradually retire a product/feature | "We will sunset the v1 API in June." |
| deprecate | verb | mark as obsolete and to be removed | "The endpoint is deprecated as of 2.0." |
| pivot | verb/noun | change strategy direction | "We pivoted from build to buy." |
| iterate | verb | improve through repeated cycles | "We iterated on the design after each review." |
| onboard | verb | bring a person/customer/team up to speed | "We onboarded three teams in Q2." |
| scale | verb/noun | grow capacity or extend a solution | "The design scales to 50k RPS." |
| ratify | verb (formal) | formally approve | "The architecture board ratified the standard." |

### C. Persuading and deciding

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| rationale | noun | the reasons behind a decision | "The rationale for the split is team autonomy." (Not *rationalization*.) |
| compelling | adjective | convincing, hard to resist | "We need a compelling case for the budget." |
| tangible | adjective | real, measurable | "The project must deliver tangible savings." |
| viable | adjective | workable, likely to succeed | "Option B is the only viable path." |
| feasible | adjective | technically or practically possible | "A rewrite is feasible but not desirable." |
| pragmatic | adjective | practical, focusing on what works | "A pragmatic approach is to ship the MVP." |
| robust | adjective | strong, able to cope with stress | "We need a more robust retry strategy." (Overused; be specific.) |
| endorse | verb | publicly support | "The CTO endorsed the plan." |
| advocate (for) | verb/noun | support strongly | "I advocated for a longer test phase." |
| buy-in | noun | agreement and commitment from stakeholders | "We need buy-in from Finance before we start." |
| alignment | noun | agreement on direction | "We have alignment on scope, not on timeline." |
| consensus | noun | general agreement | "We reached consensus after two reviews." (not "consensus of opinion", redundant) |
| contentious | adjective | likely to cause disagreement | "Ownership of the platform is contentious." |
| trade off / weigh up | verb phrase | compare pros and cons | "We weighed up cost against speed." |
| leverage | verb | use something to advantage (overused; often replace with *use*) | "We leveraged existing contracts to negotiate." |

### D. Strategy and organisation (nouns)

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| mandate | noun | official authority to act | "Our mandate is to reduce cloud spend by 20%." |
| remit | noun (mostly UK) | area of responsibility | "Security review is outside our remit." |
| accountable | adjective | answerable for outcomes (vs *responsible*: does the work) | "The VP is accountable for delivery." |
| stakeholder | noun | person with an interest in the outcome | "We mapped stakeholders before the launch." |
| governance | noun | how decisions are made and controlled | "Data governance defines who can access what." |
| roadmap | noun | plan of future work over time | "The roadmap shows three phases." |
| trajectory | noun | path or direction of development | "The growth trajectory is steep." |
| headwinds / tailwinds | noun | forces against / helping progress | "Budget freezes are a headwind." |
| runway | noun | time before resources run out | "We have nine months of runway." |
| footprint | noun | scale of resource/presence | "We reduced our cloud footprint." |
| ecosystem | noun | interconnected set of products/players (overused) | "The partner ecosystem is growing." |
| portfolio | noun | collection of projects/products | "We manage a portfolio of 40 services." |
| paradigm | noun | a model or typical pattern (formal, often overused) | "Event-driven is a different paradigm." |
| tenet / principle | noun | core belief | "One design tenet is loose coupling." |
| initiative | noun | a planned project or programme | "The reliability initiative covers three teams." |

### E. Risk, quality, and delivery

| Word | Part of speech | Meaning | Example |
|---|---|---|---|
| dependency | noun | something you rely on | "The main dependency is the identity service." |
| blocker | noun | something stopping progress | "Access is a blocker." |
| single point of failure (SPOF) | noun | one component whose failure stops everything | "The queue is a single point of failure." |
| blast radius | noun | the extent of damage from a failure | "Feature flags limit the blast radius." |
| resilience | noun | ability to recover from failure | "Resilience testing uncovered a gap." |
| technical debt | noun | cost of shortcuts that must be repaid | "We accepted technical debt to meet the date." |
| regression | noun | a change that breaks previously working behaviour | "The patch caused a regression in billing." |
| SLA / SLO | noun | agreement / internal target for service level | "Our SLO is 99.9% availability." |
| compliance | noun | conforming to rules or laws | "Compliance requires audit logs." |
| due diligence | noun | careful investigation before a decision | "We did due diligence on the vendor." |
| contingency | noun | a plan for a possible event | "We have a contingency for the vendor delay." |
| mitigation | noun | action that reduces a risk | "The mitigation is a rollback." |
| exposure | noun | degree of being subject to risk | "Our exposure to one vendor is high." |
| provision | verb/noun | set up resources; a condition in a contract | "We provisioned the cluster." |
| throughput / latency | noun | amount processed per time / delay | Precision pair; see [collocations](collocations-precision.md). |

### F. Precision with quantities and change (short list; see [collocations-precision](collocations-precision.md))
*marginal, substantial, negligible, significant (statistically vs generally), incremental, exponential (mathematical growth; do not use for "fast"), plateau, spike, dip, fluctuate, surge, taper off, order of magnitude.*

### G. Word families to master
Learn the whole family so you can use the form the sentence needs.

| Verb | Noun (thing/event) | Noun (person) | Adjective | Adverb |
|---|---|---|---|---|
| assess | assessment | assessor | assessable | - |
| mitigate | mitigation | - | mitigating | - |
| prioritise | priority, prioritisation | - | prior | - |
| escalate | escalation | - | escalated | - |
| decide | decision | decision-maker | decisive | decisively |
| ratify | ratification | - | - | - |
| advocate | advocacy | advocate | advocatory (rare) | - |
| consolidate | consolidation | - | consolidated | - |
| deprecate | deprecation | - | deprecated | - |
| accountable (adj) | accountability | - | accountable | accountably (rare) |

### H. Common confusions
- **Affect / effect:** *affect* (verb: influence); *effect* (noun: result; verb: *effect change* = bring about, formal).
- **Imply / infer:** the speaker implies; the listener infers.
- **Assure / ensure / insure:** *assure someone* (promise), *ensure* (make certain), *insure* (financial insurance). See [word nuance](word-nuance-register.md).
- **Comprise / compose / constitute:** the whole comprises the parts; the parts compose/constitute the whole. "The platform comprises six services" (not "is comprised of").
- **Principal / principle:** *principal* = main (or a school head); *principle* = a rule.
- **Complement / compliment.**
- **Discrete / discreet:** separate / careful about privacy.
- **Historic / historical:** important in history / of the past.
- **Sensitive / sensible.**
- **Economic / economical:** relating to economy / cost-saving.
- **Continual / continuous:** repeated / uninterrupted.
- **Disinterested / uninterested:** impartial / not interested.
- **Fewer / less:** see [articles & determiners](articles-determiners.md).

### Buzzword triage (use with care)
| Buzzword | Risk | Plain alternative |
|---|---|---|
| leverage (verb) | empty when overused | use, apply, take advantage of |
| synergy | vague | combined benefit |
| paradigm shift | grand | fundamental change |
| circle back | eye-roll in some cultures | follow up, come back to this |
| low-hanging fruit | fine but overused | quick wins |
| game changer | hype | significant change |
| holistic | vague | end-to-end, overall |
| robust | applied to everything | tolerant of failures, resistant to load (be specific) |
| scalable | needs a number | handles 10x load |
| actionable | fine in metrics | specific enough to act on |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/) | dictionary | Includes CEFR levels and Oxford 3000/5000 word lists; good for verifying meaning and grammar. | all | free |
| [Cambridge Dictionary](https://dictionary.cambridge.org/) | dictionary | Learner-focused definitions, example sentences, and a "business" tag on many entries. | intermediate | free |
| [Merriam-Webster](https://www.merriam-webster.com/) | dictionary | Usage notes on confusables (*comprise*, *infer*), American English. | intermediate-advanced | free |
| [Ozdic collocation dictionary](https://ozdic.com/) :gem: | dictionary | Shows what each word goes with; the fastest way to learn how to use it. | intermediate-advanced | free |
| [Macmillan Dictionary](https://www.macmillandictionary.com/) | dictionary | Clear definitions with frequency stars and business examples. | intermediate | free |
| Bill Mascull, *Business Vocabulary in Use (Advanced)* (Cambridge) | book | Structured business vocabulary with exercises and keys; check the current edition. | intermediate-advanced | paid |
| [BBC Learning English: *English at Work*](https://www.bbc.co.uk/learningenglish) | site | Workplace-scenario vocabulary in short episodes. | intermediate | free |
| [English-Corpora.org (COCA)](https://www.english-corpora.org/coca/) :gem: | tool | See real collocates and the frequency of each word in spoken/academic/business text. | advanced | freemium |
| [YouGlish](https://youglish.com/) | tool | Hear each word in context in real talks (search e.g. "mitigate"), useful for pronunciation. | all | freemium |
| Oxford Learner's Word Lists (Oxford 3000/5000) | list | Prioritises high-frequency words to avoid learning rare ones first. | intermediate | free |

## Hands-on lab (60 min plus ongoing)
1. **Diagnostic.** Highlight the 70 words above: green (I use it), yellow (I understand it), red (I don't know it). Count.
2. **Pick 10 yellows/reds.** For each, look up in Oxford or Cambridge; write the collocations (from Ozdic) and one sentence about your real work.
3. **Deck.** Create flashcards with a sentence gap (cloze) rather than word-definition pairs. Review daily.
4. **Recycle.** Write a 150-word update on your current project using at least eight target words.
5. **Speak.** Record a 90-second summary of a recent decision using at least six.
6. **Spaced review:** 1 day, 3 days, 7 days, 21 days.

## Questions

### L1 - Recall

??? question "Q1. What is the difference between *imply* and *infer*?"
    ??? success "Answer"
        The speaker or writer *implies* (suggests without saying directly); the listener or reader *infers* (draws a conclusion). "Her silence implied disapproval; I inferred that she disagreed."

??? question "Q2. Distinguish *responsible* and *accountable*."
    ??? success "Answer"
        *Responsible* = does the work; *accountable* = ultimately answerable for the outcome (one person). RACI models use both; in everyday speech people blur them, but at Staff level the difference is expected.

??? question "Q3. Which verb means to reduce the severity of a risk without eliminating it: *mitigate*, *eliminate*, *remediate*?"
    ??? success "Answer"
        *Mitigate*. *Eliminate* removes it; *remediate* fixes something that is already wrong (typically vulnerabilities/compliance issues).

??? question "Q4. What does \"the platform is comprised of six services\" get wrong, according to traditional usage?"
    ??? success "Answer"
        Traditionally, *comprise* means "to contain": "The platform comprises six services" (or "is composed of / consists of"). "Comprised of" is widespread and increasingly accepted, but editors still flag it in formal writing.

### L2 - Apply

??? question "Q5. Fill: assess / mitigate / escalate / corroborate / deprecate. (a) \"We need to ___ the impact before deciding.\" (b) \"A canary release helps ___ the risk.\" (c) \"The logs ___ the customer's timeline.\" (d) \"We will ___ the v1 API in June.\" (e) \"I ___ the issue to the VP.\""
    ??? success "Answer"
        (a) assess; (b) mitigate; (c) corroborate; (d) deprecate; (e) escalated.

??? question "Q6. Replace the buzzwords with precise language: \"We will leverage synergies across the ecosystem to drive a paradigm shift and deliver a robust, scalable solution.\""
    ??? success "Answer"
        "We will reuse the shared authentication and logging services so that each team ships features 30% faster, and we will design the platform to handle ten times today's traffic." Concrete nouns, numbers, no empty words. (Numbers are illustrative; in real writing, use your data.)

??? question "Q7. Complete with a word from the list: \"Our ___ is to reduce cloud costs by 20%, but headcount is outside our ___.\""
    ??? success "Answer"
        mandate; remit (or "scope"/"authority"). *Mandate* = authority to act; *remit* = area of responsibility.

??? question "Q8. Write one sentence for each: (a) a *trade-off*, (b) a *blast radius*, (c) *buy-in*, (d) *single point of failure*, all about your current system."
    ??? success "Answer"
        Model: (a) "The trade-off is between strict consistency and write latency." (b) "Per-tenant cells limit the blast radius to one customer." (c) "We need buy-in from the security team before we change the auth flow." (d) "The scheduler is currently a single point of failure." Check yours uses correct prepositions (*trade-off between X and Y*).

### L3 - Judge and choose

??? question "Q9. *Feasible*, *viable* and *practical*: choose for \"A full rewrite is technically ___ but not ___ given our team size.\""
    ??? success "Answer"
        "feasible ... viable" (or "practical"). *Feasible* = possible to do; *viable* = able to succeed in the real world (economic, organisational); *practical* = sensible in practice. The contrast between "can be done" and "makes sense" is the point.

??? question "Q10. In a design review, is \"robust\" a useful word? What do you write instead?"
    ??? success "Answer"
        It is vague unless qualified. Say *robust against what*: "tolerates a 30-second outage of the payment provider", "retries with exponential backoff and idempotency keys". Precise failure modes beat adjectives; use *robust* only after you have said what the robustness is.

??? question "Q11. \"Significant\" in a data update: when is it safe to use?"
    ??? success "Answer"
        Use *significant* for statistical significance when you have run a test, and add the measure (p-value or confidence interval) if the audience expects it. For general size, use a quantity ("a 12% reduction") or *substantial*, *notable*. Overusing *significant* invites the question "statistically or practically?".

??? question "Q12. \"We need alignment\" vs \"We need consensus\" vs \"We need buy-in\": how do the three differ?"
    ??? success "Answer"
        *Alignment*: shared understanding of direction and priorities (people may still disagree on details). *Consensus*: general agreement on a decision (nobody strongly objects). *Buy-in*: active commitment to support and carry out the decision. You can have alignment without buy-in ("we understand, but we won't staff it").

### L4 - Real-world decisions

??? question "Q13. You are writing a one-page memo to persuade a skeptical VP of Finance to fund tooling. Choose eight words from the lists and outline how they structure the argument."
    ??? success "Answer"
        Example: state the *baseline* (current cost and incident hours), name the *constraint* (headcount), present the *rationale* and *trade-off* (cost now vs risk later), quantify the *exposure* (revenue at risk), show a *pragmatic* phased option that *de-risks* delivery, give a *tangible* metric and a *contingency*, and ask for a *mandate* with a decision date. Each word carries a slot in the argument, which is the point of learning vocabulary by function.

??? question "Q14. A new joiner overuses \"leverage\" and \"synergy\" in updates and the team mocks it. How do you coach them?"
    ??? success "Answer"
        In a private 1:1, say that the ideas are good and the words are hiding them; ask for the concrete thing ("What exactly are we reusing?"). Offer three swaps (use, reuse, combined benefit) and show one rewritten sentence. Don't ridicule the vocabulary; explain that senior readers scan for specifics and treat buzzwords as a signal of vagueness.

??? question "Q15. In an interview, you want to sound precise but not pompous. How do you choose between *utilise/use*, *facilitate/help*, *commence/start*?"
    ??? success "Answer"
        Default to the plain word; formal words signal distance, not intelligence. Choose the formal word only if it adds precision (*remediate* vs *fix* for vulnerabilities) or matches a formal document type (contract, policy). In speech, the plain word is almost always better. The test: would a respected senior colleague say it aloud in a meeting?

## Real-world use cases
- **Design review:** *trade-off, constraint, bottleneck, blast radius, dependency*.
- **Exec update:** *mitigate, escalate, contingency, exposure, runway*.
- **Strategy doc:** *mandate, remit, trajectory, headwinds, rationale, portfolio*.
- **Vendor negotiation:** *due diligence, provision, compliance, leverage (concrete), concession* (see [negotiation](negotiation-and-saying-no.md)).
- **Interview:** *spearheaded, orchestrated, streamlined, championed* (used honestly and with numbers).

## Pitfalls & anti-patterns
- Learning words without collocations or prepositions.
- Using a word because it sounds senior, not because it fits (*utilise, leverage, holistic*).
- Confusing near-synonyms (*assure/ensure*, *imply/infer*, *affect/effect*, *comprise/compose*).
- Using *exponential* for "fast", *literally* for emphasis, *significant* without a test.
- Learning 100 words once instead of 5 words a day with review.
- Using new words only in writing; if you never say them aloud, they will not surface in meetings.

## Checklist
- [ ] I classified the 70 words red/yellow/green and made a plan for the reds.
- [ ] I wrote one real sentence for at least 40 words.
- [ ] I use ten of them in a real update or RFC this week.
- [ ] I can distinguish the confusable pairs in section H without notes.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
