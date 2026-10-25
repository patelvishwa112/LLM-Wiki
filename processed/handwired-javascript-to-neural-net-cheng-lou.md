---
title: "Handwired: compiling JavaScript into a trainable neural net"
type: bookmark
description: "Cheng Lou's Handwired rewrites ordinary JS into one matmul of hand-written weights plus ReLU — no training, exact, fully differentiable, 9,909 weights for a mini OS."
tags: [architecture, ml-research, gpu, inference, parallelism, differentiable-programming, compilers]
source: https://x.com/_chenglou/status/2110558507699466522
date: 2026-10-14
author: Cheng Lou
summary: "Cheng Lou's Handwired rewrites ordinary JS into one matmul of hand-written weights plus ReLU — no training, exact, fully differentiable, 9,909 weights for a mini OS."
raw: "[[raw/_chenglou_2110558507699466522]]"
---

# Handwired: compiling JavaScript into a trainable neural net

**Source:** Cheng Lou (@_chenglou), 2026-10-14. A two-line post pointing at the Handwired landing page and repo — a compiler that lowers normal JavaScript into a neural network.

The mechanism is small and legible. Every branch becomes arithmetic: `a > 4 ? 10 : 12` turns into `above4 = relu(a - 4) - relu(a - 5)`, where the mask is 1 above the threshold and 0 below, and then into `above4 * 10 + (1 - above4) * 12`. Both branches are always computed and the mask selects one. Loops and mutable state get the same treatment, and the resulting `+`, `*` and `relu` are collected into a single large matmul that runs either in JS or on WebGPU. Because only those two primitives exist, the compiled program is differentiable end to end while its weights were written by a human rather than learned — training is zero by construction.

That inversion is the interesting part: the network is a faithful, exact encoding of a program you already trust, and gradient descent becomes an optional post-processing step rather than the source of the weights. The README's three payoffs are (1) the whole program stays differentiable, (2) no training is needed, and (3) weight-free, primitive-only graphs are cheap for standard GPU work — fusion, sparsity, reordering. The demos make that concrete: HandwiredOS, a small desktop (windows, stacking, scroll, drag, images) shipped as **9,909 weights across 130 layers with 0 training**; a "learned gallery" that unfreezes a compiled program's weights and trains them live; and a JSON search over **100,000 documents** where JS-written regex, parsing and highlighting are compiled into WebGPU kernels and run in milliseconds.

The speculative uses he floats are the ones worth watching: unfreezing weights to see what training does to a program you understand, and bolting a frozen program onto a generic net so one model carries both Shakespeare and your particular UI. The framing stays honest — the landing page calls it a tutorial to play with, and the repo's `lab/` folder is explicitly described as old experiments.

## Why it matters

This is a differentiability answer to a problem harness engineers hit constantly: how do you get a model to steer deterministic code without rewriting it as a probabilistic policy. Handwired keeps the program exact and makes it gradient-compatible — program logic as initial weights, training as fine-tuning of behaviour rather than replacement of it.

The economics are also unusual. Existing accelerator tooling (fusion, sparsity) applies because the graph is nothing but matmul and ReLU, so single-threaded JS written for readability gets GPU-scale parallelism for free — the JSON-search demo is the proof. And because every weight is human-written, the network is inspectable in a way trained models are not.

## Key points

- Compilation rule: comparisons become differences of two ReLUs; conditional branches are both evaluated and blended by the mask; `+`, `*`, `relu` collapse into one matmul.
- "No training, exact, fully differentiable, runs in a browser without GPU" — the landing page's four claims.
- HandwiredOS: 9,909 weights, 130 layers, 0 training, rendering to regular DOM.
- JSON search demo: 100k documents, regex + JSON parsing + highlighting written in JS then compiled to WebGPU kernels, milliseconds.
- Because the primitive set is minimal, GPU fusion/sparsity/reordering have little to optimize away — the structural reason it is fast.
- Open experimental directions: unfreeze and train compiled weights; attach a frozen program to a generic net and train end to end.
- Repo: 825 commits, 2 tags, last commit 2026-10-17, Claude Code as co-author; `bun install && bun start`, entry points in `docs/`, `src/`, `template/`.

## Related

- [[torch-internals-part1-fx-graphs]]
- [[looped-transformers-explained-neural-avb]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[build-your-own-llm-workshop-justin-angel]]
