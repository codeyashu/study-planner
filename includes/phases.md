## Phase 0 — Baseline

**Week 0** · Calibrate starting level and get the toolchain working so week 1 starts with building, not setup.

**Gate (exit criteria):**

- [ ] Baseline SD mock scored with the rubric
- [ ] 3 DSA mediums attempted with times logged
- [ ] AI self-assessment scores + skip list written to docs/log/baseline.md
- [ ] uv, Docker, Ollama and API keys verified with a smoke-test call

## Phase 1 — Foundations

**Weeks 1–4** · Refresh modern Python/Java/LLM foundations and start the capstone with structured outputs, tools and workflow patterns.

**Gate (exit criteria):**

- [ ] Capstone repo with FastAPI /triage returning validated structured output and a typed tool loop
- [ ] Orchestrator-workers + evaluator-optimizer feature working with 10 golden examples
- [ ] ADRs 001-004 written; AGENTS.md in capstone repo
- [ ] Arrays/hashing, two pointers, sliding window, stack: 20+ problems solved
- [ ] interview-1 mock scored >= 2.5/4 average on the rubric

## Phase 2 — RAG + Evals

**Weeks 5–8** · Ship hybrid RAG with reranking and an eval-driven workflow: error analysis, aligned judges and CI gates with tracing.

**Gate (exit criteria):**

- [ ] Hybrid retrieval beats dense-only on the golden set (hit rate@5 reported)
- [ ] Failure taxonomy from >= 100 traces; LLM judge TPR/TNR >= 0.8 against hand labels
- [ ] Eval job in CI failing on threshold regressions; Langfuse traces for every request
- [ ] Design doc v1 reviewed; ADRs 005-008
- [ ] interview-2 mock scored >= 2.75/4

## Phase 3 — Agents + Protocols

**Weeks 9–12** · Build a durable LangGraph orchestrator with Pydantic AI sub-agents, MCP servers in Python and Spring AI, HITL and memory.

**Gate (exit criteria):**

- [ ] LangGraph orchestrator survives kill/restart mid-run and resumes from checkpoint
- [ ] HITL approval gates every side-effecting tool call
- [ ] Python MCP server + Spring AI MCP server both called by the orchestrator over Streamable HTTP
- [ ] Written multi-agent platform design + influence plan artifact
- [ ] interview-3 mock scored >= 3/4

## Phase 4 — Production & AI Architecture

**Weeks 13–16** · Make the capstone production-grade (guardrails, routing, cost, observability, SLOs) and produce Staff-level architecture/strategy artifacts.

**Gate (exit criteria):**

- [ ] promptfoo OWASP agentic red-team suite in CI with no high-severity failures
- [ ] Routing cuts cost per resolved incident >= 30% without eval regression
- [ ] SLOs + burn-rate alerts + online evals live; C4 + ADRs 013-016
- [ ] Strategy doc, tech-debt proposal and AI adoption plan written
- [ ] interview-4 mock scored >= 3/4

## Phase 5 — Scale & Depth

**Weeks 17–20** · Go deep: DSPy/GEPA, inference serving, fine-tuning trade-offs, advanced RAG, distributed consensus, free-threaded Python, JVM concurrency.

**Gate (exit criteria):**

- [ ] DSPy vs hand-prompt vs fine-tune ablation written with numbers
- [ ] Self-hosted model serving experiment with cost/quality comparison
- [ ] Gossip Glomers broadcast challenge passing; Raft explained in < 5 min
- [ ] Mentoring plan + talk/blog draft done
- [ ] interview-5 mock scored >= 3.25/4

## Phase 6 — Capstone + Interview Loop

**Weeks 21–24** · Ship capstone v1.0 on Azure with write-ups, and run full interview loops until scores are consistently strong.

**Gate (exit criteria):**

- [ ] Capstone deployed on Azure Container Apps + Foundry with passing smoke evals
- [ ] 2 blog posts, README, demo video, arc42 doc and ADR set 001-024 published
- [ ] STAR bank with 12+ stories
- [ ] interview-6 mock scored >= 3.5/4 on every dimension

## Phase 7 — Buffer

**Weeks 25–26** · Catch up on slipped work and pick a specialization for the next 6 months.

**Gate (exit criteria):**

- [ ] No P0 task left incomplete in progress.yml
- [ ] Specialization spike written up
- [ ] Final retro + next-6-month plan published
