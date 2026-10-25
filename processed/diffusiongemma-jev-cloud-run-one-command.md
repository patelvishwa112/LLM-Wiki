---
title: One-command DiffusionGemma-Jev endpoint on Cloud Run
type: bookmark
description: "Google Gemma points at djev-run: a single gcloud command serving NVFP4 DiffusionGemma 26B-A4B on one RTX PRO 6000 at $3.19/hr, ~100-123 req/s at batch 32, and ~47s cold start."
tags: [gemma, diffusion, inference, serving, cost-optimization, google, vllm]
source: https://x.com/googlegemma/status/2102536894169096357
date: 2026-09-22
author: Google Gemma
summary: "Google Gemma points at djev-run: a single gcloud command serving NVFP4 DiffusionGemma 26B-A4B on one RTX PRO 6000 at $3.19/hr, ~100-123 req/s at batch 32, and ~47s cold start."
raw: "[[raw/googlegemma_2102536894169096357]]"
---

# One-command DiffusionGemma-Jev endpoint on Cloud Run

**Source:** Google Gemma, 2026-09-22. A deployment announcement pointing at the `taeold/djev-run` repo, which packages DiffusionGemma-Jev behind vLLM on a single Cloud Run GPU.

The post itself is three numbers and a link, but the numbers are the interesting part: ~35–60 ms single-step latency, ~100–123 requests/second at batch 32, roughly $3/hour that falls to $0 when idle. Those are a diffusion language model's numbers, and they sit in the same range as small autoregressive models that need a real serving stack — which is the point. Diffusion decoders generate a canvas of tokens in parallel and refine it, so a single step either produces an answer or leaves a partially-filled one that can be pinned and completed later.

The repo behind the link is what makes it reproducible rather than a demo: weights are pulled from Hugging Face as `nvidia/diffusiongemma-26B-A4B-it-NVFP4` (26B total, ~4B active), staged into a GCS bucket, prefetched into `/dev/shm` at ~1.05 GiB/s, and served by `vllm serve` with a specific set of flags — Triton bidirectional attention, a 128-token diffusion canvas, FlashInfer masked-GEMM MoE on Blackwell, eager mode and a fixed 2 GiB KV cache to skip startup profiling. Cold start lands at ~47.5 s against a 4 m 05 s baseline, which is what makes scale-to-zero viable.

The published benchmark is the other half of the argument: on JevBench v1.3.0 (N = 231), this self-hosted setup scores 81.4–81.8% at 117–121 ms median, versus the hosted `api.djev.dev` at 81.8% in 237 ms. Same accuracy, half the latency, on your own Cloud Run service.

## Why it matters

The practical effect is that a non-autoregressive model family becomes deployable by someone without a GPU fleet, at a price that makes experimentation rational: ~$3.19/hour while active and literally zero when idle, with a one-command path. If parallel-decode latency holds up on your task, the serving economics change — one consumer-class GPU instance replacing a multi-replica AR deployment — and the `/v1/systemone` interface, which returns per-option probabilities in one diffusion pass, is a direct fit for classification and routing layers that currently pay for multiple sampled completions.

## Key points

- **~35–60 ms** single-step latency; **~100–123 req/s** at batch/concurrency 32.
- **$3.19/hour** for 1× RTX PRO 6000 (20 vCPU, 80 GiB), $0 when idle with `--min-instances=0`.
- Cold start **~47.5 s**, down from a **4 m 05 s** baseline — the enabling number for scale-to-zero.
- JevBench v1.3.0 (N=231): **81.4–81.8%** accuracy at **117–121 ms** vs hosted API **81.8%** at **237 ms**.
- Serving requires diffusion-specific config: `--attention-backend TRITON_ATTN`, `--diffusion-config '{"canvas_length":128}'`, `--language-model-only`, `--kv-cache-memory 2G`, `VLLM_FLASHINFER_MOE_BACKEND=masked_gemm`.
- `vllm_xargs` exposes `diffusion_seed_canvas` / `diffusion_pinned` / `diffusion_max_steps` / `diffusion_read_only` — partial answers can be seeded and completed; `/v1/systemone` returns choice probabilities with confidence in ~116 ms.
- Repo is Apache-2.0, built on `mmastrac/djev`; RTX PRO 6000 available in `us-central1`, `europe-west4`, `asia-southeast1`, `asia-south2`.

## Related

- [[inference-engines-2026]]
- [[how-vllm-works-amitiitbhu]]
- [[how-to-build-diffusion-language-model-kuleshov]]
- [[google-gemma-4-12b-local-fine-tuning]]
- [[inference-optimizations-sub-second-llm-checklist]]
