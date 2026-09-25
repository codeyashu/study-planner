---
title: Week 0 baseline
last_reviewed: 2026-09-25
---

# Week 0 baseline (Sat 26 – Sun 27 Sep 2026)

**Purpose:** measure where you really are before you start, so the first weeks skip what you already know and target what you don't. Score everything with the [unified rubric](../interviews/rubric.md), and write the results in `docs/log/baseline.md`.

## 1. System design mock (60 min)

Prompt: **"Design a URL shortener that handles 100 M new URLs/month with analytics"**. Use a timer: 5 min to clarify, 10 min to estimate, 20 min for high-level design, 20 min for deep dives, 5 min to wrap up. Record yourself if you can.
Then compare against the [case study](../tracks/system-design/case-studies/url-shortener.md).

## 2. Coding (3 × 30 min, Python, no IDE help)

- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [Course Schedule](https://leetcode.com/problems/course-schedule/)

Note the time to a working solution, bugs found, and whether you explained the complexity unprompted.

## 3. AI engineering self-assessment (30 min)

Rate yourself 0–3 on each item (0 = never touched, 1 = read about it, 2 = built a toy, 3 = shipped to production):

| Area | 0–3 |
|---|---|
| Calling LLM APIs with structured outputs (JSON schema / Pydantic) | |
| Prompt caching, streaming, token/cost accounting | |
| Embeddings, chunking, vector search, hybrid search, reranking | |
| Building an eval set, error analysis, LLM-as-judge alignment | |
| LangGraph (state, checkpoints, HITL) | |
| Pydantic AI / OpenAI Agents SDK / Claude Agent SDK | |
| MCP server/client, OAuth for tools | |
| Tracing LLM apps (Langfuse / Phoenix / OTel GenAI) | |
| Prompt injection defenses, OWASP LLM/Agentic Top 10 | |
| Serving open models (Ollama, vLLM), quantization | |
| Fine-tuning (LoRA/QLoRA, DPO) | |
| Spring AI | |

## 4. Environment setup (60–90 min)

- [ ] `uv` installed; `uv python install 3.14 3.14t`
- [ ] Docker Desktop / OrbStack running; `docker compose` works
- [ ] Ollama installed; pull a small model (e.g. a 3–8 B instruct model) and an embedding model
- [ ] API keys in a password manager and a local `.env` (never committed): one frontier-model provider + Azure subscription access
- [ ] JDK 25 (e.g. via SDKMAN) + Maven/Gradle
- [ ] Create the capstone repo `agentic-ops-copilot` (empty, with README)
- [ ] Clone this repo; `uv sync && uv run mkdocs serve` works

## 5. Write your skip list (30 min)

In `docs/log/baseline.md`, list:

- **Skip / skim:** topics you'd rate 3 with evidence (for each one, answer its L3 questions to confirm)
- **Focus:** everything rated 0–1 in AI, plus any DSA pattern that took more than 30 min
- **Goals in your own words**, and what "success" looks like on 14 Mar 2027
