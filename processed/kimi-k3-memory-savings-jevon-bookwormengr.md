---
tags:
- kimi
- kimi-k3
- moonshot
- architecture
- linear-attention
- kda
- mla
- kv-cache
- inference
- long-context
- investing
- ai-economics
- hardware
- memory
- models
- jevon-paradox
source: https://x.com/bookwormengr/status/2082377457852920075
date: 2026-07-29
type: bookmark
author: GDP (@bookwormengr)
raw: "[[raw/bookwormengr_2082377457852920075]]"
description: "Kimi K3 KDA hybrid linear at frontier scale — ~73% KV/state savings vs all-MLA; memory-stock debate vs Jevon's paradox"
summary: "Technical + market analysis of Kimi K3's constant KDA state (69 KDA + 24 MLA), per-channel decay, subagent snapshot math, and whether hybrid linear at 1T+ is net-new for HBM/memory demand pricing."
---

# Kimi K3 Memory Savings vs Jevon's Paradox

## Key takeaways

- **Net-new claim:** Hybrid linear wasn't new, but Kimi K3 is framed as the first **frontier-scale** proof that hybrid linear (KDA) can match full-attention-level recall — not just mid-tier Qwen/Nvidia experiments. That is the information that matters for memory demand narratives.
- **Architecture sketch:** 93 layers / 96 heads — **69 KDA + 24 gated MLA**. KDA state ~**0.22 GB constant**; only MLA grows with context. Author calc (verified with K3): all-MLA ~13.7→107 GB from 128K→1M vs K3 MLA ~3.5→29 GB + 0.22 GB KDA → **~73% savings**. MLA already ~90% vs MHA/GQA; KDA stacks another ~73% on that baseline.
- **Why KDA works better:** Per-channel (selective) decay via diagonal matrices when updating state — forget unevenly across channels instead of uniform lossy summary. Prior pure linear struggled at exact early-context recall (e.g. phone numbers).
- **vs DeepSeek V4 path:** V4 CSA/HCA can cut KV more aggressively but is sequence-lossy on **every** layer; K3 keeps ~25% full MLA uncompressed. Hypothesis: better long-context specific retrieval → wider lab adoption (ZAI, MiniMax, Qwen, Tencent, etc.) like MLA/DSA spread.
- **Subagents / snapshots rebuttal:** Snapshotting KDA every 20K over 1M ≈ 50 × 0.22 GB ≈ 11 GB; total still ≪ all-MLA. Sync subagent KV/state is usually short-lived once control returns; long-lived main-session state is where KDA bites.
- **Market lens (explicit NFA):** Memory stocks 10–30× on agentic long-context demand. Counter: inefficient OSS deploy, night idle, closed labs may already have similar tech, **Jevon's paradox** can eat savings. Still non-zero chance of demand-side narrative break + game-theoretic selling (cites Jaya Gupta style point that small demand dips can cascade).
- **Other K3 stack notes:** no positional encodings (recurrent KDA + MLA without PE), attention residuals at 2.8T, Stable Latent MoE, ~2.5× training efficiency claim, open **FlashKDA** + **MoonMoE**.

## Summary

Long X Article by @bookwormengr (GDP) bridging Kimi K3 architecture detail with HBM/memory-equity debate after agentic coding drove context memory demand. Core technical pitch is selective-decay hybrid linear at frontier quality. Investment framing is carefully hedged as not advice; optimism on AI long-term remains.

## Skeptical read

- Memory numbers are author/model-assisted calcs for one architecture — batch, precision, multi-request concurrency, and serving stack dominate real HBM.
- "First frontier hybrid linear" is contested by closed-lab opacity; market impact is narrative-sensitive, not a proven demand cliff.
- Jevons offset is empirical; treating either "bubble bust" or "demand infinite" as destiny overfits one launch week.

## Related

- [[gpt2-to-kimik3-architecture-22580-waterloo]]
- [[sparse-attention-long-context-dsa-msa-cyrusasg]]
- [[how-to-build-company-os-kimi-k3]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[multi-gpu-inference-tp-pp-sp-ep-mainzonx]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[who-will-set-price-intelligence]]
- [[the-untrainable]]
- [[aftermarket-harnesses-ttunguz]]
