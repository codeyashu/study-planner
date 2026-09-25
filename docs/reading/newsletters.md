---
title: Newsletters
tags: [reading, newsletters]
last_reviewed: 2026-09-25
---

# Newsletters

Status and cadence as of **September 2026**. Cadence is approximate; "dormant" = no new issue for ~6+ months when last checked.
Items with **RSS = yes** that matter most are already wired into the [daily feed](feed.md) via `data/feeds.yml`; the rest go to email
(create a dedicated inbox label/filter so they never land in your primary inbox).

!!! tip "Priority legend"
    - **Subscribe now** — read or skim every issue; ≤ 12 of these in total.
    - **Skim** — glance at the headlines via the feed; open 1 in 4.
    - **Optional** — follow only if the topic becomes a live need; many are better visited on demand.

    `:gem:` = lesser-known but excellent.

## AI engineering

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [Simon Willison's Weblog](https://simonwillison.net/) | Simon Willison | LLM tools, prompt injection, hands-on experiments | Daily blog; newsletter ~weekly | Free | Yes | Subscribe now | The single best "practitioner's log" of the LLM era; coined *lethal trifecta*; every claim is tried in code. |
| [Latent Space](https://www.latent.space/) | swyx & Alessio Fanelli | AI engineering, interviews, conference writeups | Weekly | Free / paid | Yes | Subscribe now | Defined the "AI engineer" role; podcast guests are the people building the frameworks you use. |
| [AINews (smol.ai)](https://news.smol.ai/) | swyx / smol.ai | AI-generated daily digest of X/Discord/Reddit | Daily | Free | Yes | Skim | Replaces doom-scrolling; read the top summary only. |
| [Hamel Husain](https://hamel.dev/) :gem: | Hamel Husain | Evals, error analysis, LLM product debugging | Irregular (~monthly) | Free | Yes | Subscribe now | The clearest voice on evals; the [evals FAQ](https://hamel.dev/blog/posts/evals-faq/) is canonical for Phase 2. |
| [Eugene Yan](https://eugeneyan.com/) | Eugene Yan | Applied ML/LLM patterns, recsys, evals | ~Monthly | Free | Yes | Subscribe now | Dense, pattern-oriented essays with production numbers; ideal for AI system design. |
| [Decoding AI](https://www.decodingai.com/) :gem: | Paul Iusztin | End-to-end LLM/agent engineering, LLMOps | Weekly | Free / paid | Yes | Subscribe now | Code-first series (agents, RAG, observability) at exactly your build level. |
| [Interconnects](https://www.interconnects.ai/) | Nathan Lambert | Post-training, RLHF/RLVR, open models | ~Weekly | Free / paid | Yes | Skim | Best insider view of post-training (author of the RLHF book); read for fine-tuning weeks. |
| [Ahead of AI](https://magazine.sebastianraschka.com/) | Sebastian Raschka | LLM research explained, architectures, reasoning models | ~Monthly | Free / paid | Yes | Skim | Visual, careful paper walkthroughs; great for Phase 5 depth. |
| [Import AI](https://importai.substack.com/) | Jack Clark | Research + policy, weekly paper roundup | Weekly | Free | Yes | Skim | Long-running, well-chosen paper picks with policy context. |
| [Lil'Log](https://lilianweng.github.io/) :gem: | Lilian Weng | Deep technical surveys (agents, hallucination, reward hacking) | Rare (a few per year) | Free | Yes | Subscribe now | Each post is a mini textbook chapter; "LLM Powered Autonomous Agents" is still the best agent primer. |
| [Chip Huyen](https://huyenchip.com/blog/) | Chip Huyen | AI engineering, agents, ML systems | Rare | Free | Yes | Skim | Author of *AI Engineering*; essays are book-quality. |
| [Jason Liu](https://jxnl.co/writing/) :gem: | Jason Liu | RAG, structured outputs, consulting lessons | Irregular | Free | Yes | Optional | Pragmatic RAG improvement playbooks ("RAG is more than embeddings"); creator of Instructor. |
| [Philipp Schmid](https://www.philschmid.de/) :gem: | Philipp Schmid | Agents, context engineering, Gemini/HF tooling | ~Monthly | Free | Yes | Optional | Short, runnable guides; good on context engineering and agent patterns. |
| [The Batch](https://www.deeplearning.ai/the-batch/) | Andrew Ng / DeepLearning.AI | Weekly AI news + Andrew's letter | Weekly | Free | No | Skim | Calm, curated weekly; the letter is often a useful product/strategy lens. |
| [TLDR AI](https://tldr.tech/ai) | TLDR | Links digest | Daily (weekdays) | Free | Yes | Skim | Fast headline scan; already in the feed, cap at 2 items/day. |
| [Ben's Bites](https://www.bensbites.com/) | Ben Tossell | AI product/tools news | ~Daily/weekly | Free / paid | Yes | Optional | Product-builder lens; good for spotting agent-product patterns. |
| [Language Models & Co.](https://newsletter.languagemodels.co/) :gem: | Jay Alammar | Visual explainers of LLM internals | **Dormant** (last issue Nov 2025) | Free | Yes | Optional | From the author of "The Illustrated Transformer"; visuals that stick. |
| [The Kaitchup](https://kaitchup.substack.com/) :gem: | Benjamin Marie | Fine-tuning, quantization, local LLMs, hands-on notebooks | Weekly | Free / paid | Yes | Optional | Most practical source for LoRA/QLoRA/quantization experiments (Phase 5). |
| [One Useful Thing](https://www.oneusefulthing.org/) | Ethan Mollick | How AI changes work and organisations | ~Weekly | Free | Yes | Optional | Good for Staff-level "AI adoption in the org" conversations. |
| [Gradient Flow](https://gradientflow.com/) | Ben Lorica | Data + AI infrastructure trends, enterprise adoption | ~Weekly | Free | Yes | Optional | Enterprise-architecture angle on AI platforms. |

## System design, distributed systems & architecture

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [Marc Brooker's blog](https://brooker.co.za/blog/) :gem: | Marc Brooker (AWS) | Distributed systems, databases, tail latency, formal methods | ~Monthly | Free | Yes | Subscribe now | Short, deep, numerate essays from the engineer behind Lambda/Aurora DSQL work. |
| [ByteByteGo](https://blog.bytebytego.com/) | Alex Xu et al. | Visual system-design explainers | Weekly | Free / paid | Yes | Skim | Great diagrams for revision; paid deep-dives are hit-and-miss for a senior. |
| [System Design Newsletter](https://newsletter.systemdesign.one/) | Neo Kim | Real-world case studies ("how X scaled Y") | Weekly | Free / paid | Yes | Skim | Short case studies with links to primary engineering posts. |
| [Quastor](https://www.quastor.org/) | Arpan / Quastor | Summaries of big-tech engineering blog posts | ~2x/week | Free / paid | No | Optional | Good discovery engine for engineering-blog posts; then read the original. |
| [Byte-Sized Design](https://bytesizeddesign.substack.com/) :gem: | Byte-Sized Design | Concise case studies of production architectures | Weekly | Free / paid | Yes | Optional | Fast reads that connect incidents/case studies to patterns. |
| [Architecture Notes](https://architecturenotes.co/) | Mahdi Yusuf | Illustrated deep-dives (Redis, Kafka, databases) | **Near-dormant** (last issue Mar 2026) | Free | Yes | Optional | Back catalogue is excellent and visual; don't expect new issues. |
| [Metadata](https://muratbuffalo.blogspot.com/) :gem: | Murat Demirbas | Distributed-systems paper reviews | ~Weekly | Free | Yes | Skim | A professor reading the papers you should read — ideal companion to [papers](papers.md). |
| [Phil Eaton's notes](https://notes.eatonphil.com/) :gem: | Phil Eaton | Databases, storage engines, consensus implementations | ~Monthly | Free | Yes | Optional | Builds things from scratch (Raft, MVCC) and explains them clearly. |
| [InfoQ](https://www.infoq.com/) | InfoQ editors | Architecture, Java, AI news + QCon talks | Daily | Free | Yes | Skim | Best single source for enterprise-architecture news and QCon talk writeups. |
| [martinfowler.com](https://martinfowler.com/) | Martin Fowler + guests | Architecture patterns, refactoring, GenAI patterns | ~Weekly | Free | Yes | Skim | Hosts the "Patterns of Distributed Systems" and GenAI pattern series. |
| [The Architect Elevator](https://architectelevator.com/blog/) :gem: | Gregor Hohpe | Enterprise architecture, architect's role, cloud strategy | Irregular | Free | Yes | Optional | Exactly the Staff/Principal "ride the elevator from engine room to penthouse" skill. |

## Career, Staff+ & engineering leadership

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/) | Gergely Orosz | Big-tech engineering culture, market, deep-dives | 2x/week | Free / paid | Yes | Subscribe now | The best source on how top companies actually run engineering; paid tier worth it for a Staff move. |
| [Irrational Exuberance](https://lethain.com/) | Will Larson | Staff engineering, eng strategy, architecture decisions | ~Weekly | Free | Yes | Subscribe now | Author of *Staff Engineer* and *Crafting Engineering Strategy*; the Staff playbook. |
| [Refactoring](https://refactoring.fm/) | Luca Rossi | Engineering management/process, research-backed | Weekly | Free / paid | Yes | Skim | Structured, practical takes on team effectiveness. |
| [Engineering Leadership](https://newsletter.eng-leadership.com/) | Gregor Ojstersek | Leadership, promotion, influence | Weekly | Free / paid | Yes | Skim | Concrete leadership advice with guest posts from Staff+ ICs and managers. |
| [High Growth Engineer](https://read.highgrowthengineer.com/) | Jordan Cutler | Senior → Staff career growth | Weekly | Free / paid | Yes | Skim | Actionable career tactics (visibility, scoping, communication). |
| [Pointer](https://www.pointer.io/) :gem: | Suraj Kolluri et al. | Curated essays for engineering leaders | 2x/week | Free | No | Optional | Hand-picked long-form essays; good Sunday queue source. |
| [No Idea Blog](https://noidea.dog/) :gem: | Tanya Reilly | Staff engineering, glue work, technical leadership | Rare | Free | No | Optional | Author of *The Staff Engineer's Path*; the "Being Glue" talk/essay is required reading. |
| [The Beautiful Mess](https://cutlefish.substack.com/) :gem: | John Cutler | Product/engineering operating models | Weekly | Free / paid | Yes | Optional | Sharp thinking about org design and how work flows — useful for L4 questions. |
| [Elevate](https://addyo.substack.com/) | Addy Osmani | Engineering leadership, AI-assisted development | ~Weekly | Free | Yes | Optional | Pragmatic takes on AI coding workflows at scale from a Google leader. |

## Python

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [Python Weekly](https://www.pythonweekly.com/) | Rahul Chaudhary | Links: articles, projects, releases | Weekly | Free | No | Skim | Broad weekly roundup; skim headlines only. |
| [PyCoder's Weekly](https://pycoders.com/) | Real Python team | Curated Python articles & projects | Weekly | Free | No | Subscribe now | Better-curated than most; one issue replaces a week of Reddit. |
| [Real Python](https://realpython.com/) | Real Python | Tutorials, podcast | Several/week | Free / paid | Yes | Optional | Mostly intermediate; useful for new-feature explainers (3.14, free-threading). |
| [Python⇒Speed](https://pythonspeed.com/) :gem: | Itamar Turner-Trauring | Performance, memory, Docker packaging for Python | ~Monthly | Free | Yes | Skim | Best source on Python performance and container builds for data/ML apps. |
| [Confessions of a Code Addict](https://blog.codingconfessions.com/) :gem: | Abhinav Upadhyay | CPython internals, systems performance | ~Monthly | Free / paid | Yes | Skim | Deep internals explained with rare clarity (GIL, bytecode, memory). |
| [Hynek Schlawack](https://hynek.me/articles/) :gem: | Hynek Schlawack | Packaging, testing, API design, attrs | Rare (~yearly) | Free | Yes | Optional | Opinionated, senior-level Python craftsmanship. |

## Java & Spring

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [Baeldung Java Weekly](https://www.baeldung.com/category/weekly-review) | Eugen Paraschiv | Java/Spring weekly review | Weekly | Free | Yes | Subscribe now | The one Java roundup to keep; in the feed. |
| [Inside Java](https://inside.java/) | Oracle Java team | JDK features, JEPs, newscasts | Several/week | Free | Yes | Skim | Primary source for Java 25+ features. |
| [This Week in Spring](https://spring.io/blog) | Josh Long | Spring ecosystem incl. Spring AI | Weekly | Free | Yes | Skim | Tracks Spring Boot 4.x / Spring AI 2.x releases. |
| [JVM Weekly](https://www.jvm-weekly.com/) :gem: | Artur Skowroński | JVM ecosystem analysis | Weekly | Free / paid | Yes | Optional | Commentary, not just links; good context for JDK roadmap. |
| [Java Annotated Monthly](https://blog.jetbrains.com/idea/tag/java-annotated/) | JetBrains | Monthly Java/Kotlin roundup | Monthly | Free | Yes | Optional | Low-volume catch-up if you skip weeklies. |

## News digests & discovery

| Newsletter | Author | Focus | Cadence | Cost | RSS | Priority | Why |
|---|---|---|---|---|---|---|---|
| [Hacker Newsletter](https://hackernewsletter.com/) | Kale Davis | Weekly best-of Hacker News | Weekly | Free | No | Optional | Replaces daily HN; the feed already pulls `hnrss.org/best` (capped). |
| [TLDR](https://tldr.tech/) | TLDR | Tech news digest | Daily | Free | Yes | Optional | Only if you want general tech news; TLDR AI is usually enough. |
| [Console](https://console.dev/) :gem: | David Mytton | Reviewed developer tools | Weekly | Free | Yes | Optional | Hand-reviewed dev tools; low noise. |
| [Changelog News](https://changelog.com/news) | The Changelog | Open-source/software news | Weekly | Free | Yes | Optional | Good OSS pulse with podcast companion. |

## Minimal starting set (week 0)

Subscribe to these 10 now and nothing else until week 4: Simon Willison, Latent Space, Hamel Husain, Eugene Yan, Decoding AI, Lil'Log,
Marc Brooker, The Pragmatic Engineer, Irrational Exuberance (lethain), PyCoder's Weekly — plus Baeldung Java Weekly via the feed.
