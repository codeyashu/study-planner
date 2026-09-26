# Study Planner — Senior → Staff + AI Architect (24 weeks)

Personal, self-updating learning system published at **https://codeyashu.github.io/study-planner/**.

- **Tracks:** Agentic AI & LLM engineering · System design · AI system design · Architecture · Advanced Python · Java/Spring AI · DSA · Staff+ skills · **Communication & English (daily 30 min)**
- **Every topic:** priority, complexity, curated resources (clarity-first, with lesser-known gems), hands-on lab, L1–L4 questions with answers, use cases
- **Daily:** a GitHub Action builds *Today* + an RSS feed and opens a "Day N" issue; a scheduled Claude agent writes a curated digest
- **Weekly:** link check, tech-radar refresh, new questions, plan rebalancing
- **Progress:** tick boxes in the daily issue and close it → `data/progress.yml` → dashboard streak/heatmap

## Quick start

```bash
uv sync
uv run mkdocs serve          # http://127.0.0.1:8000
uv run pytest                # generator tests
```

## How it's wired

| Source | Generator | Output |
|---|---|---|
| `data/topics.yml` | — | topic contract (slugs, priority, complexity, phase) |
| `data/curriculum.yml` | `scripts/build_plan.py` | `data/plan.yml`, `docs/roadmap/weeks/*`, nav files |
| `data/plan.yml` + `data/progress.yml` | `scripts/gen_today.py` | `docs/today.md`, dashboard snippet, daily issue body |
| `data/communication.yml` | `scripts/build_plan.py` (merged into the plan) | 7 daily communication tasks per week |
| `data/feeds.yml` | `scripts/build_feeds.py` | `docs/reading/feed.md` |
| `docs/tracks/communication/drills/*` | `scripts/export_vocab.py` | `build/vocab.csv` (Anki) |
| `data/progress.yml` | `scripts/stats.py` | `docs/assets/stats.json` |
| daily issue body | `scripts/sync_progress.py` | `data/progress.yml` |
| `data/resources/*.yml` + docs | `scripts/check_links.py` | `build/link-report.md` |

Agents working on this repo follow [AGENTS.md](AGENTS.md).
