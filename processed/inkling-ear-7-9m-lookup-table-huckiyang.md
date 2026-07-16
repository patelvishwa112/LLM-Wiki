---
tags:
  - models
  - multimodal
  - audio
  - speech
  - inference
  - serving
  - moe
  - quantization
  - thinky-machines
  - asr
source: https://x.com/huckiyang/status/2077625513384841679
date: 2026-07-16
type: bookmark
description: "Huck Yang on Thinky Inkling audio — no encoder; 7.9M dMel embedding table at 20 tok/s; strong ASR/style evals; SGLang multi-state serve."
author: huckiyang
summary: "Huck Yang on Thinky Inkling audio — no encoder; 7.9M dMel embedding table at 20 tok/s; strong ASR/style evals; SGLang multi-state serve."
raw: "[[raw/huckiyang_2077625513384841679]]"
---

# Inkling's Ear Is a 7.9M Lookup Table

@huckiyang on **Thinky Machines Inkling**: 975B MoE (41B active), 1M context, Apache-2.0, pretrained from scratch on 45T tokens (text, images, audio, video). Speech-research hook: **no audio encoder**.

## Front end (entire “ear”)

1. 16 kHz mono → 80-channel log-mel, 50 ms hop (**20 tokens/sec**)  
2. Each mel bin quantized to **16 levels** (dMel, Bai et al. 2024)  
3. `nn.Embedding(80×16=1280 → 6144)`  
4. Sum the 80 rows → **one audio token**

~**7.9M** parameters. No conv tower, no transformer encoder, no projector. Contrast Whisper-style ~50 tok/s + ~100M encoder. One minute speech ≈ 1,200 tokens → ~14 hours in a 1M window (upper bound).

Encoderless design aligns with scaling-law intuition for large omni models.

## Quality (surprisingly little loss)

Model post (thinking effort 0.99): AudioMC **56.6** (next open omni ~37.6); MMAU **77.2**; VoiceBench **91.4** (near Qwen3.5 Omni-Plus). Gemini 3.1 Pro still leads closed.

Reproducible Tinker cookbook:

| Task | Result |
|------|--------|
| LibriSpeech | ~**0.06 WER** zero-shot |
| Medical ASR (EkaCare, Indian accent, drugs) | WER 0.157→**0.072**, entity recall 0.806→**0.915** after LoRA SFT; generalizes to unseen drug names |
| Expresso emotion | Style accuracy 0.361→**0.852** (SFT + GRPO style+WER); WER 0.095→**0.044** |

Sixteen levels per bin still carries **what** and **how** (prosody/style).

## Serving

- Prompt: whole clip = **one sentinel**; prefill expands to `20 × seconds` positions  
- Decoder treats audio like text: sliding-window + global attention **5:1**, learned relative bias (not RoPE), width-4 causal conv mixing with 3 predecessors  
- State: full KV + sliding-window KV + short-conv state; **SGLang** unified radix cache with typed pages (conv pool from Mamba path); prefill-decode disaggregation ships all three  
- B200 day-0: **71.7k** input tok/s @ batch 32  

Open: `audio_mode: "dmel" | "flow"` with **flow** undocumented (guess: future audio generation); dmel min-value config vs code mismatch; long-form / multilingual / noise behavior.

Full figures: https://huckiyang.github.io/blog/inkling-audio-design.html

## Why it matters

Shows aggressive **tokenization-first** audio for frontier omni models: tiny discrete front end into a unified decoder, plus non-trivial multi-state serving. Useful for speech, multimodal scaling, and inference-stack design.

## Related

- [[multi-gpu-inference-tp-pp-sp-ep-mainzonx]]
- [[how-vllm-works-amitiitbhu]]
- [[inference-optimizations-sub-second-llm-checklist]]
- [[speculative-decoding-history-roofline-shreybirmiwal]]
- [[kv-caching-llms-clearly-explained-avichawla]]
