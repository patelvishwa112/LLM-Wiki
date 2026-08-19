---
tags: ["scaling-laws", "training", "post-training", "moe", "inference", "pretraining", "glm", "models", "rl", "ai-strategy"]
source: https://x.com/jietang/status/2089941544581403107
date: 2026-08-19
type: bookmark
description: "Jie Tang (Zhipu) — multi-dial scaling: params+data+inference+MoE depth; GLM-5.3 post-training-only gains vs 5.2 same base."
author: jietang
summary: "Jie Tang (Zhipu) — multi-dial scaling: params+data+inference+MoE depth; GLM-5.3 post-training-only gains vs 5.2 same base."
raw: "[[raw/jietang_2089941544581403107]]"
---

# Thoughts About Scaling Law (Jie Tang / Zhipu)

@jietang (Tsinghua / Zhipu AI): parameter count alone is the wrong release question. Params only make sense with **data**, **where compute is spent**, and **who runs the model under what load**.

## History of the mis-dials

| Era | Recipe | Lesson |
|-----|--------|--------|
| Kaplan et al. 2020 | Grow params faster than data (~2.7:1) → GPT-3, Gopher, MT-NLG | Fit error compounded at scale; trillion-param generation “detour” |
| Hoffmann / Chinchilla 2022 | ~20 tokens/param; params and data grow together | Optimized **training** compute for train-once, eval-once |
| Inference-dominant | Lifetime cost = serving billions of calls | Optimum → **smaller models over-trained** (Llama-2-7B ~290 TPP; Gemma-2-9B ~889 TPP) |

## MoE: two different “sizes”

- **Total parameters** ≈ knowledge capacity (facts, long tail)  
- **Activated params + effective depth** ≈ how far a causal chain can run before it breaks  

Dense 20:1 TPP does **not** transfer. Roberts et al. (2025): optimal TPP is **task-dependent** — memorization wants more params; reasoning wants more data. MoE follow-ups: at fixed TPP, more total params can **hurt** reasoning; **activating more experts** helps.

Vulnerability hunting analogy: not CVE retrieval — a **twenty-step inference chain** without losing the thread. That lives outside total param count.

## GLM-5.3 as controlled experiment

Same base / architecture / total + activated params as **GLM-5.2**. One month scaling **long-horizon environments + RL** only. Claimed gains “not marginal.” Thesis: after a threshold of world-holding params, capability scales via **effective depth** and especially **post-training**.

## Multi-dial stance

Dials need not turn together; the next dial is rarely last time’s winner. Slack was in post-training this round; mid-training, pretraining, and per-pass compute still on the table. “We are not done scaling.”

## Why it matters

Clean founder-level narrative of scaling-law history + inference-era overtraining + MoE knowledge-vs-reasoning split + post-training as a first-class scale axis. Pairs with Chinchilla-bug notes, GLM slime stack, and frontier RL post-training series.

## Skeptical read

GLM-5.3 product narrative; gains not independently quantified here. Still a sharp conceptual map of dials.

## Related

- [[kaplan-scaling-laws-bug-chinchilla]]
- [[slime-open-source-rl-kernel-glm-dailydose]]
- [[how-frontier-models-train-on-outcomes-2026-sergio]]
- [[controlling-reasoning-effort-in-llms]]
- [[glm-5-2-with-vision-projector-part-harry]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[kimi-k3-memory-savings-jevon-bookwormengr]]
- [[explorative-modeling-third-pretraining-axis-xm]]
- [[training-llm-from-scratch-5-lessons]]
