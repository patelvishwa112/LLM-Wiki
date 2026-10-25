---
title: How To Fine-Tune a Small LLM on Your Own Data (Full Guide)
type: bookmark
description: "Rahul's 15-step QLoRA guide for a 1.5B model on 200-500 reviewed examples: rights ledger, OCR cascade, company-level split, Colab T4 training, baseline-first eval, and vLLM/FastAPI serving."
tags: [training, fine-tuning, lora, slm, data-curation, evals, production]
source: https://x.com/sairahul1/status/2100882424343265527
date: 2026-09-18
author: Rahul
summary: "Rahul's 15-step QLoRA guide for a 1.5B model on 200-500 reviewed examples: rights ledger, OCR cascade, company-level split, Colab T4 training, baseline-first eval, and vLLM/FastAPI serving."
raw: "[[raw/sairahul1_2100882424343265527]]"
---

# How To Fine-Tune a Small LLM on Your Own Data (Full Guide)

**Source:** Rahul (@sairahul1), 2026-09-18. A long-form, code-at-every-step tutorial that takes one concrete task — startup brief → grounded funding-pitch copy — from data rights through production serving.

The thesis is narrower than the title suggests: fine-tuning does not make a model smarter, it makes it consistent at one specific task, and a 1.5B model trained on 200–500 good examples can beat a frontier model prompted generically at that task. So the ordering matters — build three baselines (strong prompt-only, prompt + retrieval, fine-tuned) and only start training once the prompt-only baseline fails at something specific. The split of responsibilities is stated plainly: weights are good for tone, structure, consistency, domain vocabulary and instruction compliance; retrieval is for facts, current market data and competitor intelligence. A hybrid pipeline — brief → optional retrieval → small fine-tuned model → plain text out — is the architecture he actually recommends.

Roughly two-thirds of the guide is data work, which is the point. Before downloading a single file, record a rights ledger per source (owner, review date, commercial-use and redistribution flags) on the premise that public availability is not training permission; raw PDFs, OCR output and permission emails stay private while metadata, hashes, schemas and processing code go public so the pipeline stays reproducible. Text extraction is a cascade — native PDF text, then layout-aware OCR (Docling, PaddleOCR), then a second engine or human review — with a per-page record in which the machine draft is explicitly labelled `machine_draft_unverified` and `gold_text` stays empty until a human fills it. Empty OCR pages are kept, not dropped. Cleaning is restricted to NFKC normalisation and whitespace repair, and numbers are never auto-corrected: a mangled `$12.5M` goes to review, because a model trained on wrong numbers produces fluent but financially wrong output. Every numeric string is tracked separately and evaluated independently of prose quality.

Dataset construction is deliberately manual: a page is not a training example, so each pair needs a written brief, a drafted output, a comparison of the draft against source evidence, and a human review before it enters the set. The output is plain text with no schema, and the rule is that an unverified metric is omitted, never invented. The split is by company rather than by page — page-level splits leak company-specific phrasing into validation and make a memorising model look like a generalising one — at 80/10/10 train/validation/test, with a split manifest, and a test set that is burned once looked at.

Training itself is unremarkable in the best way: Qwen2.5-1.5B-Instruct loaded in 4-bit NF4 via bitsandbytes, LoRA adapters at r=16 / alpha=32 / dropout 0.05 on all linear layers, learning rate 2e-4, 2 epochs, gradient accumulation 8, packing and gradient checkpointing, run on a free Colab T4 with checkpoints written to Drive every 50 steps and `resume_from_checkpoint` after the inevitable disconnect. Evaluation is against the prompt-only baseline on plain-text compliance, human usefulness rating, unsupported-claim rate, numeric preservation, repetition, readability, latency and cost per request — never against training loss. Serving is vLLM with `--enable-lora` for throughput or FastAPI + Transformers for low traffic, always behind a VPS that terminates TLS and handles auth, rate limits and queueing, because a raw model server should never face the internet.

## Why it matters

The common failure mode this addresses is reaching for a bigger model or a better prompt when the actual problem is consistency at one bounded task — and a 1.5B adapter costing roughly $1.70 per training run is a cheaper answer than another tier of API spend. The data-rights ledger and per-page provenance records are also the parts most teams skip and the parts that decide whether the artifact is shippable at all. The company-level split rule is the single most transferable idea here: it is the difference between a fine-tune that generalises to unseen inputs and one that memorised its way to a good validation number.

## Key points

- Baseline ordering: prompt-only → prompt + retrieval → fine-tuned; train only after the prompt-only baseline fails at something specific.
- Start at 0.5B–3B parameters; the guide uses `Qwen/Qwen2.5-1.5B-Instruct` (alternatives: Qwen3-0.6B, SmolLM2-1.7B-Instruct). Avoid 7B/14B for a first pass — more memory, longer runs, higher serving cost, higher overfitting risk on a small set.
- Dataset target: 200–500 human-reviewed examples; roadmap v1 = 200 reviewed examples, v2 = 1,000, v3 = larger set + retrieval.
- Rights record per source before download: `rights_status`, `permission_scope`, `commercial_use_permitted`, `redistribution_permitted`, `rights_reviewed_at`. Public ≠ permitted.
- Reproducible ingest: explicit URL allowlist, `%PDF-` magic-byte check, sha256 + byte count + timestamp per file in a `download-manifest.json`, duplicates skipped by content hash.
- Extraction cascade: native text → layout-aware OCR (Docling/PaddleOCR) → second engine or manual review. Never silently drop pages where OCR returns nothing; machine draft ≠ ground truth.
- Cleaning is NFKC + null bytes + non-breaking spaces + whitespace collapse only. Never auto-correct numbers — `$12.SM` goes to review, not to a language model.
- Split by company, not by page, at 80/10/10, with a `split_manifest` recording company IDs and dataset hash. The test set is burned once you evaluate against it.
- QLoRA config: 4-bit NF4 with double quant, `r=16`, `lora_alpha=32`, `lora_dropout=0.05`, `target_modules="all-linear"`, `learning_rate=2e-4`, `num_train_epochs=2`, `gradient_accumulation_steps=8`, `packing=True`. Lower training loss is not better generalisation.
- Colab specifics: free T4, save to Drive every 50 steps, `trainer.train(resume_from_checkpoint=True)` after a session death, and record exact library versions before every run.
- Cost model: $0.40/hr GPU × ~4 hours (3 active + 1 retry) + $0.10 storage ≈ **$1.70** per run — then budget **5–10×** that for repeated experimentation (rank sweeps, dataset rebuilds, eval runs).
- Eval dimensions: plain-text compliance, usefulness 1–10, unsupported-claim rate, numeric preservation, repetition, readability, latency, tokens/cost per request. The example scorecard (illustrative, not measured) moves usefulness 7.1 → 8.0, unsupported claims 8% → 2%, numeric errors 3% → 1%, latency 2.4s → 1.5s.
- Numeric hallucination check is code, not vibes: set difference of extracted numeric strings between source and generated output.
- Serving: vLLM with `--enable-lora --lora-modules name=./artifacts/adapters/v1 --max-model-len 2048`, or FastAPI + Transformers for low traffic. Production path is client → HTTPS + auth → VPS rate limiter → queue → GPU server.
- Retraining discipline: only reviewed examples, a documented failure pattern, a stable eval set, a dataset hash and a `rollback_artifact`; opt-in consent and PII stripping before any production data is stored.
- Closing claim: the highest-leverage improvement is almost never the learning rate — it is clear briefs, verified evidence, human-reviewed targets and a company-level split.

## Related

- [[peft-beyond-lora]]
- [[finetune-free-trl-colab-cli-paniego]]
- [[unsloth-decision-model-qwen35-4gb-lora]]
- [[multi-lora-serving-one-gpu-vllm-chawla]]
- [[google-gemma-4-12b-local-fine-tuning]]
