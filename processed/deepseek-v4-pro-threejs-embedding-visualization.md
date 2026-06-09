---
tags: ["coding-tools", "evals", "models", "visualization", "deepseek", "embeddings"]
source: https://x.com/neural_avb/status/2057088461887451530
raw: "[[raw/neural_avb_2057088461887451530]]"
date: 2026-05-17
type: note
related: ["how-to-build-your-own-llm-from-scratch-in-5-stages"]
---

# DeepSeek-V4 Pro: Three.js Embedding Visualization

## Summary
@neural_avb used DeepSeek-V4 Pro to build an interactive Three.js visualization of 4,000 LLM responses embedded in 2D space. The project demonstrates using a frontier model as a coding assistant for creative ML visualization work.

## Key Takeaways
- **Pipeline:** Generate thousands of responses at different temperatures → DistilBERT embeddings → UMAP+PCA to 2D → Judge LM (local Qwen) for correctness + Vendi scores for semantic diversity + EAD for lexical diversity
- **Visualization:** Three.js buildings where height = generation quality/correctness, color = task type, proximity = embedding similarity
- **DeepSeek-V4 Pro** handled: running embedding models, writing judge script using outlines, building the interactive Three.js page
- The model required handholding but got "so much of it done"
- Demonstrates frontier models as capable coding partners for ML visualization workflows

## Connections
- [[how-to-build-your-own-llm-from-scratch-in-5-stages]] — training and evaluating small language models
