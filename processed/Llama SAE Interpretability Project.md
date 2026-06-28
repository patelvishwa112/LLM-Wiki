---
tags:
  - mechanistic-interpretability
  - sparse-autoencoders
  - sae-steering
  - llama
  - mlx
  - llm
  - research
  - personal-project
type: concept
description: "Personal Llama SAE interpretability project — sparse autoencoders and steering on local MLX stack."
created: 2026-05-30
status: active
repo: https://github.com/patelvishwa112/llama-sae-interp
related:
  - "[[Bookmarks Index]]"
  - "[[SAE Interpretability]]"
---

# Llama SAE Interpretability — Steering LLM Behavior via Sparse Autoencoders

**Started:** May 2026
**Status:** 4 confirmed steerable features, fully reproducible
**Hardware:** Apple M1 Mac Mini, 8GB RAM
**Framework:** MLX + PyTorch (SAEs in safetensors)

## What We Did

Built a complete SAE steering pipeline that successfully controls LLM behavior through direct decoder vector addition. The key constraint: **8GB RAM** forced a three-phase memory-isolation design where the model and SAE never coexist in memory except for the final lightweight steering step.

## Architecture

### Three-Phase Pipeline (memory-isolated)

| Phase | What | Memory | Output |
|-------|------|--------|--------|
| 1. Activation Capture | Llama 3.2 1B forward pass, capture MLP outputs | ~2.5GB | `activations_L{N}.npz` |
| 2. SAE Encoding | SAE encoder + top-K=32 sparsification | ~1GB | `features_L{N}.npz` |
| 2c. DLA Scoring | W_dec · embeddings dot product, rank features | ~1.5GB | Steering vectors |
| 3. Direct Decoder Steering | h += α · W_dec[f] per autoregressive step | ~2.5GB | Steered generation |

### Key Design Decisions

- **DIRECT DECODER ADDITION** (`h += α · W_dec[f]`) — works cleanly at 2-3× scale
- **Encode-clamp-decode FAILS** — SAE reconstruction error (~5-15%) introduces artifacts that cause model collapse
- **Top-K=32 sparsification** on encoder output
- **DLA scoring with noise-floor context** for feature selection
- **Path-independent config.py** — zero hardcoded paths, works from any CWD

## Confirmed Steerable Features

| Feature | Layer | ID | DLA | Token | Scale | Effect |
|---------|-------|----|-----|-------|-------|--------|
| Bullet Points | L12 | 105206 | 0.431 | `-` | 2.5× | Numbered → bullet |
| Compliance | L11 | 29679 | 0.376 | `Sure` | 2.5× | "I need help" → "Yes, I'd help" |
| Exclamation | L13 | 90138 | 0.418 | `!` | 2-4× | Prose → exclamations |
| Enthusiasm | L13 | 109639 | 0.545 | `great` | 4× | Neutral → "great/bad" framing |

## Key Discoveries

1. **Scale Sweet Spot:** 2-3× is the range. Below 1× = no effect. Above 5× = token collapse. Found via systematic scale sweep (0.5× to 8×).

2. **Why Direct Decoder Works:** `W_dec[f]` IS the feature's learned contribution direction. Adding it directly is exactly what the model expects. The encode-clamp-decode cycle introduces artifacts the model was never trained on.

3. **DLA is Critical:** Direct Latent Access analysis with noise-floor context (random features) revealed which features truly respond to tokens vs. being noise-correlated.

4. **Memory Design Matters:** A three-phase design with disk as intermediate storage between phases makes SAE research feasible on consumer hardware.

## Failed Approaches (Documented)

- **Encode-clamp-decode:** Activation collapse — SAE lossiness amplifies reconstruction artifacts
- **Single-position steering:** L12-L13 attention heads ignore single-token perturbations
- **Factual knowledge steering:** Discrete answers not on continuous semantic dimensions
- **Language features from literature:** Correlate with but don't causally control language

## Reproducibility

```bash
git clone https://github.com/patelvishwa112/llama-sae-interp
pip install -r requirements.txt
python download_model.py  # requires HF token
python download_sae.py     # open access
python batch_test.py       # validates all 4 features
```

## Article

Full 21KB article at [ARTICLE.md](https://github.com/patelvishwa112/llama-sae-interp/blob/main/ARTICLE.md) — journey from 0% to 4 confirmed behavioral changes, with runnable code snippets explaining every piece.

## Future Directions

See Claude Code research session for next research directions in SAE interpretability space.
