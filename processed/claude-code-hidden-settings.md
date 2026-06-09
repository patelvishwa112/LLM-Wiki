---
tags: ["claude-code", "prompt-engineering", "settings"]
source: https://x.com/zodchiii/status/2053042131111927976
raw: "[[raw/zodchiii_2053042131111927976]]"
date: 2026-05-09
type: processed-note
related:
  - "[[claude-hidden-features-guide]]"
  - "[[claude-code-self-correcting-setup]]"
---

# Claude Code Hidden Settings Most Developers Never Touch

## Summary
Anthropic silently lowered Claude Code's default thinking effort from high to medium in March 2026. Most developers noticed Claude "getting worse" but blamed the model when it was actually a settings change. Six critical settings can restore or exceed pre-February quality, control permission scopes, and optimize model selection per task.

## Key Takeaways
- **Effort level**: Use `/effort high` or `max` to restore pre-February 2026 reasoning quality. The default was silently lowered to medium
- **Adaptive thinking**: Disable with `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` to force a fixed reasoning budget instead of letting Claude decide dynamically
- **Default permission mode**: Use `acceptEdits` for well-known projects, `plan` mode for unfamiliar repos to prevent destructive actions
- **Allow/deny rules**: Whitelist safe operations (Read, Glob, Grep, npm run, git status/diff/add/commit) and deny dangerous ones (.env, .ssh, rm -rf, sudo, git push)
- **Model switching**: Use `/model sonnet` for ~80% of tasks and `/model opus` only for complex refactors to save tokens
- **Compact with custom instructions**: Preserve architecture decisions, file paths, and error messages when compacting context

## Connections
- [[claude-hidden-features-guide]] — broader hidden feature catalog
- [[claude-code-self-correcting-setup]] — setups that leverage these settings for autonomous correction
- [[claude-code-cost-optimization-prompts]] — complementary cost-saving strategies
