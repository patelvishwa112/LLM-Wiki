---
type: article
description: "Alvin ZH on Ouro looped transformers: accuracy peaks then overthinks past trained recurrence; at trained depth, one episodic entropy TTT step on 97 RMSNorm scales lifts GSM8K ~+8 pts and beats deeper looping — signal must be read at trained depth and mostly caches as prompt calibration."
tags: ["training", "inference", "test-time-training", "looped-transformers", "architecture", "llm", "math", "ouro", "entropy", "adaptation", "ml-research"]
source: https://alvinzh04.github.io/blog/looped-ttt.html
date: 2026-07-14
author: AlvinZH04
summary: "Alvin ZH on Ouro looped transformers: accuracy peaks then overthinks past trained recurrence; at trained depth, one episodic entropy TTT step on 97 RMSNorm scales lifts GSM8K ~+8 pts and beats deeper looping — signal must be read at trained depth and mostly caches as prompt calibration."
raw: "[[raw/alvinzh04_looped_ttt]]"
---

# Loop deeper, or adapt? Test-time training in looped transformers

Technical blog by **Alvin ZH** (@AlvinZH04) exploring **test-time training (TTT)** on **looped (recurrent-depth) transformers** — specifically Ouro-1.4B/2.6B base models. Organizing question: with spare test-time compute, **loop deeper or adapt weights**?

Code: [github.com/AlvinZH04/Loop-TTT](https://github.com/AlvinZH04/Loop-TTT)

## Setup (minimal recipe)

- Model reuses a 24-layer recurrent core for `r` steps (trained max depth **r=4**).
- Adapt only **97 RMSNorm scale vectors** (~0.014% of params; 96 in-loop felt every recurrence + 1 readout) via **one Adam step** on a **target-label-free** objective.
- Default: **strict-masked mean entropy** over prompt tokens (Tent-style), **batch-episodic** (shared update for batch B, then restore φ₀).
- Primary: four-shot GSM8K CoT; also MATH-500 (zero-shot step-by-step), MMLU subset.

## Key findings

### 1. Loop depth: reason then overthink
GSM8K climbs with recurrence to **trained depth r=4**, then **falls** (r=16 collapses). Same inverse-U shape as token-level overthinking literature, along **latent depth**.

### 2. Narrow window where adapt beats loop
At **r=4**, one entropy step: **0.766 → 0.848** (+8.2, n=500) and beats decoding at r=8. Below peak, just loop (r1→r2 ~+40 pts). Past peak, matched-depth adaptation is harmful; **read signal at trained depth** is the reliable rule.

### 3. Design space (defaults win)
| Knob | Winner | Collapse modes |
|------|--------|----------------|
| Tokens | **Prompt** before decode | Prefix/online weaker |
| Reset | **Episodic per batch** | Continual ≈ −15.6 |
| Adapt depth m | **m=4 (trained)** | m=1/2 catastrophic; m=8 collapse |
| Steps s | **s=1** | More overfits |
| Objective | **Entropy > LM loss** | +8.2 vs +3.4 |

### 4. Is it the loop?
Performance-matched **Qwen2.5-3B** (non-looped) shows ~flat s=1 entropy update; Ouro gets large lift. Suggests **recurrent reuse amplifies** tiny scale updates — not a pure causal isolation (different arch/history).

### 5. Transfer
- **MATH-500**: entropy TTT +3.0; LM-loss **hurts**.
- **MMLU subset**: depth inverse-U holds; entropy TTT **~neutral** (letter logits).
- **Ouro-2.6B**: same depth pattern (gentler); needs ~4× smaller LR; smaller TTT gains (~+1.7–3.4).

### 6. Mostly reusable calibration
Most GSM8K gain is from **shared few-shot exemplars** (cosine ~0.99 across batches). Fixed cached vector / offline-distilled RMSNorm delta recover much of full online TTT — so “test-time training” here is largely **cacheable prompt calibration**, not per-instance adaptation.

pass@K: gains **front-loaded** (large pass@1, smaller by pass@8).

## Why it matters

Tight empirical map of **test-time compute for looped LMs**: depth dial ≠ free lunch past training; **where you read the adaptation signal** (trained recurrence) matters as much as whether you adapt. Connects Tent/entropy minimization literature to **shared-weight recurrence amplification** and practical packaging as static calibration vectors.

## Caveats (author-aligned)

Not wall-clock-matched vs deeper decode; Ouro-specific; Qwen control imperfect; MMLU/T TT split shows recipe is generative-math-skewed; overthinking analogy is operational not mechanistic identity.

## Related

- [[design-good-ml-experiments-grigorev]]
- [[kaplan-scaling-laws-bug-chinchilla]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[speculative-decoding-history-roofline-shreybirmiwal]]
- [[how-to-use-rlms-in-deep-agents]]
- [[portal-portable-task-adapters-llms]]
- [[training-llm-from-scratch-5-lessons]]
- [[how-to-build-diffusion-language-model-kuleshov]]
