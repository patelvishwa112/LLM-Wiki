---
tags: [peft, lora, fine-tuning, parameter-efficient, adapters, huggingface, training, slm]
source: https://huggingface.co/blog/peft-beyond-lora
type: article
related: [[multi-lora-training-osmosis], [training-llm-from-scratch-5-lessons]]
ingested: 2026-06-18
---

# Beyond LoRA: Can you beat the most popular fine-tuning technique?

**Authors:** Benjamin Bossan, Sayak Paul, et al. (Hugging Face)  
**Published:** June 18, 2026  
**Source Type:** Hugging Face Blog

## Core Thesis
LoRA dominates PEFT usage (98%+ on HF Hub), but benchmarks in the PEFT library show other methods (OFT, BEFT, Lily, rs-LoRA, LoRA-FA) can match or beat it on Pareto frontiers of test performance vs memory usage, especially in image generation and LLM math reasoning tasks. Don't default to LoRA — the unified PEFT API makes switching configs trivial.

## Key Takeaways
- **LoRA popularity** is self-reinforcing (tutorials, ecosystem support) rather than proven universally optimal.
- **Benchmarks matter**: HF's controlled comparisons (same model/dataset/hardware) reveal tradeoffs; e.g., OFT dominates LoRA in image-gen (better similarity + lower VRAM).
- **Variants & alternatives**: rs-LoRA (rank-stabilized init), LoRA-FA (optimizer), BEFT, Lily, OFT, GraLoRA (with conversion to LoRA for serving).
- **Ecosystem note**: Conversion tools added so non-LoRA adapters work in vLLM/etc.
- **Call to action**: Contribute experiments/PRs to PEFT benchmarks; try alternatives via simple config swap.

## Why It Matters
- Directly relevant to vault ML/training domain (lora, training, slm tags) and agent/SLM fine-tuning workflows.
- Challenges "LoRA default" assumption in efficient adaptation of models — key for resource-constrained training and multi-adapter serving.
- Provides objective data (Pareto analysis, memory/performance) to inform choices beyond paper claims.
- Complements existing notes on multi-LoRA, training from scratch, and SLM adaptation.

## Raw Source
[[huggingface_peft-beyond-lora]]

---
*Processed from HF blog article 2026-06-18. High-signal analysis of PEFT methods with practical benchmarks.*