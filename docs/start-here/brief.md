---
title: The brief
last_reviewed: 2026-09-25
---

# The brief

## Original ask (paraphrased)

> Senior engineer, 15 years of experience, with about 5–6 months. I want to upgrade in software engineering, architecture, design and AI, following the latest trends. The roadmap needs resources, links, priority and complexity. Research how others build roadmaps. Include questions by complexity and use case for every topic. Structure it so I can work through it. Include newsletters and articles, and publish it as a GitHub Page I can use daily. Keep it evolving so it doesn't go stale, and update me daily. I'm good at system design and Python but want to improve everywhere. Focus on system design, Python and AI so I can implement and be productive. Don't compromise on length, but keep it structured.

## Improved brief

**Outcome by 14 Mar 2027 (end of week 24):**

1. **Architect.** Can lead the architecture of a multi-team system: C4 and ADRs, DDD boundaries, event-driven integration, migration strategy. Can defend trade-offs to executives and staff peers.
2. **AI engineer.** Has shipped (in the capstone) a production-grade agentic system with:
    - a LangGraph orchestrator and Pydantic AI sub-agents
    - MCP tool servers in both Python and Spring AI
    - hybrid RAG with a reranker
    - an eval suite gating CI
    - Langfuse/OTel tracing, guardrails, and model routing with budgets
3. **Interview-ready.** Scores ≥ 3/4 ("Staff bar") on the [unified rubric](../interviews/rubric.md) in coding, system design, AI system design and behavioral rounds at checkpoint 6.
4. **Staying current.** Has a sustainable habit of about 20 min/day of reading, backed by a curated digest rather than doomscrolling.

**Constraints:**

- **Time:** 12–15 h/week. Every 6th week is lighter (weeks 6, 12, 18), plus 2 buffer weeks (25–26).
- **Budget:** about $30–50/month for APIs and cloud. Default to local models (Ollama) and free tiers; use paid APIs for evals and final runs.
- **Stack:**
    - Python 3.14, uv, Pydantic v2, FastAPI, LangGraph, Pydantic AI, DSPy
    - Azure (Microsoft Foundry, Container Apps, Postgres) plus Docker/Ollama locally
    - Java 25 with Spring Boot 4 and Spring AI 2.0
- **Timezone:** IST. Automation runs 06:00–06:15 IST.

## What the original ask was missing (now added)

| Gap | Added |
|---|---|
| No baseline | [Week 0 baseline](baseline.md) calibrates a *skip list*, so you don't re-learn what you already know |
| No definition of done | Every phase has **exit gates**. Every topic has a *"You're done when…"* line and a checklist |
| Reading ≠ retention | **Spaced repetition** (DSA re-solves on days 1/3/7/21), graded L1–L4 questions with hidden answers, and Sunday explain-it-back |
| Interview readiness unmeasured | **6 checkpoints** on one rubric, with a score log to track growth |
| Nothing to show at the end | **Portfolio outputs:** capstone repo, ADRs, blog posts, Staff artifacts |
| Burnout risk | Light weeks, buffer weeks, a catch-up queue on *Today* (unfinished tasks from the last 7 days), and a "never drop P0, push P2" rebalancing rule |
| Cost blind spot | Explicit budget, local-first defaults, and cost math in AI topics |
| "Keep it fresh" was vague | [Freshness contract](freshness.md): `last_reviewed` on every page, weekly version and link checks, radar changelog |
| Java unaddressed | Parallel Java/Spring AI track that ports each capstone piece (a polyglot architecture skill) |
| Staff skills implicit | Staff+ track with 8 concrete artifacts (strategy doc, tech-debt proposal, mentoring plan…) |

## Success metrics (reviewed at every checkpoint)

| Metric | Target by wk 12 | Target by wk 24 |
|---|---|---|
| Task completion | ≥ 80% of due tasks | ≥ 85% |
| DSA problems solved (with re-solves) | 110 | 250 |
| Capstone milestones | M1–M5 | M1–M8 |
| ADRs written | 8 | 15+ |
| Mock score (avg of rounds) | ≥ 2.5 / 4 | ≥ 3.0 / 4 |
| Longest streak | 21 days | 45 days |
