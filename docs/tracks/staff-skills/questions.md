---
title: Staff+ Skills — Question bank
track: staff-skills
last_reviewed: 2026-09-25
---

# Staff+ Skills — Question bank

Cross-topic questions that complement the per-page questions. Levels follow the repo scale: L1 recall, L2 apply, L3 judgement and trade-offs, L4 org-level ambiguity. Answer aloud first, in under three minutes for L3/L4, then open the model answer. Behavioral prompts (marked **Behavioral**) should be answered from your own story bank, so the model answer shows structure, not content.

Topic pages: [archetypes](staff-archetypes.md) · [strategy](technical-strategy.md) · [design docs](design-docs-rfcs.md) · [influence](influence-without-authority.md) · [debt](technical-debt.md) · [mentoring](mentoring-sponsorship.md) · [incidents](incident-leadership.md) · [communication](communication-stakeholders.md) · [decisions](decision-making.md) · [reviews](architecture-reviews.md) · [AI-era](ai-era-leadership.md) · [behavioral](behavioral-interviews.md)

## Part 1 — Graded questions

### L1 — Recall

??? question "G1. Which four archetypes does Larson describe, and which one fits cross-team domain direction best?"
    ??? success "Answer"
        Tech Lead, Architect, Solver, Right Hand. Architect fits cross-team domain direction and quality best; it is the natural home of an AI architect owning an agent platform.

??? question "G2. What are the three parts of a good strategy (Rumelt)?"
    ??? success "Answer"
        Diagnosis, guiding policy, coherent actions. A strategy without a diagnosis or without policies that rule things out is a goal list.

??? question "G3. What is an ADR and when is it written?"
    ??? success "Answer"
        A short record of one decision: context, decision, consequences, status. Written at decision time and kept with the code so future engineers know why, not just what.

??? question "G4. What is BLUF?"
    ??? success "Answer"
        Bottom Line Up Front: conclusion or ask in the first sentence, supporting detail after. It lets busy executives get the message immediately.

??? question "G5. Distinguish mentoring from sponsoring."
    ??? success "Answer"
        Mentoring is advice given to a person; sponsoring is spending your reputation to create opportunities for them in rooms they are not in. Sponsorship moves careers more.

??? question "G6. What does blameless mean in a postmortem?"
    ??? success "Answer"
        Assume people acted reasonably with what they knew and fix the system that allowed the failure. Accountability remains for the fixes, not for blame.

??? question "G7. What are Type 1 and Type 2 decisions?"
    ??? success "Answer"
        Type 1 is hard to reverse (one-way door): deliberate, senior input. Type 2 is cheap to reverse (two-way door): decide fast and learn.

??? question "G8. What are the four DORA delivery metrics?"
    ??? success "Answer"
        Lead time for changes, deployment frequency, change-failure rate, and time to recover from a failed deployment. Use them as outcome measures for AI adoption instead of usage counts.

??? question "G9. What is the lethal trifecta?"
    ??? success "Answer"
        Private data access, exposure to untrusted content, and the ability to communicate externally, all in one agent. Together they enable prompt-injection exfiltration; remove one leg or add strong controls.

??? question "G10. What does DORA 2025 mean by AI as an amplifier?"
    ??? success "Answer"
        AI magnifies an organisation's existing strengths and weaknesses, so returns depend on the underlying system (small batches, platforms, clear stance, tests), not only on the tool.

### L2 — Apply

??? question "G11. Rewrite 'We will improve reliability and adopt AI responsibly' as strategy policies."
    ??? success "Answer"
        Ground it in diagnosis (e.g., 9 SEV2s last half, 60% from unreviewed config changes; three ungoverned LLM integrations). Policies: "All tier-1 config changes ship via canary rather than direct rollout"; "All model access goes through the gateway rather than direct provider keys"; "No AI feature launches without an offline eval suite and online monitoring." Each rules something out and ties to evidence.

??? question "G12. Write a TL;DR (5 lines) for an RFC to standardise OpenTelemetry across services, including GenAI spans."
    ??? success "Answer"
        Problem (triage takes 47 min because traces break across 3 stacks), proposal (OTel SDK + collector standard, GenAI spans for LLM/tool calls with a note that GenAI conventions are still in development status), key trade-off (migration effort ~2 eng-weeks per service vs faster triage, vendor independence), expected result (median triage under 20 min), ask (approve phase 1 for 10 tier-1 services by date).

??? question "G13. Score two debt items: a hideous 2015 module untouched for 2 years, and a moderately messy pricing module changed weekly and tied to 4 incidents."
    ??? success "Answer"
        The pricing module wins by a wide margin: interest (frequent change, incidents) and reach are high. The old module has near-zero interest despite its ugliness. Fix hotspots (churn times complexity), not eyesores.

??? question "G14. Give a delegation-level statement for a mentee owning an RFC."
    ??? success "Answer"
        "You own this RFC end to end at level 3: I'll review the alternatives section before circulation and join the first stakeholder meeting; after that you present and decide, and I'm the escalation path."

??? question "G15. Draft the first 15 minutes of an IC's actions for a SEV1 booking outage."
    ??? success "Answer"
        Declare SEV1, assign ops lead, comms lead, scribe; state impact hypothesis; ask for the fastest safe mitigation (rollback of last change, failover, flag off) before diagnosing; first status update with next-update time; page owners of the suspected dependency; keep a timeline.

??? question "G16. Translate for a CFO: 'Our RAG pipeline needs reranking and a semantic cache.'"
    ??? success "Answer"
        "Two changes would raise answer accuracy from about 82% to 92% on our test set while cutting model spend 20-30% (~$X a month): one-off cost 6 engineer-weeks; payback under a quarter. We'll report accuracy and cost monthly."

??? question "G17. Build tripwires for a decision to pilot an autonomous rebooking agent."
    ??? success "Answer"
        Pause if: any unauthorised customer-impacting action; human-override rate above 20% over a week; cost per rebooking above threshold; eval accuracy on the held-out set below 97%; more than N customer complaints. Owner named for each with authority to stop the agent.

??? question "G18. Which review-checklist items must an agent that reads customer emails and amends bookings trigger?"
    ??? success "Answer"
        Prompt-injection threat model (untrusted input x private data x external action), HITL for amendments, least-privilege scoped credentials, audit log, kill switch, adversarial eval set, data-flow and residency to the model provider, cost caps, non-AI fallback queue.

??? question "G19. How would you measure whether a coding agent helps a 40-person department?"
    ??? success "Answer"
        Baseline a quarter of DORA metrics, review time, PR size, developer experience survey; staggered team rollout for natural controls; guardrails (incidents per change, security findings); review at 6 and 12 weeks; avoid acceptance rate or lines generated; investigate outlier teams.

??? question "G20. Convert 'I was on-call for a big outage' into a Staff-level STAR opening line."
    ??? success "Answer"
        "I led the response to a 90-minute EU booking outage during peak season, then drove the change that moved 40 services to canary deploys, cutting SEV2s from configuration by roughly half over two quarters." It states scope, role, and durable outcome.

### L3 — Design and trade-offs

??? question "G21. Central platform team vs federated enablement for AI in a 600-engineer company."
    ??? success "Answer"
        Hybrid: a small platform team owns the thin risk-bearing layer (gateway, identity, logging, eval harness, reference tools, policy) as a paved road; product teams own use cases, prompts, domain tools and their evals. Pure central becomes a bottleneck; pure federated duplicates stacks and leaks risk. Centralise first what security and spend demand.

??? question "G22. Mandate or persuade for adopting a shared gateway?"
    ??? success "Answer"
        Paved road first, mandate later. Seek a mandate for existential or regulatory risk (data leakage), strong network effects (identity, logging), or after persuasion fails and divergence is costly. Even with a mandate, do the persuasion work to avoid malicious compliance.

??? question "G23. Rewrite vs strangler for a 12-year-old monolith."
    ??? success "Answer"
        Default to strangler: carve seams by bounded context, route new capability to new services, shadow traffic and contract tests, keep delivering. Rewrites lose hidden behaviour and defer value. Rewrite only small, well-understood systems or platforms with no seams. Agents make characterisation tests and slice migrations cheaper, not riskless.

??? question "G24. Gatekeeping ARB vs advice process."
    ??? success "Answer"
        Gate for irreversible, regulated or safety-critical choices; advice process (seek advice from affected parties and experts, record as ADR) for the rest. Most enterprises need the hybrid, with published triggers and a five-day SLA so teams do not route around review.

??? question "G25. One approved coding agent or team choice?"
    ??? success "Answer"
        One or two approved tools with enterprise data controls, an evaluation path to add more, and tool-agnostic repo conventions (AGENTS.md). Single tool eases security, training and measurement; open choice fragments cost and review and encourages shadow AI.

??? question "G26. Consensus vs single decider."
    ??? success "Answer"
        A named decider with required consultation: faster and clearer than consensus, which gives everyone a veto. Use broader consent only for standards everyone must live with. Record advice and dissent in the ADR.

??? question "G27. How do you make a multi-year vendor decision more reversible?"
    ??? success "Answer"
        Standardise on seams (gateway, MCP, OTel, SQL), keep data and evals portable, phase adoption, shorten terms or add exit clauses, run in parallel for a period, and set revisit triggers dated in the ADR.

??? question "G28. Async review vs live design review for a global team."
    ??? success "Answer"
        Async first with a deadline (respects time zones, leaves a record), then a short live session only for unresolved issues with the decider present; rotate meeting times for fairness. Live-only excludes regions; async-only can stall.

??? question "G29. Capacity-allocated debt work vs named projects."
    ??? success "Answer"
        Use both. Allocation for small local tidy-ups and toil; named projects with business cases and metrics for high-interest, cross-cutting items. Allocation alone is diffuse and easily raided; projects alone ignore the steady trickle.

??? question "G30. Should juniors work without agents at all?"
    ??? success "Answer"
        Not entirely, but deliberately protect fundamentals: some tasks without agents, requirement to explain any submitted code, review of agent diffs line by line together. The aim is judgement: knowing when output is wrong and why, while still building agent fluency.

### L4 — Staff-level ambiguity

??? question "G31. You join with no defined project and three directors each want you. First 60 days?"
    ??? success "Answer"
        Confirm sponsor and their top risk; listen for 3-4 weeks; score problems on impact, urgency, need for cross-team work, and who else could do it; write an options memo with a recommendation and a plan for the other two; have your manager announce the choice. Revisit quarterly.

??? question "G32. The CTO wants an AI strategy in three weeks with no budget or owner and five builds in flight."
    ??? success "Answer"
        Clarify scope and decisions wanted; week 1 discovery (inventory, spend, incidents, 10 interviews); week 2 draft diagnosis and 5-6 policies, pre-wire team leads and security, grandfather in-flight builds with a migration path; week 3 present options for org model and funding with a recommendation and asks (owner, budget, mandate). Flag v1 will be tested on real decisions.

??? question "G33. Leadership says 'no debt work, only features' while the platform degrades."
    ??? success "Answer"
        Translate into delivery terms: show trend data on lead time and incident cost, bundle debt into feature work, pick one item with a hard deadline (security, EOL, compliance) and obtain explicit signed risk acceptance for the rest, use tidy-first in normal work, report leading indicators monthly.

??? question "G34. CEO mandates '50% of code written by AI'."
    ??? success "Answer"
        Find the goal behind it (speed, cost, signal). Explain that share-of-code is gameable and uncorrelated with outcomes; offer outcome targets (lead time, throughput at stable change-failure rate, developer experience), with AI share as a secondary indicator. Position it as protecting the CEO from a metric that invites bloat.

??? question "G35. Leadership wants to hire fewer juniors because agents do junior work."
    ??? success "Answer"
        Acknowledge real automation of routine tasks, then argue the pipeline risk: no juniors today means few seniors in 3-5 years, and agent output still needs people who understand the system. Propose fewer but deliberately developed juniors with apprenticeship pairing and fundamentals plus agent fluency, and track time-to-productivity.

??? question "G36. A high-performing product team shipped an AI feature that bypassed review and the gateway standard."
    ??? success "Answer"
        Assess active exposure first and contain if any. Then 1:1 to learn why (slow review, unawareness, deadline), agree a dated remediation, fix the systemic cause, log the exception, and escalate jointly with a crisp risk statement only if remediation stalls. No public shaming.

??? question "G37. Two VPs sponsor competing platform strategies (single vendor vs open source)."
    ??? success "Answer"
        Reframe from vendor vs OSS to the diagnosis; get both to agree criteria and weights before scoring; time-boxed bake-off on one real use case with a shared eval set; likely layered outcome (managed where commodity, open standards at seams, own evals and domain tools); present reversibility and let the accountable exec decide; record as ADR.

??? question "G38. An AI agent with write access made 200 wrong shipment updates after a prompt injection; leadership wants all agent work stopped."
    ??? success "Answer"
        Contain and remediate first (disable, revoke, restore data, follow the security process). Postmortem on design: untrusted input plus private data plus write access, no HITL or scoped permissions. Offer a risk-tiered policy instead of a ban: read-only and HITL agents continue; autonomous write agents paused until controls (least privilege, HITL, red team, kill switch) pass review.

??? question "G39. Three teams built three RAG stacks. Propose convergence."
    ??? success "Answer"
        Do not mandate one stack. Converge on seams: gateway, eval harness, tool/MCP registry, trace conventions; let teams keep frameworks above them. Pilot with the most willing team, publish results, offer migration help for others, set a dated target with a dashboard, and retire duplicates after a grace period.

??? question "G40. **Behavioral:** Tell me about a time you changed another team's technical direction."
    ??? success "Answer"
        Structure: stakes and why it was yours; their interests, not positions; the artifact (doc, prototype, data) that shifted the conversation; pre-wiring; what you conceded; measurable outcome; how you gave credit; what you would change. Avoid stories won by escalation alone.

## Part 2 — Scenario questions (org situations)

Each scenario gives a realistic situation and asks for a decision. Spend two minutes outlining your answer before opening.

??? question "S1. Your manager says you operate at Senior+, not Staff. Six months to the next cycle. What do you do?"
    ??? success "Answer"
        Ask for the specific gap and an example of someone who meets the bar; pick one unowned cross-team Staff project tied to a business outcome (for example, converging LLM access on a gateway with evals); write the design or strategy doc within three weeks; delegate implementation to seniors you grow; give monthly exec updates; keep a brag doc; review evidence against the rubric at day 90 and again at month 5.

??? question "S2. A security lead blocks every AI proposal after a vendor data incident last year. You need them on side."
    ??? success "Answer"
        Meet 1:1 to learn what would make them comfortable; convert their concerns into design requirements (data classification enforced in the gateway, logging, residency, approved-model list); give them ownership of policy rules; offer pre-approved reference architectures that shorten review; show a small pilot with controls. Their veto on data rules is a feature, not a cost.

??? question "S3. Your team's review queue has doubled since agents arrived; quality complaints rising."
    ??? success "Answer"
        Treat as a system problem: repo agent rules (AGENTS.md), PR size limits, tests required on changed code, CI gates and scans, agent pre-review so humans focus on design and risk, and metrics on review time and change-failure rate. Consider rotating a review captain. Do not just add reviewers.

??? question "S4. A model provider announces deprecation of the API version your five services use, with 90 days notice."
    ??? success "Answer"
        Inventory usage via gateway logs, put the deprecation in the debt register with a hard date, migrate behind the gateway once rather than five times, use the eval suites to check quality on the replacement (this is where teams without evals suffer), canary the switch, and write the lesson into policy: pinned versions with a lifecycle register.

??? question "S5. Two senior engineers on your project have fallen out and it is slowing delivery. Neither reports to you."
    ??? success "Answer"
        Talk to each privately about interests and what they need; avoid taking sides; restructure work so their interfaces are contract-based and decisions have a named decider; if it persists after good-faith attempts, tell their manager with specific delivery impact, not personality complaints. Keep records.

??? question "S6. A director asks you to lead an initiative you believe is a low-value vanity project."
    ??? success "Answer"
        Clarify the goal behind it; propose an alternative that meets the goal at higher value or a smaller scoped version; quantify opportunity cost against your existing bets; if the decision stands, decide whether it serves your sponsor relationship, time-box it, and delegate. Say no with options, never a flat refusal.

??? question "S7. Your postmortem action items from the last four incidents are 30% complete."
    ??? success "Answer"
        Reduce to 3-7 actions per incident, each owned, dated and in the normal backlog; hold a monthly operational review that tracks completion; drop actions nobody will do; aggregate themes across incidents into a reliability investment ask to leadership.

??? question "S8. A newly hired principal engineer from a big-tech company insists on rebuilding your CI on their preferred tooling."
    ??? success "Answer"
        Ask them for the diagnosis: which measured problem does it solve? Agree on evidence and a small pilot; separate reversible tooling preferences from real gaps; involve the platform owners; if the case is strong, help write the RFC with them; if not, agree a revisit trigger. Respect experience while requiring the same evidence as anyone.

??? question "S9. Your exec sponsor wants a demo of an autonomous agent next week; the system has no evals and the eval work is unfinished."
    ??? success "Answer"
        Offer a demo that is honest: scripted scenarios in a sandbox, clearly labelled as prototype, with the eval plan and timeline shown. Refuse to imply production readiness. Frame it as protecting the sponsor's credibility. Use the demo as the moment to ask for time to finish evals.

??? question "S10. The regional IT team in Asia says the global standard ignores their residency constraints."
    ??? success "Answer"
        Treat it as valid input: meet, document the constraints, check with legal. Adapt the standard through regional deployment or data-handling variants at the seams rather than exceptions, involve them in the design review, credit them publicly, and record the pattern as an approved variant.

??? question "S11. You discover a peer team's agent logs full customer emails to a third-party observability tool."
    ??? success "Answer"
        Escalate to the owning team lead and security promptly and privately, with specifics; recommend immediate mitigation (stop logging bodies, redact) and a check of retention; follow the incident process; later, encourage gateway-level redaction. Do not shame; do not sit on it.

??? question "S12. Product wants to launch an AI assistant next quarter; your eval shows 88% accuracy against a 95% bar."
    ??? success "Answer"
        Present options with numbers: limited launch (low-risk intents only), launch with HITL on all uncertain answers and added reviewer capacity, or delay for targeted improvements; show which failure categories dominate and the effort to close them. Recommend one with tripwires. Let the accountable exec choose and record the risk acceptance.

??? question "S13. You are asked to estimate the cost of a company-wide agent platform. Nobody agrees on usage."
    ??? success "Answer"
        Build a driver-based model (users x tasks x tokens x price, plus platform team, eval, security review, and support costs), with low/base/high scenarios and explicit assumptions; validate with pilot telemetry from the gateway; present ranges and the assumptions that matter most, with a plan to re-estimate quarterly.

??? question "S14. Your best engineer wants to leave for a Staff role elsewhere. You have influence but no authority."
    ??? success "Answer"
        Ask what they want; if it is scope, help create a real Staff-scope project and sponsor them to leadership with evidence; if it is pay or level, advocate to the manager with concrete impact evidence. Do not promise what you cannot deliver, and accept that leaving can be the right outcome.

??? question "S15. Legal asks whether generating code with agents creates licensing or IP exposure. You are the AI architect."
    ??? success "Answer"
        Do not answer legal questions authoritatively; give facts: which tools, vendor IP indemnity and data terms, code-scanning options for licence matches, repo rules. Pair legal with procurement and security to set policy (approved tools with enterprise terms, scans in CI, review of vendor commitments) and date-stamp the policy for review.

## Part 3 — Rapid-fire (20)

One-to-two-sentence answers. Time yourself: 30 seconds each.

??? question "R1. Diagnosis or goals first in a strategy?"
    ??? success "Answer"
        Diagnosis. Goals without diagnosis are wishes.

??? question "R2. What do non-goals do in a design doc?"
    ??? success "Answer"
        Fence scope and surface scope disagreements early.

??? question "R3. Mitigate or diagnose first in an incident?"
    ??? success "Answer"
        Mitigate first if a safe rollback, flag or failover exists.

??? question "R4. What does the IC not do?"
    ??? success "Answer"
        Debug hands-on; the IC coordinates, decides and communicates.

??? question "R5. Interest or position?"
    ??? success "Answer"
        Negotiate on interests; positions produce deadlock.

??? question "R6. What is pre-wiring?"
    ??? success "Answer"
        Sharing the framing 1:1 with key stakeholders before the public review.

??? question "R7. One thing every AI feature needs for incidents?"
    ??? success "Answer"
        A kill switch, plus versioned prompts and models for rollback.

??? question "R8. Why avoid 'percent of code by AI' as a target?"
    ??? success "Answer"
        It is gameable and uncorrelated with outcomes; measure lead time, change-failure rate and experience.

??? question "R9. What is tidy first?"
    ??? success "Answer"
        Small structural improvements made just before the behaviour change that needs them.

??? question "R10. What is a pre-mortem?"
    ??? success "Answer"
        Imagine the decision failed a year later and list why, before committing.

??? question "R11. What is glue work?"
    ??? success "Answer"
        Essential coordination and enabling work; make it visible or it can stall your career.

??? question "R12. What is the 70% rule?"
    ??? success "Answer"
        For reversible decisions, decide with about 70% of the information you would like.

??? question "R13. Meeting or doc for a decision?"
    ??? success "Answer"
        Doc first, async; meeting only for unresolved issues with the decider present.

??? question "R14. What is an SBI feedback structure?"
    ??? success "Answer"
        Situation, behaviour, impact.

??? question "R15. When to escalate?"
    ??? success "Answer"
        When the cost of delay exceeds the relationship cost, ideally jointly with a shared one-page framing.

??? question "R16. Best defence against a vendor benchmark?"
    ??? success "Answer"
        Your own eval set on your tasks in a time-boxed pilot.

??? question "R17. What does 'disagree and commit' need afterwards?"
    ??? success "Answer"
        Full effort and a recorded concern with a revisit trigger, not passive resistance.

??? question "R18. What separates a Staff STAR story from a Senior one?"
    ??? success "Answer"
        Scope beyond your team, self-defined problem, influence without authority, quantified durable outcome.

??? question "R19. How long should a design doc be?"
    ??? success "Answer"
        3-10 pages with an appendix; longer usually means two docs.

??? question "R20. Who needs a sponsor more than a mentor at promotion time?"
    ??? success "Answer"
        Anyone aiming at Staff: someone at director level must advocate for you in calibration.
