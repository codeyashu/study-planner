---
title: How others build roadmaps
last_reviewed: 2026-09-25
---

# How others build roadmaps (research, Sept 2026)

Before designing this roadmap, I analysed 17 public roadmaps and study systems. Here's what they do well, where they fall short, and what this site borrowed.

## Examples studied

| Roadmap | Shape | Borrowed | Weakness |
|---|---|---|---|
| [Lamarana12200/ai-engineering-roadmap](https://github.com/Lamarana12200/ai-engineering-roadmap) | 20 wks × 13 h, 7 phases, 8/2/2/1 h split | Phase **gates**, "Explain-it-Back Friday", an "ignorance log", one artifact per phase with a write-up | AI only |
| [tal7aouy/LLM-Engineering](https://github.com/tal7aouy/LLM-Engineering) | 24 wks, 6 phases + "2026 deep dives" | Big question bank; core path kept separate from deep dives | No tracking; starts at beginner level |
| [codejunkie99/agent-roadmap-2026](https://github.com/codejunkie99/agent-roadmap-2026) | 17 wks, primary sources | **AGENTS.md protocol**: an agent personalises and maintains the plan | No quizzes |
| [jugaldb — AI Engineering 101](https://jugaldb.substack.com/p/ai-engineering-101-the-once-a-day) | Daily 15-min reps + weekly build | **Daily rep + weekly build** rhythm | No tracking |
| [Toleflaco/ai-engineer-roadmap-java](https://github.com/Toleflaco/ai-engineer-roadmap-java) | Spring AI phases 0–6 | **ADRs as the progress log**; Java/Spring AI path | No weekly granularity |
| [JuanMelendres/cracking-code-interviews](https://github.com/JuanMelendres/cracking-code-interviews) | MkDocs site, L1–L4 syllabus, 897 flashcards | **Levelled L1–L4** questions, study packs, MkDocs + Pages | Very big, little AI |
| [ai-infra-curriculum principal track](https://github.com/ai-infra-curriculum/ai-infra-principal-engineer-learning) | 12 modules, 1000-pt scoring | **Soft skills as scored deliverables** | About 680 h |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Topic index + Anki decks | Pairing design topics with spaced repetition | Dated for LLM-era systems |
| [roadmap.sh AI Engineer](https://roadmap.sh/ai-engineer) · [Architect](https://roadmap.sh/software-architect) | Node graphs | Checking for breadth gaps | No time dimension or depth |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Scientist/Engineer tracks + notebooks | Reference depth for fine-tuning | No schedule |
| [Chip Huyen — AI Engineering](https://github.com/chiphuyen/aie-book) | Book chapters | Backbone for the AI track | Book, not a plan |
| [StaffEng](https://staffeng.com/guides/staff-archetypes/) | Archetypes, guides | Staff+ track framing | No plan |

## Gaps no single roadmap covered, and how this one fills them

1. **AI engineering + Staff-level architecture + DSA + Java together.** Those roadmaps cover one or two of these; this one runs them as parallel tracks with fixed weekly hours.
2. **Spaced repetition** is rare. Here: L1–L4 hidden-answer questions everywhere, DSA re-solve schedule, and a Sunday review hour.
3. **Interview checkpoints** are almost never scheduled. Here: 6 of them, scored on one rubric.
4. **Most roadmaps assume a beginner.** This one starts with a week-0 baseline and a skip list.
5. **They go stale.** This one has daily and weekly agents plus a [freshness contract](freshness.md).
6. **Progress lives in someone's head.** Here, GitHub issues feed `progress.yml`, which feeds the dashboard streak and heatmap.
