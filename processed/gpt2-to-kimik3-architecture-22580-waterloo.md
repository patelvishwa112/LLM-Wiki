---
title: "22580: From GPT2 to Kimi3, Explained"
tags: [architecture, transformers, attention, kv-cache, linear-attention, deltanet, mamba, moe, mla, kimi, moonshot, inference, long-context, models, training]
source: https://x.com/waterloo_intern/status/2081762065392541951
date: 2026-07-28
published: 2026-07-27
authors: ["@waterloo_intern"]
type: bookmark
description: "GPT-2→KimiK3 lineage: scale 22580× is secondary to how models store, update, and retrieve in fixed-size state (linear attn, DeltaNet, KDA, MLA, MoE, AttnRes)."
summary: "GPT-2→KimiK3 lineage: scale 22580× is secondary to how models store, update, and retrieve in fixed-size state (linear attn, DeltaNet, KDA, MLA, MoE, AttnRes)."
author: waterloo_intern
raw: "[[raw/waterloo_intern_2081762065392541951]]"
---

# 22580: From GPT2 to Kimi3, Explained

Technical worklog by @waterloo_intern (ali): ~22,580× scale from GPT-2 (2019) to KimiK3 (2026) is the headline number; the real story is successive changes to **what is stored, how state is updated, and how information is retrieved** when pure growing KV cache is not enough.

## Progression

1. **GPT-2 baseline** — Decoder-only blocks: LN → causal softmax attention → residual → LN → MLP. Autoregressive decode needs **KV cache** so past keys/values are not recomputed; cache grows with sequence length (memory-bandwidth wall at long context).

2. **Linear attention** — Feature map on Q/K (e.g. ELU+1) makes the recurrence associative → history folds into a **fixed-size** state (order D×D) instead of O(T) KV. Cheaper long context; less expressive; **interference** as capacity fills (additive overwrites).

3. **DeltaNet (fast weight / delta rule)** — Not only write; compute what the key would retrieve, **subtract old association**, then write new value → precise overwrite. Chunked parallel training (Householder-like transitions) keeps linear-time-ish inference character.

4. **Gated DeltaNet** — Add decay/gate (Mamba-2 flavor): forget associations over time, not only on explicit overwrite. Combines delta updates with state decay.

5. **Kimi Linear / KDA (Kimi Delta Attention)** — Fine-grained **per-channel** decay (not one scalar). Hybrid stack: recurrent KDA layers interleaved with **MLA** (multi-head latent attention); dense MLP → MoE. Claims better quality than full attention under controlled compare + large decode speedups (up to ~6× in earlier Kimi Linear messaging).

6. **KimiK3 stack**
   - Macrocycles of layers: majority **KDA** (constant-state recurrent memory) + periodic **MLA** (softmax-style retrieval over context when fixed state cannot hold everything).
   - Latent-space **MoE** (many experts, sparse routed + shared).
   - **SiTU** expert activation (SiLU variant path).
   - **Gated MLA** + query LoRA.
   - **AttnRes** (attention residuals) at block boundaries (~every 12 layers): layers learn to read a weighted mix of earlier depth residual blocks, not only the immediate residual sum — selective depth-wise retrieval to fight residual dilution.

## Core claim

> The central change is not scale alone. Each architectural step changes what the model stores, how it updates that state, or how it retrieves information that a fixed-size state cannot preserve.

KimiK3 = constant-state recurrent memory + periodic softmax retrieval + sparse expert capacity + selective depth residual access. Fixed-capacity associative memory needs an **eviction/selection policy** (gating, routing, decay); attention remains the strongest selective-read mechanism when you pay for it.

## Image / Diagram Summary

Full-page capture is a long dark-mode X Article with repeated section flows (screenshot is multi-column tall scroll; panels are small but the structure is clear):

- **GPT-2 stack diagrams:** token/pos emb → stacked blocks; zoomed residual attention+MLP blocks; QKV split / softmax attention schematic; decode-only final-logit inefficiency motivating KV cache.
- **Linear attention:** associative recurrence diagrams (fixed D×D state vs growing cache); code blocks for feature-map attention.
- **DeltaNet:** fast-weight / write-after-subtract visuals; parallel chunk / Householder-style transition figures; side-by-side comparison to pure additive linear state.
- **Gated DeltaNet:** block diagrams with explicit decay/gate paths on the recurrent state.
- **Kimi Linear / KDA → KimiK3:** hybrid KDA+MLA layer patterns, MoE expert routing, Gated MLA, AttnRes block stacking (depth residual mix via query-key over prior block states).

Dense pseudocode/math appears throughout; raw note holds the full evaluated article text for equations.

## Why It Matters

Compact map of the **recurrent + hybrid attention** line that Moonshot-style models sit on. Ties long-context serving (KV walls), Mamba/linear-attn research, MLA/DeepSeek-style latent attention, and MoE capacity into one functional story: **learned selection over fixed memory**. Useful next to sparse-attention / KDA notes and KV-cache fundamentals.

## Source

[22580: From GPT2 to Kimi3, Explained — @waterloo_intern](https://x.com/waterloo_intern/status/2081762065392541951)

## Related

- [[sparse-attention-long-context-dsa-msa-cyrusasg]]
- [[what-is-kv-cache-llms]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[attention-qkv-math-amitiitbhu]]
- [[how-vllm-works-amitiitbhu]]
- [[looped-nanochat-two-pass-routing-kyleliang]]
- [[kimi-k2.6-agent-swarm-300-parallel-agents]]
