---
tags: ["architecture", "kimi", "moonshot", "kv-cache", "linear-attention", "deltanet", "mla", "moe", "inference", "long-context", "models", "attention"]
source: https://x.com/swill1ams/status/2082856158520398279
date: 2026-08-01
type: bookmark
description: "Kimi K3 2.8T MoE explained via GQA/MLA/window/linear toolbox and hybrid KDA + Gated MLA for fixed-state long agents."
author: swill1ams
summary: "Kimi K3 2.8T MoE explained via GQA/MLA/window/linear toolbox and hybrid KDA + Gated MLA for fixed-state long agents."
raw: "[[raw/swill1ams_2082856158520398279]]"
---

# Kimi K3 explained: how forgetting made the biggest open model possible

## Key Takeaways

- K3: ~**2.8T** MoE (article: ~104B active) aimed at long-horizon engineering — big repos, GPU kernels, CAD, chip-design demos; successor energy after K2 Thinking’s multi-hundred tool-call runs.
- Bottleneck is **KV cache** memory/throughput at long context, not just parameter count. Hardware export pressure pushed Chinese labs toward software memory efficiency.
- Four tools against the bill (Acme meeting “Tuesday→Thursday” analogy):
  1. **Share** — GQA (heads share K/V)
  2. **Shrink** — MLA (latent cache; DeepSeek-style ~57× smaller entries, still grows)
  3. **Forget** — sliding window
  4. **Replace** — linear/recurrent fixed state (Mamba/DeltaNet line)
- **KDA** (Kimi Delta Attention): fixed-size recurrent state with delta erase-then-write + per-channel forgetting; validated on **Kimi Linear 48B** twin study vs full attention (~75% less KV, higher throughput, strong long-context scores, no short-task collapse claimed).
- K3 hybrid **3:1** — three KDA layers, every fourth **Gated MLA** for exact-ish full-history recall.
- Other stack notes: attention residuals, Stable LatentMoE, quantile balancing, per-head Muon, native 4-bit on experts; heavy RL on agent workflows + distillation of specialists.
- Practical win: prefix/cache hits for stable system+tools+repo prefixes; weights/report/kernels released (not full MIT/Apache).

## Why it matters

Best plain-English companion to the vault’s GPT2→KimiK3 lineage and bookworm Jevons/memory essays — makes “selective forgetting” the product architecture, not a side optimization.

## Related

- [[gpt2-to-kimik3-architecture-22580-waterloo]]
- [[kimi-k3-memory-savings-jevon-bookwormengr]]
- [[sparse-attention-long-context-dsa-msa-cyrusasg]]
- [[looped-transformers-explained-neural-avb]]
