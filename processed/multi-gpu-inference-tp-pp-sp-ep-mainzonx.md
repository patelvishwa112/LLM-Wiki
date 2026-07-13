---
tags: ["inference", "serving", "gpu", "tensor-parallelism", "pipeline-parallelism", "moe", "kv-cache", "vllm", "distributed-systems", "llm"]
source: https://x.com/mainzonx/status/2017308696649302483
date: 2026-01-30
type: bookmark
description: "Adam Mainz multi-GPU inference Part 2: capacity cliff (weights + KV), TP/PP/SP/EP tradeoffs, topology hierarchy (HBM → NVLink → IB), and vLLM/TensorRT-LLM orchestration."
author: MainzOnX
summary: "Adam Mainz multi-GPU inference Part 2: capacity cliff (weights + KV), TP/PP/SP/EP tradeoffs, topology hierarchy (HBM → NVLink → IB), and vLLM/TensorRT-LLM orchestration."
raw: "[[raw/mainzonx_2017308696649302483]]"
---

# Multi-GPU Inference — TP / PP / SP / EP (@MainzOnX Part 2)

Series: *Peeling Back the Curtain of the LLM Black Box*. Part 2 moves from single-chip thinking to coherent clusters. Part 3 teases layer fusion.

## Capacity cliff

- Llama 3.1 405B FP16 ≈ **810 GB** weights; H100 HBM = **80 GB** (~10× short).
- 8×H100 node ≈ 640 GB — still short without quantization/sharding.
- FP8 can ~halve weight footprint (~405 GB) and delay multi-node scale-out.
- Long context (128k–1M): **KV cache** can rival weights → network becomes the memory bus.

## Four parallelism strategies

| Mode | Shard what | Sync / catch | Fabric | Use when |
|------|------------|--------------|--------|----------|
| **TP** (tensor) | Weight matrices horizontally; same layer on all GPUs | Frequent **All-Reduce** | **NVLink** intra-node only | Lowest single-user latency; bandwidth aggregation |
| **PP** (pipeline) | Layers vertically (assembly line) | **Pipeline bubble**; micro-batch | InfiniBand / Ethernet | Model > single 8-GPU node |
| **SP** (sequence) | Token sequence / KV | **Ring Attention**; overlap comms | Multi-GPU | Context wall / long sequences |
| **EP** (expert) | Whole MoE experts per GPU | Router **All-to-All**; hot experts | Cluster | Trillion-param MoE capacity |

## Topology hierarchy

1. **HBM** ~2–3 TB/s (on-chip gold standard)
2. **NVLink** ~0.9–1.8 TB/s (chatty TP stays here)
3. **IB/Ethernet** ~50–100 GB/s (sparse PP across nodes)

Wrong parallelism on slow wires → stalls. Topology-aware design: chatty inside NVLink domain; infrequent hops across racks.

## Orchestration

- **vLLM** — PagedAttention + Ray; set TP size, engine shards.
- **TensorRT-LLM** — NVIDIA specialized engines, layer fusion, custom kernels.
- No universal TP/PP mix: **profile** compute vs communication before production.

## Why it matters

Clean mental model for distributed inference: capacity (weights + KV) forces sharding; each strategy maps to a different communication pattern and interconnect tier. Bridges single-node KV/serving notes to multi-node reality.

## Related

- [[how-vllm-works-amitiitbhu]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[inference-engines-2026]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[speculative-decoding-history-roofline-shreybirmiwal]]
- [[how-gpu-executes-code-first-principles]]
