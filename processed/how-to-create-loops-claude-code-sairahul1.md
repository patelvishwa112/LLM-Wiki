---
tags:
  - claude-code
  - loop-engineering
  - agents
  - agent-harness
  - productivity
  - verification
  - automation
source: https://x.com/sairahul1/status/2074063593759227938
date: 2026-07-06
type: bookmark
description: "Rahul (@sairahul1) on persistent Claude loops — six parts, four-file TASK/LOOP_INSTRUCTIONS/PROGRESS/outputs, verification, /loop vs /goal, permission ladder."
author: sairahul1
summary: "Rahul (@sairahul1) on persistent Claude loops — six parts, four-file TASK/LOOP_INSTRUCTIONS/PROGRESS/outputs, verification, /loop vs /goal, permission ladder."
raw: "[[raw/sairahul1_2074063593759227938]]"
---

# How to Create Loops with Claude Code

Rahul (@sairahul1) argues most Claude use is still **one-shot**: prompt, answer, session ends, context rebuilt tomorrow. For daily reviews, CI triage, monitoring, and follow-ups, the better abstraction is a **loop** — a repeatable structure around the model, not “ask again.”

## Six parts of a working loop

1. **Trigger** — manual, schedule, file change, CI event  
2. **Context** — task definition, prior progress, instructions  
3. **Action** — report, draft fix, classify, update docs  
4. **Verification** — checklist, tests, safety boundaries (separate verifier pass)  
5. **State update** — persist memory for the next run  
6. **Decision** — stop, repeat, or escalate to human  

Skipping verification, state, or stop conditions produces loops that trust themselves or never finish.

## Four-file minimal harness

```
my-loop/
├── TASK.md              # goal, scope, explicit "do not" rules
├── LOOP_INSTRUCTIONS.md  # procedure, verification, failure policy
├── PROGRESS.md          # memory — blockers, Do Not Repeat, Needs Human Review
└── outputs/             # inspectable artifacts only
```

State lives **outside the chat** so the next run continues rather than restarts.

## Operating advice

- Run **3–5 manual iterations** before `/loop` scheduling in Claude Code.  
- **Worker then verifier** — “looks good” is not verification; check named conditions.  
- **`/loop`** = time-based repeat; **`/goal`** = run until completion conditions hold.  
- **Permission ladder** — start Level 1–2 (read / draft to `outputs/`); expand tools only after stable runs.  
- Common failures: schedule too early, no state, no verification, no failure policy, too many tools too soon.

## Why it matters

Shifts leverage from **writing better prompts** to **designing systems that keep working** — aligned with harness engineering and loop taxonomy notes elsewhere in the vault, but grounded in copy-paste templates for Claude Code/Desktop.

## Related

- [[harness-engineering-2026-discipline]]
- [[wtf-is-a-loop]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[learn-harness-engineering]]
- [[continual-learning-replit-agent-vibench]]