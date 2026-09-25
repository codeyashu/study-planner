---
title: Java & Spring AI — Question bank
track: java-spring-ai
tags: [java-spring-ai, questions]
last_reviewed: 2026-09-25
---

# Java & Spring AI — Question bank

Cross-topic interview and scenario questions for the [Java & Spring AI track](index.md). Versions assumed (as of September 2026): Java 25 LTS, Spring Boot 4.x, Spring Framework 7, Spring AI 2.0.x (GA 2026-06-12). Per-topic questions live on each topic page; these add breadth. Answer out loud first, then open the answer.

## Graded questions

### L1 — Recall

??? question "L1-1. Which JDK is the current LTS and what are two features that became final in it?"
    ??? success "Answer"
        JDK 25 (GA 2025-09-16). Final: scoped values (JEP 506), module import declarations (JEP 511), compact source files and instance main (JEP 512), flexible constructor bodies (JEP 513). Structured concurrency (JEP 505) is still preview.

??? question "L1-2. What does `sealed ... permits` buy you together with pattern-matching switch?"
    ??? success "Answer"
        Compiler-checked exhaustiveness: no `default` needed, and adding a permitted subtype makes every non-exhaustive switch fail to compile.

??? question "L1-3. What do Spring AI 2.0 and Spring Boot 4 require in terms of framework versions?"
    ??? success "Answer"
        Spring AI 2.0 needs Spring Boot 4.0/4.1 and Spring Framework 7 (Jackson 3). It does not run on Boot 3.

??? question "L1-4. Which class is the primary user-facing API in Spring AI 2.0?"
    ??? success "Answer"
        `ChatClient`. `ChatModel` is the lower-level, provider-specific building block underneath.

??? question "L1-5. What key must you pass to memory advisors, and what constant holds its name?"
    ??? success "Answer"
        The conversation id: `.advisors(a -> a.param(ChatMemory.CONVERSATION_ID, id))`. Omitting it raises `IllegalArgumentException`.

??? question "L1-6. Name the three vector-store index types configurable for pgvector in Spring AI and the default."
    ??? success "Answer"
        `NONE`, `IVFFlat`, `HNSW`; the default is `HNSW` with `COSINE_DISTANCE`.

??? question "L1-7. Which starter creates a Streamable HTTP MCP server on Spring MVC?"
    ??? success "Answer"
        `spring-ai-starter-mcp-server-webmvc` with `spring.ai.mcp.server.protocol=STREAMABLE` (endpoint `/mcp` by default). `-webflux` is the reactive twin; `spring-ai-starter-mcp-server` is STDIO.

??? question "L1-8. Which annotations expose methods as MCP tools, resources and prompts?"
    ??? success "Answer"
        `@McpTool` (with `@McpToolParam`), `@McpResource`, `@McpPrompt` (with `@McpArg`); also `@McpComplete` for argument completion. They live in `org.springframework.ai.mcp.annotation`.

??? question "L1-9. What is ToolContext?"
    ??? success "Answer"
        A map of caller-side data passed with `.toolContext(...)` and accessible to `@Tool` methods via a `ToolContext` parameter, invisible to the model.

??? question "L1-10. What changed for `synchronized` and virtual threads in JDK 24?"
    ??? success "Answer"
        JEP 491: virtual threads blocking inside `synchronized` no longer pin their carrier thread. Native frames and class initialisers can still pin.

??? question "L1-11. Which annotations provide declarative retry and bulkheading in Spring Framework 7 core?"
    ??? success "Answer"
        `@Retryable` and `@ConcurrencyLimit`, enabled by `@EnableResilientMethods`; programmatic `RetryTemplate` also exists.

??? question "L1-12. What are Micrometer observations used for in Spring AI?"
    ??? success "Answer"
        They instrument chat model calls, embeddings, vector-store operations and tool calls, producing spans and metrics (including token usage) that export via OTel.

### L2 — Apply

??? question "L2-1. Write the record and call to get a typed `Invoice(String number, BigDecimal total, LocalDate dueDate)` from raw text, retrying on invalid JSON."
    ??? success "Answer"
        ```java
        record Invoice(String number, BigDecimal total, LocalDate dueDate) {}

        Invoice inv = chat.prompt()
            .user("Extract the invoice fields:\n" + text)
            .call()
            .entity(Invoice.class, s -> s.validateSchema());   // retries with error feedback (default 3)
        if (inv == null) throw new ExtractionFailed();          // entity() is @Nullable
        ```
        Add business validation (total > 0, due date plausible) after the call.

??? question "L2-2. Put chat memory inside the tool loop so tool messages are remembered. How?"
    ??? success "Answer"
        Give the memory advisor an order greater than `ToolCallingAdvisor.DEFAULT_ORDER`, e.g. `MessageChatMemoryAdvisor.builder(memory).order(BaseAdvisor.HIGHEST_PRECEDENCE + 400).build()`. Auto-configuration then disables the internal history handling. By default memory sits outside the loop and stores only the final messages.

??? question "L2-3. Restrict RAG retrieval to the caller's tenant on each request."
    ??? success "Answer"
        `.advisors(a -> a.param(VectorStoreDocumentRetriever.FILTER_EXPRESSION, "tenant == '" + tenantFromPrincipal + "'"))` with `RetrievalAugmentationAdvisor` (or `QuestionAnswerAdvisor.FILTER_EXPRESSION` for the naive advisor). Derive the value from the authenticated principal, never from request input, or build a `Filter.Expression` programmatically.

??? question "L2-4. Configure Spring AI to talk to a local Ollama model and the pgvector store in `application.yml`."
    ??? success "Answer"
        ```yaml
        spring:
          datasource: {url: jdbc:postgresql://localhost:5432/rag, username: postgres, password: postgres}
          ai:
            ollama:
              chat:
                model: llama3.1          # any pulled model
              embedding:
                model: nomic-embed-text
            vectorstore:
              pgvector:
                dimensions: 768          # must match the embedding model
                index-type: HNSW
                distance-type: COSINE_DISTANCE
                initialize-schema: true  # dev only
        ```
        Starters: `spring-ai-starter-model-ollama`, `spring-ai-starter-vector-store-pgvector`.

??? question "L2-5. Write a `Gatherers`-based pipeline to embed chunks in batches of 32 with 4 concurrent calls."
    ??? success "Answer"
        ```java
        chunks.stream()
            .gather(Gatherers.windowFixed(32))
            .gather(Gatherers.mapConcurrent(4, embeddingModel::embed))   // List<String> -> List<float[]>
            .flatMap(List::stream)
            .toList();
        ```
        Order is preserved and virtual threads back the concurrency.

??? question "L2-6. Make an MCP tool that must never run without explicit confirmation on the client. What do you set and what else do you need?"
    ??? success "Answer"
        Mark it `@McpTool(annotations = @McpTool.McpAnnotations(destructiveHint = true))` so clients can prompt. Hints are advisory, so also enforce authorisation in the tool, require a confirmation token/step in the orchestrator (HITL), and use idempotency keys.

??? question "L2-7. Cap agent runaway in Spring AI. Give two mechanisms."
    ??? success "Answer"
        `ToolCallingManager` limits (`maxCallsPerTool`, `maxTotalToolCalls`, `onLimitExceeded`) or `spring.ai.tools.limits.*`; plus application-level caps on fan-out, refinement iterations, wall-clock deadline (`StructuredTaskScope` timeout) and per-run token budgets.

??? question "L2-8. Return a versioned API: v1 unchanged, v2 adds an LLM summary. Show the mapping."
    ??? success "Answer"
        `@GetMapping(path = "/{id}/summary", version = "1.0")` and `@GetMapping(path = "/{id}/summary", version = "2.0+")` on two methods, with `configureApiVersioning(ApiVersionConfigurer c) { c.useRequestHeader("API-Version"); }` in a `WebMvcConfigurer`.

??? question "L2-9. An eval test must fail when retrieval gets worse. Sketch it."
    ??? success "Answer"
        Load a golden set of (question, expected doc ids or reference answer); run retrieval and assert recall@5 ≥ threshold, and run the RAG chain with `RelevancyEvaluator`/`FactCheckingEvaluator` (judge model ≠ generator, temperature 0), asserting on the pass-rate across cases (for example ≥ 90%). Tag `@Tag("eval")` and run on retrieval/prompt/model changes.

??? question "L2-10. Read a shared trace across Python and Java: what must both sides do?"
    ??? success "Answer"
        Use W3C trace context: the Python client sends `traceparent` on the MCP/HTTP call (OTel HTTP instrumentation does this), and the Spring service has the OTel/Micrometer tracing bridge (Boot 4 OTel starter) which extracts it. Export both to the same collector.

??? question "L2-11. Choose GC and memory flags for a 2 GiB pod running a streaming chat service."
    ??? success "Answer"
        Start with G1 (default) and `-XX:MaxRAMPercentage=60-65`, `-XX:+ExitOnOutOfMemoryError`, heap dump path, GC logging; evaluate ZGC if p99 pauses appear in logs. Cap direct memory if Netty buffers are large. Requests = limits. Validate with a load test and NMT before finalising.

??? question "L2-12. Convert a class-based DTO used by Jackson 2 into a record for Jackson 3 and keep polymorphism."
    ??? success "Answer"
        Records deserialise through the canonical constructor. Keep `@JsonTypeInfo`/`@JsonSubTypes` (annotations remain in `com.fasterxml.jackson.annotation`), use `tools.jackson.databind.json.JsonMapper` for the mapper, and catch the unchecked `JacksonException`. Snapshot-test JSON because defaults changed.

### L3 — Design & trade-offs

??? question "L3-1. Advisor vs `@Service` method for cross-cutting LLM logic: give a decision rule."
    ??? success "Answer"
        If it must wrap every model interaction uniformly and doesn't change business control flow (redaction, logging, memory, RAG augmentation, validation), use an advisor. If it is business workflow with branching, approvals or persistence, keep it in services where flow is explicit and testable. Hidden control flow in advisors is order-dependent and hard to debug.

??? question "L3-2. Native structured output vs prompt-based JSON: what's your production default and why?"
    ??? success "Answer"
        Native (constrained) where the provider supports it plus schema validation with a small retry budget plus business validation. Prompt-based only as a fallback. Watch provider limitations (no top-level arrays on OpenAI native mode; reasoning-mode local models may emit prose).

??? question "L3-3. In-memory vs JDBC vs Redis chat memory: how do you choose?"
    ??? success "Answer"
        In-memory only for dev/single-instance. JDBC (Postgres) for durable, queryable, transactional storage and simple ops; Redis for very low latency and TTL semantics but weaker durability/query. Consider retention/PII policy and encryption; window size affects cost and quality; summarisation for long sessions.

??? question "L3-4. pgvector on the primary OLTP database vs a separate Postgres for vectors."
    ??? success "Answer"
        Same DB: transactional consistency with metadata and fewer moving parts, but ANN index builds and vector queries compete for I/O, memory and locks with OLTP, and vacuum/bloat behaviours differ. Separate instance: isolation and independent scaling/tuning; costs an ingestion sync path. Start separate (or a replica) if query load or index size is non-trivial; keep together for small corpora.

??? question "L3-5. When would you choose WebFlux over MVC + virtual threads on Boot 4?"
    ??? success "Answer"
        When you need end-to-end reactive backpressure, an already reactive data layer, or a streaming gateway with extreme connection counts and tight per-request memory. Otherwise MVC + virtual threads is simpler and debuggable and Spring AI streaming still works via `Flux` return types.

??? question "L3-6. Stateless vs stateful MCP server: trade-offs and default."
    ??? success "Answer"
        Stateless scales horizontally with no affinity and matches where the MCP spec is heading, but loses server-initiated features (sampling, elicitation, subscriptions). Stateful supports those at the cost of session affinity/storage and graceful shutdown complexity. Default stateless unless a feature requires state.

??? question "L3-7. Structured concurrency (preview) vs `CompletableFuture`/executors for LLM fan-out."
    ??? success "Answer"
        Structured concurrency gives scoped lifetimes, automatic cancellation on failure/timeout and tree-shaped thread dumps; downsides are preview churn and `--enable-preview` pinning runtime versions. `CompletableFuture`/`invokeAll` on a virtual-thread executor is stable but requires manual cancellation/deadline plumbing. Wrap either behind a small internal API to keep the swap cheap.

??? question "L3-8. Hybrid search: build in Spring AI or push to the database/search engine?"
    ??? success "Answer"
        Spring AI's portable `VectorStore` API is dense-only, so hybrid needs custom retrieval. With Postgres you can do tsvector + pgvector in SQL and fuse (RRF) in a custom `DocumentRetriever`. If you need serious lexical relevance (analyzers, BM25 tuning), or scale, use a search engine with native hybrid (Elasticsearch/OpenSearch/Qdrant etc.) behind the same retriever interface.

??? question "L3-9. Native image vs AOT cache vs plain JVM for MCP microservices."
    ??? success "Answer"
        AOT cache is the default: better startup with full JIT and library compatibility. Native for scale-to-zero/tiny footprints when dependencies are proven. Plain JVM when startup isn't constrained. Prototype your most complex service first.

??? question "L3-10. Where do you put rate limiting and retries for LLM providers?"
    ??? success "Answer"
        Rate limiting/quotas/keys/fallback in a shared gateway; retries in exactly one layer (usually the client closest to the provider with jittered backoff, respecting `Retry-After`); idempotency at tool boundaries. Avoid stacking `@Retryable`, HTTP-client retries and orchestrator retries.

??? question "L3-11. Return citations: store them from the RAG advisor context, or ask the model to cite?"
    ??? success "Answer"
        Prefer system-derived citations: take the retrieved documents from the advisor context (`RetrievalAugmentationAdvisor.DOCUMENT_CONTEXT`) and return their ids/scores, optionally asking the model to reference chunk ids and validating that they belong to the retrieved set. Model-generated citations alone can be fabricated.

??? question "L3-12. One `ChatClient` for the whole app or one per use case?"
    ??? success "Answer"
        One per use case (or per profile) built from a shared builder: different system prompts, options, advisors, tool sets and model choice per capability; isolates changes and eases testing. Share infrastructure beans (memory repository, vector store) but not prompts.

### L4 — Staff-level ambiguity

??? question "L4-1. Design the migration for 40 Spring Boot 3 services to Boot 4 while AI teams need Spring AI 2.0 now."
    ??? success "Answer"
        Two tracks: (1) new AI services on a Boot 4 template immediately (separate deployables, thin adapters for platform libraries); (2) fleet migration by waves — first upgrade to the last 3.x and clear deprecations, add JDK 25 to CI, isolate Jackson customisations, run OpenRewrite recipes, migrate leaf services first, shared libraries publish Boot-4-compatible versions with a compatibility window. Metrics: % services on supported versions, upgrade lead time. Avoid a mandate date without capacity.

??? question "L4-2. Your Spring AI service's quality regressed after a provider silently updated a model alias. What changes in your engineering process?"
    ??? success "Answer"
        Pin dated model versions, not aliases; run golden-set evals in CI and nightly against the pinned and latest versions to detect drift early; track provider release notes; canary model changes with online quality signals; keep a fallback model; record model id in every trace/metric; agree upgrade procedure and ownership with the platform team.

??? question "L4-3. Propose an internal Spring AI starter. What does it include and exclude?"
    ??? success "Answer"
        Include: gateway-backed model config, standard advisors (redaction, budget, logging with policy), observation conventions, memory repository defaults, safe tool-limit defaults, test utilities (scripted `ChatModel`, fake embeddings), and Testcontainers pgvector config. Exclude: prompts, business tools, and opinionated agent logic — those belong to feature teams. Version with semver, document escape hatches, measure adoption and incidents.

??? question "L4-4. Security review flags MCP servers as an attack surface. Build the threat model."
    ??? success "Answer"
        Assets: data behind tools, ability to act. Threats: prompt injection via tool results/resources causing misuse of other tools (lethal trifecta), confused deputy (shared service identity), argument injection, excessive tool permissions, session hijack, supply chain (third-party MCP servers), data exfiltration through responses, denial of wallet. Mitigations: OAuth with end-user identity, per-tool scopes, read/write separation, HITL for destructive actions, output filtering, allow-listed servers, rate limits, audit logs, schema validation, isolation of untrusted-content readers from exfiltration-capable tools.

??? question "L4-5. Leadership wants one 'AI platform' for Java and Python teams. What do you build first?"
    ??? success "Answer"
        The shared foundations that reduce risk and duplication: LLM gateway (routing, keys, quotas, cost attribution), observability standard with cross-language tracing, eval harness and golden-set management, and a tool registry with MCP conventions and security review. Ship paved-road templates (Spring starter, Python package) after these exist. Sequence by pain (cost visibility or security usually first) and measure adoption; resist a monolithic framework mandate.

??? question "L4-6. How do you decide whether Spring AI's lack of a durable runtime is acceptable for a new use case?"
    ??? success "Answer"
        Check state duration and human involvement: if runs finish within a request/timeout, are idempotent and restartable, Spring AI is fine. If runs last minutes to days, need approvals, or must resume after crashes, use a durable runtime (LangGraph, Temporal, Camunda) and let Spring AI supply steps/tools. Also weigh team skills and operational maturity, and write the trigger to revisit.

??? question "L4-7. A team proposes replacing your Java RAG service with a managed vendor RAG product. How do you evaluate?"
    ??? success "Answer"
        Compare on measured quality (shared golden set), security/ACL integration, data residency, cost at projected scale, latency, observability and control (chunking/hybrid/rerank knobs), lock-in and exit cost, team ownership. Run a time-boxed bake-off with identical corpora and queries. Often the answer is hybrid: vendor for low-risk knowledge bases, custom for ACL-heavy domains.

??? question "L4-8. You are asked to cut LLM spend 40% without hurting quality. Outline the plan."
    ??? success "Answer"
        Measure first (tokens by feature, model, prompt component). Levers by typical yield: caching (exact/semantic) for repeats; routing easy tasks to cheaper models with evals; prompt trimming and context budgets (fewer/shorter chunks, summarised memory); batching/async APIs for non-interactive work; output length limits; avoiding retry waste (validation loops, duplicate calls); prompt caching where the provider supports it. Validate each change with the eval suite and track cost per successful task, not per call.

## Scenario questions

??? question "S1. Support copilot for 5,000 concurrent chats; LLM p50 latency 6 s; provider limit 1,200 RPM. Size and design the Java service."
    ??? success "Answer"
        Demand ≈ (5,000 sessions × maybe one message per 60 s) ≈ 83 req/s if all active — far above 20 req/s allowed (1,200 RPM). Real concurrency in flight ≈ rate × latency; even at the allowed 20 req/s that is ~120 in-flight calls. Design: MVC + virtual threads (threads aren't the limit), gateway with token bucket and multiple deployments/keys, queue with fast rejection and user-facing "busy" state, SSE streaming to improve perceived latency, semantic/response caching for FAQs, per-tenant fairness limits. Memory: 5,000 sessions × context (say 50 KB) ≈ 250 MB — fine. Negotiate a higher quota; test with a mock provider.

??? question "S2. RAG answers are correct in dev but wrong in production for one customer. Debug."
    ??? success "Answer"
        Pull traces for failing questions: check the tenant filter value and retrieved chunk ids/scores; likely causes: metadata mismatch (tenant key), documents not ingested or stale (ingestion failure/dead-letter), filtered-ANN returning fewer than topK, different embedding model version in that tenant's data, chunking that split a key clause, or similarity threshold too high. Reproduce with the exact query and filter in SQL. Add per-tenant retrieval-hit metrics and ingestion lag alerts.

??? question "S3. Your MCP server's `get_shipment_status` is called 40 times per conversation by the agent. Fix."
    ??? success "Answer"
        Inspect traces to see why: the tool returns thin or ambiguous data forcing repeated calls, or the description invites polling. Improve the tool (batch parameter, richer response including ETA/events), add a per-tool call cap and cache within a run (short TTL), give the model an explicit "no further calls needed" signal in the response, and set orchestrator limits. Check whether the agent loop lacks a stop criterion.

??? question "S4. Boot 4 upgrade breaks JSON output: dates serialise differently and unknown properties fail. Explain and fix."
    ??? success "Answer"
        Jackson 3 changed defaults and the mapper construction (`JsonMapper`, builder-configured, immutable). Diff behaviour with snapshot tests; configure explicitly via Boot's Jackson properties/customisers (`spring.jackson.*` still applies to the auto-configured mapper) and set date/time and unknown-property handling deliberately. Public APIs need contract tests before the upgrade to catch this class of change.

??? question "S5. A nightly ingestion of 2 million chunks takes 14 hours and sometimes fails midway. Redesign."
    ??? success "Answer"
        Make ingestion incremental and idempotent: content hashes to skip unchanged docs, delete-then-insert per doc id, partitioned workers consuming a queue, batched embedding calls (windowed, bounded concurrency) with rate-limit-aware backoff, checkpointed progress and a dead-letter queue, HNSW index maintenance considerations (build after bulk load or use maintenance settings). Track lag, throughput, and cost. Consider the provider's batch/async embedding APIs for cost.

??? question "S6. A prompt-injection in a PDF made the assistant call a `send_email` tool. What do you change?"
    ??? success "Answer"
        Break the trifecta: separate untrusted-content reading from exfiltration-capable tools, require HITL confirmation for `send_email` with the final recipient/body shown to the user, allow-list recipients, treat retrieved text as data (delimiting, instructions hierarchy), add output/tool-call guardrails, log and alert on anomalous tool sequences, and add adversarial tests (promptfoo-style red-team cases) to CI.

??? question "S7. Startup takes 11 s and scaling events cause a latency spike. Steps?"
    ??? success "Answer"
        Profile startup (Actuator startup endpoint, class-loading logs), remove eager work, adopt AOT cache created in the image build, tune readiness so traffic waits for warm-up (send synthetic warm-up requests), pre-scale on known peaks, and check HPA thresholds. Verify improvement in staging under scale-out tests.

??? question "S8. The Python orchestrator times out at 30 s but the Java tool sometimes takes 45 s under load. Design the fix."
    ??? success "Answer"
        Establish a timeout hierarchy with propagated deadlines: orchestrator sets a budget, the tool honours it (`withTimeout` derived from remaining time) and returns a partial/"still running" result; make slow tools async (start a job, return a job id, poll or callback); bulkhead the tool's downstreams; add SLOs and alerts on tool latency; ensure exactly one retry layer and idempotency.

??? question "S9. Finance shows one tenant consumes 60% of tokens. What do you build?"
    ??? success "Answer"
        Per-tenant token metering (tag by tenant at the gateway or via a Spring AI advisor emitting counters — with bounded cardinality), quotas and soft limits with alerts, cost dashboards, prompt-size guards (max context), caching, and a conversation with the tenant on plan/pricing. Investigate causes first (huge contexts, loops, bots).

??? question "S10. You must choose between Spring AI, LangChain4j and Embabel for a new JVM agent service. How?"
    ??? success "Answer"
        Time-boxed spike with the same golden tasks: evaluate integration with Spring Security/Actuator/observability, MCP support, structured output reliability, tool loop controls, testability, community activity and release cadence, and team familiarity. Default to Spring AI if the org is a Spring shop and needs governed, stateless features; consider Embabel for goal-planning agent designs or LangChain4j for existing investments. Record an ADR; isolate the framework behind your own interfaces where cheap.

## Rapid-fire (20)

??? question "R1. Default index type for Spring AI pgvector?"
    ??? success "Answer"
        HNSW (with cosine distance).

??? question "R2. Which annotation exposes a Spring bean method as an MCP tool?"
    ??? success "Answer"
        `@McpTool`.

??? question "R3. Default MCP Streamable HTTP endpoint path in Spring AI?"
    ??? success "Answer"
        `/mcp`.

??? question "R4. Is SSE still the recommended MCP HTTP transport in Spring AI 2.0?"
    ??? success "Answer"
        No — deprecated since 2.0; use Streamable HTTP (or stateless).

??? question "R5. Which advisor implements modular RAG?"
    ??? success "Answer"
        `RetrievalAugmentationAdvisor`.

??? question "R6. Which advisor validates JSON output against a schema and retries?"
    ??? success "Answer"
        `StructuredOutputValidationAdvisor` (or `entity(..., s -> s.validateSchema())`).

??? question "R7. Default message window size of `MessageWindowChatMemory`?"
    ??? success "Answer"
        20 messages.

??? question "R8. Which JEP made scoped values final?"
    ??? success "Answer"
        JEP 506 (JDK 25).

??? question "R9. Is structured concurrency final in JDK 25?"
    ??? success "Answer"
        No — fifth preview (JEP 505).

??? question "R10. Spring property that switches request handling to virtual threads?"
    ??? success "Answer"
        `spring.threads.virtual.enabled=true`.

??? question "R11. What replaces `ThreadLocal` for immutable, bounded request context in JDK 25?"
    ??? success "Answer"
        `ScopedValue`.

??? question "R12. Which annotation adds a concurrency bulkhead to a method in Spring 7?"
    ??? success "Answer"
        `@ConcurrencyLimit`.

??? question "R13. Where do you enable API versioning on a mapping?"
    ??? success "Answer"
        The `version` attribute of `@RequestMapping`/`@GetMapping`, plus `configureApiVersioning`.

??? question "R14. JVM flag for the Leyden AOT cache at runtime?"
    ??? success "Answer"
        `-XX:AOTCache=<file>` (created with `-XX:AOTCacheOutput=<file>` in a training run).

??? question "R15. JVM flag for compact object headers in JDK 25?"
    ??? success "Answer"
        `-XX:+UseCompactObjectHeaders`.

??? question "R16. Container setting to size heap relative to memory limit?"
    ??? success "Answer"
        `-XX:MaxRAMPercentage` (leave headroom for non-heap memory).

??? question "R17. What must match between the embedding model and pgvector config?"
    ??? success "Answer"
        The `dimensions` value (vector column size).

??? question "R18. What does `allowEmptyContext(false)` do in `ContextualQueryAugmenter`?"
    ??? success "Answer"
        When retrieval returns nothing, the augmenter uses an empty-context response instead of letting the model answer unaided.

??? question "R19. Which Testcontainers-integration annotation wires connection details automatically?"
    ??? success "Answer"
        `@ServiceConnection`.

??? question "R20. Which W3C header correlates a Python call with a Java span?"
    ??? success "Answer"
        `traceparent`.
