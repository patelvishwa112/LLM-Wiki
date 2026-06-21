---
tags: [claude-code, agent-loops, loops, agent-harness, verification, agent-ops, multi-agent, goal-execution]
source: https://x.com/mvanhorn/status/2068426104088748331
type: bookmark
ingested: 2026-06-21
related: [[guide-to-goal-codex], [self-improvement-loop-for-skills-zach-lloyd], [coding-agent-harness-eight-pillars]]
---

# WTF Is a Loop? Part 2: The 15 Loops People Are Actually Running

**Source:** [Matt Van Horn on X](https://x.com/mvanhorn/status/2068426104088748331)

**Summary:**  
A practical field guide to "Loop Engineering" — the real patterns people are using with Claude Code, Codex, and similar agentic coding tools. The post distinguishes `/goal`, `/loop`, and `/schedule` commands and catalogs 15 production-grade loops extracted from community usage across X, Reddit, GitHub, and YouTube. Emphasis on verification, budgets, anti-spin guards, and human-in-the-loop patterns.

**Why it matters:**  
This post codifies the emerging discipline of turning one-off agent interactions into reliable, long-running autonomous systems. The core insight — "write the loop, not the code" — directly supports the vault's focus on agent-harness engineering and self-improving systems. The listed loops (build-test-fix pairs, verifier loops, adversarial review, completion contracts) are immediately actionable patterns that compound productivity when combined with proper verification and cost controls. It bridges the gap between experimental prompting and production agent operations.

**Key Patterns Extracted:**
- Build-test-fix pair loops
- Independent verifier + advanced model patterns (Boris Cherny style)
- Time-boxed maintainer loops (5-minute repo upkeep)
- Anti-spin safeguards and budget enforcement
- Human approval queues and adversarial review (Clodex)
- "Write loops not code" philosophy

**Commands Clarified:**
- `/goal` for verifiable outcome loops
- `/loop <interval>` for session-bound recurring tasks
- `/schedule` for cloud/offline routines

**Related Concepts in Vault:**
- Goal execution and meta-skills
- Agent harness architecture
- Verification and faithfulness in agent systems

*Ingested via Playwright MCP + X search fallback per x-post-to-obsidian-wiki skill.*