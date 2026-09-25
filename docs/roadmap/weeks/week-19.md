---
title: Week 19 — Fine-tuning trade-offs, GraphRAG
week: 19
generated: true
---

# Week 19 — Fine-tuning trade-offs, GraphRAG

!!! abstract "At a glance"
    **Phase 5:** Scale & Depth · **Starts:** Mon 01 Feb 2027 · **Planned:** 13h 15m

    **Build:** Capstone: LoRA/QLoRA fine-tune experiment (Unsloth/TRL) vs prompt+DSPy baseline; GraphRAG spike

## By day

### Monday 01 Feb · 1h 30m

- [ ] **System Design** · 45 min · Active-active + conflict resolution (LWW, CRDTs) and DR drills → [Multi-region, DR & failover](../../tracks/system-design/multi-region-dr.md) <small>`w19-sd-1`</small>
- [ ] **DSA** · 25 min · Longest Common Subsequence revisit (space-optimised) → [Dynamic programming 2-D](../../tracks/dsa/dp-2d.md) · [resource](https://neetcode.io) <small>`w19-dsa-1`</small>
- [ ] **Python** · 20 min · Rep: subinterpreters / concurrent.interpreters (3.14) experiment → [Concurrency models: threads, processes, free-threaded 3.14t](../../tracks/python/concurrency-models.md) <small>`w19-py-1`</small>

### Tuesday 02 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Fine-tuning: when not to (prompting, RAG, DSPy first); LoRA/QLoRA mechanics; DPO vs GRPO — HF LLM course chapters → [Fine-tuning: LoRA/QLoRA, DPO, GRPO — and when not to](../../tracks/agentic-ai/fine-tuning.md) · [resource](https://huggingface.co/learn/llm-course) <small>`w19-ai-1`</small>
- [ ] **DSA** · 30 min · Maximum Subarray (Kadane) → [Greedy](../../tracks/dsa/greedy.md) · [resource](https://neetcode.io) <small>`w19-dsa-2`</small>

### Wednesday 03 Feb · 1h 30m

- [ ] **DSA** · 25 min · Jump Game + Jump Game II → [Greedy](../../tracks/dsa/greedy.md) · [resource](https://neetcode.io) <small>`w19-dsa-3`</small>
- [ ] **Architecture** · 45 min · AI-native architecture II: agent reliability patterns — deterministic control flow, bounded autonomy, compensation → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) <small>`w19-arch-1`</small>
- [ ] **Python** · 20 min · Rep: refcounting, gc generations, memory layout of objects → [CPython internals: bytecode, GIL, memory](../../tracks/python/cpython-internals.md) · [resource](https://tenthousandmeters.com/) <small>`w19-py-2`</small>

### Thursday 04 Feb · 1h 30m

- [ ] **Agentic AI** · 60 min · Advanced RAG: agentic RAG (not always better), GraphRAG, LazyGraphRAG — decide if capstone corpus benefits → [Advanced RAG: agentic RAG, GraphRAG, LazyGraphRAG](../../tracks/agentic-ai/advanced-rag.md) · [resource](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) <small>`w19-ai-2`</small>
- [ ] **Java/Spring AI** · 30 min · JVM: Leyden AOT cache + compact object headers — measure startup/memory of the MCP server → [JVM performance, GC & Leyden/AOT](../../tracks/java-spring-ai/jvm-performance.md) · [resource](https://openjdk.org/projects/jdk/25/) <small>`w19-java-1`</small>

### Friday 05 Feb · 1h 30m

- [ ] **System Design** · 45 min · Classic ML system design: recommendation & ranking funnel (candidate gen, ranking, re-ranking, features) → [Classic ML system design: recommendation & ranking](../../tracks/ai-system-design/recsys-ml-basics.md) · [resource](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) <small>`w19-sd-2`</small>
- [ ] **DSA** · 25 min · Gas Station → [Greedy](../../tracks/dsa/greedy.md) · [resource](https://neetcode.io) <small>`w19-dsa-4`</small>
- [ ] **Python** · 20 min · Rep: vectorise a hot loop with Polars instead of Python → [Performance & profiling](../../tracks/python/performance-profiling.md) <small>`w19-py-3`</small>

### Saturday 06 Feb · 3h 00m

- [ ] **Agentic AI** · 120 min · Capstone build: QLoRA fine-tune a small model on 500 labelled triage examples with Unsloth/TRL; evaluate vs DSPy baseline; write ablation → [Fine-tuning: LoRA/QLoRA, DPO, GRPO — and when not to](../../tracks/agentic-ai/fine-tuning.md) · [resource](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) <small>`w19-ai-3`</small>
- [ ] **DSA** · 30 min · Hand of Straights + Merge Triplets to Form Target Triplet → [Greedy](../../tracks/dsa/greedy.md) · [resource](https://neetcode.io) <small>`w19-dsa-5`</small>
- [ ] **Java/Spring AI** · 30 min · Virtual thread pinning diagnosis with JFR → [Virtual threads, structured concurrency & scoped values](../../tracks/java-spring-ai/virtual-threads-structured-concurrency.md) <small>`w19-java-2`</small>

### Sunday 07 Feb · 2h 45m

- [ ] **System Design** · 45 min · Written design: coding agent / code-review bot — repo context, sandboxing, tool permissions, evals, cost → [Design a coding agent / code-review bot](../../tracks/ai-system-design/coding-agent.md) · [resource](https://openai.github.io/openai-agents-python/) <small>`w19-sd-3`</small>
- [ ] **Architecture** · 30 min · Write ADR 019 for capstone: prompt + DSPy over fine-tuning for v1 (with evidence from ablation) → [AI-native architecture: LLMs as system components](../../tracks/architecture/ai-native-architecture.md) · [resource](https://adr.github.io) <small>`w19-arch-2`</small>
- [ ] **Staff+** · 30 min · Decision journal: document 2 ambiguous calls from the capstone (options, info missing, reversibility, chosen path) → [Decision-making under ambiguity](../../tracks/staff-skills/decision-making.md) <small>`w19-staff-1`</small>
- [ ] **Review** · 60 min · Explain-it-back: when to fine-tune vs RAG vs DSPy (3-min answer); flashcards on greedy proofs → [Fine-tuning: LoRA/QLoRA, DPO, GRPO — and when not to](../../tracks/agentic-ai/fine-tuning.md) <small>`w19-rev-1`</small>

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
| Review | 1 | 1h 00m |

## End-of-week

- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))
- [ ] Flashcards / explain-it-back done for this week's topics
- [ ] Progress synced (close the daily GitHub issues)
