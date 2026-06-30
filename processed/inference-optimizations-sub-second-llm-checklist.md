---
tags:
- inference
- serving
- llm
- kv-cache
- speculative-decoding
- flashattention
- pagedattention
- quantization
- throughput
- latency
description: "Ashutosh Maheshwari's 16-technique bookmark list for sub-second LLM inference — caching, attention, batching, parallelism, graphs, streaming."
summary: "Ashutosh Maheshwari's 16-technique bookmark list for sub-second LLM inference — caching, attention, batching, parallelism, graphs, streaming."
source: https://x.com/asmah2107/status/2071196830088777741
date: 2026-06-28
type: bookmark
author: asmah2107
raw: "[[raw/asmah2107_2071196830088777741]]"
---

# Inference optimizations for sub-second LLM responses

Curated **16-item study map** for low-latency LLM serving (checklist post, not deep dives). Groups naturally:

| Layer | Items |
|-------|--------|
| **Attention / memory** | KV-Caching, FlashAttention, PagedAttention, Memory Offloading |
| **Decode speed** | Speculative Decoding, Early Exit, Parallel Decoding, Streaming |
| **Precision / kernels** | Mixed Precision, Quantized Kernels |
| **Scale-out** | Tensor / Pipeline / Sequence Parallelism |
| **Serving** | Batch + Dynamic Batching, Graph opt (ONNX, TensorRT) |

Use as index when drilling into engines (vLLM, TensorRT-LLM, etc.); author planned per-topic threads.

## Related

- [[how-vllm-works-amitiitbhu]]
- [[inference-engines-2026]]
- [[mlx-engine-v185-kv-cache-agentic]]
- [[ai-engineering-roadmap-2026-from-scratch]]