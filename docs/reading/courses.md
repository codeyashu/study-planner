---
title: Courses
tags: [reading, courses]
last_reviewed: 2026-09-25
---

# Courses

Hours are the realistic time *for you* (skipping intro material), not the platform's marketing number. Status checked September 2026.
**Rule:** never run more than one course at a time; a course is a scaffold for a build task, not a goal in itself.

!!! info "Phase → week mapping"
    **P1** wk 1–4 · **P2** wk 5–8 RAG/evals · **P3** wk 9–12 agents/protocols · **P4** wk 13–16 production/architecture · **P5** wk 17–20 scale/depth · **P6** wk 21–24 capstone/interviews

## Agentic AI & LLM engineering

| Course | Provider | Hours | Cost | When | Why / how to use it |
|---|---|---|---|---|---|
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) | Hugging Face | 10–15 | Free | P3 · wk 9–10 | Framework-neutral agent fundamentals (smolagents, LangGraph, LlamaIndex units) with a certification project; do the units, skip the ones on frameworks you won't use. |
| [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) | Hugging Face + Anthropic | 6–8 | Free | P3 · wk 10 | Build MCP servers/clients end to end; pair with the [spec](https://modelcontextprotocol.io/specification/2026-07-28). |
| [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) | DeepLearning.AI | 2 | Free | P3 · wk 10 | Short, clean intro to MCP primitives (tools, resources, prompts) — do this first, then the HF course. |
| [Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) | LangChain Academy | 6 | Free | P3 · wk 9 | State, reducers, checkpointers, human-in-the-loop, memory. Written for LangGraph 1.x; the labs map directly to your capstone orchestration. |
| [Deep Agents project](https://academy.langchain.com/courses/deep-agents-with-langgraph) | LangChain Academy | 3 | Free | P3 · wk 11 | Planning + file-system + sub-agent patterns ("deep agents"); good contrast with plain ReAct loops. |
| [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai/) | DeepLearning.AI (Andrew Ng) | 6–8 | Free / paid cert | P3 · wk 9 | Reflection, tool use, planning, multi-agent — framework-free, strong on *error analysis for agents*. |
| [Evaluating AI Agents](https://learn.deeplearning.ai/courses/evaluating-ai-agents/information) | DeepLearning.AI + Arize | 2 | Free | P3 · wk 12 | Component vs trajectory evals, router/skill evaluation, tracing with Phoenix. |
| [DSPy: Build and Optimize Agentic Apps](https://www.deeplearning.ai/short-courses/dspy-build-optimize-agentic-apps/) | DeepLearning.AI + Databricks | 1.5 | Free | P2 · wk 8 | Signatures, modules, optimizers; follow with the HF [DSPy + GEPA cookbook](https://huggingface.co/learn/cookbook/dspy_gepa). |
| [Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/) | DeepLearning.AI | 10–12 | Free / paid cert | P2 · wk 5–6 | Longer RAG course: hybrid search, chunking, reranking, evaluation, production concerns. Skim the basics; do the eval and production modules. |
| [Claude Code: A Highly Agentic Coding Assistant](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/) | DeepLearning.AI + Anthropic | 2 | Free | P1 · wk 2 | Workflow patterns for AI-assisted development (CLAUDE.md/AGENTS.md, sub-agents, hooks) you'll use all 24 weeks. |
| [Anthropic courses](https://github.com/anthropics/courses) + [Anthropic Academy](https://anthropic.skilljar.com/) | Anthropic | 4–8 | Free | P1 · wk 3 | Prompt engineering, tool use and real-world prompting notebooks; Academy has API/MCP/Agent SDK modules. |
| [5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents) :gem: | Kaggle + Google | 8–10 | Free | P3 · wk 11 | Whitepapers + codelabs on agents, tools/MCP, memory, evaluation, and deploying with Google ADK. Good for the ADK comparison. |
| [Agentic AI MOOC (Fall 2025)](https://agenticai-learning.org/f25) :gem: | UC Berkeley RDI | 12+ (pick lectures) | Free | P5 · wk 17–18 | Lectures by lab/framework leads on agent infra, reasoning, evaluation, safety. Watch 4–5 lectures relevant to your capstone. Predecessor: [LLM Agents MOOC (Fall 2024)](https://llmagents-learning.org/f24). |
| [AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) | Hamel Husain & Shreya Shankar (Maven) | 20–30 | Paid | P2 · wk 7–8 (or next cohort) | The definitive evals course: error analysis, judges aligned with humans, CI evals. Oct 10, 2026 cohort reported as the last of 2026; the free [evals FAQ](https://hamel.dev/blog/posts/evals-faq/) covers the core if you skip it. |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Hugging Face | 10–20 (selected) | Free | P5 · wk 19 | Transformers, fine-tuning, and the newer reasoning/GRPO chapters. Do the fine-tuning chapters before the TRL lab. |
| [Post-training of LLMs](https://www.deeplearning.ai/short-courses/post-training-of-llms/) | DeepLearning.AI | 1.5 | Free | P5 · wk 19 | SFT vs DPO vs online RL with small runnable examples; a compact mental model before fine-tuning. |

## Deep learning foundations (depth, optional)

| Course | Provider | Hours | Cost | When | Why / how to use it |
|---|---|---|---|---|---|
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) :gem: | Andrej Karpathy | 15–20 | Free | P5 · wk 17–20 | Build micrograd → makemore → GPT → tokenizer from scratch. The best way to *feel* attention and tokenization; do at least "Let's build GPT" and "Let's build the GPT Tokenizer". |
| [Practical Deep Learning for Coders](https://course.fast.ai/) | fast.ai | 15–20 (selected) | Free | P5 (optional) | Top-down, practical; take only if you want broader DL intuition beyond LLMs. |
| [CS336: Language Modeling from Scratch](https://stanford-cs336.github.io/) :gem: | Stanford | 30+ (assignments) | Free | Buffer wk 25–26 / after | Heavy: tokenizers, kernels, scaling, data, alignment. For after the 24 weeks unless you go deep on inference. |

## Distributed systems, databases & system design

| Course | Provider | Hours | Cost | When | Why / how to use it |
|---|---|---|---|---|---|
| [Concurrent and Distributed Systems lectures](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) + [notes](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf) :gem: | Martin Kleppmann (Cambridge) | 8 | Free | P1 · wk 2–4 | The clearest short course on clocks, broadcast, replication, consensus, CRDTs. Watch at 1.5x alongside DDIA 2e. |
| [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | MIT | 40+ (labs) | Free | P5 · wk 17–20 | Paper-driven lectures + Go labs (MapReduce, Raft, fault-tolerant KV). Do Lab 3 (Raft) if you want real consensus depth; otherwise read the papers from the schedule. Lectures on [YouTube](https://www.youtube.com/@6.824). |
| [Gossip Glomers](https://fly.io/dist-sys/) :gem: | Fly.io + Kyle Kingsbury (Maelstrom) | 8–12 | Free | P5 · wk 18 | Distributed-systems challenges (broadcast, g-counter, Kafka-style log, txn KV) against a Jepsen-style checker. Can be done in Python. |
| [CMU 15-445/645 Intro to Database Systems](https://15445.courses.cs.cmu.edu/) | CMU (Andy Pavlo) | 20 (selected lectures) | Free | P1 · wk 3 / P5 | Storage, indexes, concurrency control, recovery. Pick lectures on B+trees, MVCC, logging & recovery. |
| [CMU 15-721 Advanced Database Systems](https://15721.courses.cs.cmu.edu/) | CMU | 10 (selected) | Free | P5 (optional) | Columnar execution, query optimisation; useful if you go deep on analytics/vector engines. |
| [System Design in a Hurry](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) | Hello Interview | 4–6 | Free (premium extras) | P1 · wk 1, P6 | Best free interview framework + core concepts; the [ML system design](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) counterpart for AI SD. |

## Cloud, Java & DSA

| Course | Provider | Hours | Cost | When | Why / how to use it |
|---|---|---|---|---|---|
| [Develop AI Agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-on-azure/) | Microsoft Learn | 6–8 | Free | P4 · wk 13–14 | Foundry Agent Service, tools, multi-agent with Microsoft Agent Framework. Modules may still use "Azure AI Foundry" naming (renamed Microsoft Foundry in 2026). |
| [Azure AI Engineer Associate (AI-102)](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/) | Microsoft Learn | 20–30 | Free learning / paid exam | Optional, after wk 16 | Only if a certification helps your org positioning; the learning paths are the useful part. |
| [Spring Academy](https://spring.academy/) | Broadcom / Spring | 5–10 | Free | P4 · wk 14 | Spring Boot fundamentals refresh; for Spring AI 2.0 use the [reference docs](https://docs.spring.io/spring-ai/reference/) and workshop repos in [awesome-spring-ai](https://github.com/spring-ai-community/awesome-spring-ai). |
| [NeetCode](https://neetcode.io) | NeetCode | 60–80 (250 path over 24 wks) | Free / paid | All phases | The DSA track backbone: NeetCode 250 in Python with video explanations. |
