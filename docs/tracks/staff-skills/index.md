---
title: Staff+ Skills
track: staff-skills
last_reviewed: 2026-09-25
---

# Staff+ Skills

The non-code half of the goal. Twelve topics, about 25 hours across the 24 weeks, aimed at one outcome: operate with Staff/Principal scope and interview convincingly for it, both as a Staff engineer and as an AI architect.

!!! abstract "How to use this track"
    Each topic ends in a **Staff artifact**: a real document you produce, not a summary you read. By Week 24 you should hold eight artifacts that double as interview material and as working tools in your current org. Read a page (~30 min), do the lab, then use the artifact in real work within a week. An artifact nobody has seen is not finished.

## Reading order

Read top to bottom; each page's *You're done when* line is the exit check before moving on.

1. [Staff archetypes & operating at Staff+](staff-archetypes.md) — P0, ~2 h
2. [Writing engineering strategy & vision](technical-strategy.md) — P0, ~3 h
3. [Design docs & RFCs that get approved](design-docs-rfcs.md) — P0, ~2 h
4. [Influence without authority & alignment](influence-without-authority.md) — P0, ~2 h
5. [Managing technical debt & quality](technical-debt.md) — P0, ~2 h
6. [Mentoring, sponsorship & growing engineers](mentoring-sponsorship.md) — P1, ~2 h
7. [Incident leadership & blameless postmortems](incident-leadership.md) — P1, ~2 h
8. [Communicating with executives & stakeholders](communication-stakeholders.md) — P0, ~2 h
9. [Decision-making under ambiguity](decision-making.md) — P0, ~2 h
10. [Running architecture reviews & guilds](architecture-reviews.md) — P1, ~1 h
11. [Leading engineering in the AI era: adoption, productivity, risk](ai-era-leadership.md) — P0, ~2 h
12. [Behavioral & Staff interviews: STAR stories bank](behavioral-interviews.md) — P0, ~3 h

## The one-paragraph model

At Senior, output is your own designs and code. At Staff+, output is the change in what the organisation ships because you were there: direction (strategy, design docs), alignment (influence, communication, reviews), risk handling (debt, incidents, AI governance) and grown people (mentoring, sponsorship). Coding agents compress the "hands" part of the job in 2026, which raises the value of framing, judgement, evals and alignment: exactly Staff work.

## Archetypes at a glance

From Will Larson's *Staff Engineer*; details in [Staff archetypes](staff-archetypes.md).

| Archetype | Core loop | Where you'll likely use it |
|---|---|---|
| **Tech Lead** | Guides one team's execution with an EM | Leading the first team that builds on your agent platform |
| **Architect** | Owns direction and quality of a critical domain across teams | Your primary mode as AI architect: platform, gateway, evals, governance |
| **Solver** | Goes deep on the hardest problem, then moves on | Stabilising a fragile system; occasional |
| **Right Hand** | Extends an executive's reach across the org | Likely drift if the CTO org adopts you as "the AI person" |

Target blend: **Architect + Tech Lead**, with Right Hand behaviours (exec communication, mandate-seeking) as scope grows.

## Topics

| Topic | Priority | Complexity | Phase | Hours |
|---|---|---|---|---|
| [Staff archetypes & operating at Staff+](staff-archetypes.md) | P0 | 2 | 1 | 2 |
| [Design docs & RFCs that get approved](design-docs-rfcs.md) | P0 | 2 | 2 | 2 |
| [Influence without authority & alignment](influence-without-authority.md) | P0 | 3 | 3 | 2 |
| [Communicating with executives & stakeholders](communication-stakeholders.md) | P0 | 3 | 3 | 2 |
| [Writing engineering strategy & vision](technical-strategy.md) | P0 | 4 | 4 | 3 |
| [Managing technical debt & quality](technical-debt.md) | P0 | 3 | 4 | 2 |
| [Leading engineering in the AI era: adoption, productivity, risk](ai-era-leadership.md) | P0 | 3 | 4 | 2 |
| [Incident leadership & blameless postmortems](incident-leadership.md) | P1 | 2 | 4 | 2 |
| [Running architecture reviews & guilds](architecture-reviews.md) | P1 | 2 | 4 | 1 |
| [Mentoring, sponsorship & growing engineers](mentoring-sponsorship.md) | P1 | 2 | 5 | 2 |
| [Decision-making under ambiguity](decision-making.md) | P0 | 3 | 5 | 2 |
| [Behavioral & Staff interviews: STAR stories bank](behavioral-interviews.md) | P0 | 2 | 6 | 3 |

Cross-topic practice: [Question bank](questions.md) (graded questions, org scenarios, rapid-fire).

## The eight Staff artifacts

Target weeks are approximate and follow the phase each topic is first scheduled in (roughly four weeks per phase); the authoritative schedule is `data/curriculum.yml`. Weeks 4/8/12/16/20/24 are interview checkpoints.

| # | Artifact | Topic page | Target week | "Done" means |
|---|---|---|---|---|
| 1 | **Staff role charter + brag doc** | [Staff archetypes](staff-archetypes.md) | Week 2 | Archetype blend, 2–3 bets, "not doing" list; reviewed with your manager; 5+ brag entries |
| 2 | **Capstone design doc + ADR** | [Design docs & RFCs](design-docs-rfcs.md) | Week 6 | TL;DR, NFR numbers, 2+ real alternatives, eval plan; reviewer-persona critique; ADR written |
| 3 | **Stakeholder map + monthly exec update + decision memo** | [Influence](influence-without-authority.md), [Communication](communication-stakeholders.md) | Week 10 | One real pre-wire held; update and memo pass the 2-minute test; a 3-minute verbal brief recorded |
| 4 | **Tech-debt register + investment case** | [Technical debt](technical-debt.md) | Week 14 | 10+ scored items incl. AI-specific debt; one-page business case a director could approve |
| 5 | **Game-day + blameless postmortem** | [Incident leadership](incident-leadership.md) | Week 15 | Two failure injections (one AI-quality), IC log, postmortem with 3–7 owned, dated actions |
| 6 | **Agent platform engineering strategy (v0.3)** | [Technical strategy](technical-strategy.md) | Week 16 | 3–5 pages, 5+ policies that each rule something out; tested on 2 real decisions |
| 7 | **AI adoption & governance playbook** | [AI-era leadership](ai-era-leadership.md) | Week 17 | Coding-agent policy, measurement plan, vendor scorecard, risk tiers |
| 8 | **STAR story bank v1** | [Behavioral interviews](behavioral-interviews.md) | Week 21 (mock loops by Week 24) | 10+ stories covering all 15 prompts, rubric-scored, rehearsed aloud |

Bonus artifacts (smaller, feed the eight above): growth plans and 1:1 agenda ([Mentoring](mentoring-sponsorship.md), Week 19), review-forum charter with AI checklist ([Architecture reviews](architecture-reviews.md), Week 15), decision memo and decision journal ([Decision-making](decision-making.md), Week 18).

## Suggested rhythm

- **Reading (weekday, ~30 min):** one topic page, resources skimmed by priority.
- **Lab (weekend, 60–120 min):** produce the artifact draft.
- **Use it (within a week):** send it to a real reviewer: manager, peer, sponsor.
- **Log it:** add one brag-doc entry per artifact; these become story-bank material.

## Recurring themes

- **Writing is the medium.** Docs, memos, strategies and updates are your primary output.
- **Reversibility and evidence** drive decisions; tripwires beat certainty.
- **Amplifier principle.** AI amplifies the strengths and weaknesses of your engineering system (DORA 2025), so platform, evals and review norms are leadership work.
- **Give credit, make glue work visible, sponsor others.**

## Practice for this chapter

The [eight Staff artifacts](#the-eight-staff-artifacts) above are this chapter's practice.

**[Interview prep](interview-prep/index.md) lives at the end of this chapter** — it's the same rubric used to score every other track's mock rounds, plus the behavioral/Staff prompt bank and checkpoint schedule for the whole roadmap.

## Resource list

Curated resources for the whole track live in `data/resources/staff-skills.yml`; each topic page shows the subset most relevant to it. Sources are tagged `:gem:` where they are lesser known but excellent (noidea.dog, Larson's essays, Hogan, Ojstersek, Rossi).
