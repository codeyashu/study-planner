---
title: Books
tags: [reading, books]
last_reviewed: 2026-09-25
---

# Books

Chosen for a 15-year engineer: **read the chapters listed, skim the rest.** Editions checked as of September 2026.
Priority: **P0** read during the 24 weeks · **P1** read selectively when the topic comes up · **P2** reference / optional.

!!! tip "How to read technical books at this level"
    Read the chapter summary and diagrams first, then only sections that contradict or extend what you already believe.
    Write one ADR-style note per chapter: *"This changes how I would design X because…"*. If nothing changes, move on.

## System design & distributed systems

| Book | Author(s) | Edition / year | Track | Priority | Chapters to read (15-yr engineer) | Cost |
|---|---|---|---|---|---|---|
| [Designing Data-Intensive Applications](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) | Martin Kleppmann & Chris Riccomini | **2nd ed., 2026** | system-design | P0 | All of Part II (replication, sharding, transactions, "trouble with distributed systems", consistency & consensus) and the new cloud/data-systems material. Skim storage-engine chapters if you already know LSM vs B-tree. | Paid |
| [Understanding Distributed Systems](https://understandingdistributed.systems) | Roberto Vitillo | 2nd ed., 2022 | system-design | P1 | Part II (coordination: clocks, leader election, replication), Part IV (resiliency: timeouts, retries, circuit breakers, load shedding), Part V (monitoring). A fast refresher before DDIA. | Paid |
| [Database Internals](https://www.databass.dev/) | Alex Petrov | 1st ed., 2019 | system-design | P1 | Part II only (failure detection, leader election, replication & consistency, anti-entropy, distributed transactions, consensus). | Paid |
| [System Design Interview Vol. 1 & 2](https://bytebytego.com) | Alex Xu (+ Sahn Lam, Vol. 2) | 2020 / 2022 | system-design | P1 | Vol. 1 ch. 1–4 (framework, estimation) for interview structure; Vol. 2 ch. on proximity service, message queue, payment system, S3-like storage. Use as interview-format drills, not for depth. | Paid |
| [Site Reliability Engineering](https://sre.google/books/) | Google (Beyer et al.) | 2016 (free online) | system-design | P1 | Ch. 3 (embracing risk), 4 (SLOs), 6 (monitoring), 21–22 (handling overload, cascading failures). The SRE Workbook's SLO chapters too. | Free |
| [Release It!](https://pragprog.com/titles/mnee2/release-it-second-edition/) | Michael T. Nygard | 2nd ed., 2018 | system-design | P2 | Part I (stability anti-patterns & patterns: bulkheads, circuit breakers, steady state). The rest is dated. | Paid |

## AI engineering & AI system design

| Book | Author(s) | Edition / year | Track | Priority | Chapters to read | Cost |
|---|---|---|---|---|---|---|
| [AI Engineering](https://github.com/chiphuyen/aie-book) | Chip Huyen | 1st ed., 2025 (O'Reilly) | ai-system-design | P0 | Ch. 3–4 (evaluation methodology and evaluating AI systems), 6 (RAG and agents), 8 (dataset engineering, skim), 9 (inference optimisation), 10 (architecture & user feedback). Skip ch. 1–2 intro unless you want the history. | Paid (repo free) |
| [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) | Chip Huyen | 1st ed., 2022 | ai-system-design | P2 | Ch. 7–9 (deployment, data distribution shifts, continual learning) — relevant when agents sit next to classic ML. | Paid |
| [Generative AI System Design Interview](https://bytebytego.com/courses/genai-system-design-interview) | Ali Aminian & Hao Sheng | 2024 | ai-system-design | P1 | RAG chatbot, text-to-image, personalised headshots chapters for interview framing. Light on agents/evals (2026 reviews) — supplement with [articles](articles.md). | Paid |
| [Machine Learning System Design Interview](https://bytebytego.com/courses/machine-learning-system-design-interview) | Ali Aminian & Alex Xu | 2023 | ai-system-design | P2 | Ch. 1 (framework) + search/recommendation chapters — useful because retrieval/ranking underlies RAG. | Paid |
| [LLM Engineer's Handbook](https://github.com/PacktPublishing/LLM-Engineers-Handbook) :gem: | Paul Iusztin & Maxime Labonne | 1st ed., 2024 (Packt) | agentic-ai | P1 | Feature/training/inference pipeline chapters and the RAG + LLMOps chapters; follow the repo code rather than reading linearly. | Paid (code free) |
| [Hands-On Large Language Models](https://www.llm-book.com/) :gem: | Jay Alammar & Maarten Grootendorst | 1st ed., 2024 | agentic-ai | P1 | Tokens/embeddings and transformer-internals chapters (for the visuals), semantic search & RAG, fine-tuning embedding models. | Paid |
| [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) | Sebastian Raschka | 1st ed., 2024 | agentic-ai | P2 | Ch. 3 (attention) and ch. 7 (instruction fine-tuning) — do them as Phase 5 depth labs; the rest if curious. | Paid |
| [The RLHF Book](https://rlhfbook.com/) :gem: | Nathan Lambert | Online, continuously updated | agentic-ai | P2 | Reward modelling, DPO/direct alignment and RL-from-verifiable-rewards chapters before any GRPO/DPO lab. | Free |

## Architecture

| Book | Author(s) | Edition / year | Track | Priority | Chapters to read | Cost |
|---|---|---|---|---|---|---|
| [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/) | Mark Richards & Neal Ford | **2nd ed., 2025** | architecture | P0 | Architecture characteristics, architecture quantum, logical components, the styles chapters you *don't* use daily (space-based, event-driven, microkernel), and the new GenAI/architecture chapters. Skip "what is an architect". | Paid |
| [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) | Ford, Richards, Sadalage, Dehghani | 2021 | architecture | P0 | Ch. 7–8 (service granularity, reuse), 9–10 (data ownership, distributed data access), 11–12 (orchestration vs choreography, transactional sagas), 13 (contracts). The saga matrix is interview gold. | Paid |
| [Learning Domain-Driven Design](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/) | Vlad Khononov | 2021 | architecture | P1 | Part I (strategic design: subdomains, bounded contexts, context mapping) and ch. on architectural patterns/heuristics. Skip tactical basics if you know aggregates. | Paid |
| [Balancing Coupling in Software Design](https://coupling.dev) :gem: | Vlad Khononov | 2024 | architecture | P1 | The whole model is short: integration strength × distance × volatility. Gives you precise language for "this is too coupled". | Paid |
| [Architecture Modernization](https://www.manning.com/books/architecture-modernization) | Nick Tune (with Jean-Georges Perrin) | 2024 | architecture | P1 | Chapters on modernization strategy, Wardley mapping, EventStorming and org/team alignment — directly usable for L4 migration questions. | Paid |
| [Building Event-Driven Microservices](https://www.oreilly.com/library/view/building-event-driven-microservices/9798341622180/) | Adam Bellemare | **2nd ed., 2025** | architecture | P1 | Event design, data contracts, and the chapters on integrating with legacy/request-response systems. | Paid |
| [Team Topologies](https://teamtopologies.com/book) | Matthew Skelton & Manuel Pais | 2019 (check site for newer edition) | staff-skills | P1 | Ch. 4–7 (the four team types, three interaction modes, Conway's law applied). | Paid |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | John Ousterhout | 2nd ed., 2021 | architecture | P2 | Ch. 2–6 (complexity, deep modules, information hiding). A 2-evening read that sharpens API/tool design for agents. | Paid |

## Staff+ & career

| Book | Author(s) | Edition / year | Track | Priority | Chapters to read | Cost |
|---|---|---|---|---|---|---|
| [The Staff Engineer's Path](https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/) | Tanya Reilly | 2022 | staff-skills | P0 | Part I (big picture: maps, strategy), Part II ch. on finite time and leading big projects, Part III (levelling up others). | Paid |
| [Staff Engineer: Leadership Beyond the Management Track](https://staffeng.com/book) | Will Larson | 2021 | staff-skills | P0 | Part I (archetypes, operating at Staff, getting the title). Part II interviews: pick 3 whose role matches yours. | Paid (much free on site) |
| [Crafting Engineering Strategy](https://lethain.com/crafting-engineering-strategy/) | Will Larson | 2025 (O'Reilly) | staff-skills | P1 | The strategy-writing process and 2–3 case studies; aim to write one strategy doc for your capstone. | Paid (drafts free on blog) |
| [The Software Engineer's Guidebook](https://www.engguidebook.com/) | Gergely Orosz | 2023 | staff-skills | P1 | Parts on Staff/Principal engineer and "engineering at scale"; skip early-career parts. | Paid |

## Python, Java & DSA

| Book | Author(s) | Edition / year | Track | Priority | Chapters to read | Cost |
|---|---|---|---|---|---|---|
| [Fluent Python](https://www.fluentpython.com/) | Luciano Ramalho | 2nd ed., 2022 | python | P0 | Ch. 5 (data class builders), 8 & 15 (type hints, advanced typing, protocols), 17 (iterators/generators), 19–21 (concurrency, executors, asyncio), 23–24 (descriptors, metaprogramming) for the "how Pydantic works" level. | Paid |
| [Architecture Patterns with Python (Cosmic Python)](https://www.cosmicpython.com/) | Harry Percival & Bob Gregory | 2020 (free online) | python | P1 | Repository, unit of work, service layer, events & message bus chapters — the patterns behind a clean FastAPI + agent backend. | Free |
| [Python Concurrency with asyncio](https://www.manning.com/books/python-concurrency-with-asyncio) | Matthew Fowler | 2022 | python | P1 | Event-loop internals, concurrent web requests, asyncio + multiprocessing, synchronisation and queues chapters. | Paid |
| [Effective Java](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/) | Joshua Bloch | 3rd ed., 2018 | java | P2 | Items on generics, enums/annotations, lambdas/streams, concurrency. Pair with JDK 25 JEPs for what's changed. | Paid |
| [Java Concurrency in Practice](https://jcip.net/) | Brian Goetz et al. | 2006 | java | P2 | Ch. 2–5 and 16 (memory model) — still the foundation under virtual threads and structured concurrency. | Paid |
| [Spring AI in Action](https://www.manning.com/books/spring-ai-in-action) | Craig Walls | 2025 | java | P1 | RAG, tool calling and MCP chapters; cross-check APIs against Spring AI 2.0 docs (the book predates 2.0 GA). | Paid |
| [Coding Interview Patterns](https://bytebytego.com/courses/coding-patterns) | Alex Xu & Shaun Gunawardane | 2024 | dsa | P1 | Pattern chapters matching your NeetCode weaknesses (graphs, DP, intervals, heaps). | Paid |
| [Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/) :gem: | Jeff Erickson | 2019 (free) | dsa | P2 | Recursion/backtracking, dynamic programming and graph chapters when a pattern "doesn't click". | Free |
