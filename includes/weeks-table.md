| Week | Starts | Phase | Theme | Build | Checkpoint |
|---|---|---|---|---|---|
| [W00](weeks/week-00.md) | 21 Sep | 0 · Baseline | Baseline & environment *(light)* | Dev environment ready (uv, Docker, Ollama, API keys) + baseline scores recorded in docs/log/ |  |
| [W01](weeks/week-01.md) | 28 Sep | 1 · Foundations | Agent patterns, structured outputs, SD framework | Capstone repo skeleton: uv + FastAPI + Pydantic structured-output /triage endpoint |  |
| [W02](weeks/week-02.md) | 05 Oct | 1 · Foundations | Tool calling, API design, two pointers | Capstone: typed tool calling loop (runbook search, service status, ticket create) |  |
| [W03](weeks/week-03.md) | 12 Oct | 1 · Foundations | Context engineering, workflows, sliding window | Capstone: routing + prompt-chaining workflow with history compaction |  |
| [W04](weeks/week-04.md) | 19 Oct | 1 · Foundations | Orchestrator-workers, AI-assisted dev, stack — interview-1 | Capstone: orchestrator-workers 'draft postmortem' with evaluator-optimizer loop + 10 golden examples | interview-1 |
| [W05](weeks/week-05.md) | 26 Oct | 2 · RAG + Evals | RAG fundamentals, caching, hexagonal | Capstone: RAG v0 — ingest runbooks/postmortems into pgvector, naive dense retrieval behind a Retriever port |  |
| [W06](weeks/week-06.md) | 02 Nov | 2 · RAG + Evals | Hybrid search + reranking (light week) *(light)* | Capstone: hybrid retrieval (BM25 + dense + metadata filters) with cross-encoder reranking |  |
| [W07](weeks/week-07.md) | 09 Nov | 2 · RAG + Evals | Evals I: error analysis + LLM-as-judge | Capstone: eval harness — error analysis on 100 traces, failure taxonomy, LLM-as-judge aligned to labels |  |
| [W08](weeks/week-08.md) | 16 Nov | 2 · RAG + Evals | Evals II in CI + observability — interview-2 | Capstone: promptfoo/DeepEval/Ragas in CI with thresholds + Langfuse tracing | interview-2 |
| [W09](weeks/week-09.md) | 23 Nov | 3 · Agents + Protocols | LangGraph orchestrator | Capstone: LangGraph orchestrator (state, nodes, conditional edges, Postgres checkpointer) |  |
| [W10](weeks/week-10.md) | 30 Nov | 3 · Agents + Protocols | MCP + Pydantic AI sub-agents | Capstone: Python MCP server (runbooks, service status) + Pydantic AI sub-agents inside LangGraph nodes |  |
| [W11](weeks/week-11.md) | 07 Dec | 3 · Agents + Protocols | Durable execution, HITL, multi-agent | Capstone: human-in-the-loop approval (interrupt/resume) + Spring AI MCP server wired in |  |
| [W12](weeks/week-12.md) | 14 Dec | 3 · Agents + Protocols | Protocols, memory, vendor SDKs (light) — interview-3 *(light)* | Capstone: A2A/AG-UI spike + Mem0 memory prototype + vendor SDK comparison notes | interview-3 |
| [W13](weeks/week-13.md) | 21 Dec | 4 · Production & AI Architecture | Guardrails & security | Capstone: guardrails layer (input/output/tool), prompt-injection red-team suite in CI |  |
| [W14](weeks/week-14.md) | 28 Dec | 4 · Production & AI Architecture | Cost, latency, routing | Capstone: LiteLLM routing (cheap → strong escalation), semantic + prompt caching, streaming latency budget |  |
| [W15](weeks/week-15.md) | 04 Jan | 4 · Production & AI Architecture | Managed platforms & production checklist | Capstone: Microsoft Foundry Agent Service spike + production-readiness checklist pass |  |
| [W16](weeks/week-16.md) | 11 Jan | 4 · Production & AI Architecture | Architecture docs & AI-era leadership — interview-4 | Capstone: C4 + arc42 doc set, observability dashboards, SLOs live | interview-4 |
| [W17](weeks/week-17.md) | 18 Jan | 5 · Scale & Depth | DSPy + Raft + free-threaded Python | Capstone: DSPy/GEPA-optimised triage classifier vs hand prompt, measured with the eval harness |  |
| [W18](weeks/week-18.md) | 25 Jan | 5 · Scale & Depth | Inference serving (light) *(light)* | Capstone: self-hosted vLLM (or Ollama) serving experiment with quantised model behind LiteLLM |  |
| [W19](weeks/week-19.md) | 01 Feb | 5 · Scale & Depth | Fine-tuning trade-offs, GraphRAG | Capstone: LoRA/QLoRA fine-tune experiment (Unsloth/TRL) vs prompt+DSPy baseline; GraphRAG spike |  |
| [W20](weeks/week-20.md) | 08 Feb | 5 · Scale & Depth | Consolidation — interview-5 | Capstone: advanced RAG decision implemented (or rejected with evidence); talk/blog draft | interview-5 |
| [W21](weeks/week-21.md) | 15 Feb | 6 · Capstone + Interview Loop | Capstone polish + STAR bank I | Capstone: deploy to Azure Container Apps + Foundry; end-to-end demo script |  |
| [W22](weeks/week-22.md) | 22 Feb | 6 · Capstone + Interview Loop | Write-ups + STAR bank II | Capstone: README, demo video, blog post #1 (eval-driven agent development) |  |
| [W23](weeks/week-23.md) | 01 Mar | 6 · Capstone + Interview Loop | Full mock loops | Capstone: blog post #2 (guardrails/architecture), final ADR review, portfolio page |  |
| [W24](weeks/week-24.md) | 08 Mar | 6 · Capstone + Interview Loop | Final loop — interview-6 | Capstone v1.0 shipped: repo, deployed demo, 2 blog posts, ADR set, arc42 doc | interview-6 |
| [W25](weeks/week-25.md) | 15 Mar | 7 · Buffer | Buffer I — catch-up + specialization choice *(light)* | Catch up on any unfinished capstone increments; choose a specialization (serving, evals platform, or multi-agent) and scope a 2-week spike |  |
| [W26](weeks/week-26.md) | 22 Mar | 7 · Buffer | Buffer II — catch-up + next plan *(light)* | Finish specialization spike; publish final retro and next-6-month plan |  |
