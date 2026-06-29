# LLM Wiki — Intelligence Layer

## Vault Identity

**Purpose:** A compounding knowledge graph that connects AI research, agent architectures, trading/quant strategies, browser automation, prompt engineering, mechanistic interpretability, and personal projects into a unified thinking system.
**Principle:** This is not a filing cabinet. It is a training set building on itself. Every note is a data point about patterns noticed, what returns, what compounds.

## Vault Structure

```
raw/                    — Raw scraped articles (author_statusid.md)
  anthropic/            —   Anthropic research: articles, papers, transcripts
processed/              — Processed/synthesized notes with YAML frontmatter
  tags: [...]           —   Multi-domain tags for cross-topic reasoning
  source: URL           —   Link back to original
  type: concept         —   Note type: bookmark, concept, entity, comparison
  related: [[...]]      —   Explicit wikilinks to connected notes
entities/               — Entity profiles (companies, people, projects, models)
index.md                — OKF v0.1 bundle index (read first)
Bookmarks Index.md      — Master index organized by topic
SCHEMA.md               — Structural conventions
CLAUDE.md               — Vault conventions and navigation
PERSONAL.md             — Personal context (gitignored)
```

## Knowledge Domains (by tag cluster)

| Domain | Primary Tags |
|--------|-------------|
| Agent Architecture | agents, agent-harness, workers, orchestration, multi-agent, agent-ops |
| Claude/AI Tools | claude, claude-code, claude-cowork, prompt-engineering, skills, mcp, artifacts |
| Interpretability | mechanistic-interpretability, probing, patching, faithfulness, superposition, sparse-autoencoders |
| Trading/Quant | polymarket, markov-chains, trading, monte-carlo, kelly-criterion, prediction-markets |
| Browser Agents | browser-agents, agent-memory, autobrowse, browserbase |
| ML Research | mlx, qwen, training, slm, lora |
| Personal Projects | experiment, ghost-in-residual-stream, values-slm |
| Meta/Learning | second-brain, knowledge-graph, obsidian, vault |

## How to Navigate This Vault

1. **Start with tags, not folders.** Two notes in different domains may share a tag and reveal unexpected connections. Tags are the primary navigation primitive.
2. **Follow wikilinks.** Every note's "Related" section is an explicit edge in the knowledge graph. Traverse them.
3. **Raw notes are source material.** `raw/author_statusid.md` contains the full original article. Processed notes are distilled versions. When detail matters, read the raw.
4. **Cross-domain is where insight lives.** The most valuable connections live between domains — e.g., Markov Chain state transitions ↔ agent FSM design ↔ browser workflow convergence.
5. **The Bookmarks Index is the entry point.** It organizes everything by topic. Start there when exploring a new domain.
6. **OKF bundle root:** Read `index.md` first for progressive disclosure (agents and humans).

## OKF alignment (Open Knowledge Format v0.1)

This repository is an **OKF-style knowledge bundle**: git-distributed markdown concepts with YAML frontmatter.

| OKF role | Vault path |
|----------|------------|
| Bundle index | `index.md` (`okf_version: "0.1"`) |
| Concepts | `processed/*.md` — **required:** `type`; **required on new ingests:** `description` (one-line; quote if it contains `: `) |
| Optional indexes | `Bookmarks Index.md`, `entities/TAG-INDEX.md`, `processed/index.md`, `log.md` |
| Entity concepts | `entities/*.md` (exclude `TAG-INDEX.md` from concept count) |
| Citations / archive | `raw/` — provenance; may be omitted from slim OKF exports |

**Agent rules:** Pull knowledge on demand — index → tags → specific concept files. Never mirror the whole wiki into harness MEMORY.md.

**Frontmatter hygiene:** Do not put `related: [[wikilinks]]` in YAML (breaks PyYAML/TAG-INDEX). Use `## Related` in the body only. Run `python3 scripts/okf-frontmatter-fix.py` after bulk imports if needed.

## Vault Operations

### File Placement Rules

Every file has exactly one correct home:

| Content Type | Destination | Example |
|-------------|-------------|---------|
| Raw scraped article (X, web, paper) | `raw/author_statusid.md` | `raw/nurijanian_2063186118409929161.md` |
| Anthropic research source | `raw/anthropic/articles/` or `papers/` | `raw/anthropic/papers/arxiv-2204.05862.md` |
| Synthesized/processed note | `processed/slug.md` | `processed/problem-first-skill-invert-bad-ideas.md` |
| Entity profile (company, person, tool) | `entities/name.md` | `entities/deepseek.md` |
| Career or personal document | `Career/` (gitignored) | `Career/Resume - May 2026.md` |
| Owner identity/context | `PERSONAL.md` (gitignored) | — |

### Ingestion Workflow

When adding a new article or source:

1. **Save raw** → `raw/author_statusid.md` with `source_url`, `ingested` date, `sha256`
2. **Create processed note** → `processed/slug.md` with YAML frontmatter (`tags`, `source`, `date`, **`type`** (required), **`description`** (required, one line; OKF — duplicate `summary` text if both present), quoted `summary` optional, `raw: "[[raw/...]]"`). Put `## Related` wikilinks in the body only, not invalid `related:` YAML lists.
3. **Update Bookmarks Index** → add to both By Topic section and A-Z listing
4. **Regenerate OKF indexes** → `python3 scripts/regenerate-okf-indexes.py` (TAG-INDEX + `processed/index.md`)
5. **Append changelog** → `python3 scripts/append-okf-log.py "Ingest: <title> (<source>)"`
6. **Create entity pages** → if the article introduces a new company, person, tool, or concept that warrants a standalone entity page, create one in `entities/`
7. **Run wiki-sync** → `~/scripts/wiki-sync.sh` or wait for cron job (`c09d51fd4ed2`, every 6 hours)

### Sensitive Information Policy

**NEVER include in tracked files:**
- Owner's name, employer, job title, location
- Resume content, career plans, compensation targets
- Personal filesystem paths (`/Users/...`, `~/.hermes/...`)
- API keys, tokens, credentials
- Any information that identifies the vault owner

**Where personal info lives:**
- `PERSONAL.md` — owner identity and context (gitignored)
- `Career/` — resume, transition plan, portfolio plan, job tracking (gitignored)

**Before every commit, verify:** no personal references in tracked files. If a processed note mentions the owner, strip it — the note should only contain the article's content and analysis, not personalized commentary.

### Entities Maintenance

`entities/TAG-INDEX.md` is the master cross-reference mapping every tag to all processed articles. It must be regenerated whenever new processed notes are added or tags change.

The entities/ folder also contains standalone entity profiles for significant companies, people, tools, and models. These complement but do not replace the TAG-INDEX.

## Intelligence Operations

### Connection Finder
When asked to find connections: read tags across ALL notes, not just the ones in the same domain. Look for shared structural patterns (e.g., "decompose into swappable units" appears in iii harness, Claude Code techniques, and Autobrowse). Name the pattern and list every note that exhibits it.

### Question Answerer
Before answering from general knowledge: search the vault for relevant notes. Tell the user what their own accumulated knowledge says first. Then identify gaps where new information is needed.

### Synthesis Generator
When asked to synthesize across notes: identify the central pattern or claim, organize supporting evidence hierarchically, name tensions and unresolved questions, and produce an insight no individual note contains.

### Contradiction Detector
When asked to find contradictions: look for notes that make opposing claims or recommend conflicting approaches. Quote the specific sections. Ask the user to clarify their actual position.

### Discovery Engine
Proactively surface: notes that share tags but aren't explicitly linked, notes that would strengthen an existing argument, and gaps in the knowledge graph where a connecting concept is missing.

## Anti-Patterns

- **Never give generic answers** when relevant notes exist in the vault. Ground responses in the user's own accumulated knowledge.
- **Never silo by topic.** The value is in cross-domain connections. File-by-type, think-across-topics.
- **Never treat raw notes as final.** Raw notes are source material. Processed notes are the refined understanding. Cite both when appropriate.
- **Never ignore contradictions.** If two notes conflict, surface it. Intellectual honesty compounds.
- **Never wait to be asked about a connection that clearly exists.** Proactive surfacing is the difference between a filing cabinet and a thinking partner.
