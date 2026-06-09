---
title: "10 Lessons from Shipping with AI Coding Agents (AGENTS.md / CLAUDE.md)"
tags: ["agents", "claude-code", "codex", "prompt-engineering", "agent-ops", "agents-md", "claude-md"]
source: https://x.com/voxyz_ai/status/2060753730643837205
raw: "[[raw/voxyz_ai_2060753730643837205]]"
date: 2026-05-30
published: 2026-05-30
authors: ["Vox (@Voxyz_ai)"]
type: article
related: ["[[raw/voxyz_ai_2060753730643837205]]"]
status: processed
---

# 10 Lessons from Shipping with AI Coding Agents

> The entry file isn't the agent's knowledge base. It's the agent's working contract. It answers four questions: where am I and how does the code run, how should I act when I'm unsure, how do I prove I'm done, and which calls aren't mine to make?

## Key Takeaways

- Keep the root file (AGENTS.md/CLAUDE.md) **100-200 lines max**. Longer = worse adherence.
- AGENTS.md is a **router, not a library** — point to docs, don't embed them
- Write **behavior rules**, not just project knowledge. The tool knows facts; it doesn't know how to act
- Rules must be **machine-checkable** — "use named exports" not "write clean code"
- **One source of truth**: AGENTS.md is the master, CLAUDE.md just imports it
- Red lines go in **hooks/sandbox/rules**, not just in the file. The file is a "please remember," not enforcement
- Give **sensitive directories their own local file** with directory-specific risks
- Long-term memory must be **auditable** (git-tracked, deletable). Don't trust auto-memory alone
- Keep **three file types separate**: personal preferences (global), team conventions (per-project), machine permissions (hooks/rules)
- The file grows like a **test suite** — every mistake becomes a more specific rule

## Summary

Vox (@Voxyz_ai) shares 10 practical lessons from running Codex and Claude Code in production. The core insight: the context file (AGENTS.md or CLAUDE.md) is a working contract between you and the agent, not a documentation dump. The post draws direct parallels to Andrej Karpathy's 162K-star CLAUDE.md repo, which succeeded because it targeted behavior rules — "ask when unsure, make the smallest change, don't refactor for fun" — not project-specific knowledge.

### The 10 Lessons

**1. Shorter is better — 200 lines is the ceiling.** Codex has a 32 KiB concatenation limit for project docs; Claude Code loads the full file every session. Longer files mean worse adherence and rules getting squeezed out.

**2. "Do not introduce" and "Stop and ask" lists.** A stack list won't stop the agent from pulling in conflicting dependencies. A do-not list with a Reason and Revisit column tells the tool why a rule exists and when it can loosen. The Stop-and-ask column says "this call isn't yours to make alone."

**3. Write rules the tool can actually check.** "Write clean code" says nothing. "Use named exports," "components under 200 lines," "async/await instead of .then()" — these are testable in 5 seconds.

**4. Behavior rules > project knowledge.** Where agents go off the rails is behavior, not knowledge. They don't ask when unsure. They "improve" adjacent code. Karpathy's file took off because it captures failure modes as behavior rules.

**5. AGENTS.md is a router, not a library.** A power user's entry file points to where information lives: "when you need X, go read Y." Includes PLANS.md for multi-hour tasks: write a plan, split into phases, wait for sign-off. Isolated worktrees + tight goals + fine phases = overnight runs that produce clean commits, not disasters.

**6. Sensitive directories get their own local file.** Closer files carry more weight. Subdirectory files should carry only that directory's local risks. Codex overrides; Claude Code concatenates. Both walk from root down.

**7. The file states intent; hooks/sandbox/rules enforce it.** Anthropic explicitly says writing a rule in CLAUDE.md doesn't block the action — use PreToolUse hooks. Codex has hooks + rules (experimental). The real hard edges: sandbox, permission profiles, CI, isolated worktrees, withholding prod credentials. "The more dangerous the action, the further down these layers it belongs."

**8. Memory must be auditable.** Claude Code auto-memory is on by default (MEMORY.md). Codex's is off. Both vendors agree: mandatory rules go in the version-controlled file; auto-memory is backup. If it's not in a git diff, it's pollution.

**9. Keep three types of files apart.** Personal preferences (global, ~/.codex/config.toml), team conventions (per-project AGENTS.md), machine permissions (hooks.json, rules). Mixing them creates a drawer nobody dares clean.

**10. One source of truth for both tools.** Anthropic: Claude Code reads CLAUDE.md, not AGENTS.md. Fix: make AGENTS.md the source, CLAUDE.md has one import line. Or symlink. Don't maintain two files.

### Practical Setup

- Run `/init` for first draft (Codex → AGENTS.md, Claude Code → CLAUDE.md)
- Cut root file under 200 lines / 32 KiB
- Move big docs to `docs/` and `PLANS.md`
- Add Do NOT introduce and Stop and ask sections
- Back red lines with hooks/rules/sandbox
- AGENTS.md as source of truth → imported by CLAUDE.md

### Bottom Line

The entry file grows like a test suite. Every repeated mistake becomes a more specific rule. Every manual process becomes a doc pointer, hook, rule, or test command. In a month, the tools haven't gotten smarter — you've just turned implicit project knowledge into something they read, run, and verify before every job.

## Source

[Original X post by @Voxyz_ai](https://x.com/voxyz_ai/status/2060753730643837205)
