---
title: Dashboard
hide: [navigation, toc]
---

# Senior → Staff + AI Architect · 24-week roadmap

<div class="sp-kpis" data-stats markdown>
<div class="sp-kpi"><span class="sp-kpi__value" data-kpi="streak">–</span><span class="sp-kpi__label">day streak</span></div>
<div class="sp-kpi"><span class="sp-kpi__value" data-kpi="done">–</span><span class="sp-kpi__label">tasks done</span></div>
<div class="sp-kpi"><span class="sp-kpi__value" data-kpi="behind">–</span><span class="sp-kpi__label">behind plan</span></div>
<div class="sp-kpi"><span class="sp-kpi__value" data-kpi="week">–</span><span class="sp-kpi__label">current week</span></div>
</div>

## Today

--8<-- "includes/today-snippet.md"

[Open Today :material-arrow-right:](today.md){ .md-button .md-button--primary } [This week's plan](roadmap/index.md){ .md-button } [Latest digest](digest/index.md){ .md-button }

## Consistency

<div class="sp-heatmap" data-heatmap></div>

<div class="sp-tracks" data-tracks></div>

## The map

```mermaid
gantt
    title 26 weeks · Sat 26 Sep 2026 → Sun 28 Mar 2027
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Phases
    0 Baseline                     :p0, 2026-09-26, 2d
    1 Foundations refresh          :p1, 2026-09-28, 4w
    2 RAG + Evals                  :p2, after p1, 4w
    3 Agents + Protocols           :p3, after p2, 4w
    4 Production & AI architecture :p4, after p3, 4w
    5 Scale & depth                :p5, after p4, 4w
    6 Capstone + interview loop    :p6, after p5, 4w
    7 Buffer                       :p7, after p6, 2w
    section Checkpoints
    Mock 1 :milestone, 2026-10-25, 0d
    Mock 2 :milestone, 2026-11-22, 0d
    Mock 3 :milestone, 2026-12-20, 0d
    Mock 4 :milestone, 2027-01-17, 0d
    Mock 5 :milestone, 2027-02-14, 0d
    Mock 6 :milestone, 2027-03-14, 0d
```

## Where to go

<div class="grid cards" markdown>

-   :material-rocket-launch: **Start here**

    ---

    The brief, how the system works, weekly rhythm, rules, the week-0 baseline.

    [:octicons-arrow-right-24: Start here](start-here/index.md)

-   :material-map-marker-path: **Roadmap**

    ---

    Phases with exit gates, and 27 day-by-day week pages generated from the curriculum.

    [:octicons-arrow-right-24: Roadmap](roadmap/index.md)

-   :material-robot: **Agentic AI & LLM engineering**

    ---

    29 topics from context engineering to MCP, LangGraph, evals, guardrails, serving and fine-tuning.

    [:octicons-arrow-right-24: Agentic AI](tracks/agentic-ai/index.md)

-   :material-sitemap: **System design & AI system design**

    ---

    Distributed-systems depth, 9 case studies, 12 AI system design walkthroughs.

    [:octicons-arrow-right-24: System design](tracks/system-design/index.md) · [AI SD](tracks/ai-system-design/index.md)

-   :material-domain: **Architecture · Python · Java/Spring AI**

    ---

    DDD, hexagonal, sagas, modernization; expert Python; Java 25 + Spring AI 2.0.

    [:octicons-arrow-right-24: Architecture](tracks/architecture/index.md) · [Python](tracks/python/index.md) · [Java](tracks/java-spring-ai/index.md)

-   :material-graph: **DSA · Staff+ skills**

    ---

    NeetCode-250 pattern path with spaced repetition; strategy, influence, STAR bank.

    [:octicons-arrow-right-24: DSA](tracks/dsa/index.md) · [Staff+](tracks/staff-skills/index.md)

-   :material-hammer-wrench: **Projects**

    ---

    The *Agentic Ops Copilot* capstone plus six phase projects with rubrics.

    [:octicons-arrow-right-24: Projects](projects/index.md)

-   :material-account-voice: **Interviews**

    ---

    Six checkpoints on one rubric, mock prompt banks, AI mock-interviewer prompts.

    [:octicons-arrow-right-24: Interviews](interviews/index.md)

-   :material-newspaper-variant: **Reading & trends**

    ---

    Daily auto-feed, curated digest, newsletters, papers, and a living tech radar.

    [:octicons-arrow-right-24: Reading](reading/index.md) · [Radar](trends/radar.md)

</div>
