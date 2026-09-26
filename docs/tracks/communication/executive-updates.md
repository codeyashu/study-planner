---
title: "Executive updates, summaries & escalations"
track: communication
slug: executive-updates
priority: P0
complexity: 3
est_hours: 2
phase: 4
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Executive updates, summaries & escalations

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 4 · **Prereqs:** [Email writing that gets action](email-writing.md), [Concise writing & editing](concise-writing-editing.md), [Structuring spoken answers](structuring-spoken-answers.md)
    **You're done when:** you can produce, in 10 minutes each, a weekly executive update, a one-paragraph executive summary and an escalation message that a VP can act on without a follow-up question, and deliver the same content as a 3-minute spoken briefing.

Drilled in [Week 11](drills/week-11.md) (escalation emails), [Week 12](drills/week-12.md) (executive summaries), [Week 13](drills/week-13.md) (executive updates and the 3-minute briefing) and [Week 16](drills/week-16.md) (the one-pager).

## Why it matters

Executives decide with incomplete information and little time. They do not want to know everything; they want to know **what changed, whether they need to act, and what will happen if they do not**. At Staff/Principal level, the quality of your upward communication decides whether your work is funded, whether risks are addressed early, and whether leaders trust you when things go wrong.

Typical failures:

- **Narrating activity** ("we did A, B, C") instead of reporting status against a goal.
- **Green-washing:** everything is green until suddenly it is red. Executives punish surprises far more than bad news.
- **Burying the ask.**
- **Escalating with blame or emotion,** which converts a problem into a conflict.
- **Too much technical detail,** or none where the executive needs a specific number to decide.

## Core concepts

### 1. What executives need: the four questions

Every executive communication should answer:

1. **Status:** Where are we versus the goal? (On track / at risk / off track.)
2. **Change:** What is different since the last update?
3. **Impact:** What does it mean for customers, cost, date or risk, in their terms?
4. **Ask:** What do you need from me, by when? (Or "no action needed".)

Use their vocabulary (revenue, customer impact, delivery date, risk, cost) and translate technical causes into consequences: not "the Kafka consumer lag exceeded the threshold" but "shipment status updates are delayed by up to 40 minutes for 3 carriers".

### 2. The executive update (weekly or biweekly)

**Template**

```text
Subject: [Program] update, week of 22 Sept: AMBER (was GREEN)

Status: AMBER. Launch date 15 Nov unchanged, but at risk.
Since last update: Rate and label APIs complete (80% overall). Tracking webhook in review.
Risk / issue: Vendor sandbox credentials outstanding (requested 3 Sept). Testing is blocked. If not received by 30 Sept, launch slips to 6 Dec.
Mitigation: Escalated via Procurement on 19 Sept; fallback: contract test doubles (cost: 1 week of effort).
Ask: Introduction to the vendor's VP by 26 Sept. (Owner: Dana)
Next update: 29 Sept.
```

**Rules**

- **Status colour with a definition:** Green: on track, no help needed. Amber: at risk, mitigation under way, may need help. Red: will miss, or blocked, decision or help needed now. Agree the definitions with your audience.
- **Report change, not activity.** Only include items that changed status or need attention.
- **Lead with the headline;** keep to one screen (150-250 words).
- **Trend and comparison:** "was GREEN", "down from 14 days to 9".
- **Amber early.** Flip to amber when you see the risk, not when it is certain. Executives prefer "amber with a plan" to "red without warning".
- **Numbers with context:** "p95 latency 320 ms (target 300)".
- **Consistent format** so readers can scan week to week.
- **No surprises rule:** no executive should hear bad news from someone else first.

### 3. The executive summary (for a document or proposal)

A standalone 100-200 word section that lets a leader decide without reading the rest. Structure:

| Element | Content |
|---|---|
| **Situation / problem** | One or two sentences with the stakes and numbers |
| **Recommendation** | What you propose |
| **Benefit** | Expected outcomes, quantified |
| **Cost / risk** | Money, people, time, main risk |
| **Ask / decision** | Approval, funding, by when |

**Example**

> **Executive summary.** Shipment-status updates reach customers up to 14 minutes late, driving 30% of support tickets and three customer escalations in Q2. We recommend replacing carrier polling with an event-driven ingestion layer, starting with the five highest-volume carriers, which would cut delay to under 60 seconds for about 70% of volume. Phase 1 costs about EUR 9k/month in infrastructure and 4 engineer-months. The main risk is running two ingestion paths during migration; we mitigate with a 6-week parallel run. We request approval and 4 engineer-months from the Q4 budget by 10 October.

**Test:** give it to someone who has not seen the document. Can they tell you the problem, recommendation and ask?

### 4. Escalation: principles and template

**When to escalate:** when (a) you are blocked and the owner cannot or will not unblock you, (b) a risk exceeds your authority, (c) a deadline or commitment will be missed, (d) an ethical, security or compliance issue exists, or (e) two teams disagree and cannot resolve it. **How early:** as soon as the issue is likely to affect a commitment, after a reasonable attempt to resolve it at the lowest level.

**Principles**

1. **Facts, not blame.** Describe behaviours and outcomes, not character.
2. **Show your work.** What you have tried and when.
3. **Quantify impact** in business terms.
4. **Ask for a specific action** with a deadline; offer options.
5. **Tell the other party first** or at the same time ("I'm raising this with Dana today; here's my summary.").
6. **Keep an audit trail** in writing, but resolve in conversation where possible.
7. **Follow through:** close the loop when resolved.

**Template**

```text
Subject: Escalation: [issue], impact on [date/customer], decision needed by [date]

Summary: [one sentence: what is wrong and what you need].
Impact: [customers, revenue, date, risk, with numbers].
Background: [2-3 lines, dated: what happened].
What we have tried: [bulleted, with dates].
Options: [A: ..., B: ...] Recommendation: [A, because...].
Ask: [Name] to [action] by [date].
I can [offer: join a call, prepare a brief]. Next update: [date].
```

**Tone phrases**

| Purpose | Phrase |
|---|---|
| Open neutrally | "I want to flag a risk to the 15 Nov launch." · "I need your help to unblock..." |
| Avoid blame | "The dependency was delayed" / "We have not received..." rather than "They failed to deliver". |
| Show effort | "We have followed up on 10, 15 and 22 Sept." |
| Ask | "Could you contact their VP by Monday?" · "Can you make the call on scope by Friday?" |
| Keep the relationship | "I've shared this summary with Priya so we are aligned." |
| Close | "I'll update you on Monday whatever the outcome." |

### 5. The 3-minute spoken executive briefing

Same content, different medium: listeners cannot re-read, so repeat the headline.

| Time | Content |
|---|---|
| 0:00-0:20 | **Headline:** "Bottom line: we're amber. The launch date holds, but only if the vendor delivers credentials by 30 September." |
| 0:20-1:00 | **Situation:** what has happened since last time; one number |
| 1:00-1:50 | **Issue / risk:** cause, impact in business terms |
| 1:50-2:30 | **Options and recommendation** |
| 2:30-3:00 | **Ask and next step,** restate the headline |

Delivery: 120-140 wpm; pause after the headline and the ask; no jargon without translation; expect interruptions and plan a 30-second version. For Q&A see [Executive presence & handling Q&A](executive-presence.md).

### 6. Language for executive updates

**Precision with status**

| Instead of | Say |
|---|---|
| "We're kind of behind." | "We are two weeks behind plan (15 vs 29 Sept)." |
| "It should be fine." | "I'm 80% confident we'll make 15 Nov; the risk is the vendor." |
| "There are some issues." | "Two issues: X (blocking) and Y (minor)." |
| "We're working on it." | "Priya owns the fix; ETA Friday; next update Monday." |
| "Everything's green." | "Green on delivery and cost; amber on quality (test pass rate 91% vs 95% target)." |

**Confidence and risk vocabulary:** on track, at risk, slipping, off track, blocked, mitigated, contained, resolved, root cause, contributing factor, exposure, blast radius, critical path, dependency, decision point, contingency, fallback, trigger. Use them precisely.

**Bad news phrases:** "The launch will slip by three weeks." · "We got this wrong: we underestimated the migration." · "Here is what we are doing about it." Avoid "unfortunately" as a habit, "we had some challenges" (vague), and "it wasn't our fault".

**Numbers:** give the unit, the baseline and the period ("errors fell from 4.2% to 0.6% over two weeks"). See [Collocations & precision with numbers and data](collocations-precision.md).

### 7. Postmortem/incident summaries for executives

Structure: **Impact** (who, how long, business cost), **Cause** (one plain sentence), **Fix** (what restored service), **Prevention** (2-3 actions with owners and dates), **Learning** (what we now know). Keep blameless: systems, not people ("the deploy pipeline allowed a config change without validation"). See [Week 9](drills/week-09.md) (blameless postmortem prose) and the Google SRE book chapter on postmortem culture.

### 8. Before / after: an executive update

**Before**

> Hi Dana, Hope you're well. So, the team has been working really hard on the carrier integration and we have made a lot of progress on multiple fronts including the rate API and label service. There were some challenges with the vendor but we are working on resolving them. We should be able to deliver on time hopefully. Let me know if you have any questions.

**After**

> **Carrier integration: AMBER (was GREEN).** Launch 15 Nov holds if the vendor delivers sandbox credentials by 30 Sept (requested 3 Sept; testing is blocked). Rate and label APIs are complete; overall 80%. Fallback: test doubles, costing one week. **Ask:** please introduce me to the vendor's VP of Partnerships by 26 Sept. Next update 29 Sept.

**What changed:** status and trend first; the date and dependency are explicit; work narrative replaced by outcomes; a fallback and cost show planning; a single dated ask; the next update date sets expectations.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Atlassian Incident Management Handbook](https://www.atlassian.com/incident-management/handbook) | guide | Templates and roles for incident comms and stakeholder updates | intermediate | free |
| [Google SRE Book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) | book chapter | The model for blameless postmortem writing and how to summarise for leaders | intermediate | free |
| [Plain Language guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/) | guide | Lead with the conclusion; write for the reader's decision | intermediate | free |
| [GOV.UK content design guidance](https://www.gov.uk/guidance/content-design) :gem: | guide | How to write for people with little time: user need first | intermediate | free |
| [StaffEng](https://staffeng.com/) | site | Staff-level stories on writing up, managing up and stakeholder communication | intermediate | free |
| [lethain.com](https://lethain.com/) | blog | Will Larson's posts on status, managing up and engineering strategy | advanced | free |
| Barbara Minto, *The Pyramid Principle* | book | Answer-first structuring for executive communication | advanced | paid |
| Josh Bernoff, *Writing Without Bullshit* | book | Readers are busy: put the point first, write for the boss | intermediate | paid |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Executive summary and report-writing pages | intermediate | free |

## Hands-on lab (75 min)

1. **Weekly update (20 min).** Write an update for your current program using the template. Include colour with definition, trend, one risk, mitigation, one ask and next-update date. Keep it under 200 words.
2. **Executive summary (20 min).** Write a 150-word summary for a proposal you own. Give it to a colleague who has not seen the work; ask them to state the ask.
3. **Escalation (15 min).** Write an escalation message for a real or realistic blocker with the template; remove any blame words; check that the ask has an owner and a date.
4. **3-minute briefing (15 min).** Deliver one of the above aloud, timed, recorded; check the headline appears in the first 20 seconds and again at the end.
5. **Score (5 min).** Use the checklist below.

**Expected output:** an update, a summary, an escalation and a recorded briefing, each self-scored.

## Questions

### L1 — Recall

??? question "Q1. What four questions should an executive communication answer?"

    ??? success "Answer"
        Status (versus goal), what changed, impact in business terms, and the ask (or "no action needed").

??? question "Q2. Define green, amber and red in a status report."

    ??? success "Answer"
        Green: on track, no help needed. Amber: at risk, mitigation under way, may need help. Red: will miss the commitment or is blocked; decision or help needed now. Definitions should be agreed with the audience.

??? question "Q3. What are the seven principles of a good escalation?"

    ??? success "Answer"
        Facts not blame; show what you tried; quantify impact; specific ask with deadline and options; tell the other party; keep a written trail but resolve in conversation; follow through.

??? question "Q4. What goes in an executive summary?"

    ??? success "Answer"
        Problem and stakes, recommendation, benefit, cost/risk, and the decision requested with a date.

### L2 — Apply

??? question "Q5. Rewrite "The team has been working hard and there are some challenges but we're hopeful.""

    ??? success "Answer"
        "Status: AMBER. Two issues threaten the 15 Nov launch: the vendor credentials (blocking) and a 9% test failure rate (fixable in a week). We're 80% confident of launch. I need an introduction to the vendor's VP by Friday." Status, specifics, confidence, ask.

??? question "Q6. Write an escalation opening (two sentences) for a peer team that missed a dependency date twice."

    ??? success "Answer"
        "I want to flag a risk to the 15 Nov launch: the tracking-events dependency, due on 5 Sept, has slipped twice (now 26 Sept). I've discussed this with Sanjay on the 12th and 19th and would like your help to agree a firm date by Friday." Facts, dates, effort shown, ask; no blame.

??? question "Q7. Convert to business impact: "The Kafka consumer group is lagging by 40 minutes for three partitions.""

    ??? success "Answer"
        "Shipment status updates for three carriers are up to 40 minutes late, affecting about 2,000 bookings; customers may see outdated status." Impact in the executive's terms; the technical cause can follow if needed.

??? question "Q8. Write the headline for a 3-minute briefing on a security patch that must be applied by Friday but will need a 2-hour maintenance window."

    ??? success "Answer"
        "Bottom line: we need a two-hour maintenance window this Thursday night to apply a critical security patch; I need your approval by Wednesday noon." Ask and deadline in the first sentence.

### L3 — Judge and choose

??? question "Q9. Status is truly uncertain: 60% chance of making the date. Green, amber or red? What do you tell the executive?"

    ??? success "Answer"
        Amber, and quantify: "Amber: about 60% likely to hit 15 Nov. The risk is X; we'll know by 30 Sept; the fallback is Y." A 60% chance is not green. Reporting the probability and the trigger date is more useful than a colour alone.

??? question "Q10. Should you tell your VP about a problem before you have a solution?"

    ??? success "Answer"
        Yes, if it could affect a commitment or the VP may hear about it elsewhere. Bring what you know: facts, impact, what you are doing to find a solution and when you will report again. "I don't have a fix yet; here's the plan to have one by Thursday." Waiting for a solution risks a surprise later.

??? question "Q11. You believe another team's director is the cause of your delay. Do you name them in the escalation?"

    ??? success "Answer"
        Name the dependency and team factually ("the tracking-events dependency owned by Platform"), not the person's failings. Share the draft with the other team's lead first so they can correct facts or fix it. Naming individuals shifts the discussion from the problem to the blame and burns trust.

??? question "Q12. Bullets or paragraphs for an executive update?"

    ??? success "Answer"
        Short labelled bullets (Status, Since last, Risk, Ask) for scanning; a short paragraph for the reasoning in an executive summary, where logic between sentences matters. Consistent format week to week beats novelty.

### L4 — Staff-level

??? question "Q13. You discover a serious risk 3 days before a board update in which your VP will say "all on track". What do you do?"

    ??? success "Answer"
        Tell your VP immediately, in person or by call, then send a written summary: facts, impact, options, recommendation, and the effect on the board message. Offer alternative wording ("on track for date, with one significant risk we're mitigating"). Do not wait for the update or hope it resolves. The VP can only manage what they know.

??? question "Q14. Leadership wants an "everything green" dashboard; your projects are honestly amber. How do you handle it?"

    ??? success "Answer"
        Explain the cost of false green (late surprises, loss of trust), propose clear colour definitions and an "amber with plan is normal" norm, and show the trend and mitigation for each amber. Give leaders what they need: a decision, not a colour. If the culture punishes honesty, escalate through your manager and document; do not misreport.

??? question "Q15. Write the first three sentences of an executive update following a major incident that caused 3 hours of downtime for one region, where a change made by your team was the cause."

    ??? success "Answer"
        "The EU booking service was unavailable for 3 hours 10 minutes yesterday (14:05-17:15 UTC), affecting roughly 5,800 bookings. The cause was a configuration change our team deployed without validation; service was restored by rollback. We're making config validation mandatory in the pipeline by 10 October and will send a full postmortem by Friday." Ownership without excuses, impact, cause, prevention, dated commitment. See [Week 9](drills/week-09.md).

## Real-world use cases

- **Weekly program status to a VP** with colour, change, risk and ask.
- **Quarterly business review:** executive summary with the trend in three metrics.
- **Major incident:** timeline of impact, cause, fix, prevention, and stakeholder comms.
- **Blocked dependency:** escalation to a director of a partner team.
- **Budget or headcount request:** executive summary plus one-pager (see [Week 16](drills/week-16.md)).

## Pitfalls & anti-patterns

- Watermelon status: green outside, red inside.
- Narrating activity instead of reporting against a goal.
- Escalating with an accusation, or copying up as a threat.
- No ask, or an ask with no owner and date.
- Excess detail: the reader must dig for the point.
- Jargon and unexplained acronyms.
- Late bad news; the second surprise is worse than the first.
- Changing the format every week.
- Over-apologising and under-informing.

## Checklist

- [ ] I can write a weekly update in under 200 words with status, change, risk, ask and next update date.
- [ ] I have written an executive summary that a colleague could act on.
- [ ] I wrote an escalation with facts, impact, options and an owner and date for the ask.
- [ ] I can deliver a 3-minute briefing with the headline in the first 20 seconds.
- [ ] I define green, amber and red with my audience.
- [ ] I answered all L3 questions out loud in < 3 min each.
