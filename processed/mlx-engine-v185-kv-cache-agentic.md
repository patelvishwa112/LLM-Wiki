---
tags: [mlx, apple-silicon, inference, kv-cache, agents, agentic-workflows, vlm, lm-studio, serving, optimization, open-source]
source: https://x.com/ostensiblyneil/status/2063006720616734835
raw: "[[raw/ostensiblyneil_2063006720616734835]]"
date: 2026-06-06
type: bookmark
author: ostensiblyneil
summary: MLX Engine v1.8.5 (LM Studio) adds disk-backed KV cache checkpointing for agentic workflows and continuous batching for VLMs. Solves the cache-rewind problem for models like Qwen 3.5 and Gemma 4. 256-token block boundaries, LRU disk store, unified-memory-aware eviction. Benchmarks: 2.2x faster parallel chat, 82% less extra RAM, 3.5x faster repeated image prompts on M3 Max.
related: [[inference-engines-2026]], [[what-is-kv-cache-llms]]
---

# MLX Engine v1.8.5 — KV Cache for Agentic Workflows

By Neil Mehta, LM Studio

## Core Problem

Open-source models (Qwen 3.5, Gemma 4) use hybrid/sliding-window attention that reduces KV cache memory but makes rewinding hard. When an agent sends a follow-up request, the engine must either re-compute the entire prompt prefix or find a way to checkpoint and restore the KV cache.

## Solution: Disk-Backed KV Cache

**Boundary-based checkpointing** at every 256 tokens. Background disk-writer streams local attention KV cache blocks at boundaries. Since Apple Silicon has unified memory, committed blocks are evicted from RAM — memory scales with active sequences only.

**LRU disk store** optimizes for usage patterns: repeated system prompts stay cached, stale conversations get evicted. Single scratch file with safetensors blobs, in-memory offset table, free-list reuse.

**Temporary by design:** /tmp storage, model-lifetime metadata, auto-cleanup on unload or process exit.

## Key Numbers (M3 Max, Qwen3.6-27B-4bit)

- Parallel chat: **2.2x faster** (16.78s vs 37.60s)
- Long-prompt RAM: **82% less** (+1.18GB vs +6.47GB)
- Repeated image prompt: **3.5x faster** on second request (6.88s vs 23.79s)

## Relevance

MLX Engine runs on Apple Silicon — directly applicable to Mac Mini M1 workflows. Disk-backed KV cache makes local agentic inference viable by keeping memory footprint manageable across multi-turn agent sessions. Continuous batching enables concurrent VLM requests.
