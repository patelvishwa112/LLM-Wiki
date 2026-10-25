---
title: "CUDA from Zero to Hero #1 — Hardware First, Then Kernels"
type: bookmark
description: "First entry in Pramod Goyal's CUDA learning series: why GPUs exist, the SM/block/warp memory hierarchy, and a first naive matmul kernel that replaces one serial thread with M*N parallel ones."
tags: [cuda, gpu, gpu-architecture, parallelism, fundamentals, hardware]
source: https://x.com/goyal__pramod/status/2103565642800431533
date: 2026-09-25
author: Pramod Goyal
summary: "First entry in Pramod Goyal's CUDA learning series: why GPUs exist, the SM/block/warp memory hierarchy, and a first naive matmul kernel that replaces one serial thread with M*N parallel ones."
raw: "[[raw/goyal__pramod_2103565642800431533]]"
---

# CUDA from Zero to Hero #1 — Hardware First, Then Kernels

**Source:** Pramod Goyal, 2026-09-25. Opening post of a series of CUDA learning notes, written to be exhaustive enough to take a beginner to current-practice level, built around hand-writing kernels and improving them.

The premise is that you cannot understand CUDA code without simultaneously understanding the machine it runs on. Goyal starts from the CPU block diagram (DRAM, cache, control, ALUs) and its limit: a CPU is built to run work in sequence, with a handful of cores offering coarse parallelism. A matrix multiply — the core operation of most AI — needs no such sequencing, since every output element can be computed independently from one row and one column. So the GPU answer is simply far more ALUs per control unit, at the cost of less cache per ALU and no pretence of general-purpose latency hiding.

From there he lands the memory-hierarchy rule that motivates everything later: the larger the storage, the slower the access. Global memory (VRAM, the advertised number on the box) is the slow tier; an SM (streaming multiprocessor) holds blocks, blocks hold threads, and threads of a block can only see that block's shared memory. Threads are scheduled in 32-thread warps, which execute together. Copying data from global memory into an SM is called out explicitly as expensive — the cited authority being Horace He's "Making GPUs go Brrr" — which is why the intended pattern is to move data in once, compute locally, and write back once. He flags the diagrams as deliberate oversimplifications that will be refined in later instalments.

The CUDA section maps those boxes onto the programming model: a grid contains blocks, blocks contain threads, addressable in 1D/2D/3D (he stays in 1D for this article), running on a device (GPU) launched from a host (CPU), where "kernel" just means a function. The worked example is matmul. The deliberately bad kernel launches `<<<1, 1>>>`, so a single GPU thread runs the entire triple loop and the GPU's parallelism goes unused — a good illustration that "runs on the GPU" is not the same as "is parallel". The naive fix gives each thread one output element, computing a global id as `threadIdx.x + blockDim.x * blockIdx.x`, deriving `row = gid/N` and `col = gid%N`, then looping only over `K`. Since memory is 1D and row-major, the M×N output is really M stacked rows of N values — that layout is what makes the `gid` decomposition work.

Two details carry the pedagogical weight. First, `blockDim` is the block's dimension while `blockIdx` is its index; multiplying them yields the count of threads that came before the block, so the readable interpretation of the id formula is "which thread am I, plus everyone ahead of me". Second, you cannot launch M×N threads in the general case, so you fix 256 threads per block and compute `blocksPerGrid = (M*N + threadsPerBlock - 1)/threadsPerBlock` — a ceiling — which necessarily over-provisions, hence the mandatory `if (gid >= M*N) return;` guard. He recommends GPU Puzzles and LeetGPU as practice, and promises the next part on bottlenecks and optimisation.

## Why it matters

The `gid` formula, the ceiling-division launch config, and the out-of-range guard are the three lines that appear in essentially every custom kernel, and they are the same three lines that get mis-sized and silently corrupt results. More substantively, the post states the performance model that inference work lives on: global memory is the expensive tier, shared memory is per-block only, and warps of 32 are the scheduling unit. Anyone reasoning about why a matmul kernel is bandwidth-bound, or why fused and tiled kernels beat naive ones, needs exactly this frame before touching a serving stack.

## Key points

- A GPU's structural bet is "more ALUs, less control and cache" — matmul is parallel by construction, since each output needs only one row and one column.
- Memory hierarchy rule: bigger storage means slower access; global memory (VRAM) is the slow tier, and moving data global → SM is explicitly flagged as inefficient (cites Horace He, "Making GPUs go Brrr").
- Threads in a block see only that block's shared memory; execution is scheduled in 32-thread warps that run all their threads simultaneously.
- CUDA hierarchy is grid → blocks → threads, laid out 1D/2D/3D; host = CPU, device = GPU, kernel = a function.
- Anti-pattern: launching `<<<1, 1>>>` makes one thread run the whole triple loop, so the GPU gives you nothing over the CPU version.
- Naive kernel: one thread per output element, `gid = threadIdx.x + blockDim.x*blockIdx.x`, `row = gid/N`, `col = gid%N`, inner loop over `K` only.
- Launch config uses 256 threads per block and `blocksPerGrid = (M*N + threadsPerBlock - 1)/threadsPerBlock`, which over-provisions, requiring `if (gid >= M*N) return;`.
- Underlying data layout is 1D row-major, so the M×N result is M rows of N values stacked — that is why flat indexing works.
- Practice pointers: GPU Puzzles (srush) and LeetGPU; next instalment covers identifying bottlenecks and optimising.

## Related

- [[how-gpu-executes-code-first-principles]]
- [[efficiently-scaling-transformer-inference-checklist-wafer]]
- [[how-vllm-works-amitiitbhu]]
- [[inference-engines-2026]]
