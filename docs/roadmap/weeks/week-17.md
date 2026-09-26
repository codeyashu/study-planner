---
title: Week 17 — DSPy + Raft + free-threaded Python
week: 17
generated: true
---

# Week 17 — DSPy + Raft + free-threaded Python

!!! abstract "At a glance"
    **Phase 5:** Scale & Depth · **Starts:** Mon 18 Jan 2027 · **Planned:** 16h 45m

    **Build:** Capstone: DSPy/GEPA-optimised triage classifier vs hand prompt, measured with the eval harness

## By day

### Monday 18 Jan · 2h 00m

- [ ] **System Design** · 45 min · Raft: leader election, log replication, safety — Raft visualisation + paper sections 5.1-5.4 → [Consensus: Raft, leases, fencing](../../tracks/system-design/consensus-raft.md) · [resource](https://thesecretlivesofdata.com/raft/) <small>`w17-sd-1`</small>
- [ ] **DSA** · 25 min · Coin Change II revisit + Unique Paths → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w17-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: threads vs processes vs asyncio decision table; run a CPU-bound benchmark on 3.14 vs 3.14t → [Concurrency models: threads, processes, free-threaded 3.14t](../../tracks/python/concurrency-models.md) · [resource](https://py-free-threading.github.io/) <small>`w17-py-1`</small>
- [ ] **Communication** · 30 min · Grammar: Participle clauses and concise modification → [Week 17 drills · day 1](../../tracks/communication/drills/week-17.md#day-1) <small>`w17-comm-1`</small>

### Tuesday 19 Jan · 2h 00m

- [ ] **Agentic AI** · 60 min · DSPy 3.x: signatures, modules, metrics, optimizers — work through The Data Quarry 'Learning DSPy' optimizers post → [DSPy & prompt optimization (GEPA)](../../tracks/agentic-ai/dspy.md) · [resource](https://thedataquarry.com/blog/learning-dspy-3-working-with-optimizers/) <small>`w17-ai-1`</small>
- [ ] **DSA** · 30 min · Longest Common Subsequence → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w17-dsa-2`</small>
- [ ] **Communication** · 30 min · Vocabulary: Intensifiers and nuance: considerably, notably, arguably → [Week 17 drills · day 2](../../tracks/communication/drills/week-17.md#day-2) <small>`w17-comm-2`</small>

### Wednesday 20 Jan · 2h 00m

- [ ] **DSA** · 25 min · Best Time to Buy and Sell Stock with Cooldown → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w17-dsa-3`</small>
- [ ] **Architecture** · 45 min · Legacy modernization & strangler fig (Architecture Modernization, Nick Tune) — plan inserting agents into a legacy ops tool → [Legacy modernization & strangler fig](../../tracks/architecture/legacy-modernization.md) · [resource](https://www.manning.com/books/architecture-modernization) <small>`w17-arch-1`</small>
- [ ] **Python** · 20 min · Rep: free-threaded 3.14t — thread-safety of your code, extension compatibility checks → [Concurrency models: threads, processes, free-threaded 3.14t](../../tracks/python/concurrency-models.md) · [resource](https://py-free-threading.github.io/) <small>`w17-py-2`</small>
- [ ] **Communication** · 30 min · Speaking drill: Rhythm and stress in long sentences → [Week 17 drills · day 3](../../tracks/communication/drills/week-17.md#day-3) <small>`w17-comm-3`</small>

### Thursday 21 Jan · 2h 00m

- [ ] **Agentic AI** · 60 min · GEPA reflective optimizer (dspy.GEPA) — run the HF cookbook on a small task and read the traces → [DSPy & prompt optimization (GEPA)](../../tracks/agentic-ai/dspy.md) · [resource](https://huggingface.co/learn/cookbook/dspy_gepa) <small>`w17-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · Virtual threads: fan out 20 LLM calls with Executors.newVirtualThreadPerTaskExecutor; pinning pitfalls → [Virtual threads, structured concurrency & scoped values](../../tracks/java-spring-ai/virtual-threads-structured-concurrency.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w17-java-1`</small>
- [ ] **Communication** · 30 min · Idioms & phrasal verbs: Growth idioms: raise the bar, stretch goal → [Week 17 drills · day 4](../../tracks/communication/drills/week-17.md#day-4) <small>`w17-comm-4`</small>

### Friday 22 Jan · 2h 00m

- [ ] **System Design** · 45 min · Fly.io Gossip Glomers challenges 1-3 (echo, unique IDs, broadcast) in Go or Python Maelstrom → [Consensus: Raft, leases, fencing](../../tracks/system-design/consensus-raft.md) · [resource](https://fly.io/dist-sys/) <small>`w17-sd-2`</small>
- [ ] **DSA** · 25 min · Target Sum → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w17-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: dis module — read bytecode of a hot function; specialising adaptive interpreter → [CPython internals: bytecode, GIL, memory](../../tracks/python/cpython-internals.md) · [resource](https://tenthousandmeters.com/) <small>`w17-py-3`</small>
- [ ] **Communication** · 30 min · Writing: Blog post outline → [Week 17 drills · day 5](../../tracks/communication/drills/week-17.md#day-5) <small>`w17-comm-5`</small>

### Saturday 23 Jan · 3h 30m

- [ ] **Agentic AI** · 120 min · Capstone build: DSPy program for incident classification + GEPA optimisation; compare to hand-tuned prompt on the golden set (accuracy, cost) → [DSPy & prompt optimization (GEPA)](../../tracks/agentic-ai/dspy.md) · [resource](https://dspy.ai/) <small>`w17-ai-3`</small>
- [ ] **DSA** · 30 min · Interleaving String → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w17-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Structured concurrency (preview in 25): StructuredTaskScope for parallel tool calls with cancellation → [Virtual threads, structured concurrency & scoped values](../../tracks/java-spring-ai/virtual-threads-structured-concurrency.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w17-java-2`</small>
- [ ] **Communication** · 30 min · Record & shadow: Rhythm and stress in long sentences → [Week 17 drills · day 6](../../tracks/communication/drills/week-17.md#day-6) <small>`w17-comm-6`</small>

### Sunday 24 Jan · 3h 15m

- [ ] **System Design** · 45 min · Written design: LLM inference/serving platform — batching, KV cache, autoscaling on GPUs, multi-model routing, SLOs → [Design an LLM inference/serving platform](../../tracks/ai-system-design/llm-serving-platform.md) · [resource](https://docs.vllm.ai/) <small>`w17-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 017 for capstone: introduce agents via strangler fig behind existing ticketing UI → [Legacy modernization & strangler fig](../../tracks/architecture/legacy-modernization.md) · [resource](https://adr.github.io) <small>`w17-arch-2`</small>
- [ ] **Staff+** · 30 min · Decision-making under ambiguity: write a one-way vs two-way door analysis for a real pending decision → [Decision-making under ambiguity](../../tracks/staff-skills/decision-making.md) <small>`w17-staff-1`</small>
- [ ] **Communication** · 30 min · Soft skills + weekly review: Mentoring conversations → [Week 17 drills · day 7](../../tracks/communication/drills/week-17.md#day-7) <small>`w17-comm-7`</small>
- [ ] **Review** · 60 min · Explain-it-back: Raft election + log matching; flashcards on DSPy concepts and 2-D DP recurrences → [Consensus: Raft, leases, fencing](../../tracks/system-design/consensus-raft.md) <small>`w17-rev-1`</small>

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
