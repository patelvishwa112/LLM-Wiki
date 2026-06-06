---
tags: ["architecture", "transformers", "training", "llm", "hyperparameters", "stability", "attention"]
source: https://youtu.be/lVynu4bo1rY
date: 2026-05-25
type: lecture
duration: "1:29:10"
---

# Everything You Didn't Want to Know About Architectures and Hyperparameters

University lecture surveying transformer architecture choices across 19+ modern open-source models (Qwen, Gemma, LLaMA, Olmo, Grok, etc.). Core thesis: architecture is a tradeoff between generalization, GPU efficiency, and training stability — and most models have converged on similar patterns.

---

## Chapters with Timestamps

### 0:00 — Introduction & Philosophy
The best way to understand architecture is to train models yourself. Second best: learn from everyone else's choices. Survey approach — look at all modern models and ask: what's fixed across all effective architectures, and what can be varied?

- Survey covers 19+ dense models + MoE variants
- Architecture = tradeoff between learning (generalization), GPU efficiency, and stability (not blowing up)
- Historical arc: early experimentation → LLaMA 2 convergence → stability innovations → long context variations

### 5:00 — Pre-Norm: The One Thing Everyone Agrees On
**Key insight: Keep the residual stream clean.**

Original transformer put layer norm in the residual path (post-norm). Every modern model moves it outside — before each computation (pre-norm). This allows gradients to propagate straight through the residual stream, improving both stability and signal propagation.

- Only exception: OPT-350M (widely considered a failed model)
- Pre-norm enables deeper networks without gradient attenuation
- Reduces gradient spikes compared to post-norm
- Warm-up still needed but convergence is much better
- Grok, Gemma 2, Olmo 2 use "post-norm outside residual" — layer norm AFTER computation but still outside residual stream

### 12:30 — RMS Norm: Free Speed Win
**Key insight: Data movement, not FLOPs, is the bottleneck.**

RMS norm drops mean subtraction and bias from layer norm. No expressiveness loss in practice, but significantly faster because it reduces memory movement. Layer norm can be 25% of runtime despite being only 0.17% of FLOPs — because GPUs spend most time moving data, not computing.

- Arithmetic intensity concept: matrix multiplies = high intensity (good), normalization = low intensity (bad)
- 200M param model: RMS norm gives more steps/sec AND better performance
- Bias terms in transformers are generally useless — most implementations drop them entirely

### 18:00 — Activation Functions: SwiGLU over ReLU
SwiGLU (gated activation) replaced ReLU as the standard. Copied from LLaMA, now universal. The gating mechanism provides better signal control.

### 22:00 — Position Embeddings: RoPE
Rotary Position Embeddings are the standard. Encode position via rotation in attention space. More stable than learned absolute positions, especially for long context.

### 28:00 — Hyperparameters: Rules of Thumb
**FF dim = 4× hidden dim** (factor-of-four rule). Nearly universal.  
**Head dim × num_heads = model dimension**. Keep head dim reasonable (64-128).  
**Aspect ratio ≈ 100** (sequence length / batch size).  
**Vocab sizes** keep growing but with diminishing returns — most models use 32K-256K tokens.

### 40:00 — Regularization: The Weight Decay Puzzle
**Key insight: Weight decay is NOT a regularizer — it's an optimizer.**

In single-pass SGD on internet-scale data, overfitting doesn't happen (you never see the same data twice). Yet weight decay persists in modern models. Why? It interacts with learning rate decay to find better minima. Stronger weight decay + learning rate decay → significantly lower final loss.

- Dropout is largely abandoned (doesn't interact well with optimization at scale)
- Weight decay remains widely used despite no overfitting concern
- Counterintuitive: what looks like regularization is actually optimization

### 55:00 — Training Stability: The Softmax Danger Zones
**Key insight: Softmax operations are the primary instability source. Two of them: output and attention.**

Three stability interventions, from gentle to aggressive:

1. **Z-Loss** (Devlin 2014, revived by Baichuan/DCLM/Olmo): Penalize log Z being far from zero. Since softmax is overparameterized, you can push the normalizer toward 1 without affecting outputs. Simple regularizer that prevents blowups.

2. **QK Norm** (from multimodal → language models): Add layer norm to queries and keys BEFORE the attention softmax. Ensures inputs to softmax always have scale ≈ 1. Now standard in virtually all large models. No performance cost, prevents attention degeneracies.

3. **Logit Soft Capping** (Gemma 2/3/4): Hard-cap attention logits with tanh. Strongest intervention — guarantees stability but costs some quality (can't express high-confidence signals). Google-specific trick.

NVIDIA systematic comparison: QK norm wins (slightly better + allows higher learning rate). Soft capping alone loses performance.

### 1:14:00 — Attention Efficiency: GQA and MQA
**Key insight: Inference is memory-bound, not compute-bound.**

The KV cache problem: during autoregressive generation, arithmetic intensity drops to N/D (sequence/dim) — terrible. You're reading parameters constantly with minimal compute.

- **MQA (Multi-Query Attention)**: Share one KV across all heads. Fastest but significant quality loss.
- **GQA (Grouped Query Attention)**: Share KVs across groups of query heads. Sweet spot — nearly full multi-head performance at much lower inference cost. Adopted by virtually all modern models.
- GQA with small head reduction (e.g., 8 query heads → 4 KV heads) gets most of the gains with near-zero quality loss.
- DeepSeek-V2's Multi-head Latent Attention is a different factorization approach.

### 1:25:00 — Sliding Window Attention & Long Context
**Key insight: Alternating global + local attention is the dominant long-context pattern.**

Hybrid architectures: every N layers use full attention, layers in between use sliding window (local). Local layers aggregate information → global layers distribute it.

- Cohere Command A: first open model to do this (1 global : 3 local ratio)
- Llama 4, Gemma 4, Olmo 3: all use sliding window + full attention with RoPE
- Qwen 3.5: same pattern but uses gated DeltaNet (state-space model) instead of sliding window
- Some models drop RoPE for long-range (NoPE) — treat distant tokens as bag-of-words
- This is the most active area of architecture research: managing long context cost

### 1:28:00 — Conclusion
When you look across all models, patterns emerge: pre-norm, RMS norm, SwiGLU, RoPE, GQA, sliding window. Differences exist in tokenization, position embeddings, and how context is handled. The commonalities give you intuition; the differences show where the frontier is.

---

## Key Takeaways

1. **Keep the residual stream clean** — pre-norm is universal because it lets gradients propagate straight through
2. **Data movement > FLOPs** — RMS norm saves ~25% runtime on normalization despite being <1% of compute
3. **SwiGLU, RoPE, GQA** — the holy trinity of modern transformer design, copied from LLaMA and now universal
4. **Weight decay is an optimizer, not a regularizer** — persists despite no overfitting because it helps find better minima with LR decay
5. **Stability through norms** — Z-loss for output softmax, QK norm for attention softmax. If in doubt, add a layer norm.
6. **Long context = hybrid attention** — alternating global + local (or SSM) layers is the dominant pattern
7. **Architecture is co-design** — every choice reflects tension between learning, GPU efficiency, and stability

## Source
- [YouTube: lVynu4bo1rY](https://youtu.be/lVynu4bo1rY)
- [Full timestamped transcript](raw/youtube_lVynu4bo1rY_timestamped.txt) (2649 lines, 110KB)

## Related
- [[how-to-build-your-own-llm-from-scratch-in-5-stages]] — complementary article on the full training pipeline
- [[macro-evals-for-agentic-systems-openai-cookbook]] — systems thinking applied to evals
