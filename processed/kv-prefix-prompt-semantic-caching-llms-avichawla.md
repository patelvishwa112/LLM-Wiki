---
tags: ["llm", "inference", "kv-cache", "serving", "vllm", "prompt-caching", "cost-optimization", "transformers", "fundamentals"]
source: https://x.com/_avichawla/status/2093265776266637739
date: 2026-08-28
type: bookmark
description: "Avi Chawla: four LLM cache layers (KV, prefix, prompt, semantic) from first principles — what each stores, what breaks reuse, RAG/LMCache, Anthropic billing."
author: _avichawla
summary: "Avi Chawla: four LLM cache layers (KV, prefix, prompt, semantic) from first principles — what each stores, what breaks reuse, RAG/LMCache, Anthropic billing."
raw: "[[raw/_avichawla_2093265776266637739]]"
---

# KV, Prefix, Prompt and Semantic Caching in LLMs

Avi Chawla (@_avichawla, 2026-08-28). Sequel to [[kv-caching-llms-clearly-explained-avichawla]]: four things called “caching” store four different objects. Demos on SmolLM2-360M (transformers v5 `DynamicCache`); vLLM internals in pseudocode; one Anthropic API example.

| Layer | Stores | Keyed by | On miss | Correctness |
|-------|--------|----------|---------|-------------|
| **KV cache** | K/V tensors, one request | in-process `past_key_values` | recompute prefill/decode | exact, neutral |
| **Prefix caching** | same tensors, kept after the request | hash chain over token-ID blocks (vLLM default 16) | re-prefill from first miss | exact, neutral |
| **Prompt caching** | provider’s billed prefix reuse | rendered prompt + `cache_control` breakpoint | pay full input | exact, neutral |
| **Semantic cache** | finished **response strings** | cosine NN over embeddings | run the model | **fuzzy — can be wrong with HTTP 200** |

First three save **prefill** (decode cost unchanged). Semantic is the only layer that also skips **output** tokens — and the only one that can return a wrong answer silently.

## KV (per request)

Prefill writes K/V per token per layer; decode appends one pair. Queries are not cached (causal mask: Q is used once). Decode becomes **HBM-bandwidth bound**. ~40 GB KV for 70B BF16 @ 128K. Shrink via GQA, DeepSeek MLA, or 4-bit quantized cache (`quanto`; can be slower on short contexts). Engine **frees** the cache when the request ends unless you persist `past_key_values` across turns — otherwise turn 20 re-prefills 1–19.

## Prefix (server block reuse)

Keep KV blocks after the request; index with a **parent-hash + token-ID** chain so reuse is exact-prefix only. Refcounts pin live blocks; LRU drops unreferenced ones (same GPU pool as the running batch). **Salt** isolates tenants. Only **complete** blocks are cached (tail always recomputed). Unique-prompt traffic can **regress** throughput (hashing cost, no hits).

**RAG:** chunk reorder shares nothing under the chain. Stitching per-chunk caches is wrong (positional encodings, no cross-chunk attention, extra sinks). **LMCache / CacheBlend** reuses chunks at arbitrary positions and recomputes a small corrective subset (~2–3× TTFT claimed vs full prefill). https://github.com/LMCache/LMCache

## Prompt (provider billing)

Same KV reuse, billed: write ~**1.25×**, read **0.1×** (Anthropic/OpenAI as of the article). Marker on the **last** stable block; variable content below it. Both usage counters zero = below minimum cacheable length (no error). Anthropic walks back ~**20 blocks** — long chats lose the write. Provider-injected system text is part of the rendered prefix.

## Semantic

Embed every request (hit **and** miss). Thresholds 0.75–0.97 are traffic-specific. Negation vs paraphrase can sit <0.01 cosine apart. Cache stores answers with **no correctness check**. Prefer measuring **byte-identical** repeat rate before embeddings (exact response cache: no false positives, lower hit rate).

## Production takeaways

- Stable content first, variable last, marker on the boundary.
- Tool-schema reorder, web search / citations / thinking / `tool_choice`, A/B reasoning effort, history **summarization**, or routing to another model all split or cold the cache. Truncate tool outputs **in place**.
- Debug misses on **token IDs**, not logged text (BOS, default system template, newlines).

## Skeptical read

- 360M laptop KV demos ≠ production scheduler/eviction.
- LMCache TTFT multiple is the author’s report, not a reproduced bench here.
- Provider prices, TTL, and the 20-block walk are vendor-dated.
- GIFs/video in the X article are not in the text raw.

## Related

- [[kv-caching-llms-clearly-explained-avichawla]]
- [[what-is-kv-cache-llms]]
- [[how-vllm-works-amitiitbhu]]
- [[deep-agents-prompt-caching]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[opus-48-token-economy-guide]]
