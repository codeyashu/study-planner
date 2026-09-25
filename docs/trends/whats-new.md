---
title: What changed in 2025–2026
tags: [trends, timeline]
last_reviewed: 2026-09-25
---

# What changed in 2025–2026

Dated timeline of events that affect the tracks and the [radar](radar.md). Newest first within each half-year.
Where only a month is known the day is omitted; entries marked *(approx.)* were reported by a single source or with a range and should be re-verified before you quote them.
Track tags: **AI** agents/LLMs · **SD** system design · **ARCH** architecture · **PY** Python · **JAVA** Java/Spring · **META** tooling for this site.

## 2026 (Jan–Sep)

| Date | Event | Track | Why it matters to you |
|---|---|---|---|
| 2026-09 | Hamel Husain publishes an updated "AI Evals: Everything You Need to Know" guide; the Oct 10 Maven evals cohort is reported as the last of 2026 | AI | Evals stay the highest-leverage skill; the free FAQ is the core reference. |
| 2026-09 | AWS Bedrock AgentCore: new Runtime reaches GA | AI | Managed agent hosting on AWS; keep agent code portable. |
| 2026-09-25 | Snapshot of current releases: LangGraph 1.2.x, Pydantic AI 2.x, DSPy 3.4, MS Agent Framework 1.x, Google ADK 2.x, Zensical 0.0.x | AI | Baseline used to build the radar. |
| 2026-08-26 | OpenAI Assistants API retired | AI | Migrate any Assistants code to Responses API / Agents SDK. |
| 2026-07-28 | MCP specification revision 2026-07-28: stateless core, `server/discover`, tasks as extension, MRTR, deprecation of Roots/Sampling/Logging and DCR | AI | Biggest protocol change since launch; matters for MCP server design and scaling. |
| 2026-07 | OTel GenAI semantic conventions move to a dedicated repository; still "Development" status | AI | Expect attribute renames; keep an adapter layer in tracing code. |
| 2026-06-12 | Spring AI 2.0.0 GA (Boot 4.x, Framework 7; MCP annotations; SSE deprecated; 2.0.1 followed with CVE fixes) | JAVA | Java track baseline. |
| 2026-06 | LlamaIndex Workflows 1.0 | AI | Another event-driven workflow model to compare with LangGraph. |
| 2026-05/06 *(approx.)* | Google ADK Python 2.0 GA with a graph Workflow Runtime | AI | Convergence of frameworks on graph-shaped workflows. |
| 2026-05-11 | LangGraph 1.2 | AI | Continued 1.x line after the 1.0 stability promise. |
| 2026-04 | Mem0 v3 released | AI | Memory layers maturing; still evaluate against simple baselines. |
| 2026-04 | OpenAI Agents SDK adds sandbox agents (beta) | AI | Isolated execution for code/file tasks is becoming a standard feature. |
| 2026-04-03 | Microsoft Agent Framework 1.0 GA (merges AutoGen and Semantic Kernel lines; those move to maintenance) | AI | Consolidation on the Azure side; Hold for AutoGen/SK in new work. |
| 2026-03-24 | *Designing Data-Intensive Applications*, 2nd edition announced as published | SD | The core system-design book is refreshed; see [books](../reading/books.md). |
| 2026-03-19 | OpenAI announces acquisition of Astral (uv, ruff, ty); tools stay open source | PY | Watch governance, but uv remains Adopt. |
| 2026-03-12 | A2A protocol v1.0 announced (signed Agent Cards; JSON-RPC/gRPC/REST) | AI | Cross-vendor agent-to-agent interop is now versioned and stable. |
| 2026-03-09 | OpenAI announces acquisition of promptfoo; stays OSS | AI | Red-teaming/eval tooling moves under a lab. |
| 2026-03 | AWS Bedrock AgentCore Policy and Evaluations reach GA | AI | Managed guardrails and agent evals appear at the platform level. |
| 2026-01 | ClickHouse acquires Langfuse; stays open source | AI | Observability consolidation; self-hosting remains possible. |
| 2026-01 | Research: "Is Agentic RAG worth it?" (arXiv 2601.07711) | AI | Evidence against defaulting to agentic retrieval. |
| 2026 (early) | Material for MkDocs enters maintenance mode; work moves to Zensical | META | This site's toolchain has a migration path; Zensical is pre-0.1 (0.0.x). |
| 2026 | Azure AI Foundry renamed Microsoft Foundry; Foundry Agent Service on the Responses API | AI | Naming changes in Azure docs and training modules. |
| 2026 | GEPA presented as an ICLR 2026 Oral; `dspy.GEPA` available | AI | Reflective optimisation becomes mainstream in DSPy. |

## 2025 (highlights)

| Date | Event | Track | Why it matters to you |
|---|---|---|---|
| 2025-12 | MCP donated to the Linux Foundation's Agentic AI Foundation; AGENTS.md also under LF stewardship | AI | Neutral governance lowers adoption risk. |
| 2025-12 *(approx.)* | OWASP Top 10 for Agentic Applications 2026 published | AI | Standard threat vocabulary for agent reviews. |
| 2025-11-25 | MCP specification 2025-11-25 (last stable before the 2026-07-28 revision) | AI | Reference version for most current SDKs and servers. |
| 2025-11-05 | Zensical announced by the Material for MkDocs team | META | Successor tooling for this site. |
| 2025-11 | Spring Boot 4.0 GA (Jackson 3, API versioning, JSpecify null-safety) | JAVA | Baseline for Spring AI 2.0. |
| 2025-10-22 | LangGraph 1.0 GA | AI | First stability commitment for the main agent orchestrator. |
| 2025-10-07 *(approx.)* | Python 3.14 released; free-threaded build later declared officially supported (PEP 779) | PY | Free-threading becomes a supported option, not an experiment. |
| 2025-09-16 | JDK 25 (LTS) GA: Scoped Values final, compact source files, flexible constructor bodies, compact object headers | JAVA | New LTS baseline for the Java track. |
| 2025-09 | Pydantic AI v1 released | AI | Stable API line for the Python-typed agent framework. |
| 2025-09 *(approx.)* | Claude Code SDK renamed Claude Agent SDK | AI | The agent loop behind Claude Code is available for general agents. |
| 2025-06-16 | Simon Willison names the "lethal trifecta" for agents | AI | Shared vocabulary for agent-security design reviews. |
| 2025-05 | Anthropic's contextual retrieval and multi-agent research posts circulate widely (dates approx.) | AI | Concrete numbers for RAG and multi-agent design. |
| 2025-01 | DeepSeek-R1 paper (arXiv 2501.12948) popularises RL with verifiable rewards | AI | Origin of the GRPO/RLVR interest in the radar. |

## How this page is maintained

The weekly agent appends new entries at the top of the current-year table, moving items only when a primary source confirms a date.
Do not add entries from social posts; link a release note, spec, or official announcement in the corresponding radar row or topic page instead.
