---
title: Papers
tags: [reading, papers]
last_reviewed: 2026-09-25
---

# Papers

Read papers with the **three-pass method**: (1) abstract + figures + conclusion (10 min), (2) skim the design and evaluation sections
(30 min), (3) only for the 5–6 papers that matter for your capstone, read fully and re-derive a key diagram.
Difficulty: **E** accessible · **M** needs distributed-systems or ML background · **H** dense / math-heavy.
"Explainer" links were opened and verified as of September 2026; `-` means no explainer I could verify.

!!! tip "Pair papers with a lab"
    Raft paper + [Raft visualisation](https://thesecretlivesofdata.com/raft/) + [Gossip Glomers](https://fly.io/dist-sys/) is one weekend.
    RAG paper + your hybrid-search pipeline is another. A paper you didn't implement or diagram is a paper you'll forget.

## Distributed systems

| Paper | Why read it | Diff. | Explainer |
|---|---|---|---|
| [Dynamo: Amazon's Highly Available Key-value Store](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) (SOSP 2007) | Consistent hashing, sloppy quorums, vector clocks, hinted handoff, anti-entropy — the vocabulary of every leaderless store (Cassandra, Riak, DynamoDB lineage). Interview staple. | M | [Murat Demirbas' blog](https://muratbuffalo.blogspot.com/) has reviews of most classics (search by title) |
| [Bigtable](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/) (OSDI 2006) | SSTables, memtable, tablets, and the LSM design that HBase/Cassandra/RocksDB inherit. | M | - |
| [The Google File System](https://research.google/pubs/the-google-file-system/) (SOSP 2003) | Design for failure as the norm: single master, chunk leases, relaxed consistency for append-heavy workloads. | E | - |
| [MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) (OSDI 2004) | The programming model behind batch processing; useful to explain why Spark/Flink evolved. | E | - |
| [Spanner](https://research.google/pubs/spanner-googles-globally-distributed-database-2/) (OSDI 2012) | TrueTime, external consistency, Paxos groups + 2PC; the "you can have strong consistency at global scale" paper. | H | [Marc Brooker on Aurora DSQL](https://brooker.co.za/blog/2024/12/03/aurora-dsql.html) — a modern take on the same design space |
| [In Search of an Understandable Consensus Algorithm (Raft)](https://raft.github.io/raft.pdf) (USENIX ATC 2014) | Designed to be understood: leader election, log replication, safety, membership change. Must implement once (MIT 6.5840 Lab 3). | M | [The Secret Lives of Data: Raft](https://thesecretlivesofdata.com/raft/) and the [Raft site](https://raft.github.io/) |
| [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) (Lamport, 2001) | Short but subtle; read after Raft to see what Raft simplifies (single-decree Paxos, then Multi-Paxos). | H | - |
| [Kafka: a Distributed Messaging System for Log Processing](https://notes.stephenholiday.com/Kafka.pdf) (NetDB 2011; PDF mirror) | Partitioned commit log, consumer offsets, sequential I/O and zero-copy — why Kafka is fast and simple. | E | Jay Kreps' [The Log](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) |
| [Amazon Aurora: Design Considerations for High Throughput Cloud-Native Relational Databases](https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases) (SIGMOD 2017) | "The log is the database": pushing redo processing into the storage tier; quorum I/O; less network amplification. | M | - |
| [The Chubby Lock Service](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/) (OSDI 2006) | Coarse-grained locks, leases and sessions as a service; the ancestor of ZooKeeper/etcd usage patterns. Read with Kleppmann's [distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) essay. | M | Kleppmann essay (above) |
| [Zanzibar: Google's Consistent, Global Authorization System](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/) (USENIX ATC 2019) | Relationship-based access control at billions of ACLs; the "zookie" consistency token. Basis for SpiceDB/OpenFGA and highly relevant to agent authorization. | M | - |
| [FoundationDB: A Distributed Unbundled Transactional Key Value Store](https://www.foundationdb.org/files/fdb-paper.pdf) (SIGMOD 2021) | Deterministic simulation testing plus a layered, unbundled design; the best modern paper on how to *test* distributed systems. | H | - |
| [Large-scale cluster management at Google with Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) (EuroSys 2015) | Scheduling, priorities, and resource isolation; roots of Kubernetes. | M | - |
| [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/) (CACM 2013) | Latency percentiles at fan-out; hedged requests. Also listed in [articles](articles.md). | E | - |

## AI: foundations & alignment

| Paper | Why read it | Diff. | Explainer |
|---|---|---|---|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017) | The transformer. Read after watching the visual explainers; know self-attention, multi-head, positional encodings. | M | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/); 3Blue1Brown [Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M) and [Attention](https://www.youtube.com/watch?v=eMlx5fFNoYc) |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) (2022) | Origin of "think step by step" and the seed of reasoning models; short and readable. | E | - |
| [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) (2022) | The RLHF recipe (SFT → reward model → PPO) that produced ChatGPT. | M | [Illustrating RLHF (Hugging Face)](https://huggingface.co/blog/rlhf); [Chip Huyen on RLHF](https://huyenchip.com/2023/05/02/rlhf.html) |
| [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (2022) | RLAIF: self-critique against written principles; the basis for scalable oversight and judge-model thinking. | M | - |
| [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290) (2023) | Replaces the RL loop with a classification-style loss on preference pairs; the default open-model alignment method. | H | [Umar Jamil on YouTube](https://www.youtube.com/@umarjamilai) (channel; search DPO) |
| [DeepSeekMath (introduces GRPO)](https://arxiv.org/abs/2402.03300) (2024) | Where GRPO first appears — the RL method behind "reasoning" fine-tuning without a value model. | H | - |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) (2025) | RL with verifiable rewards producing reasoning behaviour; why RLVR became mainstream in 2025–26. | H | [Interconnects](https://www.interconnects.ai/) coverage (newsletter; search R1) |
| [Llama 2](https://arxiv.org/abs/2307.09288) (2023) | Very detailed open recipe (pre-training, SFT, RLHF, safety). Good reference for what a full post-training pipeline involves. | M | - |

## AI: retrieval, agents & context

| Paper | Why read it | Diff. | Explainer |
|---|---|---|---|
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020) | Names and formalises RAG (parametric + non-parametric memory). Modern RAG differs a lot; read for the framing. | M | [Pinecone rerankers series](https://www.pinecone.io/learn/series/rag/rerankers/) for the modern pipeline |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (2022) | The thought → action → observation loop that underlies most agent frameworks. | E | [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) |
| [Toolformer](https://arxiv.org/abs/2302.04761) (2023) | Self-supervised tool-use learning; historical root of function calling. | M | - |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (2023) | Verbal self-reflection as memory across trials; basis for evaluator-optimizer loops. | M | Lilian Weng agents post (above) |
| [Self-RAG](https://arxiv.org/abs/2310.11511) (2023) | Learned retrieval decisions and self-critique tokens; a precursor of "agentic RAG". | M | - |
| [Is Agentic RAG worth it?](https://arxiv.org/abs/2601.07711) (2026) | Experimental comparison showing agentic RAG isn't always better than well-tuned classic pipelines — supports the [radar](../trends/radar.md) hold entry. | M | - |
| [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) (Microsoft GraphRAG, 2024) | Graph-based indexing for corpus-level "global" questions where vector search fails. | M | [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) and [GraphRAG project](https://www.microsoft.com/en-us/research/project/graphrag/) |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) (2023) | Position bias in long contexts; classic evidence for why retrieval quality and ordering matter. | E | [Chroma: Context Rot](https://research.trychroma.com/context-rot) for the updated picture |
| [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) (2023) | Programming, not prompting: signatures, modules, optimizers. | M | [dspy.ai](https://dspy.ai/) docs |
| [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) (2025) | Prompt optimisation by reflecting on trajectories, beating GRPO with far fewer rollouts; ships as `dspy.GEPA`. | M | [HF DSPy + GEPA cookbook](https://huggingface.co/learn/cookbook/dspy_gepa) |
| [Agentic Context Engineering (ACE)](https://arxiv.org/abs/2510.04618) (2025) | Evolving playbooks as contexts that accumulate and refine strategies — a research view of context engineering. | M | Anthropic's [context engineering post](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |

## AI: efficient training & inference

| Paper | Why read it | Diff. | Explainer |
|---|---|---|---|
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (2021) | Parameter-efficient fine-tuning via low-rank updates; the base of nearly all adapter work. | M | [Umar Jamil](https://www.youtube.com/@umarjamilai) (channel; search LoRA) |
| [QLoRA](https://arxiv.org/abs/2305.14314) (2023) | 4-bit NF4 base + LoRA adapters: fine-tune large models on one GPU. Pair with a TRL/Unsloth lab. | M | - |
| [Efficient Memory Management for LLM Serving with PagedAttention (vLLM)](https://arxiv.org/abs/2309.06180) (SOSP 2023) | OS-style paging for KV cache; explains continuous batching throughput and why memory, not FLOPs, limits serving. | M | [vLLM blog post](https://blog.vllm.ai/2023/06/20/vllm.html) |
| [FlashAttention](https://arxiv.org/abs/2205.14135) (2022) | IO-aware exact attention (tiling, recomputation) — a lesson in memory-hierarchy-aware algorithm design. See also [FlashAttention-2](https://arxiv.org/abs/2307.08691). | H | - |
| [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) (2022) | Draft-and-verify decoding gives lossless speed-ups; now a standard serving feature. | M | - |
| [Outrageously Large Neural Networks: Sparsely-Gated Mixture-of-Experts](https://arxiv.org/abs/1701.06538) (2017) | The MoE layer; explains why frontier models have huge total but small active parameter counts. | H | [Mixture of Experts Explained (Hugging Face)](https://huggingface.co/blog/moe); [Maarten Grootendorst visual guide](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) |
| [WebGPT](https://arxiv.org/abs/2112.09332) (2021) | Early browser-using agent trained with human feedback; historical context for search agents. | M | - |

## Suggested reading order (with the roadmap)

1. **P1 (wk 1–4):** Dynamo, GFS, Kafka, Raft (with visualisation), Tail at Scale.
2. **P2 (wk 5–8):** RAG (Lewis), Lost in the Middle, Self-RAG (skim), Is Agentic RAG worth it?, LLM-judge papers via [articles](articles.md).
3. **P3 (wk 9–12):** ReAct, Reflexion, Toolformer (skim), DSPy, GEPA, ACE.
4. **P4 (wk 13–16):** Aurora, Zanzibar, Chubby, Spanner.
5. **P5 (wk 17–20):** Paxos Made Simple, FoundationDB, PagedAttention, FlashAttention, speculative decoding, LoRA/QLoRA, DPO, GRPO/R1, MoE.
6. **P6 (wk 21–24):** revisit Dynamo/Spanner/Raft trade-offs for interviews; re-read your own notes.
