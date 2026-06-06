---
title: "Dynamic Workflows — The Plan Moves Out of Chat"
tags: ["claude-code", "workflows", "agents", "subagents", "orchestration", "architecture"]
source: https://x.com/voxyz_ai/status/2061782441606451381
date: 2026-06-02
published: 2026-06-02
authors: ["Vox (@Voxyz_ai)"]
type: bookmark
raw: "[[raw/voxyz_ai_2061782441606451381]]"
related: ["[[opus-48-token-economy-guide]]"]
---

# Claude Code Dynamic Workflows — Vox's 5 Rules

Vox's framework for evaluating Claude Code Dynamic Workflows. Core thesis: the real innovation isn't "hundreds of subagents" — it's that the plan moves out of chat context and into an executable orchestration script.

## Key Takeaways

- **"Where does the plan live?" is the first question.** In chat = thought. In a skill = method. In a workflow script = runtime object. Each step up improves scalability.
- **Not every big task needs a workflow.** Run 5 qualifier questions: Is it parallelizable? Are the steps well-defined? Can it run without human judgment? Is it large enough to justify overhead? Can you scope it precisely?
- **Good workflows are staged pipelines.** The Bun port (750K lines Zig→Rust, 99.8% tests passing, 11 days) was: map lifetimes → write .rs files (2 reviewers each) → fix loop → cleanup pass → PRs. The pipeline shape is more useful than the line count.
- **Approval gates go OUTSIDE the workflow.** Workflows accept no user input while running — only permission prompts can pause them. Where humans judge, split into two workflows with an approval gap.
- **The deliverable is an audit trail.** Not "done" — a structured report with: what was attempted, what succeeded/failed, what decisions were made, what needs human review, and what the next step is.
- **Caps:** 16 concurrent agents, max 1,000 per workflow. Workflow script can't read/write files — agents do. Subagents run in acceptEdits mode (file edits auto-approved). Not durable across sessions.
- **Where to save:** Project-wide: `.claude/workflows/`. Personal: `~/.claude/workflows/`. One-off: keep the report, discard the script.

## The Plan Ladder

| Where | What It Is | Scale |
|-------|-----------|-------|
| Chat context | A thought | Single task |
| AGENTS.md | A working contract | Project norms |
| PLANS.md | A long-task roadmap | Multi-turn project |
| Skill SKILL.md | A reusable method | Recurring task type |
| Workflow script | An executable runtime object | Staged multi-agent pipeline |

## The Bun Pipeline Pattern

1. Map/analyze phase (understand the landscape)
2. Generation phase (produce artifacts, multiple reviewers)
3. Fix loop (build + test until clean)
4. Cleanup pass (remove cruft)
5. Delivery (PRs, reports)

## Workflow Brief Template

Vox provides a copy-paste brief to hand Claude Code when requesting a workflow — the "save-worthy core" of the article.

## Relevance to Hermes

Directly applicable. Hermes's `/goal` mode and `delegate_task` are in the chat-context + skill zone. Dynamic Workflows represents the next rung: moving the plan into an executable script that orchestrates subagents without context pollution. The approval-gate rule (split at human judgment points) applies to any agent orchestration. The audit trail deliverable pattern is worth adopting for Hermes goal execution summaries.

References:
- Anthropic blog: Introducing Dynamic Workflows in Claude Code
- Docs: code.claude.com/docs/en/workflows
- Agents docs: code.claude.com/docs/en/agents
