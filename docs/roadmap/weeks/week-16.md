---
title: Week 16 — Architecture docs & AI-era leadership — interview-4
week: 16
generated: true
---

# Week 16 — Architecture docs & AI-era leadership — interview-4

!!! abstract "At a glance"
    **Phase 4:** Production & AI Architecture · **Starts:** Mon 11 Jan 2027 · **Planned:** 16h 45m

    **Build:** Capstone: C4 + arc42 doc set, observability dashboards, SLOs live

!!! warning "Interview checkpoint: interview-4"
    Run the full mock loop and score it with the [rubric](../../interviews/rubric.md).

## By day

### Monday 11 Jan · 2h 00m

- [ ] **System Design** · 45 min · LLM capacity planning II: GPU vs API break-even, rate-limit headroom, multi-provider failover → [LLM capacity, latency & cost planning](../../tracks/ai-system-design/capacity-cost-planning.md) <small>`w16-sd-1`</small>
- [ ] **DSA** · 25 min · Decode Ways → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w16-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: Pydantic computed fields + serializers for API responses → [Pydantic v2 in depth](../../tracks/python/pydantic-v2.md) <small>`w16-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Mixed error review (your personal error log) → [Week 16 drills · day 1](../../tracks/communication/drills/week-16.md#day-1) <small>`w16-comm-1`</small>

### Tuesday 12 Jan · 2h 00m

- [ ] **Agentic AI** · 60 min · LLM observability in production: online evals, sampling, PII in traces, cost dashboards in Langfuse/Phoenix → [LLM observability: Langfuse, Phoenix, OTel GenAI semconv](../../tracks/agentic-ai/llm-observability.md) · [resource](https://arize.com/docs/phoenix) <small>`w16-ai-1`</small>
- [ ] **DSA** · 30 min · Coin Change → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w16-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Review and 100-word check → [Week 16 drills · day 2](../../tracks/communication/drills/week-16.md#day-2) <small>`w16-comm-2`</small>

### Wednesday 13 Jan · 2h 00m

- [ ] **DSA** · 25 min · Maximum Product Subarray + Palindromic Substrings → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w16-dsa-3`</small>
- [ ] **Architecture** · 45 min · Team Topologies: stream-aligned vs platform teams, cognitive load, Conway's law for an AI platform → [Team Topologies & Conway's law](../../tracks/architecture/team-topologies.md) · [resource](https://teamtopologies.com) <small>`w16-arch-1`</small>
- [ ] **Python** · 20 min · Rep: overloads + Literal types for a typed client API → [Advanced typing: generics, Protocols, ParamSpec, TypedDict](../../tracks/python/typing-advanced.md) · [resource](https://typing.python.org) <small>`w16-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: A 5-minute pitch → [Week 16 drills · day 3](../../tracks/communication/drills/week-16.md#day-3) <small>`w16-comm-3`</small>

### Thursday 14 Jan · 2h 00m

- [ ] **Agentic AI** · 60 min · Cost optimisation review: find top-3 token sinks from traces and fix (context trimming, cache hits, cheaper model) → [Cost & latency optimization: caching, batching, streaming](../../tracks/agentic-ai/cost-latency-optimization.md) <small>`w16-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Write the polyglot decision doc: Java vs Python for AI services (talent, ecosystem, ops, latency) → [Java vs Python for AI: polyglot architecture decisions](../../tracks/java-spring-ai/polyglot-ai-architecture.md) <small>`w16-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Idiom review round → [Week 16 drills · day 4](../../tracks/communication/drills/week-16.md#day-4) <small>`w16-comm-4`</small>

### Friday 15 Jan · 2h 00m

- [ ] **System Design** · 45 min · Intelligent document processing pipeline: OCR/layout models, extraction schemas, human review queue → [Design an intelligent document processing pipeline](../../tracks/ai-system-design/document-processing.md) <small>`w16-sd-2`</small>
- [ ] **DSA** · 25 min · Word Break → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w16-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: benchmark with pytest-benchmark; avoid premature optimisation → [Performance & profiling](../../tracks/python/performance-profiling.md) <small>`w16-py-3`</small>
- [ ] **Communication** · 30 min · Writing: The one-pager → [Week 16 drills · day 5](../../tracks/communication/drills/week-16.md#day-5) <small>`w16-comm-5`</small>

### Saturday 16 Jan · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: Langfuse dashboards + alerting on SLO burn and eval-score drift; online LLM-as-judge on 10% of traffic → [LLM observability: Langfuse, Phoenix, OTel GenAI semconv](../../tracks/agentic-ai/llm-observability.md) · [resource](https://langfuse.com/docs) <small>`w16-ai-3`</small>
- [ ] **DSA** · 30 min · Timed coding mock (interview-4): Longest Increasing Subsequence + Partition Equal Subset Sum in 30 min → [Dynamic programming 1-D](../../tracks/dsa/dp-1d.md) · [resource](https://neetcode.io) <small>`w16-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Testcontainers + WireMock contract tests for the Java MCP server → [Observability & testing: Micrometer, OTel, Testcontainers](../../tracks/java-spring-ai/observability-testing.md) <small>`w16-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: A 5-minute pitch → [Week 16 drills · day 6](../../tracks/communication/drills/week-16.md#day-6) <small>`w16-comm-6`</small>

### Sunday 17 Jan · 3h 15m

- [ ] **System Design** · 45 min · Timed 45-min SD mock (interview-4): metrics & monitoring system (ingestion, TSDB, downsampling, alerting) → [Metrics & monitoring system](../../tracks/system-design/case-studies/metrics-monitoring.md) <small>`w16-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 016 for capstone: ownership model — platform team owns gateway/evals, stream teams own agents → [Team Topologies & Conway's law](../../tracks/architecture/team-topologies.md) · [resource](https://adr.github.io) <small>`w16-arch-2`</small>
- [ ] **Staff+** · 30 min · Artifact: AI adoption plan for an engineering org — productivity measurement, risk policy, enablement → [Leading engineering in the AI era: adoption, productivity, risk](../../tracks/staff-skills/ai-era-leadership.md) <small>`w16-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Executive presence — checkpoint comm-4: re-record and compare against the baseline rubric → [Week 16 drills · day 7](../../tracks/communication/drills/week-16.md#day-7) <small>`w16-comm-7`</small>
- [ ] **Review** · 60 min · interview-4: full mock — SD + coding + AI SD + behavioral, score with docs/interviews/rubric.md and log gaps into next week's plan → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) <small>`w16-rev-1`</small>

## By track

| Track | Tasks | Time |
|---|---|---|
| Agentic AI | 3 | 4h 00m |
| System Design | 3 | 2h 15m |
| DSA | 5 | 2h 15m |
| Architecture | 2 | 1h 15m |
| Python | 3 | 1h 00m |
| Java/Spring AI | 2 | 1h 00m |
| Staff+ | 1 | 30m |
| Communication | 7 | 3h 30m |
| Review | 1 | 1h 00m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
