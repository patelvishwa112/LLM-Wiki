# Controlled Tag Taxonomy

> Companion to `SCHEMA.v2.md`. This is the **canonical, controlled vocabulary** for the `tags` field. **Every tag on a note MUST appear in this file.** New tags are added here first (with a one-line purpose) before being used. Migration from the legacy free-for-all vocabulary is defined in `tags-migration.json`.

- **Canonical tags:** 121  (collapsed from 1072 legacy tags; 42 legacy tags / 43 usages dropped as noise)

- **Facets:** tags below are the TOPIC facet. Note *type* (bookmark/article/concept/note/resource/experiment) and *status* (draft/living/stable/superseded) are separate frontmatter fields — do **not** encode them as tags.

- **Conventions:** lowercase, hyphenated, singular-or-plural per the canonical spelling below; one term per concept (synonyms are collapsed); aim for 3-8 tags per note.


## Facet: TOPIC (domain > tag)


### Agents & Harness
_How autonomous, tool-using LLM systems are built and run — the vault's core domain._

- **`agents`** (313) — Any autonomous or tool-using LLM system; the single largest topic in the vault.
- **`agent-harness`** (136) — The scaffolding/runtime wrapped around a model: control loop, tools, state.
- **`harness-engineering`** (52) — Designing and optimizing the harness itself as an engineering discipline.
- **`loop-engineering`** (59) — The agent control loop — iteration, feedback loops, loop-driven development.
- **`multi-agent`** (66) — Multiple cooperating or competing agents: teams, swarms, crews, delegation.
- **`orchestration`** (42) — Coordinating steps, agents, and tools into a pipeline.
- **`subagents`** (30) — Delegated child agents spawned and managed by a parent agent.
- **`agent-architecture`** (17) — Structural design patterns for a single agent.
- **`agent-memory`** (58) — Persistent, episodic, semantic, or procedural memory and context state for agents.
- **`agent-ops`** (66) — Running agents in production: sandboxes, approvals, recovery, reliability, auditability.
- **`agent-frameworks`** (29) — Libraries/SDKs for building agents (LangChain, LangGraph, DSPy, CrewAI, ADK).
- **`browser-agents`** (8) — Agents that drive a real web browser (Autobrowse, Browserbase, Playwright).
- **`coding-agents`** (8) — Autonomous coding agents (Devin, Goose, background coding agents).
- **`tool-use`** (13) — Tool/function calling, tool design, programmatic tool calling, structured outputs.
- **`planning`** (4) — Task planning and decomposition by agents.
- **`autonomy`** (2) — Degree of independent action; fully autonomous operation.
- **`human-in-the-loop`** (14) — Human oversight, approval, and collaboration inside the loop.

### AI Coding & Dev Tools
_Tools and workflows for building software with AI._

- **`claude-code`** (124) — Claude Code CLI: config, hooks, slash-commands, CLAUDE.md, plan mode.
- **`claude-cowork`** (14) — Claude Cowork product and workflows.
- **`coding-tools`** (65) — AI coding assistants & dev workflow (Cursor, Copilot, VS Code, worktrees, git, code review).
- **`codex`** (21) — OpenAI Codex / codex CLI.

### Claude / Anthropic Ecosystem
_Claude, Anthropic, and its protocols._

- **`claude`** (52) — Claude models and product surface (includes Artifacts, Opus).
- **`anthropic`** (36) — Anthropic the company: its research, releases, and positioning.
- **`mcp`** (52) — Model Context Protocol — servers/clients/hosts and protocol standards.
- **`computer-use`** (3) — The computer-use capability (screen/desktop control).

### Prompt / Skills / Context
_Steering models through prompts, skills, and context._

- **`prompt-engineering`** (60) — Prompt design and prompting techniques, prompt optimization, meta-prompting.
- **`skills`** (96) — Claude Skills: authoring, skill packs, document-to-skill, progressive disclosure of skills.
- **`context-engineering`** (57) — Managing the context window: compaction, progressive disclosure, semantic state.
- **`long-context`** (12) — Long-context models and their limits (context rot, context window).

### Model Training & Post-training
_Turning base models into capable ones._

- **`training`** (97) — Model training generally: frameworks, curricula, from-scratch, optimizers.
- **`pretraining`** (11) — The pretraining stage.
- **`post-training`** (22) — The post-training stage broadly.
- **`fine-tuning`** (36) — SFT, LoRA/PEFT, adapters, instruction tuning.
- **`distillation`** (23) — Model/knowledge distillation, teacher-student, on-policy & API distillation.
- **`continual-learning`** (22) — Online/continual learning, adaptation, catastrophic forgetting, plasticity.
- **`rl`** (112) — Reinforcement learning (RLVR, GRPO/PPO/DPO, policy optimization, rollouts, exploration).
- **`rlhf`** (14) — RL from human feedback specifically.
- **`reward-modeling`** (7) — Reward models, reward design, preference data.
- **`synthetic-data`** (5) — Synthetic / model-generated training data.

### Model Architecture & Internals
_How models are built at the layer level._

- **`transformers`** (17) — Transformer architecture and its variants.
- **`attention`** (27) — Attention mechanisms (Flash/GQA/MQA/MLA, linear & sparse attention, softmax).
- **`moe`** (8) — Mixture-of-experts architectures.
- **`kv-cache`** (19) — The KV cache.
- **`quantization`** (7) — Quantization, pruning, and model compression.
- **`diffusion-models`** (8) — Diffusion and flow-matching generative models.
- **`multimodal`** (24) — Vision/audio/video/speech and VLMs; multimodal models.
- **`embeddings`** (5) — Embedding models and learned representations.
- **`tokenization`** (2) — Tokenizers and vocabulary.
- **`scaling-laws`** (12) — Scaling laws and compute-optimal training.
- **`model-architecture`** (8) — Novel architectures (SSM/Mamba, recurrence, hypernetworks).
- **`reasoning`** (32) — Reasoning models, test-time compute, extended thinking, recursive/looped LMs.

### Inference & ML Systems
_Serving models efficiently at scale._

- **`inference`** (67) — Inference algorithms and local inference; decoding, routing, speculative decoding, batching.
- **`serving`** (19) — Model serving and providers (vLLM, SGLang, Together, OpenRouter, LiteLLM).
- **`gpu`** (27) — GPUs, CUDA, kernels, profiling, hardware.
- **`distributed-systems`** (17) — Parallelism (tensor/pipeline) and distributed training/serving.
- **`cost-optimization`** (43) — Token/cost efficiency, caching, latency and throughput tuning.

### Models, Labs & Open Source
_The model and lab landscape._

- **`models`** (34) — Foundation/frontier models generally, model specs.
- **`frontier-labs`** (85) — Labs and their models (OpenAI, DeepMind, DeepSeek, Kimi/Moonshot, Qwen/GLM, xAI, etc.).
- **`open-source`** (28) — Open-weight/open-source models and tooling (HuggingFace).
- **`slm`** (10) — Small language models / tiny models.

### Evals, Verification & Observability
_Knowing whether the system works._

- **`evals`** (72) — Evaluation methodology, rubrics, LLM eval, criteria drift, gap closure.
- **`benchmarks`** (13) — Named benchmarks and benchmarking (ARC-AGI, BrowseComp, RULER, SkillsBench).
- **`llm-judges`** (13) — LLM-as-judge / model-graded evaluation.
- **`verification`** (70) — Testing, self-verification, regression tests, debugging, static analysis.
- **`observability`** (63) — Tracing, monitoring, agent traces/trajectories, eval tooling (LangSmith, Arize, Langfuse).

### Interpretability
_Understanding model internals._

- **`interpretability`** (63) — Mechanistic interpretability broadly: circuits, superposition, probing, steering, features, faithfulness.
- **`sparse-autoencoders`** (9) — Sparse autoencoders and feature dictionaries.

### Alignment & Safety
_Making models safe and aligned._

- **`alignment`** (28) — Alignment research: sycophancy, deceptive/agentic misalignment, alignment faking, refusal.
- **`safety`** (29) — AI safety broadly: misuse, sabotage, scalable oversight, biosecurity, classifiers.
- **`constitutional-ai`** (5) — The Constitutional AI method.
- **`red-teaming`** (1) — Red-teaming specifically.
- **`jailbreaks`** (1) — Jailbreaks specifically.
- **`reward-hacking`** (2) — Reward hacking / specification gaming.
- **`security`** (27) — Agent/app security: prompt injection, guardrails, threat modeling, zero-trust.
- **`ai-policy`** (17) — Governance, regulation, societal impacts, compliance, geopolitics.

### Retrieval, RAG & Knowledge Graphs
_Getting the right knowledge into context._

- **`rag`** (22) — Retrieval-augmented generation and chunking.
- **`vector-search`** (14) — Vector DBs, ANN/HNSW, semantic search, embedding search.
- **`knowledge-graph`** (35) — Knowledge graphs, GraphRAG, ontologies, entity extraction/resolution.

### Infrastructure & Data
_The plumbing beneath AI systems._

- **`infrastructure`** (34) — Infra/devops/mlops, pipelines, platforms, OS/Linux, backups.
- **`automation`** (24) — Cron/scheduled tasks, CI/CD, workflow automation (n8n).
- **`databases`** (12) — Databases (Postgres, SQLite, Trino, Kusto).
- **`data-engineering`** (29) — Data pipelines, quality, curation, labeling, scraping, ingestion, visualization.
- **`web-dev`** (30) — Web/frontend engineering, browser internals, UI/UX, generative UI.

### Quant, Trading & Finance
_Markets and quantitative methods._

- **`trading`** (15) — Trading strategies and execution (TWAP/VWAP, systematic trading, backtesting).
- **`quant`** (22) — Quantitative methods (Bayesian, factor models, regime detection, Monte Carlo, Markov chains).
- **`finance`** (30) — Finance, investing, accounting, macro, risk management.
- **`prediction-markets`** (4) — Prediction markets (Polymarket, longshot bias).

### Research & Meta-AI
_Frontier research directions and the practice of AI._

- **`ml-research`** (36) — ML/DL research, classical ML, AGI, research taste, ablations.
- **`ai-research`** (33) — AI research automation, research agents, autoresearch.
- **`ai-engineering`** (30) — The discipline of building with AI (agentic/LLM engineering, software factory).
- **`recursive-self-improvement`** (20) — Self-improving/self-evolving systems, meta-evolution, evolutionary search.
- **`papers`** (10) — Papers / arXiv treated as content.
- **`world-models`** (16) — World models, JEPA, self-supervised representation learning, energy-based models.
- **`robotics`** (14) — Robotics, humanoids, physical AI, VLA, action chunking.

### Knowledge Management (meta)
_The vault itself and how knowledge compounds._

- **`second-brain`** (24) — PKM, atomic notes, Zettelkasten, note-taking.
- **`knowledge-management`** (27) — Vault/wiki architecture, OKF, curation, knowledge compounding.
- **`obsidian`** (14) — Obsidian specifically.
- **`writing`** (26) — Writing, documentation, memos, copywriting, storytelling.

### Career, Business & Productivity
_The human/operator layer._

- **`career`** (61) — Careers, interviewing, roles, networking, career strategy.
- **`hiring`** (6) — Hiring and recruiting (employer side).
- **`productivity`** (117) — Personal productivity, focus, process, playbooks, SOPs.
- **`learning`** (60) — Learning and study techniques, spaced repetition, fundamentals, courses.
- **`decision-making`** (28) — Judgment, mental models, problem-solving, philosophy.
- **`communication`** (16) — Communication, soft skills, stakeholders, persuasion.
- **`pm`** (26) — Product management (PRDs, requirements, PM operating systems).
- **`product`** (43) — Product discovery/strategy, PMF, design, market research.
- **`startups`** (29) — Startups, founders, solo/one-person companies, business models, moats.
- **`venture-capital`** (12) — VC and fundraising.
- **`gtm`** (16) — Go-to-market: sales, marketing, distribution, positioning.
- **`creator-economy`** (43) — Content/audience building, personal brand, social growth, newsletters.
- **`enterprise`** (40) — Enterprise AI adoption, B2B.
- **`ai-strategy`** (19) — AI strategy for orgs and individuals.
- **`ai-economics`** (18) — AI economics, token economy, Jevons paradox.

### Personal Projects
_Owner-specific projects and prototypes._

- **`hermes`** (25) — Hermes project.
- **`fable`** (13) — Fable project.
- **`openclaw`** (6) — OpenClaw project.
- **`projects`** (41) — Personal projects and experiments generally (includes named prototypes).

### Cross-cutting utility
_General tags used when no sharper facet fits._

- **`llm`** (26) — Generic LLM/AI catch-all for notes with no sharper topical home.
- **`architecture`** (31) — Software/system architecture, modularity, separation of concerns.
- **`workflows`** (28) — Workflow and agentic-workflow design.
- **`production`** (23) — Production readiness and deployment concerns.

---
_Counts in parentheses are current note-usages that will map to that tag after migration._
