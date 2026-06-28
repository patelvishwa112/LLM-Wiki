---
title: 'A Harness for Every Task: Dynamic Workflows in Claude Code'
tags:
- claude-code
- agents
- workflows
- multi-agent
- orchestration
- agent-harness
source: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
date: 2026-06-02
published: 2026-06-02
authors:
- Thariq Shihipar
- Sid Bidasaria
type: article
raw: '[[raw/claude-com_dynamic-workflows]]'
description: 'A Harness for Every Task: Dynamic Workflows in Claude Code'
---

# A Harness for Every Task: Dynamic Workflows in Claude Code

## Key Takeaways
- Claude Code can now dynamically author its own multi-agent harness in JavaScript, custom-built per task
- Default single-context harness breaks down on long, parallel, structured, or adversarial tasks due to three failure modes: agentic laziness, self-preferential bias, goal drift
- Workflows solve this by orchestrating separate subagents, each with its own context window and isolated goal
- Six core patterns compose into workflows: classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done
- Trigger word "ultracode" forces workflow mode; save with "s" in workflow menu
- Key capabilities: per-agent model selection, worktree isolation, resume from interruption
- Bun was rewritten from Zig to Rust using this feature
- Caveat: uses significantly more tokens — be intentional about when to use

## Summary

Anthropic released dynamic workflows in Claude Code (June 2026), enabling Claude to write its own harness on the fly. The default harness does planning + execution in a single context window, which works for typical coding but fails on complex tasks through three failure modes: **agentic laziness** (stopping early), **self-preferential bias** (over-trusting its own work), and **goal drift** (losing fidelity across many turns).

Dynamic workflows combat all three by spawning separate subagents, each with isolated context and narrow goals. The workflow is a JavaScript file with special functions for spawning/coordinating subagents, plus standard JS (JSON, Math, Array). Subagents can use different models and run in separate worktrees.

### Six Core Patterns

1. **Classify-and-act** — Route tasks to appropriate agents
2. **Fan-out-and-synthesize** — Parallel execution with barrier merge
3. **Adversarial verification** — One agent produces, another verifies
4. **Generate-and-filter** — Generate then filter/rubric-evaluate
5. **Tournament** — Agents compete, judged pairwise
6. **Loop until done** — Unknown-workload tasks with stop conditions

### Use Cases Beyond Coding

- **Migrations/refactors** — Bun: Zig→Rust rewrite via workflows (subagent per fix, adversarial review, merge)
- **Deep research** — Fan-out web searches, verify claims, synthesize cited report
- **Deep verification** — Per-claim fact checking with source quality verification
- **Sorting at scale** — Pairwise comparison agents for qualitative ranking (1000+ items)
- **Memory/rule adherence** — Verifier per CLAUDE.md rule; reverse: mine sessions for corrections → cluster → verify → distill
- **Root-cause investigation** — Separate evidence agents, hypothesis panel with verifiers
- **Triaging at scale** — Classify, dedupe, fix-or-escalate, with quarantine pattern
- **Exploration and taste** — Generate solutions, review against rubric
- **Evals** — Worktree-isolated agents with comparison/grading
- **Model/intelligence routing** — Classifier researches complexity, routes to Sonnet or Opus

### Tips

- Detailed prompting with named patterns produces best results
- Combine with `/goal` and `/loop` for recurring workflows
- Set token budgets: "use 10k tokens"
- Save workflows to `~/.claude/workflows` or distribute as skills
- Works for non-technical work too — often more useful there
- Quick workflows possible: "quick adversarial review of an assumption"

## Related

- [[Claude Code Best Practices]]
- [[Agent Harness Architecture]]
- [[Agentic Workflow Patterns]]
