---
type: bookmark
description: "Shrey Birmiwal walks speculative decoding from roofline arithmetic intensity through Leviathan draft-verify, rejection sampling, Medusa/Eagle/DFlash/DDTree, up to ~8x lossless decode speedups."
tags:
  - inference
  - serving
  - llm
  - speculative-decoding
  - gpu
  - kv-cache
  - throughput
  - latency
  - medusa
  - eagle
  - roofline
source: https://x.com/shreybirmiwal/status/2074666256402448732
date: 2026-07-08
author: Shrey Birmiwal (@shreybirmiwal)
summary: "Decode is memory-bound (low arithmetic intensity); draft models + parallel verification raise tokens per target forward pass with exact distribution via rejection sampling — tree and diffusion drafters reach 7–8x."
raw: "[[raw/shreybirmiwal_2074666256402448732]]"
---

# Speculative decoding — history and roofline intuition

Long-form explainer on **speculative decoding** as a near–free-lunch, **lossless** inference speedup (author cites up to **~8×** on some workloads).

## Hardware framing

Autoregressive decode loads full weights + KV per token → low **arithmetic intensity** → **memory-bound** on GPUs (**roofline** point A). Goals: raise intensity toward the ridge (point B) without sacrificing per-user latency like extreme batching (point C).

- **Batch parallel** amortizes weights, not per-sequence KV; hurts latency; KV HBM caps batch size.
- **Sequence parallel (prefill)** knows all prompt tokens → parallel forward; amortizes weights **and** shared KV.

Decode lacks known future tokens — speculation imports prefill-style **parallel verification** into decode.

## Leviathan draft–verify

Small **draft model** guesses several tokens; **target model** verifies in one parallel pass. Accept prefix until first mismatch; gain 1..n+1 tokens per target step. Intensity scales with accepted guesses / (W + KV).

Only wins when **memory-bound**; if already compute-bound, draft + verify cost is pure overhead.

## Lossless rejection sampling

Accept draft token x with probability min(1, p(x)/q(x)); on reject, sample residual max(p−q,0). Proof: combined paths sum to **p(x)** — identical distribution to target-only sampling.

## Architecture advances (selected)

| Line | Idea | Speedup notes |
|------|------|----------------|
| Medusa | Extra heads on target last layer (MTP-style) | ~3.5× coding; independent heads limit acceptance |
| Eagle 1/2 | Drafter uses target hidden states; dynamic trees | Higher acceptance; tree branches uncertain tokens |
| DFlash | Block diffusion drafter | ~6×; flat latency vs block length |
| SpecInfer / DDTree | Tree attention verification | 7–8× on some workloads; DDTree + DFlash sampling |

## Forward-looking threads

Speculation for **throughput** on long-context agents; disaggregated speculator chips; MoE-aware and workload-routed drafters; online on-policy speculator training (Baseten, Modal); **DSpark** (DeepSeek ’26) atop DDTree.

## Related

- [[inference-optimizations-sub-second-llm-checklist]]
- [[how-vllm-works-amitiitbhu]]
- [[how-gpu-executes-code-first-principles]]
- [[how-to-build-diffusion-language-model-kuleshov]]