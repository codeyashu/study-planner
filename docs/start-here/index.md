---
title: Start here
last_reviewed: 2026-09-25
---

# Start here

This site is a **living learning system**, not a static reading list. Three things keep it moving:

1. **A generated plan.** Every day has concrete tasks (`data/curriculum.yml` → `data/plan.yml` → [Today](../today.md) and the [week pages](../roadmap/index.md)).
2. **Daily automation.** At 06:00 IST a GitHub Action rebuilds *Today*, pulls ~30 RSS feeds into the [feed](../reading/feed.md), and opens a **"Day N" GitHub issue** with your checklist. At ~06:15 IST a scheduled Claude agent writes the [daily digest](../digest/index.md): 3–5 must-reads matched to *today's* topic, a question of the day, and any release that changes something on the site.
3. **A weekly refresh.** On Sundays an agent re-checks versions and links, updates the [tech radar](../trends/radar.md), adds new questions, and rebalances next week if you slipped.

## Read in this order

| # | Page | Why | Time |
|---|---|---|---|
| 1 | [The brief](brief.md) | What we're optimising for, constraints, success criteria | 5 min |
| 2 | [How to use this site](how-to-use.md) | Daily loop, issues → progress, spaced repetition, question levels | 10 min |
| 3 | [Weekly rhythm](../roadmap/weekly-template.md) | Where each track's hours go | 3 min |
| 4 | [Phases & gates](../roadmap/phases.md) | What "done" means for each phase | 5 min |
| 5 | [Week 0 baseline](baseline.md) | Measure yourself before starting | 3–4 h, this weekend |
| 6 | [Research: how others build roadmaps](research.md) | What this roadmap borrows and fixes | 10 min |
| 7 | [Freshness contract](freshness.md) | How content avoids going stale | 3 min |

## The one-screen summary

- **Goal:** Staff/Principal engineer + AI architect who ships production agentic systems. Interview-ready by week 24, measured at 6 checkpoints on one rubric.
- **Time:** 12–15 h/week. Weekdays about 1.5 h, Saturday about 3 h (build), Sunday about 2.5 h (build + review).
- **Tracks:** Agentic AI (4 h) · System design + AI SD (2.5 h) · DSA (2.5 h) · Architecture (1.5 h) · Python (1.5 h) · Java/Spring AI (1 h) · Staff+ (0.5 h) · Review (1 h).
- **Output:** the *Agentic Ops Copilot* capstone, 6 phase projects, 15+ ADRs, 8 Staff artifacts, 2+ blog posts, and about 250 DSA problems.
