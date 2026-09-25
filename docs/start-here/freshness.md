---
title: Freshness contract
last_reviewed: 2026-09-25
---

# Freshness contract

AI tooling changes monthly, so this site promises the following:

| Mechanism | Cadence | Who |
|---|---|---|
| RSS feed page ([feed](../reading/feed.md)) rebuilt | Daily 06:00 IST | GitHub Action `daily.yml` |
| Curated digest: 3–5 must-reads for *today's* topic, releases, question of the day | Daily ~06:15 IST | Scheduled Claude agent (AGENTS.md §6.1) |
| A release that changes a fact (version, API, deprecation) → topic page updated + `last_reviewed` bumped | Same day | Daily agent |
| Link check of all resources and pages → issue if broken | Sundays | Action `weekly-links.yml` |
| [Tech radar](../trends/radar.md) re-verified, rings moved with changelog | Sundays | Weekly agent (AGENTS.md §6.2) |
| ≥ 20 new graded questions for next week's topics | Sundays | Weekly agent |
| Plan rebalanced if > 3 days behind | Sundays | Weekly agent |
| Every page shows `last_reviewed` and git "last updated" | Always | Front-matter + git-revision-date plugin |

**Staleness rule:** any topic page with `last_reviewed` older than 90 days is re-reviewed by the weekly agent before it's scheduled again.

**Version claims** are always written as "as of Month YYYY" so they can be audited.
