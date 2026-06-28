---
tags:
- transformers
- attention
- llm
- fundamentals
- math
- qkv
- softmax
- embeddings
- education
source: https://x.com/amitiitbhu/status/2040027305297526811
date: 2026-04-03
type: bookmark
author: amitiitbhu
summary: 'Amit Shekhar: hand-worked scaled dot-product attention on "I love AI" —
  X→Q/K/V via learned weights, QK^T scores, ÷√d_k, row softmax (e.g. I→love 70.7%),
  multiply V; bridges to KV cache (only last row needed at decode).'
raw: '[[raw/amitiitbhu_2040027305297526811]]'
description: 'Amit Shekhar: hand-worked scaled dot-product attention on "I love AI"
  — X→Q/K/V via learned weights, QK^T scores, ÷√d_k, row softmax (e.g. I→love 70.7%),
  multiply V; bridges to KV cache (only last row needed at decode).'
---

# Scaled Dot-Product Attention (Worked Example)

End-to-end **numeric** tutorial for `softmax(QK^T/√d_k)V` — prerequisite for [[what-is-kv-cache-llms]] and [[kv-caching-llms-clearly-explained-avichawla]].

## Intuition

| Role | Meaning |
|------|---------|
| **Query** | What this token is looking for |
| **Key** | What this token advertises |
| **Value** | Content to aggregate if match is strong |

Dot product Q·K = relevance score; softmax → distribution over tokens; multiply **V** → new contextual embedding.

## Why √d_k scaling

Large dot products → peaked softmax → vanishing gradients. Dividing by √d_k keeps scores in a learnable range (author notes deeper theory as follow-up).

## Toy result (I row)

After softmax, **70.7%** weight on "love" → output vector dominated by love's **V** — demonstrates contextual mixing in one layer.

## Production scale

Same math at d=512–8192+; W_Q, W_K, W_V trained; stacked in multi-head and deep blocks ([[everything-you-didnt-want-to-know-about-architectures]] for norm/stability variants).

## Related

- [[what-is-kv-cache-llms]]
- [[kv-caching-llms-clearly-explained-avichawla]]
- [[how-vllm-works-amitiitbhu]]
- [[how-gpu-executes-code-first-principles]]
- [[ai-engineering-roadmap-2026-from-scratch]]
- [[build-your-own-llm-workshop-justin-angel]]