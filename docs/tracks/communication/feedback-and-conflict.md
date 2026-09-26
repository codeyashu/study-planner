---
title: "Feedback, disagreement & conflict"
track: communication
slug: feedback-and-conflict
priority: P0
complexity: 3
est_hours: 3
phase: 1
tags: [communication, P0, soft-skills, feedback, conflict]
last_reviewed: 2026-09-25
---

# Feedback, disagreement & conflict

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 3 h · **Phase:** 1 · **Prereqs:** [Conditionals, modals & hedging](conditionals-modals-hedging.md) · [Listening, questions & cross-cultural](listening-questions-cross-cultural.md)
    **You're done when:** you can deliver a piece of corrective feedback and a respectful disagreement, out loud, in under 60 seconds each, using an explicit structure (SBI, NVC-lite, or Disagree-and-commit) and adjust the directness for the audience.

## Why it matters
At Staff level most of your leverage is exercised through words, and the hardest words are the uncomfortable ones: telling a peer their design will not scale, telling a senior manager that a date is not credible, telling a report their code reviews are landing badly. In a second language the risk doubles. Either you soften so much the message disappears ("maybe we could possibly think about..."), or you translate your first-language directness word for word and sound harsher than you meant.

Two facts to hold onto:

- **Feedback is a specific, observable-behaviour conversation, not a verdict on the person.** Structures like SBI keep you on facts and stop you from arguing about character.
- **Disagreement is normal and valuable at Staff level; the skill is disagreeing in a way that keeps the relationship and the decision moving.** "Strong opinions, loosely held" and "disagree and commit" are standard vocabulary in global engineering organisations.

## Core concepts

### 1. SBI: Situation, Behavior, Impact
Developed by the Center for Creative Leadership. Three parts, each one sentence.

| Part | What it is | Test |
|---|---|---|
| **S**ituation | When and where, concrete | Could a camera have recorded it? |
| **B**ehavior | What the person did or said, observable | No adjectives about character ("careless", "arrogant") |
| **I**mpact | Effect on you, the team, the customer or the outcome | Real consequence, not a rule broken |

Then add an **invitation**: "How did you see it?" or "What was going on for you?" This turns a verdict into a conversation.

**Script (corrective):**
"In yesterday's design review (S), you interrupted Priya twice while she was explaining the retry logic (B). She stopped presenting, and we never got to the failure-mode discussion, which is the part I most wanted to hear (I). How did that feel from your side?"

**Script (positive):**
"In the incident bridge last night (S), you paused the debate and restated the three options with the risk of each (B). That let us decide in five minutes instead of twenty, and the on-call engineer could stop guessing (I). Please keep doing that."

Weak versus strong:

| Weak | Strong (SBI) |
|---|---|
| "You're not a team player." | "In the sprint planning on Tuesday, you declined all three reviews when Anna asked; the release was blocked for a day." |
| "Your docs are sloppy." | "In the payments RFC, section 3 had two contradictory retry values. Two teams implemented different ones." |
| "Great job on the migration." | "You wrote the rollback runbook before the cutover, and when the queue lag spiked we reverted in eight minutes." |

### 2. NVC-lite: Observation, Feeling/Need, Request
A trimmed version of Marshall Rosenberg's Nonviolent Communication, useful when the issue is a repeated behaviour that affects you personally.

1. **Observation** (no evaluation): "In the last three stand-ups, the update was 'still working on it'."
2. **Effect / need**: "I need enough visibility to warn the customer team if a date will slip."
3. **Request** (specific, doable, ask not demand): "Could you add one line on what is blocking you and when you expect it to clear?"

At work, prefer "I need / I'm concerned" to "I feel hurt". Drop the emotion vocabulary if your culture or team finds it too personal.

### 3. Disagreeing well
A ladder from mild to firm. Use the lowest rung that gets the message across, and go up if it is not heard.

| Rung | Phrase | Use when |
|---|---|---|
| 1 Curious | "Help me understand how this handles a partial failure?" | You have a doubt, not yet a position |
| 2 Alternative | "Another option we could look at is..." | You prefer something else but are not certain |
| 3 Concern | "I have a concern about the rollback path. If step 3 fails, we have no way back." | You see a real risk |
| 4 Position | "I disagree with this approach, for two reasons. First..." | You are confident and it matters |
| 5 Escalate calmly | "I do not think we are going to agree here. I would like to take this to Maria for a decision, and I will write up both options." | Deadlock; the decision needs an owner |

Rules of thumb:

- **Disagree with the idea, not the person.** "That approach worries me" not "You haven't thought this through".
- **Acknowledge before you challenge.** "I see why you want the simple option. My concern is..." (avoid "but" sarcasm; "and" or "my concern is" often sounds better).
- **Give the reason and the alternative.** A bare "no" starts a fight; "no, because X; what about Y?" starts a design discussion.
- **Do it in the right room.** Disagree in public about ideas; give feedback on style in private. Never surprise a senior in a group with a challenge you could have shared beforehand ("no surprises").

### 4. Disagree and commit
Once the decision owner has decided after hearing all views, you commit fully. The phrasing matters:

- "I still see it differently, and I want that recorded in the decision log. That said, I am on board and I will make it work."
- Not: "Fine, whatever you think." (passive-aggressive) or "Okay, but I told you so when it fails."

### 5. Receiving feedback
Staff engineers who cannot receive feedback stop getting it. Script:

1. **Listen through** without defending.
2. **Clarify**: "Can you give me an example so I can see it?"
3. **Thank** without agreeing or arguing: "Thanks, that is useful. Let me think about it and come back tomorrow."
4. **Act, then close the loop**: "Since you raised the review tone, I have started... Is that better?"

### 6. Conflict styles (Thomas-Kilmann)
Five modes: competing, collaborating, compromising, avoiding, accommodating. Staff-level judgment is picking the right one.

| Mode | Use when |
|---|---|
| Competing | Safety, security, legal, or an emergency; no time |
| Collaborating | Complex issue, both sides matter, time available |
| Compromising | Equal stakes and a deadline; a "good enough" split |
| Avoiding | Trivial issue or a cooling-off period is needed (name it: "Let's revisit this Thursday") |
| Accommodating | You are wrong or the issue matters more to them |

### 7. Cross-cultural notes
People differ; treat these as hypotheses to check, not labels.

- **Directness varies.** Many people in the Netherlands, Germany, Denmark and Israel are comfortable with blunt task feedback ("This does not work."). Many colleagues in India, Japan, Thailand, and parts of the Middle East and Latin America may hear that as rude and may themselves say "yes" or "we will try" when they mean "this is hard". US workplace feedback is often framed positively first ("feedback sandwich" culture), and a British "quite good" or "interesting idea" can mean "I have doubts".
- **Hierarchy shapes what can be said upward.** In more hierarchical settings, junior engineers may not contradict a senior in public. Give them a safe channel: "Please send me your concerns in writing before the review" or "Which risks would you flag if this were your design?"
- **Face.** In many cultures, correcting someone publicly costs them face. Move it to a one-to-one and ask a question instead of stating the error.
- **In global teams, say what you mean and check it.** "Just to be sure I have been clear: I am saying this design does not meet the availability target. Does that match what you heard?" is fine across every culture.
- **Read indirect "no"s.** "That may be difficult", "we will look into it", "let me check with the team" often mean no. Ask: "Is that a blocker, or is it manageable with more time?"

### 8. The feedback sandwich: use with care
Praise, criticism, praise is widely known but often backfires: people learn to brace for the "but". Better: a short honest opening ("I want to talk about the review comments"), the SBI, the invitation, and a genuine positive on its own occasion.

## Reference tables

**Softening ladder for corrective feedback**

| Direct | Softer | Softest |
|---|---|---|
| "This is wrong." | "I think there may be an issue here." | "I wonder if we have considered..." |
| "You missed the deadline." | "The deadline was missed, and it affected X." | "I noticed the date moved. What got in the way?" |
| "That will not work." | "I do not think that will scale." | "Would that still hold at 10x load?" |

**Phrases for the moment**

| Situation | Say |
|---|---|
| Interrupted, want to finish | "Let me finish this point and then I would like your view." |
| You are being talked over | "Sorry, I was not done. The key point is..." |
| Heated | "Let us pause for a moment. I think we agree on the goal; we differ on the route." |
| Buy time | "That is fair. I need to think about it. Can we continue tomorrow?" |
| Turn blame into problem | "Rather than who, can we look at what allowed it to happen?" |
| Check understanding | "Let me play back what I heard, and tell me if I have got it wrong." |
| Name the elephant | "I sense we are not fully aligned. Can we say out loud where we differ?" |

## Resources
| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Center for Creative Leadership: SBI feedback model](https://www.ccl.org) | article | Origin of Situation-Behavior-Impact; search "SBI" on the site | intermediate | free |
| *Crucial Conversations* (Patterson, Grenny et al.) | book | The classic on high-stakes dialogue: start with heart, make it safe | intermediate | paid |
| *Radical Candor* (Kim Scott) | book | Care personally + challenge directly; vocabulary many managers now share | intermediate | paid |
| *Nonviolent Communication* (Marshall Rosenberg) | book | Source of observation / need / request; read the first chapters | intermediate | paid |
| *Difficult Conversations* (Stone, Patton, Heen) | book | Separates the "what happened", feelings and identity conversations; excellent for engineers | intermediate | paid |
| [Harvard Business Review: search "giving feedback"](https://hbr.org) | article | Practical pieces on feedback; the Kim Scott and Jack Zenger articles are good starting points | intermediate | freemium |
| *The Culture Map* (Erin Meyer) :gem: | book | Eight scales incl. "Disagreeing" and "Evaluating" across cultures; the best text for global teams | intermediate | paid |
| [Amy Edmondson: Psychological safety talks (TEDx / HBS)](https://www.ted.com) :gem: | video | Why teams need safety to disagree; helps you argue for it as a Staff | intermediate | free |
| [BBC Learning English: The English We Speak](https://www.bbc.co.uk/learningenglish) | podcast | Short episodes on idioms for disagreement and diplomacy | intermediate | free |

## Hands-on lab
**Time: 60-90 min.**

1. **Feedback bank (20 min).** Write three SBI statements from the last month at work: one corrective to a peer, one positive to a report, one upward to a manager. Check each: is the behavior something a camera would record? Is the impact real?
2. **Record it (15 min).** Say each aloud (40 s max), record on your phone, listen. Mark: filler words, hedges ("maybe", "sort of"), and any place you made it about the person.
3. **Disagreement ladder (15 min).** Pick a real technical disagreement (e.g. queue vs. direct call). Write your position at rungs 1, 3 and 4. Read them aloud and feel the difference in tone.
4. **Role-play with an AI tutor (20 min).** Use the negotiation/conflict prompt in [AI tutor prompts](ai-tutor-prompts.md); have the AI play a defensive tech lead. Do it twice: once at your natural directness, once adjusted for a high-context, hierarchical colleague.
5. **Log (5 min).** Write the phrases that felt natural in `docs/log/`.

## Questions

### L1 — Recall
??? question "Q1. What do the letters in SBI stand for, and what is the test for the B?"
    ??? success "Answer"
        Situation, Behavior, Impact. The Behavior must be observable, something a camera or a recording would capture (what was said or done), not an interpretation or trait ("you were rude" is a judgment; "you raised your voice and said 'that is stupid'" is a behavior).

??? question "Q2. Name the three steps of NVC-lite as used at work."
    ??? success "Answer"
        Observation (no evaluation), effect or need, and a specific request. Example: "In the last three stand-ups the update was 'still working' (observation); I need to know early if a date will slip (need); could you add what is blocking you? (request)."

??? question "Q3. What is the risk of the classic 'feedback sandwich'?"
    ??? success "Answer"
        Recipients learn to expect a criticism after praise, so praise loses value and the criticism gets buried and under-heard. Prefer a direct opening, SBI, and praise given separately when earned.

??? question "Q4. What does 'disagree and commit' mean, and what does it not mean?"
    ??? success "Answer"
        After the decision owner decides, you state your disagreement once, ideally recorded, and then support the decision fully. It does not mean silent resentment, passive-aggressive compliance, or reopening the decision at every setback.

### L2 — Apply
??? question "Q5. Convert to SBI: 'You never update the ticket and it is really annoying.'"
    ??? success "Answer"
        "On the last three incidents (S), the ticket was not updated until after the call ended (B). Support could not tell customers whether we had a workaround, and two escalated to their account managers (I). Could we agree that you update it every 30 minutes during an incident?" Note the specific count, the observable behavior, a consequence, and a request.

??? question "Q6. Rewrite as a rung-3 concern: 'That design is going to fall over in production.'"
    ??? success "Answer"
        "I have a concern about how this behaves under load: the single writer becomes a bottleneck at around 2,000 messages a second, and we expect five times that at peak. Could we test it, or is there a partitioned option we can look at?" Concern + reason + number + constructive next step.

??? question "Q7. A colleague says 'that might be difficult' in response to your request for a two-week extension of scope. What should you do?"
    ??? success "Answer"
        Do not assume it is a yes or a soft maybe. In many contexts it is a polite refusal. Clarify without pressure: "When you say it might be difficult, is that a blocker, or something we could manage with more time or another person? I would rather know now." Then agree the next step in writing.

??? question "Q8. Correct the tone: 'You should have asked me before changing the schema.'"
    ??? success "Answer"
        Better: "The schema change on Monday broke the reporting job, and I only heard about it from the analysts. Next time, could you ping me on the PR so I can check downstream consumers? I would like to set up a checklist for schema changes." Removes "should have", states impact, requests a specific future action, and proposes a shared process.

### L3 — Design & trade-offs
??? question "Q9. Give feedback publicly or privately? Decide for: (a) a factual error in a design doc during a review with 15 people, (b) a pattern of dismissive comments on pull requests."
    ??? success "Answer"
        (a) Publicly, but with a question form and focus on the artifact: "Section 3 says P99 is 200 ms; the dashboard I have shows 450 ms. Can we reconcile that?" Correcting facts publicly protects everyone from acting on a wrong statement. (b) Privately: a pattern about how someone treats colleagues is personal and public correction costs face and reduces the chance of change. Use SBI with two or three concrete PR examples. Exception to (a): if the author is junior or from a high-face culture, send a heads-up before the meeting.

??? question "Q10. Your peer principal engineer proposes an architecture you think is wrong; your director prefers it. Choose between competing, collaborating and avoiding, and defend."
    ??? success "Answer"
        Collaborating first: it is a complex issue, and your relationship with the peer matters. Ask questions, offer to run a small spike or a written trade-off analysis. If you are still convinced there is a serious risk (data loss, security), escalate the concern in writing with options, not a complaint: competing is justified for safety issues, not for taste. Avoiding is wrong unless the issue is minor; silence now becomes "I told you so" later. After the decision, disagree and commit.

??? question "Q11. Compare NVC-lite and SBI: when would you choose each?"
    ??? success "Answer"
        SBI is best for performance-type feedback to any audience: fast, factual, culture-neutral. NVC-lite fits repeated behaviours that affect your ability to work ("I need...") and where you want to state your own need and make a request. In hierarchical cultures the "need/request" phrasing may sound demanding upward; SBI plus a question is safer. In either case the invitation to respond matters more than the structure.

??? question "Q12. A report is a strong engineer but two peers say he is intimidating in reviews. What are the risks of each of: telling him what peers said, waiting for a 1:1 next month, having the peers speak with him?"
    ??? success "Answer"
        Reporting what peers said protects nothing if it is vague hearsay and can break trust; use your own observations plus permission-based examples. Waiting a month lets the pattern continue and the team learn that nothing happens. Peer-to-peer can work if they are willing but risks defensiveness and a proxy conflict. Best: gather two specific PR examples, do SBI within a week, ask how he sees it, agree a small experiment (e.g. lead with questions in reviews for four weeks) and revisit.

### L4 — Staff-level ambiguity
??? question "Q13. In a global review, an architect in another office, senior to you, says in front of 30 people that your team's estimate is unrealistic. You believe he has misread the scope. Script your next 60 seconds and your follow-up."
    ??? success "Answer"
        In the meeting: stay calm, do not counter-attack. "Thank you, that is a fair challenge. The estimate assumes we reuse the existing gateway; if that assumption is wrong then you are right. I would like to walk through the assumptions with you after this meeting, and then bring the outcome back to the group." This acknowledges, states the reason, moves to a private forum, and promises closure. Afterward: a short one-to-one call; ask for his view first; walk through the scope; agree on a revised note. If he was wrong, let him say it privately and correct it in the doc without triumph. Do not send a broad email that shames him.

??? question "Q14. Your VP wants a launch date you believe is impossible. You have been told 'just make it work'. Write what you say."
    ??? success "Answer"
        "I want to help us hit the date, and I need to be direct about the risk. Based on the work remaining, I put the chance of hitting the fifteenth at about thirty percent. Here are three ways to increase it: reduce scope by cutting the partner integration, add two engineers for three weeks, or move the date by two weeks. Which of these would you like me to plan around? I will commit to whichever you choose." Direct, quantified, options not complaints, ends with a decision request and commitment. Follow with the same in writing.

??? question "Q15. Two of your senior engineers are in a long-running feud that slows the team. Outline your conversations and the language you use."
    ??? success "Answer"
        Separate one-to-ones first, listening only: "Tell me how you see the situation." Use neutral wording ("the disagreement about ownership of the scheduler") not accusation. Identify shared goals and specific behaviours that hurt the team, using SBI. Then a joint session with ground rules: each summarises the other's position before rebutting. If there is genuine technical disagreement, define a decision process (owner, criteria, deadline). If it is personal, coach or involve the manager. Avoid taking sides in email, and avoid "you two need to sort it out" without support.

## Real-world use cases
- **Design review pushback**: rung 3 concern with a number and an alternative, keeping the relationship for the next review.
- **Post-incident feedback**: using SBI in a blameless review to address a runbook that was not followed, focused on system fixes.
- **Global handoffs (India/EU/US)**: converting "I will try" into an explicit commitment or a stated constraint, by asking "what would make this a yes?"
- **Promotion feedback**: giving a direct, kind message to a strong senior engineer who is not yet ready for Staff, with three specific evidence gaps.
- **AI-tooling rollout**: disagreeing with a mandate to use a coding agent on the payments path, framed as risk, evidence, and a pilot proposal.

## Pitfalls & anti-patterns
- Feedback that is a personality verdict ("you are disorganised").
- Delayed feedback: a two-month-old example loses force and looks like ambush at review time.
- Over-softening: "It might perhaps be worth possibly considering..." reads as no position; a non-native speaker's over-hedging is often heard as low confidence.
- Cultural mimicry: pretending to be blunt (or elaborately polite) because someone told you the culture is X.
- Using "with all due respect" or "no offence" as a preface: these usually announce disrespect.
- "Just curious..." for a rhetorical challenge; be honest about what you think.
- Public corrections of style; private corrections of facts that could mislead others should not wait.
- Committing weakly after a decision ("as you wish"): erodes trust.
- Sending a written rebuke when a call would do; equally, a call with nothing written afterwards.

## Checklist
- [ ] I can state SBI and NVC-lite from memory and give one example of each about my own work
- [ ] I wrote and recorded three SBI statements and removed all judgment adjectives
- [ ] I can climb the disagreement ladder (rung 1 to 5) on a real topic
- [ ] I can convert an indirect "maybe" into a clear next step by asking a follow-up question
- [ ] I answered all L3 questions out loud in under 3 minutes each
- [ ] I practised the L4 VP-deadline script with an AI tutor and revised the wording twice

!!! tip "See also"
    Staff-skills: [Influence without authority](../staff-skills/influence-without-authority.md) · [Mentoring & sponsorship](../staff-skills/mentoring-sponsorship.md) · [Incident leadership](../staff-skills/incident-leadership.md). Language: [Conditionals, modals & hedging](conditionals-modals-hedging.md) · [Negotiation & saying no](negotiation-and-saying-no.md).
