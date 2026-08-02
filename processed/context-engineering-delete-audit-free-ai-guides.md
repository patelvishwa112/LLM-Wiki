---
tags: ["context-engineering", "prompt-engineering", "claude-code", "agents", "agent-harness", "skills", "mcp", "compaction"]
source: https://x.com/free_ai_guides/status/2082463119742320825
date: 2026-08-01
type: bookmark
description: "4-layer context audit (instructions, memory, files, tools) with delete tests after Anthropic cut ~80% of Claude Code system prompt."
author: free_ai_guides
summary: "4-layer context audit (instructions, memory, files, tools) with delete tests after Anthropic cut ~80% of Claude Code system prompt."
raw: "[[raw/free_ai_guides_2082463119742320825]]"
---

# Context engineering rules changed: what to delete

## Key Takeaways

- Anthropic (Thariq Shihipar) removed ~**80%** of Claude Code system instructions with no coding-eval loss — “unhobbling” constraints that only protected older models.
- Past a point, more context **hurts** (attention dilution, conflicts). Supported by Chroma long-context unreliability work and Manus tool-bloat findings.
- **4-layer audit** (visible → hidden):
  1. **Standing instructions** — cut defaults (“be helpful”), dead rules, one side of contradictions; keep specific domain traps/formats.
  2. **Memory** — drop stale jobs/projects/prefs; stale memory worse than none.
  3. **Knowledge/files** — kill superseded versions and one-offs; one current doc per topic, prefer many focused files.
  4. **Tools/connectors** — unused MCP/skills/plugins still pay description tax every request.
- **Delete test** per item: still true? conflicts? would a competent hire need it? what concrete failure if removed?
- Convert process rules → outcome descriptions; re-audit after model upgrades. Safety/legal/permissions stay explicit.
- Does **not** apply to weak/local models that still need scaffolding, brand-new setups, or when outputs already excellent.

## Why it matters

Operationalizes the same “less context” shift as Anthropic’s Claude 5 / Fable context rules — a runnable checklist for CLAUDE.md, memory, vault files, and MCP surface area.

## Related

- [[new-rules-context-engineering-claude-5-trq212]]
- [[context-engineering-field-guide-phosphenq]]
- [[context-engineering-os-loop-engineering-vartekxx]]
- [[how-to-create-right-skill-ai-agent]]
