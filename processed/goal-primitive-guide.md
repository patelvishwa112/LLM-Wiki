---
tags: ["agents", "claude-code", "coding-tools", "orchestration"]
source: https://x.com/Saboo_Shubham_/status/2054988166541770782
date: 2026-05-12
type: processed-note
related:
  - "[[coding-agent-harness-eight-pillars]]"
  - "[[iii-agent-harness-workers]]"
  - "[[claude-cowork-60-power-moves]]"
---

# /goal: The Agent Primitive

## Summary
`/goal` is emerging as a primitive for coding agents — as fundamental as HTTP or JSON. Instead of prompting the agent for the next response (you driving), `/goal` flips the model: you define what "done" looks like once, and the agent works toward it autonomously. Three major tools — OpenAI Codex CLI, Anthropic Claude Code, and Hermes Agent — have independently converged on this primitive, making cross-tool composition possible.

## Key Takeaways
- **Primitive, not feature**: `/goal` is becoming as fundamental to coding agents as HTTP is to the web — a building block, not a product feature
- **Shift in control**: From prompting (you driving, one response at a time) to assigning (agent drives toward a defined target)
- **Three-tool convergence**: Codex (implementation), Claude Code (review), Hermes Agent (orchestration) all speak `/goal` — enabling composition across tools
- **Composability**: The convergence matters because it lets you use a builder, reviewer, and orchestrator that all accept the same instruction format

## Connections
- [[coding-agent-harness-eight-pillars]] — the harness architecture that `/goal` fits into as a delegation primitive
- [[iii-agent-harness-workers]] — worker orchestration pattern aligned with `/goal`-style delegation
- [[claude-cowork-60-power-moves]] — Cowork slash commands including `/plan` and related delegation patterns
