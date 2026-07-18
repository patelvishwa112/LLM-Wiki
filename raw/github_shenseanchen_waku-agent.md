---
source_url: https://github.com/ShenSeanChen/waku-agent
ingested: 2026-07-18
author: ShenSeanChen
title: waku-agent — local-first personal AI assistant
sha256: 00f86c3b09d54b03421130034a0f085d4a3e534c83f7a3e4ca6f8237aac21940
note: README capture via Firecrawl GitHub landing + README sections; stars ~277 forks ~75 as of ingest
stars: 277
forks: 75
license: MIT
---

# waku-agent

**Repo:** https://github.com/ShenSeanChen/waku-agent  
**Author:** @ShenSeanChen (Sean's AI Stories)  
**License:** MIT  
**Tagline:** Your own AI assistant. On your laptop. In code you can read in an afternoon.

Waku is a local-first personal assistant that exposes four pillars behind serious agents: **Harness · Loop · Memory · Eval/LLM-Ops**. No heavy frameworks hiding the core. Positioned as a readable blueprint vs products (ChatGPT/Claude Desktop) and vs larger OSS assistants (OpenClaw, Hermes) — same architecture, ~1/100th the code.

## Pillars

- **Local-first:** memory is one SQLite file (`.waku/state.db`); human-readable `.waku/MEMORY.md` mirror.
- **Memory:** semantic + episodic + procedural; retrieval **gate** (whether to retrieve); consolidation pass (what to keep).
- **Loop:** ~95 lines plain Python in `waku/loop/agent.py` — reason → tools → observe; max_iterations hard stop.
- **Dashboard:** localhost:7777 cockpit — Overview / Gateway / Loop / Memory / Tools / Data / Ops.
- **Eval:** deterministic pytest + LLM-as-judge (DeepEval); `make gate` release gate; always-on JSONL traces.

## Quickstart (from README)

```
git clone https://github.com/ShenSeanChen/waku-agent && cd waku-agent
uv venv && uv pip install -e .
cp .env.example .env
uv run waku
uv run waku dashboard   # localhost:7777
```

Providers: Anthropic (default), OpenAI, Gemini, DeepSeek, MiniMax, Kimi, GLM, OpenRouter — via ~60-line adapter.

## Gateways

- CLI, dashboard, Telegram (long-poll), voice (wake word "waku waku", faster-whisper + macOS say / Kokoro)
- Optional Apple Calendar/Mail brief (`make brief`)

## Memory model

- Working memory: sliding window (`WAKU_HISTORY_TURNS`, default 12)
- Long-term: SQLite + FTS5 facts/episodes; SOUL.md preferences; skills as procedural SKILL.md
- Tools: manage_memory, update_soul, create_skill; MCP via `.waku/mcp.json`

## Loop (essence)

```
while not done:
    response = llm(messages, tools)
    if response wants tools:
        results = run(tool_calls)
        messages += results
    else:
        done
```

## Eval / ops

- `make eval` — deterministic 0/1
- `make eval-judge` — scored judge
- `make gate` — both as release gate
- Traces: `.waku/traces/<date>.jsonl`; optional Phoenix/Langfuse OTel
- Usage ledger: `.waku/usage.jsonl`
- `make shootout` — multi-provider:model trials with cost/latency/pass rates

## Experimental

- `delegate_task` to pi coding agent (live)
- Skeletons: run_command, browse_web, schedule_task

## Layout map (whiteboard → code)

| Box | Module |
|-----|--------|
| Gateway | `waku/gateway/` |
| Working memory / session | `waku/runtime/session.py` |
| Loop | `waku/loop/agent.py` |
| Tools | `waku/tools/` |
| Procedural memory | `waku/memory/procedural/` + `skills/` |
| Semantic / episodic | `waku/memory/semantic/`, `episodic/` |
| Retrieval gate | `waku/memory/retrieval_gate.py` |
| Consolidation | `waku/memory/consolidation.py` |
| Tracing / release gate | `waku/ops/` |
| Evals | `evals/deterministic/`, `evals/judge/` |

## Links

- YouTube walkthrough: https://www.youtube.com/watch?v=rvRyBhILrls
- Channel: https://www.youtube.com/@SeanAIStories
- X: https://x.com/ShenSeanChen
- Architecture docs/whiteboards under `docs/`
