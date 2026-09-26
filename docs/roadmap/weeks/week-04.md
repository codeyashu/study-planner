---
title: "Week 04 — Orchestrator-workers, AI-assisted dev, stack — interview-1"
week: 4
generated: true
---

# Week 04 — Orchestrator-workers, AI-assisted dev, stack — interview-1

!!! abstract "At a glance"
    **Phase 1:** Foundations · **Starts:** Mon 19 Oct 2026 · **Planned:** 16h 45m

    **Build:** Capstone: orchestrator-workers 'draft postmortem' with evaluator-optimizer loop + 10 golden examples

!!! warning "Interview checkpoint: interview-1"
    Run the full mock loop and score it with the [rubric](../../tracks/staff-skills/interview-prep/rubric.md).

## By day

### Monday 19 Oct · 2h 00m

- [ ] **System Design** · 45 min · Interview framework refresh: practise requirements + estimation opening for 'design Pastebin' in 10 min, recorded → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) · [resource](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) <small>`w04-sd-1`</small>
- [ ] **DSA** · 25 min · Valid Parentheses + Min Stack → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w04-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: asyncio.Semaphore + bounded queue for backpressure on concurrent LLM calls → [asyncio in depth: TaskGroups, cancellation, backpressure](../../tracks/python/asyncio-deep.md) <small>`w04-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Conditionals and modals for hedging and softening → [Week 04 drills · day 1](../../tracks/communication/drills/week-04.md#day-1) <small>`w04-comm-1`</small>

### Tuesday 20 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · AI-assisted development: write AGENTS.md for the capstone repo (commands, conventions, test policy) and add a Claude Code skill for 'add a tool' → [AI-assisted development: coding agents, AGENTS.md, skills](../../tracks/agentic-ai/ai-assisted-development.md) · [resource](https://agents.md/) <small>`w04-ai-1`</small>
- [ ] **DSA** · 30 min · Evaluate Reverse Polish Notation → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w04-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Diplomatic and hedging language → [Week 04 drills · day 2](../../tracks/communication/drills/week-04.md#day-2) <small>`w04-comm-2`</small>

### Wednesday 21 Oct · 2h 00m

- [ ] **DSA** · 25 min · Daily Temperatures (monotonic decreasing stack) → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w04-dsa-3`</small>
- [ ] **Architecture** · 45 min · SOLID & refactoring at scale: refactor the capstone tool loop (SRP, DIP via ports), note code smells found → [SOLID, refactoring & code quality at scale](../../tracks/architecture/solid-refactoring.md) · [resource](https://refactoring.guru) <small>`w04-arch-1`</small>
- [ ] **Python** · 20 min · Rep: async context managers (contextlib.asynccontextmanager) for a pooled client; generator-based pipelines → [Iterators, generators & context managers](../../tracks/python/generators-context-managers.md) <small>`w04-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Cutting filler words (um, like, you know) → [Week 04 drills · day 3](../../tracks/communication/drills/week-04.md#day-3) <small>`w04-comm-3`</small>

### Thursday 22 Oct · 2h 00m

- [ ] **Agentic AI** · 60 min · Context engineering lab: just-in-time retrieval (tool fetches runbook) vs preloaded context — compare token usage and answer quality on 10 cases → [Context engineering](../../tracks/agentic-ai/context-engineering.md) · [resource](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) <small>`w04-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Java 25 features: compact source files, flexible constructor bodies, module imports, scoped values (final) — 4 micro-examples → [Modern Java 21→25: records, sealed types, patterns](../../tracks/java-spring-ai/modern-java.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w04-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Negotiation: meet halfway, off the table → [Week 04 drills · day 4](../../tracks/communication/drills/week-04.md#day-4) <small>`w04-comm-4`</small>

### Friday 23 Oct · 2h 00m

- [ ] **System Design** · 45 min · Scalability patterns recap: stateless services, horizontal scaling, queues for load levelling — map to the capstone → [Scalability fundamentals & latency numbers](../../tracks/system-design/scalability-fundamentals.md) · [resource](https://samwho.dev/blog/) <small>`w04-sd-2`</small>
- [ ] **DSA** · 25 min · Car Fleet (sort + stack) → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w04-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: FastAPI StreamingResponse / SSE for token streaming with client-disconnect handling → [FastAPI for production](../../tracks/python/fastapi-production.md) <small>`w04-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Editing for concision: cut 30 percent → [Week 04 drills · day 5](../../tracks/communication/drills/week-04.md#day-5) <small>`w04-comm-5`</small>

### Saturday 24 Oct · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: orchestrator-workers for 'draft postmortem' (timeline, impact, root cause workers) + evaluator-optimizer critique loop; commit 10 golden examples as seed eval set → [Agent & workflow patterns (Building Effective Agents)](../../tracks/agentic-ai/agent-patterns.md) · [resource](https://www.anthropic.com/engineering/building-effective-agents) <small>`w04-ai-3`</small>
- [ ] **DSA** · 30 min · Timed coding mock (interview-1): Largest Rectangle in Histogram in 30 min, narrate trade-offs → [Stack & monotonic stack](../../tracks/dsa/stack.md) · [resource](https://neetcode.io) <small>`w04-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Port the /triage endpoint to Spring AI (ChatClient + record output) and compare with Python implementation → [Spring AI 2.0 fundamentals: ChatClient, advisors, structured output](../../tracks/java-spring-ai/spring-ai-fundamentals.md) <small>`w04-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Cutting filler words (um, like, you know) → [Week 04 drills · day 6](../../tracks/communication/drills/week-04.md#day-6) <small>`w04-comm-6`</small>

### Sunday 25 Oct · 3h 15m

- [ ] **System Design** · 45 min · Timed 45-min SD mock (interview-1): Pastebin / URL shortener variant with custom aliases + expiry; self-score → [URL shortener](../../tracks/system-design/case-studies/url-shortener.md) <small>`w04-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 004 for capstone: structured-output validation strategy (schema-constrained decoding + bounded retry) → [The architect role & trade-off thinking](../../tracks/architecture/architect-role-tradeoffs.md) · [resource](https://adr.github.io) <small>`w04-arch-2`</small>
- [ ] **Staff+** · 30 min · List 3 candidate 'Staff projects' at work or in the capstone with scope, stakeholders, and why they are Staff-level → [Staff archetypes & operating at Staff+](../../tracks/staff-skills/staff-archetypes.md) · [resource](https://noidea.dog/staff-resources) <small>`w04-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Disagreeing respectfully — checkpoint comm-1: re-record and compare against the baseline rubric → [Week 04 drills · day 7](../../tracks/communication/drills/week-04.md#day-7) <small>`w04-comm-7`</small>
- [ ] **Review** · 60 min · interview-1: full mock — SD + coding + AI SD + behavioral, score with the unified interview rubric and log gaps into next week's plan → [Interview framework & back-of-envelope estimation](../../tracks/system-design/framework-and-estimation.md) <small>`w04-rev-1`</small>

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
