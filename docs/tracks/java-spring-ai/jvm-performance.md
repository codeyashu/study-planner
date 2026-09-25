---
title: "JVM performance, GC & Leyden/AOT"
track: java-spring-ai
slug: jvm-performance
priority: P2
complexity: 4
est_hours: 3
phase: 5
tags: [java-spring-ai, P2]
last_reviewed: 2026-09-25
---

# JVM performance, GC & Leyden/AOT

!!! abstract "At a glance"
    **Priority:** P2 · **Complexity:** 4/5 · **Est. time:** 3 h · **Phase:** 5 · **Prereqs:** [Virtual threads & structured concurrency](virtual-threads-structured-concurrency.md), [Spring Boot 4](spring-boot-4.md)
    **You're done when:** you can choose a GC and container memory settings for an AI service from data (JFR/GC logs), cut startup time with an AOT cache, and explain when native image, CRaC-style snapshots or "just add pods" is the right lever.

## Why it matters

AI services have unusual JVM profiles: **many long-lived streaming connections**, bursts of large JSON payloads and embedding batches, ONNX/native buffers off-heap, and a heavy tail of I/O waits — while the "real" latency is the model's. So JVM tuning is rarely about shaving milliseconds off the LLM path; it's about **density (cost per pod), predictable tail latency under GC, fast startup for autoscaling/serverless, and not getting OOM-killed in a container**. As a Staff engineer you should be able to say what to measure, which two or three flags matter on JDK 25, and when tuning is the wrong answer.

## Core concepts

### Measure first

| Question | Tool |
|---|---|
| Where is CPU time going? | JFR (`-XX:StartFlightRecording`), [async-profiler](https://github.com/async-profiler/async-profiler) flame graphs |
| GC pauses, allocation rate, promotion | GC logs `-Xlog:gc*:file=gc.log`, JFR GC events, Micrometer `jvm.gc.*` |
| Memory beyond heap | NMT `-XX:NativeMemoryTracking=summary`, `jcmd VM.native_memory` |
| Virtual thread pinning | JFR `jdk.VirtualThreadPinned` |
| Startup | `-Xlog:class+load`, Spring Boot startup actuator endpoint, `-Xlog:startuptime`-style timing |
| Real bottleneck? | Distributed traces — usually the model or DB, not the JVM |

### GC choice on JDK 25 (LTS)

| Collector | Flag | Characteristics | Pick when |
|---|---|---|---|
| **G1** (default) | `-XX:+UseG1GC` | Balanced throughput/pause (~tens–200 ms targets via `MaxGCPauseMillis`) | Default; most services; heaps ≤ ~16 GB |
| **ZGC (generational)** | `-XX:+UseZGC` | Sub-millisecond pauses, scales to TB heaps; generational mode is the only mode since JDK 24 | Tail-latency-sensitive, large heaps, high allocation rate |
| **Shenandoah** | `-XX:+UseShenandoahGC` | Low-pause concurrent compaction; generational mode is production-ready in JDK 25 (verify in your distribution's build) | Alternative low-pause option where offered |
| **Serial / Parallel** | `-XX:+UseSerialGC` / `-XX:+UseParallelGC` | Lowest overhead / max throughput | Tiny containers (< 2 CPUs or < 1.8 GB — JVM picks Serial automatically); batch jobs |

Rules of thumb: measure allocation rate and pause distribution before switching; G1 is fine for most AI backends. Choose ZGC when p99/p999 pause matters (interactive streaming with many concurrent sessions) or heap is large (semantic caches, in-memory indexes). Low-pause collectors trade some throughput/memory headroom.

### Container memory: the classic incident

`-Xmx` isn't the process footprint. RSS ≈ heap + metaspace + code cache + thread stacks + direct buffers (Netty/HTTP clients) + native libs (ONNX, Tika/PDF, compression) + GC structures.

```
-XX:MaxRAMPercentage=65        # heap as % of container limit; leave headroom for non-heap
-XX:+ExitOnOutOfMemoryError    # let the orchestrator restart, don't limp
-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/dumps
-XX:MaxDirectMemorySize=256m   # if Netty/direct buffers matter
```

Set memory *requests = limits* for predictable behaviour; watch `container_memory_working_set_bytes` vs `jvm.memory.used`. OOM-kills with a healthy heap almost always mean off-heap (direct buffers, native libs) or too-high `MaxRAMPercentage`.

Virtual threads: stacks live in the heap, so thousands of blocked streaming requests (each holding response buffers, conversation context) show up as **heap pressure**, not thread count.

### Compact object headers (JEP 519, product in JDK 25)

`-XX:+UseCompactObjectHeaders` shrinks object headers from 12 to 8 bytes on 64-bit. Real-world reports show notable heap and allocation reductions (often up to ~10–20% on object-heavy workloads) and some throughput gain. It's opt-in in 25 — try it in staging, compare GC logs/RSS, keep the flag if stable. Relevant to AI services holding many small objects (documents, chunks, JSON trees).

### Startup and warm-up: the Leyden/AOT cache

Project Leyden's AOT work landed incrementally: **JEP 483** (JDK 24, ahead-of-time class loading & linking), **JEP 514** (JDK 25, simpler AOT cache creation ergonomics), **JEP 515** (JDK 25, ahead-of-time method profiling so JIT warms faster). Practical workflow with Spring Boot (see the Boot reference on AOT cache support):

```bash
# 1. Training run: exercises typical startup + a few requests, writes the cache
java -XX:AOTCacheOutput=app.aot -jar app.jar     # stop the app after warm-up traffic

# 2. Production runs use the cache
java -XX:AOTCache=app.aot -jar app.jar
```

(Spring Boot recommends running from an extracted layout — `java -Djarmode=tools -jar app.jar extract` — for AOT cache use; check the reference for the exact recommended steps for your Boot 4.x.) The cache is tied to the exact JDK build, JAR contents and classpath, so **create it in the container build** in the same image that runs it. Typical effect on a Spring app: startup dropping by roughly a third to a half, with no code changes and no closed-world restrictions.

| Option | Startup | Peak perf | Constraints |
|---|---|---|---|
| Plain JVM | Slow-ish (seconds) | Best after warm-up (JIT) | None |
| **AOT cache (Leyden)** | Much faster | Same as JVM | Rebuild per JDK/app build |
| GraalVM native image | Fastest (tens of ms), small RSS | Lower peak throughput (no JIT unless PGO) | Closed world, reflection metadata, longer builds, some libraries problematic — verify Spring AI + your model SDKs |
| Snapshot/restore (CRaC-like) | Fast | JVM-level | Needs supporting JDK build and platform |

Decision: AI backends are typically long-running services where a 3–8 s startup is fine — reach for AOT cache when you autoscale aggressively or run scale-to-zero; consider native image for CLI tools/functions where cold-start dominates; don't pay native-image complexity for a service whose latency is 95% model wait.

### Throughput levers that matter for AI services

1. **Connection pooling and HTTP clients:** reuse clients; HTTP/2 to providers; tune timeouts (read timeouts of 30–120 s for long generations) and connection limits per provider.
2. **JSON:** Jackson 3 is fast; avoid re-serialising large prompts multiple times; stream large payloads; watch for building giant `String` prompts (allocation spikes).
3. **Streaming:** backpressure (`Flux` with bounded buffers); cancel upstream when clients disconnect to stop token spend.
4. **Batching embeddings** (windowed batches, bounded concurrency) — the biggest throughput win for ingestion.
5. **Caching:** response/semantic cache in front of the model; Caffeine for hot metadata; beware unbounded caches.
6. **CPU-bound local inference** (ONNX embeddings/rerankers): dedicated bounded pool, native memory accounting, or move to a model server (often Python).

### Java vs Python perf framing (for the polyglot decision)

Neither language is the bottleneck for LLM calls. Java wins on steady-state CPU-heavy glue work and concurrency density per pod (virtual threads, no GIL); Python wins on ecosystem for ML tooling and local inference. See [polyglot AI architecture](polyglot-ai-architecture.md).

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Spring Boot: efficient deployments](https://docs.spring.io/spring-boot/reference/packaging/efficient.html) | docs | Layered jars, extracted layout, container tips | intermediate | free |
| [Spring Boot: AOT cache](https://docs.spring.io/spring-boot/reference/packaging/aot-cache.html) | docs | The supported workflow for JDK AOT cache with Boot | intermediate | free |
| [Project Leyden](https://openjdk.org/projects/leyden/) | docs | Roadmap and rationale for AOT class loading/profiling | advanced | free |
| [JEP 483: AOT class loading & linking](https://openjdk.org/jeps/483) | docs | Foundation of the AOT cache | advanced | free |
| [JEP 515: AOT method profiling](https://openjdk.org/jeps/515) | docs | Why warm-up improves in JDK 25 | advanced | free |
| [JEP 519: Compact object headers](https://openjdk.org/jeps/519) | docs | Memory footprint gains and caveats | advanced | free |
| [async-profiler](https://github.com/async-profiler/async-profiler) :gem: | code | Low-overhead flame graphs incl. allocation and lock profiling | advanced | free |
| [Aleksey Shipilev](https://shipilev.net/) :gem: | article | Deep, honest JVM performance and GC writing (Shenandoah author) | advanced | free |
| [javaalmanac.io](https://javaalmanac.io/) :gem: | interactive | Check which JDK version introduced a flag/feature | intermediate | free |
| [inside.java](https://inside.java/) | article | JDK team posts on GC and Leyden updates | advanced | free |

## Hands-on lab

**Goal (2 h):** profile and tune the Spring AI RAG/MCP service under load.

1. Containerise the service (Temurin/OpenJDK 25) with memory limit 1 GiB, `-XX:MaxRAMPercentage=65`, GC logging and JFR on.
2. Load test `/ask` (mock the model with a 1.5 s sleep, or use a local model) at 300 concurrent for 5 min. Record p50/p99, RSS, GC pause p99, CPU.
3. Compare G1 vs `-XX:+UseZGC` on identical load; add `-XX:+UseCompactObjectHeaders`; tabulate.
4. Build an AOT cache in the Dockerfile (training run with 20 warm-up requests). Measure time-to-ready (Actuator health) before/after; note cache size and rebuild triggers.
5. Provoke an off-heap problem: increase `MaxRAMPercentage` to 90 and stream large responses; observe OOMKill vs heap headroom; fix using NMT to explain RSS.
6. Capture a flame graph (async-profiler) of ingestion and identify the top three frames (often JSON, tokenisation, Tika).

**Expected output:** a comparison table (GC × flags → p99, RSS, pause), startup time before/after AOT, and one flame graph with a written finding.

## Questions

### L1 — Recall

??? question "Q1. Which GC is the JDK 25 default and when do you pick ZGC instead?"
    ??? success "Answer"
        G1 is the default (except JVM ergonomics pick Serial on very small containers). Choose ZGC (generational, sub-millisecond pauses, scales to huge heaps) when tail-latency pauses or large heaps matter and G1 pauses show up in your p99/p999 data.

??? question "Q2. What is the Leyden AOT cache and what constrains it?"
    ??? success "Answer"
        A JDK-generated archive (`-XX:AOTCache`, produced via a training run with `-XX:AOTCacheOutput`) storing pre-loaded/linked classes (JEP 483), with JDK 25 adding method profiling (JEP 515) and simpler creation (JEP 514). It speeds startup/warm-up without a closed-world restriction, but is tied to the exact JDK, JAR and classpath, so it must be built with the deployed artefact.

??? question "Q3. Why can a container be OOMKilled while the Java heap looks healthy?"
    ??? success "Answer"
        RSS includes non-heap memory: metaspace, code cache, thread stacks, direct/native buffers (Netty, compression, ONNX, PDF libraries) and GC overhead. If `MaxRAMPercentage`/`-Xmx` leaves too little headroom or native usage grows, the kernel kills the process. Diagnose with NMT and container working-set metrics.

### L2 — Apply

??? question "Q4. A 2 GiB pod OOMKills weekly; heap is capped at 1.5 GiB. What do you change and check?"
    ??? success "Answer"
        Reduce heap to ~60–65% (`MaxRAMPercentage`), enable NMT (`summary`) and compare against RSS to find the growth (direct buffers, metaspace leaks, native libs), cap direct memory if relevant, add `ExitOnOutOfMemoryError` and heap dump. Check for unbounded caches or large in-flight payloads under streaming. If the workload genuinely needs more, raise the limit rather than the heap ratio.

??? question "Q5. Startup is 9 s and your HPA scales in bursts. Options ranked?"
    ??? success "Answer"
        (1) Remove startup work (lazy init, trim classpath/auto-config, avoid heavy `@PostConstruct` and eager pool creation) — cheapest. (2) AOT cache in the image build (~30–50% faster, no code change). (3) Keep spare capacity/pre-scale on predictable load and tune readiness so pods take traffic only when warm. (4) Native image or snapshot/restore for scale-to-zero or functions. Measure each in staging; choose the first that meets the scale-out SLO.

??? question "Q6. p99 latency spikes coincide with G1 mixed collections on a 12 GiB heap with high allocation from JSON. Approach?"
    ??? success "Answer"
        Confirm via GC logs/JFR (pause and allocation rate). First reduce allocation (avoid intermediate strings/trees, stream, reuse buffers). Then try ZGC (or tune `MaxGCPauseMillis`/region size for G1) and compare p99 and CPU/RSS trade-offs under the same load. Also check whether the spikes are GC at all (thread dumps/JFR) — LLM/provider tail latency often explains "spikes".

### L3 — Design & trade-offs

??? question "Q7. Native image vs JVM+AOT cache for a fleet of AI tool microservices — decide."
    ??? success "Answer"
        JVM + AOT cache by default: near-native startup gains, unchanged JIT peak performance, full library compatibility, simpler debugging/profiling and no reflection-config burden. Native image where cold start and RSS dominate (functions, scale-to-zero, sidecars, CLIs) and dependencies are proven to work under GraalVM. Because these services spend most time waiting on I/O, peak CPU differences rarely matter; operational simplicity usually wins. Prototype the one riskiest service (largest dependency set) before committing.

??? question "Q8. Is it worth tuning the JVM for an AI service whose latency is 95% LLM wait?"
    ??? success "Answer"
        Tune for **cost and reliability**, not latency: right-size memory (no OOMKill), pick a GC that keeps pods dense, ensure virtual threads/pools don't overload dependencies, cut startup for autoscaling. Skip micro-tuning of the request path; larger wins are model choice, caching, prompt size, batching and parallelism. Show this with a latency breakdown from traces before spending time.

??? question "Q9. Where should CPU-heavy local inference (embeddings/reranker) run?"
    ??? success "Answer"
        In a dedicated model server (often Python/vLLM/Triton/ONNX Runtime service) scaled independently on GPU/CPU nodes, called from Java via HTTP/gRPC. In-JVM ONNX is acceptable for small models and low volume but complicates memory (native), GC and pod sizing, and couples scaling of API and inference. Decide on volume, latency budget, and who owns the model lifecycle.

### L4 — Staff-level ambiguity

??? question "Q10. Finance says AI platform cloud cost grew 3x. Where do you look on the JVM side and what do you propose?"
    ??? success "Answer"
        Break down cost by component first (model tokens usually dominate; JVM/pods second). On the JVM side: pod density (memory requests vs actual, `MaxRAMPercentage`), idle over-provisioning due to slow startup (AOT cache enabling tighter autoscaling), GC/CPU waste, compact object headers, right-sized thread/connection pools, and consolidating low-traffic tool services. Then quantify: cost per 1k requests before/after per change, prioritise by savings/effort, and put the metrics on a dashboard owned by the platform team. Push back on tuning work that saves 2% of pod cost while token spend is 80% of the bill.

??? question "Q11. The org standardises on one JVM runtime image. What decisions and guardrails go into it?"
    ??? success "Answer"
        Vendor/distribution and support policy (LTS-only, JDK 25), base image (distroless/slim, CVE scanning cadence), default flags (container-aware memory ratios, `ExitOnOutOfMemoryError`, heap-dump path, GC logging, JFR-on-demand), a documented per-service override process, AOT-cache build step in the shared Dockerfile/buildpack, observability agent/starter, and an upgrade cadence (each LTS within N months) with compatibility tests. Publish the rationale (ADR) and a benchmark harness so teams can justify deviations with data.

## Real-world use cases

- **Streaming chat gateway** with tens of thousands of open SSE connections: ZGC + virtual threads, bounded per-session buffers, cancel-on-disconnect to stop token spend.
- **Bulk ingestion workers:** batch embedding with bounded concurrency; Serial/Parallel GC in small batch pods; NMT-driven memory limits due to PDF/OCR native libs.
- **Scale-to-zero tool services** (MCP servers): AOT cache to keep cold starts inside SLO; native image evaluated for the smallest ones.
- **Cost review:** memory right-sizing and startup improvements that let HPA run leaner.

## Pitfalls & anti-patterns

- Copy-pasting decade-old GC flag lists (CMS-era tuning) into JDK 25.
- Setting `-Xmx` equal to the container limit.
- Tuning without JFR/GC-log evidence; optimising the JVM when the model is the latency.
- Building the AOT cache on a different JDK/image than production.
- Unbounded in-memory caches and streaming buffers.
- Adopting native image because of a conference talk without spiking your dependencies.

## Checklist

- [ ] I can pick and justify a GC and container memory settings from data
- [ ] I built an AOT cache in a container build and measured startup
- [ ] I compared G1 vs ZGC (and compact object headers) on the same load
- [ ] I can explain OOMKill with healthy heap using NMT
- [ ] I answered all L3 questions out loud in < 3 min each
