---
title: "Hermes /goal — How to Turn a Chat Message Into a Standing Job"
tags: ["hermes", "goal", "productivity", "agents", "workflows", "autonomy"]
source: https://x.com/zaimiri/status/2061745669077926042
date: 2026-06-02
published: 2026-06-02
authors: ["zaimiri (@zaimiri)"]
type: bookmark
raw: "[[raw/zaimiri_2061745669077926042]]"
related: ["[[dynamic-workflows-where-plan-lives]]", "[[agent-memory-landscape-2026]]"]
---

# Hermes /goal — Standing Jobs Instead of Disposable Prompts

Zaimiri's practical guide to Hermes /goal mode. The core insight: /goal turns a chat message into a standing job with a control loop (goal → work → judge → continue → verify → stop).

## Key Takeaways

- **/goal changes the rhythm.** Normal chat: prompt → response → prompt → response → maybe done. /goal: define finish line once → autonomous work loop → judged continuation → verified result. You stop babysitting every turn and start assigning work.
- **It's a control loop, not magic.** A lightweight judge checks after each turn whether the goal is actually satisfied. Five stop conditions: achieved, paused, cleared, user interrupt, turn budget (default 20). `/goal resume` resets the counter.
- **The six-piece goal pattern.** Job + allowed scope + sources to inspect + done criteria + checks to run + final reporting format. If you can't describe "done," don't use /goal yet — make the task smaller first.
- **/subgoal is underrated.** Add criteria mid-run without restarting. Hermes persists subgoals with the goal; the judge considers all of them.
- **Verification must be external.** "Do not make the agent's self-report the proof. Make the proof something Hermes can inspect." Best goals include explicit checks: "verify the test passes," "confirm the file was pushed."
- **Signal/Telegram makes it a pocket operator.** Send a goal from your phone, let Hermes work in background, check back when done. The machine still has all tools — you just don't sit in front of it.
- **Good for:** 3+ back-and-forth tasks. **Bad for:** one-offs, taste-call-heavy work, sensitive actions without approval boundaries, tasks where "done" can't be described.

## The Six-Piece Goal Pattern

```
/goal
Task: [what to do]
Sources: [what to read/inspect]
Voice: [style constraints]
Constraints: [what NOT to do — no publish, no schedule, etc.]
Verification: [checks to run — lint, tests, file exists, etc.]
Done means: [concrete finish line]
Final reply: [reporting format]
```

## Command Reference

| Command | Purpose |
|---------|---------|
| `/goal <desc>` | Set a standing goal |
| `/goal status` | Check current state |
| `/goal pause` | Pause the loop |
| `/goal resume` | Resume with reset turn counter |
| `/goal clear` | Remove the contract |
| `/subgoal <criteria>` | Add requirements mid-run |

## Where /goal Shines vs Fails

**Use for:** fix test suites, clean doc folders, inspect repos + write plans, research passes with sourced briefs, migrate prompts into skills, debug tools until commands work, draft → lint → revise → route pipelines.

**Skip for:** one-off questions, tiny edits, tasks needing taste calls every 2 minutes, sensitive actions without approval gates, tasks where done can't be described.
