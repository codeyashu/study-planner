---
title: LLM capacity, latency & cost planning
track: ai-system-design
slug: capacity-cost-planning
priority: P0
complexity: 3
est_hours: 2
phase: 4
tags: [ai-system-design, P0]
last_reviewed: 2026-09-25
---

# LLM capacity, latency & cost planning

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 3/5 · **Est. time:** 2 h · **Phase:** 4 · **Prereqs:** [Framework](framework.md), [Estimation basics](../system-design/framework-and-estimation.md), [Cost & latency optimization](../agentic-ai/cost-latency-optimization.md), [Inference serving](../agentic-ai/inference-serving.md)
    **You're done when:** in under 5 minutes you can produce a defensible token, latency, GPU-or-API-cost and rate-limit estimate for any LLM feature, name the three biggest cost levers with expected savings, and state the assumptions that would change your answer.

This page is a **toolkit** rather than one design problem: it is the estimation chapter every other design in this track leans on. It follows the design-walkthrough style where useful.

## Why it matters

LLM cost and latency are first-class non-functional requirements. Interviewers use the estimation step to test whether you understand what actually drives cost (input tokens, output tokens, cache hits, model tier, agent loop length) and latency (TTFT, TPOT, retrieval, tool calls). In real projects, a design that ignores these usually dies at the first finance review or rate-limit incident.

## Core concepts

### 1. The unit economics equation

```text
cost/request = (uncached_in × P_in) + (cached_in × P_cache_read) + (cache_writes × P_cache_write)
             + (reasoning_tokens + output_tokens) × P_out  + tools/retrieval/infra
cost/month   = requests/month × cost/request
```

Facts to know (state prices as assumptions; they move quarterly):

- Output tokens cost roughly 4–6× input tokens at major providers; reasoning ("thinking") tokens bill as output.
- Cached input reads are typically ~10% of base input price (Anthropic and OpenAI both offer prompt caching; Anthropic charges a premium for cache writes and requires explicit cache breakpoints, OpenAI caches automatically above a minimum prefix length). Batch APIs give ~50% off for async work.
- Small/fast model tiers are commonly 5–20× cheaper than frontier tiers.
- Token estimate: ~4 characters or ~0.75 English words per token; code and non-Latin scripts use more tokens per character.

### 2. Latency model

```text
E2E ≈ network + gateway + retrieval + rerank + guardrails + TTFT + (output_tokens × TPOT) + tool round-trips
TTFT ≈ queueing + prefill(input_tokens)   # prefill is compute-bound, roughly linear in prompt length
TPOT ≈ 1 / decode speed                   # memory-bandwidth-bound; ~10–100 tok/s per stream depending on model/hardware
```

Typical planning numbers (assumptions; measure): frontier API TTFT 0.4–2 s, decode 40–120 tok/s; small models TTFT 0.2–0.6 s, 100–250 tok/s; reasoning models can spend 5–60 s "thinking" before the first visible token. Streaming makes perceived latency ≈ TTFT; batch/async jobs don't care.

An agent with N sequential steps multiplies: `E2E ≈ N × (TTFT + out × TPOT + tool_latency)`. Ten steps at 3 s = 30 s — design UX (progress events, AG-UI) accordingly.

### 3. Rate limits and concurrency

Providers limit **RPM, input TPM and output TPM** per deployment. Plan with:

```text
peak_TPM = peak_RPS × 60 × (avg_in + avg_out)
concurrent_streams = peak_RPS × avg_generation_seconds      # Little's law
```

If peak_TPM exceeds a single deployment's quota: multiple deployments/regions/providers behind a [gateway](llm-gateway.md), provisioned throughput for the baseline, PAYG for bursts, queues + priority classes for batch.

### 4. Self-hosted GPU sizing

```text
weights_GB  = params × bytes_per_param            (FP16 2, FP8 1, INT4 0.5)
KV_per_token = 2 × layers × kv_heads × head_dim × bytes
concurrent_seqs ≈ (GPU_mem_total × 0.9 − weights_GB) / (avg_ctx × KV_per_token)
decode_tok/s per stream ≤ HBM_bandwidth / weights_bytes (batch 1); aggregate scales with batch until compute/KV-bound
GPUs_needed = ceil(peak_output_tok_s / benchmarked_tok_s_per_GPU_at_SLO) × (1 + headroom) + N+1 spare
```

Always replace the benchmark term with a real load test (see [serving platform](llm-serving-platform.md)). Break-even: self-host wins only at sustained utilisation (rule of thumb > 50–60%) for a narrow task where a smaller model passes your evals.

### 5. The cost levers (ordered by typical ROI)

| Lever | Typical effect | Watch out |
|---|---|---|
| Prompt caching (static prefix first) | −30–70% input cost for long stable prefixes; lower TTFT | Prefix must be byte-identical; write premium; TTL |
| Model routing / cascades | −40–80% at same quality on easy-majority traffic | Needs per-slice evals; escalation latency |
| Context diet (fewer/better chunks, summaries, tool-output trimming) | −20–50% input | Recall risk — measure |
| Output control (concise format, max_tokens, structured outputs) | −10–40% output | Truncation bugs |
| Batch APIs for async work | −50% | Latency of hours |
| Semantic/exact response cache | Variable, often low for personalised traffic | Wrong/leaked answers |
| Fine-tuned small model for narrow task | −80–95% | Data + MLOps effort |
| Agent loop limits, early stopping | Avoids tail cost | Quality cliffs |
| Speculative decoding, quantisation (self-hosted) | 1.5–3× throughput | Eval parity |

### 6. Worked example — shipment tracking assistant

```text
Given: 50k B2B customers × 5 turns/week ≈ 1M turns/month; peak 12 turns/s (Monday morning)
Turn: system+tools 2.5k (cacheable) + history 1.5k + 5 chunks 2.5k + question 0.1k = 6.6k input; 350 output
Prices (assumed): frontier $3/M in, $0.30/M cached, $15/M out; small $0.30/M in, $1.5/M out
Baseline all-frontier, no cache: in 6.6B × $3/M = $19.8k; out 0.35B × $15/M = $5.25k → $25k/month
+ prompt cache on 2.5k prefix at 90% hit: saves 1M × 2.5k × 0.9 × $2.7/M ≈ $6.1k → $19k
+ route 65% of turns (status lookups) to small model: on those turns cost drops ~90% → 
    remaining: 35% × $19k ≈ $6.7k + 65% × ~$1.9k ≈ $1.2k → ~$7.9k/month
+ trim to 4 chunks and cap output at 250 tokens → ~$6.5k/month (−74% vs baseline)
Latency budget (p95 TTFT 1.2 s): guardrail 100 + retrieval 120 + rerank 120 + TTFT (cached) 500 + gateway 30 = ~870 ms
Rate limits: 12 turns/s × 60 × 7k tokens = ~5M TPM peak → needs pooled deployments; a 1M TPM quota is not enough
Concurrent streams: 12 × 6 s = ~72 (tiny) → capacity problem is TPM quota, not connections
```

### 7. Senior-level nuance

- **Cost per *successful task*, not per call**: retries, agent loops and human escalations are part of cost. Track `cost / resolved_conversation`.
- **Tail matters**: p99 requests (giant contexts, runaway loops) can be 30% of spend. Cap them.
- **Long context isn't free**: cost linear in tokens, prefill latency grows, quality can degrade with distractors.
- **Provisioned throughput** trades flexibility for price/latency predictability; pool it across teams via a gateway.
- **Forecast with distributions**, not averages: token counts are heavy-tailed. Use p50/p90/p99 from sampled traces.
- **Re-plan quarterly**: prices fall and model tiers shift; keep the model in a spreadsheet/notebook with assumptions as inputs.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [Transformer Inference Arithmetic (kipply)](https://kipp.ly/p/transformer-inference-arithmetic) :gem: | article | First-principles memory, FLOPs and latency math | advanced | free |
| [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) :gem: | book | Roofline thinking for accelerators | advanced | free |
| [LLM Inference Performance Engineering (Databricks)](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices) | article | TTFT/TPOT definitions and hardware trade-offs | intermediate | free |
| [Prompt caching (Claude docs)](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) | docs | Breakpoints, TTLs, pricing multipliers | intermediate | free |
| [Prompt caching (OpenAI docs)](https://platform.openai.com/docs/guides/prompt-caching) | docs | Automatic caching rules | intermediate | free |
| [Batch processing (Claude docs)](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) | docs | Async discount mechanics | intermediate | free |
| [RouteLLM (LMSYS)](https://lmsys.org/blog/2024-07-01-routellm/) | article | Cost/quality curves for routing | advanced | free |
| [vLLM automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html) | docs | Self-hosted equivalent of prompt caching | intermediate | free |
| [AI Engineering (Chip Huyen)](https://github.com/chiphuyen/aie-book) | book | Inference cost/latency optimisation chapter | advanced | paid |

## Hands-on lab

**Goal (60–90 min):** build a reusable estimator notebook and calibrate it with real traces.

1. In a Python notebook (or spreadsheet) define inputs: requests/day, token distributions (p50/p90), cache-hit rate, price table, routing split. Output: $/month, peak TPM, concurrent streams, latency budget.
2. Instrument a small LLM app (your capstone) to log input/output/cached tokens per call; compare measured averages to your assumed ones.
3. Apply three levers one at a time and record the delta; verify quality with a small eval set.
4. **Expected output:** a notebook plus a table "assumed vs measured" and a one-paragraph recommendation.

## Questions

### L1 — Recall

??? question "Q1. Why does the order of content in a prompt matter for cost?"
    ??? success "Answer"
        Prompt caching matches on an exact prefix. Static content (system prompt, tool definitions, few-shot examples) must come first and dynamic content (retrieved chunks, user input) after; any change early in the prompt invalidates the cache for everything after it.

??? question "Q2. What are TTFT and TPOT, and which phases determine them?"
    ??? success "Answer"
        Time to first token is dominated by queueing and prefill (compute-bound, grows with prompt length). Time per output token is decode speed (memory-bandwidth-bound). Total generation time ≈ TTFT + output_tokens × TPOT.

??? question "Q3. Why do reasoning models complicate cost estimates?"
    ??? success "Answer"
        Hidden thinking tokens are billed as output tokens and add seconds of latency before the first visible token; their count varies by problem difficulty, so cost is heavy-tailed. Budget with thinking limits and measure distributions per task type.

### L2 — Apply

??? question "Q4. 3M requests/month, 5k input (60% cacheable prefix, 90% hit), 400 output. Prices (assumed): $3/M in, $0.30/M cached, $15/M out. Monthly cost?"
    ??? success "Answer"
        Cacheable tokens: 3M × 3,000 × 0.9 = 8.1B → $2,430; uncached input: 3M × 5,000 = 15B minus 8.1B = 6.9B → $20,700; output: 1.2B × $15/M = $18,000. Total ≈ **$41.1k**. Without caching input would be 15B × $3 = $45k → total $63k; caching saves ~35%.

??? question "Q5. Peak 40 RPS, avg 3k in + 500 out, generation ~8 s. Compute peak TPM and concurrent streams."
    ??? success "Answer"
        TPM = 40 × 60 × 3,500 = 8.4M tokens/min (input and output limits may be separate: 7.2M in, 1.2M out). Concurrent streams = 40 × 8 = 320. Check both against the provider's TPM and concurrency quotas; likely need multiple deployments or provisioned capacity.

??? question "Q6. An 8B model (GQA: 32 layers, 8 KV heads, head_dim 128), FP16 weights, on an 80 GB GPU with 4k average context. How many concurrent sequences fit?"
    ??? success "Answer"
        Weights 16 GB; usable memory ≈ 0.9 × 80 = 72 GB → ~56 GB left for KV. KV/token = 2×32×8×128×2 B = 131 KB → 4k tokens ≈ 0.54 GB/seq → ~104 concurrent sequences (less with fragmentation/overheads; FP8 KV doubles it).

### L3 — Design & trade-offs

??? question "Q7. Your CFO wants a 50% cost cut in one quarter without quality loss. Prioritise levers."
    ??? success "Answer"
        Decompose spend by feature/model/token type from gateway logs. Ordered plan: (1) caching fixes — days, low risk; (2) context diet on the top-3 spending features — weeks; (3) routing/cascade for easy-majority traffic with eval gates — weeks; (4) batch APIs for async workloads; (5) output caps. Track quality on golden sets per slice as guardrail; stop a lever if a critical slice regresses. Report cost per successful task weekly.

??? question "Q8. Provisioned throughput vs pay-as-you-go for an interactive assistant with 5× peak/avg ratio?"
    ??? success "Answer"
        Provision to the baseline (roughly the p50–p70 load) where utilisation stays high, and burst on PAYG (or a second provider) for peaks. Provisioning for the peak wastes money ~80% of the time. Pool provisioned capacity across teams via a gateway to raise utilisation; batch workloads fill troughs.

??? question "Q9. Would you self-host for a workload of 200M output tokens/month?"
    ??? success "Answer"
        Probably not. At an assumed $10/M output, the API cost is ~$2k/month — less than one GPU (~$2k+/month) plus engineering time. Self-hosting starts making sense when API spend reaches tens of thousands per month at steady load, data residency forces it, or latency/customisation needs demand it. Run the break-even with real utilisation.

### L4 — Staff-level ambiguity

??? question "Q10. Costs are unpredictable month to month as teams launch agents. Design a FinOps approach for LLM spend."
    ??? success "Answer"
        Central gateway with per-team virtual keys, budgets, and tagging (feature, environment, tenant); dashboards for cost per successful task; forecasting from token distributions; budget alerts at 50/80/100% and graceful degradation policies; a pre-launch cost review for agent features (loop limits, per-run caps, expected cost distribution from load tests); monthly review with finance; chargeback to teams. Provide a shared estimator template so teams forecast consistently.

??? question "Q11. Vendor prices dropped 60% but total spend went up. How do you explain and manage it?"
    ??? success "Answer"
        Cheaper tokens increase usage (Jevons effect) and teams shift to bigger contexts, reasoning models and agent loops. Report unit cost (per successful task) and total spend separately; check whether spend growth maps to product value (adoption, resolved tasks). Apply governance where tokens/task grew without quality gains (context bloat, unbounded loops), and invest savings in evals and routing rather than assuming price drops solve cost.

## Real-world use cases

- **Shipment tracking assistant** costing above.
- **Bulk document extraction**: batch APIs and small models dominate; estimate per document and reviewer time (see [Document processing](document-processing.md)).
- **Enterprise assistant rollout to 100k employees**: TPM quota and provisioned throughput planning before launch day.
- **Agent platform budgets**: per-run caps derived from load-tested cost distributions ([Agent platform](agent-platform.md)).

## Pitfalls & anti-patterns

- Averaging token counts and ignoring heavy tails.
- Forgetting output/reasoning tokens or multi-call agent loops in estimates.
- Presenting prices as facts instead of dated assumptions.
- Computing GPU needs from spec-sheet FLOPs instead of measured throughput at SLO.
- Optimising cost without a quality guardrail.
- Planning for average load and ignoring quota limits at peak.

## Checklist

- [ ] I can do a full token → cost → TPM → latency estimate in 5 minutes
- [ ] I can compute KV cache size and concurrency for a given GPU
- [ ] I can rank cost levers with expected savings and risks
- [ ] I built the estimator notebook and calibrated it with real traces
- [ ] I answered all L3 questions out loud in < 3 min each
