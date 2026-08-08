---
tags: ["agents", "training", "rl", "sft", "recursive-self-improvement", "meta-evolution", "evals", "mle", "openmle", "evolutionary-search", "slm"]
source: https://x.com/neural_avb/status/2086073348531110130
date: 2026-08-08
type: bookmark
description: "neural_avb on OpenMLE / Frontis-MA1 — meta-evolution trains Draft/Improve/Debug/Crossover operators so a 35B SLM beats frontier stacks on MLE tasks under a 12 GPU-hour budget."
author: neural_avb
summary: "neural_avb on OpenMLE / Frontis-MA1 — meta-evolution trains Draft/Improve/Debug/Crossover operators so a 35B SLM beats frontier stacks on MLE tasks under a 12 GPU-hour budget."
raw: "[[raw/neural_avb_2086073348531110130]]"
paper_url: http://arxiv.org/abs/2607.28568
---

# Frontis-MA1 / OpenMLE (neural_avb)

Breakdown of **OpenMLE** and finetuned model **Frontis-MA1**. Frame: not full RSI, but **meta-evolution** on the ML-engineering (MLE) domain.

## Claim

Start from **Qwen3.6-35B-A3B**, finetune under a strict **~12 GPU-hour per-task** budget (RTX 4090-class feasible). Resulting **Frontis-MA1 (35B)** beats **GPT-5.5 + Codex** and **Kimi K3** on MLE tasks (paper claims).

## Four learned operators (same base model + sandbox)

1. **Draft** — new program from scratch  
2. **Improve** — better a parent program  
3. **Debug** — fix from error signals  
4. **Crossover** — combine two parents  

Each gets a different bounded context slice; output is executed Python scored in a sandbox.

## Training recipe

1. **SFT warm start** — generate, execute, keep high-scoring valid trajectories; difficulty-aware sampling  
2. **RL** — sandbox score as reward  
3. **Long-horizon evolutionary search (inference)** — population search with experience board, novelty-aware parent selection, on-demand memory synthesis, operator-conditioned context

## Experience board (inference-time)

- Experience cards: provenance, score, error type, resources  
- Method families, best-per-family, underexplored directions, repeated failures  
- Parent selection uses more than raw fitness (avoids local optima)

## Ladder (paper’s distinction)

| Rung | Meaning |
|------|---------|
| Evolution/search | Fixed algorithm mutates candidates (e.g. AlphaEvolve-style) |
| **Meta-evolution** | Operators/searcher learned from past search trajectories ← Frontis |
| True RSI | Improved system further improves the *improver* process itself |

Quoting the paper’s stance (via post): meta-evolution reuses evolutionary trajectories to train the proposer of future modifications; full RSI needs a sustained loop where each upgraded system improves the process that produces successors.

## Links

- arXiv: http://arxiv.org/abs/2607.28568  
- Paper Breakdown: http://paperbreakdown.com/abs/2607.28568  

## Why it matters

Clean conceptual placement of “SLM + trained search operators + verifiable MLE sandbox” on the RSI spectrum. Complements vault notes on RSI moats, verifiability/RLVR, and evolutionary coding environments.

## Skeptical read

Narrow domain (MLE). Frontier comparisons depend on harness pairing and task set. Article written with Claude + Paper Breakdown harness — verify numbers against the paper PDF for any decision use.

## Related

- [[loop-is-the-moat-rsi-m0egpt]]
- [[anthropic-recursive-self-improvement]]
- [[recursive-self-improvement-ai-101]]
- [[verifiability-constraint-rlvr-unverifiable-tanayj]]
- [[harbor-rl-coding-environments]]
- [[looped-transformers-explained-neural-avb]]
- [[prime-agent-rlm-continual-harness-primeintellect]]
- [[continual-learning-replit-agent-vibench]]
- [[sia-recursive-self-improving-agent]]
- [[zen-and-the-art-of-ai-research]]
