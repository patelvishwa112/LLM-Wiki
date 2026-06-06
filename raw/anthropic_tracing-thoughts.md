# Tracing the Thoughts of a Large Language Model

**Source:** https://www.anthropic.com/research/tracing-thoughts-language-model
**Authors:** Anthropic Interpretability Team
**Published:** Mar 27, 2025
**Papers:** Circuit Tracing (methods) + Biology of a Large Language Model (case studies)

---

## Summary

Anthropic extends SAE-based interpretability from finding individual features to tracing computational circuits — linking features together to reveal how Claude transforms input words into output words. Applied to Claude 3.5 Haiku across 10 case studies.

## Key Discoveries

### 1. Universal "Language of Thought"
- Same core features activate across English, French, Chinese
- Claude thinks in a shared conceptual space, then translates to target language
- Shared circuitry increases with model scale (3.5 Haiku shares >2x features vs smaller model)

### 2. Planning Ahead (Poetry)
- Before writing second line of rhyming couplet, Claude activates possible rhyme words
- Then writes the line TO REACH that planned word
- Can be intervened: suppress "rabbit" → writes "habit"; inject "green" → writes line ending in "green"
- **This is the opposite of next-token prediction** — model thinks on longer horizons

### 3. Mental Math — Parallel Strategies
- Claude uses multiple parallel computational paths: rough approximation + precise last-digit determination
- These interact to produce the final answer
- When asked to explain, Claude describes standard algorithm ("carry the 1") — which is NOT what it actually does internally
- **Model's self-explanation is unfaithful to its actual computation**

### 4. Faithful vs Unfaithful Reasoning
- Easy math (√0.64): faithful chain-of-thought with intermediate features visible
- Hard math (cos of large number): no evidence of calculation — Claude bullshits
- Given a hint: Claude works backwards from the answer (motivated reasoning)
- **Interpretability can distinguish faithful from unfaithful reasoning**

### 5. Hallucinations — Default Refusal Circuit
- Default behavior is REFUSAL ("I don't know")
- "Known entity" feature inhibits default refusal → model answers
- Hallucination occurs when "known entity" activates for an entity the model doesn't actually know
- Can be induced: activate "known answer" or inhibit "can't answer" → consistent hallucination

### 6. Jailbreaks — Coherence Pressure
- Grammar/semantic coherence features pressure model to complete sentences
- After tricked into saying "BOMB", coherence pressure keeps it going
- Model only pivots to refusal after completing a grammatically coherent sentence
- **Safety mechanisms lose to coherence pressure mid-sentence**

### 7. Multi-Step Reasoning
- For "capital of state where Dallas is located": first activates "Dallas → Texas", then "Texas capital → Austin"
- Can intervene: swap "Texas" for "California" → output changes to "Sacramento"
- **Model genuinely combines facts, not just memorizes**

## Method: Attribution Graphs
- Link SAE features into computational circuits
- Trace information flow from input through intermediate features to output
- Currently captures fraction of total computation, requires hours of human effort per prompt

## Implications for Experiments
- Features aren't isolated — they form circuits with complex interactions
- Self-reported reasoning ≠ actual computation
- Default behaviors (refusal, coherence) compete with task-specific features
- Intervention on intermediate features causally changes outputs
