---
title: "vLLM's Architecture, Appreciated: Paging, Blocks, and Continuous Batching"
type: bookmark
description: "A conceptual walkthrough of why vLLM is cleanly designed — prefill versus decode, KV cache growth as the core memory problem, PagedAttention block tables borrowed from OS paging, and continuous batching."
tags: [vllm, inference, serving, kv-cache, pagedattention, continuous-batching, gpu]
source: https://x.com/attharrva15/status/2103918757446062165
date: 2026-09-26
author: Atharva
summary: "A conceptual walkthrough of why vLLM is cleanly designed — prefill versus decode, KV cache growth as the core memory problem, PagedAttention block tables borrowed from OS paging, and continuous batching."
raw: "[[raw/attharrva15_2103918757446062165]]"
---

# vLLM's Architecture, Appreciated: Paging, Blocks, and Continuous Batching

**Source:** Atharva (@attharrva15), 2026-09-26. A short appreciation post — explicitly not a tutorial — explaining why vLLM's design reads as clean engineering rather than cleverness.

The setup is the standard inference asymmetry, stated plainly: prefill pushes all input tokens through the GPU at once and is compute-bound, while decode moves the weights plus the whole KV cache to emit a single token and is bandwidth-bound. Since output length is unknown when a request arrives, the KV cache grows unpredictably, and that is where naive servers die. Reserving a max-length contiguous block per request wastes memory; packing tightly means constant moving and resizing; and static batching makes every short request wait for the longest one in the batch. The post's framing of the problem is the cleanest part — a production server must accept requests of different prompt lengths, different output lengths, and unpredictable cache growth, while still keeping the GPU busy.

The answer, in the author's telling, is borrowed rather than invented. PagedAttention splits each request's KV cache into fixed-size blocks and keeps a per-request block table mapping logical blocks to physical ones, exactly as an OS maps virtual pages to frames — which also makes prefix sharing between similar prompts nearly free, since two requests can point at the same physical blocks. Continuous batching is the complementary move: finished requests leave the batch immediately instead of holding the slot until the longest sequence completes. The author's own summary is that nothing here is sorcery — paging applied to the KV cache, batching that refuses to wait, and a scheduler that keeps asking what work can be done right now.

Treat the numbers accordingly: the post mentions roughly 3% memory wastage from fragmentation as something the author "heard," with no measurement, benchmark, or reproduction behind it, and no code. Its value is pedagogical — the OS-paging analogy and the prefill/decode intensity split are the two mental models worth carrying into any serving discussion.

## Why it matters

Almost every serving cost question reduces to KV cache memory management and batch utilization, and this post gives the shortest correct explanation of why the naive approaches fail. The deeper point for builders is methodological: vLLM's wins came from importing a proven systems abstraction (virtual memory paging) rather than inventing a new one, which is a reliable heuristic when facing a novel-looking infrastructure problem. Useful as an orientation piece before reading engineering-level material on the same engine.

## Key points

- Prefill is compute-bound (all input tokens processed in parallel); decode is bandwidth-bound (weights plus KV cache read to produce one token).
- The core constraint is that output length is unknown at admission time, so KV cache size is unpredictable — contiguous max-length reservation wastes memory and tight packing forces expensive relocation.
- PagedAttention splits KV cache into fixed-size blocks with a per-request logical-to-physical block table, mirroring OS virtual memory paging, and enables sharing physical blocks across requests with common prefixes.
- Continuous batching replaces static batching, so completed requests free their slots instead of waiting for the longest sequence in the batch.
- The ~3% fragmentation figure is second-hand in the post ("I heard"), with no benchmark or setup given — treat it as illustrative, not measured.
- The author's thesis is that vLLM's quality is compositional: it reuses working systems abstractions rather than inventing new mechanisms.

## Related

- [[how-vllm-works-amitiitbhu]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[what-is-kv-cache-llms]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[efficiently-scaling-transformer-inference-checklist-wafer]]
- [[inference-engines-2026]]
