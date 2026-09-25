---
title: "Pydantic AI"
track: agentic-ai
slug: pydantic-ai
priority: P0
complexity: 2
est_hours: 4
phase: 3
tags: [agentic-ai, P0]
last_reviewed: 2026-09-25
---

# Pydantic AI

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 2/5 · **Est. time:** 4 h · **Phase:** 3 · **Prereqs:** [Pydantic v2](../python/pydantic-v2.md), [Prompting & structured outputs](prompting-structured-outputs.md), [Tool calling](tool-calling.md)
    **You're done when:** the copilot's log, metrics and runbook sub-agents are Pydantic AI agents with typed dependencies, typed outputs and validators, usage limits, MCP tools, `TestModel`-based unit tests, and an `pydantic_evals` dataset — and you can call them from LangGraph nodes.

## Why it matters

Pydantic AI (from the Pydantic team) is a **type-safe, provider-agnostic agent framework** that brings the "FastAPI feeling" to LLM apps: validated inputs/outputs, dependency injection, first-class testing, and OpenTelemetry instrumentation. **V1 shipped in September 2025; V2.0 went stable on 2026-06-23** and the project ships releases very frequently (the 2.4x series by late September 2026) — so pin versions and read the changelog. V2's headline is the **capability** primitive (bundling instructions, tools, hooks and model settings into composable units) with a leaner core and a separate first-party "Harness" for things like memory, guardrails and code mode.

For this curriculum it is the **sub-agent layer** under [LangGraph](langgraph.md): LangGraph owns topology, state and durability; Pydantic AI agents do the typed, tool-using work inside nodes. Its design also matches the way a senior Python engineer thinks: types as contracts, DI for testability, small composable pieces.

## Core concepts

### Minimal agent

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class Triage(BaseModel):
    service: str
    severity: str = Field(pattern=r"^SEV[1-4]$")
    needs_human: bool

agent = Agent(
    "anthropic:claude-sonnet-4-6",          # provider:model  (config value; also 'openai:...', 'google:...', ...)
    output_type=Triage,
    instructions="Triage the production alert. Use only the provided text.",
)
result = agent.run_sync("booking-api p95 3.2s since deploy a1b2c3")
print(result.output)        # Triage(...)  <- validated instance
print(result.usage())       # tokens/requests  (RunUsage)
```

Key APIs (as of Pydantic AI 2.x; check the docs for your pinned version):

- **Model strings:** `"openai:gpt-5.2"`, `"anthropic:claude-sonnet-4-6"`, `"google:..."`, plus Azure/Bedrock/Ollama via providers. **Breaking change in V2:** the bare `openai:` prefix now uses the **Responses API**; use `openai-chat:` for Chat Completions (relevant for Ollama/vLLM/OpenAI-compatible servers, which typically speak Chat Completions).
- **`instructions` vs `system_prompt`:** `instructions` are re-evaluated per run and *not* retained in message history when you pass history forward (usually what you want); `system_prompt` is preserved in history.
- **`Agent[Deps, Output]`** generics: `deps_type` and `output_type` give end-to-end typing checked by mypy/pyright/ty. (V2 changed generic defaults from `None` to `object`.)
- **Runs:** `agent.run_sync`, `await agent.run`, `agent.run_stream` / `run_stream_events` for streaming, `agent.iter` for step-by-step graph iteration.

### Dependencies and RunContext

Dependencies (DB pools, HTTP clients, config, the current user) are passed at run time and are available in tools, instructions and validators through `RunContext`:

```python
from dataclasses import dataclass
import httpx
from pydantic_ai import Agent, RunContext, ModelRetry

@dataclass
class Deps:
    http: httpx.AsyncClient
    logs_api: str
    user_id: str

class LogFinding(BaseModel):
    summary: str
    top_signatures: list[str]
    evidence_ids: list[str] = Field(min_length=1, description="ids of log groups supporting the summary")

log_agent = Agent(
    "anthropic:claude-sonnet-4-6",
    deps_type=Deps,
    output_type=LogFinding,
    instructions="You are the log analyst. Query logs, then summarise root-cause signals with evidence ids.",
    retries=2,                      # default tool/validation retries
)

@log_agent.instructions
async def add_context(ctx: RunContext[Deps]) -> str:
    return f"Requesting user: {ctx.deps.user_id}. Current time is provided by tools; never guess dates."

@log_agent.tool
async def query_logs(ctx: RunContext[Deps], service: str, window_minutes: int = 30) -> list[dict]:
    """Grouped error signatures for ONE service in the last N minutes (5-240). Returns <=20 groups."""
    if not 5 <= window_minutes <= 240:
        raise ModelRetry("window_minutes must be between 5 and 240")
    r = await ctx.deps.http.get(f"{ctx.deps.logs_api}/groups",
                                params={"service": service, "minutes": window_minutes})
    r.raise_for_status()
    return r.json()[:20]

@log_agent.output_validator
async def check_evidence(ctx: RunContext[Deps], out: LogFinding) -> LogFinding:
    if not out.top_signatures:
        raise ModelRetry("Include at least one error signature or say none were found.")
    return out
```

- `@agent.tool` receives `RunContext`; `@agent.tool_plain` doesn't. Function signature + docstring produce the JSON schema and description (parameter descriptions parsed from Google/NumPy/Sphinx docstrings). Type hints do the validation; failures become automatic retry prompts to the model.
- `ModelRetry` = "tell the model what's wrong and let it try again" — counts against retries. Use it for model-fixable errors only; let real infra exceptions propagate (or handle them with normal retries).
- **Toolsets** group tools (function toolsets, MCP toolsets, filtered/prefixed/approval-wrapped toolsets) and can be attached per agent or per run.

### Output modes and validation

`output_type` can be a Pydantic model, dataclass, TypedDict, scalar, a **union** (`Triage | Clarification`, each registered as a separate output tool so the model chooses), a list of types, or output functions. Modes (see [prompting & structured outputs](prompting-structured-outputs.md)): **tool output** (default, most portable), **`NativeOutput`** (provider constrained decoding, when supported), **`PromptedOutput`** (schema in the prompt; works anywhere, least reliable), **`TextOutput`** (function over text). Validation errors — Pydantic or your `output_validator` — are fed back to the model automatically within the retry budget. When streaming, validators can see partial output (`ctx.partial_output`), so avoid side effects on partials.

V2 default `end_strategy='graceful'`: function tools called in the same response as a successful output tool are still executed (V1 skipped them) — check side-effecting tools accordingly.

### Limits, settings and safety valves

```python
from pydantic_ai import UsageLimits, UsageLimitExceeded
from pydantic_ai.settings import ModelSettings

try:
    res = await log_agent.run(
        "Investigate booking-api latency", deps=deps,
        usage_limits=UsageLimits(request_limit=8, tool_calls_limit=6, output_tokens_limit=4000),
        model_settings=ModelSettings(temperature=0, max_tokens=1500, timeout=60),
    )
except UsageLimitExceeded:
    ...  # partial results / escalate
```

Also: `retries` on the agent and per tool, `max_concurrency`, message history (`message_history=` to continue conversations; history processors to trim/summarise — see [context engineering](context-engineering.md)), and **model fallback** (`FallbackModel`) for provider outages ([model routing](model-routing-gateways.md)).

### Capabilities (V2) in one paragraph

A **capability** bundles instructions, tools/toolsets, lifecycle hooks and model settings into one reusable unit that is passed via `capabilities=[...]`: built-ins include `Thinking(effort=...)`, `WebSearch()`, `ToolSearch()` (load tool definitions on demand — helps the tool-overload problem in [context engineering](context-engineering.md)), and a generic `Capability(id, description, instructions, toolset, defer_loading=True)`. The first-party Harness package adds things like code mode, memory and guardrails. Use capabilities to package "how our org does X" (e.g. a `RunbookSearch` capability with tool, instructions and safety hook) and share across agents.

### MCP integration

`MCPToolset` (V2; replaces per-transport server classes) connects to MCP servers over Streamable HTTP (URL) or stdio (`StdioTransport`) and registers as a toolset; manage connections with `async with agent:`. Details and security in [MCP](mcp.md).

```python
from pydantic_ai.mcp import MCPToolset

ops_tools = MCPToolset("http://localhost:8000/mcp")   # streamable HTTP
agent = Agent("anthropic:claude-sonnet-4-6", toolsets=[ops_tools], output_type=str)

async def main():
    async with agent:
        print((await agent.run("List active alerts for booking-api")).output)
```

### Testing: the reason many teams choose it

```python
import pytest
from pydantic_ai import models
from pydantic_ai.models.test import TestModel
from pydantic_ai.models.function import FunctionModel, AgentInfo

models.ALLOW_MODEL_REQUESTS = False      # any accidental real call raises in tests

async def test_log_agent_calls_tool_and_returns_typed_output():
    with log_agent.override(model=TestModel()):
        res = await log_agent.run("investigate", deps=fake_deps())
    assert isinstance(res.output, LogFinding)

async def test_retries_on_bad_window():
    def scripted(messages, info: AgentInfo):
        ...   # return ModelResponse with a ToolCallPart having window_minutes=999, then a valid one
    with log_agent.override(model=FunctionModel(scripted)):
        ...
```

`TestModel` auto-generates schema-valid tool calls and outputs (fast smoke tests of wiring), `FunctionModel` lets you script model behaviour precisely (retries, multi-step), `agent.override(model=..., deps=..., toolsets=...)` swaps pieces without touching production code, and `ALLOW_MODEL_REQUESTS=False` guards CI. Message history and captured tool calls (`capture_run_messages`) support trajectory assertions. This is **unit testing**; quality measurement still needs evals.

### Evals and observability built in

- **`pydantic_evals`**: `Dataset` of `Case`s with inputs/expected outputs/metadata, evaluators (`EqualsExpected`, custom `Evaluator` classes, `LLMJudge`), concurrency, report tables and span-based evaluation (assert on which tools were called) — a neat fit for trajectory checks. Compare with other options in [eval tooling](eval-tooling.md).
- **Instrumentation:** `Agent.instrument_all()` or `Agent(..., instrument=True)` emits OTel spans following the GenAI conventions (V2 default instrumentation version 5, with `gen_ai.aggregated_usage.*` on run spans) to Logfire or any OTLP backend (Langfuse/Phoenix) — see [LLM observability](llm-observability.md).

### Durable execution, graphs, and other protocols

- **Durable execution:** wrap agents with `TemporalAgent`, DBOS or Prefect variants so model calls and tools become durable activities/steps ([durable execution & HITL](durable-execution-hitl.md)). Seven engines are supported as of 2026.
- **Deferred tools / human approval:** tools can be marked as requiring approval or deferring to external execution, returning a "deferred tool requests" output so your app can collect approvals and resume the run with results — Pydantic AI's built-in HITL primitive.
- **`pydantic-graph`:** a typed state-machine library used by the agent loop and available standalone; V2 removed `pydantic_graph.persistence` and Mermaid modules — for durable graphs prefer LangGraph or a workflow engine.
- **Protocols:** A2A (`agent.to_a2a()`), AG-UI event streaming to frontends, MCP client/server ([A2A & AG-UI](a2a-ag-ui.md)); **Pydantic AI Gateway** and **Logfire** as optional commercial pieces — the framework itself is MIT and model-agnostic.

### How it compares (positioning)

| | Pydantic AI | LangGraph | OpenAI Agents SDK / Claude Agent SDK | Raw SDK loop |
|---|---|---|---|---|
| Strength | Typed agents, DI, tests, provider-agnostic | Stateful graphs, checkpoints, interrupts | Vendor-native features (sandboxes, handoffs, built-in tools) | Total control |
| Multi-agent topology | Delegation via tools; graph via pydantic-graph | First-class | Handoffs (OpenAI) / subagents (Claude) | DIY |
| Durability | Via Temporal/DBOS/Prefect | Built-in checkpointers | Vendor/runtime specific | DIY |
| Lock-in | Low | Low-medium (LangChain ecosystem) | Higher | None |

See [vendor agent SDKs](vendor-agent-sdks.md) for the comparison in depth.

### Agent delegation and composition

A parent agent can call another agent from inside a tool (passing `ctx.deps` and `ctx.usage` so token/cost limits aggregate across the sub-run):

```python
@orchestrator.tool
async def analyse_logs(ctx: RunContext[Deps], service: str) -> LogFinding:
    r = await log_agent.run(f"Analyse logs for {service}", deps=ctx.deps, usage=ctx.usage)
    return r.output
```

Use this for simple "programmatic hand-off" patterns; use LangGraph when you need checkpointed parallel fan-out and approvals.

### What juniors miss

- Assuming `openai:` still means Chat Completions after V2, then wondering why an Ollama endpoint fails (use `openai-chat:` or the provider class).
- Stuffing everything into `system_prompt` (retained in history) instead of `instructions`.
- Raising `ModelRetry` for infrastructure errors (burns the retry budget, confuses the model).
- No `UsageLimits`; unbounded tool loops.
- Sharing one mutable object across concurrent runs via deps.
- Forgetting `ALLOW_MODEL_REQUESTS=False` in tests -> CI hitting real APIs.
- Treating a fast-moving 2.x API as frozen: pin the version and read the upgrade guide.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Pydantic AI docs - overview](https://pydantic.dev/docs/ai/overview/) | docs | Canonical docs: agents, tools, output, MCP, testing, durable execution | intermediate | free |
| [Pydantic AI - Agents](https://pydantic.dev/docs/ai/core-concepts/agent/) | docs | Constructor args, `RunContext`, tools, usage limits, retries | intermediate | free |
| [Pydantic AI - Output](https://pydantic.dev/docs/ai/core-concepts/output/) | docs | Tool/native/prompted output, validators, union outputs | intermediate | free |
| [Pydantic AI - MCP client](https://pydantic.dev/docs/ai/mcp/client/) | docs | `MCPToolset` over stdio and Streamable HTTP | intermediate | free |
| [Pydantic AI - Unit testing](https://pydantic.dev/docs/ai/testing/) | docs | `TestModel`, `FunctionModel`, `override`, `ALLOW_MODEL_REQUESTS` | intermediate | free |
| [Pydantic Evals](https://pydantic.dev/docs/ai/evals/) | docs | Datasets, evaluators, LLM judges, span-based checks | intermediate | free |
| [Pydantic AI V2 announcement](https://pydantic.dev/articles/pydantic-ai-v2) :gem: | article | Capabilities and the Harness; explains the V2 design rationale and breaking changes | intermediate | free |
| [Pydantic AI - Durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) | docs | Temporal/DBOS/Prefect integration and engine trade-offs | advanced | free |
| [Pydantic Logfire docs](https://logfire.pydantic.dev/docs/) | docs | OTel-native observability that pairs with Pydantic AI (or export to Langfuse) | intermediate | freemium |

## Hands-on lab

**Goal:** build the copilot's typed sub-agents and call them from the LangGraph orchestrator. (3 h)

1. `uv add pydantic-ai pydantic-evals httpx` and pin the version in `pyproject.toml`. Put model IDs in config: `LLM_MODEL_SMALL`, `LLM_MODEL_BIG`, with tabs for Anthropic, Azure OpenAI (Microsoft Foundry) and Ollama (`openai-chat:` with a custom base URL/provider).
2. Implement three agents in `copilot/agents/`: `log_agent` (above), `metrics_agent` (tools: `get_service_health`, `query_metric_series`; output `MetricFinding` with `anomalies: list[Anomaly]`), and `runbook_agent` (tool wraps hybrid `search_runbooks`; output `RunbookAnswer` with `citations` validator ensuring every cited ID was retrieved — track retrieved IDs on `deps`).
3. Add `UsageLimits` per agent, output validators with `ModelRetry`, and `instrument=True`; run against the stub backends and Ollama; confirm traces in Langfuse.
4. Wire MCP: expose your stub ops tools through a small MCP server (FastMCP), attach it with `MCPToolset`, and compare tool-selection behaviour with the direct function tools.
5. Write unit tests: `TestModel` smoke test per agent; a `FunctionModel` test that scripts a bad first tool call and asserts the retry produces a valid one; `ALLOW_MODEL_REQUESTS=False` in `conftest.py`.
6. Build a `pydantic_evals.Dataset` for `runbook_agent` (20 cases from the golden set) with evaluators: `citations_exist`, `LLMJudge` for groundedness (use your validated rubric); add a span-based evaluator asserting `search_runbooks` was called at most twice. Run and save the report.
7. Replace the LangGraph `run_agent` stubs with these agents (`await agent.run(..., deps=deps, usage=...)`); re-run the crash/approval tests from the previous labs.
8. Compare cost/latency between a big and a small model for `log_agent` on 20 cases; record in `COSTMODEL.md`.

*Expected:* three typed sub-agents with green unit tests and no network use in CI, an eval report with per-case pass/fail, traces showing per-agent usage, and the LangGraph orchestrator producing structured `findings` from real agents.

## Questions

### L1 — Recall

??? question "Q1. What are `deps_type`, `RunContext` and why do they matter?"
    ??? success "Answer"
        `deps_type` declares the type of dependencies (HTTP client, DB pool, config, user identity) injected at run time; tools, dynamic instructions and validators receive them via `RunContext[Deps]` (`ctx.deps`). It gives typed access, keeps agents free of globals, and makes testing easy by overriding deps with fakes — the same DI pattern that makes FastAPI code testable.

??? question "Q2. What happens when a tool raises `ModelRetry` or output validation fails?"
    ??? success "Answer"
        The message is sent back to the model as a retry prompt (tool return with a retry marker or validation error details), and the model gets another attempt, up to the configured retry budget; exceeding it raises an error. `ModelRetry` is intended for problems the model can fix (bad arguments, missing evidence), not for infrastructure failures.

??? question "Q3. What changed for the `openai:` prefix in Pydantic AI V2?"
    ??? success "Answer"
        The bare `openai:` prefix now uses OpenAI's Responses API instead of Chat Completions. To keep Chat Completions behaviour (needed for many OpenAI-compatible servers such as Ollama or vLLM), use the `openai-chat:` prefix or configure the corresponding model/provider class explicitly.

### L2 — Apply

??? question "Q4. Write a test proving an agent retries after the model calls a tool with invalid arguments, without any network calls."
    ??? success "Answer"
        ```python
        from pydantic_ai import models
        from pydantic_ai.messages import ModelResponse, ToolCallPart, TextPart
        from pydantic_ai.models.function import FunctionModel, AgentInfo

        models.ALLOW_MODEL_REQUESTS = False
        calls = {"n": 0}

        def scripted(messages, info: AgentInfo) -> ModelResponse:
            calls["n"] += 1
            if calls["n"] == 1:
                return ModelResponse(parts=[ToolCallPart("query_logs", {"service": "booking-api", "window_minutes": 999})])
            if calls["n"] == 2:   # after retry prompt about bad window
                return ModelResponse(parts=[ToolCallPart("query_logs", {"service": "booking-api", "window_minutes": 30})])
            return ModelResponse(parts=[ToolCallPart("final_result", {...valid LogFinding fields...})])

        async def test_retry():
            with log_agent.override(model=FunctionModel(scripted)):
                res = await log_agent.run("go", deps=fake_deps())
            assert calls["n"] == 3 and res.output.evidence_ids
        ```
        (The output tool name is `final_result` by default; adjust to your version.) The point: script the model, assert on call counts and the final typed output.

??? question "Q5. Aggregate token usage across a parent agent and a sub-agent called from a tool, with a shared limit."
    ??? success "Answer"
        Pass the parent's usage into the sub-run: `await sub_agent.run(prompt, deps=ctx.deps, usage=ctx.usage)`. The sub-run's tokens/requests accumulate on the same `RunUsage`, and the parent's `UsageLimits` (e.g. `request_limit`, `tool_calls_limit`) apply to the whole tree. Without passing `usage`, the sub-agent's consumption isn't counted and limits are bypassed.

??? question "Q6. The Ollama-backed agent fails with 404 on `/v1/responses` after upgrading to V2. Fix."
    ??? success "Answer"
        V2's bare `openai:` prefix uses the Responses API, which Ollama's OpenAI-compatible endpoint may not implement. Switch to Chat Completions: use `openai-chat:<model>` with the provider configured for `base_url="http://localhost:11434/v1"` (e.g. `OpenAIProvider(base_url=..., api_key="ollama")` and `OpenAIChatModel`), or use the dedicated Ollama provider. Add a startup smoke test per configured model to catch this in CI.

### L3 — Design & trade-offs

??? question "Q7. Pydantic AI as the only framework vs Pydantic AI inside LangGraph. Decide for the copilot."
    ??? success "Answer"
        Pydantic AI alone is sufficient for single-agent typed tool use and simple delegation, with Temporal/DBOS for durability. The copilot needs parallel fan-out, checkpointed state, long human approvals and resumability with streaming — LangGraph's native strengths — so we use LangGraph for orchestration and Pydantic AI for the typed sub-agents (each node one agent run). Downsides: two abstractions and release cadences; mitigate with a thin adapter (`run_agent(name, input, ctx)`), pinned versions, and integration tests. If requirements shrink to a single agent, drop LangGraph.

??? question "Q8. Typed output via tool output vs NativeOutput for the triage agent across Anthropic, Azure OpenAI and local Ollama models."
    ??? success "Answer"
        Default to tool output for portability: it works on all three and integrates with validator retries. Use `NativeOutput` where the provider supports constrained decoding and the schema fits its supported subset (e.g. Anthropic/OpenAI for a high-volume extractor) to eliminate malformed outputs and reduce retries. For small local models, tool calling can be weak — compare tool output vs `PromptedOutput` (or constrained decoding via the server) on the golden set. Make the mode a per-model config and measure valid-output rate, retry rate and latency.

??? question "Q9. Capabilities vs plain toolsets vs subclassing Agent for org-wide standards (e.g. every agent must have PII redaction and cost limits)."
    ??? success "Answer"
        Use capabilities for reusable behaviour bundles (instructions + hooks + settings + tools) that teams opt into or that a factory adds by default (`make_agent(...)` applies `PIIRedaction()` and default `UsageLimits`). Toolsets are for sets of tools only. Subclassing Agent couples teams to your class hierarchy and complicates upgrades. Enforce standards additionally with a lint/CI check that all agents come from the factory, and with gateway-level controls for cost, since capabilities can be bypassed by direct SDK calls.

### L4 — Staff-level ambiguity

??? question "Q10. Pydantic AI releases weekly and V2 just broke defaults. How do you adopt it responsibly across 10 teams?"
    ??? success "Answer"
        Publish an internal `agentkit` wrapper with pinned Pydantic AI versions, shared factory functions, capabilities (tracing, redaction, limits) and lint rules; upgrade centrally on a cadence (e.g. monthly) after running a shared regression suite (unit tests with `TestModel`, golden evals) and reading the changelog; provide codemods for breaking changes (e.g. `openai:` -> `openai-chat:`); allow teams to lag one minor with clear EOL; monitor deprecation warnings in CI. Keep business logic (prompts, tools, schemas) independent of framework internals to reduce migration cost, and evaluate alternatives yearly through an ADR rather than reacting to each release.

??? question "Q11. A team wants to standardise on the OpenAI Agents SDK because 'it's from the model vendor'. How do you steer the decision?"
    ??? success "Answer"
        Compare on requirements, not vendor: multi-provider needs (Azure, Anthropic, local), typing and DI, test tooling, durability, tracing/OTel, protocol support (MCP/A2A/AG-UI), maturity and lock-in. Run a small bake-off implementing the same two agents and golden evals in each; score developer ergonomics, test speed, portability (swap the model with config), operational fit (Microsoft Foundry deployment), and community/maintenance. Often the outcome: a provider-agnostic framework for the platform default with vendor SDKs allowed where their unique features (sandboxes, computer use) justify — documented in an ADR with an exit plan. See [vendor agent SDKs](vendor-agent-sdks.md).

## Real-world use cases

- **Incident copilot sub-agents:** typed findings (logs, metrics, runbooks) with validators guaranteeing evidence IDs.
- **Document extraction services:** `NativeOutput` for high-volume, unions for "extracted | needs_clarification".
- **Internal support bots:** dependency-injected user identity so tool authorisation uses the caller's rights.
- **Agent test suites:** `TestModel`/`FunctionModel` unit tests run in seconds in CI; evals nightly.

## Pitfalls & anti-patterns

- Using `system_prompt` for volatile content; forgetting message-history semantics.
- No usage limits; unbounded retries.
- `ModelRetry` for infrastructure errors.
- Real model calls in unit tests.
- Not pinning versions; ignoring V2 breaking changes.
- Sharing mutable state via deps across concurrent runs.
- Sub-agent runs without passing `usage`, bypassing budgets.

## Checklist

- [ ] I can explain deps/RunContext, output modes, validators and retries
- [ ] I built three typed sub-agents with tools, limits and unit tests using `TestModel`/`FunctionModel`
- [ ] I attached an MCP server via `MCPToolset` and traced runs to Langfuse
- [ ] I ran a `pydantic_evals` dataset with code and judge evaluators
- [ ] I called the agents from LangGraph nodes
- [ ] I answered all L3 questions out loud in < 3 min each
