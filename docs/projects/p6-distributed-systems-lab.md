---
title: "P6: Distributed systems lab (Gossip Glomers)"
tags: [projects, phase-5, system-design, distributed-systems]
last_reviewed: 2026-09-25
---

# P6: Distributed systems lab (Gossip Glomers)

!!! abstract "At a glance"
    **Phase:** 5 · **Weeks:** 17–20 (~2 h/week of system-design time + one Sunday) · **Feeds:** system design depth, capstone reliability (idempotency, retries), interview stories
    **Goal:** Solve the Fly.io **Gossip Glomers** challenges (echo, unique IDs, broadcast, grow-only counter, Kafka-style log, totally-available transactions) against the Maelstrom test harness, in **Go** (the reference path) and/or **Python**, and write up what you learned about partitions, latency, consistency and the cost of coordination.
    **Done when:** challenges 1–5 pass Maelstrom (including partition runs), 6a–6b pass, and a write-up explains your design choices with measured msgs-per-op and latency.

## Why this project

You are already strong in system design at the whiteboard. What separates Staff from Senior in distributed-systems deep dives is having *felt* the failure modes: a broadcast that works until the network partitions, a counter that double-counts on retry, a log that loses writes under concurrency. Maelstrom (built on Jepsen's checker) turns hand-waving into pass/fail. It is also the best preparation for [consensus](../tracks/system-design/consensus-raft.md) and [consistency models](../tracks/system-design/consistency-models.md) questions.

## Skills practised

- [Consistency models, CAP and PACELC](../tracks/system-design/consistency-models.md)
- [Replication](../tracks/system-design/replication.md), [partitioning](../tracks/system-design/partitioning-sharding.md)
- [Consensus: Raft, leases, fencing](../tracks/system-design/consensus-raft.md)
- [Messaging and streaming](../tracks/system-design/messaging-streaming.md) (the Kafka-style log challenge)
- [Reliability patterns](../tracks/system-design/reliability-patterns.md): retries, idempotency
- [Concurrency models in Python](../tracks/python/concurrency-models.md) / [asyncio](../tracks/python/asyncio-deep.md)
- Case study: [distributed key-value store](../tracks/system-design/case-studies/distributed-kv-store.md)

## Spec

### Challenges

| # | Challenge | Core idea | What to measure / learn |
|---|---|---|---|
| 1 | Echo | Maelstrom protocol, node runtime | Your node framework (reuse for all) |
| 2 | Unique ID generation | Coordination-free IDs | Why node-id + counter / time-based schemes stay unique under partitions |
| 3a–3e | Broadcast (single, multi-node, fault-tolerant, efficient I & II) | Gossip, topology, anti-entropy, batching | msgs-per-op vs median/max latency trade-off; tree vs grid vs custom topology |
| 4 | Grow-only counter | CRDT-ish counter on a sequentially consistent KV | Retries + CAS; why "add then read" is not linearizable here |
| 5a–5c | Kafka-style log | Offsets, commits, a linearizable KV (`lin-kv`) | Where you *need* linearizability vs where you can relax; contention on offsets |
| 6a–6c | Totally-available transactions | Read uncommitted → read committed | Isolation anomalies (dirty writes/reads, G0/G1) and what availability costs |

### Language plan

- **Go path (recommended first):** Fly.io's challenge text and the Maelstrom Go library make this the smoothest route; also a useful second language for infra roles.
- **Python path:** Maelstrom ships demo nodes in several languages; write your own small Python node runtime (stdin/stdout JSON, asyncio for RPC with timeouts). Re-implement challenges 3 and 4 in Python after Go to compare ergonomics and performance.

### Required analysis in the write-up

1. **Broadcast efficiency:** table of topology × batching interval → msgs-per-op, median latency, max latency; show where you met the 3d/3e targets stated in the challenge.
2. **Partition behaviour:** what happens during and after `--nemesis partition`; how anti-entropy converges.
3. **Consistency reasoning:** for the counter and log, state the consistency model each operation provides and why the checker accepts/rejects it.
4. **Transactions:** which anomalies you prevented at each isolation level and how.
5. **Transfer to production:** map each lesson to a real system (Kafka, Cassandra, DynamoDB, Postgres isolation, your capstone's idempotent tool execution).

## Step-by-step plan

| Step | When | What |
|---|---|---|
| 1 | Wk 17 weekday | Install Maelstrom (JVM + Graphviz + gnuplot per its docs); read the protocol doc; run the demo |
| 2 | Wk 17 weekday | Challenges 1–2 in Go |
| 3 | Wk 17 Sun (1 h) | Broadcast 3a–3c; partition runs |
| 4 | Wk 18 weekdays | 3d–3e efficiency: experiment with topologies and batching; record table |
| 5 | Wk 19 weekdays | Counter (4) and Kafka-style log (5a–5b); 5c optimisation |
| 6 | Wk 20 weekdays | Transactions 6a–6b (6c stretch) |
| 7 | Wk 20 Sun (1 h) | Python port of 3 and 4; write-up |

## Acceptance criteria

- [ ] Challenges 1–5b pass Maelstrom with the workloads/node counts specified by each challenge, including partition nemesis where required
- [ ] 3d and 3e: msgs-per-op and latency targets from the challenge met; table shows your trade-off exploration
- [ ] 6a–6b pass
- [ ] Python implementations of 3 (at least 3c) and 4 pass
- [ ] Repo has a README per challenge: approach, invariants, test command, results
- [ ] Write-up (1500+ words) with the five analysis sections above

## Stretch

- 5c and 6c.
- Implement a toy Raft on Maelstrom's `lin-kv` workload (see Maelstrom's Raft guide) and compare with your 5x solution.
- Read two Jepsen analyses of systems you use and map their anomalies to your 6x lessons.
- Add a Maelstrom-inspired fault-injection test to the capstone (duplicate/delayed tool responses) to verify idempotent execution.

## Deliverables

1. Public repo `gossip-glomers` (Go + Python) with per-challenge READMEs and CI running at least the fast Maelstrom tests
2. Write-up: *"What Gossip Glomers taught a system designer"* (publishable)
3. 3 flashcards per challenge in your spaced-repetition deck
4. One capstone ADR amendment if a lesson changes the idempotency/retry design

## Rubric

Generic [rubric](rubric.md) (code quality, docs, write-up apply; evals = Maelstrom checks; observability = Maelstrom results analysis) plus:

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Correctness | < 3 challenges pass | 1–3 pass | 1–5b + 6a–6b pass incl. partitions | Plus 5c/6c or Raft stretch |
| Efficiency | Not measured | Meets targets by luck | Topology/batching table, targets met | Plus explanation of the latency–traffic Pareto frontier |
| Consistency reasoning | Absent | Names models | Correctly states guarantees per operation | Plus counter-examples (histories) showing why weaker designs fail |
| Transfer | None | Generic | Maps to named production systems | Plus concrete capstone change backed by a test |
| Polyglot | One language | Second language partial | Go + Python for 3 and 4 | Plus comparison of runtime models (goroutines vs asyncio) with numbers |

## Resources

| Resource | Why |
|---|---|
| [Fly.io Gossip Glomers](https://fly.io/dist-sys/) :gem: | The challenges |
| [Maelstrom](https://github.com/jepsen-io/maelstrom) | Test harness, protocol docs, Raft guide |
| [Jepsen analyses](https://jepsen.io/analyses) | Real-world anomalies |
| [Kleppmann: Distributed Systems lecture notes (Cambridge)](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf) | Theory behind broadcast, CRDTs, consensus |
| [Kleppmann lectures (YouTube playlist)](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) | Video companion |
| [The Secret Lives of Data: Raft](https://thesecretlivesofdata.com/raft/) :gem: | Visual Raft |
| [Unmesh Joshi: Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/) | Named patterns you will reinvent |
| [Marc Brooker's blog](https://brooker.co.za/blog/) :gem: | Retries, backoff, metastability |
| [DDIA 2nd edition](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) | Chapters on replication, consistency, transactions |
