---
tags:
- ai-engineering
- roadmap
- transformers
- agents
- mcp
- infrastructure
- safety
- curriculum
source: https://x.com/ghumare64/status/2063574610889560271
date: 2026-06-07
type: bookmark
author: ghumare64
summary: '12-layer 2026 AI Engineering roadmap: build from scratch (math → backprop
  → transformers + KV cache → full LLM + DPO → RAG → multimodal → MCP/A2A → agent
  loops → long-horizon agents → vLLM/serving → Constitutional AI) and ship reusable
  skills/artifacts at every layer. Designed to close the gap between slogan-level
  knowledge and mechanism-level understanding.'
raw: '[[raw/ghumare64_2063574610889560271]]'
description: '12-layer 2026 AI Engineering roadmap: build from scratch (math → backprop
  → transformers + KV cache → full LLM + DPO → RAG → multimodal → MCP/A2A → agent
  loops → long-horizon agents → vLLM/serving → Constitutional AI) and ship reusable
  skills/artifacts at every layer. Designed to close the gap between slogan-level
  knowledge and mechanism-level understanding.'
---

# The 2026 AI Engineering Roadmap

Rohit Ghumare's curriculum for engineers who need to move fluidly from matrix multiplies to autoscaling fleets.

## The Method
- **Build it first**: Write the algorithm from raw math (no frameworks).
- **Then ship the tool**: Every lesson ends in a reusable SKILL.md artifact (prompts, skills, agents, MCP servers) that installs directly into Hermes, Claude Code, Cursor, etc.

## 12 Layers
1. Math you actually use (linear algebra, gradients, autodiff)
2. Deep learning core (backprop through MLP by hand)
3. Transformer + KV cache + FlashAttention
4. LLM end-to-end (tokenizer → pretrain → SFT → DPO)
5. LLM engineering (context engineering, advanced RAG)
6. Multimodal (CLIP, Q-Former, gated cross-attention)
7. Tools & protocols (MCP fundamentals + auth, A2A)
8. Agent & harness engineering (agent loop, memory, virtual context)
9. Autonomous systems (long-horizon agents)
10. Infrastructure (vLLM internals, speculative decoding, prefill/decode disaggregation)
11. Safety & alignment (reward hacking, Constitutional AI / RLAIF)
12. Capstones (full systems: coding agent, production RAG, MCP server with governance)

## Why It Matters
The edge in 2026 is moving up and down the stack without flinching. This curriculum turns slogans into mechanisms you can debug at 2 a.m.

Directly relevant to Hermes skill authoring, agent engineering, and the full AI engineering stack.