---
title: "Managed platforms: Microsoft Foundry, Bedrock AgentCore"
track: agentic-ai
slug: managed-agent-platforms
priority: P1
complexity: 3
est_hours: 3
phase: 4
tags: [agentic-ai, P1]
last_reviewed: 2026-09-25
---

# Managed platforms: Microsoft Foundry, Bedrock AgentCore

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 3/5 · **Est. time:** 3 h · **Phase:** 4 · **Prereqs:** [Vendor agent SDKs](vendor-agent-sdks.md), [MCP](mcp.md), [Guardrails & security](guardrails-security.md), [Multi-region & DR](../system-design/multi-region-dr.md)
    **You're done when:** you can explain what a managed agent platform provides that a container platform doesn't, deploy the capstone's agent to Foundry (hosted agent) and know the AgentCore equivalent, and can present a build-vs-buy decision with a portability plan.

## Why it matters

Running agents in production requires a pile of undifferentiated infrastructure: session isolation, sandboxes for code/browser tools, per-agent identity and credential brokering, long-running execution, memory stores, tool gateways, tracing and evaluation. Hyperscalers now sell this as **agent platforms**. For a Maersk-style Azure estate the target is **Microsoft Foundry** (renamed from Azure AI Foundry in 2026); AWS's equivalent is **Bedrock AgentCore**; Google's is **Vertex AI Agent Engine**.

The architect's job: decide which layers to rent, keep the *agent logic and tools* portable (MCP, A2A, OTel, open frameworks), and avoid a proprietary state/identity trap. This is also the "deploy to Azure Container Apps + Foundry" leg of the capstone.

## Core concepts

### What a managed agent platform bundles

| Capability | Why it's hard to DIY | Foundry Agent Service | Bedrock AgentCore |
|---|---|---|---|
| **Runtime / hosting** | Session isolation, autoscale, long-running tasks, cold starts | Agent Runtime: prompt agents (no code) and **hosted agents** (your container or zip; VM-isolated sessions, autoscale) | **Runtime**: serverless, per-session microVM isolation, framework/model-agnostic, MCP and A2A protocols, extended async runs |
| **Managed loop ("no-code")** | Reasonable default agent | **Prompt agents** (instructions + model + tools, versioned) | **Harness**: declare model/prompt/tools in config; managed loop |
| **Tool gateway** | Auth to many backends, MCP conversion, governance | **Toolboxes**: curated tools exposed via one managed MCP endpoint with central auth/versioning | **Gateway**: turn APIs/Lambdas into MCP tools; connect existing MCP servers |
| **Identity** | Per-agent credentials, user delegation (OBO) | Entra identity per agent, RBAC, OAuth identity passthrough (OBO) | **Identity**: workload identity, OAuth/API-key credential providers, any IdP |
| **Memory** | Short + long-term stores | Built-in memory tool; BYO Cosmos DB/Storage/AI Search for state | **Memory**: short- and long-term, shareable across agents |
| **Sandboxed tools** | Code exec, browsing safely | Code interpreter, web/file search tools | **Code Interpreter**, **Browser** runtimes |
| **Policy** | Deterministic tool-call authorisation | Content filters/guardrails incl. XPIA (cross-prompt injection) detection; Entra RBAC | **Policy** (GA Mar 2026): Cedar-compatible rules intercepting every tool call at the Gateway |
| **Observability & eval** | Traces, quality measurement | Agent tracing, App Insights, evaluations, agent optimizer (preview) | **Observability** (OTel to CloudWatch), **Evaluations** (GA Mar 2026), Optimization |
| **Publishing & registry** | Discovery, distribution | Versioned publish; Teams/M365 Copilot; Entra Agent Registry; A2A v1.0 GA endpoints | **Registry** for agents/MCP servers/skills |

### Microsoft Foundry Agent Service (as of Sept 2026)

Three agent types:

1. **Prompt agents** — configuration only; fastest path; versioned; portal, SDK or REST; CI/CD friendly.
2. **Voice-based prompt agents** — managed real-time voice via Voice Live (parts in preview).
3. **Hosted agents** — bring code built with Agent Framework, LangGraph, OpenAI Agents SDK, Anthropic Agent SDK, GitHub Copilot SDK or custom; ship a container or a zip (Foundry builds it); managed endpoint, dedicated Entra identity, session-level state persistence, autoscale, tracing, BYO VNet with VM-isolated sessions.

You can also call the **Responses API** directly ("ephemeral agents") with your own orchestration while still using Foundry models, tools, OBO auth and project-level observability. The Assistants API was retired on 2026-08-26 — migrate anything still using Assistants/threads to Responses-based agents.

```python
# Ephemeral agent via Foundry's OpenAI-compatible Responses endpoint (pattern; check quickstart for current names)
# uv add azure-ai-projects azure-identity openai
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(endpoint="https://<res>.services.ai.azure.com/api/projects/<proj>",
                          credential=DefaultAzureCredential())
openai = project.get_openai_client()          # OpenAI client bound to the project
resp = openai.responses.create(model="<deployment>", input="Summarise delay risk for MSK-123",
                               instructions="You are the Ops Copilot.")
print(resp.output_text)
```

```python
# Hosted agent skeleton with Microsoft Agent Framework (containerised, deployed to Foundry)
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import DefaultAzureCredential

agent = Agent(
    client=FoundryChatClient(project_endpoint="<endpoint>", model="<deployment>",
                             credential=DefaultAzureCredential()),
    name="ops-copilot", instructions="…", tools=[…],
)
# Wrap with the hosting adapter/entry point described in the hosted-agents quickstart,
# build image → push to ACR → deploy as a hosted agent; identity is assigned automatically.
```

Foundry specifics worth knowing: **Toolboxes** (one governed MCP endpoint per tool bundle), **Agent identity** (least-privilege per agent, Entra Agent ID/Registry), **Guardrails** (jailbreak/XPIA detection), **cost model** = inference + tool usage + (hosted) container compute, private networking (prompt agents; hosted with BYO VNet).

### Bedrock AgentCore (as of Sept 2026)

Modular services usable together or separately: **Runtime, Harness, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Policy, Evaluations, Optimization, Registry, Payments (x402/MPP microtransactions)**. Works with Strands Agents (default), LangGraph, CrewAI, LlamaIndex, Google ADK, OpenAI Agents SDK and any model.

Workflow: `npm install -g @aws/agentcore` → `agentcore create` (Harness or code-based agent; Strands/LangGraph/ADK/OpenAI Agents; CodeZip or Container build) → `agentcore dev` (local + inspector) → `agentcore deploy` (CDK under the hood) → `agentcore invoke`. In code, `bedrock-agentcore` provides `BedrockAgentCoreApp` with an `@app.entrypoint` handler. Invocation via `InvokeAgentRuntime` with a session ID; **session isolation per microVM**.

### Google Vertex AI Agent Engine (brief)

Managed runtime for ADK/LangGraph/other agents with sessions, memory bank and evaluation on GCP; conceptually parallel to the two above.

### Comparison and decision framework

| Dimension | Container platform (ACA/EKS/Cloud Run) | Foundry / AgentCore / Agent Engine |
|---|---|---|
| Control | Full | Constrained to platform contracts |
| Time to first prod agent | Weeks (identity, sandboxing, tracing to build) | Days |
| Per-agent identity & OBO | Build yourself | Built in |
| Session isolation / sandboxes | Build yourself (gVisor/Firecracker) | Built in |
| Cost | Compute + ops effort | Usage-based premium; less ops |
| Portability | High | Medium (depends on how much you adopt: hosted containers portable; proprietary state/toolbox less) |
| Compliance fit | You certify | Inherits cloud compliance posture |

**Portability plan (do this regardless):**

- **Tools via MCP** behind a gateway (Foundry toolbox / AgentCore Gateway / your own).
- **Agent logic in an open framework** (LangGraph, Pydantic AI, Agent Framework) packaged as a plain container — hosted-agent models accept your image.
- **OTel GenAI traces** exported to your backend (Langfuse) in addition to the platform's.
- **State in your own stores** (Postgres/Redis/Cosmos) where feasible, not opaque platform memory, for anything hard to migrate.
- **Models via gateway alias**, so Foundry-hosted models are one route among many.
- **Evals in your CI**, not only in the platform's eval service.

### Capstone deployment mapping

| Capstone component | Local (docker-compose) | Azure |
|---|---|---|
| Orchestrator (LangGraph) + Pydantic AI sub-agents | Container | **Hosted agent on Foundry** (or Azure Container Apps + Responses API) |
| MCP servers (Python, Spring AI) | Containers | Azure Container Apps (internal ingress) behind APIM/toolbox |
| LLM gateway | LiteLLM container | LiteLLM on ACA → Foundry model deployments |
| Models | Ollama | Foundry deployments (Azure OpenAI/partner models) |
| Vector/RAG | pgvector | Azure Database for PostgreSQL + pgvector or Azure AI Search |
| Observability | Langfuse | Langfuse (ACA) + App Insights via OTel |
| Identity | static tokens | Entra ID, managed identities, agent identity, OBO |

### Senior-level nuance

- **Ask what's actually proprietary.** Compare: is state exportable? Can you run the same container elsewhere? Are traces OTel? Is the tool endpoint standard MCP?
- **Preview vs GA.** Many platform features (voice agents, agent optimizer, some evaluations) are preview — no SLA. Check region availability and quotas (model capacity is the real bottleneck).
- **Identity is the differentiator**, not the loop: per-agent Entra/IAM identities with OBO and audit are hard to replicate; that's the strongest reason to buy.
- **Cost transparency.** Bundle pricing includes inference, tool calls, sandbox seconds, memory operations, logging ingestion (App Insights/CloudWatch can dominate). Model the total cost per task.
- **Multi-cloud reality.** An enterprise may run Foundry for M365-adjacent agents and AgentCore for AWS-native data — unify with A2A/MCP and a shared registry rather than forcing one platform.
- **Data residency and zones**: confirm the agent runtime, memory and tracing stores all reside in the required region.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | docs | Agent types, toolboxes, identity, publishing, A2A | intermediate | free |
| [Foundry hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) | docs | Containers/zip hosting, identity, VNet, sessions | intermediate | free |
| [Microsoft Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/) | docs | The recommended framework for Foundry hosted agents | intermediate | free |
| [AWS: What is Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) | docs | Service catalog and integrations | intermediate | free |
| [AgentCore CLI quickstart](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-cli.html) | docs | create → dev → deploy → invoke workflow | intermediate | free |
| [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) | docs | Consumption dimensions to model total cost | intermediate | free |
| [AgentCore samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples) :gem: | docs | End-to-end examples across frameworks | intermediate | free |
| [Google ADK docs](https://adk.dev/) | docs | Agent Engine deployment path on GCP | intermediate | free |

## Hands-on lab

**Goal (2 h):** deploy the capstone agent to a managed platform and document portability.

1. **Package**: ensure the orchestrator runs as a plain container with health endpoint, config via env, OTel exporter configured, tools via MCP URLs.
2. **Azure path**: create a Foundry project + model deployment; deploy the container as a **hosted agent** (or run on Azure Container Apps calling the Responses API); assign least-privilege RBAC to its identity; register the MCP servers as a **toolbox** or keep them on ACA behind APIM.
3. **Identity**: replace static tokens with managed identity/OBO for the ticketing API call; show in logs which identity performed a write.
4. **Observability**: verify traces in App Insights and in Langfuse (dual export).
5. **AgentCore thought exercise / optional**: scaffold the same agent with `agentcore create` (LangGraph template), deploy to a sandbox account, invoke with a session ID; compare setup time, cost dimensions and what you had to change.
6. **ADR**: document what's proprietary, exit plan, quotas, region, cost/task, and go/no-go criteria.

**Expected output:** agent reachable via Foundry endpoint with Entra-authenticated calls, traces in both backends, and an ADR with a portability table.

## Questions

### L1 — Recall

??? question "Q1. Name the three Foundry Agent Service agent types."
    ??? success "Answer"
        Prompt agents (config-only), voice-based prompt agents (managed real-time voice), and hosted agents (your code as container/zip with managed endpoint, identity and scaling).

??? question "Q2. What are AgentCore Runtime's key isolation and protocol characteristics?"
    ??? success "Answer"
        Serverless with per-session microVM isolation, framework- and model-agnostic, supports MCP and A2A, and extended/async runs for long tasks, with built-in identity.

??? question "Q3. What is a Foundry toolbox?"
    ??? success "Answer"
        A curated, versioned bundle of tools (web/file search, code interpreter, MCP servers, custom functions) exposed through one managed MCP-compatible endpoint with centralised authentication and governance, reusable across agents and frameworks.

### L2 — Apply

??? question "Q4. Your agent must call the ticketing API as the end user. Which platform capability do you use?"
    ??? success "Answer"
        OAuth identity passthrough/On-Behalf-Of in Foundry (or AgentCore Identity's OAuth credential providers), so the API sees the user's delegated identity with scoped permissions, rather than a broad shared service credential; log both agent and user identities.

??? question "Q5. Traces show App Insights/CloudWatch ingestion is 40% of the agent's monthly cost. What do you do?"
    ??? success "Answer"
        Sample low-value traces, drop or truncate large prompt/response bodies (or store them in cheaper storage with references), reduce log verbosity, use tail-based sampling that keeps errors and slow traces, set retention tiers, and export full-fidelity traces only to a cheaper backend (self-hosted Langfuse). Ensure PII isn't logged.

??? question "Q6. You built on the Assistants API/threads. What's the migration situation in Foundry?"
    ??? success "Answer"
        The Assistants API was retired on 2026-08-26; agents should move to Responses-API-based Foundry agents (prompt or hosted agents), migrating threads/conversation state to the new conversation/session mechanisms and re-testing tool behaviour with evals.

### L3 — Design & trade-offs

??? question "Q7. Azure Container Apps vs Foundry hosted agents for the capstone orchestrator."
    ??? success "Answer"
        ACA: maximal control, standard container ops, cost-predictable, portable, but you build identity brokering, session isolation, agent registry/publishing and tracing integration. Hosted agents: per-agent Entra identity, session state persistence, VM-isolated sessions, managed endpoint, publishing to Teams/Copilot/registry, built-in tracing/evals; more constrained and partly preview-dependent. Choose hosted agents when identity/publishing/M365 distribution matters and the container remains portable; choose ACA for max control or multi-cloud parity. Keep the artifact identical (container) to allow either.

??? question "Q8. Buy AgentCore Memory/Foundry memory or use your own Postgres for agent memory?"
    ??? success "Answer"
        Managed: fast, integrated, scoped, less ops; but opaque schemas, limited eval/erasure control and portability. Own Postgres: full control over schema, RLS, erasure, evals, and migration; you build extraction logic. If memory holds personal data with erasure obligations or is core IP, own it (or use managed with proven export/delete). For low-risk conversational continuity, managed is fine.

??? question "Q9. How do you compare Foundry vs AgentCore for a company that is 80% Azure, 20% AWS?"
    ??? success "Answer"
        Primary platform Foundry (identity, M365, procurement, data gravity). Use AgentCore only where workloads/data live in AWS. Bridge through open protocols: MCP toolboxes/gateways, A2A between agents, OTel traces to one backend, shared agent registry and policy standards; avoid duplicating governance by centralising identity federation (Entra ↔ AWS IAM Identity Center/OIDC).

### L4 — Staff-level ambiguity

??? question "Q10. A vendor pitches the platform as 'zero lock-in because it supports open protocols.' How do you validate the claim?"
    ??? success "Answer"
        Test exit: export an agent definition, state, memory and traces; deploy the same container elsewhere; call tools through the standard MCP endpoint from a non-platform client; verify OTel export; check pricing for egress and data export; review contract for data portability and deprecation windows. Score each layer (loop, tools, state, identity, observability, deployment) for portability, and require a time-boxed pilot with a rehearsed migration of one agent.

??? question "Q11. Design a governance model for 50 teams shipping agents on Foundry."
    ??? success "Answer"
        Landing zone with shared Foundry hub/project structure per business unit; policy-as-code (Azure Policy) for regions, models, network isolation; central toolbox/registry of approved tools and MCP servers; agent identity standards (least privilege, no shared credentials); required guardrails and eval gates before publishing; cost budgets and tags per team; observability baseline (OTel + dashboards); lifecycle (versioning, deprecation, kill switch); platform team offering templates and office hours. Measure adoption, incidents and cost per agent.

## Real-world use cases

- **Enterprise Copilot extensions**: hosted agents published to Teams/M365 Copilot via Foundry with Entra-governed access to SharePoint/internal APIs.
- **AWS-native data agents**: AgentCore Gateway wrapping Lambda/DynamoDB tools with Policy enforcing per-tool authorisation.
- **Browser automation for procurement** using managed Browser runtimes rather than self-managed headless clusters.
- **Regulated workloads**: private networking/BYO VNet with VM-isolated agent sessions.

## Pitfalls & anti-patterns

- Adopting proprietary state/tools everywhere, then discovering no exit.
- Assuming preview features have SLAs.
- Ignoring model quota/capacity and region availability.
- Letting observability ingestion costs dominate.
- Shared service principals for all agents.
- Duplicating governance separately in each cloud.

## Checklist

- [ ] I can compare Foundry, AgentCore and container hosting per capability
- [ ] I deployed (or fully designed) the capstone agent on Foundry with Entra identity
- [ ] Tools are MCP, traces are OTel, state ownership is decided
- [ ] I wrote a portability/exit ADR
- [ ] I answered all L3 questions out loud in < 3 min each
