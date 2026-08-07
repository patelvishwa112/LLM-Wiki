---
tags: ["graph-engineering", "loop-engineering", "claude-code", "agents", "multi-agent", "dynamic-workflows", "verification", "parallelism", "agent-harness", "harness-engineering", "cost-optimization", "subagents"]
source: https://x.com/mojeskoqq/status/2085035505662439707
date: 2026-08-05
type: bookmark
description: "Claude Code dynamic workflows (ultracode work plans) as graph engineering — fake edges, parallel helpers, independent checkers; five copyable prompts + Bun ceiling."
author: mojeskoqq
summary: "Claude Code dynamic workflows (ultracode work plans) as graph engineering — fake edges, parallel helpers, independent checkers; five copyable prompts + Bun ceiling."
raw: "[[raw/mojeskoqq_2085035505662439707]]"
---

# Graph Engineering: 16 AIs, minutes not hours (@mojeskoqq)

## Key takeaways

**Graph engineering** = choose the **shape** of multi-step work before handing it to AI: what must be ordered vs what can run in parallel. Claude Code **dynamic workflows** (“work plans”) implement that shape: many small helpers + independent checkers + one merge job.

Supermarket analogy: one register (serial prompt chain) vs open every register for independent customers.

### Nodes, edges, thumb test

- **Node** = one job, one helper, one input/output  
- **Edge** = real dependency only when the next step **needs** the prior result  
- At every “and then”: *Does the next step need the previous result?* Cover prior step with a thumb — if next can still start, the arrow is **fake** (waste).

### Loop vs graph

| | Loop | Graph |
|---|------|--------|
| Shape | One agent iterates | Many workers side-by-side + separate checkers |
| Wins | Cost, mid-run steering | Wall-clock width, clean per-helper memory, **independent verification**, jobs that don’t fit one context |
| Loses | Width | Cost; no mid-run Q&A; auto-approved file edits |

**Width, not brains.** Sixteen helpers find more; they do not think better. A plan you never needed is pure bill.

### Claude Code setup (as of article)

- Version **≥ 2.1.160** (trigger **`ultracode`**; plain language also works)  
- Paid plan; Pro: `/config` → Dynamic workflows on  
- `/config workflowSizeGuideline=large` for big prompts (default medium ~&lt;15)  
- Keyword does **not** fire from cron/API/PR comments — interactive only  
- First run: small slice (e.g. ≤12 files), **separate branch**  
- `/workflows`: p pause, x stop, r restart helper, **s save** as `/name`  
- Helpers **always auto-approve file edits** inside a plan — “change nothing” is a request; real guard = branch/worktree  
- Model inherits session model (Opus default post-2.1.219)

### Five prompt shapes (Part 6)

1. **Full sweep + 3 skeptics** — map ≤40 files → 1 agent/file → ordered kill rules (UNREACHABLE/HANDLED beats vote); confirm only with **literal trigger input**  
2. **Four-lens review** — correctness / security / performance / blast-radius (+ judge); fix merge-base; drop findings without concrete failure  
3. **Mechanical migrate N files** — few worktrees not one-per-file; baseline tests before edit; ban destructive git  
4. **Iterative bug hunt** — rounds until two empty rounds  
5. **Non-code research** — parallel angles + source-checked claims  

Common shape: **fan-out → independent checker who did not do the work → single merge**.

### Failure modes & Bun case

Self-review weak; helpers collide on same files; cost; **reader overload**. Jarred Sumner Bun rewrite: extreme width/cost; ceiling is **how much a human can review** (Kelley / Hashimoto / Willison thread).

### When not to graph

Small tasks; need step-by-step control; still discovering the problem; true serial dependencies. Prefer a **loop**.

### Closing line

> Someone writing prompts asks a question. Someone doing graph engineering decides the shape of the answer.

## Why it matters

Best practitioner field guide in the vault for Claude Code dynamic workflows: pairs conceptual fake-edges / three-commitments essays with **runnable** ultracode prompts, cost/ops controls (`/workflows`, s-save), and honest “when not.”

## Related

- [[claude-code-dynamic-workflows-intro]]
- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[graph-engineering-dynamic-workflows-fleet-0xcodila]]
- [[graph-engineering-fake-edges-diamond-anatolikopadze]]
- [[graph-engineering-substance-over-meme-akshay]]
- [[graph-engineering-three-commitments-cyrilxbt]]
- [[master-agent-architecture-harness-loop-graph-marfin]]
- [[three-layers-harness-loop-graph-lunarresearcher]]
- [[loop-graph-harness-pipeline-archiveexplorer]]
- [[wtf-is-a-loop]]

## Source

https://x.com/mojeskoqq/status/2085035505662439707
