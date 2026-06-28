---
tags:
- claude-code
- agent-harness
- skills
- prompt-engineering
- agent-ops
source: https://x.com/mikenevermiss/status/2068197417506222428
type: bookmark
related:
- - hermes-agent-skill-authoring
- - writing-plans
- - iii-agent-harness-workers
- - agent-harness-engineering-claude-14-step-roadmap
summary: '"@mikenevermiss proposes an expanded 12-rule CLAUDE.md template for Claude
  Code (building on the original 4 rules from Karpathy/Forrest). Addresses modern
  multi-agent setups, hooks, skill libraries, and long-running workflows. Includes
  a clean, concise full template and claims it drops unsupervised error rates to ~3%.
  Key additions: hard token budgets, git worktrees for agents, PROGRESS.md checkpoints,
  separate research/implementation sessions, scoped hooks, and unique skill descriptions."

  '
why_it_matters: '"Directly relevant to the vault''s own CLAUDE.md conventions and
  the hermes-agent-skill-authoring skill. The 12 rules provide a battle-tested pattern
  for reliable agent behavior in complex projects. Strong emphasis on verifiability,
  cost control, isolation, and explicit failure modes aligns with production agent-harness
  design. The template is short enough for high compliance."

  '
description: '"@mikenevermiss proposes an expanded 12-rule CLAUDE.md template for
  Claude Code (building on the original 4 rules from Karpathy/Forrest). Addresses
  modern multi-agent setups, hooks, skill libraries, and long-running workflows. Includes
  a clean, concise full template and claims it drops unsupervised error rates to ~3%.
  Key additions: hard token budgets, git worktrees for agents, PROGRESS.md checkpoints,
  separate research/implementation sessions, scoped hooks, and unique skill descriptions."'
---

# Updated CLAUDE.md Pattern for Claude Code (12 Rules)

**Source:** [X Post by mikenevermiss](https://x.com/mikenevermiss/status/2068197417506222428)

This post provides an updated, production-grade **CLAUDE.md** template that expands the original 4 rules to **12 rules** to handle the realities of 2026 Claude Code usage (multi-agent workflows, hooks, skill libraries, long-running tasks).

## Original 4 Rules (Karpathy / Forrest Chang)
1. Think Before Coding
2. Simplicity First
3. Surgical Changes
4. Goal-Driven Execution

These reduced error rates significantly in early 2026 but left ~60% of failure modes unaddressed as the ecosystem matured.

## The 8 New Rules (2026 Edition)
5. **No Model Calls for Deterministic Decisions** — Routing, retry logic, thresholds, and binary decisions belong in code, not the LLM.
6. **Hard Token Budgets** — Every session must have a strict token limit. Hit it → summarize to file and stop.
7. **One Agent, One Directory** — Use git worktrees. Never let two agents share a working directory.
8. **Checkpoint Multi-Step Work** — For tasks >3 steps, maintain a `PROGRESS.md` after each step.
9. **Fail Loudly** — Never paper over errors or accept tests that don't actually verify the intended behavior.
10. **Unique Skill Descriptions** — Skill descriptions must be mutually exclusive so the dispatcher doesn't load the wrong one.
11. **Research and Implementation Are Separate Sessions** — Use a researcher subagent, then start a clean session for the writer/implementer.
12. **Scoped Hooks Only** — Every hook must have explicit conditions (directory, file type, session event). No unconditional hooks on every tool call.

## Full Recommended CLAUDE.md Template
The post provides a clean, concise template (under ~100 lines for high compliance):

```markdown
# CLAUDE.md
## Project
[one sentence: what this codebase does and what tech stack it uses]

## Behavioral Rules
### Think Before Coding
state your assumptions before writing code. surface tradeoffs. ask before guessing on anything that affects architecture or data. push back when a simpler approach exists.

### Simplicity First
write the minimum code that solves the problem. no speculative features. no abstractions for single-use code. if a senior engineer would call it overcomplicated, simplify.

### Surgical Changes
touch only what the task requires. do not improve adjacent code, formatting, comments, or naming that was not part of the ask. match existing code style exactly.

### Goal-Driven Execution
define what success looks like before starting. loop until that definition is met and verified. do not ask for step-by-step instructions. figure out the path.

### No Model Calls for Deterministic Decisions
routing, retry logic, status-based branching, and threshold decisions belong in code, not LLM calls. if a rule can be written, write it.

### Hard Token Budgets
every session has a hard token limit: [set your number, e.g., 50,000 tokens]. if the limit is reached without a verified solution, write findings to a file and stop. do not continue past budget.

### One Agent, One Directory
agents running in parallel work in separate git worktrees. no two agents share a directory. if you need a second agent, run: git worktree add ../agent-2 [branch-name]

### Checkpoint Multi-Step Work
for any task longer than three steps, create PROGRESS.md in the working directory. write to it after each step: what was done, what was found, what comes next, what is blocked. if the session ends before completion, the next session reads PROGRESS.md first.

### Fail Loudly
if a step fails, stop and report the failure with specifics before continuing. if a test passes but does not cover the actual behavior, say so. success means verifiable, not reported.

### Unique Skill Descriptions
each skill covers exactly one job. its description cannot apply to any other skill in the project. if two skills overlap in description, rename before deploying.

### Research and Implementation Are Separate Sessions
use a subagent for any task that requires reading more than five files or querying more than two sources. get a structured report. start a clean session for implementation with only that report as input.

### Scoped Hooks Only
every hook has an explicit condition: file extension, directory path, or session event. no hook runs unconditionally on every tool call. batch logging to session end where possible.

## What Not to Touch
[list directories or files claude should never modify: e.g., /secrets, /migrations/archive, /prod-config]

## Success Criteria Default
when in doubt about whether a task is done: does the test pass, does the build succeed, and is the output verifiable by something other than claude's own judgment? if no to any of those, it is not done.
```

## Impact
The post claims this drops unsupervised error rates from ~41% (no CLAUDE.md) → ~11% (original 4 rules) → ~3% (full 12 rules).

## Relevance to Vault
- Directly informs the vault's own CLAUDE.md and the hermes-agent-skill-authoring skill
- Strong patterns for agent isolation (worktrees), cost control (token budgets), verifiability, and explicit failure handling
- Complements [[hermes-agent-skill-authoring]], [[writing-plans]], [[iii-agent-harness-workers]], and [[agent-harness-engineering-claude-14-step-roadmap]]

**Related:** claude-code, agent-harness, skills files, prompt engineering, agent safety.