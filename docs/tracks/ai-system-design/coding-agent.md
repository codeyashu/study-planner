---
title: Design a coding agent / code-review bot
track: ai-system-design
slug: coding-agent
priority: P1
complexity: 4
est_hours: 3
phase: 5
tags: [ai-system-design, P1]
last_reviewed: 2026-09-25
---

# Design a coding agent / code-review bot

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 4/5 · **Est. time:** 3 h · **Phase:** 5 · **Prereqs:** [Framework](framework.md), [AI-assisted development](../agentic-ai/ai-assisted-development.md), [Tool calling](../agentic-ai/tool-calling.md), [Agent patterns](../agentic-ai/agent-patterns.md), [Guardrails & security](../agentic-ai/guardrails-security.md)
    **You're done when:** you can design (a) a PR code-review bot and (b) an asynchronous coding agent that takes an issue and opens a PR — covering repository context retrieval, sandboxed execution, tool design, test-based verification, AGENTS.md conventions, security against injected instructions and secret exfiltration, evals (SWE-bench-style + internal), and cost per task.

## Problem

"Design an AI system for our engineering org (2,000 engineers, 3,000 repos): (1) automatically review every pull request and leave useful comments; (2) let engineers assign issues to an agent that writes code, runs tests and opens a PR."

Enterprise flavour: repos include Java/Spring Boot services for booking and tracking, Python data pipelines, infra-as-code; strict security (no code leaving approved providers), SOX controls on some repos.

## Clarifying questions

| Question | Why |
|---|---|
| Review bot: comment-only or also suggest fixes? Blocking or advisory? | Precision requirements; trust |
| Coding agent: which task types (bug fixes, dependency upgrades, test writing, features)? | Autonomy level, eval sets |
| Execution environment: can agents run builds/tests? Network access? | Sandbox design, dependency caching |
| Code hosting (GitHub/GitLab/Azure DevOps), CI system? | Integration points, webhooks |
| Model restrictions (approved providers, data residency)? | Model strategy, self-hosting |
| Monorepo vs many repos; sizes? | Context retrieval strategy |
| Success metrics: accepted comments, merged PRs, time saved? | Evals and ROI |

## Requirements

**Functional (review bot):** triggered on PR open/update; understands diff in repo context; comments inline with severity and rationale; summarises PR; respects repo conventions (AGENTS.md, lint rules); learns from dismissed comments; configurable per repo.

**Functional (coding agent):** accept issue/task; plan; read/search code; edit files; run build/tests/linters in a sandbox; iterate; open PR with description and test evidence; respond to review comments; stop and ask when blocked.

| NFR | Target (assumed) |
|---|---|
| Quality (review) | ≥ 60% of comments rated useful/addressed; false-positive "blocking" comments < 5% |
| Quality (agent) | ≥ 40% of assigned well-scoped tasks merged with ≤ 1 human revision round (start narrow) |
| Latency | Review within 5 min of PR update; agent task within 30 min typical |
| Cost | Review < $0.50/PR avg; agent < $5/task avg, hard cap $20 |
| Safety | No secret exfiltration; sandbox isolation; no pushes to protected branches; human merge required; injection-resistant |
| Scale | 8k PRs/day; 1k agent tasks/day |

## Estimation

```text
Review bot: 8k PRs/day (+ updates → ~15k review runs/day)
  context per run: diff 3k tokens + related code 15k + conventions 2k + instructions 2k ≈ 22k input
  multi-pass (find issues → verify each → dedupe) ≈ 3 calls → ~60k input, 3k output per run
  15k × 60k = 900M input tokens/day; 45M output
  at assumed $3/M in, $15/M out → $2.7k + $0.7k ≈ $3.4k/day (~$0.23/run) → caching repo context helps
Coding agent: 1k tasks/day × ~40 LLM steps × growing context (avg 40k tokens/step)
  = 1.6B input tokens/day; with prompt caching of the stable prefix/history (~80% cached at 10% price)
  → effective ≈ 0.2 × 1.6B × $3 + 0.8 × 1.6B × $0.3 ≈ $960 + $384 ≈ $1.3k/day + output (~$300)
  ≈ $1.6/task → within budget; without caching ~$5/task
Sandbox compute: 1k tasks × 30 min × 4 vCPU = 2k vCPU-hours/day; peaks → autoscaled pool of microVMs
```

Callout: for agents, **prompt caching is the difference between viable and not**, because every step resends the growing transcript.

## Architecture

```mermaid
flowchart TB
  GH[Code host webhooks<br/>PR opened, issue assigned, comment] --> ING[Event ingress<br/>dedupe, auth, per-repo config]
  ING --> Q[(Task queue)]
  Q --> RV[Review worker]
  Q --> AG[Agent orchestrator<br/>durable loop, budget, max steps]
  RV --> CTX[Repo context service]
  AG --> CTX
  CTX --> IDX[(Code index<br/>symbols graph, embeddings, BM25)]
  CTX --> CONV[(Conventions<br/>AGENTS.md, lint config, past review feedback)]
  AG --> SBX[Sandbox pool<br/>ephemeral microVMs, repo checkout,<br/>dependency cache, egress allow-list]
  SBX --> TOOLS[Tools: read/search/edit files,<br/>run tests, lint, git diff]
  RV & AG --> LGW[LLM gateway<br/>approved models, caching, budgets]
  AG --> PR[Git service<br/>branch, commit, open PR<br/>(bot identity, no protected-branch rights)]
  RV --> CMT[Post review comments]
  CMT & PR --> GH
  GH -->|reactions, resolved/dismissed| FB[(Feedback store)]
  FB --> EV[Eval & tuning pipeline]
  RV & AG -. OTel .-> OBS[(Tracing)]
```

## Component deep dives

### 1. Repository context

| Technique | Strength | Weakness |
|---|---|---|
| Agentic search (grep/ripgrep, file reads, `find`) driven by the model | Precise, always fresh, no index | More steps/tokens; needs good tools |
| Symbol graph / repo map (tree-sitter tags, call graph, like Aider's repo map) | Compact overview of structure | Build per commit; language coverage |
| Embeddings over code chunks | Fuzzy "where is X handled" | Stale quickly; weaker than grep for code |
| LSP-backed tools (go-to-definition, references) | Exact semantics | Heavy to run per sandbox |
| Conventions files (AGENTS.md, CLAUDE.md-style) | Encodes build/test commands, style, do/don't | Must be maintained |

2026 practice in leading coding agents leans heavily on **agentic search + a compact repo map + conventions files**, with embeddings as optional help. For review, the context service fetches: changed files in full, callers/callees of changed symbols, related tests, and repo conventions.

### 2. Tool design for the coding agent

Few, well-designed tools: `search_code(query, path_glob)`, `read_file(path, range)`, `edit_file(path, old, new)` (exact-string replacement is more robust than whole-file rewrites), `run(cmd)` restricted to allow-listed commands (build, test, lint) with timeouts and truncated output, `git_diff()`, `open_pr(title, body)`. Return structured, concise errors ("test X failed: assertion at line 42") — tool output quality determines agent success.

### 3. Agent loop and verification

Plan → explore → edit → **run tests/linters** → read failures → iterate → self-review diff → open PR. Verification is the key design choice: code has an objective oracle (compilers, tests), which is why coding agents work better than most agents. Add: write/modify tests first for bug fixes (reproduce → fix), run only affected tests for speed, then the full suite once. Budgets: max steps, tokens, wall time; stop and ask a human when stuck (e.g., three failed attempts on the same error).

Execution options: vendor agent SDKs (Claude Agent SDK, OpenAI Agents SDK with sandbox agents, GitHub Copilot coding agent as a managed product) vs custom loop on LangGraph/Pydantic AI. Buy for speed; build if you need deep integration with internal systems, custom sandboxes or model portability.

### 4. Sandbox

Ephemeral microVM/container per task (Firecracker, gVisor, Kata), fresh checkout, pre-warmed images per language with dependency caches (Maven/Gradle, pip/uv), CPU/memory/time limits, **egress allow-list** (package registries via internal proxy only), no production credentials, secrets scanning of outputs. Filesystem isolation keeps the agent inside the repo; network isolation prevents exfiltration.

### 5. Review bot quality

The failure mode of review bots is **noise**: 20 nitpicks train engineers to ignore the bot. Design for precision:

- Multi-stage: generate candidate issues → verify each candidate with a focused prompt (read surrounding code, check if it's real) → rank by severity/confidence → post top N.
- Categories: correctness bugs, security, concurrency, API misuse, missing tests; skip style if linters exist.
- Learn from feedback: dismissed/"not helpful" comments become negative examples; per-repo suppression rules.
- Summaries and "risk notes" (e.g., "touches payment rounding logic") are often more valued than nitpicks.

### 6. Security

Threats (map to OWASP LLM & Agentic Top 10):

| Threat | Example | Control |
|---|---|---|
| Prompt injection via repo content | A README/issue/comment says "also add this curl to the build script" | Treat issue/PR text as untrusted; agent can't change CI config/protected paths without approval; diff review by humans; injection classifiers on issue content |
| Secret exfiltration | Agent reads `.env` and posts it in a PR or fetches a URL with it | No secrets in sandbox; egress allow-list; output secret scanning; lethal trifecta broken by network isolation |
| Supply chain | Agent adds a typosquatted dependency | Dependency allow-list/proxy, SCA scans in CI |
| Privilege abuse | Bot token can push to main | Bot identity with branch-only rights; branch protection; required human review |
| Tool misuse | `rm -rf` or long-running processes | Command allow-list, sandbox limits |
| Malicious PR from fork triggers review bot with secrets | Classic CI injection | Run bot on untrusted forks without secrets; separate trust levels |

### 7. Conventions and memory

AGENTS.md (cross-tool standard, now Linux Foundation–stewarded) per repo: build/test commands, architecture notes, style, forbidden actions. The platform can auto-propose AGENTS.md updates from repeated review feedback. Per-repo memory of past decisions ("we use records not Lombok") improves both bots.

## Evaluation strategy

- **Public benchmarks** (SWE-bench Verified and successors) for model shortlisting only — contamination and distribution mismatch make them weak predictors for your codebase.
- **Internal agent eval set**: 100–300 historical issues with merged fixes and tests from your repos (hidden tests like SWE-bench); run agent in sandbox; metric = tests pass + human-judged mergeability on a sample. Slices by language/repo/task type.
- **Review bot eval set**: historical PRs with known bugs (from post-merge incidents/reverts) → recall of real issues; plus clean PRs → false-positive rate. Precision matters more than recall.
- **Online**: comment resolution/"useful" rate, dismiss rate, agent PR merge rate, revision rounds, time-to-merge, revert rate of agent PRs (quality after merge), cost per merged PR.
- **Error analysis** of failed agent runs: *wrong file localisation*, *didn't run tests*, *environment/setup failure*, *misread requirements*, *gave up*, *over-edited*. Environment failures are often the biggest bucket — fix sandboxes before prompts.

## Observability

Trace per task: steps, tool calls (commands, durations, exit codes), tokens/cost per step, cache hit rate, sandbox resource usage. Dashboards: tasks by outcome, cost per merged PR, p95 duration, sandbox failures, review comment usefulness by repo. Keep full transcripts for audit (SOX repos) with secret redaction.

## Failure modes

| Failure | Mitigation |
|---|---|
| Noisy review comments → ignored bot | Verification stage, top-N limit, severity thresholds, feedback learning |
| Agent "fixes" by deleting/skipping tests | Detect test deletions/skip annotations in diff; forbid via policy; human review |
| Runaway loops/cost | Step/token/time budgets, repeated-error detection |
| Environment setup failures | Pre-built images, AGENTS.md with setup commands, caching |
| Injected instructions from issue text | Untrusted-content handling, restricted paths, human merge |
| Large diffs nobody reviews | Cap diff size; split tasks; require tests |
| Model provider outage | Gateway fallback; queue tasks (async anyway) |

## Scaling & cost optimization

- Prompt caching (stable system prompt, tool definitions, repo map, transcript prefix).
- Route: small model for PR summaries and triage; frontier for verification and agent planning.
- Skip review for trivial PRs (docs-only, generated files, lockfiles).
- Sandbox pool with warm images; per-language dependency caches; scale to zero off-hours.
- Batch nightly jobs (dependency upgrades across 3,000 repos) with batch APIs.

## What a Staff-level answer adds

- **Adoption and trust strategy**: start advisory, measure usefulness, earn the right to block; start the agent on narrow task types (dependency bumps, flaky test fixes, small bugs).
- **Developer-experience metrics** (DORA + time saved) and honest ROI, including review burden of agent PRs on humans.
- **Governance**: code provenance labels on AI-authored commits, SOX controls (human approval), licence compliance checks.
- **Platform leverage**: shared sandbox infra and MCP tools for internal systems (ticketing, CI logs, feature flags) usable by any coding agent (Claude Code, Copilot, internal).
- **Org impact**: shifts engineers toward specification and review; invest in tests and AGENTS.md because they multiply agent effectiveness.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [SWE-bench paper](https://arxiv.org/abs/2310.06770) | paper | The benchmark design you should mirror internally | advanced | free |
| [SWE-bench site](https://www.swebench.com/) | interactive | Leaderboards and variants (Verified, etc.) | intermediate | free |
| [Claude Code best practices (Anthropic)](https://www.anthropic.com/engineering/claude-code-best-practices) | article | Real agentic-coding workflow patterns and CLAUDE.md usage | intermediate | free |
| [Claude Code sandboxing (Anthropic)](https://www.anthropic.com/engineering/claude-code-sandboxing) :gem: | article | Filesystem + network isolation design | advanced | free |
| [Aider repo map](https://aider.chat/docs/repomap.html) :gem: | docs | Compact repo context via tree-sitter — elegant and cheap | intermediate | free |
| [Writing effective tools for agents (Anthropic)](https://www.anthropic.com/engineering/writing-tools-for-agents) | article | Tool design determines agent success | intermediate | free |
| [AGENTS.md](https://agents.md/) | docs | Cross-tool repo conventions standard | intro | free |
| [GitHub Copilot coding agent docs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent) | docs | Managed product baseline to compare with a build | intermediate | paid |
| [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) | docs | Build custom coding agents on the Claude Code harness | intermediate | paid |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | docs | Sandbox agents (beta, Apr 2026) for code execution | intermediate | free |

## Follow-up questions

### L2 — Apply

??? question "Q1. The review bot posts ~15 comments per PR and engineers ignore it. What do you change first?"
    ??? success "Answer"
        Precision over recall: add a verification pass per candidate comment (re-read code context, confirm it's a real issue), drop style comments already covered by linters, cap at top 3–5 by severity and confidence, collapse minor notes into a summary. Measure useful/resolved rate before and after on a sample of repos. Collect dismiss reasons to build negative examples and per-repo suppressions.

??? question "Q2. Estimate the per-task cost of an agent: 30 steps, context grows from 10k to 70k tokens linearly, 500 output tokens/step, assumed $3/M input, $0.30/M cached, $15/M output, 85% cache hit."
    ??? success "Answer"
        Average context ≈ 40k → total input ≈ 30 × 40k = 1.2M tokens. Cached 1.02M × $0.30/M = $0.31; uncached 0.18M × $3/M = $0.54; output 15k × $15/M = $0.23. Total ≈ **$1.08/task**. Without caching: $3.60 + $0.23 = $3.83. Compaction (clearing old tool outputs) reduces further.

??? question "Q3. How does the agent know how to build and test a repo it has never seen?"
    ??? success "Answer"
        AGENTS.md with build/test/lint commands and setup notes; fallback detection (pom.xml/gradle → `./mvnw test`/`./gradlew test`; pyproject → `uv run pytest`); CI config parsing (workflow files show real commands); pre-built sandbox images per language with dependency caches. If setup fails twice, the agent reports the blocker and suggests an AGENTS.md addition.

??? question "Q4. Design the sandbox network policy."
    ??? success "Answer"
        Default deny egress. Allow: internal package proxy (Maven/PyPI/npm mirrors with allow-listed packages), code host API via a scoped proxy for the git operations the platform performs (not the agent directly), LLM gateway only from the orchestrator (not from inside the sandbox). No access to internal production networks or metadata endpoints. Log all egress attempts; alert on denied attempts (possible injection).

### L3 — Design & trade-offs

??? question "Q5. Embeddings-based code retrieval vs agentic grep/search for the agent's context — decide."
    ??? success "Answer"
        Default to agentic search (ripgrep, file reads, symbol lookup) plus a compact repo map: always fresh, precise for identifiers, no index maintenance per commit. Embeddings help for fuzzy conceptual queries in huge monorepos ("where do we compute demurrage?") — add as an optional tool, not the primary mechanism. Validate with the internal eval set (localisation accuracy per method).

??? question "Q6. Should the review bot be allowed to block merges?"
    ??? success "Answer"
        Not initially. Start advisory; measure precision per category. Allow blocking only for narrow, high-precision categories (e.g., hardcoded secrets, known-vulnerable patterns, missing migration for schema change) where deterministic tools or verified detections have ≥ 95% precision, with a human override. General LLM opinions stay advisory — blocking on probabilistic judgments erodes trust and velocity.

??? question "Q7. Buy (Copilot coding agent / Claude Code / vendor product) vs build a custom agent platform?"
    ??? success "Answer"
        Buy for the broad developer population: fastest value, vendor keeps up with model changes. Build (or extend via SDKs and MCP) where you need: internal system integrations (ticketing, feature flags, internal CI), custom sandboxes/network policies, model portability/residency, or fleet-wide automation (upgrade 3,000 repos). Common pattern: vendor agents for interactive use + internal platform for batch/fleet tasks, both governed by the same sandbox, MCP tools and policies.

??? question "Q8. The agent's PRs pass tests but reviewers find subtle design problems. How do you improve?"
    ??? success "Answer"
        Tests measure correctness, not design fit. Improve context: AGENTS.md with architecture principles, examples of idiomatic code, relevant ADRs; add a self-review step against conventions; restrict tasks to well-scoped types until quality is proven; capture reviewer comments as feedback data (patterns → conventions/linters). Measure revision rounds and reviewer time per agent PR — if review cost exceeds time saved, narrow scope.

### L4 — Staff-level ambiguity

??? question "Q9. Leadership wants '30% of code written by AI agents' as an OKR. What's your response?"
    ??? success "Answer"
        Push back on the output metric (lines of code incentivises churn and review burden). Propose outcome metrics: lead time for changes, % of eligible toil tasks automated (dependency upgrades, flaky tests), review time, change failure rate of AI-authored changes, developer satisfaction. Keep "AI-authored share" as a tracked indicator, not a target. Pair with investment in tests, AGENTS.md and sandbox infra — the multipliers of agent effectiveness.

??? question "Q10. An agent PR introduced a vulnerability that reached production. What systemic changes do you make?"
    ??? success "Answer"
        Blameless postmortem: how did review (human + bot) and CI (SAST/SCA) miss it? Changes: mandatory security scanning for all PRs (not only agent), agent PRs labelled for provenance with required reviewer from code owners for sensitive paths, security-focused eval cases added to both review-bot and agent eval sets, restrict agent autonomy for security-sensitive modules (auth, payments), and track change failure rate for AI-authored PRs separately.

??? question "Q11. How do you run a fleet-wide migration (e.g., Spring Boot 3 → 4 across 400 services) with agents?"
    ??? success "Answer"
        Treat as a campaign: deterministic codemods (OpenRewrite recipes) first for mechanical changes; agents handle residual compile/test failures in sandboxes; batch execution with concurrency limits; per-repo PRs with standard descriptions and test evidence; dashboard of status (open/merged/failing); human owners review; escalate stuck repos. Eval on a pilot of 10 representative services before scaling; track cost per migrated service and failure taxonomy to improve recipes.

## Real-world use cases

- **PR review bot across an enterprise's Java/Python services**: precision-first comments, summaries and risk notes.
- **Dependency and framework upgrade campaigns**: codemods + agents fixing residual breakage (e.g., Spring Boot 4 migration).
- **Flaky test triage agent**: reproduces, diagnoses, proposes fix or quarantine.
- **Issue-to-PR agent for small bugs** in internal tools, with human review and merge.

## Checklist

- [ ] I can draw the review bot and coding agent architectures with sandbox and gateway
- [ ] I can compute cost per agent task with and without caching
- [ ] I can design tools, verification loop, budgets and stop conditions
- [ ] I can list coding-agent security threats and concrete controls
- [ ] I can design internal SWE-bench-style evals and online metrics
- [ ] I answered all L3/L4 questions out loud in < 3 min each
