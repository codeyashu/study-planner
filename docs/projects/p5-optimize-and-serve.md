---
title: "P5: Optimise and serve"
tags: [projects, phase-5, agentic-ai, dspy, inference, fine-tuning]
last_reviewed: 2026-09-25
---

# P5: Optimise and serve

!!! abstract "At a glance"
    **Phase:** 5 · **Weeks:** 18–20 (~12 h build; Saturday blocks) · **Feeds:** capstone M6, ADR 0012 revisit, stretch goals
    **Goal:** Three linked experiments on one capstone task (exception classification + action planning):
    (1) **program optimisation** with DSPy (MIPROv2 and GEPA) vs hand-written prompts;
    (2) **serving benchmark** of an open model on Ollama vs vLLM (quantisation levels, concurrency);
    (3) **LoRA fine-tune** of a small model for the classifier.
    End with a **go/no-go memo** recommending which (if any) goes to production, with cost, latency and quality evidence.
    **Done when:** the memo makes a clear recommendation backed by three results tables and a total-cost-of-ownership estimate.

## Why this project

Staff/AI-architect interviews increasingly ask "prompt, optimise, or fine-tune?" and "API or self-host?". Most candidates answer from blog posts. You will answer from your own numbers, and you will have practised writing the decision memo a Principal engineer writes for leadership.

## Skills practised

- [DSPy](../tracks/agentic-ai/dspy.md): signatures, modules, metrics, MIPROv2, GEPA
- [Inference serving](../tracks/agentic-ai/inference-serving.md): continuous batching, KV cache, quantisation, throughput vs latency
- [Fine-tuning](../tracks/agentic-ai/fine-tuning.md): LoRA/QLoRA with TRL or Unsloth, data prep, overfitting checks
- [Cost and latency optimisation](../tracks/agentic-ai/cost-latency-optimization.md), [capacity and cost planning](../tracks/ai-system-design/capacity-cost-planning.md), [LLM serving platform](../tracks/ai-system-design/llm-serving-platform.md)
- [Decision making](../tracks/staff-skills/decision-making.md), [design docs and RFCs](../tracks/staff-skills/design-docs-rfcs.md)
- [Performance profiling](../tracks/python/performance-profiling.md)

## Spec

### Task and data

- **Task A (classification):** exception event text → one of ~12 exception types + severity. Easy to measure; good fine-tune candidate.
- **Task B (planning):** case context → structured action plan; metric = plan matches acceptable plans + judge score. Good DSPy candidate.
- **Data:** 600+ labelled classification examples (synthetic with human spot-check of 150), split train/dev/test 60/20/20 and **frozen**; 120 planning cases from P3 scenarios expanded. Never tune on test.

### Experiment 1: DSPy

| Arm | Description |
|---|---|
| Baseline | Your best hand prompt from the capstone |
| DSPy zero-shot | `dspy.Predict` / `ChainOfThought` with a clean signature |
| MIPROv2 | Instruction + few-shot optimisation |
| GEPA | Reflective prompt evolution with textual feedback from the metric |
| Cross-model | Optimise on a small/cheap model; evaluate transfer to another model |

Report: accuracy/F1 (A), plan score (B), optimisation cost ($ and wall time), tokens per inference, and whether gains hold on the test set.

### Experiment 2: Serving benchmark

| Dimension | Levels |
|---|---|
| Engine | Ollama (llama.cpp backend) on laptop; vLLM on a rented single GPU for ~2–4 h (optional SGLang) |
| Model | One 7–8B instruct model; one 1–3B model |
| Quantisation | FP16/BF16 (vLLM), 8-bit, 4-bit (GGUF Q4_K_M / AWQ or GPTQ) |
| Concurrency | 1, 4, 16, 64 concurrent requests |
| Workload | Task A prompts (short in, short out) and RAG prompts (long in, medium out) |

Metrics: time-to-first-token p50/p95, inter-token latency, output tokens/s per request and aggregate, max concurrency within a p95 SLO, GPU memory, $/1M output tokens (GPU $/h ÷ aggregate throughput), and quality delta from quantisation on Task A.

### Experiment 3: LoRA fine-tune

- Fine-tune a 1–3B model on Task A train split with LoRA/QLoRA (Unsloth or TRL `SFTTrainer`) on a free/cheap GPU (Colab/Kaggle or rented).
- Compare with: prompt-only large model, DSPy-optimised small model, fine-tuned small model.
- Check: learning curves (train vs dev loss), confusion matrix, robustness on a perturbed test set (typos, new phrasing), latency and cost when served via Ollama.

### Go/no-go memo (1–2 pages)

```text
Title: Should the Ops Copilot classifier move off the frontier API?
1. Recommendation (one paragraph, with confidence)
2. Context and decision criteria (quality floor, p95 SLO, $/month, ops burden)
3. Options compared (table: quality, p95, $/1k requests, ops effort, risk)
4. Evidence (links to experiment tables)
5. Risks and mitigations (drift, retraining cadence, GPU availability, security)
6. Decision triggers to revisit (volume > X/day, price change, new model release)
7. Cost of reversal
```

## Step-by-step plan

| Step | When | What |
|---|---|---|
| 1 | Wk 18 weekdays | Freeze datasets; metrics as Python functions with tests |
| 2 | Wk 18 Sat | DSPy baseline + MIPROv2 on Task A; GEPA on Task B |
| 3 | Wk 18 Sun | Cross-model transfer; results table; wire best module into capstone behind a flag |
| 4 | Wk 19 weekdays | Benchmark harness (async load generator, records TTFT/ITL); Ollama runs locally |
| 5 | Wk 19 Sat | vLLM runs on rented GPU (script everything first; time-box the rental); quantisation quality check |
| 6 | Wk 19 Sun | LoRA fine-tune on Task A; evaluate |
| 7 | Wk 20 weekdays | TCO model: API cost vs self-host at 1k, 10k, 100k requests/day |
| 8 | Wk 20 Sat/Sun | Memo + write-up + ADR (revisit 0012 routing) |

## Acceptance criteria

- [ ] Frozen train/dev/test with hashes recorded; no test leakage (documented)
- [ ] DSPy table: baseline vs >= 2 optimisers on both tasks, with optimisation cost
- [ ] Serving table: >= 2 engines × >= 2 quantisation levels × 4 concurrency levels, with TTFT p95 and aggregate tok/s
- [ ] Throughput-vs-latency plot identifying the max concurrency meeting a stated SLO
- [ ] Fine-tune results with learning curves and confusion matrix; overfitting check
- [ ] TCO table at three volumes including engineering/ops time, not just GPU $
- [ ] Memo gives an unambiguous go/no-go per option and revisit triggers
- [ ] Total spend on GPUs + APIs for P5 <= $25

## Stretch

- GRPO/DPO small experiment on Task B with Unsloth; compare with SFT.
- Speculative decoding or prefix caching in vLLM for RAG prompts.
- Serve the fine-tuned adapter via vLLM multi-LoRA and route to it from LiteLLM.
- Free-threaded Python 3.14t for the load generator vs asyncio (CPU-bound metric computation).

## Deliverables

1. `experiments/p5-optimise-serve/` (DSPy programs, benchmark harness, fine-tune notebook, results)
2. Go/no-go memo in `docs/writeups/`
3. Write-up: *"Prompt, optimise, or fine-tune? Numbers from one ops task"* (publishable)
4. ADR updates (routing, model choice); capstone flag for optimised module (M6)

## Rubric

Generic [rubric](rubric.md) plus:

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Experimental hygiene | Tuned on test | Splits exist, not frozen | Frozen splits, fixed seeds, costs recorded | Plus variance across runs and perturbation robustness |
| DSPy depth | Ran an example | One optimiser, one task | Two optimisers, two tasks, transfer test | Plus analysis of *why* optimised prompts work (inspect instructions/demos) |
| Serving benchmark | Single request timing | Throughput only | TTFT/ITL/throughput vs concurrency with SLO | Plus quantisation quality delta and $/1M tokens |
| Fine-tune | Training ran | Eval on dev only | Test + confusion matrix + learning curves | Plus data-quality ablation (100 vs 300 vs all examples) |
| Decision memo | Summary of results | Recommendation without criteria | Criteria-driven recommendation with TCO | Plus revisit triggers, reversal cost, stakeholder framing |

## Resources

| Resource | Why |
|---|---|
| [DSPy docs](https://dspy.ai/) | Signatures, optimisers incl. GEPA |
| [Hugging Face cookbook: DSPy GEPA](https://huggingface.co/learn/cookbook/dspy_gepa) | Worked GEPA example |
| [The Data Quarry: Learning DSPy, optimisers](https://thedataquarry.com/blog/learning-dspy-3-working-with-optimizers/) :gem: | Clear explanation of how optimisers behave |
| [vLLM docs](https://docs.vllm.ai/) | Serving, benchmarking, quantisation |
| [SGLang docs](https://docs.sglang.ai/) | Alternative engine |
| [Ollama](https://ollama.com) | Local serving |
| [TRL docs](https://huggingface.co/docs/trl) | SFT, DPO, GRPO trainers |
| [Unsloth RL guide](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) | Efficient LoRA/RL fine-tuning |
| [Hugging Face LLM course](https://huggingface.co/learn/llm-course) | Fine-tuning fundamentals |
| [Chip Huyen: AI Engineering (book repo)](https://github.com/chiphuyen/aie-book) | Fine-tune vs prompt decision framing |
