---
tags: ["claude-code", "deepseek", "cost-optimization"]
source: https://x.com/godofprompt/status/2052798956699017621
date: 2026-05-08
type: processed-note
related:
  - "[[claude-code-investment-research-setup]]"
  - "[[claude-code-cost-optimization-prompts]]"
---

# DeepSeek V4 as a Parallel Claude Code Session

## Summary
DeepSeek V4 now supports Claude Code's API protocol natively, enabling a parallel second-opinion session at a fraction of Claude Opus 4.7's cost ($0.14/M vs $5.00/M). The setup routes tasks by cost tier while keeping the original Claude session as the primary — the human remains the decision layer.

## Key Takeaways
- **Cost comparison**: DeepSeek V4 Flash at $0.14/M tokens vs Claude Opus 4.7 at $5.00/M (~35x cheaper)
- **Setup**: Export `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, and model variables pointing to DeepSeek's API — then run `claude` as usual in a separate terminal
- **Task routing strategy**:
  - Complex reasoning, writing, nuance → Claude Opus 4.7 (primary session)
  - Bulk generation, templates, structured output → DeepSeek V4 Flash ($0.14/M)
  - Architecture reviews, second opinions → DeepSeek V4 Pro ($1.74/M)
- **Key principle**: Never replace Claude entirely. Run both sessions in parallel. The decision layer is yours

## Connections
- [[claude-code-investment-research-setup]] — another Claude Code optimization setup for research workflows
- [[claude-code-cost-optimization-prompts]] — complementary prompt-level cost reduction strategies
