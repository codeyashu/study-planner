---
title: "Email writing that gets action"
track: communication
slug: email-writing
priority: P0
complexity: 2
est_hours: 2
phase: 1
tags: [communication, P0]
last_reviewed: 2026-09-25
---

# Email writing that gets action

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 2/5 · **Est. time:** 2 h · **Phase:** 1 · **Prereqs:** [Concise writing & editing](concise-writing-editing.md)
    **You're done when:** each of your work emails has a subject line that states content and action, a first line that carries the point or ask, one clear owner and date per request, and you have a template library (BLUF, status, escalation, follow-up, decline) you actually use.

Drilled in [Week 1](drills/week-01.md) (concise emails and subject lines), [Week 11](drills/week-11.md) (escalation emails) and [Week 23](drills/week-23.md) (follow-up and thank-you emails).

## Why it matters

Email is where senior engineers are judged by people who never see the code. A VP reads 100+ messages a day, often on a phone, usually in 5-10 seconds each. The email that gets action has three properties: **it is opened** (subject line), **it is understood in one screen** (BLUF), and **it makes the next step obvious** (a specific ask with an owner and date).

For fluent non-native writers, the frequent problems are: over-formal or archaic phrases ("kindly do the needful", "please revert"), overly indirect requests that never state the ask, and either too much apology or too much bluntness because the politeness conventions differ across cultures. Global companies have their own norms: direct and short in US and Netherlands cultures; more relational and indirect in others. A good email is clear first and warm second, and the warmth is brief.

## Core concepts

### 1. BLUF: bottom line up front

State the conclusion, decision or ask in the first one or two lines; then give the reasons and details. The idea comes from military writing; adopt it as a habit for anything the reader must act on.

```text
Subject: Decision needed by Fri 3 Oct: defer EU cutover to November?

Hi Dana,

BLUF: I recommend deferring the EU cutover from 20 Oct to 10 Nov. I need your approval by Friday to notify the carriers.

Why: two of the three integration tests still fail (pass rate 68%), and the vendor sandbox was down for six days in September.
Impact: no customer impact if we defer; a failed cutover during peak would delay about 4,000 bookings a day.
Options: (1) defer to 10 Nov, cost: none; (2) go on 20 Oct with manual fallback, cost: 3 extra support staff for two weeks.

Reply "approve" and I'll send the carrier notice.

Thanks,
Rahul
```

### 2. Subject lines that work

Formula: **[Action or type] + what + when/for whom**.

| Weak | Strong |
|---|---|
| Update | Status: carrier integration is at risk (decision needed Friday) |
| Question | Question: can we use the EU region for the pilot? (reply by Tue) |
| Meeting | Decision meeting Thu 10:00: tracking API cutover |
| Fwd: urgent | FYI, no action: vendor SLA changed to 99.5% |
| Issue in prod | P1: booking API errors 8% since 09:10 UTC; mitigation under way |

Useful tags: **Action / Decision / FYI / Approval / Question / Update / Escalation / Reminder**. Use a date if there is one; do not use "urgent" without a reason and time; do not write everything in capitals.

### 3. Structure of a good email

1. **Subject line** (states content and action).
2. **Greeting** (short: "Hi Dana,").
3. **Purpose/ask** (BLUF).
4. **Context** in 1-3 short paragraphs or bullets (only what the reader needs).
5. **Options or details** (if a decision is needed: 2-3 options with trade-off and your recommendation).
6. **The ask, with owner and deadline** repeated at the end if the email is long.
7. **Close and name.**

Formatting: short paragraphs (2-4 lines); bullets for parallel items; bold for the ask or deadline only; no wall of text; no more than one topic per email (if two topics, send two emails or number them).

### 4. Writing a request that gets done

- **One request, one owner, one date.** "Could someone look at this?" produces nothing. "Sanjay, could you review the runbook by Wednesday?" does.
- **Give the reason** for the deadline: "so we can freeze scope on Thursday".
- **Make it easy to say yes:** attach the doc, give the link, say what "done" looks like ("comments in the doc are enough").
- **State the consequence** of no response when it matters: "If I don't hear by Friday, I'll proceed with option 1."
- **Cc carefully:** To = people who must act; Cc = people who must know. Do not add executives to pressure someone; it damages trust.

### 5. Tone and register

| Situation | Guidance | Example |
|---|---|---|
| Peer, routine | Friendly and direct | "Hi Priya, can you review the PR by Thursday? Thanks." |
| Senior leader | Formal-neutral, short, respectful, not servile | "Hi Dana, I recommend option 1. I need your decision by Friday." |
| Sensitive news | Direct, human, factual | "I wanted you to hear this from me: the launch will slip by three weeks." |
| Disagreement | Focus on the issue, not the person | "I see a risk in this plan: the vendor has missed the date twice. Could we add a fallback?" |
| Complaint or escalation | Facts, impact, ask; no accusation | see the escalation template |
| Cross-cultural | Prefer explicit, plain language; avoid idioms and sarcasm | "Please confirm by Friday" not "Let's circle back and ping" |

**Phrases to retire or replace** (not "wrong" everywhere, but often read as archaic, indirect or odd in global English):

| Avoid | Prefer |
|---|---|
| Kindly do the needful. | Please process the request by Friday. |
| Please revert. | Please reply. / Let me know. |
| Please find attached herewith. | Attached is X. |
| As per our discussion (fine) / as per my last email (passive-aggressive) | As we discussed... / As I mentioned on 3 Sept... |
| Do let me know. | Let me know if... (both fine; "do" adds warmth in UK English) |
| I hope this email finds you well. | (Skip it or use "Hope you had a good weekend" for people you know.) |
| Regards (cold) / Best regards | Thanks / Best / Thanks again (after a favour) |
| Please ASAP | Please by 16:00 today |
| Same is completed / The same | It is completed / That is completed (missing referent is a common pattern) |
| Prepone (used in India) | Move earlier / bring forward |
| Out of station | Out of office / traveling |

### 6. Templates

**a) Status update**

```text
Subject: Status (week of 22 Sept): carrier integration amber

Summary: Amber. Development is 80% done; testing is blocked on vendor credentials.
Progress: Rate API and label service complete; tracking webhook in review.
Risks: Vendor sandbox credentials outstanding since 3 Sept. If not received by 30 Sept, 15 Nov launch is at risk.
Next: Load test (owner: Ravi, 29 Sept); vendor escalation (owner: Priya, 26 Sept).
Ask: Procurement to escalate to the vendor by Monday.
```

**b) Escalation email** (facts, impact, ask, deadline, no blame)

```text
Subject: Escalation: vendor credentials blocking EU launch (need action by Mon 29 Sept)

Hi Marcus,

I need your help to unblock the EU launch. The vendor has not delivered sandbox credentials requested on 3 Sept; we have followed up on 10, 15 and 22 Sept (thread below).

Impact: testing is blocked; if we do not have credentials by 30 Sept, the 15 Nov launch moves to January, delaying about EUR 1.2M of forecast revenue.
What we've tried: three emails to their support and two calls with the account manager.
Ask: can you contact their VP of Partnerships by Monday?
I can join a call with them; I'll send you a two-line brief today.

Thanks,
Rahul
```

**c) Follow-up / gentle reminder**

```text
Subject: Reminder: review of the tracking API design (due Wed)

Hi Sanjay, following up on my note of Monday. Could you review the design doc by Wednesday so we can freeze scope Thursday? If a few comments are easier, that's fine too. If you're too busy, could you tell me who else could review?
```

**d) Decline / say no politely**

```text
Hi Priya, thanks for thinking of me. I can't take the migration review this sprint because we're committed to the launch until 15 Nov. I could do it from 18 Nov, or I can recommend Ananya, who has done two of these. Which would you prefer?
```

Structure: appreciate, clear no with reason, alternative. See [Negotiation & saying no](negotiation-and-saying-no.md).

**e) Thank-you / follow-up after an interview** (see [Week 23](drills/week-23.md))

```text
Subject: Thank you: Staff Engineer conversation on Tuesday

Hi Elena, thank you for the conversation on Tuesday. I especially enjoyed discussing how your team handles multi-region failover. Our discussion of idempotency in the booking flow made me think about X, which I've outlined below. I'm excited about the role and happy to provide anything else. Best, Rahul
```

**f) Meeting request**

```text
Subject: 30 min this week: decide fallback for the tracking API

Hi Dana, can we meet for 30 minutes this week to decide on the fallback for the tracking API? I'll send a one-page brief in advance. Thursday 10:00-10:30 or Friday 14:00-14:30 work for me. What suits you?
```

### 7. Before/after rewrite

**Before**

> Subject: Issue
>
> Hi All,
> Hope you are doing well. There is one issue that we are facing wherein the booking API is throwing errors. Kindly look into it and revert at the earliest. Let me know if you need any further details.
> Regards, Rahul

**After**

> Subject: P1: booking API returns 500 for 8% of requests since 09:10 UTC
>
> Hi Payments team,
> The booking API is failing for about 8% of requests since 09:10 UTC (dashboard link below). Last deploy was at 08:55 UTC. Could someone from Payments join the bridge (link) by 09:45 to check the rate-limiter change? I'll post updates every 15 minutes.
> Rahul

Changes: subject states priority and symptom; facts (percentage, time, deploy); a specific ask with a time; removed "kindly look into it and revert" (unclear who, what, when); commitment to updates.

### 8. Email hygiene and productivity

- **Read as the recipient**: only the subject and first two lines. Do they get the ask?
- **Reply-all discipline**; **BCC** rarely; **forward** with a two-line note that says why you forward.
- **Delay send** for angry drafts: sleep on them; check facts and tone; remove sarcasm.
- **Escalate off email** when a thread passes three replies with no resolution: call or short meeting; send a summary email afterwards.
- **Attachments:** name files clearly (Design_TrackingAPI_v3_2026-09-25.pdf); link to the live doc where possible.
- **Time zones:** state times in UTC or both zones.
- **Signature:** name, role and team; avoid long legal footers when you can.
- **Confidentiality:** do not put secrets or personal data in email; use approved channels.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Plain Language guidelines (plainlanguage.gov)](https://www.plainlanguage.gov/guidelines/) | guide | Direct, reader-first advice, including for email and short documents | intermediate | free |
| [GOV.UK content design guidance](https://www.gov.uk/guidance/content-design) :gem: | guide | Front-load the message, write for the reader's task; excellent for email discipline | intermediate | free |
| [Grammarly blog](https://www.grammarly.com/blog/) | article | Articles on email etiquette, subject lines and tone; many with samples | beginner-intermediate | free |
| [Purdue OWL](https://owl.purdue.edu/) | reference | Professional writing and email pages | intermediate | free |
| [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) | guide | Tone, plain words and bias-free wording, useful for global audiences | intermediate | free |
| [Cambridge Dictionary](https://dictionary.cambridge.org/) | reference | Check register labels and usage notes (e.g. "revert", "prepone" are not in standard US/UK use) | all | free |
| [Atlassian Incident Management Handbook](https://www.atlassian.com/incident-management/handbook) | guide | Stakeholder communication templates for incidents | intermediate | free |
| Josh Bernoff, *Writing Without Bullshit* | book | Direct, reader-first business writing; strong on the "boss-first" front-loading | intermediate | paid |
| HBR article on military-style "BLUF" emails (Kabir Sehgal) | article | The origin of BLUF for business email (search HBR for the title) | intermediate | free/limited |

## Hands-on lab (60 min)

1. **Audit (15 min).** Take your last 10 sent emails. For each, note: does the subject state content and action? Is the ask in line 1-2? Is there one owner and one date? Score y/n. Note phrases from the "retire" list.
2. **Rewrite (25 min).** Pick the three worst; rewrite with BLUF and specific asks. Word count should drop 20-40%.
3. **Template library (15 min).** Save five templates (status, escalation, follow-up, decline, meeting request) in your notes app or email client.
4. **Test (5 min + week).** Send two rewritten emails; track response time and whether follow-up was required.

**Expected output:** three before/after emails, a template library and a note of your response-rate observations.

## Questions

### L1 — Recall

??? question "Q1. What does BLUF stand for and what should the first lines contain?"

    ??? success "Answer"
        Bottom line up front. The conclusion, decision or ask, so the reader can act even if they read only two lines.

??? question "Q2. Give the formula for a subject line that gets action."

    ??? success "Answer"
        Type/action + what + when or for whom, e.g. "Decision needed by Fri 3 Oct: defer EU cutover?". It should state content and action, with a date where relevant.

??? question "Q3. What three things should a request contain?"

    ??? success "Answer"
        One owner, one date, one clear action (plus a reason and what "done" looks like).

??? question "Q4. Why is "Please revert" risky in global email?"

    ??? success "Answer"
        In UK/US usage "revert" means to return to a previous state, so it may be unclear or read as odd; common in Indian English for "reply". Use "please reply" or "let me know".

### L2 — Apply

??? question "Q5. Rewrite the subject line "Regarding the issue" for a production incident."

    ??? success "Answer"
        "P1: checkout API error rate 12% since 14:05 UTC, mitigation under way". It has severity, symptom, since when and status.

??? question "Q6. Rewrite: "Kindly do the needful at the earliest and revert.""

    ??? success "Answer"
        "Could you update the ticket status by 17:00 today and reply when done?" Specific action, deadline, and reply instruction.

??? question "Q7. Write the first two lines of an email asking your VP to approve a $40k budget."

    ??? success "Answer"
        "Could you approve $40k for load-testing tooling by Friday? Without it, we cannot validate the peak-season capacity before 1 November." Ask, amount, deadline, consequence.

??? question "Q8. Fix: "Hi All, Please find attached herewith the document. Do the needful and let me know.""

    ??? success "Answer"
        "Hi all, attached is the vendor comparison. Could each of you add your scores by Wednesday? I'll consolidate on Thursday." Who, what, when; "herewith" and "do the needful" removed.

### L3 — Judge and choose

??? question "Q9. Should you cc your skip-level manager on a request to a peer who is late?"

    ??? success "Answer"
        Usually not as a first step: it reads as escalation by exposure. First send a clear reminder with a date; if there is no response, talk to the peer or their manager directly; if you cc, tell the recipient beforehand ("I'm adding Dana as this affects the launch date"). Escalation with transparency preserves trust.

??? question "Q10. One long email covering three topics vs three short emails. Which?"

    ??? success "Answer"
        Three, unless the topics are tightly linked and the reader is the same and expects a digest. Multi-topic emails get answers to the first topic and lose the rest. If you use one email, number the items and specify the ask for each.

??? question "Q11. Is it OK to use "Dear Sir/Madam" and "Yours faithfully" internally at a global company?"

    ??? success "Answer"
        Too formal for internal work; use "Hi [name]," and "Thanks/Best". "Dear [name]" is fine for formal external or legal contexts, first contact with a senior external person. Match the recipient's own style in their reply.

??? question "Q12. A colleague replies "Noted." to a request for a decision. Is that a yes?"

    ??? success "Answer"
        No: it acknowledges only. Follow up: "Thanks: to confirm, are you approving option 1?" Design emails so the reply can be one word ("approve") and ask for it explicitly.

### L4 — Staff-level

??? question "Q13. You must tell a VP that your team missed a commitment and the cause is partly another team. Draft the opening."

    ??? success "Answer"
        "The tracking launch will slip from 15 Nov to 6 Dec. Two causes: the vendor API change in September and our underestimate of the data migration. I'd like 15 minutes on Thursday to walk you through the recovery options; my recommendation is to cut reporting from scope." Facts, shared ownership, no blame on the other team, and a proposed decision.

??? question "Q14. You are copied on a heated thread between two directors. What is your role and what do you send?"

    ??? success "Answer"
        Do not reply-all. Contact each privately, or propose a call, and then send a neutral summary of decisions, owners and dates. If the thread affects your team's commitments, state facts and impact in a short separate message to the relevant leader. De-escalate: move to a live conversation; the written record follows.

??? question "Q15. Your emails get ignored by a busy executive. Diagnose and redesign your approach."

    ??? success "Answer"
        Likely: vague subject, ask buried, multiple asks, too long, no deadline, or wrong channel. Redesign: 1) Subject with the decision and date, 2) BLUF, 3) one ask with a default ("If I don't hear by Friday I'll proceed with option 1"), 4) three-line body, details in an attachment, 5) use their preferred channel or ask an assistant for a 10-minute slot. Also verify that the email is a decision they own.

## Real-world use cases

- **Approval request to a VP:** BLUF with options, cost, consequence and default.
- **Vendor escalation:** facts, timeline, impact, ask, next contact.
- **Cross-team dependency request:** owner and date, link to design doc, what "done" means.
- **Post-incident stakeholder update:** impact, cause, fix, prevention, next update.
- **Job search follow-ups:** thank-you and status emails with specific references.

## Pitfalls & anti-patterns

- Vague subject lines ("Update", "Issue", "Quick question").
- Burying the ask in paragraph four.
- "Someone" as the owner; no deadline.
- Copying executives to pressure a peer.
- Using region-specific stock phrases (kindly do the needful, prepone) with global readers.
- Over-apologising ("sorry to disturb") or over-thanking in advance ("thanks in advance" can sound presumptuous to some readers).
- Writing when angry, or sending a long email when a call would settle it.
- Forwarding a long thread with no summary.

## Checklist

- [ ] My last five emails have a subject line with content and action.
- [ ] Every request states owner, date and definition of done.
- [ ] I have five saved templates and used at least two this week.
- [ ] I have replaced my region-specific stock phrases with plain alternatives.
- [ ] I wrote one escalation email with facts, impact, ask and deadline.
- [ ] I answered all L3 questions out loud in < 3 min each.
