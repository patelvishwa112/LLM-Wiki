---
tags:
  - gpu
  - gpu-architecture
  - cuda
  - parallelism
  - fundamentals
  - hardware
source: https://x.com/rocky_t07/status/2059997637726937492
raw: "[[raw/rocky_t07_2059997637726937492]]"
date: 2026-05-28
author: Rocky (@Rocky_T07)
type: bookmark
summary: A first-principles walkthrough of how GPUs execute code — from the thread hierarchy (Thread → Warp → Block → SM → GPU), through the full execution pipeline, to why GPUs revolutionized parallel computation. Includes the memory aid GBWT (Grid → Block → Warp → Thread).
related:
  - "[[what-is-kv-cache-llms]]"
---

# How GPUs Execute Code — First Principles

**Source:** Rocky (@Rocky_T07) explains GPU execution from the hardware up, using a vector addition example throughout.

## GPU vs CPU

| CPU | GPU |
|-----|-----|
| Polymath — good at many operations | Specialist — massively parallel |
| Low-latency, complex decision making | High-throughput, independent calculations |
| Few cores, deep pipelines | Thousands of lightweight threads |

**Key tradeoff:** GPU sacrifices flexibility for massive parallel execution. Works best when calculations are independent.

## The Thread Hierarchy (GBWT)

The fundamental organizing principle of GPU compute:

```
Thread → Warp → Block → SM → GPU (Grid)
```

| Unit | Composition | Role |
|------|------------|------|
| **Thread** | 1 worker | Executes a single calculation (e.g., `x[0] + y[0] = z[0]`) |
| **Warp** | 32 threads | Batch execution unit — GPUs prefer batched work |
| **Block** | 8 warps (256 threads) | Scheduling unit assigned to an SM |
| **SM** | Hardware unit | Mini-factory with schedulers, registers, shared memory, cores |
| **GPU** | Many SMs | The full parallel computation machine |

**Memory aid:** GBWT — Grid → Block → Warp → Thread

## SM (Streaming Multiprocessor) Internals

The SM is the actual execution unit. Each SM contains:

- **Schedulers** — decide which warps run next
- **Registers** — ultra-fast temporary storage per thread
- **Shared Memory** — fast memory shared across threads in a block
- **Cores** — perform mathematical operations

## Execution Pipeline (Step by Step)

1. **CPU dispatches** — code is read by CPU, passed to GPU with block/thread config (`<<<blocks, threads>>>`). This is "CPU overhead."
2. **GPU spawns threads** — thousands created, each with a specialized task
3. **Threads → Blocks** — grouped into blocks that become schedulable units
4. **Blocks → SMs** — GPU scheduler distributes blocks across available SMs
5. **Compute** — data fetched from memory, cores execute, results stored
6. **Warp-level latency hiding** — SM switches between warps while one waits for memory, keeping the GPU busy
7. **Output returned** — GPU signals completion to CPU

## Key Insight

> GPUs don't solve one difficult problem very fast — they solve millions of small problems together.

When training an LLM, rendering a game, or running a simulation, you're feeding millions of tiny calculations into thousands of threads running simultaneously. The hierarchy is always the same: Thread → Warp → Block → SM → GPU.
