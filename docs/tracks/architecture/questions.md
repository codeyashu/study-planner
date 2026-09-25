---
title: Architecture question bank
track: architecture
last_reviewed: 2026-09-25
---

# Architecture question bank

Cross-topic bank complementing the questions inside each topic page. **Part A**: 60 graded questions (L1–L4). **Part B**: 16 architecture katas (requirements → questions to ask → style → decomposition → ADR). **Part C**: 25 rapid-fire questions for daily warm-ups.

How to use: answer out loud first (L3 in under 3 minutes, L4 in 5, katas in 12–15), then open the model answer and note what you missed. Model answers are one reasonable position, not the only one — the defensible reasoning matters more than the verdict.

Topic pages: [index](index.md).

## Part A — Graded questions

### L1 — Recall

??? question "A1. What is the difference between coupling and cohesion, and how are they related in Khononov's model?"
    ??? success "Answer"
        Cohesion is how strongly the parts of a module belong together (change together); coupling is how much a change in one module forces change in another. In the balanced-coupling model they are two views of one idea: things that change together should be close (strong coupling at low distance = cohesion); strong coupling at high distance is the costly case. See [Coupling & modularity](coupling-modularity.md).

??? question "A2. Define bounded context, ubiquitous language and context map."
    ??? success "Answer"
        Bounded context: a boundary within which one model and its terms have a single consistent meaning. Ubiquitous language: the shared vocabulary of domain experts and engineers inside that context, used in code, tests and conversation. Context map: a diagram/description of the relationships between contexts using patterns such as customer/supplier, conformist, ACL, open host service/published language, shared kernel, partnership and separate ways. See [DDD strategic](ddd-strategic.md).

??? question "A3. What does an aggregate protect, and what is the rule for referencing other aggregates?"
    ??? success "Answer"
        An aggregate is a consistency boundary protecting business invariants that must hold immediately within a single transaction; it's accessed only through its root. Other aggregates are referenced by identity, not by object reference, and cross-aggregate consistency is eventual (via domain events). See [DDD tactical](ddd-tactical.md).

??? question "A4. What is the transactional outbox and what guarantee does it give?"
    ??? success "Answer"
        The application writes events to an outbox table in the same local transaction as the state change; a relay (poller or CDC) publishes them to the broker afterwards. Guarantee: at-least-once publication with no lost or phantom events; consumers must be idempotent. See [Sagas & outbox](sagas-outbox.md).

??? question "A5. Name the four C4 levels."
    ??? success "Answer"
        System context, containers, components, code. Plus supplementary landscape, dynamic and deployment diagrams. See [C4, arc42 & diagrams as code](documenting-architecture.md).

??? question "A6. What is a fitness function?"
    ??? success "Answer"
        An objective, ideally automated check of an architectural characteristic (e.g. no dependency cycles, p95 < 300 ms, no breaking API changes, eval score above baseline), run on triggers or continually. It turns architectural principles into executable governance. See [Evolutionary architecture](evolutionary-architecture.md).

??? question "A7. What are Team Topologies' four team types?"
    ??? success "Answer"
        Stream-aligned, enabling, complicated-subsystem and platform teams; interacting via collaboration, X-as-a-Service and facilitating. See [Team Topologies](team-topologies.md).

??? question "A8. State the dependency rule of hexagonal/clean architecture."
    ??? success "Answer"
        Source-code dependencies point inward: the domain and use cases know nothing about frameworks, databases or SDKs; outer adapters implement interfaces (ports) owned by the core. See [Hexagonal architecture](hexagonal-clean.md).

??? question "A9. Give one difference between CQRS and event sourcing."
    ??? success "Answer"
        CQRS separates the write model from one or more read models (may use ordinary tables); event sourcing stores state as an append-only sequence of events from which state is derived. CQRS doesn't require ES; ES practically needs projections (CQRS). See [CQRS & event sourcing](cqrs-event-sourcing.md).

??? question "A10. What are the three saga step types?"
    ??? success "Answer"
        Compensatable steps (can be undone), the pivot (go/no-go; after it the saga completes) and retriable steps (guaranteed to eventually succeed). See [Sagas & outbox](sagas-outbox.md).

??? question "A11. What is an ADR and which sections must it have?"
    ??? success "Answer"
        A short record of one architecturally significant decision. Minimum: title, status, context (forces), decision, consequences (positive and negative); good ones add options considered, deciders and a review trigger. See [ADRs](adrs.md).

??? question "A12. What is the Strangler Fig pattern?"
    ??? success "Answer"
        Incrementally replace a legacy system by routing slices of functionality through a facade to new implementations, retiring legacy pieces as traffic moves. See [Legacy modernization](legacy-modernization.md).

??? question "A13. Define backward and forward compatibility for schemas."
    ??? success "Answer"
        Backward: new readers can read data written by the old schema. Forward: old readers can read data written by the new schema. Full: both. See [API contracts](api-contracts-versioning.md).

??? question "A14. What is the difference between a workflow and an agent in AI systems?"
    ??? success "Answer"
        A workflow follows predefined code paths orchestrating LLM calls and tools; an agent lets the LLM dynamically decide steps and tool use. Prefer the simplest that meets quality targets. See [AI-native architecture](ai-native-architecture.md).

### L2 — Apply

??? question "A15. A team's 'microservices' all deploy together and share one database. Diagnose and give two remedies."
    ??? success "Answer"
        A distributed monolith: strong (intrusive) coupling at high distance with high volatility. Remedies: (1) reduce strength — assign table ownership per service, expose APIs/events instead of shared tables; (2) reduce distance — merge the services that always change together into one deployable owned by one team. Decide using co-change analysis and subdomain boundaries.

??? question "A16. Write the invariant and repository save logic that prevents overbooking a vessel under concurrency."
    ??? success "Answer"
        Invariant in the `Voyage` aggregate: `allocated + requested <= capacity` in `allocate()`. Persistence: optimistic concurrency — `UPDATE ... SET version = version + 1 WHERE id = ? AND version = ?`; zero rows means conflict → reload and retry the command (idempotent by booking id). For a hot voyage, serialise commands per voyage (partitioned queue keyed by voyage id) or shard capacity buckets.

??? question "A17. Choose sync REST vs async events for `OrderPlaced → SendConfirmationEmail`. Justify."
    ??? success "Answer"
        Async event (via outbox). Email is a downstream reaction; the order path must not fail or slow because the email service is down. Consumer is idempotent (dedupe on order id) so redelivery doesn't send duplicates. Use REST only when the caller needs an immediate result (e.g. credit check).

??? question "A18. Refactor a use case that imports `openai` directly so it can be tested and provider-swapped."
    ??? success "Answer"
        Define a task-shaped port in the domain (`DocumentClassifier.classify(text) -> DocumentType`), move the SDK call, prompt, model and parsing into an adapter, inject through the composition root, test the use case with a fake, test the adapter with recorded responses and evals, and add an import-linter rule forbidding `openai` in the core.

??? question "A19. Your consumers replay a Kafka topic from offset 0 monthly. Which compatibility mode do you set, and why?"
    ??? success "Answer"
        `BACKWARD_TRANSITIVE` (or `FULL_TRANSITIVE`): the latest consumer schema must read every historical version in the log. Plain BACKWARD only checks against the previous version and can break replay of old data.

??? question "A20. Convert 'the system must be scalable and highly available' into testable characteristics."
    ??? success "Answer"
        Ask the driver, rank, then quantify: e.g. sustain 3× peak (1,200 bookings/min) with p99 < 500 ms and linear cost; 99.9% monthly availability for booking intake per region; zero lost bookings (RPO 0 for accepted bookings); recovery within 15 min (RTO). Each becomes a fitness function or SLO.

??? question "A21. A saga's payment step times out; the payment may or may not have succeeded. How do you proceed?"
    ??? success "Answer"
        Never assume failure. Query the payment status with the idempotency key (or wait for the callback), treat unknown as a pending state with a timeout policy, and only compensate (release capacity) when payment is confirmed failed or after voiding any authorisation. Use idempotent retries and reconciliation as a safety net.

??? question "A22. Draft a Y-statement for choosing pgvector over a dedicated vector DB."
    ??? success "Answer"
        In the context of adding RAG to an existing Postgres-based product with ~5M chunks and 50 QPS, facing operational overhead and consistency concerns, we decided for pgvector behind a `VectorStore` port and neglected Qdrant and a managed vector service, to achieve one operational surface and transactional consistency with source data, accepting weaker scaling headroom and shared resources with OLTP (review at 50M vectors or 500 QPS).

??? question "A23. Where do you put the transaction boundary and the outbox write in a hexagonal service?"
    ??? success "Answer"
        In the application use case via a Unit of Work port: load aggregate, execute behaviour, add outbox rows from the aggregate's events, commit once. Controllers don't manage transactions; the domain doesn't know about persistence.

??? question "A24. Give a fitness function set for a modular monolith."
    ??? success "Answer"
        import-linter/ArchUnit contracts: modules import only each other's `api`; domain has no framework/SDK imports; no cycles; per-module DB schema ownership check (queries don't join across schemas); CODEOWNERS presence; module-level test coverage threshold; and a ratchet on cross-module calls. Failing messages link the ADR.

??? question "A25. A client's app crashed when you added an enum value. How do you evolve enums safely?"
    ??? success "Answer"
        Document enums as open (clients must handle unknown values), include an UNSPECIFIED/UNKNOWN default, and roll out new values behind a capability/version gate so old clients don't receive them, plus contract tests with unknown values. For events, treat new values as schema changes with announced migration.

??? question "A26. Estimate: 8 stream-aligned teams, each owning 3 services. What does Team Topologies suggest?"
    ??? success "Answer"
        Check cognitive load: 3 services per team is plausible if services are small and platform reduces extraneous load (CI/CD, observability). Ensure each service belongs to one bounded context owned by one team, provide a platform team so teams don't run infrastructure themselves, and watch on-call burden. If on-call and onboarding suffer, consolidate services within contexts.

??? question "A27. What are the checks between an LLM's output and a state-changing action?"
    ??? success "Answer"
        Schema validation, domain invariants, grounding/citation checks, policy/safety rules (allow-lists, limits), risk tiering (auto / sampled review / human approval), idempotent execution via domain commands and audit logging. Cheap deterministic checks first; LLM-judge or human last.

### L3 — Design & trade-offs

??? question "A28. Modular monolith with an extracted ingest service vs full microservices for a 5-team, 30-engineer product. Decide."
    ??? success "Answer"
        Modular monolith + extracted high-volume ingest (divergent scaling/availability). Five teams can own modules without the operational tax of many services; boundaries are enforced with tooling, and you extract further only when evidence appears (independent release need, scaling divergence, team growth). Trade-offs: one deployment cadence for the core and shared failure domain; mitigate with feature flags, strong CI and clear ownership. Record triggers for revisiting in an ADR.

??? question "A29. Event sourcing vs state-based + audit table for a shipment-tracking aggregate. Which?"
    ??? success "Answer"
        Usually state-based + outbox (and possibly an append-only history table). Tracking is naturally event-like, but unless you need temporal queries, replay-based read-model rebuilds or intent-rich audit as a core requirement, ES's schema evolution and projection costs aren't justified. If tracking events are the domain (ETA models need full history), keep them as an append-only stream *as data* without making every aggregate event-sourced.

??? question "A30. Choreography vs orchestration for a 6-step order fulfilment with returns and partial shipments."
    ??? success "Answer"
        Orchestration (workflow engine or persisted state machine): branching, partial states, timers and compensation need an explicit owner and queryable state. Use events outwards for fan-out (notifications, analytics). Choreography would scatter logic and make "where is order 123?" hard to answer.

??? question "A31. Shared library of domain types vs generated contract types per consumer for 12 services."
    ??? success "Answer"
        Generated contract types per consumer from a producer-owned schema. A shared domain library is model coupling across teams and forces lock-step upgrades; generated clients keep coupling at contract level, and consumers map to their internal models (ACL). Share only stable primitives (Money, ids).

??? question "A32. Where should PII redaction for LLM calls live: in each service, or at the gateway?"
    ??? success "Answer"
        Both, with different roles: the gateway enforces a baseline policy consistently (detect/redact/block by data classification, tenant and provider region, and logs safely); services minimise data by design (send only needed fields, use references) since the gateway can't know semantics. Central enforcement avoids 30 divergent implementations; domain-level minimisation avoids sending data that shouldn't leave the context at all.

??? question "A33. Build vs buy an internal LLM gateway."
    ??? success "Answer"
        Start from OSS (e.g. LiteLLM) or managed gateway features to get routing, quotas and observability quickly; build custom layers only for differentiating needs (tenant-specific policy, cost chargeback integration). Building from scratch rarely pays. Decision criteria: features needed vs OSS coverage, ops capacity, security review, data-residency, exit plan. Keep your services on a stable internal API so gateways are swappable.

??? question "A34. How would you decide the granularity of services in a new logistics platform?"
    ??? success "Answer"
        Start from subdomains and bounded contexts (EventStorming), check characteristic divergence (ingest vs booking), team ownership (one team per service, ≤ 2–3 services per team), transactional boundaries (don't split what needs ACID), and change coupling. Begin coarse (modules), split when evidence appears. Avoid entity services and nano-services.

??? question "A35. Argue for and against an enterprise API gateway that also performs orchestration and transformation logic."
    ??? success "Answer"
        For: central place for cross-cutting concerns and quick composition for clients. Against: business logic in the pipe (ESB anti-pattern) becomes an ownerless bottleneck, couples all clients, and is hard to test/version. Recommendation: gateway for authn/z, rate limiting, routing, observability; composition in BFFs or owning services; orchestration in domain workflows.

??? question "A36. Compare Kafka-based event backbone vs cloud queues/topics for a company with 3 consumers needing replay."
    ??? success "Answer"
        Log-based platforms (Kafka/Event Hubs Kafka endpoint) give retention, replay, partition ordering and independent consumer groups — needed for replay. Queues/topics (Service Bus, SQS+SNS) are simpler for commands, DLQ and per-message semantics but replay after ack is limited. Use the log for events, queues for work distribution/commands where semantics fit; weigh ops burden and team skills.

??? question "A37. When would you introduce a data mesh in an organisation with a central data team?"
    ??? success "Answer"
        When the central team is a capacity/knowledge bottleneck across many domains, domains have (or can get) data skills, a self-serve platform exists or is funded, and governance can be federated with automation. Otherwise start with mesh-lite: platform + a few domain-owned data products with contracts.

??? question "A38. Rewrite vs strangle for a 15-year-old pricing engine embedded in a monolith."
    ??? success "Answer"
        Strangle via branch by abstraction: introduce a pricing interface inside the monolith, characterise behaviour with golden-master tests from production, build the new engine behind the interface, shadow-run and diff, canary by customer segment, then delete the old code. Rewrite risks: hidden rules, moving target, no value until the end. Consider a clean rebuild only if the domain is small and well specified.

??? question "A39. Design the failure handling for an agent tool that calls a flaky customs API."
    ??? success "Answer"
        Tool returns structured errors (retryable vs terminal) with helpful messages; the orchestrator (not the LLM) owns retries with backoff and jitter, circuit breaker, timeout budget and idempotency keys; degrade to a queue for later processing and inform the user; log traces. Set a per-run retry/step budget so the agent can't loop, and expose status via the workflow rather than in prompt state.

??? question "A40. Team owns three agents; each grows its own prompt/memory store. How do you keep bounded contexts intact?"
    ??? success "Answer"
        Each agent belongs to a context with its own tools, data and evals; cross-context data via published contracts (events/APIs), never shared memory tables; memory stores are per-context with ACLs and retention; a shared platform provides the runtime, gateway and tracing. If two agents share most of their language and tools, that's one context.

??? question "A41. How do you decide whether a component should be a library, a module or a service?"
    ??? success "Answer"
        Library: stable, generic, low volatility, owned centrally (or copy-paste). Module (in a modular monolith): domain capability sharing deployment but with enforced boundaries. Service: needs independent deploy/scale/failure isolation or has a distinct owner team and contract. Use balanced-coupling: volatile parts shouldn't be strongly coupled at distance.

??? question "A42. Multi-region active-active vs active-passive for booking intake: architectural implications."
    ??? success "Answer"
        Active-active demands conflict handling (per-region ownership of bookings or CRDT-like merging), global uniqueness of ids, cross-region event replication and data residency management — significantly more complexity. Active-passive is simpler with RTO/RPO trade-offs. Choose by business RPO/RTO and regulatory needs; often partition by customer home region (cell-based) for active-active with mostly local writes.

### L4 — Staff-level ambiguity

??? question "A43. You're the new Principal Architect; three teams have conflicting proposals for the same platform decision. How do you run it?"
    ??? success "Answer"
        Reframe from solutions to drivers and characteristics; make the decision owner and deadline explicit; each team documents options fairly (including the others') in one ADR draft; agree evaluation criteria and weights first; use time-boxed spikes for uncertain claims; hold a decision meeting with the decider; record dissent and review triggers. Communicate the outcome with reasoning, and follow up with fitness functions to verify assumptions. Aim to preserve relationships: everyone's concerns appear as explicit consequences.

??? question "A44. Executives want to 'adopt AI everywhere' within 6 months. What architectural foundation do you insist on first?"
    ??? success "Answer"
        A thin, high-leverage foundation: an LLM gateway (auth, quotas, cost, PII policy, failover), an eval harness and standards (each feature ships with offline evals and online monitoring), trace/observability conventions, an action-safety policy (autonomy levels, least privilege, approval), and a data-access pattern (ACL-aware retrieval). Then let teams build features on paved roads. Avoid a big platform first; sequence gateway → templates → evals → guardrails, driven by first 2–3 use cases.

??? question "A45. A critical system has no documentation, and its two experts are leaving in 3 months. What do you do?"
    ??? success "Answer"
        Capture knowledge as executable artefacts first: characterisation tests around critical behaviours, recorded runbooks from incident walkthroughs, C4 context/container from traces and deployment manifests, and retrospective ADRs for surprising decisions (with confidence tags). Use interview sessions with the experts guided by scenarios (failure modes, deploys, edge cases), record and transcribe them, and have an LLM draft summaries for the experts to verify. Assign successors to shadow, and run a game day where successors operate the system with experts observing.

??? question "A46. Your microservices estate has 150 services and monthly incidents from cascading failures. Propose a resilience strategy across teams."
    ??? success "Answer"
        Map the dependency graph from traces; identify critical paths and fan-in hubs; set SLOs and error budgets per tier; standardise resilience defaults (timeouts, retries with budgets, circuit breakers, bulkheads) in the platform's service template/mesh; introduce degradation modes for hubs; run game days and fault injection as continual fitness functions; reduce sync chains via events where the business allows; consolidate over-granular services. Prioritise the top-10 incident sources first and publish results.

??? question "A47. Product proposes an 'autonomous agent' that negotiates rates with carriers by email. What's your architecture stance?"
    ??? success "Answer"
        Treat it as L1 (propose) then bounded L2: the agent drafts and proposes counteroffers within policy limits; outbound emails require approval initially; commitments (rates) are domain commands validated by rules; the agent processes untrusted carrier emails, so it must not hold private pricing data plus an external channel simultaneously (lethal trifecta): split roles (reader agent extracts structured offers; pricing service decides; comms step sends templated messages). Evals on adversarial emails, audit trails, and metrics on acceptance and reversal rates drive promotion of autonomy.

??? question "A48. Two divisions use different message formats for the same business events, and integration is slow. How do you converge without a big canonical model?"
    ??? success "Answer"
        Identify the few cross-division events and entities that matter (shipment status, party ids), define a published language for them owned by the upstream context (aligned with industry standards where available), add ACLs to translate at each side, and standardise identifiers/reference data governance. Introduce schema registry compatibility rules and an integration catalogue. Leave internal models alone. Measure integration lead time and defect rates to prove value before expanding.

??? question "A49. How do you decide when to stop investing in a legacy system's modernization?"
    ??? success "Answer"
        Compare cost of change and risk against business value: if change pressure is low, run cost is acceptable and risks are contained (Retain), stop investing beyond safety and security. Mark it as "frozen" with an ACL boundary and monitor triggers (new business need, security end-of-life, vendor support end). Invest where the cost of delay in that area is high. Record the decision in an ADR with review date.

??? question "A50. A high-profile outage traces to an accepted ADR's assumption that no longer held. What changes?"
    ??? success "Answer"
        Blameless review focusing on the mechanism: assumptions weren't monitored. Add review triggers with measurable thresholds to ADRs, convert assumptions to fitness functions or alerts (e.g. traffic > 5k/s triggers review), assign ADR owners to review periodically, and run quarterly assumption audits for critical decisions. Publish the learning; don't punish the decision's author — the process lacked feedback.

??? question "A51. Leadership asks you to reduce architecture 'complexity'. How do you define and measure it?"
    ??? success "Answer"
        Define through outcomes and structure: lead time and change failure rate, onboarding time, coordination cost (cross-team PRs, coordinated releases), number of technologies and integration styles in use, dependency graph metrics (fan-in/out, cycles), co-change coupling, cognitive load surveys. Identify accidental complexity sources (duplicate systems, unowned services, unnecessary distribution) and propose consolidation with measured targets. Avoid a single vanity metric.

??? question "A52. Your team wants to adopt event sourcing for a new domain because 'we might need audit later'. Response?"
    ??? success "Answer"
        Ask what audit means concretely (regulatory requirement? who queries it? retention?). Cheaper alternatives: append-only audit/history tables, CDC to an audit store, outbox events. ES is justified when temporal queries, replay-based read models or intent-rich history are core requirements. YAGNI applies, but keep the door open: design aggregates with clear commands/events so moving to ES later is feasible.

??? question "A53. How do you handle an architect-vs-team disagreement where the team has built something contradicting an ADR, and it works well?"
    ??? success "Answer"
        Treat it as data: why did the ADR not fit? Investigate the team's constraints and results (metrics). If the deviation is better, supersede or amend the ADR with the new evidence and update fitness functions; if it creates risk (e.g. security), agree remediation and an exception with an expiry. Emphasise that ADRs guide, and learning flows both ways; publicly credit the team.

??? question "A54. Design the governance for LLM prompts: who owns them, how they change, how they roll out."
    ??? success "Answer"
        Prompts are code-like artefacts owned by the team owning the capability (stream-aligned), versioned in the repo or a prompt registry with semantic versions, changed via PRs that run eval gates (quality/cost/latency/safety), rolled out with canaries/shadow and feature flags, traced with prompt version ids, and reviewed for security (injection resilience). Platform provides the registry, eval harness and rollback tooling; the guild curates patterns.

??? question "A55. Explain to a CFO why architecture investment (fitness functions, ADRs, modularisation) pays off."
    ??? success "Answer"
        Frame in money and risk: change lead time and failure rates directly determine feature throughput; coupled systems increase the cost of every change (coordination), incident cost and onboarding time. Show data from your org: hours lost to coordinated releases and incidents; cost of delay of two blocked features; an investment plan with staged milestones and leading indicators (co-change ratio, deployment frequency). Compare with the interest analogy for technical debt. Ask for a limited pilot with measurable outcomes.

??? question "A56. When should an architect say 'no' to a technically attractive proposal?"
    ??? success "Answer"
        When it doesn't serve the top characteristics or business drivers, exceeds the team's capacity to operate (cognitive load), adds one-way-door risk without evidence, or duplicates a paved-road capability. Say 'not now' with conditions ('if X metric crosses Y' or 'after the platform supports Z'), offer a smaller experiment, and record it in an ADR so the reasoning is visible.

??? question "A57. Your company is considering moving core logistics workloads from a hyperscaler to another for cost. What architectural questions do you raise?"
    ??? success "Answer"
        Which managed services are we coupled to (databases, messaging, identity, AI services)? What's the abstraction we own (ports, IaC portability)? Data gravity and egress cost; regulatory and residency implications; skills and operations; migration strategy (strangler by workload, dual-run), and realistic savings vs migration and dual-running costs. Consider negotiating and optimising first. Decision as an ADR with cost model and exit criteria.

??? question "A58. How would you structure architecture work in a company of 500 engineers without creating an ivory tower?"
    ??? success "Answer"
        A small architecture group focused on enabling: principles and paved roads, an advice-process ADR practice, fitness functions, guild forums, and embedded architects rotating into critical initiatives. Decisions are made by teams; org-level decisions (identity, cloud, LLM gateway) owned by a platform/architecture council with SLAs. Measure by team outcomes (lead time, incident rates) and satisfaction, not review counts.

??? question "A59. What would you put on a one-page architecture strategy for an AI-enabled product organisation?"
    ??? success "Answer"
        Diagnosis (current constraints: duplicate LLM stacks, coupling, unclear ownership), guiding policies (modular monolith by default, agents as bounded contexts, LLM behind ports and gateway, actions via domain commands, evals as fitness functions, autonomy ladder), coherent actions with owners and dates (gateway in Q1, eval standard in Q2, extract tracking ingest in Q3), measures (lead time, cost per task, incident/injection findings), and explicit non-goals (no mandated framework, no central approval board).

??? question "A60. Pick the single practice that would most improve an average 100-engineer company's architecture and defend it."
    ??? success "Answer"
        Automated, owned boundaries: module/service ownership plus fitness functions in CI (dependency rules, API compatibility, SLO checks). It converts principles into feedback at commit time, scales without a review board, protects the highest-cost coupling problems, and gives coding agents the same guardrails. ADRs are a close second because they preserve reasoning, but rules without checks decay.

## Part B — Architecture katas

Format for each: **Requirements** → *ask for* (clarifying questions) → *style and decomposition* → *key decisions/ADRs* → *risks*. Give yourself 12–15 minutes. Model answers are compact; expand your own with numbers.

??? question "K1. Freight booking portal"
    Shippers book containers across 40 ports; 2,000 concurrent users, 300 bookings/minute peak; price and capacity from two internal systems; must show booking status in near-real-time; 4 teams; EU + India data residency; 6-month MVP.

    ??? success "Answer"
        **Ask:** what is consistency-critical (capacity allocation vs price display)? Cut-off deadlines? Amendment frequency? Integration SLAs of pricing/capacity systems? Residency: which data can cross regions? Team skills?

        **Style:** modular monolith (Booking, Pricing-adapter, Capacity-adapter, Customer, Notifications) with ports to the two internal systems (ACL), async status updates via outbox events; deploy per-region cells for residency. Top characteristics: availability of intake, data residency, modifiability.

        **Decisions:** ADR-1 modular monolith over microservices (4 teams, MVP speed, extract later); ADR-2 capacity reserve-then-confirm saga with expiry; ADR-3 region cells with customer home region routing; ADR-4 events + read model for status.

        **Risks:** capacity system latency (timeouts, degrade to "pending"), double allocation (idempotency keys), cross-region reporting (aggregate anonymised).

??? question "K2. Carrier EDI ingestion hub"
    Ingest 200 carrier feeds (EDIFACT over SFTP/AS2, JSON webhooks, CSV emails) — 15k messages/min peak; normalise to a canonical shipment event; downstream consumers: tracking, ETA, customer notifications; partners change formats without notice.

    ??? success "Answer"
        **Ask:** latency needs per consumer, replay/audit requirements, ordering per shipment, correctness of duplicates, partner onboarding cadence.

        **Style:** event-driven ingestion pipeline: channel adapters per protocol → raw topic (claim check for big payloads) → per-partner translators (plugin/microkernel) → canonical event topic keyed by shipment id → consumers. Invalid message channel with an ops UI for reprocessing; schema registry with transitive compatibility; LLM-assisted translator only for free-text emails behind validation.

        **Decisions:** ADR: Kafka log with replay; ADR: canonical model scoped to shipment events (published language), not enterprise-wide; idempotent receiver by (partner, message id).

        **Risks:** silent partner format drift (contract tests + parse-failure-rate alerts), ordering across sources (version/time semantics), DLQ graveyard (owner + SLA).

??? question "K3. Payment platform for a marketplace"
    Collect from buyers, hold funds, pay out to sellers in 30 currencies; 500 tx/s peak; auditors require full traceability; refunds/chargebacks; PSP outages happen.

    ??? success "Answer"
        **Ask:** regulatory scope (PCI, licensing), settlement cycles, consistency expectations for balances, multi-PSP requirement, fraud checks.

        **Style:** core ledger event-sourced (double-entry journal, immutable), payment orchestration as durable workflows/sagas, PSPs behind ports with per-country adapters, idempotency keys everywhere, reconciliation jobs. CQRS read models for balances and reports.

        **Decisions:** ADR: ES/append-only ledger (auditability, temporal queries); ADR: orchestration via workflow engine; ADR: PSP routing with circuit breakers and failover; ADR: money as value objects with decimal arithmetic.

        **Risks:** exactly-once illusions (idempotent consumers + reconciliation), hot merchant accounts (sharded balances), PCI scope (tokenisation, isolating card data in a separate quantum).

??? question "K4. Enterprise RAG assistant"
    10 million documents across SharePoint, Confluence and a DMS; 5,000 users with document-level permissions; answers must cite sources; documents change hourly; regulated content must be deletable within 1 hour.

    ??? success "Answer"
        **Ask:** permission model source of truth, latency target, languages, answer accuracy bar, audit needs, data classes allowed to leave the region.

        **Style:** ingestion as event-driven projection (connectors → change events → chunk/embed → hybrid index with ACL metadata), query path: authn → ACL filter → hybrid retrieval + rerank → LLM via gateway → citation verification. Retrieval port and generation port in a hexagonal core; deletion propagation events; freshness SLO metric.

        **Decisions:** ADR: hybrid search (BM25+dense) with cross-encoder rerank; ADR: ACL enforcement at retrieval (pre-filter), never post-hoc in the prompt; ADR: eval-gated releases (golden questions incl. permission-boundary tests).

        **Risks:** ACL drift (sync events + reconciliation), prompt injection via documents (treat as untrusted, no tools with side effects), cost (routing, caching).

??? question "K5. Ride/haul dispatch marketplace"
    Match trucks with loads across a country; 100k trucks send location every 10 s; dispatchers need live map and auto-suggestions; matching decisions must be explainable.

    ??? success "Answer"
        **Ask:** matching latency, acceptable stale location age, decision audit needs, peak concurrent loads, geographic partitioning.

        **Style:** event streaming for locations (partition by region/geohash), stateful stream processing for proximity indexing, matching service (complicated subsystem) using an optimiser plus an LLM-based explanation component behind a port; dispatcher UI via server push. Read models in geo-capable store; commands go through domain services with aggregates for `Load` and `Assignment`.

        **Decisions:** ADR: sharded geo index in memory with snapshots; ADR: assignment as saga with driver acceptance timeout; ADR: explanations generated post-hoc from decision features (not the LLM making the decision).

        **Risks:** hot cities (dynamic partitioning), stale locations (TTL semantics), double assignment (aggregate invariant + optimistic concurrency).

??? question "K6. Migrate a mainframe billing system"
    COBOL billing (nightly batch, 30 years old) produces invoices for 200k customers; business wants weekly pricing changes and self-service invoice queries; no one dares change the code; 3-year horizon.

    ??? success "Answer"
        **Ask:** where is change pressure (pricing rules?), regulatory audit needs, batch windows, data quality, interface inventory, licence renewal date.

        **Style:** strangler: place an integration layer around the mainframe (MQ/CDC → event backbone), build a read model for self-service invoice queries first (fast value, low risk), then extract the pricing/rating capability as a new service using shadow runs against golden-master outputs; leave the ledger-like batch last.

        **Decisions:** ADR: CDC from DB2 into a lakehouse/read model (mainframe remains source of truth initially); ADR: pricing extraction with branch by abstraction or event interception; ADR: parallel-run through two billing cycles before cutover; use LLMs for rule extraction and test generation with expert validation.

        **Risks:** hidden rules (characterisation), dual-run costs, transitional architecture becoming permanent (kill list), key-person risk.

??? question "K7. Multi-tenant SaaS with regulated customers"
    B2B SaaS for 400 tenants; large banks demand data isolation and BYOK encryption; small tenants are cost-sensitive; noisy neighbour incidents.

    ??? success "Answer"
        **Ask:** isolation requirements per tier (logical/physical), compliance certifications, regional needs, tenant size distribution, onboarding automation.

        **Style:** tiered tenancy: pooled multi-tenant for small tenants (row-level security, per-tenant quotas), siloed cells (dedicated DB/compute) for large regulated tenants, same codebase, control plane for provisioning. Cell-based architecture limits blast radius; routing layer by tenant.

        **Decisions:** ADR: tenancy tiers and cell model; ADR: per-tenant keys (KMS) with envelope encryption; ADR: noisy-neighbour controls (rate limits, bulkheads, fair queues); ADR: tenant-aware observability and cost attribution.

        **Risks:** operational overhead of many cells (automation), schema migrations across cells (expand/contract, staged rollout), tenant moves between tiers (data migration tooling).

??? question "K8. Notification platform for 20 products"
    Email/SMS/push/WhatsApp; 50M messages/day, spikes 10×; user preferences and quiet hours; templates per locale; deliverability tracking; an LLM feature drafts personalised messages.

    ??? success "Answer"
        **Ask:** ordering guarantees, transactional vs marketing SLAs, per-channel provider limits, compliance (opt-in), personalisation latency.

        **Style:** event-driven: products publish `NotificationRequested`; a routing service applies preferences and rate limits; per-channel workers with provider adapters (ports), retries and DLQ; separate queues per priority class (transactional vs marketing). LLM personalisation as an async pre-step with fallback to static templates and content guardrails.

        **Decisions:** ADR: priority-lane topics; ADR: idempotency by (request id, channel); ADR: provider failover per channel; ADR: LLM drafts require template-level approval for regulated content.

        **Risks:** provider throttling (backpressure and smoothing), duplicate sends (idempotency), preference/consent correctness (source of truth and audit).

??? question "K9. Consolidate three RAG stacks"
    Three teams built RAG apps with different vector DBs, chunking, embeddings and no evals; CTO wants convergence in one quarter without stopping delivery.

    ??? success "Answer"
        **Ask:** which apps are business-critical, quality baselines, data classification differences, team capacity, provider contracts.

        **Style:** platform + domain split: platform provides gateway, ingestion pipeline templates, hybrid retrieval service or library, eval harness and tracing; teams keep domain-specific prompts/chunking configs. Migrate opportunistically: first standardise evals and tracing (visible quality baseline), then the gateway, then retrieval implementation.

        **Decisions:** ADR: default retrieval stack (pgvector or chosen store) with an exception process; ADR: eval-first migration (no migration without golden-set parity); ADR: shared ingestion contract (events) not shared index.

        **Risks:** forced migration without quality proof (parity gates), platform team as bottleneck (self-service templates), politics (co-create standards with the three teams).

??? question "K10. Real-time visibility for cold-chain shipments"
    IoT sensors report temperature every minute for 500k containers; alert within 2 minutes on excursions; alerts trigger workflows (reroute, quality claims); auditors need immutable records.

    ??? success "Answer"
        **Ask:** alert SLA per customer, sensor connectivity gaps, evidence requirements, retention, false-alarm tolerance.

        **Style:** streaming architecture: device gateway → Kafka (key by container) → stream processor evaluating rules/thresholds with state (stuck sensors, gaps) → alerts topic → workflow orchestrator for responses; raw readings to object storage/lakehouse for audit (append-only with retention lock); aggregates in a time-series store for UI.

        **Decisions:** ADR: stream processing with event-time and watermarks; ADR: alert deduplication and hysteresis; ADR: immutable audit store with hash chaining or WORM retention; ADR: ML anomaly detection as an optional layer behind a port, not replacing rules initially.

        **Risks:** offline sensors (late data), alert fatigue, cost of storing raw data (tiering).

??? question "K11. Public API platform for partners"
    5,000 partners integrate; long tail of old clients; need monetisation tiers; frequent product changes; security incidents from leaked keys.

    ??? success "Answer"
        **Ask:** SLAs per tier, change cadence, partner support model, auth requirements (OAuth2 client credentials, mTLS?), data sensitivity.

        **Style:** API gateway with authn/z, quotas per tier and analytics; versioning strategy additive-first with date-based pinning for breaking changes (Stripe-like) or long-lived major versions; developer portal, sandbox, changelog and deprecation policy with brownouts; contract tests and OpenAPI breaking-change gates.

        **Decisions:** ADR: versioning model; ADR: OAuth2 with short-lived tokens and key rotation tooling; ADR: usage-based quota enforcement at gateway; ADR: webhooks with signing and replay.

        **Risks:** Hyrum's law with the long tail (usage analytics, brownouts), support cost (self-service tooling), abuse (rate limiting, anomaly detection).

??? question "K12. Post-merger customer master"
    Two companies with different customer IDs and CRMs; sales wants one customer view within 6 months; finance needs legal-entity accuracy; GDPR applies.

    ??? success "Answer"
        **Ask:** which decisions need the *golden record* vs a unified view; matching rules and tolerance; legal entity hierarchies; where updates originate.

        **Style:** don't merge systems first; build a customer identity/master context: ingest via CDC from both CRMs, match/merge service (deterministic rules + optional ML with human review), publish `CustomerMerged`/`CustomerUpdated` events as published language, keep source-system ids as cross-references. Consumers ACL into their models. Consent and erasure propagate via events.

        **Decisions:** ADR: registry-style MDM (cross-reference + golden attributes) first, not migration; ADR: survivorship rules per attribute; ADR: human-in-the-loop for low-confidence matches; ADR: erasure workflow across systems.

        **Risks:** false merges (undo capability, audit), politics over ownership, downstream systems assuming single id.

??? question "K13. Agentic customer-support automation"
    Support handles 50k tickets/day; leadership wants 40% auto-resolution; agents may issue refunds ≤ $100, re-ship items, and update addresses; PII everywhere; some tickets contain hostile content.

    ??? success "Answer"
        **Ask:** current resolution taxonomy, acceptable error rate per action, reversal costs, audit/regulatory needs, languages, escalation SLAs.

        **Style:** workflow-first: classify → retrieve policy/customer context → propose action → validate → execute or escalate. Actions as domain commands via tools with idempotency keys; autonomy ladder starting at L1 (agent proposes, human approves) and promoting action types to L2 with evidence; gateway, tracing, eval suite from real tickets.

        **Decisions:** ADR: autonomy levels per action type; ADR: lethal-trifecta separation (untrusted content reader with no tools; actor with scoped tools); ADR: per-run budgets and kill switch; ADR: eval gate on prompt/model changes with adversarial tickets.

        **Risks:** injection via ticket content, refund abuse (limits and anomaly detection), quality drift (online sampling), customer trust (transparent escalation).

??? question "K14. Replace a nightly ETL with near-real-time analytics"
    Retail analytics loads 30 OLTP databases nightly into a warehouse; dashboards stale by a day; DBAs object to load on OLTP; schema changes break jobs weekly.

    ??? success "Answer"
        **Ask:** which dashboards truly need freshness (minutes vs hours), tolerance for eventual consistency, PII handling, cost limits.

        **Style:** log-based CDC (Debezium) into Kafka → bronze/silver/gold lakehouse with idempotent merges; latency tiers: minutes for operational dashboards, hourly/daily for finance. Schema change handling via registry compatibility and additive migrations; data contracts for gold tables; data quality tests and freshness SLOs.

        **Decisions:** ADR: CDC over query-based extraction (deletes, low load); ADR: medallion layers on Iceberg/Delta; ADR: contract ownership by source teams for exposed tables; ADR: tiered latency (don't stream everything).

        **Risks:** initial snapshot load and lag, schema drift (alerts and contracts), cost growth (partitioning, compaction), PII (masking at bronze→silver).

??? question "K15. Internal developer platform with an AI gateway"
    600 engineers; 40 teams; need self-service environments, standardised CI/CD, observability and safe LLM access; platform team of 10.

    ??? success "Answer"
        **Ask:** current pain (lead time? onboarding? incidents?), tech diversity, compliance, adoption incentives, budget.

        **Style:** platform-as-product: thin paved roads (service templates with CI/CD, tracing, SLO dashboards), self-service via portal/CLI, golden paths for Python and Java; LLM gateway as a platform service; enabling team for guidance. Measure adoption and DORA metrics of consumers; treat platform teams as X-as-a-Service with roadmap and SLAs.

        **Decisions:** ADR: opinionated defaults with escape hatches; ADR: single gateway egress for model providers; ADR: service catalogue with ownership metadata; ADR: platform funding and success metrics.

        **Risks:** platform as ticket queue, mandate without value, feature bloat; mitigate with user research, adoption metrics and deprecating unused features.

??? question "K16. Cloud-portable AI application"
    A bank wants an AI assistant deployable on Azure now, possibly AWS or on-prem later; models via provider APIs today, self-hosted later for sensitive data; auditors need reproducible decisions.

    ??? success "Answer"
        **Ask:** which portability level is real (workload, data, or just exit plan), residency, cost of abstraction, audit reproducibility definition, team skills.

        **Style:** hexagonal core with ports for model, retrieval, tools, memory, and event bus; adapters per cloud/provider; containerised workloads with IaC modules; a gateway with OpenAI-compatible API to swap model backends (hosted or self-hosted via vLLM); data stores chosen for portability (Postgres/pgvector, object storage API).

        **Decisions:** ADR: portability strategy — abstract only volatile/high-lock-in seams, accept managed services where exit cost is modest; ADR: decision logging (inputs, retrieved docs versions, model/prompt versions, outputs) in immutable storage; ADR: eval parity suite for any model backend swap; ADR: pinned model versions and change control.

        **Risks:** lowest-common-denominator abstractions, behavioural differences across models (evals catch), audit reproducibility of non-deterministic outputs (store outputs; pin versions).

## Part C — Rapid-fire (25)

Answer each in one or two sentences before opening the answer.

??? question "R1. What does 'why is more important than how' imply in practice?"
    ??? success "Answer"
        Record the reasoning and rejected options (ADRs); the how changes, the why lets successors judge whether it still applies.

??? question "R2. Modular monolith's key enforcement mechanism?"
    ??? success "Answer"
        Automated boundary checks (import-linter/ArchUnit/Modulith verification) plus module ownership.

??? question "R3. One-line definition of a distributed monolith."
    ??? success "Answer"
        Many deployables that must change and release together because of strong coupling across boundaries.

??? question "R4. Which subdomain type do you buy?"
    ??? success "Answer"
        Generic.

??? question "R5. Which DDD relationship pattern protects you from a messy legacy model?"
    ??? success "Answer"
        Anti-corruption layer.

??? question "R6. Reference other aggregates by ___?"
    ??? success "Answer"
        Identity.

??? question "R7. What makes a value object a value object?"
    ??? success "Answer"
        Immutability and equality by attributes, no identity.

??? question "R8. Outbox delivery semantics?"
    ??? success "Answer"
        At-least-once; consumers dedupe (idempotent).

??? question "R9. Why not 2PC across services?"
    ??? success "Answer"
        Blocking locks, coordinator failure, reduced availability, unsupported by most services.

??? question "R10. Saga compensation for 'charge card'?"
    ??? success "Answer"
        Refund/void — but ideally make charge the pivot so it isn't compensated; earlier steps are the compensatable ones.

??? question "R11. Command vs event naming?"
    ??? success "Answer"
        Commands are imperative (`ReserveCapacity`); events are past tense (`CapacityReserved`).

??? question "R12. CQRS Level 1 means?"
    ??? success "Answer"
        Reads bypass the domain model and query optimised SQL/views on the same DB.

??? question "R13. Event sourcing's biggest long-term cost?"
    ??? success "Answer"
        Event schema evolution (plus projections and PII erasure).

??? question "R14. Broker vs mediator topology?"
    ??? success "Answer"
        Choreography (no central coordinator) vs orchestration (central mediator).

??? question "R15. Claim check pattern?"
    ??? success "Answer"
        Store the large payload elsewhere; pass a reference in the message.

??? question "R16. Strongest integration strength level?"
    ??? success "Answer"
        Intrusive coupling (using another component's internals).

??? question "R17. Balanced coupling rule of thumb?"
    ??? success "Answer"
        Strong coupling only at low distance; high distance needs contract-level coupling — unless the parts are stable.

??? question "R18. The two events of expand/contract?"
    ??? success "Answer"
        Add new alongside old (expand), then remove old after consumers migrate (contract) — with a migrate phase between.

??? question "R19. Hyrum's Law in one line."
    ??? success "Answer"
        With enough users, every observable behaviour of your API will be depended on by somebody.

??? question "R20. C4 'container' means?"
    ??? success "Answer"
        A separately runnable/deployable unit (app, service, database, broker) — not necessarily a Docker container.

??? question "R21. Inverse Conway Maneuver?"
    ??? success "Answer"
        Shape teams deliberately so the desired architecture emerges.

??? question "R22. Which team type reduces others' cognitive load with a self-service product?"
    ??? success "Answer"
        Platform team.

??? question "R23. Why must an ADR list negative consequences?"
    ??? success "Answer"
        To be an honest trade-off record rather than advocacy, and to define what to monitor.

??? question "R24. Name the three legs of the lethal trifecta."
    ??? success "Answer"
        Access to private data, exposure to untrusted content, ability to communicate externally.

??? question "R25. Where do business invariants belong when an LLM proposes an action?"
    ??? success "Answer"
        In the domain model/service that executes the command — never only in the prompt.
