---
title: Interviews
tags: [interviews, checkpoints]
last_reviewed: 2026-09-25
---

# Interviews

!!! abstract "Strategy in one paragraph"
    Interview readiness is a **checkpoint, not the goal**. Every 4 weeks (weeks 4, 8, 12, 16, 20, 24) you run a mock loop scored with the **same [unified rubric](rubric.md)**, so scores are comparable and you can see growth. Each loop is sized to what you have studied so far and ends in a short gap analysis that changes the next 4 weeks of the plan. By week 24 you run a full Staff loop (coding, system design, AI system design, low-level design, behavioral/leadership) and should be scoring at the Staff bar.

## Pages

| Page | Use it for |
|---|---|
| [Unified rubric](rubric.md) | Scoring every round, Senior vs Staff descriptors, scoring sheet |
| [Checkpoints](checkpoints.md) | Exact prompts, targets and remediation per checkpoint |
| [Mock prompt bank](mock-prompts.md) | 105 prompts across system design, AI system design, LLD, behavioral |
| [AI mock interviewer](ai-mock-interviewer.md) | Copy-paste prompts to run strict mocks with Claude/ChatGPT |
| [Company process](company-process.md) | How Staff/Principal loops work in 2026 and a prep timeline |

## Why the same rubric every time

- **Comparable scores:** growth only means something if the ruler does not change.
- **Targets rise, rubric doesn't:** CP1 expects Senior-bar 3s; CP6 expects Staff-bar 3–4s. The descriptors are fixed; the *target column* moves.
- **Fast diagnosis:** a persistent 2 on one dimension (e.g. "trade-off articulation") is a clearer signal than "SD felt bad".

## Loop composition per checkpoint

| CP | Week | Date (week ends) | Coding (DSA) | System design | AI system design | LLD | Behavioral / Staff | Total time |
|---|---|---|---|---|---|---|---|---|
| CP1 | 4 | Sun 2026-10-25 | 2 mediums (45 min) | 1 classic (45 min) | — (5-min verbal) | — | 1 story (15 min) | ~2 h |
| CP2 | 8 | Sun 2026-11-22 | 2 mediums (45 min) | 1 storage-heavy (45 min) | 1 RAG (45 min) | — | 2 stories (20 min) | ~2.75 h |
| CP3 | 12 | Sun 2026-12-20 | 1 medium + 1 hard (60 min) | 1 async/streaming (45 min) | 1 agent platform (45 min) | 1 (45 min) | 3 stories (30 min) | ~3.75 h |
| CP4 | 16 | Sun 2027-01-17 | 2 mediums (45 min) | 1 (60 min, Staff scope) | 1 gateway/eval (60 min) | — | Staff leadership round (45 min) | ~3.5 h |
| CP5 | 20 | Sun 2027-02-14 | 1 medium + 1 hard (60 min) | 1 distributed-depth (60 min) | 1 serving/cost (60 min) | 1 concurrency LLD (45 min) | 3 stories (30 min) | ~4.25 h |
| CP6 | 24 | Sun 2027-03-14 | 2 rounds (2 × 45 min) | 1 (60 min) | 1 (60 min) | 1 (45 min) | Staff behavioral + project deep dive (2 × 45 min) | ~6.5 h over 2 days |

Split long loops across Saturday and Sunday. Details and exact prompts: [checkpoints](checkpoints.md).

## How to run mocks

### Interviewer options (use at least two kinds per checkpoint)

| Option | Best for | Cost | How |
|---|---|---|---|
| **Peers / colleagues** | Behavioral, SD — realistic human pushback | Free | Trade mocks with a senior/Staff peer; give them the [rubric](rubric.md) and a prompt from the [bank](mock-prompts.md); they score, you swap next week |
| **Paid expert mocks** (Hello Interview, interviewing.io, Exponent and similar) | Calibrated Staff-bar feedback from current big-tech interviewers | Paid per session | Book 1 for CP3 or CP4 (calibration) and 1–2 for CP6. Ask the interviewer to score against *your* rubric in addition to theirs |
| **AI mock interviewer** | High-frequency reps, any hour, strict time-box | ~$0 | Use the prompts in [AI mock interviewer](ai-mock-interviewer.md); voice mode for realism |
| **Recording yourself** | Communication, filler words, structure, time management | Free | Record screen + audio (whiteboard tool such as Excalidraw); watch at 1.5× within 24 h; score yourself before reading any feedback |
| **Community mock platforms** | Coding under a stranger's eye | Free–low | Peer-matching platforms for DSA; good for CP1–CP3 nerves |

### Protocol for every mock

1. **Prepare the environment:** timer, whiteboard (Excalidraw / tldraw), plain editor without autocomplete for coding, camera on.
2. **No looking things up.** If you would not have it in a real interview, you do not have it now.
3. **Time-box strictly.** Stop at the bell; unfinished = unfinished.
4. **Score immediately** with the [scoring sheet](rubric.md#scoring-sheet): yourself first, then the interviewer/AI; record both.
5. **Write 3 lines:** biggest strength, biggest gap, one concrete drill for next week.
6. **Log it** in the table below and add any missed concepts as flashcards.

### Recording-review checklist

- [ ] Did I restate the problem and clarify requirements in the first 3–5 minutes?
- [ ] Did I say numbers out loud (QPS, storage, latency, cost)?
- [ ] Did I name at least two options before choosing, and say *why*?
- [ ] How many times did I go silent for more than 20 seconds?
- [ ] Did I drive, or did the interviewer have to pull me forward?
- [ ] Did I finish with risks, bottlenecks and what I would do next?

## Score log

Copy this table into `docs/log/` or your notes and fill it after each checkpoint. Scores are the **round average (1–4)** from the [scoring sheet](rubric.md#scoring-sheet).

| CP | Date | Coding | SD | AI SD | LLD | Behavioral/Staff | Overall | Target met? | Top gap | Plan change |
|---|---|---|---|---|---|---|---|---|---|---|
| CP0 baseline (wk 0) | 2026-09-26/27 | | | | — | — | | n/a | | |
| CP1 (wk 4) | | | | — | — | | | | | |
| CP2 (wk 8) | | | | | — | | | | | |
| CP3 (wk 12) | | | | | | | | | | |
| CP4 (wk 16) | | | | | — | | | | | |
| CP5 (wk 20) | | | | | | | | | | |
| CP6 (wk 24) | | | | | | | | | | |

!!! tip "Where the prep material lives"
    - Coding: [DSA track](../../dsa/approach-complexity.md) and the [problem tracker](../../dsa/problem-tracker.md)
    - System design: [framework and estimation](../../system-design/framework-and-estimation.md)
    - AI system design: [AI SD framework](../../ai-system-design/framework.md)
    - LLD: [concurrency and LLD](../../dsa/concurrency-lld.md), [design patterns](../../architecture/design-patterns.md)
    - Behavioral: [behavioral interviews](../behavioral-interviews.md), [Staff archetypes](../staff-archetypes.md)
