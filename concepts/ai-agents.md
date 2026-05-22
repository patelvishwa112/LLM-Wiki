---
title: AI Agents
created: 2026-05-22
updated: 2026-05-22
type: concept
tags: [agents, engineering]
sources: [raw/articles/anthropic-engineering-building-effective-agents.md, raw/articles/anthropic-research-building-effective-agents.md, raw/articles/anthropic-engineering-multi-agent-research-system.md, raw/articles/anthropic-engineering-writing-tools-for-agents.md, raw/articles/anthropic-engineering-equipping-agents-for-the-real-world-with-agent-skills.md, raw/articles/anthropic-engineering-advanced-tool-use.md, raw/articles/anthropic-engineering-claude-think-tool.md, raw/articles/anthropic-engineering-demystifying-evals-for-ai-agents.md]
confidence: high
---

# AI Agents

Anthropic uses "agent" to mean an LLM-driven loop that calls tools, observes
their results, and continues until it has finished a task. The engineering
canon below establishes patterns (orchestrator–worker, augmented LLM, evaluator
loops) and tool-design discipline.

## What the sources say

### Patterns and frameworks
- [[anthropic-engineering-building-effective-agents]] — The canonical
  taxonomy of agent patterns from Anthropic Engineering
- [[anthropic-research-building-effective-agents]] — Research-side companion
- [[anthropic-engineering-multi-agent-research-system]] — Building a
  research-grade multi-agent system at scale

### Tool design
- [[anthropic-engineering-writing-tools-for-agents]] — Designing tools so
  agents actually use them well
- [[anthropic-engineering-advanced-tool-use]] — Advanced tool use on the
  Claude Developer Platform
- [[anthropic-engineering-claude-think-tool]] — The "think" tool: scratch
  space inside the agent loop
- [[anthropic-engineering-equipping-agents-for-the-real-world-with-agent-skills]]
  — Agent Skills primitive
- [[anthropic-engineering-code-execution-with-mcp]] — Using MCP for code
  execution inside agents

### Evaluation
- [[anthropic-engineering-demystifying-evals-for-ai-agents]] — Practical
  agent evaluation

## Misalignment risks

Long-running agents create new failure modes. See [[agentic-misalignment]],
[[deceptive-alignment]], and [[reward-hacking-and-tampering]].

## Related

- [[claude-code]]
- [[model-context-protocol]]
- [[computer-use]]
- [[extended-thinking]]
- [[agentic-misalignment]]
