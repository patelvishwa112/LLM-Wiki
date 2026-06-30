---
tags:
- pytorch
- torch-compile
- fx
- dynamo
- inductor
- training
- compilation
- debugging
description: "PyTorch 2.0 compile series pt.1 — torch.fx IR (Graph/Node/GraphModule), symbolic tracing via Proxies, and tracing limits before TorchDynamo."
summary: "PyTorch 2.0 compile series pt.1 — torch.fx IR (Graph/Node/GraphModule), symbolic tracing via Proxies, and tracing limits before TorchDynamo."
source: https://x.com/jino_rohit/status/2071247775837356399
date: 2026-06-28
type: bookmark
author: jino_rohit
raw: "[[raw/jino_rohit_2071247775837356399]]"
---

# Torch Internals (Part 1) - FX Graphs

Jino Rohit starts a **PyTorch + torch.compile internals** series. Part 1: **torch.fx** as the shared IR from Dynamo through Inductor.

## Core model

| Object | Role |
|--------|------|
| **Graph** | Ordered DAG of ops (placeholder → calls → output) |
| **Node** | Single op; read `op` before `target`; track `users` for transforms |
| **GraphModule** | Executable module wrapping a traced Graph |

## Symbolic tracing

`symbolic_trace` runs `forward` with **Proxy** tensors — hooks record ops as nodes, no real compute. Enables graph surgery and compiler handoff.

**Fails on:** data-dependent branches, arbitrary Python helpers. **OK on:** static flags fixed at init.

## Series arc

FX (this post) → **TorchDynamo** next (bytecode JIT, graph breaks).

## Related

- [[pytorch-profiler-beginners-guide]]
- [[how-gpu-executes-code-first-principles]]
- [[training-llm-from-scratch-5-lessons]]