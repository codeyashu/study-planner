---
title: Week 01 — Agent patterns, structured outputs, SD framework
week: 1
generated: true
---

# Week 01 — Agent patterns, structured outputs, SD framework

!!! abstract "At a glance"
    **Phase 1:** Foundations · **Starts:** Mon 28 Sep 2026 · **Planned:** 16h 45m

    **Build:** Capstone repo skeleton: uv + FastAPI + Pydantic structured-output /triage endpoint

## By day

### Monday 28 Sep · 2h 00m

- [ ] **System Design** · 45 min · Hello Interview 'System Design in a Hurry': rebuild your delivery framework (reqs → entities → API → HLD → deep dives) as a one-page checklist → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) · [resource](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) <small>`w01-sd-1`</small>
- [ ] **DSA** · 25 min · Contains Duplicate + Valid Anagram (hash set / Counter) → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w01-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: uv workspace + dependency groups; ruff rule set (I, UP, B, SIM) + ty in pre-commit on capstone → [Modern tooling: uv, ruff, ty, pre-commit](../../tracks/python/modern-tooling.md) · [resource](https://docs.astral.sh/uv/) <small>`w01-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Articles & determiners: a/the/zero → [Week 01 drills · day 1](../../tracks/communication/drills/week-01.md#day-1) <small>`w01-comm-1`</small>

### Tuesday 29 Sep · 2h 00m

- [ ] **Agentic AI** · 60 min · Read Anthropic 'Building effective agents' and map each pattern (chaining, routing, parallelisation, orchestrator-workers, evaluator-optimizer, agents) to an Agentic Ops Copilot use case → [Agent & workflow patterns (Building Effective Agents)](../../tracks/agentic-ai/agent-patterns.md) · [resource](https://www.anthropic.com/engineering/building-effective-agents) <small>`w01-ai-1`</small>
- [ ] **DSA** · 30 min · Two Sum + Group Anagrams (hash map keyed by sorted tuple/count signature) → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w01-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Precision verbs for business (assess, mitigate, prioritise) → [Week 01 drills · day 2](../../tracks/communication/drills/week-01.md#day-2) <small>`w01-comm-2`</small>

### Wednesday 30 Sep · 2h 00m

- [ ] **DSA** · 25 min · Top K Frequent Elements (bucket sort vs heap — state both complexities) → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w01-dsa-3`</small>
- [ ] **Architecture** · 45 min · Fundamentals of Software Architecture 2e ch1-2: laws of architecture, architecture characteristics; list top-5 characteristics for the capstone → [The architect role & trade-off thinking](../../tracks/architecture/architect-role-tradeoffs.md) <small>`w01-arch-1`</small>
- [ ] **Python** · 20 min · Rep: Pydantic v2 model_config (strict, frozen, extra='forbid'), field_validator vs model_validator on IncidentTriage → [Pydantic v2 in depth](../../tracks/python/pydantic-v2.md) <small>`w01-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Pace and deliberate pausing → [Week 01 drills · day 3](../../tracks/communication/drills/week-01.md#day-3) <small>`w01-comm-3`</small>

### Thursday 01 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · LLM fundamentals refresh: tokenisation, temperature/top-p, reasoning vs non-reasoning models — run one prompt on 2 hosted + 1 Ollama model and log tokens, latency, cost → [LLM fundamentals: tokens, transformers, sampling, reasoning models](../../tracks/agentic-ai/llm-fundamentals.md) · [resource](https://github.com/chiphuyen/aie-book) <small>`w01-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Modern Java 21→25 tour: records, sealed interfaces, pattern matching for switch — model Incident/Severity as sealed hierarchy → [Modern Java 21→25: records, sealed types, patterns](../../tracks/java-spring-ai/modern-java.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w01-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Workplace basics: touch base, ballpark, on the same page → [Week 01 drills · day 4](../../tracks/communication/drills/week-01.md#day-4) <small>`w01-comm-4`</small>

### Friday 02 Oct · 2h 00m

- [ ] **System Design** · 45 min · Latency numbers + back-of-envelope drill: estimate QPS, storage and bandwidth for 3 prompts (URL shortener, chat, LLM triage API) in 15 min each → [Scalability fundamentals & latency numbers](../../tracks/system-design/scalability-fundamentals.md) <small>`w01-sd-2`</small>
- [ ] **DSA** · 25 min · Product of Array Except Self (prefix/suffix, O(1) extra space) → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w01-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: FastAPI lifespan + dependency-injected settings (pydantic-settings) and httpx AsyncClient reuse → [FastAPI for production](../../tracks/python/fastapi-production.md) <small>`w01-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Concise emails and subject lines (BLUF) → [Week 01 drills · day 5](../../tracks/communication/drills/week-01.md#day-5) <small>`w01-comm-5`</small>

### Saturday 03 Oct · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: create repo (uv, ruff, ty, pre-commit, pytest), FastAPI app with lifespan + /health + /triage returning a Pydantic-validated IncidentTriage structured output → [Prompting & structured outputs](../../tracks/agentic-ai/prompting-structured-outputs.md) · [resource](https://ai.pydantic.dev/) <small>`w01-ai-3`</small>
- [ ] **DSA** · 30 min · Longest Consecutive Sequence + Encode and Decode Strings → [Arrays & hashing](../../tracks/dsa/arrays-hashing.md) · [resource](https://neetcode.io) <small>`w01-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Generate Spring Boot 4 / Java 25 project for the Java side of capstone (web, actuator, Spring AI starter); run /actuator/health → [Spring Boot 4 & Spring Framework 7](../../tracks/java-spring-ai/spring-boot-4.md) <small>`w01-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Pace and deliberate pausing → [Week 01 drills · day 6](../../tracks/communication/drills/week-01.md#day-6) <small>`w01-comm-6`</small>

### Sunday 04 Oct · 3h 15m

- [ ] **System Design** · 45 min · Written design: URL shortener at 100M URLs/month — ID generation, KV choice, cache, 301 vs 302, analytics pipeline; 2-page doc → [URL shortener](../../tracks/system-design/case-studies/url-shortener.md) <small>`w01-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 001 for capstone: record architecture decisions using MADR template in docs/adr/ → [Architecture Decision Records](../../tracks/architecture/adrs.md) · [resource](https://adr.github.io) <small>`w01-arch-2`</small>
- [ ] **Staff+** · 30 min · Read StaffEng archetypes (Tech Lead, Architect, Solver, Right Hand) and note which work you already do → [Staff archetypes & operating at Staff+](../../tracks/staff-skills/staff-archetypes.md) · [resource](https://staffeng.com/guides/staff-archetypes/) <small>`w01-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Active listening and clarifying questions → [Week 01 drills · day 7](../../tracks/communication/drills/week-01.md#day-7) <small>`w01-comm-7`</small>
- [ ] **Review** · 60 min · Flashcards: 15 cards on agent patterns + latency numbers; explain-it-back the 6 BEA patterns in 5 min → [Agent & workflow patterns (Building Effective Agents)](../../tracks/agentic-ai/agent-patterns.md) <small>`w01-rev-1`</small>

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
