---
title: Engineering blogs
tags: [reading, engineering-blogs, case-studies]
last_reviewed: 2026-09-25
---

# Engineering blogs

Primary sources beat summaries: when a system-design topic comes up, read the company's own post, then compare with the textbook
answer. Where a **standout post is linked, it was opened and verified (September 2026)**. Where only "look for" topics are listed,
the blog root is verified but I did not verify a specific post URL, so search the blog by the given keywords rather than trusting a guessed link.
Some sites (Medium, Netflix, DoorDash, OpenAI) block automated checkers, so root links there were not machine-verified but are their well-known official addresses.

!!! tip "How to use"
    For each post ask: *what was the load, what broke, what was the trade-off, what did they NOT do?* Add one row to your case-study notes under `docs/tracks/system-design/case-studies/`.

## AI labs & AI-native companies

| Blog | Standout posts / what to look for |
|---|---|
| [Anthropic Engineering](https://www.anthropic.com/engineering) | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) · [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) · [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| [OpenAI](https://openai.com/news/engineering/) | Look for engineering write-ups on scaling Postgres/ChatGPT infrastructure and Agents SDK/Responses API design; use the [news feed](https://openai.com/news/rss.xml) already in the daily feed. |
| [Hugging Face Blog](https://huggingface.co/blog) | [Mixture of Experts Explained](https://huggingface.co/blog/moe) · [Illustrating RLHF](https://huggingface.co/blog/rlhf) — clear explainers plus TRL/inference-engine posts. |
| [Vercel](https://vercel.com/blog) | [How we built AEO tracking for coding agents](https://vercel.com/blog/how-we-built-aeo-tracking-for-coding-agents) (a real agent-system build); also look for AI SDK and Fluid compute posts. |
| [Notion Tech](https://www.notion.com/blog/topic/tech) | [Herding elephants: sharding Postgres at Notion](https://www.notion.com/blog/sharding-postgres-at-notion) — a model migration write-up (shard key, dual writes, cutover). |

## Consumer-scale platforms

| Blog | Standout posts / what to look for |
|---|---|
| [Discord Engineering](https://discord.com/category/engineering) | [How Discord Stores Trillions of Messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) — Cassandra → ScyllaDB, hot partitions, request coalescing. Also look for their Elixir/Rust scale posts. |
| [Netflix TechBlog](https://netflixtechblog.com/) | Look for: chaos engineering, Zuul/edge gateway, Cosmos/media pipelines, and data-platform posts (search the blog by these keywords). |
| [Uber Engineering](https://www.uber.com/blog/engineering/) | Look for: Schemaless/Docstore, Ringpop, Cadence/Temporal-lineage workflows, and Michelangelo ML platform posts. |
| [Airbnb Engineering](https://medium.com/airbnb-engineering) | Look for: service-oriented migration, search ranking, and Minerva metrics-platform posts. |
| [Pinterest Engineering](https://medium.com/pinterest-engineering) | Look for: sharded MySQL/HBase evolution, Pinot-based analytics and ML serving posts. |
| [Spotify Engineering](https://engineering.atspotify.com/) | Look for: Backstage, squad/platform model, and ML platform posts. |
| [Grab Tech](https://engineering.grab.com/) | Look for: super-app platform, feature-store/ML and data-lake posts; good for emerging-market scale constraints. |
| [Zalando Engineering](https://engineering.zalando.com/) | [Micro Frontends: from Fragments to Renderers](https://engineering.zalando.com/posts/2021/03/micro-frontends-part1.html) · also look for their API guidelines and event-driven architecture posts. |
| [Canva Engineering](https://www.canva.dev/blog/engineering/) | Look for: design-system, GraphQL and infrastructure-cost posts. |
| [DoorDash Engineering](https://careersatdoordash.com/engineering-blog/) | Look for: dispatch/ML, event-processing platform (Kafka/Flink) and microservices-migration posts; strong logistics relevance. |

## Infrastructure, payments & developer platforms

| Blog | Standout posts / what to look for |
|---|---|
| [Stripe Engineering](https://stripe.com/blog/engineering) | [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) · [Online migrations at scale](https://stripe.com/blog/online-migrations). |
| [Cloudflare Blog](https://blog.cloudflare.com/) | [How we built Pingora](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/) · [Details of the July 2, 2019 outage](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/) · [Bad software deploy outage](https://blog.cloudflare.com/cloudflare-outage/) — outstanding postmortems. |
| [Figma Engineering](https://www.figma.com/blog/engineering/) | [How Figma's multiplayer technology works](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) — CRDT-inspired collaboration design. Also look for their Postgres scaling series. |
| [Shopify Engineering](https://shopify.engineering/) | [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) — modular monolith; also look for flash-sale/BFCM scale posts. |
| [Meta Engineering](https://engineering.fb.com/) | [More details about the October 4 outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) — BGP/DNS outage postmortem; also look for RocksDB, TAO and Llama infra posts. |
| [Slack Engineering](https://slack.engineering/) | [Flannel: An Application-Level Edge Cache to Make Slack Scale](https://slack.engineering/flannel-an-application-level-edge-cache-to-make-slack-scale/) — lazy loading and edge caching for large workspaces. |
| [Dropbox Tech](https://dropbox.tech/) | [Inside the Magic Pocket](https://dropbox.tech/infrastructure/inside-the-magic-pocket) — exabyte-scale storage built after leaving S3. |
| [LinkedIn Engineering](https://www.linkedin.com/blog/engineering) | Look for: Kafka origins, Venice/Espresso data infra and ranking/LLM platform posts; Jay Kreps' [The Log](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) is the classic. |
| [GitHub Engineering](https://github.blog/engineering/) | Look for: MySQL scaling, Git infrastructure, and availability-report postmortems. |
| [Datadog Engineering](https://www.datadoghq.com/blog/engineering/) | Look for: Husky/Monocle time-series and event-store internals; strong on observability at scale. |
| [AWS Builders' Library](https://aws.amazon.com/builders-library/) :gem: | [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — the highest signal-to-noise cloud engineering writing. |
| [Google Research Blog](https://research.google/blog/) | Systems and ML research explained by the authors; pair with [papers](papers.md). |

## Maersk / logistics

There is no dedicated Maersk engineering blog that I could verify. What exists: the open-source org [MaerskTech on GitHub](https://github.com/MaerskTech),
the [Maersk Innovation Center](https://innovation.maersk.com/), and technology articles under
[Logistics Insights](https://www.maersk.com/insights/tags/software-engineering). Internal engineering knowledge lives on internal sites, not here.

## Feeds worth wiring

Only some of these are in `data/feeds.yml` (mostly AI/architecture sources). If you want a system-design firehose, the weekly agent can propose adding
Cloudflare, Stripe and Netflix feeds after their RSS URLs are verified; avoid adding more than 2 per week.
