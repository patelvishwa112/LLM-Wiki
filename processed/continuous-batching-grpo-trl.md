---
tags: [trl, grpo, continuous-batching, rl, rollouts, huggingface, agent-training, kv-cache, logprobs, rloo]
source: https://x.com/sergiopaniego/status/2067946867237818830
type: concept
ingested: 2026-06-20
related: [[agent-harness], [agents], [rlm-agents-structured-outputs]]
---

# Continuous Batching for GRPO Rollouts in TRL

**Source:** [X Post by @sergiopaniego](https://x.com/sergiopaniego/status/2067946867237818830) (Hugging Face)

## Summary

Sergio Paniego details an efficiency improvement for online RL training in TRL: **continuous batching for GRPO (and RLOO) rollouts**.

Instead of the default `generate()` (wasteful for high-N variable-length completions) or external vLLM, a new in-process path (`use_continuous_batching=True`) recycles KV cache slots dynamically. Benefits:
- ~1.25x faster at N=64
- Lower VRAM (avoids max-length pre-allocation)
- Proper logprobs capture (fixes prior paged attention issues that broke importance sampling)
- Tunable `max_memory_percent` (default 0.5) to protect backward pass
- CUDA graphs disabled due to per-step weight changes

Requires `transformers>=5.8.0`. Ships in next TRL release; currently on main. Includes PR #5765, benchmarks, and example scripts.

## Why It Matters

This directly advances high-throughput agent/RL training infrastructure — critical for scaling rollouts, agent traces, and online RL loops without external dependencies. It exemplifies the "harness engineering" discipline: squeezing performance out of the generation step that dominates agent training time. Strong connection to agent-harness patterns, structured outputs, and efficient multi-turn/rollout systems.

Complements prior work from the same author on releasing large-scale agent traces (504 verified multi-turn trajectories) and profiling tools.

## Key Technical Details
- Flag: `use_continuous_batching=True`
- KV cache recycling for variable-length generations (math, reasoning)
- Logprobs support for importance sampling correction
- Memory headroom for training backward pass

## Related
- [[agent-harness]] and rollout optimization
- GRPO / RLOO trainers in TRL
- Hugging Face transformers / TRL ecosystem
- Agent traces and trajectory data (related Sergio posts)