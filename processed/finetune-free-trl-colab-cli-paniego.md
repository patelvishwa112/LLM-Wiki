---
tags: ["training", "fine-tuning", "agents", "trl"]
source: https://x.com/SergioPaniego/status/2066498136273531363
date: 2026-06-20
type: bookmark
description: "Sergio Paniego: one prompt + Colab CLI + TRL QLoRA on free T4; agent writes SFT script, trackio Space, Hub adapter, self-debugs T4 precision."
author: SergioPaniego
summary: "Sergio Paniego: one prompt + Colab CLI + TRL QLoRA on free T4; agent writes SFT script, trackio Space, Hub adapter, self-debugs T4 precision."
raw: "[[raw/SergioPaniego_2066498136273531363]]"
---

# Fine-Tune a Model for Free From One Prompt (TRL + Colab CLI)

Sergio Paniego. Google Colab CLI (drive Colab runtimes from terminal) + HF stack. Demo: Qwen2.5-0.5B-Instruct QLoRA on philschmid/gretel-synthetic-text-to-sql.

## Loop

Agent in TRL repo reads `examples/scripts/`, writes a self-contained SFT script, provisions T4 via Colab CLI, installs missing bits (TRL, trackio, 4-bit), HF login, short demo run, trackio Space, push adapter, tear down. Retarget by swapping model/dataset in the prompt.

Self-debug: T4 lacked a precision mode; agent fixed and reran. Live loss: https://huggingface.co/spaces/sergiopaniego/trl-text-to-sql-trackio — adapter https://huggingface.co/sergiopaniego/Qwen2.5-0.5B-Instruct-text-to-sql-qlora

Setup: `uv tool install google-colab-cli`, authorize, `hf auth login`, paste prompt.

Related HF Jobs posts in the article. Tiny-model demo, not a training recipe paper.

## Related

- [[why-rl-environments-work-now-paniego]]
