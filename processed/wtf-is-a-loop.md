---
tags: ["agents", "loops", "claude-code", "orchestration", "agent-harness", "skills"]
source: https://x.com/mvanhorn/status/2063865685558903149
date: 2026-06-08
type: bookmark
author: mvanhorn
title: "WTF Is a Loop? Peter Steinberger vs. Boris Cherny"
summary: "A deep analysis of AI coding loops: what they are, their 5-year lineage from ReAct to orchestration, why the loop (not the model) is now the expensive part, and how skills inside loops create compounding systems."
raw: "[[raw/mvanhorn_2063865685558903149]]"
related: ["[[rlm-structured-outputs]]", "[[4-agent-trading-desk]]"]
---

# WTF Is a Loop?

## Key Takeaways

1. **A loop is cron plus a decision-maker in the body.** The model, not a hardcoded branch, decides the next action each tick. Cron provides scheduling; the agent provides intelligence.

2. **The lineage is real and progressive.** ReAct (2022) → AutoGPT (2023) → Ralph loop (2025) → /goal (spring 2026) → orchestration loops (now). Single-agent ralph is old hat; multi-agent supervision on top is the new layer.

3. **Feedback is the magic, not the loop itself.** A loop that writes, runs, reads the result, and corrects is what actually works. Continuous review/validation gates (like roborev) make loops trustworthy.

4. **The expensive resource shifted from tokens to loop management.** Uber burned its annual AI budget in 4 months. Production needs: max iteration cap, no-progress detection, dollar budget ceiling.

5. **The reusable unit inside a loop is a skill, not a prompt.** Loops calling sharp, named skills compound. Loops that re-derive everything just burn money. Steinberger: "If you do something more than once, turn it into an automated skill."

## Boris Cherny's Three Stages

1. Write code by hand with autocomplete
2. Run 5-10 Claude sessions in parallel, prompt each one
3. Don't prompt at all — write the loops that prompt Claude (259 PRs in 30 days, IDE deleted since Nov 2025)

## Production Hard Stops

Essential guardrails: maximum iteration count, no-progress detection, token/dollar budget ceiling. Without these → infinite loops and billing surprises.

## The Starter On-Ramp

`/loop babysit all my PRs. Auto-fix build issues, and when comments come in, use a worktree agent to fix them.`

## Consciousness of Approach

This connects to the broader agent harness discourse: the move from human-in-the-loop to human-above-the-loop. The engineer's job shifts from writing code to writing the thing that writes the code. The same pattern appears in RLMs (subagent fan-out), trading desks (4-agent pipeline), and CI/CD loops.
