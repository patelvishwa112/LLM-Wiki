---
title: Serving 100 fine-tuned models on one GPU with multi-LoRA
type: bookmark
description: "Avi Chawla's measured walkthrough of multi-LoRA serving in vLLM on Runpod: merged copies at 15.2 GB versus 40 MB adapters, 245-second median cold starts, and why a shared worker pool beats one endpoint per variant."
tags: [lora, vllm, inference, serving, gpu, fine-tuning, cost-optimization]
source: https://x.com/_avichawla/status/2099772866225148024
date: 2026-09-15
author: Avi Chawla
summary: "Avi Chawla's measured walkthrough of multi-LoRA serving in vLLM on Runpod: merged copies at 15.2 GB versus 40 MB adapters, 245-second median cold starts, and why a shared worker pool beats one endpoint per variant."
raw: "[[raw/_avichawla_2099772866225148024]]"
---

# Serving 100 fine-tuned models on one GPU with multi-LoRA

**Source:** Avi Chawla, 2026-09-15. A long tutorial on serving many LoRA variants from a single base model in vLLM, with a hands-on Runpod Serverless experiment.

The core arithmetic is the argument. One hundred fine-tuned variants of a 7B model occupy roughly 1.5 TB as merged weights, but about 19.3 GB when they share one base: a 15.2 GB base model plus roughly 4 GB of rank-8 adapters at 40 MB each, leaving some 60 GB of an 80 GB GPU for KV cache. Merging is not neutral — each adapter inlines into a fresh 15.2 GB copy, so three variants cost 45.6 GB to get what three 40 MB files already held. The layout also decides how many scaling pools exist: one endpoint per variant means 100 pools, each with its own workers, cold starts, and idle capacity, and an idle extraction worker cannot absorb a SQL request.

Chawla maps four deployment options — merged with one endpoint per variant, unmerged registered at startup, unmerged resolved at request time, and hosted per tenant — and then builds the second one. Three adapters (extraction to JSON, SQL generation, support routing) are trained with TRL/PEFT at rank 16 over all seven projection modules, roughly 70 MB each, on 600-row synthetic sets, then served through Runpod's vLLM worker with `ENABLE_LORA`, `MAX_LORAS=3`, and a registered `LORA_MODULES` list.

The measurements are the useful part. Warm requests showed no degradation: adapters stayed inside the base model's normal latency variation, so the memory win is not paid for at request time. Cold starts were brutal — three clean trials waited 409, 245, and 214 seconds before pickup against roughly half a second of execution, a median of 245 seconds, with 99.7 percent of measured time spent before inference and pickup delay about 307x execution. That number is a configuration artifact, not a platform property: nothing was cached, so each wake pulled the worker image and downloaded the base model plus adapters, whereas Runpod's own tuning cut a 32B model's startup from 324 to 91 seconds.

The three-endpoint comparison is where intuition breaks. The separate layout billed fewer worker-seconds but only because it completed far fewer requests, most stuck behind a boot for over two minutes; at one request every three seconds per endpoint, a warm worker never hit the five-second idle timeout. The shared endpoint stayed warm because combined traffic kept landing on one pool. Chawla's conclusion: keep adapters separate whenever they share a base, and budget startup and idle time per endpoint rather than per request.

## Why it matters

This is the concrete cost model behind "ship a fine-tune per customer." Multi-LoRA turns per-tenant specialization from a GPU-fleet problem into a memory-budget problem, which changes the unit economics of vertical AI products. It also shows that serverless latency is dominated by artifact loading, so baking weights into images or caching them on a network volume matters as much as the adapter layout, and that worker-seconds are a misleading cost metric when a run completes less work.

## Key points

- 100 variants of a 7B model: ~1.5 TB merged versus ~19.3 GB shared (15.2 GB base + ~4 GB adapters).
- One rank-8 adapter is ~40 MB; merging it creates a 15.2 GB model copy.
- Shared layout leaves ~60 GB of an 80 GB GPU for KV cache.
- Four deployment types: merged per variant, unmerged registered at startup, unmerged resolved at request time, hosted per tenant.
- Experiment used Qwen 1.5B, rank 16 across seven projection modules, ~70 MB adapters, 600 training rows per task, one RTX 4090.
- Cold starts measured at 409, 245, and 214 seconds (median 245); execution ~0.5 s; ~307x pickup-to-execution ratio.
- Warm latency across three adapters stayed within normal base-model variance.
- The three-endpoint run used fewer billed worker-seconds only because it completed fewer requests, most waiting over two minutes.
- Request-time adapter loading trades a larger catalogue for a slow first request per adapter.
- Runpod tuning separately took a 32B model on 2x H200 from 324 s to 91 s startup.

## Related

- [[how-vllm-works-amitiitbhu]]
- [[peft-beyond-lora]]
- [[adapad-lora-parallel-deflation]]
- [[multi-lora-training-osmosis]]
- [[inference-engines-2026]]
