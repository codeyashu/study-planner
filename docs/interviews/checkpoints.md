---
title: Interview checkpoints
tags: [interviews, checkpoints]
last_reviewed: 2026-09-25
---

# Interview checkpoints

!!! abstract "Format"
    Each checkpoint lists **scope** (what you have studied), **the exact loop** (prompts, time-boxes), **target scores** on the [unified rubric](rubric.md), and **what to do if below target**. Run the loop on the checkpoint weekend (Sat + Sun), log scores in the [score log](index.md#score-log), and adjust the next phase before Monday.
    Problem names refer to well-known LeetCode problems; if you have solved one recently, swap for another from the same pattern in the [problem tracker](../tracks/dsa/problem-tracker.md).

## Target trajectory

| Round | CP1 | CP2 | CP3 | CP4 | CP5 | CP6 |
|---|---|---|---|---|---|---|
| Bar applied | Senior | Senior | Senior→Staff | Staff | Staff | Staff |
| Coding | 2.5 | 3.0 | 3.0 | 3.0 | 3.0 | 3.5 |
| System design | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.5 |
| AI system design | — | 2.5 | 3.0 | 3.0 | 3.0 | 3.5 |
| LLD | — | — | 2.5 | — | 3.0 | 3.0 |
| Behavioral / Staff | 2.5 | 3.0 | 3.0 | 3.0 | 3.0 | 3.5 |

Note: a 3.0 at CP4 (Staff bar) is harder than a 3.0 at CP2 (Senior bar). Flat numbers across checkpoints still mean growth.

---

## CP0 — Baseline (week 0, Sat–Sun 2026-09-26/27)

Not scored against targets; it calibrates the skip list.

- **SD (45 min):** Design a [URL shortener](../tracks/system-design/case-studies/url-shortener.md) at 100M new URLs/month.
- **Coding (3 × 25 min):** Top K Frequent Elements · Longest Substring Without Repeating Characters · Product of Array Except Self.
- **AI self-assessment (30 min):** answer 10 L2/L3 questions from [LLM fundamentals](../tracks/agentic-ai/llm-fundamentals.md), [RAG fundamentals](../tracks/agentic-ai/rag-fundamentals.md), [agent patterns](../tracks/agentic-ai/agent-patterns.md) without notes; mark each confident / shaky / unknown.

**Use the result:** SD >= 3 → shorten Phase 1 SD fundamentals to review-only. Coding < 2 on 2+ problems → add 2 problems/week in Phase 1.

---

## CP1 — Week 4 (weekend of 2026-10-24/25)

**Scope:** Phase 1: Python foundations, LLM APIs and structured outputs, SD framework + fundamentals, DSA arrays/hashing/two pointers/sliding window, Staff archetypes.

| Round | Time | Exact prompt |
|---|---|---|
| System design | 45 min | "Design a URL shortener like bit.ly. 100M new links/month, 10:1 read:write, custom aliases, link expiry, click analytics available within 1 minute." (Compare with CP0.) |
| Coding 1 | 22 min | *Group Anagrams* |
| Coding 2 | 22 min | *Minimum Window Substring* (stretch medium/hard in sliding window) — or *Container With Most Water* if first attempt |
| AI (verbal) | 5 min | "Explain the difference between JSON mode, tool-calling, and schema-constrained decoding, and when each fails." |
| Behavioral | 15 min | "Tell me about a conflict with a peer or another team over a technical decision. What happened, what did you do, and what was the outcome?" |

**Targets:** SD 3.0 (Senior), Coding 2.5, Behavioral 2.5.

**If below target:**

- SD < 3 → re-read [framework and estimation](../tracks/system-design/framework-and-estimation.md); do 2 extra 30-min timed designs on classic prompts (pastebin, rate limiter) in weeks 5–6; record both.
- Coding < 2.5 → weekday DSA from 2.5 h to 3.5 h for 2 weeks (take the hour from Python reps); redo all failed problems 3 and 7 days later.
- Behavioral < 2.5 → write 6 STAR stories (conflict, failure, influence, ambiguity, mentoring, biggest impact) in a story bank; see [behavioral interviews](../tracks/staff-skills/behavioral-interviews.md).

---

## CP2 — Week 8 (weekend of 2026-11-21/22)

**Scope:** + RAG, evals, observability, DDD/hexagonal, SD storage/caching/search, DSA stack/binary search/linked list/trees.

| Round | Time | Exact prompt |
|---|---|---|
| System design | 45 min | "Design a [news feed](../tracks/system-design/case-studies/news-feed.md) for a social network with 300M DAU. Posts with media; feed ranked by recency with light personalisation; p99 feed load < 300 ms." |
| AI system design | 45 min | "Design an [enterprise RAG assistant](../tracks/ai-system-design/rag-system.md) over 2M internal documents (Confluence, SharePoint, PDFs) for 20k employees with document-level permissions. Answers must cite sources. How do you know it works?" |
| Coding 1 | 22 min | *Search in Rotated Sorted Array* |
| Coding 2 | 22 min | *Lowest Common Ancestor of a Binary Tree* then follow-up: iterative version |
| Behavioral | 20 min | "Tell me about a project that failed or missed its goals." + "Tell me about a time you had to make a decision with incomplete data." |

**Targets:** SD 3.0, AI SD 2.5, Coding 3.0, Behavioral 3.0 (Senior bar).

**If below target:**

- AI SD < 2.5 → the gap is almost always *evaluation* or *retrieval depth*. Write a 1-page design for the RAG prompt using your P2 ablation numbers; re-do the mock in week 9 with the [AI mock interviewer](ai-mock-interviewer.md).
- SD deep dive weak → pick the component you hand-waved (usually fan-out or cache invalidation) and write a 500-word deep dive; read the matching topic page ([caching](../tracks/system-design/caching.md), [partitioning](../tracks/system-design/partitioning-sharding.md)).
- Coding < 3 on trees → 5 extra tree problems in week 9 (recursion + BFS mix).

---

## CP3 — Week 12 (weekend of 2026-12-19/20)

**Scope:** + agents, LangGraph, MCP, A2A, memory, event-driven/sagas, SD queues/streams, DSA tries/heaps/backtracking/graphs. First LLD round. Start applying the Staff bar to SD.

| Round | Time | Exact prompt |
|---|---|---|
| System design | 45 min | "Design a [notification system](../tracks/system-design/case-studies/notification-system.md) that sends 1B notifications/day across push, email and SMS, with user preferences, rate limiting per user, retries, and exactly-once *user-visible* delivery." |
| AI system design | 45 min | "Design a [multi-agent platform](../tracks/ai-system-design/agent-platform.md) that lets 50 internal teams build and run agents that call internal APIs. Cover tool registry, identity/permissions, human approval, durability, evaluation, and cost control." |
| Coding 1 | 25 min | *Course Schedule II* |
| Coding 2 | 35 min | *Word Search II* (hard; trie + backtracking) |
| LLD | 45 min | "Design a parking lot system" — with follow-up change request: "add EV charging spots with time-based pricing and reservations." |
| Behavioral | 30 min | "Tell me about a time you influenced a decision outside your team without authority." + "Describe the most technically complex project you led." + "Tell me about a time you disagreed with your manager." |

**Targets:** SD 3.0 (moving to Staff bar), AI SD 3.0, Coding 3.0, LLD 2.5, Behavioral 3.0.

**Calibration:** book **one paid expert mock** (SD or AI SD) this checkpoint to check that your self-scores are not inflated. If paid score is >= 1 point lower than self-score, recalibrate: for CP4–CP6 subtract that gap from self-scores unless a peer/paid scorer agrees.

**If below target:**

- AI SD < 3 on agent platform → re-read [agent platform](../tracks/ai-system-design/agent-platform.md), [MCP](../tracks/agentic-ai/mcp.md), [durable execution](../tracks/agentic-ai/durable-execution-hitl.md); present your P3 failure analysis as a 10-minute talk to yourself on camera.
- LLD < 2.5 → 1 LLD per week in weeks 13–16 from the [prompt bank](mock-prompts.md#low-level-design-15), written in Python with tests.
- Graphs/backtracking weak → move 4 h from Phase 4's advanced-graphs block earlier.

---

## CP4 — Week 16 (weekend of 2027-01-16/17)

**Scope:** + guardrails/security, cost/latency, AI gateway, managed agent platforms, C4/arc42/Team Topologies, strategy doc, DSA advanced graphs/1-D DP. **Staff bar for all rounds from now on.**

| Round | Time | Exact prompt |
|---|---|---|
| System design | 60 min | "Design a [rate limiter](../tracks/system-design/rate-limiting.md) service used by every API in a company with 2,000 microservices across 3 regions. Support per-tenant, per-endpoint and global limits; < 2 ms added p99; survive a region loss. Then: how would you roll this out to 2,000 services owned by 150 teams?" |
| AI system design | 60 min | "Design a [multi-tenant LLM gateway](../tracks/ai-system-design/llm-gateway.md) for a company where 40 product teams use 5 model providers. Requirements: routing, fallbacks, per-team budgets, PII protection, prompt-injection defences, observability, and chargeback. Also: how do you [evaluate](../tracks/ai-system-design/evaluation-platform.md) that a model swap doesn't regress 40 products?" |
| Coding 1 | 22 min | *Network Delay Time* |
| Coding 2 | 22 min | *Coin Change* then follow-up: return the actual coins |
| Staff leadership | 45 min | "Walk me through a technical strategy you set for a group of teams: how did you identify the problem, get alignment, and measure success?" Follow-ups: "What would you do differently?", "Who disagreed and how did you handle it?", "Tell me about a time you had to push back on a senior leader." |

**Targets:** all 3.0 at Staff bar.

**If below target:**

- Staff leadership < 3 → the usual gap is *scope*: stories are team-level. Re-mine your 15 years for org-level stories; write your [technical strategy](../tracks/staff-skills/technical-strategy.md) artefact and use it as a story; practise with a Staff peer.
- SD rollout/migration question weak → read [legacy modernization](../tracks/architecture/legacy-modernization.md) and [influence without authority](../tracks/staff-skills/influence-without-authority.md); add a "rollout plan" section to every SD practice from now on.
- AI SD security weak → re-do the P4 threat model from memory in 20 minutes.

---

## CP5 — Week 20 (weekend of 2027-02-13/14)

**Scope:** + DSPy, inference/serving, fine-tuning, GraphRAG, distributed systems depth (Raft, Gossip Glomers), Python perf, Java 25 concurrency, DSA 2-D DP/intervals/greedy.

| Round | Time | Exact prompt |
|---|---|---|
| System design | 60 min | "Design a [distributed key-value store](../tracks/system-design/case-studies/distributed-kv-store.md) with tunable consistency, 10 TB across 3 regions. Deep dive: replication, failure detection, conflict resolution, rebalancing. When would you use consensus and where would you avoid it?" |
| AI system design | 60 min | "Design an [LLM inference platform](../tracks/ai-system-design/llm-serving-platform.md) serving 3 open-weight models to internal teams at 5k requests/min peak with p95 TTFT < 500 ms. Cover GPU capacity planning, batching, quantisation, autoscaling, multi-LoRA, and when to buy API capacity instead." Follow-up: "Leadership asks whether to fine-tune our own model. What do you recommend and how do you decide?" |
| Coding 1 | 22 min | *Merge Intervals* then follow-up *Insert Interval* |
| Coding 2 | 35 min | *Edit Distance* (hard-ish 2-D DP), then space-optimise |
| LLD | 45 min | "Design a thread-safe in-memory rate limiter / LRU cache with TTL supporting concurrent access; implement in Python (and describe Java 25 virtual-thread version)." See [concurrency and LLD](../tracks/dsa/concurrency-lld.md). |
| Behavioral | 30 min | "Tell me about a time you mentored someone into a bigger role." + "Describe an incident you led. What did you change afterwards?" + "Tell me about a time you killed or significantly changed a project." |

**Targets:** all 3.0 at Staff bar; LLD 3.0.

**If below target:**

- Distributed depth weak → Gossip Glomers write-up review; re-derive quorum math and Raft leader election on paper; watch the matching Kleppmann lecture.
- Serving/cost weak → redo the [capacity and cost planning](../tracks/ai-system-design/capacity-cost-planning.md) exercises with your P5 benchmark numbers.
- This is the last checkpoint before the final loop: if any round is <= 2.5, weeks 21–22 get **3 extra mocks** of that round type (swap out capstone polish, keep M7 deploy).

---

## CP6 — Week 24 (final loop, weekend of 2027-03-13/14)

**Scope:** everything. Simulates a full Staff/Principal onsite over two days, ideally with at least two human interviewers (one paid expert).

| Day | Round | Time | Exact prompt |
|---|---|---|---|
| Sat | Coding 1 | 45 min | *LRU Cache* (implement) → follow-up: make it thread-safe; then *Top K Frequent Words* |
| Sat | System design | 60 min | "Design a [payment system](../tracks/system-design/case-studies/payment-system.md) for a marketplace: 5k TPS peak, multiple PSPs, idempotency, ledger, reconciliation, refunds, and regulatory audit. How do you migrate from a monolith?" |
| Sat | LLD | 45 min | "Design a workflow/state-machine engine for shipment lifecycle events with pluggable transitions, guards and side effects; implement the core." |
| Sat | Behavioral / Staff | 45 min | Bar-raiser style: "Tell me about your highest-impact work in the last 3 years", "a time you were wrong", "how you grow Staff+ engineers", "a decision you made that was unpopular" — interviewer drills 3 levels deep on each |
| Sun | Coding 2 | 45 min | *Alien Dictionary* (or *Word Ladder*) + one medium DP (*Longest Increasing Subsequence*) |
| Sun | AI system design | 60 min | "Design an AI copilot for operations teams that triages exceptions, answers questions over contracts and SOPs, and takes actions in systems of record with human approval. Multi-tenant, auditable, $0.05/case budget." (This is your capstone: the interviewer should push hard on evals, safety and cost.) |
| Sun | Project deep dive | 45 min | "Walk me through the most significant system you built recently." Present the capstone: architecture, three ADRs, one failure analysis, what you'd change. Interviewer challenges every decision. |

**Targets:** each round >= 3.0 at Staff bar; weighted overall >= 3.5; no round below 3.

**If below target:** use buffer weeks 25–26: two mocks per week of the weakest round type, one paid; re-run that single round at the end of week 26. If still below, keep a 2-mock-per-week cadence while starting real applications with lower-stakes companies first (see [company process](company-process.md)).

---

## After each checkpoint (30 min, Sunday evening)

1. Fill the [score log](index.md#score-log).
2. Pick **one** dimension to fix (the lowest weighted score). Write the drill into next week's plan.
3. Add missed concepts as flashcards; add failed problems to the retry queue (3/7/21 days).
4. Update the weekly retro with the checkpoint result.
