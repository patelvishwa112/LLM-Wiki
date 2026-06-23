---
tags: [vllm, inference, serving, kv-cache, pagedattention, continuous-batching, gpu, llm, agents, throughput]
source: https://x.com/amitiitbhu/status/2069384034074107905
raw: "[[raw/amitiitbhu_2069384034074107905]]"
date: 2026-06-23
type: bookmark
author: amitiitbhu
summary: "Amit Shekhar explains vLLM: KV cache as the serving bottleneck, naive max-length reservation vs PagedAttention block tables and prefix sharing, static vs continuous batching, and OpenAI-compatible deployment for chat and agent workloads."
---

# How vLLM Works

By **Amit Shekhar** (@amitiitbhu), Outcome School.

## Serving bottleneck

LLM serving is usually **memory-bound**, not compute-bound: each active request holds a growing **KV cache** through prefill + decode. Naive engines reserve a **full max-length contiguous** buffer per request → wasted RAM and fragmentation → few concurrent users per GPU.

## vLLM core

| Mechanism | What it does |
|-----------|----------------|
| **PagedAttention** | KV in fixed token blocks; block table; on-demand alloc; prefix/beam **sharing** |
| **Continuous batching** | Refill finished decode slots every step (not wait for whole batch) |

Together: higher **throughput** and **utilization** on same hardware; **OpenAI-compatible** HTTP API for drop-in apps.

## Agent angle

Multi-step agents resend large system/tool context each turn — **shared prefix blocks** matter; short decode steps benefit from **continuous batching**.

## Vault links

- [[what-is-kv-cache-llms]] — KV fundamentals (same author)
- [[inference-engines-2026]]
- [[mlx-engine-v185-kv-cache-agentic]]
- [[how-to-design-a-loop-that-prompts-your-agent]]
- [[sakana-fugu-orchestrator-models]] — orchestration (same author, separate article)

## Related

- [[sub-agents-inference-time-scaling]]
- [[0xsojalsec-llms-local]]