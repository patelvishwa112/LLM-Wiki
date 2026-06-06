# Everything You Didn't Want to Know About Architectures and Hyperparameters
URL: https://youtu.be/lVynu4bo1rY
Type: YouTube Lecture

---

## Summary
Lecture surveying modern transformer architectures across major open-source models.

## Key Topics Covered

### 1. Architecture Variations (The Building Blocks Everyone Agrees On)
- **Pre-Norm**: Move layer norm outside residual stream. Universal adoption. Keeps residual stream clean for gradient propagation.
- **RMS Norm**: Drop mean subtraction and bias. Saves ~25% runtime on normalization despite being <1% of FLOPs. Data movement is the bottleneck.
- **SwiGLU over ReLU**: Standard activation in modern transformers, copied from LLaMA.
- **RoPE**: Rotary position embeddings, standard for position encoding.

### 2. Hyperparameter Rules of Thumb
- FF dim = 4× hidden dim (factor-of-four rule)
- Head dim × num_heads = model dimension
- Aspect ratio ≈ 100 (sequence length / batch size)
- Weight decay persists even though overfitting isn't a concern in single-pass SGD — it interacts with optimizers in surprising ways
- Vocab sizes keep growing but with diminishing returns

### 3. Stability Tricks
- **Z-Loss**: Regularize the log normalizer of the output softmax to be near zero. From Devlin 2014, adopted by Baichuan, DCLM, Olmo.
- **QK Norm**: Add layer norm to queries and keys before attention softmax. Stabilizes attention. Universal in large models.
- **Logit Soft Capping** (Gemma): Hard-cap attention logits with tanh. Safe but costs some quality.

### 4. Attention Efficiency
- **GQA (Grouped Query Attention)**: Share keys/values across groups of query heads. Sweet spot between multi-head (expressiveness) and multi-query (speed). Adopted by nearly all modern models.
- **Sliding Window Attention**: Alternate between global attention layers and local windowed layers. Llama 4, Gemma 4, Olmo 3 all use this. Qwen 3.5 uses gated DeltaNet instead of sliding window.
- **MQA**: Multi-query attention — one KV for all heads. Fast but quality loss.

### 5. Models Surveyed
Qwen 2/3, Gemma 2/3/4, LLaMA 2/3/4, InternLM2, Olmo 2/3, Grok, Command A, NeMo Tron 4, and ~19 other dense models.

### Core Insight
Architecture choices are tradeoffs between: learning from data (generalization), training efficiently on GPUs, and not blowing up (stability). Most models have converged on similar patterns — pre-norm, RMS norm, SwiGLU, RoPE, GQA, sliding window. The variation is in how they handle long context and stability.

## Tags
architecture, transformers, training, llm, hyperparameters, stability, attention
