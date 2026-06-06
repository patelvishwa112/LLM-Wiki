# LLM Wiki

An open, compunding knowledge graph of AI research, agent architectures, prompt engineering, mechanistic interpretability, browser automation, ML training, and more — built on the Karpathy-style LLM Wiki pattern.

**567 notes and growing.** Raw source material in `raw/`, synthesized analysis in `processed/`, concept explainers in `concepts/`. Tag-based navigation with wikilinks connecting ideas across domains.

## Structure

```
raw/                    — Raw scraped articles (author_statusid.md)
  anthropic/            —   Anthropic research: articles, papers, transcripts
processed/              — Synthesized notes with YAML frontmatter
  tags: [...]           —   Multi-domain tags
  source: URL           —   Link back to original
  type: concept         —   Note type: bookmark, concept, entity, comparison
  related: [[...]]      —   Explicit wikilinks
entities/               — Entity profiles (companies, people, projects, models)
Bookmarks Index.md      — Master index by topic + A-Z
CLAUDE.md               — Vault conventions and navigation
SCHEMA.md               — Frontmatter spec and tag taxonomy
```

## Knowledge Domains

| Domain | Primary Tags |
|--------|-------------|
| Agent Architecture | agents, agent-harness, workers, orchestration, multi-agent, agent-ops |
| Claude / AI Tools | claude, claude-code, claude-cowork, prompt-engineering, skills, mcp, artifacts |
| Mechanistic Interpretability | mechanistic-interpretability, probing, patching, faithfulness, superposition, sparse-autoencoders |
| Trading / Quant | polymarket, markov-chains, trading, monte-carlo, kelly-criterion |
| Browser Agents | browser-agents, agent-memory, autobrowse, browserbase |
| ML Research | mlx, qwen, training, slm, lora |
| Spec-Driven Development | spec-driven-development, presets, extensions, templates |
| Meta | second-brain, knowledge-graph, obsidian, vault |

## How to Navigate

1. **Start with tags, not folders.** Two notes in different domains may share a tag and reveal unexpected connections.
2. **Follow wikilinks.** Every note's `related` section is an explicit edge in the knowledge graph.
3. **Raw notes are source material.** Processed notes are distilled versions. When detail matters, read the raw.
4. **Cross-domain is where insight lives.** The most valuable connections live between domains.
5. **The Bookmarks Index is the entry point.** It organizes everything by topic. Start there.

## Using with an AI Agent

This wiki is designed for agent consumption. Point your agent at `CLAUDE.md` for navigation conventions. Use tag-based search for topic retrieval. Processed notes have structured YAML frontmatter optimized for programmatic access.

See the [wiki-search skill](https://github.com/patelvishwa112/LLM-Wiki) for a retrieval playbook that works with the vault structure.

## Contributing

This is a personal knowledge base shared openly. If you find something useful or want to suggest a connection, open an issue. Pull requests welcome for corrections, additional sources, or cross-links.

## License

Content is sourced from public articles, papers, and posts — attribution is preserved in frontmatter. The organization and synthesis is MIT licensed.

## Acknowledgments

Built on the pattern established by [Andrej Karpathy's LLM Wiki](https://github.com/karpathy/llm-wiki). Raw/processed split, YAML frontmatter, tag-based navigation, and agent-friendly conventions.
