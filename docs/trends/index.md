---
title: Trends & tech radar
tags: [trends, radar]
last_reviewed: 2026-09-25
---

# Trends & tech radar

A **personal** radar for one learner (Python-first, Azure + cloud-agnostic, Java/Spring AI alongside; goal Staff/AI architect).
Rings answer *"what should I do with this in the next 24 weeks?"*, not *"is it good?"*.

| Page | What it is |
|---|---|
| [Radar (Sept 2026)](radar.md) | 56 blips across four quadrants and four rings, each with rationale, "as of" date and a source link |
| [What changed in 2025–2026](whats-new.md) | Dated timeline of releases/events that shaped the radar |
| [Daily feed](../reading/feed.md) | Auto-generated headlines; the input for radar moves |

## Rings

| Ring | Meaning for this learner |
|---|---|
| **Adopt** | Use by default in the capstone and labs; be able to defend it in an interview. |
| **Trial** | Build one small thing with it in the relevant phase; know its trade-offs. |
| **Assess** | Read the docs/spec, watch one talk; do not build on it yet. |
| **Hold** | Do not start new work with it; know *why* it fell out and what replaced it (interview material). |

## How the radar is maintained

- **Weekly agent** (Sunday ~07:00 IST, see `AGENTS.md` §6.2): re-verifies versions and status of every blip against primary sources
  (release notes, PyPI, official docs), moves rings when evidence changes, updates the "as of" date, and adds a dated line to the changelog below.
- **Daily agent** flags releases affecting any blip in its digest; it does *not* edit the radar, it only proposes a move in the digest.
- **Ring-move rules:**
    - Assess → Trial: stable release (not preview) + a second independent production report + fits a roadmap task.
    - Trial → Adopt: used in a lab or the capstone without regret, and a clear "when not to use" is known.
    - Any → Hold: vendor maintenance-mode announcement, retirement date, or repeated evidence it underperforms simpler baselines.
- **Blip format:** name, ring, quadrant, 1–2 line rationale, `as of` date, source link. Prefer primary sources. Version claims must say "as of".
- **Human override:** if you built something and disagree with a ring, edit the row and add a changelog line with your reason.

## Changelog

| Date | Change |
|---|---|
| 2026-09-25 | Initial radar published (56 blips). Versions checked against PyPI/official docs on this date: LangGraph 1.2.x, Pydantic AI 2.x, DSPy 3.4, Microsoft Agent Framework 1.x, Google ADK 2.x, MCP Python SDK 2.x, Zensical 0.0.x. |
