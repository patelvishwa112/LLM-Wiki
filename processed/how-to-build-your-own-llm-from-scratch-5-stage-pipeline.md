---
tags: ["llm", "training", "tokenization", "alignment", "rlhf", "data", "evaluation", "transformer", "pretraining", "sft"]
source: https://x.com/sairahul1/status/2066076937806856661
date: 2026-06-14
type: bookmark
author: sairahul1
title: "How To Build Your Own LLM from Scratch (The 5-Stage Pipeline Behind GPT and Claude)"
summary: "A complete 5-stage pipeline for building a working LLM from scratch: data cleaning, BPE tokenization, decoder-only transformer training with next-token prediction, SFT + RLHF alignment, and evaluation with perplexity + human benchmarks. Includes minimal PyTorch code and 5 niche LLM product ideas."
raw: "[[raw/sairahul1_2066076937806856661]]"
---

## Key Takeaways

**The 5-stage pipeline (architecture is the least important part):**
1. **Data** — Brutal multi-step filtering of Common Crawl: HTML extraction, toxicity removal, deduplication, quality scoring, domain balancing. "Data quality beats data quantity."
2. **Tokenization** — BPE tokenizer (32k–100k vocab). Minimal working code provided. 1 token ≈ 0.75 words.
3. **Training** — Next-token prediction on decoder-only transformer (causal self-attention + residual blocks). Minimal 44M-param PyTorch implementation included. Loss = surprise at next token.
4. **Alignment** — SFT (format imitation) + RLHF (preference learning via reward model). SFT needs only a few thousand examples.
5. **Evaluation** — Perplexity during pretraining; human benchmarks (MMLU, Chatbot Arena, AlpacaEval) after alignment. Perplexity becomes misleading post-SFT.

**Scaling rule of thumb:** ~20 tokens of training data per parameter.

**5 high-value niche LLM ideas (same pipeline, different data):**
- Coding Assistant (GitHub + Stack Overflow)
- SQL Query Generator (Spider + WikiSQL)
- US Legal Document Summarizer (CourtListener + MultiLegalPile)
- Medical Symptom Explainer (PubMed + MedQA) — with strict disclaimers
- E-commerce Product Description Writer (high-converting Shopify copy)

**Critical mistakes to avoid:**
- Obsessing over architecture (standardized)
- Treating data as commodity (top labs spend more on cleaning)
- Skipping scaling math (undertrained models waste compute)
- Stopping at SFT (RLHF teaches preference)
- Trusting perplexity after alignment (switch to human evals)

**Core insight:** Two labs with identical architecture produce wildly different models. The architecture is shared; data quality, cleaning, alignment, and honest evaluation are where the real differentiation happens.

**Related concepts in vault:** [[llm-training-pipeline]], [[rlhf]], [[data-quality]], [[transformer-architecture]], [[alignment]]
