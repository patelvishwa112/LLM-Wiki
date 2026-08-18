---
tags: ["papers", "evals", "reward-models", "reasoning", "inference-scaling", "rl", "training", "post-training", "deepmind", "verification", "llm-judges"]
source: https://arxiv.org/abs/2408.15240
date: 2025-02
type: paper
description: "DeepMind GenRM (ICLR 2025) — train verifiers as next-token Yes/No (+ CoT); Best-of-N beats discriminative RM and LLM-as-Judge; easy-to-hard MATH gains."
author: zhang-et-al-deepmind
summary: "DeepMind GenRM (ICLR 2025) — train verifiers as next-token Yes/No (+ CoT); Best-of-N beats discriminative RM and LLM-as-Judge; easy-to-hard MATH gains."
raw: "[[raw/arxiv_2408.15240_generative_verifiers_genrm]]"
arxiv: "2408.15240"
venue: "ICLR 2025"
---

# Generative Verifiers (GenRM) — reward modeling as next-token prediction

Zhang, Hosseini, Bansal, Kazemi, Kumar, Agarwal (Google DeepMind et al.), **ICLR 2025**. arXiv:2408.15240. Project: [generative-reward-models](https://sites.google.com/view/generative-reward-models).

## Claim

Best-of-N reasoning quality is bottlenecked by the **verifier**. Standard LLM verifiers are **discriminative** classifiers (scalar / binary CE) and throw away pretrained generation. **GenRM** trains verification with ordinary **next-token prediction** so the model can use instruction tuning, CoT, and test-time compute.

## Method

| Variant | Train | Score |
|---------|-------|-------|
| **GenRM** | SFT to emit Yes/No to “Is the answer correct?” | P(Yes ∣ problem, solution) |
| **GenRM-CoT** | SFT CoT critique **then** Yes/No (synthetic rationales OK) | Average P(Yes) over multiple sampled CoTs |

Can jointly train solution generation + verification under one NTP objective (transfer; harder with DPO-style verifiers).

**Motivating example (GSM8K):** solution misses “each” in pricing; discriminative RM ≈ 0.999 “correct”; GenRM-CoT flags the bad step → No; majority-vote score tiny.

## Headline results (paper)

- Algorithmic Best-of-N: **~5% → 45.3%**
- GSM8K (Gemma2-9B GenRM-CoT on Gemini 1.0 Pro candidates): **73% → 93.4%**
- Easy-to-hard **MATH500** (train GSM-level only): **28% → 44.6%**
- MMLU abstract algebra: **37.9% → 53.5%**
- Beats discriminative RMs, **DPO** verifiers, LLM-as-a-Judge; scales with data, model size, verification samples

## Why it matters

Unifies generation and verification under the LM objective. Gives a clean **test-time compute** knob on the verifier (more CoT samples) without only scaling generator N. Synthetic process critiques suffice for subtle error catching. Core building block for process reward / Best-of-N / agent eval stacks.

## Caveats

BoN gains need diverse candidates; multi-sample CoT verification is expensive; results task/setup-specific. Wiki raw is a condensed extract — cite PDF for numbers in tables.

## Related

- [[generative-verifiers-genrm-marfinxx]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[how-frontier-models-train-on-outcomes-2026-sergio]]
- [[controlling-reasoning-effort-in-llms]]
- [[rlhf-from-first-principles]]
- [[dair-ai-ten-papers-co-evolving-agents-verification]]
