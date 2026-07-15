---
type: bookmark
description: "Deel COO Dan Westgarth: self-improving software via closed bug loop — Bug Hunter on customer-account replicas + multimodal Deel Code with Playwright browser verification; human approves every PR."
tags: ["agents", "loop-engineering", "verification", "self-improvement", "multi-agent", "playwright", "testing", "enterprise", "agent-harness", "human-in-the-loop", "deel"]
source: https://x.com/danwestgarth/status/2077346634275430478
date: 2026-07-15
author: danwestgarth
summary: "Deel COO Dan Westgarth: self-improving software via closed bug loop — Bug Hunter on customer-account replicas + multimodal Deel Code with Playwright browser verification; human approves every PR."
raw: "[[raw/danwestgarth_2077346634275430478]]"
---

# Building a Self-Improving, AI-Native Company

**Dan Westgarth** (@DanWestgarth), COO at **Deel**, on turning bug fixing into a closed adaptive loop — not “AI that makes ticket queue faster,” but software that **observes → detects → repairs → verifies** with humans only at final ship judgment.

## Thesis

A self-improving company needs self-improving software: recursive loops that learn from real outcomes with little human intervention. Most workplace AI bolts a faster engine onto existing human workflows. Deel’s first closed loop is production bugs.

## Old loop vs new loop

| | Traditional | Deel agents |
|--|-------------|-------------|
| Who notices first | Customer | Bug Hunter (continuous) |
| Where correction lives | People outside software | System interior + human gate |
| Environment | Eng test setups | Isolated **replicas of real customer accounts** |

**Long tail:** failures from role × dataset × integration × legacy workflow combinations that static deterministic tests never enumerate.

## Agent 1: Bug Hunter

- Continuously navigates product like a user on **safe account replicas** (aggressive exploration without touching live users).
- Signals: console errors, failed network requests, broken UI, dead interactions.
- **Rerun to confirm** (filter flakiness / model false positives).
- **Deduplicate** across hundreds of accounts → one ticket with blast-radius context.

## Agent 2: Deel Code

- Multimodal intake: ticket text + screenshots + Loom/video reconstruction (separate sub-agents).
- **Narrow scopes only** — image analyzer describes what it sees; don’t let one agent both “look” and implement (early failure: edited unrelated files).
- Pipeline: requirements analysis → repo navigation → implementation → open PR (each agent minimal context).

### Verification lesson (“the moment that broke agents”)

A fix passed tests, looked good in review, merged — still broke UI (dropdown closed everything). **Diff correctness ≠ behavior correctness.**

**Fix:** put a browser in the loop — after code change, **Playwright on preview** reproduces original issue and checks symptom gone. Only browser-verified PRs reach humans.

## Human role

Engineers move to **end of loop**: is this right, should it ship? Nothing merges without human sign-off. Agents propose; people approve the high-stakes judgment.

## Closed-loop systems

Pattern: observe self against real-world environments → detect mismatch → attempt correction → verify → repeat (including overnight). Software shifts from systems that only **execute** to systems that **adapt**. Bug fixing is first instance of a broader pattern.

## Why it matters

Concrete enterprise case of production **observe–verify loops** with customer-replica exploration, multimodal diagnosis, and **browser-as-oracle** — maps cleanly to loop-engineering / verification vault cluster (not just coding-assistant demos).

## Related

- [[continual-learning-replit-agent-vibench]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[software-factory-linear-claude-cloud-routines]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[fable-5-self-improving-system-14-steps]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[human-in-the-loop-agent-loops]]
- [[ai-native-engineering-org]]
- [[loop-engineering-technical-roadmap-h100envy]]
