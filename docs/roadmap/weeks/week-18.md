---
title: "Week 18 — Inference serving (light)"
week: 18
generated: true
---

# Week 18 — Inference serving (light)

!!! abstract "At a glance"
    **Phase 5:** Scale & Depth · **Starts:** Mon 25 Jan 2027 · **Planned:** 11h 00m · **Light week**

    **Build:** Capstone: self-hosted vLLM (or Ollama) serving experiment with quantised model behind LiteLLM

## By day

### Monday 25 Jan · 1h 20m

- [ ] **System Design** · 30 min · Leases, fencing tokens, clock pitfalls — Kleppmann lectures on distributed locks → [Consensus: Raft, leases, fencing](../../tracks/system-design/consensus-raft.md) · [resource](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) <small>`w18-sd-1`</small>
- [ ] **DSA** · 15 min · Edit Distance → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w18-dsa-1`</small>
- [ ] **Python** · 15 min · Rep: GIL internals + what changes without it → [CPython internals: bytecode, GIL, memory](../../tracks/python/cpython-internals.md) · [resource](https://blog.codingconfessions.com/) <small>`w18-py-1`</small>
- [ ] **Communication** · 20 min · Grammar: Review: hardest patterns from your error log → [Week 18 drills · day 1](../../tracks/communication/drills/week-18.md#day-1) <small>`w18-comm-1`</small>

### Tuesday 26 Jan · 1h 20m

- [ ] **Agentic AI** · 40 min · Inference serving: continuous batching, PagedAttention, prefix caching — vLLM vs SGLang vs Ollama → [Inference serving: vLLM, SGLang, Ollama, quantization](../../tracks/agentic-ai/inference-serving.md) · [resource](https://docs.vllm.ai/) <small>`w18-ai-1`</small>
- [ ] **DSA** · 20 min · Longest Increasing Path in a Matrix → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w18-dsa-2`</small>
- [ ] **Communication** · 20 min · Vocabulary: Review, spaced repetition round → [Week 18 drills · day 2](../../tracks/communication/drills/week-18.md#day-2) <small>`w18-comm-2`</small>

### Wednesday 27 Jan · 1h 20m

- [ ] **DSA** · 15 min · Distinct Subsequences → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w18-dsa-3`</small>
- [ ] **Architecture** · 30 min · Data architecture: CDC, lakehouse, data mesh — keeping a vector index in sync with source systems → [Data architecture: lakehouse, data mesh, CDC](../../tracks/architecture/data-architecture.md) <small>`w18-arch-1`</small>
- [ ] **Python** · 15 min · Rep: concurrent.futures vs asyncio.to_thread for blocking SDKs → [Concurrency models: threads, processes, free-threaded 3.14t](../../tracks/python/concurrency-models.md) <small>`w18-py-2`</small>
- [ ] **Communication** · 20 min · Speaking drill: Shadowing practice 3 → [Week 18 drills · day 3](../../tracks/communication/drills/week-18.md#day-3) <small>`w18-comm-3`</small>

### Thursday 28 Jan · 1h 20m

- [ ] **Agentic AI** · 40 min · Quantisation (GGUF, AWQ, GPTQ, FP8) — quality/latency trade-off measured with the eval set → [Inference serving: vLLM, SGLang, Ollama, quantization](../../tracks/agentic-ai/inference-serving.md) · [resource](https://docs.sglang.ai/) <small>`w18-ai-2`</small>
- [ ] **Java/Spring AI** · 20 min · Scoped values (final in 25) vs ThreadLocal for request context in virtual threads → [Virtual threads, structured concurrency & scoped values](../../tracks/java-spring-ai/virtual-threads-structured-concurrency.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w18-java-1`</small>
- [ ] **Communication** · 20 min · Idioms & phrasal verbs: Idiom review round → [Week 18 drills · day 4](../../tracks/communication/drills/week-18.md#day-4) <small>`w18-comm-4`</small>

### Friday 29 Jan · 1h 15m

- [ ] **System Design** · 30 min · Multi-region: active-passive vs active-active, RPO/RTO, failover testing → [Multi-region, DR & failover](../../tracks/system-design/multi-region-dr.md) <small>`w18-sd-2`</small>
- [ ] **DSA** · 15 min · Burst Balloons → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w18-dsa-4`</small>
- [ ] **Python** · 10 min · Rep: profile async code with py-spy --idle → [Performance & profiling](../../tracks/python/performance-profiling.md) <small>`w18-py-3`</small>
- [ ] **Communication** · 20 min · Writing: Editing a colleague's draft → [Week 18 drills · day 5](../../tracks/communication/drills/week-18.md#day-5) <small>`w18-comm-5`</small>

### Saturday 30 Jan · 2h 15m

- [ ] **Agentic AI** · 75 min · Capstone build: serve a quantised 7-8B model via vLLM/Ollama behind LiteLLM; route the 'classify' node to it and compare quality/cost → [Inference serving: vLLM, SGLang, Ollama, quantization](../../tracks/agentic-ai/inference-serving.md) · [resource](https://docs.vllm.ai/) <small>`w18-ai-3`</small>
- [ ] **DSA** · 20 min · Regular Expression Matching → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w18-dsa-5`</small>
- [ ] **Java/Spring AI** · 20 min · JVM performance intro: GC choices (G1, ZGC), JFR recording of the MCP server → [JVM performance, GC & Leyden/AOT](../../tracks/java-spring-ai/jvm-performance.md) <small>`w18-java-2`</small>
- [ ] **Communication** · 20 min · Record & shadow: Shadowing practice 3 → [Week 18 drills · day 6](../../tracks/communication/drills/week-18.md#day-6) <small>`w18-comm-6`</small>

### Sunday 31 Jan · 2h 10m

- [ ] **System Design** · 30 min · Written design: distributed key-value store — partitioning, replication, quorum, hinted handoff, anti-entropy (Dynamo) → [Distributed key-value store](../../tracks/system-design/case-studies/distributed-kv-store.md) · [resource](https://martinfowler.com/articles/patterns-of-distributed-systems/) <small>`w18-sd-3`</small>
- [ ] **Architecture** · 20 min · Write ADR 018 for capstone: CDC (Debezium-style) from ticket DB into the RAG index → [Data architecture: lakehouse, data mesh, CDC](../../tracks/architecture/data-architecture.md) · [resource](https://adr.github.io) <small>`w18-arch-2`</small>
- [ ] **Staff+** · 20 min · Artifact: mentoring plan — 1 mentee, goals, cadence, sponsorship opportunities you'll create → [Mentoring, sponsorship & growing engineers](../../tracks/staff-skills/mentoring-sponsorship.md) <small>`w18-staff-1`</small>
- [ ] **Communication** · 20 min · Soft skills + weekly review: Giving upward feedback → [Week 18 drills · day 7](../../tracks/communication/drills/week-18.md#day-7) <small>`w18-comm-7`</small>
- [ ] **Review** · 40 min · Light-week retro + flashcards: inference serving vocabulary, quorum math → [Inference serving: vLLM, SGLang, Ollama, quantization](../../tracks/agentic-ai/inference-serving.md) <small>`w18-rev-1`</small>

## By track

| Track | Tasks | Time |
|---|---|---|
| Agentic AI | 3 | 2h 35m |
| System Design | 3 | 1h 30m |
| DSA | 5 | 1h 25m |
| Architecture | 2 | 50m |
| Python | 3 | 40m |
| Java/Spring AI | 2 | 40m |
| Staff+ | 1 | 20m |
| Communication | 7 | 2h 20m |
| Review | 1 | 40m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
