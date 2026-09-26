---
title: "Active vs passive voice, inversion & emphasis"
track: communication
slug: active-passive-emphasis
priority: P1
complexity: 4
est_hours: 2
phase: 3
tags: [communication, P1]
last_reviewed: 2026-09-25
---

# Active vs passive voice, inversion & emphasis

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 4/5 · **Est. time:** 2 h · **Phase:** 3 · **Prereqs:** [sentence structure & parallelism](sentence-structure-parallelism.md)
    **You're done when:** you can choose active or passive on purpose (agent, focus, blame, register), form every passive variant correctly, and use cleft, fronting and inversion for emphasis without sounding theatrical.

## Why it matters
"Mistakes were made" is the sentence everyone remembers as evasive; "We deployed the change without a canary" is the sentence a blameless postmortem needs. Passive is neither bad nor good: it is a **focus and responsibility tool**. Staff engineers write incident reports, risk statements, requirements and strategy where the choice signals ownership, precision and tone. Emphasis structures (clefts, inversion) let you land the key idea in speech and writing, in a language where word order is nearly fixed.

## Core concepts

### Forming the passive
`be + past participle` (agent optional, with *by*). Tense is carried by *be*.

| Tense | Active | Passive |
|---|---|---|
| Present simple | The team reviews PRs. | PRs are reviewed (by the team). |
| Present continuous | We are migrating the DB. | The DB is being migrated. |
| Past simple | They deployed the patch. | The patch was deployed. |
| Past continuous | They were testing it. | It was being tested. |
| Present perfect | We have fixed the bug. | The bug has been fixed. |
| Past perfect | We had approved it. | It had been approved. |
| Future | We will release it. | It will be released. |
| Modal | We must review it. | It must be reviewed. |
| Modal perfect | We should have tested it. | It should have been tested. |
| Infinitive | We want to fix it. | We want it to be fixed. / It needs to be fixed. |
| -ing | We resent being asked. | She avoided being blamed. |

**Only transitive verbs** (verbs with a direct object) can be passivised. Intransitive verbs cannot: "The outage was happened" is wrong (*happen, occur, exist, arrive, fall, remain, seem, become*). Also not passivised: *have* (possession), *resemble, fit, suit* in the stative sense.

**The get-passive** is informal and often signals an unfortunate or unplanned event: "The service got hit by a spike", "We got paged at 3 a.m." Avoid in formal documents.

**Indirect-object passives:** "I was given the access" (person as subject) is more natural than "The access was given to me" or "It was given me". *Told, asked, offered, shown, sent* also take a personal subject: "We were told to wait."

**Passive with reporting verbs (impersonal):** "It is said/believed/expected/reported that..." or "X is said/believed to..." - "The vendor is expected to respond by Friday." Formal, hides source; use it when the source is unimportant or you cannot name it.

**Causative:** *have/get + object + past participle*: "We had the audit completed by an external firm." "I'll get the report reviewed."

### When to use the passive (legitimately)

| Reason | Example |
|---|---|
| The actor is unknown | "The credentials were leaked." |
| The actor is obvious or irrelevant | "Customers were notified." (by the support team, clear from the context) |
| The **receiver** is the topic (given information) | "Our payment service is used by 40 teams." (cf. topic continuity) |
| Systems and processes (methods, runbooks, specs) | "The logs are shipped to Loki and retained for 30 days." |
| Blameless analysis (system focus, not person focus) | "The configuration was changed without review": a system gap, not an accusation. |
| Diplomatic distance | "Mistakes were made in the estimation" (careful: see below) |
| Formal/legal register | "Payment shall be made within 30 days." |
| Long agent, short receiver (end-weight) | "The system was designed by a team that no longer exists." |

### When to prefer the active

| Reason | Example |
|---|---|
| The actor matters and is known | Instead of "It was decided to cancel the project": "The steering committee decided to cancel the project." |
| Ownership and accountability | "We missed the deadline" (not "The deadline was missed") |
| Shorter and more direct | Active is typically 20-30% shorter. |
| Instructions | "Restart the service" (imperative) |
| Executive updates and commitments | "I will deliver the plan on Friday." (not "The plan will be delivered") |

**"Mistakes were made" problem:** When the passive dodges responsibility in a context where the audience expects ownership (customer apology, exec summary of a failure), it reads as evasive. Balance: "We deployed a configuration change without review. Our process allowed this. We have added a mandatory review gate." Blameless does not mean agentless; it means you attribute cause to the *process and system*, but you can still say "we".

### Passive detectors and traps
- **The "by zombies" test:** if you can add "by zombies" after the verb and the sentence still parses, it is passive ("The bug was fixed by zombies").
- **Nominalisation + weak verb** hides the agent too: "There was a failure of the cache" vs "The cache failed"; "The implementation of the fix was carried out" vs "We implemented the fix."
- **Adjectival participles** are not real passives: "The system is *broken*", "We are *concerned*", "The team is *motivated*" are state descriptions.
- **Passive with intransitives (error)**, **double passive (error)**: "It was decided to be cancelled".
- **Mixed voice in a list** breaks parallelism: "We tested, deployed, and the results were monitored" → "We tested, deployed and monitored."
- **Scientific writing** conventionally uses passive for methods; modern guides (Purdue OWL, IEEE-style, many corporate style guides) allow active first person. Follow the target style guide.

### Inversion: form and use
Inversion = auxiliary/verb before subject. English uses it for questions, and for **emphasis after negative or restrictive adverbials at the front of a sentence** (formal, written, or a deliberate rhetorical register).

| Trigger | Pattern | Example |
|---|---|---|
| Never / rarely / seldom / hardly ever | Adverb + aux + S + verb | "Never have we seen such a spike." |
| Not only ... but also | Not only + aux + S + V | "Not only did the change increase latency, but it also broke the SLA." |
| No sooner ... than / Hardly ... when | Had + S + p.p. | "No sooner had we deployed than the alerts fired." |
| Only + adverbial | Only + adverbial + aux + S | "Only after the audit did we find the gap." "Only when latency exceeds 200 ms does the circuit open." |
| Under no circumstances / at no time / in no way | + aux + S | "Under no circumstances should credentials be shared." |
| Little / scarcely | | "Little did we know that the fix would cause a second outage." |
| So + adj / Such + be | So + adj + aux + S + that | "So severe was the impact that we invoked the DR plan." |
| Conditional inversion | Should / Had / Were + S | "Should you need help, contact SRE." "Had we tested, we'd have caught it." "Were we to delay, costs would rise." |
| Fronted directional/locative + be/verb | "Here comes the report", "Attached is the spec", "Included in the pack are three scenarios." |

**Rules**
- Use an auxiliary; if none exists, insert *do/does/did*.
- Inversion is *not* used in the subordinate clause after a normal negative: "I never realised that it failed."
- "Not until" needs inversion in the main clause: "Not until Monday did we notice." 
- **Register:** formal/dramatic. Use in speeches, RFC intros, executive narratives sparingly (one per page at most). In casual talk it sounds pompous.

### Emphasis structures

| Structure | Pattern | Example | Use |
|---|---|---|---|
| **It-cleft** | It is/was + X + that/who... | "It was the retry logic that caused the outage." | Correct an assumption, isolate the key element. |
| **Wh-cleft (pseudo-cleft)** | What + S + V + is/was + X | "What we need is a single owner." | Introduce the key point after a set-up. |
| **Reverse wh-cleft** | X + is what... | "A single owner is what we need." | |
| **All-cleft** | All (that) + S + V + is + X | "All we ask is a decision by Friday." | Minimise/limit. |
| **Fronting** | Object/complement to the front | "This risk we can accept; that one we cannot." | Contrast. |
| **Do-emphasis** | do/does/did + base | "I *do* understand the concern, but..." | Concessive, polite disagreement. |
| **Existential there** | There + be + N | "There is a risk that..." | Introduce new information (but prefer a real subject when possible). |
| **Emphatic reflexives / own** | "We ourselves", "our very own" | | Sparingly. |
| **Intensifiers** | very, really, extremely, deeply, genuinely | | Prefer strong words (*critical* not *very important*). |
| **Stress in speech** | Nuclear stress on the key word | "I didn't say **he** was late." | See [pronunciation](pronunciation-stress-intonation.md). |

**Where emphasis belongs:** the end of the sentence (natural stress position). Then the beginning. Middle is weak. Use clefts when the normal order would bury the key element.

**Example transformation:** "The lack of a rollback plan caused the extended outage." → "What turned a 5-minute fault into a 2-hour outage was the lack of a rollback plan."

### Other emphasis and information devices
- **Contrast pair:** "not X but Y" ("This is not a tooling problem but an ownership problem.")
- **Short sentence after long:** "We tried three fixes over two weeks; none worked. The reason: we were fixing a symptom."
- **Italics/bold in writing:** minimal; do not stack.
- **Parenthetical and dashes** for asides; not for essentials.
- **Repetition** (anaphora) in speech.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| Joseph Williams & Bizup, *Style: Lessons in Clarity and Grace* | book | Best treatment of agent/action and when passive helps cohesion. | advanced | paid |
| Steven Pinker, *The Sense of Style* | book | Chapter explaining when the passive is right (given-new, topic continuity), correcting the "never use passive" myth. | advanced | paid |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Active/passive voice handouts with revision exercises. | intermediate | free |
| [Google developer documentation style guide](https://developers.google.com/style) | style guide | Its "Active voice" guidance is a good model for technical docs, including when passive is okay. | intermediate | free |
| [Plain Language guidelines](https://www.plainlanguage.gov/) | guide | Advises active voice for clear government and business writing; examples of before/after. | intermediate | free |
| Hewings, *Advanced Grammar in Use* | book | Passive forms, cleft sentences and inversion units with exercises and keys. | advanced | paid |
| Michael Swan, *Practical English Usage* | book | Entries on passive, inversion, emphasis. | advanced | paid |
| [Grammarly blog](https://www.grammarly.com/blog/) | articles | Approachable overview of passive vs active; use with caution because its detectors over-flag. | beginner-intermediate | free |
| [Cambridge Dictionary grammar](https://dictionary.cambridge.org/) | reference | Concise pages on passives, cleft sentences and inversion for learners. | intermediate | free |

## Hands-on lab (45-60 min)
1. **Voice audit.** Highlight all passives in a 500-word incident report or RFC. For each, label: (a) agent unknown/irrelevant, (b) system focus (good), (c) evasive (rewrite), (d) weak (nominalisation, rewrite).
2. **Ownership rewrite.** Rewrite an exec update so that every commitment, decision and risk owner is active.
3. **Emphasis practice.** For five key sentences in a strategy doc, create one cleft version. Keep the one that reads naturally and delete the rest (one cleft per page is plenty).
4. **Inversion set.** Write three formal inversions about your project ("Only after ... did we ..."). Then decide which one you would actually put in a document (usually none, or one).
5. **Speak it.** Record yourself giving the 30-second summary of your project using one cleft ("What we learned is...").

## Questions

### L1 - Recall

??? question "Q1. Form the passive: (a) \"The team has approved the design\" (b) \"They must be testing it\" (c) \"We should have reviewed the change.\""
    ??? success "Answer"
        (a) The design has been approved (by the team). (b) It must be being tested. (c) The change should have been reviewed. The passive always keeps the same tense/modal on *be* and changes the verb to a past participle.

??? question "Q2. Why is \"The outage was occurred at 09:12\" wrong?"
    ??? success "Answer"
        *Occur* is intransitive (no direct object), so it cannot be passivised. Correct: "The outage occurred at 09:12."

??? question "Q3. Give three legitimate reasons to use the passive."
    ??? success "Answer"
        Actor unknown or irrelevant ("The key was leaked"), focus on the receiver/topic continuity ("The service is used by 40 teams"), system/process description or blameless focus ("Logs are retained for 30 days"), and formal/legal register ("Payment shall be made...").

??? question "Q4. Invert: \"We rarely see this pattern in production.\" Start with \"Rarely\"."
    ??? success "Answer"
        "Rarely do we see this pattern in production." The adverb triggers auxiliary inversion (*do* is inserted because the original had no auxiliary).

### L2 - Apply

??? question "Q5. Rewrite in the active and name what improved: \"It was decided by the leadership team that the migration would be postponed, and stakeholders will be informed.\""
    ??? success "Answer"
        "The leadership team decided to postpone the migration, and I will inform stakeholders." Shorter (about half), names the decision-makers, and states who will act. If the decision-maker should be anonymous, "The migration has been postponed" is fine.

??? question "Q6. Rewrite to blameless-but-accountable: \"John pushed a bad config and broke production.\""
    ??? success "Answer"
        "A configuration change went to production without validation, which caused the outage. Our pipeline allowed the change without review; we have added a validation step." The passive/system focus moves attention to the control gap; adding "we" preserves accountability.

??? question "Q7. Change into a cleft sentence to emphasise the cause: \"A missing index caused the slow queries.\""
    ??? success "Answer"
        "It was a missing index that caused the slow queries." or "What caused the slow queries was a missing index." The first isolates the cause; the second creates suspense before the answer.

??? question "Q8. Correct: \"Not only the change increased latency but also it broke the SLA. Only after the audit we discovered the gap.\""
    ??? success "Answer"
        "Not only **did the change increase** latency, but it also broke the SLA. Only after the audit **did we discover** the gap." After *not only* and *only + adverbial* at the start, the auxiliary precedes the subject.

### L3 - Judge and choose

??? question "Q9. \"Mistakes were made.\" Is this passive always wrong in a postmortem? Decide and defend."
    ??? success "Answer"
        On its own it is evasive because it names neither the mistakes nor an owner, and it has become a byword for dodging. In a postmortem, use passive to focus on systems ("The change was deployed without a canary") but pair it with specifics and an ownership statement ("We did not have a canary policy. We own that.") The rule: passive to remove blame from individuals, never to remove accountability from the organisation.

??? question "Q10. Pinker and Williams both argue that \"never use the passive\" is bad advice. When does the passive produce a better paragraph?"
    ??? success "Answer"
        When it keeps the topic (the receiver) in subject position across sentences ("Our billing service handles 10M requests a day. It is called by every checkout flow."), when it moves long or new agents to the end ("The bug was found by a customer in Brazil who..."), and when the agent is unknown. The active is a default, not a law.

??? question "Q11. Inversion in a customer-facing RFC intro: \"Never before have we had the chance to...\" Good or bad?"
    ??? success "Answer"
        Probably bad. Formal negative inversion sounds rhetorical and stiff in technical documents; it draws attention to the writer's style. In a keynote or an all-hands speech it can work once. Choose a plain sentence for docs: "This is the first time we can...".

??? question "Q12. \"What we need is a decision\" vs \"We need a decision\": when is the cleft worth it?"
    ??? success "Answer"
        When the sentence follows a long discussion of options and you want the audience to focus on a single ask; the cleft creates a beat of anticipation. For routine requests the plain form is better, since overuse turns emphasis into noise.

### L4 - Real-world decisions

??? question "Q13. You are the on-call lead writing the customer-facing incident summary for a major client after your team's mistake. Choose voice for the key sentences."
    ??? success "Answer"
        Active and specific for the ownership statement: "We deployed a change that we had not adequately tested, and it disrupted your bookings for 47 minutes. We apologise." Passive for the technical description where the actor doesn't matter ("Bookings were queued and no data was lost"). Avoid "Mistakes were made" and avoid naming individuals. Use active *we* for what we are doing now: "We are adding automated checks".

??? question "Q14. A colleague argues: \"Our company style guide says never use passive.\" You disagree in a review. Draft a short, evidence-based reply."
    ??? success "Answer"
        "I agree active is the default, and I've changed the sentences where the actor matters. For these three, though, the passive keeps the topic in subject position (or the actor is irrelevant), and the active versions add words without adding information. The Google developer documentation style guide also allows passive when the actor is unimportant. Happy to change them if you feel strongly." It concedes the default, points to a specific reason and a reputable source, and keeps the tone collaborative.

??? question "Q15. In a promotion packet, your peers use passive: \"The platform was redesigned and adoption was increased.\" How would you coach them to write ownership without sounding arrogant?"
    ??? success "Answer"
        Use accurate active verbs that match the level of contribution: "I led the redesign of the platform and worked with three teams to raise adoption from 12 to 40". Distinguish sole ownership (*I designed*) from shared (*we*, *I contributed to*, *I drove*). Passive hides the agent, which committees read as either inflated or vague. Numbers plus a precise verb signal confidence without boasting.

## Real-world use cases
- **Postmortems:** agent-neutral timelines, explicit ownership of remediation.
- **Runbooks and READMEs:** imperatives, passives for state ("The cache is populated at start-up").
- **Security advisories and legal text:** formal passive and *shall*.
- **Executive updates:** active commitments, passive for facts about systems.
- **Keynotes and interviews:** clefts ("What I learned is...") and occasional inversion for a memorable line.

## Pitfalls & anti-patterns
- Evasive passive ("It was decided", "Mistakes were made").
- Passivising intransitives (*was happened, was arrived*).
- Tense errors inside the passive (*has been finished yesterday*).
- Mixed voices within a list.
- Overusing inversion or clefts; the effect disappears.
- Applying "avoid the passive" mechanically, producing awkward "we" chains.
- Nominalisations pretending to be active ("There was a discussion about").
- *Get*-passives in formal writing.

## Checklist
- [ ] I can form passives across all tenses and modals.
- [ ] I can justify the choice of voice in each sentence of an incident summary.
- [ ] I can use one cleft and one inversion pattern naturally and know when not to.
- [ ] I audited a document for evasive passives and nominalisations.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
