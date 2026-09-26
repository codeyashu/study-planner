---
title: Roadmap
last_reviewed: 2026-09-26
---

# The roadmap

Learn by doing. Vendor-neutral where it matters — dual-run **local Ollama** (free, private) against a **frontier API** (Claude/GPT/Gemini) so you feel the trade-off, not just read about it. 26 weeks, ~17–18 h/week. Verified 26 Sep 2026 — if a link looks stale, trust the tool's own docs over this page.

**Legend:** `P0` blocks everything after it · `P1` core, do it early · `P2` depth, do it when a project needs it · **∥** can run in the background (a talk, a chapter) while you build something else · **🚢** a real ship point — working software a peer could use, not a checkbox.

## Spine

Five resources that pay off across the whole plan, not one topic. Read them once early, then dip back in.

| Resource | Use it for |
|---|---|
| [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | The patterns ladder every agentic-ai topic assumes you know |
| [Chip Huyen — AI Engineering](https://github.com/chiphuyen/aie-book) | The systems view: evals, RAG, agents, deployment, in one head |
| [Kleppmann & Riccomini — DDIA, 2nd ed.](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) | The distributed-systems ground truth under every design decision |
| [Percival & Gregory — Architecture Patterns with Python (Cosmic Python, free)](https://www.cosmicpython.com/) | The Python architecture vocabulary (ports, adapters, UoW) used across the capstone |
| [Will Larson — StaffEng](https://staffeng.com/guides/staff-archetypes/) | What "Staff" actually means before you try to act like one |

## Phase 0 — Setup (this weekend, ~3–4 h)

```bash
# Toolchain
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.14 3.14t
brew install --cask docker ollama          # or your platform's equivalent

# Local models — pick one small + one embedding model
ollama pull qwen3:8b                        # or llama3.1:8b
ollama pull nomic-embed-text

# Repo
git clone <your-capstone-repo> agentic-ops-copilot && cd agentic-ops-copilot
uv init && uv add pydantic pydantic-ai fastapi langgraph
docker compose up -d postgres               # capstone data layer, from week 1
```

Then the [week-0 baseline](../start-here/baseline.md): a system-design mock, 3 DSA mediums, an AI self-assessment, a recorded 2-min talk. It produces the skip list that makes week 1 start on building, not re-learning.

## The tracks

Nine chapters, run mostly in parallel, not in series. **A–D are sequential** (each needs the last); **E–I run every week alongside them** at the hours shown. Full day-by-day schedule: [weekly rhythm](weekly-template.md) → [all 26 weeks](#all-weeks) → [phase gates](phases.md).

**A — Foundations** *(wk 1–4, P0)*
Do: modern Python/Java tooling, LLM fundamentals, prompting, tool calling, agent patterns. ∥ read the Spine while you set up.
Deliverable: a typed tool-calling agent with structured output, in a repo with `AGENTS.md`.
→ [Agentic AI ch. 1–5](../tracks/agentic-ai/index.md#reading-order) · [Python](../tracks/python/index.md) · [Java & Spring AI](../tracks/java-spring-ai/index.md)

**B — RAG as a spectrum** *(wk 5–8, P0)*
Do: chunking → hybrid search + rerank → pgvector/Qdrant → agentic/GraphRAG only once plain RAG is measured and beaten.
Deliverable: hybrid RAG over your own corpus, with an ablation report (chunking × hybrid weights × reranker) and numbers, not vibes.
→ [Agentic AI ch. 6–9](../tracks/agentic-ai/index.md#reading-order) · [P2: hybrid RAG with ablation](../tracks/agentic-ai/projects/p2-hybrid-rag-with-ablation.md)

**C — Evals & observability** *(wk 5–8, P0, parallel with B)*
Do: error analysis on real traces *before* you write a single eval. Only then promptfoo/DeepEval/Ragas, then Langfuse + OTel GenAI tracing.
Deliverable: a failure taxonomy from ≥100 traces, an eval suite gating CI, and traces on every request.
🚢 **SHIP POINT 1 (end of week 8):** hybrid RAG + eval harness + tracing, running end to end. Show it to someone.
→ [Agentic AI ch. 10–12](../tracks/agentic-ai/index.md#reading-order)

**D — Orchestration & protocols** *(wk 9–12, P0)*
Do: LangGraph for the durable, branching, checkpointed orchestrator; Pydantic AI for typed sub-agents; MCP for tools (one server in Python, one in Spring AI); durable execution + HITL before autonomy.
**Menu (choose on merit):** [LangGraph vs Pydantic AI vs vendor SDKs](../tracks/agentic-ai/index.md#framework-choice-guide) — the framework choice guide has the real trade-offs, not a default answer.
Deliverable: the orchestrator survives `kill -9` mid-run and resumes from checkpoint.
→ [Agentic AI ch. 13–21](../tracks/agentic-ai/index.md#reading-order) · [P3: MCP agent + failure analysis](../tracks/agentic-ai/projects/p3-mcp-agent-and-failure-analysis.md)

**E — Production hardening** *(wk 13–16, P0)*
Do: OWASP LLM/Agentic Top 10 + red-team in CI, LiteLLM routing with budgets, cost/latency work, SLOs, Foundry/AgentCore deploy.
🚢 **SHIP POINT 2 (end of week 16):** capstone is guardrailed, routed, observable and deployed — production-grade, not a demo.
→ [Agentic AI ch. 22–24, 27, 29](../tracks/agentic-ai/index.md#reading-order) · [P4: LLM gateway & guardrails](../tracks/agentic-ai/projects/p4-llm-gateway-and-guardrails.md)

**F — System design** *(wk 1–20, P0, ~2.25 h/wk, parallel to everything)*
Do: one topic + one case study per week, following the [recommended path](../tracks/system-design/index.md#recommended-path); estimation and scalability come first, consensus last.
→ [System Design](../tracks/system-design/index.md) · [AI System Design](../tracks/ai-system-design/index.md)

**G — Architecture & DSA** *(wk 1–24, P0/P1, ~3.5 h/wk combined, parallel)*
Do: one ADR/week on the capstone's real decisions; DSA patterns with re-solves on days 1/3/7/21 from the [problem tracker](../tracks/dsa/problem-tracker.md).
→ [Architecture](../tracks/architecture/index.md) · [DSA](../tracks/dsa/index.md)

**H — Staff+ & Communication** *(wk 1–26, P1, ~4 h/wk combined, parallel)*
Do: one Staff artifact every ~2 weeks (strategy doc, tech-debt proposal, mentoring plan…); 30 min/day of graded English/communication drills.
→ [Staff+ Skills](../tracks/staff-skills/index.md) · [Communication & English](../tracks/communication/index.md)

**I — Depth & specialisation** *(wk 17–20, P1)*
Do: DSPy/GEPA optimisation, self-hosted serving (vLLM/SGLang), a real fine-tuning ablation, Gossip Glomers for distributed-systems muscle.
Deliverable: a go/no-go memo on fine-tuning, backed by numbers.
→ [Agentic AI ch. 16, 25–26](../tracks/agentic-ai/index.md#reading-order) · [P5: optimise & serve](../tracks/agentic-ai/projects/p5-optimize-and-serve.md) · [P6: distributed systems lab](../tracks/agentic-ai/projects/p6-distributed-systems-lab.md)

🚢 **SHIP POINT 3 — Capstone v1.0 (end of week 24):** deployed on Azure, write-ups published, full interview loops run until scores hold steady. Weeks 25–26 are buffer: catch-up, then pick what's next.

## Exit criteria (gate, not vibe)

Every phase has a measurable gate — thresholds, not "I read the chapter." → [Phases & exit gates](phases.md)

## All weeks

Same plan, mechanical: one row per week with its build, checkpoint and theme. → [Weekly rhythm](weekly-template.md) · [Today](../today.md)

--8<-- "includes/weeks-table.md"
