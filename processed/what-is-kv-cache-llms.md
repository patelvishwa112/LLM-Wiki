---
tags: ["llm", "transformers", "attention", "kv-cache", "inference", "fundamentals"]
source: https://x.com/amitiitbhu/status/2037413998279491927
date: 2026-03-27
type: bookmark
author: "Amit Shekhar (@amitiitbhu)"
raw: "[[raw/amitiitbhu_2037413998279491927]]"
related: []
---

# What is KV Cache in LLMs?

## Key Takeaways

- **KV Cache prevents redundant computation in autoregressive generation.** Without it, every new token requires recomputing Key/Value for ALL previous tokens. With it, K/V computed once, stored, and reused — ~50x fewer computations for a 100-token sequence.
- **Why only K and V (not Q):** Query is transient — only needed for the current token being generated. Keys and Values of past tokens are needed at every future step. Store what's reused; discard what's ephemeral.
- **Speed vs memory trade-off:** KV Cache consumes more memory (stores K/V for every generated token). For long sequences this can be significant. Paged Attention (next article) addresses this.
- **Simple analogy:** Classroom — Query = new student's question, Key = name tags saying what each student knows, Value = actual notes. Once you've read everyone's name tags and notes, you don't need to ask them to repeat themselves.

## Summary

Amit Shekhar provides a clear, example-driven explanation of KV Cache in LLMs. Starting from how LLMs generate text token-by-token, he walks through the attention mechanism (Q/K/V), demonstrates the repeated computation problem with a worked example, then shows how KV Cache eliminates it by storing and reusing Key/Value pairs. The article closes with the speed-memory trade-off and a preview of Paged Attention.
