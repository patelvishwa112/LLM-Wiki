---
source_url: https://huggingface.co/blog/peft-beyond-lora
ingested: 2026-06-18
domain: huggingface.co
title: Beyond LoRA: Can you beat the most popular fine-tuning technique?
authors: Benjamin Bossan, Sayak Paul, et al.
published: June 18, 2026
---

# Beyond LoRA: Can you beat the most popular fine-tuning technique?

[Full article content from Firecrawl extraction - see original for images, tables, and interactive Space]

## Key Sections

### When you plan to fine-tune a model in a parameter-efficient way, think beyond LoRA

If you want to fine-tune an open model on your own data, you are probably interested in so-called parameter-efficient fine-tuning, in short _PEFT_. ... (full intro on why PEFT, memory issues, etc.)

### LoRA: The queen of fine-tuning techniques 👑

Statistics: 98.4% of PEFT mentions on HF Hub are LoRA. Similar dominance in image gen and GitHub code.

Questions whether this is because it's truly best or self-reinforcing popularity.

### Choosing the right PEFT technique based on paper results is problematic

Bias in papers, different benchmarks, reproducibility issues.

### How we approach benchmarking in `PEFT`

HF added benchmarks in PEFT lib: MetaMathQA (LLM math reasoning) and image generation (cat plushy concept learning on FLUX).

Same conditions for all methods: base model, dataset, code, hardware.

Tracks: test performance, VRAM, forgetting/drift, runtime, checkpoint size.

### Our findings: LoRA works well but is not necessarily the best choice

LoRA on Pareto frontier in LLM benchmark but other methods (BEFT, Lily, OFT) offer better tradeoffs or strictly dominate in image-gen (OFT beats LoRA on score + memory).

Variants like rs-LoRA, LoRA-FA also highlighted.

Conversion support added to turn other adapters into LoRA for ecosystem compatibility (vLLM etc.).

### Conclusion

LoRA not bad, but don't default to it. Use PEFT unified API to try others easily. Contribute benchmarks/PRs.

Example code diff for switching from LoraConfig to OFTConfig.

---

**Note:** Full markdown, images, and interactive Space at source URL. Extracted via Firecrawl for wiki ingestion. Long article (~8k+ chars) - key takeaways synthesized in processed note.