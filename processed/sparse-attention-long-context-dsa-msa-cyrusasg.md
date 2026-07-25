---
tags: ["inference", "serving", "kv-cache", "sparse-attention", "long-context", "attention", "mla", "gqa", "deepseek", "minimax", "agents", "gpu", "architecture", "training"]
source: https://x.com/cyrusasg/status/2080697631286681998
date: 2026-07-25
type: bookmark
description: "Cyrus maps 1M-context sparse attention: KV-cache bandwidth bill, compress vs restrict vs replace axes; NSA→DSA/MSA/Inkling/KDA; indexer KL training; silicon-first design."
author: cyrusasg
summary: "Cyrus maps 1M-context sparse attention: KV-cache bandwidth bill, compress vs restrict vs replace axes; NSA→DSA/MSA/Inkling/KDA; indexer KL training; silicon-first design."
raw: "[[raw/cyrusasg_2080697631286681998]]"
---

# Sparse attention design space for 1M context (Cyrus / Decagon)

Field guide to why frontier 1M windows (GLM-5.2, DeepSeek-v4, MiniMax M3, Kimi K3, Inkling) are forced by **agents** (long coding, tool traces, repos in working memory) and how labs stop reading every KV token on every decode step.

## The bill

Decode is **HBM-bandwidth bound**: full KV history re-read per new token; cache grows with length × batch. Toy 1T / 100 layers / GQA-8 / d=128 ≈ **0.4 MB/token** → ~50 GB at 128K, **>400 GB at 1M** before weights. Sparse attention is the main lever of 2025–26.

Framing question: **who decides what each query attends to, and at what granularity?**

## Three axes

1. **Compress cache** — MQA/GQA head sharing; DeepSeek **MLA** low-rank latents (still dense over a smaller “everything”).
2. **Restrict pattern** — static windows/global tokens → **learned** selection (the 2025–26 center of mass).
3. **Replace primitive** — linear attention / Mamba / recurrence; fixed-size state.

MiniMax arc: Lightning linear hybrid (M1) → honest revert to full attention (M2) when multi-hop reasoning failed at scale → **fork**: learned sparse softmax (DeepSeek/MSA) vs linear hybrids (**DeltaNet** / gated variants / **KDA** on Kimi K3, up to ~75% KV cut, 3:1 with MLA).

## NSA template → descendants

**NSA** (DeepSeek, Feb 2025): three paths — block compression summaries, top-block selection, sliding window + learned gate; block-aligned for tensor cores. Training thesis: sparsity must be in **gradients** (ideally from pretrain start) or dense retrieval heads scramble at sparse inference.

| Design | Substrate | What is selected | Budget / shape |
|---|---|---|---|
| **DSA** | MLA + lightning indexer (few heads, ReLU, FP8) | **Token**-level top-k (~2048) | O(Lk) exact attn; retrofit onto dense then CPT; GLM IndexShare = 1 indexer / 4 layers |
| **MSA** | Plain **GQA**, full-precision KV | **128-token blocks**, top-16 (+ always last block) | Fixed 2048 KV tokens; selection per GQA group |
| **Inkling** | No indexer | Layer pattern 5:1 window(512):global + **sconvs** | Per-layer sparsity; global layers still dense; simpler failure modes |

Agentic risk for Inkling-style: need a token 700K back while next global layer is several layers away — learned selection bets differently.

## Training non-diff top-k

Shared recipe: **self-distillation** — KL of indexer scores vs dense main-branch attention (teacher=student same forward); **stop-grad** into backbone; dense warmup then hand routing to indexer. DSA: short frozen-indexer warmup (~1k steps / 2.1B tok) then large sparse CPT. MSA: native-from-zero slightly beats dense-convert on retrieval long-ctx; always-keep local block stabilizer. Sparsity migrating earlier in training over time.

## Payoff + silicon causality

MSA numbers mean different things: ~28× algorithmic attn compute @1M; kernel ~14× prefill / ~7.6× decode (H800); product M3 vs M2 ~9× prefill / ~15× decode @1M. Kernel tricks: **exp-free top-k** (order-preserving raw scores), **KV-outer** sparse loop (each block read once, contiguous). Lesson: algorithm + kernel co-design; paper FLOPs only land if memory access cooperates.

Trend: architectures designed **backwards from silicon** (128-token blocks, FP8 indexer, IndexShare when indexer is the bottleneck). Open bet: spend real parameters on the **indexer as in-layer retrieval**, not only cheapen it.

## Why it matters

- Connects agent long-horizon demand to concrete serving physics (KV GB and decode bandwidth).
- Clean taxonomy for reading DSA/MSA/MLA/KDA papers and choosing block vs token granularity tradeoffs.
- Training recipe for sparse routers is transferable mental model (distill dense teacher, detach backbone).

## Related

- [[kv-caching-llms-clearly-explained-avichawla]]
- [[how-vllm-works-amitiitbhu]]
- [[multi-gpu-inference-tp-pp-sp-ep-mainzonx]]
- [[speculative-decoding-history-roofline-shreybirmiwal]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[inkling-ear-7-9m-lookup-table-huckiyang]]
- [[glm-5-2-with-vision-projector-part-harry]]
- [[continuous-batching-grpo-trl]]
