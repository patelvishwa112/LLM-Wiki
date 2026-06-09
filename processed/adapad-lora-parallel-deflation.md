---
tags: ["training", "lora", "fine-tuning", "models", "papers"]
source: https://x.com/optimalab1/status/2055029895676174338
raw: "[[raw/optimalab1_2055029895676174338]]"
date: 2026-05-14
type: note
related: ["how-to-build-your-own-llm-from-scratch-in-5-stages"]
---

# AdaPaD: Parallel Rank-1 Deflation for LoRA

## Summary
AdaPaD introduces parallel rank-1 deflation for LoRA that self-corrects during fine-tuning. Led end-to-end by Barbara Su (Rice CS → MSc Stanford), with theoretical contributions from Jasper Liao (Rice CS). The work spans algorithm design, GLUE/SQuAD pipelines, and multi-GPU H200 scaling.

## Key Takeaways
- **AdaPaD:** A self-correcting LoRA variant using parallel rank-1 deflation
- **End-to-end execution:** Algorithm design, standard benchmarks (GLUE, SQuAD), and multi-GPU H200 scaling all led by a single researcher
- **Self-correction:** The deflation mechanism allows the adapter to correct its own updates during training
- Available at: akyrillidis.github.io/aiowls/adapad.html

## Connections
- [[how-to-build-your-own-llm-from-scratch-in-5-stages]] — LoRA and fine-tuning as key stages in LLM development
