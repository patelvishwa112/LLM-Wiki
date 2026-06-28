---
tags:
- llm
- inference
- kv-cache
- transformers
- attention
- ttft
- prefill
- gqa
- mqa
- fundamentals
- serving
- gpu
source: https://x.com/_avichawla/status/2034902650534187503
date: 2026-03-20
type: bookmark
author: _avichawla
summary: 'Avi Chawla: six-part KV cache primer — last-token generation, Q/K/V reuse,
  O(n²) waste without cache, prefill vs decode (TTFT), memory cost (Qwen 72B example),
  GQA/MQA and paged attention follow-ons; ~5× decode speedup; links provider prompt
  caching as separate TTFT lever.'
raw: '[[raw/_avichawla_2034902650534187503]]'
description: 'Avi Chawla: six-part KV cache primer — last-token generation, Q/K/V
  reuse, O(n²) waste without cache, prefill vs decode (TTFT), memory cost (Qwen 72B
  example), GQA/MQA and paged attention follow-ons; ~5× decode speedup; links provider
  prompt caching as separate TTFT lever.'
---

# KV Caching in LLMs (Avi Chawla)

Canonical **first-principles** walkthrough — complements shorter [[what-is-kv-cache-llms]] (Amit Shekhar).

## Mechanism

| Phase | Work |
|-------|------|
| Without cache | Recompute all K,V every decode step |
| With cache | Append K,V for new token; attend with cached prefix |

Only last-token **Q** is fresh each step; past **K,V** are stable.

## User-visible effect

Slow **first token** = **prefill** (build cache). Fast stream = **decode** (cache hits).

## Scale constraints

- Memory ∝ layers × seq × hidden (per request)
- **GQA/MQA** reduce KV footprint
- Context length ↔ concurrency tradeoff
- **PagedAttention** (vLLM) addresses fragmentation — see [[how-vllm-works-amitiitbhu]]

## Agent / harness link

Provider **prompt caching** ([[deep-agents-prompt-caching]]) reuses KV across *requests* with identical prefixes — same physics, different lifecycle than per-session decode cache.

## Related

- [[what-is-kv-cache-llms]]
- [[how-vllm-works-amitiitbhu]]
- [[how-gpu-executes-code-first-principles]]
- [[mlx-engine-v185-kv-cache-agentic]]
- [[deep-agents-prompt-caching]]
- [[inference-engines-2026]]