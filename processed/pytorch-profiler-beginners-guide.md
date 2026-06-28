---
title: 'Profiling in PyTorch: A Beginner''s Guide to torch.profiler'
source: https://huggingface.co/blog/torch-profiler
authors:
- Aritra Roy Gosthipaty
- Sayak Paul
- Sergio Paniego
- Rémi Ouazan Reboul
- Pedro Cuenca
published: 2026-05-29
type: article
tags:
- pytorch
- profiling
- cuda
- gpu-optimization
- torch.compile
- cublas
- perfetto
- kernel-analysis
related:
- '[[custom-kernels-agent-skills]]'
- '[[accelerating-generative-ai]]'
- '[[delta-weight-sync]]'
raw: '[[raw/huggingface_torch-profiler]]'
description: 'Profiling in PyTorch: A Beginner''s Guide to torch.profiler'
---

# Profiling in PyTorch: A Beginner's Guide to torch.profiler

Part 1 of a 3-part series from Hugging Face that builds the skill of reading `torch.profiler` traces from the ground up. Uses a single `matmul + add` operation as the vehicle to teach profiler literacy — no prior profiling experience needed.

## Key Takeaways

### 1. The Profiler Produces Two Artifacts
- **Profiler table** (`prof.key_averages().table()`): Statistical summary. Answers "what is taking the most time." Shows Self vs Total time and call counts.
- **Profiler trace** (Chrome trace JSON → Perfetto UI): Temporal view. Answers "when and why." Shows CPU lane, GPU lane, and the gaps between them.

### 2. The Self vs Total Distinction Is Critical
- **Self CPU/CUDA** = time spent inside the event only (excluding children)
- **CPU/CUDA total** = event + all children
- If `CPU total` ≫ `Self CPU` for a row, the cost lives in children — drill down, not up.

### 3. Overhead-Bound vs Compute-Bound
- **Overhead-bound**: CPU time (ms) dwarfs GPU time (µs). The GPU is idle while the CPU dispatches. Small matrices → fix by making work bigger or fusing ops.
- **Compute-bound**: CPU ≈ GPU time, both in ms. The GPU is the bottleneck — this is where you want to be.

### 4. Cold Start Is Real
First `ProfileStep` is always wider due to workspace allocations, cuBLAS heuristics, and lazy module loading. Use `schedule(wait=1, warmup=1, active=N)` and/or manual warmup loops before profiling.

### 5. The GPU Lane Offset Is a Profiler Artifact
The ~2.5ms gap between CPU and GPU lanes is caused by the profiler's own `Activity Buffer Request` — memory allocation on GPU VRAM for event buffers. Profile 20+ iterations to confirm it only appears once.

### 6. Kernel Runtimes Are Not Constants
Same kernel, same inputs, same hardware — different runtimes across iterations due to GPU clocks (idle/boost), thermals, power management, and driver housekeeping. **Read the trace, not just the mean.**

### 7. Heavyweight Kernels Signal Themselves
Scan the CPU lane for `cudaOccupancyMaxActiveBlocksPerMultiprocessor` — this runtime query only fires for adaptively-launched kernels (GEMM, conv). Elementwise/reduction kernels skip it because their resource footprint (32 registers, zero shared memory) never hits any hardware limit.

### 8. `cudaDeviceSynchronize` Size Tells You Everything
A sync covering 26 µs of GPU work that takes 1.78 ms means the run was 98% idle — textbook overhead-bound symptom.

### 9. torch.compile ≠ Kernel Fusion (Usually)
For a `matmul + add`, Inductor fuses at the **dispatcher level** (`aten::addmm` replaces separate `aten::add` + `aten::mm`), but the GPU kernel is still the same cuBLAS GEMM. The bias add becomes a GEMM epilogue + a `Memcpy DtoD` to seed the destination buffer. True kernel-level fusion (single kernel, no memcpy) is what FlashAttention-style hand-written Triton kernels do.

### 10. torch.compile Has Per-Call CPU Overhead
The Dynamo → AOTAutograd → Inductor stack is ~2× more expensive per step than eager for a single op. This amortizes over ML models with dozens of ops, but for micro-benchmarks it's a tax.

## The Dispatch Chain (Eager)
```
ProfileStep#N → record_function("matmul_add") → aten::matmul → aten::mm → cudaOccupancyMaxActiveBlocksPerMultiprocessor → cudaLaunchKernel
                                                                    → aten::add → cudaLaunchKernel
                → cudaDeviceSynchronize (flush)
```

## The Dispatch Chain (Compiled)
```
ProfileStep#N → Torch-Compiled Region → TorchDynamo Cache Lookup
                                       → AOTDispatcher Runtime Wrapper Prologue
                                       → ## Call CompiledFxGraph <hash> → aten::addmm(b, x, w)
                                                                          → cudaMemcpyAsync (DtoD)
                                                                          → cudaLaunchKernel (GEMM with bias epilogue)
```

## Profiler Setup Recipe
```python
with torch.profiler.profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.CUDA,
    ],
    schedule=torch.profiler.schedule(wait=1, warmup=1, active=3, repeat=1),
) as prof:
    for _ in range(5):
        step()
        prof.step()

# Table
print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=15))

# Trace (open in https://ui.perfetto.dev)
prof.export_chrome_trace("trace.json")
```

## Cheatsheet: Diagnostic Patterns (25 patterns)

See the full 25-pattern cheatsheet in the raw article covering: Profiler Table (5), CPU Lane (6), GPU Lane (5), Dispatch Chain (4), and torch.compile (5).

## Why This Matters

This series bridges the gap between "I know I should profile" and "I can actually read a trace." Part 2 will scale up to `nn.Linear` and MLPs. Part 3 will apply everything to LLMs with `transformers`. The mental models from a single `matmul + add` — overhead-bound vs compute-bound, cold start, kernel variance, occupancy queries, dispatcher-level vs kernel-level fusion — travel directly to production workloads.

## Series
- **Part 1 (this post):** `matmul + add` — learn to read traces
- **Part 2 (coming):** `nn.Linear` + MLP — optimize from traces
- **Part 3 (coming):** LLMs with `transformers` — real-world profiling
