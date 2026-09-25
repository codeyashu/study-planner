---
title: "Multi-region, DR & failover"
track: system-design
slug: multi-region-dr
priority: P1
complexity: 4
est_hours: 3
phase: 5
tags: [system-design, P1]
last_reviewed: 2026-09-25
---

# Multi-region, DR & failover

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 4/5 · **Est. time:** 3 h · **Phase:** 5 · **Prereqs:** [Replication](replication.md), [Consistency models](consistency-models.md), [Reliability patterns](reliability-patterns.md)
    **You're done when:** you can map RPO/RTO to DR strategies (backup-restore, pilot light, warm standby, active-active), design data and traffic layers for multi-region, explain static stability and cell-based architecture, and reason about residency, cost and AI-specific concerns (GPU capacity, model availability, data sovereignty).

## Why it matters

"Multi-region" is one of the most over-requested and under-analysed requirements. Executives hear "active-active" and imagine free resilience; engineers know it multiplies complexity (data consistency, conflict resolution, operational load, cost 2–3×). A Staff engineer's job is to translate business impact (cost per hour of downtime, regulatory requirements, latency needs) into an **explicit RPO/RTO tier**, pick the *least complex* architecture that meets it, and make sure the failover actually works via rehearsals. Most regional outages that hurt customers involved failover mechanisms that had never been exercised, or control-plane dependencies that failed alongside the region.

AI adds specific pressures: **GPU capacity is regional and scarce** (you can't autoscale H100s into a failover region on demand), model/endpoint availability differs by region, data residency laws constrain where prompts, embeddings and logs may live, and provider quotas are per-region.

## Core concepts

### RPO, RTO and the DR spectrum

- **RPO:** how much data you can lose (time). **RTO:** how long you can be down. **MTTR** and **blast radius** complement them. Derive them from business impact analysis, per system tier (ledger vs recommendations).

| Strategy | RPO | RTO | Cost | Notes |
|---|---|---|---|---|
| **Backup & restore** | hours | hours–days | $ | Cross-region backups; the baseline everyone needs regardless |
| **Pilot light** | minutes | tens of minutes–hours | $$ | Data replicated continuously; core infra minimal, scale up on failover |
| **Warm standby** | seconds–minutes | minutes | $$$ | Scaled-down full stack running; scale up and switch traffic |
| **Active-active (multi-site)** | ~0 to seconds | ~0 to minutes | $$$$ | Both regions serve traffic; requires data design for concurrent writes |

(AWS Well-Architected DR whitepaper terminology.) Availability targets: single region with 3 AZs typically reaches 99.9–99.99%; going beyond that with regions is justified only when region-level failure risk × business impact exceeds the added cost and complexity. Region-wide outages of a major cloud are rare but do occur (usually via control plane, networking or a bad deploy/config), and many recent "regional" events were actually **global control-plane or dependency failures** that multi-region deployment within the same provider wouldn't fix.

### Data layer patterns

| Pattern | Write path | Consistency | Failure behaviour |
|---|---|---|---|
| **Primary/replica cross-region (async)** | Single write region | Reads stale in secondary | Failover loses replication-lag worth of data (RPO = lag); manual/approved promotion |
| **Synchronous cross-region quorum (Spanner-like)** | Global consensus | Strong | Higher write latency (RTT to a quorum); survives region loss without data loss |
| **Partitioned active-active (home region per tenant/entity)** | Each entity has a home region | Strong within partition; async replicas elsewhere | Failover moves partition leadership; small RPO risk |
| **Multi-writer with conflict resolution** | Any region | Eventual (CRDT/LWW) | Conflicts; suits specific data types only |
| **Global tables (DynamoDB, Cosmos DB multi-write)** | Any region | Eventual with LWW | Simple but silent conflicts on concurrent writes |

Guidance: prefer **single-writer-per-entity** designs (home region, cell) over true multi-writer for anything with invariants. Use **async replication + reconciliation** for tolerable-RPO data; use **consensus stores** for small critical control data (leader/routing tables); use **object storage cross-region replication** for blobs (RTC/replication time control gives an SLA). See [Replication](replication.md) and [Consistency models](consistency-models.md).

Also protect against **logical corruption**: replicas copy bad deletes/migrations instantly. Keep point-in-time recovery and immutable backups (object lock) in a separate account/region.

### Traffic layer

- **Global routing:** GeoDNS/latency-based DNS with health checks (slow because of TTL caching), **anycast** (fast failover, handled by CDN/edge), or global load balancers (Azure Front Door, Cloudflare, Google Cloud Global LB). Prefer anycast/global LB for fast failover; keep DNS TTLs low (30–60 s) but don't rely on clients honouring them.
- **Health checks that reflect user-visible health** (synthetic transactions through the full path), with hysteresis to avoid flapping. Beware failover **stampedes**: shifting 100% of traffic to a warm-standby region that is scaled to 30% capacity causes an overload outage. Pre-scale, shift gradually, or keep headroom (N+1 regions with each region sized to absorb failed region's share).
- **Session/state affinity:** stateless services with externalised state; tokens (JWT) valid across regions; regional caches warmed or tolerant of cold start (see [Caching](caching.md)).
- **Client-side failover** (SDKs with multiple endpoints) is fast and independent of DNS but needs client updates.

### Static stability, control planes and cells

- **Static stability (AWS):** systems keep working when dependencies (especially control planes) are impaired; pre-provision capacity across AZs so failover doesn't require *creating* resources during the outage (when everyone else is also calling the control plane). Data plane vs control plane split: recovery paths must rely on data-plane operations only (e.g. Route 53 ARC routing controls/data-plane health checks rather than API calls to change records during an event).
- **Cell-based architecture:** partition the fleet into independent, identical cells (full stack), each serving a slice of customers, with a thin routing layer above. Blast radius = 1/N; deploy to one cell at a time; failures and poison requests contained; a cell can be evacuated. Slack and AWS have public write-ups. Combine with **shuffle sharding**.
- **Dependency mapping:** the failover region must not depend on the failed region for auth, config, secrets, DNS, container registry, CI/CD, observability, or feature flags. Discover these by game days: block the primary region in a controlled test.
- **Bulkhead the global services** (identity, routing, config) — they're the true single points of failure in "multi-region" designs.

### Testing and operations

- **Failover is a product feature you must rehearse:** scheduled game days (quarterly) with real traffic shifts, runbooks that are executable and version-controlled, automated where safe, RTO/RPO measured not assumed. Untested DR = no DR.
- **Chaos and fault injection** at region level (block traffic, throttle replication) plus dependency failure injection.
- **Failback** is often harder than failover (data reconciliation back to the recovered region); plan it explicitly.
- **Deployment safety:** progressive delivery across regions (one region at a time with bake time) so a bad release doesn't take all regions down simultaneously; multi-region is not resilience if every region runs the same change at the same second.
- **Cost:** active-active roughly doubles compute and adds inter-region transfer; warm standby ~30–60%; pilot light ~10–20% (order-of-magnitude). Weigh against expected loss.

### Data residency and sovereignty

Regulations (GDPR transfers, India DPDP, China, sector rules) may require data to stay in a jurisdiction. Architecture responses: **regional deployments (cells per jurisdiction)** with tenant homing, no cross-border replication of personal data (or only pseudonymised/aggregated), regional key management (KMS/HSM per region, customer-managed keys), regional logging/observability stores, and clear rules for support access. This sometimes conflicts with DR (can't fail over EU data to the US): design DR *within* the jurisdiction (multiple EU regions).

### AI/LLM specifics

- **GPU capacity and quotas are regional:** capacity reservations or provisioned throughput in the DR region cost real money whether used or not; test whether the DR region can actually obtain the GPUs. Plan degraded modes: smaller models, lower concurrency, queueing for batch, or routing to hosted APIs when self-hosted GPU capacity is unavailable.
- **Model availability and versions vary by region/provider** (some models launch in select regions only); keep model routing configuration region-aware and tested; fallback models need eval coverage so quality in failover mode is known.
- **State replication:** vector indexes (rebuildable from raw documents, or replicate index snapshots), conversation history/memory stores (RPO matters to users), agent checkpoints (durable execution state must be in the replicated store; in-flight runs resume or restart in the DR region by design), prompt/config registries.
- **Data flows to model providers:** prompts and documents sent to a provider endpoint in another region may violate residency; use regional endpoints (e.g. EU data zones) and confirm zero-data-retention terms.
- **Gateway layer:** an LLM gateway with multi-region provider deployments and health-based routing is a natural DR control point ([LLM gateway](../ai-system-design/llm-gateway.md)).

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [AWS — Disaster recovery of workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) | docs | Clear definitions of backup/restore, pilot light, warm standby, active-active with RTO/RPO framing | intermediate | free |
| [AWS Builders' Library — Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) :gem: | article | Control-plane vs data-plane thinking; the mindset behind resilient failover | advanced | free |
| [AWS — Reducing scope of impact with cell-based architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) | docs | Cells, routing layer, sizing, shuffle sharding | advanced | free |
| [Slack — Slack's migration to a cellular architecture](https://slack.engineering/slacks-migration-to-a-cellular-architecture/) :gem: | article | Real-world migration and the incident that motivated it | intermediate | free |
| [Spanner: Google's globally distributed database](https://research.google/pubs/spanner-googles-globally-distributed-database-2/) | paper | Synchronous multi-region consensus and TrueTime trade-offs | advanced | free |
| [GitHub — October 21 post-incident analysis](https://github.blog/2018-10-30-oct21-post-incident-analysis/) | article | What cross-region failover with async replication really costs | advanced | free |
| [Azure Cosmos DB consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) | docs | Multi-region consistency options in a managed system | intermediate | free |
| [Marc Brooker's blog](https://brooker.co.za/blog/) | article | Concise essays on availability math, correlated failures and blast radius | advanced | free |

## Hands-on lab

**Goal:** run a failover drill between two "regions" and measure RPO/RTO (2 h).

1. Simulate regions with two docker-compose stacks (or two Kubernetes namespaces/kind clusters): app + Postgres primary in `region-a`, async streaming replica + warm app in `region-b`, MinIO with bucket replication, and a front proxy (Envoy/Traefik) doing health-checked weighted routing.
2. Generate load (k6 at 100 RPS of writes+reads with a client-side record of acknowledged writes).
3. Kill `region-a` (stop containers / block network with `iptables` or `tc`). Measure detection time, time to promote the replica, time until traffic succeeds (RTO), and count acknowledged writes missing in `region-b` (RPO).
4. Repeat with `synchronous_commit` quorum to a replica and compare RPO and write latency (add 60 ms latency with `tc netem` to emulate cross-region).
5. Bonus: demonstrate a failover stampede — route 100% traffic to a standby sized for 30% and observe the overload; fix with gradual shifting and load shedding.
6. Write the runbook and a one-page "DR tier" table for the capstone system.
7. **Expected output:** RTO of tens of seconds to minutes depending on automation; RPO > 0 for async and 0 for sync (with higher latency); stampede overload reproduced and mitigated.

## Questions

### L1 — Recall

??? question "Q1. Order the DR strategies by cost and recovery speed."
    ??? success "Answer"
        Backup & restore (cheapest, slowest: RPO hours, RTO hours–days), pilot light (data replicated, minimal compute; RTO tens of minutes+), warm standby (scaled-down full stack; RTO minutes), active-active (full capacity in multiple regions; RTO near zero, highest cost and complexity).

??? question "Q2. What is static stability?"
    ??? success "Answer"
        A design principle where a system continues operating in its current state despite dependency or control-plane failures — e.g. capacity is pre-provisioned across AZs/regions so recovery doesn't require launching new resources or calling impaired control-plane APIs during the failure.

??? question "Q3. What is a cell-based architecture and its main benefit?"
    ??? success "Answer"
        Partitioning the system into independent, identical, fully isolated stacks (cells) that each serve a subset of customers, behind a thin router. The main benefit is bounded blast radius: a failure, bad deploy or poison workload affects only one cell (1/N of customers) and can be contained or evacuated.

??? question "Q4. Why isn't replication a backup?"
    ??? success "Answer"
        Replication faithfully copies every change, including accidental deletes, corruption and malicious writes, within seconds. Backups (point-in-time, immutable, separately controlled) allow restoring to a state before the damage.

### L2 — Apply

??? question "Q5. The business states RPO 5 min and RTO 30 min for the order service. Choose a strategy and data replication setup."
    ??? success "Answer"
        Warm standby (or pilot light with well-automated scale-up) in a second region. Data: async cross-region replication with lag SLO < 60 s (alerts at 2 min) → RPO < 5 min; PITR backups for corruption. Infra as code so the standby stack is identical; autoscaling pre-warmed to ~50% of peak; routing via global LB with health checks and a documented promotion runbook (approved by an incident commander) to avoid split-brain; quarterly failover drills to verify RTO < 30 min and measure actual RPO. Manage dependencies (secrets, DNS, identity, registry) in the standby region.

??? question "Q6. Your failover test overloaded the standby region, causing a secondary outage. What went wrong and how do you fix it?"
    ??? success "Answer"
        Capacity mismatch and abrupt traffic shift: standby was scaled to a fraction of primary, caches were cold, DB connection pools were small, and 100% of traffic arrived at once (stampede). Fixes: pre-scale/reserved capacity to at least the peak share it must absorb; shift traffic gradually (10/25/50/100%) with health checks; warm caches (replicate or pre-load hot keys); apply load shedding and priority controls during failover; validate connection limits and quotas (including cloud service quotas per region) beforehand; make load tests in the standby region part of DR readiness.

??? question "Q7. An LLM feature must survive loss of the region hosting your self-hosted GPU cluster. What's your plan?"
    ??? success "Answer"
        Tiered approach: (1) active provider-hosted fallback (multi-region managed endpoints) reachable through the gateway with pre-tested prompts and evals for the fallback model; (2) reserved or provisioned GPU capacity in a second region sized for the critical subset of traffic (interactive), with batch workloads paused; (3) model artefacts pre-replicated to the second region's storage and image registry; (4) degraded modes (smaller model, shorter context, retrieval-only answers). Test by draining the primary GPU pool and measuring quality and latency in failover mode; document the capacity you can obtain in the DR region (quota, availability).

### L3 — Design & trade-offs

??? question "Q8. Active-active vs active-passive for a customer-facing booking platform with 99.99% target."
    ??? success "Answer"
        99.99% (~4.3 min/month) is very tight; an active-passive design with minutes-scale RTO can't fit a regional event within one month's budget, though such events are rare. First check whether the budget is dominated by regional failures (rare) or by deploys and dependencies (frequent) — often the latter, addressed by cells, progressive delivery and better dependency handling rather than active-active. If regional resilience is needed: partitioned active-active (each booking has a home region; users routed to the nearest; failover moves partition leadership) keeps writes single-writer per entity while providing regional capacity; synchronous replication only for the tiny critical dataset. Avoid multi-writer LWW for bookings. Cost and complexity are high; justify with expected loss per hour of downtime.

??? question "Q9. How do you handle data residency (EU customer data stays in the EU) while offering DR?"
    ??? success "Answer"
        Treat the EU as a self-contained deployment (its own cells/regions): DR must be between EU regions (e.g. Frankfurt ↔ Ireland), not to the US. Tenant homing assigns customers to jurisdictions at onboarding; control plane and global services hold only non-personal metadata or are duplicated per jurisdiction; encryption keys per region under customer/regional control; logs, traces and LLM prompts stay in-region (regional provider endpoints, region-scoped observability). Cross-border access for support is via audited, just-in-time processes. Document the data flow map and verify with automated checks.

??? question "Q10. Which parts of an LLM/RAG system need replication to a DR region, and what can be rebuilt?"
    ??? success "Answer"
        Replicate: source documents/raw artefacts (object storage replication), metadata/ACL DB (async replica or quorum), conversation/memory stores and agent checkpoints (per RPO), prompt/config/eval registries. Rebuildable: vector indexes and search indexes (from raw documents/parsed artefacts) — but rebuild time may exceed the RTO, so replicate index snapshots or maintain a warm replica for large corpora; caches; embeddings caches (optional). Model artefacts replicated for self-hosted models. Decide per component using RTO: if rebuilding a 100M-vector index takes 20 h and RTO is 1 h, replicate the index.

### L4 — Staff-level ambiguity

??? question "Q11. The CEO read about a cloud regional outage and demands 'multi-region for everything by Q4'. How do you respond?"
    ??? success "Answer"
        Convert to a business-impact conversation: classify systems by tier with cost of downtime, regulatory requirements and current measured availability. Show root causes of last year's incidents (most are deploys, dependencies, capacity, not region loss) and the cost/complexity of full multi-region. Propose a tiered plan: Tier 0 (payments, identity, order intake) get warm-standby or partitioned active-active with rehearsed failover; Tier 1 gets pilot light/backup-restore with clear RPO/RTO; Tier 2 gets backup only. Fund foundational work first (IaC parity, dependency mapping, cross-region backups, progressive regional deploys, game days) since it benefits all tiers. Present cost, staffing and timeline with milestones, and success metrics (drill-verified RTO/RPO). This turns an abstract mandate into an investable roadmap.

??? question "Q12. A failover drill succeeded technically but revealed that 14 hidden dependencies (auth provider, config service, CI, secrets) lived only in the primary region. How do you fix systemically?"
    ??? success "Answer"
        Build a dependency inventory using the drill findings plus tracing/network flow data; classify each as global, regional, or single-region and assign owners. Establish an architecture rule: any Tier-0 dependency must have a documented multi-region story or a tested degradation mode; add DR-readiness checks to launch reviews and to the service catalogue. Automate "region isolation" tests in staging (block a region's egress/ingress) as a CI-like periodic job. Prioritise the dependencies by criticality: identity, secrets, config/feature flags, DNS, artefact registry, observability. Track progress on a shared dashboard; repeat drills until no cross-region hidden dependency remains. Record decisions as ADRs.

## Real-world use cases

- **AWS/Slack:** cellular architectures to limit blast radius.
- **Google Spanner users (Ads):** synchronous multi-region with explicit latency budget.
- **GitHub 2018:** partition and async-replication failover with data reconciliation.
- **Logistics platforms:** tracking APIs active-active read-only globally; booking writes partitioned by trade lane/region with warm standby.
- **LLM products:** provider/region fallbacks via gateway; reserved GPU capacity only for critical interactive tiers.

## Pitfalls & anti-patterns

- Declaring "multi-region" without measuring RPO/RTO or rehearsing failover.
- Active-active multi-writer for data with invariants.
- Standby sized too small; failover stampedes; cold caches.
- Hidden global dependencies (identity, config, DNS, registry, CI/CD).
- Deploying to all regions simultaneously.
- Replication treated as backup; no immutable backups.
- Ignoring residency law in DR design; ignoring GPU quota in AI DR.

## Checklist

- [ ] I can map RPO/RTO to a DR strategy and cost tier
- [ ] I can design the data and traffic layers for multi-region with residency constraints
- [ ] I ran a failover drill and measured RTO/RPO
- [ ] I can explain static stability, cells and dependency mapping
- [ ] I answered all L3 questions out loud in < 3 min each
