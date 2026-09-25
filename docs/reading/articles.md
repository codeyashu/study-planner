---
title: Must-read articles & essays
tags: [reading, articles]
last_reviewed: 2026-09-25
---

# Must-read articles & essays

Curated for a 15-year engineer. Each item says **why** it earns a slot, an estimated read time, and the **roadmap week** where it fits best.
Use these for the weekly 1-hour deep-read slot (see [reading system](index.md)); apply *read → note → 1 flashcard*.

!!! info "Phase → week mapping"
    **P1** wk 1–4 foundations · **P2** wk 5–8 RAG & evals · **P3** wk 9–12 agents & protocols · **P4** wk 13–16 production & architecture ·
    **P5** wk 17–20 scale & depth · **P6** wk 21–24 capstone & interviews

## Agents & context engineering

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic | The canonical "workflows vs agents" taxonomy (prompt chaining, routing, orchestrator-workers, evaluator-optimizer). Start every agent design here. | 20 min | P3 · wk 9 |
| [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng :gem: | Planning / memory / tool-use decomposition with references to every foundational paper; still the best mental model. | 45 min | P3 · wk 9 |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic | Treats context as a finite budget: compaction, just-in-time retrieval, sub-agents, note-taking. The 2025–26 successor to "prompt engineering". | 25 min | P3 · wk 10 |
| [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) :gem: | Production lessons: KV-cache hit rate as the key metric, masking tools instead of removing them, file system as memory. | 20 min | P3 · wk 10 |
| [How contexts fail and how to fix them](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) — Drew Breunig :gem: | Names the failure modes (poisoning, distraction, confusion, clash) so you can debug long-running agents systematically. | 15 min | P3 · wk 10 |
| [Context Rot](https://research.trychroma.com/context-rot) — Chroma research :gem: | Empirical evidence that performance degrades well before the advertised context limit; kills "just stuff it in 1M tokens". | 20 min | P2 · wk 6 |
| [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — Anthropic | Honest multi-agent write-up: token cost (~15x chat), orchestration prompts, eval approach, when multi-agent is worth it. | 25 min | P3 · wk 11 |
| [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) — Cognition | The counter-argument: context sharing and conflicting decisions make naive multi-agent brittle. Read right after the Anthropic post and form your own view. | 12 min | P3 · wk 11 |
| [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — Anthropic | Tool design as API design for a non-deterministic caller: namespacing, token-efficient responses, eval-driven tool iteration. | 20 min | P3 · wk 10 |
| [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic | Why loading hundreds of MCP tool schemas into context doesn't scale and how "tools as code" cuts tokens. | 15 min | P3 · wk 12 |
| [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) — HumanLayer :gem: | Engineering principles for agents you can operate: own your prompts, own your control flow, stateless reducer, pause/resume. | 40 min | P4 · wk 13 |
| [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — OpenAI (PDF) | Vendor view on orchestration patterns and guardrails layering; useful to compare with Anthropic's taxonomy. | 30 min | P3 · wk 9 |
| [Agents](https://huyenchip.com/2025/01/07/agents.html) — Chip Huyen | Book-chapter depth on planning, tool selection and failure modes of agents, with evaluation angles. | 50 min | P3 · wk 11 |

## RAG & search

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/) — Eugene Yan | Seven patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback) — a system-design checklist. | 60 min | P2 · wk 5 |
| [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — Anthropic | Numbers on contextual embeddings + BM25 + reranking reducing retrieval failures; a clean baseline for your RAG lab. | 15 min | P2 · wk 5 |
| [Rerankers and two-stage retrieval](https://www.pinecone.io/learn/series/rag/rerankers/) — Pinecone | Clear explanation of bi-encoder vs cross-encoder and why two-stage retrieval wins on quality/latency. | 20 min | P2 · wk 6 |
| [Hybrid search revamped](https://qdrant.tech/articles/hybrid-search/) — Qdrant | Fusion strategies (RRF, weighted), multi-stage queries; practical with code. | 20 min | P2 · wk 6 |
| [Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/) — Jason Liu :gem: | A flywheel: synthetic questions → retrieval metrics → segment failures → targeted fixes. Very "consultant-practical". | 25 min | P2 · wk 7 |
| [There Are Only 6 RAG Evals](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/) — Jason Liu :gem: | Reduces RAG eval to relationships between question, context and answer; cuts through metric soup. | 12 min | P2 · wk 7 |
| [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) — Microsoft Research | Why GraphRAG's up-front indexing cost is the problem and how deferred graph construction changes the economics. | 15 min | P5 · wk 18 |

## Evals

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — Hamel Husain | Three levels of evals (unit, human/model, A/B) tied to a real product; the "why" before any tooling. | 30 min | P2 · wk 7 |
| [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) — Hamel Husain & Shreya Shankar :gem: | Error-analysis-first: open coding, axial coding, binary pass/fail judges. Answers the questions you'll actually hit. | 60 min | P2 · wk 7–8 |
| [Using LLM-as-a-Judge for evaluation](https://hamel.dev/blog/posts/llm-judge/) — Hamel Husain | "Critique shadowing": align a judge with a domain expert and measure agreement before trusting it. | 30 min | P2 · wk 8 |
| [Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/) — Eugene Yan | Survey of judge techniques, biases, and when they correlate with humans; numbers from many papers. | 45 min | P2 · wk 8 |
| [Task-Specific LLM Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/) — Eugene Yan | Which metrics hold up for classification, summarisation, translation, toxicity; practical thresholds. | 30 min | P2 · wk 7 |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Anthropic | Agent-specific eval design: graders, transcripts vs outcomes, capability vs regression suites. | 25 min | P3 · wk 12 |
| [Who Validates the Validators?](https://arxiv.org/abs/2404.12272) — Shankar et al. | Research on "criteria drift": you can't fully define eval criteria before seeing outputs. Justifies iterative eval design. | 30 min | P2 · wk 8 |

## LLM production lessons

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [What We've Learned From A Year of Building with LLMs](https://applied-llms.org/) — Yan, Bischof, Frye, Husain, Liu, Shankar | Tactical, operational and strategic lessons from six practitioners. The best single overview. | 90 min | P1 · wk 3 |
| [Building A Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html) — Chip Huyen | Reference architecture: context construction, guardrails, router, gateway, cache, agent patterns, observability. Use as your capstone skeleton. | 45 min | P4 · wk 13 |
| [All the Hard Stuff Nobody Talks About when Building Products with LLMs](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm) — Honeycomb :gem: | Early but timeless: context windows, latency, prompt injection, legal — from a team that shipped. | 20 min | P1 · wk 3 |
| [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Simon Willison | Private data + untrusted content + exfiltration channel = breach. The security frame for every agent design review. | 10 min | P3 · wk 12 |
| [Prompt injection: What's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) — Simon Willison | Concrete exploit scenarios; why "better prompts" don't fix it. | 15 min | P4 · wk 14 |
| [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/) — Bharani Subramaniam & Martin Fowler | Pattern-language treatment (RAG, guardrails, evals, fine-tuning) in architecture vocabulary — handy for ADRs. | 60 min | P4 · wk 14 |

## Distributed systems classics

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/) — Jeff Hodges | Short list of hard-won truths (failure is common, backpressure, measure p99). Re-read yearly. | 15 min | P1 · wk 1 |
| [The Log](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) — Jay Kreps | The log as the unifying abstraction behind databases, Kafka and stream processing. Foundation for event-driven architecture. | 45 min | P1 · wk 2 |
| [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — AWS Builders' Library | Retry storms, jitter, and retry budgets explained by AWS; applies directly to LLM-provider calls. | 20 min | P1 · wk 2 |
| [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) — AWS Builders' Library :gem: | Why queues hide overload, LIFO vs FIFO under backlog, shuffle-sharding. The rest of the [library](https://aws.amazon.com/builders-library/) is equally good. | 25 min | P4 · wk 15 |
| [The Tail at Scale](https://cacm.acm.org/research/the-tail-at-scale/) — Dean & Barroso | Why p99 dominates at fan-out; hedged requests and tied requests. Required for any latency discussion. | 30 min | P5 · wk 17 |
| [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html) — Martin Kleppmann | Why CAP is a poor design vocabulary; use linearizability, latency and consistency models instead. Interview gold. | 20 min | P1 · wk 3 |
| [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) — Martin Kleppmann | Fencing tokens, why Redlock is unsafe under timing assumptions. Classic L3 interview material. | 25 min | P5 · wk 18 |
| [Load Balancing](https://samwho.dev/load-balancing/) — Sam Who :gem: | Interactive visual essay on round-robin, least-connections, PEWMA. Best intuition-builder there is. | 20 min | P1 · wk 1 |
| [Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/) — Unmesh Joshi | WAL, leader & followers, high-water mark, lease, generation clock — named patterns with code. | 2 h (catalogue) | P5 · wk 17–18 |
| [How Discord Stores Trillions of Messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) — Discord | Cassandra → ScyllaDB migration, hot partitions, request coalescing via data services. A perfect case study. | 20 min | P5 · wk 19 |

## Architecture

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html) — Martin Fowler | The default stance for new systems; pairs with modular-monolith discussions. | 10 min | P4 · wk 15 |
| [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — Michael Nygard | The original ADR post. Short; defines the format you'll use in `docs/log/adrs/`. | 10 min | P4 · wk 13 |
| [Choose Boring Technology](https://mcfunley.com/choose-boring-technology) — Dan McKinley | "Innovation tokens" — the argument you need when every team wants a new agent framework. | 15 min | P4 · wk 16 |
| [Online migrations at scale](https://stripe.com/blog/online-migrations) — Stripe | Dual-write → backfill → read switch → cleanup; the migration pattern Staff engineers own. | 15 min | P4 · wk 16 |
| [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) — Shopify | Modular monolith with enforced boundaries instead of microservices. A strong counterweight to microservice defaults. | 20 min | P4 · wk 15 |

## Staff+ & career

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [Staff archetypes](https://staffeng.com/guides/staff-archetypes/) — Will Larson | Tech lead, architect, solver, right hand — decide which one you're aiming for. | 15 min | P1 · wk 1 |
| [Work on what matters](https://lethain.com/work-on-what-matters/) — Will Larson | Avoid snacking and preening; find the work the company actually needs. | 10 min | P1 · wk 4 |
| [Writing an engineering strategy](https://lethain.com/eng-strategies/) — Will Larson | How to write strategy docs that get used; a core Staff artifact. | 20 min | P4 · wk 16 |
| [Being Glue](https://noidea.dog/glue) — Tanya Reilly | The invisible technical-leadership work, and how to make it count for promotion. | 25 min | P6 · wk 21 |
| [How I ship projects at big tech companies](https://www.seangoedecke.com/how-to-ship/) — Sean Goedecke :gem: | "Shipping is a social construct": owning the outcome, not the code. Candid and very senior. His [blog](https://www.seangoedecke.com/) is a gem overall. | 15 min | P6 · wk 22 |
| [The Engineer/Manager Pendulum](https://charity.wtf/2017/05/11/the-engineer-manager-pendulum/) — Charity Majors | Frames the IC vs manager choice for a 15-year engineer. | 15 min | P6 · wk 24 |

## Python & Java

| Article | Why it matters | Read | Fits |
|---|---|---|---|
| [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html) — Python docs | Free-threaded build support, template strings, deferred annotations, multiple interpreters. Know it for interviews. | 40 min | P1 · wk 2 |
| [Python free-threading guide](https://py-free-threading.github.io/) :gem: | How to run/test/port to 3.14t; which libraries are ready. | 30 min | P5 · wk 19 |
| [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) — Alexis King | The idea behind Pydantic-at-the-boundary and typed domain models; language-agnostic. | 25 min | P1 · wk 3 |
| [Notes on structured concurrency](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) — Nathaniel J. Smith :gem: | Why `asyncio.TaskGroup` and Java's StructuredTaskScope exist. Changes how you write concurrent agents. | 40 min | P3 · wk 10 |
| [JEP 444: Virtual Threads](https://openjdk.org/jeps/444) — OpenJDK | Primary source on virtual threads, pinning and when they help; basis for Spring Boot 4 concurrency. | 30 min | P4 · wk 14 |
| [JEP 505: Structured Concurrency (Fifth Preview)](https://openjdk.org/jeps/505) — OpenJDK | Still preview in JDK 25; compare with Python TaskGroup for the Java track. | 20 min | P4 · wk 14 |
