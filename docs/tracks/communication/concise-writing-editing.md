---
title: "Concise writing & editing"
track: communication
slug: concise-writing-editing
priority: P0
complexity: 3
est_hours: 2
phase: 1
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Concise writing & editing

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 1 · **Prereqs:** [Sentence structure & parallelism](sentence-structure-parallelism.md) (helpful, not required)
    **You're done when:** you can cut a 300-word draft to about 200 words without losing a single decision, number or ask, using a written editing checklist, and can explain each cut.

Drilled in [Week 1](drills/week-01.md) (concise emails), [Week 4](drills/week-04.md) (cut 30 percent), [Week 6](drills/week-06.md) (tightening paragraphs) and [Week 13](drills/week-13.md) (nominalisation vs strong verbs).

## Why it matters

At Staff level you are read by people with less time and less context than you have. Every unnecessary word is a tax on their attention, and every buried point is a risk that your recommendation is not seen. Concise writing is not short writing: it is **writing in which each word carries weight**. Fluent non-native writers often over-pad for politeness or safety ("I would like to kindly request you to please..."), stack hedges, or translate long formal patterns from other languages.

Concision also shows thinking: you cannot cut what you have not understood. Editing is the highest-leverage writing skill.

## Core concepts

### 1. Concise is about the reader's cost, not word count

Cut what does not change the reader's understanding or action. Keep what does: numbers, dates, owners, conditions, caveats that change a decision. A 200-word email with every decision is better than a 60-word email with an unclear ask.

### 2. The seven cuts (with before/after)

**Cut 1: Throat-clearing openers**

| Before | After |
|---|---|
| I am writing this email to inform you that the deployment has been postponed. | The deployment is postponed. |
| I just wanted to reach out and check in regarding the status of the review. | Is the review done? / Where does the review stand? |

**Cut 2: Redundant pairs and pleonasm**

| Before | After |
|---|---|
| each and every | every |
| first and foremost | first |
| completely eliminate | eliminate |
| past history · future plans · end result | history · plans · result |
| basic fundamentals · advance planning | fundamentals · planning |
| in my personal opinion | in my opinion (or just state it) |
| revert back | revert (note: "revert back to X" is idiomatic in Indian English but redundant elsewhere; "reply" or "get back to you" are better) |

**Cut 3: Wordy phrases → single words**

| Wordy | Concise |
|---|---|
| due to the fact that | because |
| in order to | to |
| at this point in time · at the present time | now |
| in the event that | if |
| with regard to · with reference to · in relation to | about, on |
| a number of | several / many (or the number) |
| is able to · has the ability to | can |
| make a decision · reach a decision | decide |
| give consideration to | consider |
| in spite of the fact that | although |
| prior to · subsequent to | before · after |
| on a daily basis | daily |
| it is important to note that | (delete, or state the point) |
| the majority of | most |

**Cut 4: Nominalisations → strong verbs** (see the week 13 grammar focus)

| Before | After |
|---|---|
| We conducted an analysis of the logs. | We analyzed the logs. |
| The team made a recommendation to adopt Kafka. | The team recommended Kafka. |
| There was a failure of the cache to invalidate. | The cache failed to invalidate. |
| Implementation of the fix will result in a reduction of latency. | The fix will reduce latency. |

**Cut 5: Weak "there is / it is" constructions and hidden subjects**

| Before | After |
|---|---|
| There are three reasons why we should defer. | We should defer for three reasons. |
| It is the case that costs have risen. | Costs have risen. |
| It was decided that the migration should be paused. | We paused the migration. (or "Ops paused...") |

**Cut 6: Stacked hedges and softeners**

| Before | After |
|---|---|
| I think that maybe we might possibly want to consider perhaps deferring. | I recommend we defer. / We may need to defer. (one hedge only) |
| It seems like it might be somewhat slow at times. | It is slow under load (p95: 900 ms). |
| I just wanted to quickly ask if you could possibly take a look. | Could you review this by Friday? |

One hedge per claim; if you are unsure, quantify the uncertainty ("70% confident") instead of piling modals. See [Conditionals, modals & hedging](conditionals-modals-hedging.md).

**Cut 7: Repeated context and closing filler**

Delete the last paragraph if it restates the first, and delete "Please let me know if you have any questions" unless there is a specific, likely question.

### 3. What NOT to cut

- **Numbers, dates, owners** and the **ask**.
- **The reason** for a recommendation (one sentence).
- **Conditions and constraints** ("assuming the vendor delivers by June").
- **Warmth on sensitive messages.** A curt message to a peer after a hard incident can read as blame; keep one human sentence.
- **Definitions** for a mixed audience.
- **Articles and connectors** in an attempt to be "short": telegraphic style ("Deploy delayed. Root cause: cache.") is fine in chat or a status line but inappropriate in formal email or docs.

### 4. Structure before words: the top-down edit

Edit in **layers**; do not polish sentences in a draft that has the wrong structure.

1. **Purpose:** Can you state the message in one sentence? If not, do not edit; think.
2. **Order:** Answer/ask first (BLUF), then reason, then detail.
3. **Paragraphs:** One idea each, topic sentence first, 3-5 lines.
4. **Sentences:** average 15-20 words; break sentences over 30; vary length.
5. **Words:** apply the seven cuts.
6. **Mechanics:** spelling, grammar, punctuation, consistency of tense and terminology.
7. **Read aloud** (or use text-to-speech). Where you stumble, the reader will.

### 5. Editing checklist (copy into your notes)

- [ ] One sentence states the purpose and the ask, and it is near the top.
- [ ] Every paragraph starts with its point.
- [ ] Every number has a unit and a comparison (from what, to what, over what period).
- [ ] No sentence over about 30 words without a reason.
- [ ] Active voice unless the actor is unknown or irrelevant.
- [ ] Verbs, not nominalisations (analysis of -> analyze).
- [ ] At most one hedge per claim.
- [ ] No "very, really, quite, just, actually, basically" unless needed.
- [ ] Jargon defined or replaced; acronyms expanded on first use for a mixed audience.
- [ ] Terminology consistent (do not alternate "service", "app" and "component" for one thing).
- [ ] Read aloud once.
- [ ] Subject line or title states the content and action.

### 6. Full before/after rewrite (status update)

**Before (142 words)**

> Hi Team,
>
> I hope you are all doing well. I just wanted to reach out and give you a quick update with regard to the status of the carrier integration project. As of this point in time, we have basically completed a majority of the development work, however there are a number of issues that we are currently facing which may possibly have an impact on the timeline. In particular, due to the fact that the vendor has not yet provided the sandbox credentials, we have been unable to proceed with the testing phase. It is important to note that this is a blocker for us. We would really appreciate it if someone could kindly look into this at the earliest possible convenience. Please let me know if you have any questions or need any further information.
>
> Thanks and regards,
> Rahul

**After (61 words)**

> Subject: Carrier integration: blocked on vendor sandbox credentials
>
> Hi team,
>
> Development is about 80% complete, but testing is blocked: the vendor has not sent sandbox credentials, requested on 3 September. If we do not have them by 30 September, the 15 November launch is at risk.
>
> Ask: can someone in Procurement escalate to the vendor by Monday?
>
> Rahul

**What changed:** subject line carries the headline; "a majority" and "basically" replaced by the number (80%); the risk has a date; the ask is specific with owner and deadline; polite filler removed; nothing the reader needs was lost, and a fact (request date) was added.

### 7. Editing at scale: a quick method for your own drafts

**The 30% rule:** write the draft; then remove a third. Work through in three passes: (1) delete whole sentences that repeat or add no decision; (2) shorten sentences with the seven cuts; (3) shorten the structure (merge sections, remove headings that are one line).

**The "so what" test:** after each sentence, ask "so what?" If the reader cannot act or decide differently, delete or merge.

**The "cold read" test:** would a reader who opens this at 7 a.m. on a phone know what to do?

**Tools:** Hemingway Editor highlights long sentences, adverbs and passive voice, but it does not know your audience; use it as a smell detector, not an authority. Grammarly's tone and clarity suggestions are useful; do not accept every rewrite, and remember that a tool can flatten your voice. Do not paste confidential material into third-party tools without checking your company policy.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Plain Language guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/) | guide | US government's rules with before/after examples for concision, active voice, short sentences | intermediate | free |
| [GOV.UK content design guidance](https://www.gov.uk/guidance/content-design) :gem: | guide | Writing for a busy, mixed audience: the best public model of concise, action-first prose | intermediate | free |
| [Google developer documentation style guide](https://developers.google.com/style) | guide | Active voice, present tense, clear procedures; the engineer's house style | intermediate | free |
| [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) | guide | Practical guidance on tone, plain words, bias-free communication | intermediate | free |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Clear grammar, conciseness and style pages with exercises | intermediate | free |
| [Hemingway Editor](https://hemingwayapp.com/) | tool | Highlights long sentences, adverbs, passive voice: a quick cut-detector | all | free/paid |
| [Grammarly blog](https://www.grammarly.com/blog/) | article | Short pages on wordiness, filler words, and tone | intermediate | free |
| Zinsser, *On Writing Well* | book | Classic on clutter and clarity; the chapter "Clutter" is the model for this page | intermediate | paid |
| Williams, *Style: Lessons in Clarity and Grace* | book | Explains why nominalisations and buried subjects make prose heavy, with systematic fixes | advanced | paid |

## Hands-on lab (60 min)

1. **Collect (10 min).** Pull three of your own sent emails or docs (over 150 words each).
2. **Cut (30 min).** Edit each with the layered method: purpose, order, paragraphs, sentences, words. Aim for 30% shorter with nothing decision-critical lost.
3. **Compare (10 min).** Record before/after word counts and a one-line reason for each major cut in a table.
4. **Read aloud (5 min).** Read the after-versions aloud; fix stumbles.
5. **Peer test (5 min, later).** Send the "after" version to a colleague and ask them to say what action you want.

**Expected output:** three before/after pairs with a 25-35% word reduction and your own top-five "wordy habits" list (e.g. "I just wanted to", "please find attached", "as per").

## Questions

### L1 — Recall

??? question "Q1. Give concise replacements for: *due to the fact that*, *in order to*, *at this point in time*, *a majority of*."

    ??? success "Answer"
        because; to; now; most.

??? question "Q2. What is a nominalisation? Give one before/after."

    ??? success "Answer"
        A verb or adjective turned into a noun ("conduct an analysis of" for "analyze"). Before: "We performed an evaluation of the vendors." After: "We evaluated the vendors." Fewer words, clearer actor and action.

??? question "Q3. State the layers of a top-down edit."

    ??? success "Answer"
        Purpose, order, paragraphs, sentences, words, mechanics, read aloud.

??? question "Q4. What should you never cut when shortening?"

    ??? success "Answer"
        Numbers, dates, owners, the ask, the reason and conditions that change a decision, and necessary warmth in sensitive messages.

### L2 — Apply

??? question "Q5. Cut to one sentence: "I wanted to take this opportunity to let you know that, due to the fact that we have encountered some unexpected issues, the release will unfortunately be delayed until such time as we are able to resolve them.""

    ??? success "Answer"
        "The release is delayed until we resolve unexpected issues." Better with detail: "The release is delayed by two days while we fix a failing payment test." Removed throat-clearing, "due to the fact that", "unfortunately" (unnecessary), and "until such time as". Adding a concrete cause and time improves it further.

??? question "Q6. Rewrite with a strong verb and active voice: "A determination was made by the committee that the implementation of the change should be postponed.""

    ??? success "Answer"
        "The committee decided to postpone the change." Nominalisations (determination, implementation) become verbs; passive turns to active; 17 words become 7.

??? question "Q7. Edit: "It is my belief that it might be somewhat beneficial to possibly consider the option of adding a cache.""

    ??? success "Answer"
        "I recommend adding a cache." or, if genuinely unsure, "Adding a cache may help." One hedge only; the belief and consideration language is redundant.

??? question "Q8. Spot the problem: "Please find attached herewith the report for your kind perusal.""

    ??? success "Answer"
        Stacked formal redundancy (find attached herewith, kind perusal). Use: "The report is attached." or "Attached is the Q3 latency report; the key finding is on page 2." Also the "perusal" is unnatural and can even mean "read carefully" or "skim" ambiguously.

### L3 — Judge and choose

??? question "Q9. Two versions of an email to your VP: (A) 40 words, no explanation; (B) 110 words with context. Which do you send when asking for budget?"

    ??? success "Answer"
        Neither by default: choose the version where the VP can decide without a follow-up. A lean but complete: ask, amount, reason, consequence of no, deadline. If A omits the reason or deadline, it is too short; if B holds context the VP already has, cut it. Concise means "sufficient", not "minimal".

??? question "Q10. Is "revert back" acceptable in global business writing?"

    ??? success "Answer"
        It is widely used in Indian English (meaning "reply"), but "revert" in UK/US usage generally means "return to a previous state" (revert to the previous version), so "please revert" may confuse or read as odd; "revert back" is also redundant. Prefer "reply", "get back to you", "let me know". You are not wrong in one variety, but the goal is to be understood by a global reader.

??? question "Q11. Telegraphic style ("Deploy delayed. Cache issue. ETA Fri.") vs full sentences: when is each appropriate?"

    ??? success "Answer"
        Telegraphic in chat, incident timelines and status tables, where reader and context are shared. Full sentences in emails to executives, external parties or first messages, where missing articles and verbs look curt or ambiguous. Match reader, medium, and stakes.

### L4 — Staff-level

??? question "Q12. Your VP says your emails are "too long"; your team says your updates are "too curt". Diagnose and adjust."

    ??? success "Answer"
        Different readers need different depth. Adopt layered writing: BLUF first line (VP), details below with headers or bullets (team). For the VP: decision, impact, ask; for the team: owners, dates, technical detail. Link to a doc for depth. Ask each: "What do you need from my updates?" and test with one thing to keep and one to cut.

??? question "Q13. You are asked to edit a senior peer's long, jargon-heavy design summary. How do you give the edit without offending?"

    ??? success "Answer"
        Ask first ("Can I suggest edits for concision?"), use suggestion mode, explain each substantial cut in a comment ("the reader needs the decision first"), edit for structure before words, preserve their technical content and voice, and give a positive summary of what works. Offer a before/after of the first paragraph as a sample.

??? question "Q14. Should you use an AI assistant to shorten your writing? What are the risks?"

    ??? success "Answer"
        Useful as a first-cut editor: paste non-confidential text, ask for "cut 30% without removing numbers or the ask". Risks: it may remove the nuance or the ask, flatten your voice, invent details, or leak confidential data if the tool is not approved. Always compare against your checklist and verify all numbers. You are accountable for the final text.

## Real-world use cases

- **Incident status update:** headline, impact, ETA, next update time, in five lines.
- **Design doc executive summary:** 150 words that a VP can act on.
- **Slack escalation:** three sentences with the ask and deadline.
- **Performance review self-assessment:** achievements in verbs and numbers, not adjectives.
- **PR descriptions and commit messages:** what and why in the first line.

## Pitfalls & anti-patterns

- Cutting numbers and caveats while keeping filler.
- Over-compressing into telegraphic prose for senior readers.
- Editing sentences before fixing structure.
- Trusting a tool's readability score over your reader.
- Removing all warmth, so a message reads as blame.
- Writing "brief" emails that need three follow-ups.
- Keeping favourite phrases ("as per", "kindly do the needful", "revert back") that read oddly outside your region.

## Checklist

- [ ] I can cut a 300-word draft by a third and defend each cut.
- [ ] I know my top five wordy habits and their replacements.
- [ ] I edit in layers (purpose, order, paragraphs, sentences, words).
- [ ] I read drafts aloud before sending important ones.
- [ ] I applied the checklist to three real messages this week.
- [ ] I answered all L3 questions out loud in < 3 min each.
