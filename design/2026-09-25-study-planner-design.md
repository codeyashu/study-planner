# Design spec — Study Planner (2026-09-25)

> Approved plan from the brainstorming/planning session. Source of truth for structure; content evolves per AGENTS.md.


## Context
Rahul: 15-yr senior engineer, strong in system design + Python. Wants 5–6 months (≈ Mon 2026-09-28 → 2027-03-14, + 2 buffer weeks) to become **Staff/Principal + AI architect + hands-on agentic AI engineer**, with interview readiness as checkpoint. 12–15 hrs/week. Stack: Python-first (Pydantic, Pydantic AI, LangGraph, DSPy…), Azure + local/cloud-agnostic, Java/Spring AI alongside. Full DSA track. Public repo `git@github.com:codeyashu/study-planner.git` (empty, public) → MkDocs Material GitHub Pages site used daily. Must stay fresh: daily Claude agent + RSS aggregator + weekly deep refresh + daily GitHub issue + progress tracking.

Research done (3 parallel web agents, Sept 2026): 17 existing roadmaps analysed. Gap found: none combine AI engineering + Staff architecture + DSA + Java + interview checkpoints + spaced repetition. Borrowed patterns: phase gates + "explain-it-back" (Lamarana12200), levelled L1–L4 syllabus + flashcards + MkDocs (JuanMelendres), ADRs as progress log (Toleflaco, Java/Spring AI), AGENTS.md agent protocol (codejunkie99), daily-rep + weekly-build rhythm (jugaldb), soft skills as scored deliverables (ai-infra-curriculum).

## Improved brief (goes into `docs/start-here/brief.md`)
Added what original prompt missed: week-0 baseline assessment; measurable exit criteria per phase; spaced repetition; peer/AI mock interviews with one fixed rubric; portfolio output (ADRs, blog posts, capstone README); cloud/API cost budget (~$30–50/mo, local-first via Ollama); burnout buffers (every 6th week lighter, 2 buffer weeks); timezone for automation (assume **IST, agent runs 06:00 IST** — changeable); "freshness contract" (every page has `last_reviewed`, weekly agent re-verifies versions/links).

## Weekly template (~14.5 h)
| Track | h/wk | Rhythm |
|---|---|---|
| Agentic AI / LLM eng | 4 | weekly build, eval-first |
| System Design (+ AI system design) | 2.5 | 1 design write-up/wk |
| DSA (full) | 2.5 | 5–7 problems/wk, pattern-tagged, NeetCode 250 path |
| Architecture & design | 1.5 | 1 ADR/wk on capstone |
| Python advanced | 1.5 | 15-min daily reps |
| Java / Spring AI | 1 | port each AI build to Spring AI 2.0 |
| Staff skills | 0.5–1 | artifact every 2 wks |
| Review (Sun) | 1 | flashcards, explain-it-back, retro |
Weekdays 1.5 h, Sat 3 h (build block), Sun 2.5 h (build + review).

## Phases (gate at end of each; interview checkpoint wk 4/8/12/16/20/24, same rubric)
0. **Wk 0 (this weekend)** — baseline: 1 SD mock, 3 DSA mediums, AI self-assessment quiz → calibrates skip list.
1. **Wk 1–4 Foundations refresh** — uv/ruff/ty, Pydantic v2, asyncio TaskGroups, typing, FastAPI; LLM APIs, structured outputs, Building Effective Agents + context engineering; Spring Boot 4 + Spring AI basics; SD framework + fundamentals (Hello Interview, samwho); DSA arrays/hashing/two-pointers/sliding window; Staff archetype doc.
2. **Wk 5–8 RAG + Evals** — hybrid search pgvector + BM25 + reranker, chunking; error analysis → evals (Hamel), promptfoo/DeepEval/Ragas in CI, Langfuse + OTel GenAI semconv; DDD, hexagonal, repo/UoW (Cosmic Python); SD storage/caching/search; DSA stack/binary search/linked list/trees.
3. **Wk 9–12 Agents + Protocols** — LangGraph 1.x (durable exec, HITL), Pydantic AI, MCP server+client (2026-07-28 spec, OAuth), A2A, AG-UI, memory (Mem0/Letta), Claude Agent SDK / OpenAI Agents SDK; Spring AI `@McpTool` agent; event-driven, sagas, outbox; SD queues/streams; DSA tries/heaps/backtracking/graphs.
4. **Wk 13–16 Production & AI architecture** — guardrails, OWASP LLM + Agentic Top 10, lethal trifecta, red-teaming; cost/latency (caching, batching, routing via LiteLLM), AI gateway; Microsoft Foundry Agent Service + MS Agent Framework, Bedrock AgentCore awareness; SD: design LLM platform, multi-tenant RAG, rate limiter; C4, arc42, Team Topologies; strategy doc + tech-debt proposal; DSA advanced graphs/1-D DP.
5. **Wk 17–20 Scale & depth** — DSPy/GEPA, inference (vLLM vs SGLang, quantisation), fine-tuning trade-offs (LoRA/QLoRA, DPO/GRPO via Unsloth/TRL), GraphRAG/LazyGraphRAG; distributed systems depth (DDIA 2e, Kleppmann lectures, Raft, Gossip Glomers); free-threaded Python 3.14t, perf; Java 25 virtual threads / structured concurrency; DSA 2-D DP/intervals/greedy; mentoring/talk artifact.
6. **Wk 21–24 Capstone + interview loop** — finish capstone, full ADR set, 2 blog posts, full mock loops (coding, SD, AI SD, behavioral/Staff).
7. **Wk 25–26 Buffer** — catch-up or deeper specialisation.

**Capstone** (built across phases, specs in repo, code in separate repo user creates later): *Agentic Ops Copilot* — LangGraph orchestrator + Pydantic AI sub-agents, MCP tool servers (one in Python, one in Spring AI), hybrid RAG on pgvector, eval suite in CI, Langfuse tracing, guardrails, LiteLLM routing; runs locally via docker-compose + Ollama, deploys to Azure Container Apps + Foundry. Per-phase mini-projects each with spec, acceptance criteria, rubric, write-up requirement (ablation / failure analysis).

## Repo structure (new local clone: `~/Documents/study-planner`)
```
study-planner/
  mkdocs.yml                 # Material: tabs, search, tags, blog, admonitions, tasklist, mermaid, dark mode
  pyproject.toml / uv.lock   # mkdocs-material, mkdocs-quiz, feedparser, pyyaml, git-revision-date
  AGENTS.md                  # agent protocol: daily / weekly / on-demand procedures, content rules, templates
  CLAUDE.md                  # @AGENTS.md
  data/
    plan.yml                 # machine-readable: week→day→task ids (track, minutes, resource refs)
    progress.yml             # completed task ids + dates (source of truth for streak/heatmap)
    feeds.yml                # RSS sources (≈30, verified by research agent) + tags
    resources.yml            # every resource: id, url, track, priority, complexity, free/paid, gem flag, last_checked
  docs/
    index.md                 # dashboard: today's tasks, phase, streak heatmap, week progress per track
    today.md                 # generated daily
    start-here/              # brief, how-to-use, weekly template, rules, freshness contract, baseline test
    roadmap/                 # overview, phase-0..7.md, weeks/week-00..26.md (day-by-day tasks)
    tracks/<track>/          # index + topic pages (template below) — 8 tracks:
                             #   system-design, ai-system-design, architecture, python, agentic-ai,
                             #   java-spring-ai, dsa (pattern pages + NeetCode 250 map), staff-skills
    questions/<track>.md     # bank L1–L4 + use-case scenarios, collapsible answers; quizzes via mkdocs-quiz
    projects/                # capstone spec, phase projects, rubrics
    interviews/              # checkpoints wk 4..24, unified rubric, mock scripts, behavioral STAR bank
    reading/                 # newsletters (w/ RSS), podcasts, YouTube, books, papers, eng blogs, today's-feed
    trends/radar.md          # tech radar (adopt/trial/assess/hold), refreshed weekly
    digest/posts/            # blog plugin: daily digest posts YYYY-MM-DD.md
    log/adrs/, log/retros/   # ADR + weekly retro templates
  scripts/
    gen_today.py             # plan.yml + date + progress → docs/today.md
    build_feeds.py           # feeds.yml → docs/reading/feed.md (last 48h, deduped, tagged)
    sync_progress.py         # closed "Day N" issue checkboxes → progress.yml
    stats.py                 # progress.yml → docs/assets/stats.json (heatmap/streak)
    check_links.py           # resources.yml link check → report
  .github/workflows/
    deploy.yml               # push to main → mkdocs build --strict → Pages
    daily.yml                # cron 00:30 UTC (06:00 IST): gen_today + build_feeds + open "Day N" issue, commit
    progress.yml             # on issue closed/edited → sync_progress + stats, commit
    weekly-links.yml         # Sun: check_links → open issue if broken
  docs/superpowers/specs/2026-09-25-study-planner-design.md   # this design, per brainstorming flow
```

**Topic page template** (every topic): Why it matters · Priority (P0/P1/P2) · Complexity (1–5) · Est. hours · Prereqs · Core concepts explained (own words, diagrams via Mermaid) · Resources table (clarity-first, "gem" tag for less-famous clear explainers, free/paid, level) · Hands-on lab · Questions L1 recall → L2 apply → L3 design/trade-off → L4 Staff-ambiguity, each with collapsible answer · Real-world use cases/scenarios · Pitfalls · Done-checklist · `last_reviewed` front-matter.

Content targets v1: ~90–110 topic pages, ~500 questions with answers, ~300 curated resources, 26 week pages, 30 feeds.

## Freshness / daily automation
1. **daily.yml (GitHub Action, free, no LLM)** — today page, RSS feed page, opens "Day N" issue with checklist (GitHub notifications = reminder). Close/tick issue → progress.yml → dashboard streak.
2. **Claude cloud routine (`/schedule`), daily 06:15 IST** — follows AGENTS.md `daily` procedure: web-research last-24h notable releases/articles relevant to tracks, write `digest/posts/<date>.md` (3–5 must-reads w/ why + which track), append comment to Day-N issue, commit. Needs the claude.ai GitHub integration authorised for the repo (user does once). Fallback: `anthropics/claude-code-action` workflow with `ANTHROPIC_API_KEY` secret (user adds).
3. **Weekly routine (Sun 07:00 IST)** — AGENTS.md `weekly` procedure: re-verify versions/links, update trends radar, add 20+ new questions, adjust next week from progress (slip → reschedule), write retro prompt.
4. Also a local `/loop`-free option: user can say "update roadmap" in any session; AGENTS.md defines it.

## Execution steps (after approval)
1. Clone repo to `~/Documents/study-planner`; scaffold uv project, mkdocs.yml, AGENTS.md/CLAUDE.md, data schemas, templates; write design spec.
2. Write scripts + workflows; unit-test scripts with pytest (gen_today, sync_progress, build_feeds on fixture data).
3. Content generation in parallel via subagents (one per track, ~8), each given: research notes above, topic template, question-level rubric, resources.yml schema. Then me: roadmap/phases/week pages (plan.yml as source), reading lists, interviews, projects, dashboard.
4. Review pass: consistency, no placeholders, link check, `mkdocs build --strict`.
5. Local preview (`.claude/launch.json` → `uv run mkdocs serve`) + screenshots light/dark/mobile.
6. **Confirm with user**, then push to `main`, enable Pages (Actions source) via `gh api`, verify live URL.
7. Set up daily + weekly Claude routines via `/schedule` (confirm first); document manual fallback.
8. Save user-profile memory (goals, timezone, stack) for future sessions.

## Verification
- `uv run pytest` (scripts) green; `uv run mkdocs build --strict` no warnings.
- `check_links.py` → 0 broken in resources.yml (or flagged).
- Preview: dashboard renders today's tasks, heatmap reads stats.json, quizzes work, search works, dark mode OK, 375px width OK.
- Actions: trigger `daily.yml` via `workflow_dispatch` → issue "Day 1" created, today.md committed, site redeployed; close issue → progress.yml updated → streak shows 1.
- Routine: run once manually → digest post committed and visible on site.

## Implementation notes

- Quizzes: implemented as nested collapsible admonitions (`??? question` / `??? success`) instead of the mkdocs-quiz plugin — zero plugin risk, works with search, maps 1:1 to Anki cards.
- Spec lives in `design/` (outside `docs/`) so it is not published as a site page.
- Weekly day-slot mapping is fixed in `scripts/common.py` (SLOTS).
