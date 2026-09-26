---
title: "Tenses & aspect: perfect vs simple, narrative tenses"
track: communication
slug: tenses-aspect
priority: P0
complexity: 3
est_hours: 2
phase: 1
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Tenses & aspect: perfect vs simple, narrative tenses

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 1 · **Prereqs:** none (pairs with [conditionals, modals & hedging](conditionals-modals-hedging.md))
    **You're done when:** you can narrate a project (status, history, plan) in one paragraph choosing tense by *relevance to now*, not by the calendar, and you can defend each choice.

## Why it matters
Status updates, incident timelines, interview stories and RFC "background" sections all mix past, present and future. The most damaging fluent-speaker errors are (1) using the past simple where the present perfect is needed ("I worked on this for two years" when you still do), (2) using continuous forms with stative verbs ("I am knowing"), and (3) losing control of tense in stories (jumping between past and present). Tense choice also signals stance: "We've fixed it" (it is fixed now, take my word) vs "We fixed it" (a past event, maybe later broke).

## Core concepts

### Two dimensions: time and aspect
- **Tense** places the event relative to now (past, present, future).
- **Aspect** shows how the speaker views it: **simple** (a fact/complete event), **continuous/progressive** (in progress, temporary, unfinished), **perfect** (a connection between two times: earlier event, present/reference-time relevance).

| | Simple | Continuous | Perfect | Perfect continuous |
|---|---|---|---|---|
| Present | We deploy on Fridays. | We're deploying now. | We've deployed twice this week. | We've been deploying since 9. |
| Past | We deployed yesterday. | We were deploying when it failed. | We had deployed before the freeze. | We had been deploying for an hour when it failed. |
| Future | We'll deploy tomorrow. | We'll be deploying at 10. | We'll have deployed by Friday. | We'll have been deploying for six hours by then. |

### Present perfect vs past simple (the most important contrast)

| Present perfect (have + past participle) | Past simple |
|---|---|
| Time frame **not finished** or **unspecified**: *this week, so far, recently, already, yet, ever, never, since, for* | Time frame **finished** and stated or understood: *yesterday, last week, in 2023, when I joined, ago* |
| Focus on **present result/relevance**: "We've migrated the database" (so it is on the new system now) | Focus on the **event**: "We migrated the database in March" |
| Experience in a life/career up to now: "I've led three migrations" | A specific occasion: "I led the 2024 migration" |
| Unfinished states: "I've worked here for 15 years" (I still do) | Finished: "I worked there for five years" (I don't now) |

**Rules and exceptions**
- **Never** combine present perfect with a *finished* time marker: "I have finished it yesterday" is wrong; use "I finished it yesterday".
- **Question about time** ("When did you...?") requires the past simple: "When did the outage start?"
- **American English** often uses the past simple with *already, yet, just*: "Did you send it yet?" "I just sent it." Both are acceptable in the US; the perfect is standard in UK and safer in formal writing.
- **Since / for**: "since 2022" (a point), "for three years" (a duration), always with a perfect for unfinished periods ("I have worked here since 2022", not "I work here since 2022").
- **Gone / been**: "She's gone to Singapore" (she is there now) vs "She's been to Singapore" (visited, returned).
- **Recent news lead-in**: A common natural pattern: present perfect to announce, past simple to give details. "We've had an incident. It started at 09:12 and lasted 40 minutes."

### Present perfect continuous vs present perfect simple
- *Continuous* stresses **duration, activity, or recent activity with visible results**: "I've been working on the RFC all week." "We've been seeing timeouts since the upgrade."
- *Simple* stresses **result/completion or count**: "I've written three RFCs." "We've fixed 12 bugs."
- Stative verbs (*know, believe, own, need, want, belong, understand*) generally take the simple form: "I've known him for years", not "I've been knowing".
- With *how long* it's usually continuous (activity) or simple (state): "How long have you been leading the team?"

### Continuous with stative verbs
Verbs of state normally avoid the continuous: *be, have (possess), know, understand, believe, need, want, like, prefer, belong, seem, mean, own, remember, depend*.
- "I understand" (not "I'm understanding"); "We need a decision" (not "we are needing").
- Some verbs change meaning: "I **have** a meeting" (own) vs "I'm **having** a meeting" (activity); "**think**" (opinion) vs "I'm thinking about it" (process).
- "I'm loving it" and "I'm understanding" occur in casual speech and marketing; avoid in professional writing.

### Present tenses for schedules, plans and predictions

| Use | Form | Example |
|---|---|---|
| Fixed schedule/timetable | present simple | "The freeze starts on Monday." |
| Personal arrangement | present continuous | "I'm meeting the vendor at 3." |
| Decision made now, offer, promise | will | "I'll check and get back to you." |
| Prior intention/plan | be going to | "We're going to migrate in Q2." |
| Prediction based on evidence | be going to | "Look at the queue: it's going to overflow." |
| After time conjunctions (*when, after, before, as soon as, until, once*) | present simple (not will) | "When the build finishes, I'll notify you." |

**Trap:** "If the test will fail, we'll roll back" (wrong) - "If the test fails, we'll roll back."

### Narrative tenses
Used for stories (interviews, incident narratives, postmortems). Four tools:

| Tense | Function | Example |
|---|---|---|
| Past simple | Main events in order (the "spine") | "The alert fired, I joined the bridge, and we rolled back." |
| Past continuous | Background/ongoing situation or interrupted action | "We were running a load test when the primary failed." |
| Past perfect | Event before the main story time | "By the time I joined, the team had already restarted the service." |
| Past perfect continuous | Duration before a past moment, explaining a cause | "The queue had been growing for hours before anyone noticed." |

Also useful: **used to** (past habit or state, no longer true), **would** (repeated past action in a story: "Every morning he would check the dashboards").

**Story rules**
1. Pick the *spine* tense (usually past simple) and stay there. Do not jump to present.
2. Use the **historical present** deliberately (for vividness: "So I'm on call, the pager goes off, and I see...") but then keep it consistent. In interviews prefer past.
3. Use the past perfect *only* for events clearly earlier than the spine, and once you have made the sequence clear, return to the past simple. Do not chain "had" forever.
4. Mark sequence with time expressions (*by then, previously, at that point, a week earlier, eventually*).

### Reported speech and sequence of tenses
- Backshift is *optional* if the fact is still true: "She said the deadline is Friday" (true now) or "was Friday".
- Standard backshift: present simple → past simple; present perfect → past perfect; will → would; can → could.
- "He told me that he **had deployed** the fix" / "He said he'd deployed it".
- **say/tell**: *say* (no object) vs *tell* (someone): "He said that...", "He told me that...", never "He said me".

### Future perfect and future continuous (planning language)
- **Future continuous** = in progress at a future time or a polite plan: "I'll be presenting at 3" / "Will you be joining the call?" (polite question).
- **Future perfect** = completed by a future time: "By Friday we will have migrated 80% of services."
- **Be due to / be set to / be scheduled to / be expected to** are common in reports: "The release is due to go out on Monday."

### Tense in professional documents
| Section | Typical tense |
|---|---|
| Executive summary of a finished piece of work | present perfect / past simple |
| Background/history | past simple + present perfect |
| Current state | present simple |
| Plan | will / present continuous / going to |
| Postmortem timeline | past simple (timestamps) with past perfect for pre-existing conditions |
| Design doc (proposal) | present simple for what the system does ("The service validates..."); *will* for future behaviour when explaining changes |
| Commit messages | imperative ("Fix race in scheduler") |
| Standup | present perfect ("I've finished X"), present continuous ("I'm working on Y"), will/going to ("I'll start Z") |

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Perfect English Grammar](https://www.perfect-english-grammar.com/) | site | Clear tense contrast pages with exercises. | intermediate | free |
| [BBC Learning English](https://www.bbc.co.uk/learningenglish) | site | Short grammar videos and quizzes; also *6 Minute Grammar*. | intermediate | free |
| Murphy, *English Grammar in Use* and Hewings, *Advanced Grammar in Use* | book | Tenses units with keys; the standard for self-study. | intermediate-advanced | paid |
| Michael Swan, *Practical English Usage* | book | Authoritative on "since/for", perfect vs simple, reported speech. | advanced | paid |
| [English with Lucy (YouTube)](https://www.youtube.com/@EnglishwithLucy) | video | Lively explanations of perfect tenses and narrative tenses. | intermediate | free |
| [Cambridge Dictionary grammar section](https://dictionary.cambridge.org/) | reference | Concise, correct rule statements with examples and common learner errors. | intermediate | free |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Verb tense consistency in professional writing. | intermediate | free |
| BBC *6 Minute English* transcripts :gem: | audio | Hear real speakers using perfect and narrative tenses; use transcripts for shadowing (find via BBC Learning English). | intermediate-advanced | free |

## Hands-on lab (60 min)
1. **Timeline tense audit.** Write a 200-word incident timeline of a real outage. Mark every verb with its tense name. Check: spine = past simple; background = past continuous; pre-conditions = past perfect.
2. **Convert to spoken.** Tell the same story aloud in 90 seconds (record). Transcribe 10 lines and check for tense slips. Log the pattern (usually a slip from past to present).
3. **Standup script.** Write three days of standup updates using present perfect (done), continuous (in progress), will/going to (next).
4. **Career summary.** Write a 5-sentence self-introduction: two sentences with present perfect (experience up to now), two with past simple (specific achievements), one with present/future (current focus).
5. Compare with a native-level example from a BBC 6 Minute English transcript.

## Questions

### L1 - Recall

??? question "Q1. Why is \"I have finished the migration yesterday\" wrong?"
    ??? success "Answer"
        Present perfect cannot be used with a finished time marker (*yesterday, last week, in 2023, ago*). Use the past simple: "I finished the migration yesterday". If you want the perfect, drop the time marker: "I've finished the migration."

??? question "Q2. Which is correct: \"I work here since 2019\" or \"I have worked here since 2019\"? What about \"I'm working here for 6 years\"?"
    ??? success "Answer"
        "I have worked here since 2019" (or "I've been working here since 2019"). For duration to now you need a perfect form: "I've worked/I've been working here for six years". The other two are errors.

??? question "Q3. In \"When the build will finish, I'll ping you\", what is wrong?"
    ??? success "Answer"
        After time conjunctions (*when, after, before, as soon as, until, once*) English uses the present simple for future time: "When the build finishes, I'll ping you."

??? question "Q4. Name the four narrative tenses and one job for each."
    ??? success "Answer"
        Past simple (main events), past continuous (background/interrupted action), past perfect (earlier event), past perfect continuous (duration before a past moment, often a cause).

### L2 - Apply

??? question "Q5. Correct: \"Yesterday I have been in the incident call. The system was failing since 9. When I have joined, the team already restarted the pods.\""
    ??? success "Answer"
        "Yesterday I **was** in the incident call. The system **had been failing** since 9 (or **had been failing** for an hour). When I **joined**, the team **had already restarted** the pods." Finished time (*yesterday*) needs the past simple; duration before a past moment needs the past perfect continuous; the restart happened before joining, so past perfect.

??? question "Q6. Choose: (a) \"I (have led / led) three migrations in my career.\" (b) \"I (have led / led) the 2024 migration of our payment stack.\" (c) \"(Did you send / Have you sent) the report already?\""
    ??? success "Answer"
        (a) have led (career up to now, no specific time); (b) led (a specific finished occasion); (c) Have you sent (UK/formal); "Did you send" is acceptable in American English.

??? question "Q7. Change to reported speech: \"We're migrating to Kubernetes in Q3,\" she said. \"I've already tested it.\""
    ??? success "Answer"
        She said (that) they were migrating to Kubernetes in Q3 and (that) she had already tested it. Backshift: present continuous → past continuous, present perfect → past perfect. Optional: if the plan is still true, "are migrating" is fine.

??? question "Q8. Turn into a good spoken status update using the right tenses: \"Auth service migrate. Finish 3 of 5 endpoints. Work on rate limiting now. Start load test Monday.\""
    ??? success "Answer"
        "We've migrated three of the five endpoints of the auth service. I'm working on rate limiting now, and we're going to start load testing on Monday." (*Migrated* counted result = present perfect; now = continuous; plan = going to or present continuous "we're starting load testing Monday".)

### L3 - Judge and choose

??? question "Q9. \"We fixed the bug\" vs \"We've fixed the bug\": what does each communicate to a VP, and when would you prefer each?"
    ??? success "Answer"
        *We've fixed the bug* emphasises the current state (bug is fixed now): ideal for "where are we?" answers. *We fixed the bug* frames it as an event in the past, appropriate when telling what happened and when ("We fixed it on Tuesday"), or when it may have regressed. In a status update lead with the perfect for the result, then use the past simple for details.

??? question "Q10. In an interview, you tell a story about a production incident. Is the historical present (\"So I'm on call, the pager goes off...\") a good idea?"
    ??? success "Answer"
        It can add energy in a spoken story, but it is risky: you must stay consistent, and slipping between present and past makes you sound uncertain. For an interview, choose the past simple spine with past continuous background; it is easier to keep clean. Use the historical present only if you can sustain it for the whole story, ideally in a short anecdote.

??? question "Q11. \"I've been working on X\" vs \"I've worked on X\": which is better in a CV summary and in a standup?"
    ??? success "Answer"
        CV: past simple or present perfect simple for achievements ("Led...", "Have delivered..."), and *have worked on X for 10 years* for the continuing experience; avoid the continuous for completed projects. Standup: continuous is natural for ongoing work ("I've been working on X since Monday"), simple for finished ("I've finished X").

??? question "Q12. \"The queue had grown for hours\" vs \"The queue had been growing for hours\": choose and explain."
    ??? success "Answer"
        *Had been growing* is better: it stresses the process and duration before the moment of discovery. *Had grown* stresses completion or a change in state ("had grown to 2M messages"). If you add a quantity, use the simple; if you add a duration, use the continuous.

### L4 - Real-world decisions

??? question "Q13. You are writing a postmortem summary for executives. Draft the first two sentences choosing tenses deliberately. Explain the choices."
    ??? success "Answer"
        "On 12 March a configuration change **caused** a 47-minute outage of the booking API. The issue **has been resolved**, and we **are** rolling out safeguards that **will prevent** a repeat." Past simple for the dated event; present perfect for the current state of the fix; present continuous/future for actions. This ordering (what happened, where we are now, what happens next) is the executive pattern.

??? question "Q14. A colleague writes: \"I am agree with your proposal since a long time.\" What are the errors and how do you mirror the correct form in your reply?"
    ??? success "Answer"
        Errors: *agree* is stative (no continuous, and no *am*): "I agree"; *since a long time* should be *for a long time*, and a duration up to now needs a perfect: "I have agreed with your approach for a long time" (or more naturally "I've always agreed with this approach"). Reply naturally with the correct form, e.g. "Great, I've supported this approach for a while too, so let's go ahead." Do not correct publicly unless asked.

??? question "Q15. You are asked to \"walk us through your last project\" in a Staff interview. What tense plan do you use for the 2-minute answer?"
    ??? success "Answer"
        Context in past simple or present perfect if still ongoing ("We had a monolith..."), actions in past simple ("I proposed, I aligned, I led..."), background in past continuous ("teams were struggling..."), earlier events in past perfect ("after we had lost two enterprise customers"), current result in present perfect ("we've reduced latency by 40% and the pattern has since been adopted by three teams"), and lessons in present simple ("What I'd do differently..."). Rehearse the shape, not the words.

## Real-world use cases
- **Weekly status.** Present perfect for progress, continuous for in-flight work, going to/will for plan; keep the same three-part order.
- **Incident bridges.** "We're seeing elevated errors" (now), "we've rolled back" (state), "we'll update in 15 minutes" (commitment).
- **Interview STAR answers.** Situation (past continuous/past perfect), Task and Action (past simple), Result (past simple + present perfect for lasting impact).
- **Roadmap reviews.** Future continuous ("we'll be onboarding two teams in Q3") sounds planned and confident; future perfect for milestones ("by Q4 we will have retired the legacy API").
- **Reference letters and LinkedIn.** Present perfect for continuing responsibility ("I have led the platform team since 2022").

## Pitfalls & anti-patterns
- Present perfect with finished time markers.
- Continuous with stative verbs (*I am knowing, we are having a problem with*: the latter is fine, "are having" = experiencing).
- Using *will* after *if/when/before/after* for future time.
- Losing the story spine (jumping past-present-past).
- Chaining *had* past perfect for a whole story.
- Saying "since 3 years" or "for 2019".
- Overusing "was/were going to" to hedge; be clear whether the plan was abandoned.
- *Say/tell* confusion in reported speech ("He said me").

## Checklist
- [ ] I can state present perfect vs past simple rules in 30 seconds with three examples.
- [ ] I can narrate a 2-minute story with a consistent spine and correct background/earlier-event tenses.
- [ ] I audited a piece of my own writing for tense slips.
- [ ] I can use future perfect and future continuous naturally in planning statements.
- [ ] I answered all L3 questions out loud in under 3 minutes each.
