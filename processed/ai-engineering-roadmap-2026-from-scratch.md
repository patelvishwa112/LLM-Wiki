---
title: "The 2026 AI Engineering Roadmap — Build It From Scratch, Ship the Tool"
tags: ["ai-engineering", "roadmap", "2026", "training", "inference", "agents", "agent-harness", "skills", "mcp", "safety", "infrastructure", "serving", "transformer", "kv-cache", "fundamentals", "from-scratch", "courses", "open-source", "rag", "multimodal", "alignment"]
source: https://x.com/ghumare64/status/2063574610889560271
date: 2026-06-07
published: 2026-06-07
authors: ["Rohit Ghumare (@ghumare64)"]
type: bookmark
raw: "[[raw/ghumare64_2063574610889560271]]"
related: ["[[agent-harness-engineering-agentforge]]", "[[harness-engineering-2026-discipline]]", "[[rlhf-from-first-principles]]", "[[how-gpu-executes-code-first-principles]]", "[[what-is-kv-cache-llms]]", "[[mcp-core-architecture-explained]]"]
summary: "Rohit Ghumare's 12-layer AI engineering roadmap for 2026, built around his open-source course (503 lessons). Method: build every algorithm from raw math, then ship a reusable SKILL.md artifact. Covers math → deep learning → transformers → LLMs → RAG → multimodal → MCP/A2A → agents → autonomous systems → infrastructure → safety → capstones."
---

# The 2026 AI Engineering Roadmap — Build It From Scratch, Ship the Tool

Rohit Ghumare's 12-layer roadmap for AI engineering in 2026, structured around his open-source course `ai-engineering-from-scratch` (503 lessons, MIT licensed).

## Core Thesis

In 2023, an "AI engineer" wired an API key to a prompt template. By 2026, the model IS the product surface. The highest-paid engineers move from matrix multiply to autoscaling serving fleet without flinching.

The gap that matters: knowing the slogan ("prefill is compute-bound, decode is memory-bound") vs. knowing the mechanism (which matmuls dominate, why decode waits on HBM bandwidth, what sits in KV cache and why it grows linearly). Most courses give you a vibe. This one gives you a mechanism.

## The Method: Build It, Then Ship It

Every one of 503 lessons follows:

1. **BUILD IT:** Write the algorithm from raw math. Backprop. Tokenizer. Attention. Agent loop. No framework, no `pip install` doing the interesting part. Then run the same thing through the production library to see what it hid.
2. **SHIP IT:** Every lesson ends in a reusable artifact — a prompt, skill, agent, or MCP server in `outputs/`. Not throwaway homework. A real tool that drops into Claude, Cursor, Codex, OpenClaw, or Hermes as SKILL.md.

~500 skills ship across the curriculum: `prompt-loss-function-selector`, `skill-tokenizer`, `skill-inference-optimizer`, `skill-agent-loop`, `skill-mcp-auth`, `skill-vllm-scheduler-reader`, etc.

Two meta-skills: `/find-your-level` (placement quiz → personalized path) and `/check-understanding <phase>` (quiz per phase → exact lessons to review).

## The 12 Layers

### Layer 1: Math You Actually Use
Linear algebra, gradients, probability, automatic differentiation. Build a tiny autodiff engine. **Artifact:** Chain rule & autodiff.

### Layer 2: Deep Learning Core
Backprop through MLP by hand. Vanishing gradients, dead ReLUs, init, residual connections become diagnosis tools. **Artifacts:** `prompt-loss-function-selector`, `prompt-loss-debugger`.

### Layer 3: Transformers & KV Cache
Attention from scratch: matmul → softmax → matmul. Build KV cache to see the formula: `2 × batch × n_kv_heads × seq_len × d_head × dtype_bytes`. GQA shrinks n_kv_heads. FlashAttention tiles the score matrix. **Artifact:** `skill-inference-optimizer`.

### Layer 4: End-to-End LLM (~500 lines PyTorch)
BPE tokenizer → decoder-only GPT → pretraining loop → SFT + DPO. Watch loss curves, see vocabulary size effects on cost. **Artifacts:** `skill-tokenizer`, `prompt-tokenizer-analyzer`.

### Layer 5: LLM Engineering
Context engineering as token budget allocation. RAG: recall, reranking, faithfulness. **Artifacts:** `skill-advanced-rag`, `prompt-advanced-rag-debugger`.

### Layer 6: Multimodal
Image → patches → embeddings → tokens alongside text. CLIP contrastive objective. Q-Former and gated cross-attention for modality fusion. **Build:** CLIP from scratch.

### Layer 7: Tools & Protocols (2026 Inflection Point)
MCP for tool discovery, A2A for agent-to-agent communication. November 2025 MCP auth spec: Client ID Metadata Documents, audience-pinned tokens, JWKS refresh-not-rotate. **Artifact:** `skill-mcp-auth`.

### Layer 8: Agent & Harness Engineering
Agent loop (~120 lines Python): plan → act → observe → verify → repeat. Verification gates + observation budget = survives long tasks. Virtual context / MemGPT for memory. **Artifact:** `skill-agent-loop`.

### Layer 9: Autonomous Systems
Long-horizon agents, self-improvement loops, guardrails. METR frames capability as task length — how long before coherence falls apart. **Build:** Long-horizon agents.

### Layer 10: Infrastructure & Production
Speculative decoding (draft model → target verifies, EAGLE-3 acceptance rates). Prefill/decode disaggregation (separate hardware for compute-bound vs bandwidth-bound phases). **Artifact:** `skill-vllm-scheduler-reader`.

### Layer 11: Safety & Alignment
Reward hacking/Goodhart, sycophancy as measurable RLHF side effect, deceptive alignment experiments, Constitutional AI / RLAIF as mitigation. **Build:** Constitutional AI / RLAIF.

### Layer 12: Capstones
Terminal-native coding agent, production RAG chatbot, speculative-decoding inference server, MCP server with registry + governance. Portfolio-grade, every layer connected.

## The Bet

Frameworks churn. What doesn't: attention is still matmul+softmax, KV cache still grows the same way, gradients still flow backward like 1986. Learn mechanics once → every new framework is a thin shell.

**Course:** https://github.com/rohitg00/ai-engineering-from-scratch (MIT)
**Site:** https://aiengineeringfromscratch.com
**Install:** `npx skills add rohitg00/ai-engineering-from-scratch`
