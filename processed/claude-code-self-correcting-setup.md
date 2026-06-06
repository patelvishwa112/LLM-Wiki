---
tags: ["claude-code", "self-correction", "hooks", "claude-md", "engineering"]
source: https://x.com/zodchiii/status/2059563487676784696
date: 2026-05-27
type: bookmark
---

# How to Make Claude Code Fix Its Own Mistakes Automatically

By @zodchiii | May 27, 2026 | 32.4K views | 205 bookmarks

## Key Takeaways

- **CLAUDE.md as living mistake log**: After every correction, say "Update CLAUDE.md so you don't make that mistake again." Sweet spot: ~12 rules under 200 lines
- **PostToolUse hooks**: Auto-format + type-check + lint every file the moment Claude writes it. Errors caught in same turn
- **Stop hooks as quality gate**: Tests run automatically when Claude says "done." If they fail, Claude continues fixing without manual intervention
- **PreToolUse hooks**: Filter large log files before Claude reads them; block writes to sensitive files like .env
- **Auto-retry with token budget**: "You have 3 attempts. Don't try the same fix twice." Combined with Stop hooks = self-correcting loop
- **Result**: 45 min → 10 min per feature, same-mistake repeats near zero

## Summary

Darkzodchi lays out a complete 6-step system for making Claude Code self-correcting. Step 1 builds a living CLAUDE.md that grows from every mistake. Steps 2-4 set up hooks (PostToolUse, Stop, PreToolUse) to catch errors in real-time. Step 5 adds auto-retry with token budgets. Step 6 ties it together with cross-session memory. Includes a full copy-paste settings.json.

## Source

https://x.com/zodchiii/status/2059563487676784696
