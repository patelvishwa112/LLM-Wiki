---
tags: ["agent-harness", "agents", "harness-engineering", "deepseek", "observability", "loop-engineering", "context-management", "coding-tools", "open-source", "production"]
source: https://x.com/saboo_shubham_/status/2089177978265870817
date: 2026-08
type: bookmark
description: "Five portable harness patterns from DeepSeek open-source agent (dsh): event-log context, loop reminders, truncation honesty, permissioned code-mode, workspace restarts."
author: saboo_shubham_
summary: "Five portable harness patterns from DeepSeek open-source agent (dsh): event-log context, loop reminders, truncation honesty, permissioned code-mode, workspace restarts."
raw: "[[raw/saboo_shubham_2089177978265870817]]"
---

# 5 patterns from DeepSeek’s open-source agent harness

@Saboo_Shubham_ weekend read of DeepSeek’s open agent harness (claimed fastest GH repo to 100k★ / 48h). Patterns portable — no need to switch stacks. Try: `npx @deepseek-ai/dsh web`.

## 1. Derive model context from an append-only log

**Problem:** messages array + separate telemetry drift → debug from a false history.

**Pattern:** Session = event log. Every LLM request is **recomputed** from the log. Architecture rule: anything in a model request must be reconstructable; new model-facing data = new event type first.

**Check:** Outgoing request compared field-by-field to fresh derivation (messages, system, tools, temperature…) → **log-reconstruction desync** on mismatch.

Trace UI is free: trajectory is the log, not extra instrumentation.

**Port:** Append event first → build request from append → equality check in dev (~20 lines).

## 2. Break loops with escalating reminders, not hard blocks

Hard-block kills legitimate retries; ignore burns tokens.

**Pattern:** Count consecutive same-tool + identical args (order-insensitive). At 3 / 5 / 8 inject firmer context reminders (re-read last result, change approach, wrap up). **Never block** — model keeps final say.

Details: unrelated small calls (e.g. todo) don’t reset; **denied** calls count; **per-agent** counters (subagent loops don’t warn parent).

Portable via tool-watch hooks (e.g. Claude Code).

## 3. Tell the model what it didn’t see

Truncated search that doesn’t say so → model believes the world is 100 files.

**Pattern:** Cap with **project-wide sample**, not first-N alpha; mark cut; save full list to file + path. Policy denials: explicit “policy denial, not a bug — do not retry another way.”

**Audit:** Disclose cuts? Reach residual? Errors say if retry helps?

## 4. Code-mode that can’t dodge permissions

`run_code` / program-of-tools pattern for N tool calls per turn + summary-only context.

**Pattern:** Every in-program tool call still hits full permission pipeline, individual logs, denied → **catchable error** (not hang/null).

Evaluating frameworks: check permission path first.

## 5. Kill the context, keep the workspace

Long runs: context becomes the bug.

**Pattern:** Fixed objective in **rounds**; each round = new agent, **zero** chat history. Shared workspace files + structured handoff only: **status, summary, evidence, next steps, blocker**.

Rules: can’t self-block before ≥3 rounds; only human creates/changes objective.

**Port:** Handoff schema + size cap; decide file-state vs context-death before overnight runs.

## Extras

Trajectory: per-call tokens, TTFT vs decode; session zip export of raw events. UI via YAML row patches (`cordis.patch.yml`).

## Why it matters

Concrete harness engineering checklist: single source of truth for context, soft anti-loop, honest tools, permissioned code-mode, structured multi-round restarts. Aligns with observability, loop engineering, and production agent notes.

## Skeptical read

Star-count claim + Awesome LLM Apps CTA. Patterns are the value; verify against current dsh source (fast-moving).

## Related

- [[agent-harness-engineering-agentforge]]
- [[agent-harness-should-repair-itself]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[three-layers-harness-loop-graph-lunarresearcher]]
- [[aftermarket-harnesses-ttunguz]]
- [[shepherd-reversible-execution-traces-avichawla]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[eval-engineering-merge-gate-hanakoxbt]]
