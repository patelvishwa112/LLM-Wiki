---
tags:
- trimming
- pruning
- model-compression
- vocabulary
- multilingual
- embeddings
- inference-optimization
- huggingface
source: https://huggingface.co/blog/lbourdois/introduction-to-trimming
raw: '[[raw/hf_trimming_intro_2026-05-28]]'
date: 2026-05-28
type: bookmark
author: Loïck BOURDOIS et al.
description: Introduction to Trimming ✂
---

# Introduction to Trimming ✂

## Key Takeaways

- **Trimming is vocabulary-targeted pruning** — removes tokens from a model's vocabulary and updates the embedding + lm_head layers. No retraining needed, runs on CPU.
- **Two main use cases:** (1) Remove unused languages from multilingual models, (2) Make vocabulary size a multiple of 8 or 64 for GPU optimization (Karpathy's 25% speedup observation).
- **Massive parameter savings:** granite-embedding-107m went from 107M → 17M (-83.84%) with a 16K vocab. Even conservative 32K vocab trims show 20-60% reductions.
- **Performance generally maintained or slightly improved** — hypothesis is that removing noisy/unused tokens benefits the model. In 5/8 embedding model cases, the trimmed 32K model slightly outperformed the original.
- **One hard limitation:** Trimming only works when the embedding layer is the LAST layer of the network. Dense layers on top (like embeddinggemma's architecture) cause degradation. Same issue with reranker models (classification head on top).
- **5,526 trimmed models released** across architectures: text encoders, encoder-decoders, decoders, embedding models, VLMs. Covers English, Dutch, French, Korean, Tamil, Arabic, German, Spanish.
- **Prior art gap filled:** Previous tools (smaller-transformers, hf-trim, lm-vocab-trimmer) were limited to sentencepiece tokenizers, specific architectures (mBERT, mT5, mBART), and didn't allow controlling final vocabulary size. This work handles BPE tokenizers, multiple architectures, and arbitrary target vocab sizes.

## Summary

Trimming is a lightweight model compression technique that surgically removes tokens from a model's vocabulary and updates only the embedding-related layers (token embedding matrix and language modeling head). Unlike full pruning which modifies the transformer backbone, trimming touches only the vocabulary surface — making it fast, CPU-friendly, and training-free.

The technique is particularly impactful for multilingual models where many languages in the vocabulary go unused. For example, cutting a 250K-token vocabulary down to 16K-32K English-only tokens can shrink a 107M parameter embedding model to 17M parameters while maintaining benchmark performance on MTEB.

The authors tested trimming across 16 models spanning text embeddings (granite-embedding, multilingual-e5, bge-m3, Qwen3-Embedding, embeddinggemma), text encoders, encoder-decoders, decoders (GPT-2, gemma-3), and VLMs. Results show consistent parameter savings with minimal to no performance degradation — and in several cases, slight improvements attributed to noise removal from the vocabulary.

The key architectural constraint: trimming only works when the embedding layer is the final layer before the output. Models with additional dense layers post-embedding (like embeddinggemma's two dense layers) or classification heads (rerankers) show degradation because those layers expect the full vocabulary dimensionality.

This technique is immediately practical for anyone deploying multilingual models where only a subset of languages is needed, or for optimizing older models whose vocabulary size isn't a multiple of 64.

## Source

[Introduction to Trimming — Hugging Face Blog](https://huggingface.co/blog/lbourdois/introduction-to-trimming)

## Authors

Loïck BOURDOIS, Tom Aarsen, Bram Vanroy, Christopher Akiki, Woojun Jung, Manuel Romero, Prithiv Sakthi — Hugging Face Fellows collaboration across 8 languages.
