---
tags: [multi-agent, agents, self-improving, loops, kimi, agent-swarm, verification, skills, agent-architecture]
source: https://x.com/0xMovez/status/2067291911468044494
type: bookmark
ingested: 2026-06-17
---

# The Self-Improving Loop: 300-Agent Swarm on Kimi

**Source:** [X Post by @0xMovez](https://x.com/0xMovez/status/2067291911468044494)

## Summary
Detailed playbook for building a compounding self-improving agent system using Kimi's 300-agent swarm capability (K2.6). The approach combines massive parallel agent execution (up to 300 agents, 4000 steps) with a verification gate (Opus 4.8) and persistent "Skills" that capture workflows for reuse. Key innovation is the "loop + dreaming" pattern where each run not only completes the task but improves the system for future runs through saved skills, constraints, and distilled lessons.

## Why It Matters
This represents a shift from one-shot prompting or static workflows (e.g., LangGraph DAGs that don't improve) to truly compounding agent systems. By treating the swarm as a contractor with detailed specs, demanding file outputs, using an external verifier to filter garbage, and explicitly saving reusable Skills + constraints, the system gets meaningfully better over time (run #50 >> run #1). Cost collapses dramatically on replays. Aligns with broader 2026 trends in agent harnesses, persistent loops, and self-improving architectures seen across Claude Code ecosystems.

## Key Concepts
- **Spec over Prompt**: Detailed specs seed reusable skills
- **Wasteful Parallelism**: 300 bounded-context agents beats single long-context
- **Verify Gate**: Opus 4.8 as honest refuter before saving skills
- **Skill Distillation**: Capture full workflow (input/output format, steps) for 30s replays
- **Constraints Evolution**: Turn verifier feedback into permanent project rules
- **Background Promotion**: Turn stable loops into proactive scheduled agents

## Related
- [[multi-agent-systems]]
- [[agent-skills]]
- [[self-improving-agents]]
- [[agent-loops]]
- [[kimi-ai]]
- [[verification-gates]]

## Tags
multi-agent, agents, self-improving, loops, kimi, agent-swarm, verification, skills, agent-architecture