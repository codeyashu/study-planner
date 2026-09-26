# AGENTS.md — Operating protocol for AI agents working on this repo

This repo is Rahul's personal 24-week learning system (Senior → Staff/Principal engineer + AI architect + hands-on agentic AI engineer).
It is published as a MkDocs Material site on GitHub Pages. Any agent (Claude Code, a scheduled routine, a GitHub Action) that touches
this repo MUST follow this file.

## 1. Learner profile (keep decisions consistent with this)

- 15 years experience; already strong in system design and Python. Skip beginner material; go for depth, trade-offs, production reality.
- Goal: Staff/Principal + AI architect + ship production agentic systems; interview-ready as a checkpoint (weeks 4/8/12/16/20/24).
- Time: ~17–18 h/week (12–15 h technical + 30 min/day Communication & English). Weekdays ~2 h, Saturday ~3.5 h build block, Sunday ~3 h build + review.
- Stack: Python-first (uv, Pydantic v2, FastAPI, Pydantic AI, LangGraph, DSPy), Azure (Microsoft Foundry) + local/cloud-agnostic (Docker, Ollama, pgvector), Java 25 / Spring Boot 4 / Spring AI 2.0 alongside. Full DSA track (NeetCode 250 path, Python).
- Timezone: IST (UTC+05:30). Roadmap start: Week 0 = Sat 2026-09-26; Week 1 = Mon 2026-09-28; Week 24 ends Sun 2027-03-14; buffer weeks 25–26.
- English: B2+ heading to C1 — understands well; gaps in speaking fluency, vocabulary range and writing precision. Wants medium-to-high difficulty communication practice (grammar, vocabulary, idioms, phrasal verbs, pronunciation, business writing, soft skills).
- Prefers resources that EXPLAIN well (visual, intuitive, practical), including lesser-known gems — not only famous ones.

## 2. Repository map

| Path | Purpose | Edited by |
|---|---|---|
| `data/topics.yml` | Topic contract: every topic slug, priority, complexity, phase | humans / weekly agent |
| `data/curriculum.yml` | Week-by-week tasks per track (source for plan) | humans / weekly agent |
| `data/communication.yml` | Weekly arc for the Communication & English track (merged into the plan as 7 daily 30-min tasks) | humans / weekly agent |
| `data/plan.yml` | GENERATED day-by-day plan (`scripts/build_plan.py`) | script only |
| `data/progress.yml` | Completed task ids + dates | `scripts/sync_progress.py`, human |
| `data/feeds.yml` | RSS sources | humans / weekly agent |
| `data/resources/<track>.yml` | Curated resources with metadata | track authors / weekly agent |
| `docs/tracks/<track>/<slug>.md` | Topic pages (template §4) | agents / human |
| `docs/tracks/<track>/questions.md` | Cross-topic interview & scenario question bank | agents |
| `docs/tracks/communication/drills/week-NN.md` | Daily English/communication drills (day types fixed; see comm section §6.4) | agents / human |
| `docs/roadmap/weeks/week-NN.md` | GENERATED week pages | script only |
| `docs/today.md` | GENERATED daily page | script only |
| `docs/digest/posts/YYYY-MM-DD.md` | Daily digest posts (blog) | daily agent |
| `docs/trends/radar.md` | Tech radar | weekly agent |
| `docs/log/` | ADRs, weekly retros, learning log | human (agent may draft) |

Generated files: never hand-edit; change the source and re-run the script.

## 3. Content rules (all pages)

1. **Depth for a 15-yr engineer.** Explain *why* and *trade-offs*. No "what is a database" filler. Every concept ties to a production scenario.
2. **Clarity-first resources.** For each topic: 5–10 resources, mix of free/paid, favour the clearest explainer over the most famous. Tag lesser-known but excellent ones with `:gem:` ("gem"). Prefer official docs for APIs.
3. **Never invent URLs.** Only include links you are confident exist (official docs, known blogs, verified pages). If unsure, link the site root or omit. Dated/versioned claims must say "as of <Month YYYY>".
4. **Freshness.** Every page has `last_reviewed:` in front-matter. When you change facts, update it. Mention versions (e.g. "LangGraph 1.x", "Spring AI 2.0 (GA June 2026)").
5. **Questions are graded** (see §5) and ALWAYS have a model answer in a collapsible block.
6. **MkDocs syntax** (Material + pymdownx): admonitions `!!! note`, collapsibles `??? question "…"` / `??? success "Answer"`, task lists `- [ ]`, tabs `=== "Python"`, Mermaid in ```` ```mermaid ```` fences, tables. Relative links between pages use `.md` paths (e.g. `../system-design/caching.md`). No raw HTML unless necessary. No emoji other than `:gem:` markers and Material icon shortcodes.
7. **Tone:** direct, dense, structured. Headings + bullets + tables. Long is fine; padding is not.

## 4. Topic page template (MANDATORY structure)

```markdown
---
title: <Title from topics.yml>
track: <track>
slug: <slug>
priority: P0|P1|P2
complexity: 1-5
est_hours: <n>
phase: <n>
tags: [<track>, <priority>]
last_reviewed: YYYY-MM-DD
---

# <Title>

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 4 h · **Phase:** 2 · **Prereqs:** [link](...)
    **You're done when:** <one-sentence measurable outcome>

## Why it matters
Why a Staff/AI architect needs this in 2026; where it shows up in real systems and interviews.

## Core concepts
Own-words explanation, organised in sub-headings. Include at least one Mermaid diagram or comparison table where it helps.
Cover the trade-offs, numbers/thresholds of thumb, and "senior-level nuance" (what juniors miss).

## Resources
| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Name](url) :gem: | article/video/book/course/docs/interactive | … | intermediate/advanced | free/paid |

## Hands-on lab
Concrete exercise (30–120 min) with steps and expected output; tie to the capstone where possible.

## Questions
### L1 — Recall
??? question "Q1. …"
    ??? success "Answer"
        …
### L2 — Apply
### L3 — Design & trade-offs
### L4 — Staff-level ambiguity
(≥ 3 L1, ≥ 3 L2, ≥ 3 L3, ≥ 2 L4 per topic)

## Real-world use cases
3–5 scenarios (company/domain examples, incl. logistics/enterprise where natural) with how the concept applies.

## Pitfalls & anti-patterns
Bullet list.

## Checklist
- [ ] I can explain … without notes
- [ ] I built/ran …
- [ ] I answered all L3 questions out loud in < 3 min each
```

Nesting note: inside `??? question`, indent the `??? success "Answer"` block by 4 spaces and its body by 8.

## 5. Question levels

| Level | Tests | Example stem |
|---|---|---|
| L1 Recall | definitions, mechanisms | "What does a write-ahead log guarantee?" |
| L2 Apply | use in a concrete situation, code, numbers | "Size a Redis cluster for 50k QPS, 1 KB values, 99p < 5 ms." |
| L3 Design | trade-offs between options, failure modes | "Hybrid search vs pure dense for a legal corpus — decide and defend." |
| L4 Staff | ambiguity, org impact, migration, influence | "Three teams built three RAG stacks. Propose a convergence plan." |

Use-case/scenario questions describe a realistic situation (inputs, constraints, scale) and ask for a decision.

## 6. Procedures for automated agents

### 6.1 `daily` (runs ~06:15 IST, after `daily.yml` Action)
1. Read `data/plan.yml`, `data/progress.yml`, `docs/today.md` to know today's week/day/topics.
2. Web-research the last ~24–48 h: notable releases (frameworks in `docs/trends/radar.md`), strong articles/papers/videos relevant to the current phase and topics. Check the feeds in `data/feeds.yml` first.
3. Write `docs/digest/posts/YYYY-MM-DD.md`:
   ```markdown
   ---
   date: YYYY-MM-DD
   categories: [Daily]
   tags: [<tracks touched>]
   ---
   # Day N — <short theme>
   **Today's focus:** <from today.md> · **Phase:** n · **Week:** n
   <!-- more -->
   ## Must-read (3–5)
   1. [Title](url) — source · ~N min · track · *why it matters for today's topic*
   ## Worth knowing (releases / news, ≤ 5 bullets)
   ## Question of the day
   ??? question "…" (L2/L3, tied to today's topic, with answer)
   ## Tip for today's task
   ## English word of the day
   **Word/idiom:** … · **Meaning:** … · **Example (work context):** … · **Grammar/style tip (1–2 lines, C1 level):** …
   ```
3b. English section: choose a C1-level word or idiom that is *not* in `docs/tracks/communication/drills/` for the current or earlier weeks, relevant to the day's technical theme, in genuinely current workplace usage; mark register (formal/informal, US/UK). Verify it in a dictionary (Cambridge/Oxford/Merriam-Webster).
4. Only link to pages you actually opened. No duplicates of the previous 7 digests.
5. If a release changes a fact on a topic page (version, API, deprecation), update that page and its `last_reviewed`.
6. Comment the digest link on today's GitHub issue "Day N — …" if tools allow.
7. Commit: `digest: YYYY-MM-DD` and push to `main`.

### 6.2 `weekly` (Sunday ~07:00 IST)
1. Run `uv run python scripts/check_links.py` → fix or replace broken resources.
2. Re-verify versions/status for items in `docs/trends/radar.md`; move rings (adopt/trial/assess/hold) with a dated changelog line.
3. Add ≥ 20 new graded questions across next week's topics (in topic pages or track `questions.md`).
4. Read `data/progress.yml`: if the learner is > 3 days behind, rebalance next week in `data/curriculum.yml` (push P2 items to buffer weeks; never drop P0), then `uv run python scripts/build_plan.py`.
5. Draft `docs/log/retros/week-NN.md` from the template with stats (tasks done by track, streak).
6. Add 3–5 new newsletters/articles worth reviewing to `docs/reading/` if genuinely good.
6b. Communication: read the learner's error log (`docs/log/comm-errors.md`, if present) and the past week's drill scores; adjust next week's focus in `data/communication.yml` if a pattern needs reinforcement, then rebuild the plan.
7. Commit: `weekly: refresh week NN` and push.

### 6.4 Communication & English track
- Daily task ids are `wNN-comm-1..7` (Mon Grammar, Tue Vocabulary, Wed Speaking, Thu Idioms & phrasal verbs, Fri Writing, Sat Speaking record, Sun Soft skills + weekly review). Each links to `drills/week-NN.md#day-N`.
- Drill heading format is strict: `## Day N — <Type>: <focus> {#day-N}`. Vocabulary/idiom tables use the exact headers `| Word | Part of speech | Meaning | Example |` and `| Expression | Meaning | Example |` so `scripts/export_vocab.py` can build the Anki deck.
- Difficulty ramps medium (wk 1–8) → medium-high (wk 9–20) → high (wk 21–26). Vocabulary never repeats across weeks; later drills recycle earlier words.
- Accuracy rule: grammar explanations and idiom usage must be verifiable in Cambridge/Oxford/Merriam-Webster; never invent idioms.

### 6.3 `on-demand` ("update roadmap", "add topic X", "I finished X")
- New topic → add to `data/topics.yml`, create page per §4, schedule in `data/curriculum.yml`, rebuild plan.
- Progress report → update `data/progress.yml` (task ids), run `scripts/stats.py`.
- Always run `uv run mkdocs build --strict` before committing.

## 7. Commands

```bash
uv sync                                   # install
uv run mkdocs serve                       # local preview at http://127.0.0.1:8000
uv run mkdocs build --strict              # must pass before commit
uv run python scripts/build_plan.py       # curriculum.yml -> plan.yml + week pages
uv run python scripts/gen_today.py        # today page (use --date YYYY-MM-DD to test)
uv run python scripts/build_feeds.py      # RSS -> docs/reading/feed.md
uv run python scripts/stats.py            # progress -> docs/assets/stats.json
uv run python scripts/check_links.py      # link check of resources
uv run python scripts/export_vocab.py     # drill vocab/idiom tables -> build/vocab.csv (Anki)
uv run pytest                             # script tests
```

## 8. Roadmap page style (added 2026-09-26)

`docs/roadmap/index.md` is the front door and must stay in this shape — dense, track-lettered, operator-manual, not a plain link list:

- **Spine** (3–5 resources that pay off across the *whole* plan) at the top, not per-topic resource sprawl.
- **Phase 0 setup** as copy-paste shell commands, not prose.
- **Lettered tracks (A, B, C…)**, each: one `Do:` line, a `Deliverable:`, and a link into the relevant chapter's `#reading-order`. Mark parallel/background tracks explicitly (`parallel to everything`).
- **🚢 SHIP POINT** callouts at real milestones (something a peer could use), not just at week boundaries.
- **Menu (choose on merit)** callouts where a real framework/vendor decision exists — link to that chapter's comparison table instead of duplicating it.
- **P0/P1/P2** and **∥** (can run in the background) markers throughout.
- Keep [Phases & gates](../docs/roadmap/phases.md) as the detailed, measurable-threshold layer underneath — the spine page narrates it, phases.md proves it.

When the weekly agent (§6.2) touches this page, preserve this shape: tighten prose further, never expand back into a bare table.
