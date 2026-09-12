---
title: Vault Automation — Self-Maintaining Loop
type: concept
tags: [knowledge-management]
description: "The three maintenance cadences (finalize / nightly / weekly), what each does, and the cron lines to enable them. One entry point: scripts/maintain.py."
status: current
as_of: 2026-09-12
---

# Vault Automation — the self-maintaining loop

The vault historically ran a 6-hour ingest cron (`c09d51fd4ed2`) that added notes
but **skipped the maintenance steps**, so `INDEX.tsv`, the OKF indexes, and `log.md`
drifted, supersession was never applied, and orphans/broken links/contradictions
piled up silently. This document defines the loop that fixes that and makes it
**impossible to half-skip**: three cadences behind **one entry point**.

```
python3 scripts/maintain.py finalize [--apply] [-m MSG]   # after every ingest (6h)
python3 scripts/maintain.py nightly  [--apply]            # nightly
python3 scripts/maintain.py weekly   [--apply]            # weekly
```

Every script **defaults to `--dry-run`** (prints what it would do, writes nothing)
and only mutates the vault under **`--apply`**. Nothing is ever deleted (the mount
blocks deletion and the supersession model is "keep information, rank it").

---

## Cadence 1 — `finalize` (after every ingest, ~6h)

`scripts/finalize-ingest.py` — the **post-ingest SOP as one idempotent command**.
This is what every ingest MUST call so indexes and the log never drift again.
In order:

1. `okf-frontmatter-fix.py` — move any stray invalid `related:` YAML out of
   frontmatter into a body `## Related` section (invalid `related:` breaks PyYAML
   and the TAG-INDEX generator — see CLAUDE.md / SCHEMA.v2).
2. `build-search-index.py` — rebuild **`INDEX.tsv`** (the retrieval index).
3. `regenerate-tag-index.py` — rebuild **`entities/TAG-INDEX.md`**.
4. `regenerate-processed-index.py` — rebuild **`processed/index.md`**.
5. `append-okf-log.py "<msg>"` — append a dated entry to **`log.md`**.

i.e. rebuild INDEX.tsv + regenerate all three index artifacts (INDEX.tsv,
TAG-INDEX.md, processed/index.md) + fix stray related YAML + append the changelog.
Idempotent: a clean vault re-run is a no-op (the log dedupes on message).

```
python3 scripts/maintain.py finalize --apply -m "Ingest: <title> (<source>)"
```

## Cadence 2 — `nightly` (nightly)

`scripts/nightly-reconcile.py` — supersession reconcile + health sweep.

- **Supersession.** Reuses `scripts/detect-duplicates.py`'s same-topic clustering
  (imported directly — single source of truth for the heuristic + thresholds in
  `docs/supersession.md`). It **auto-applies only unambiguous clusters**, defined
  conservatively as: a **clean 2-note pair**, both dated, effective dates
  **> 14 days** apart (not co-current), and **no time-slice snapshot** member
  (`…-landscape`, `-YYYY`, "state of / as of", "snapshot"). For those it sets the
  older note `status: superseded` + `superseded_by: <newer>` and the newer
  `status: current` + `supersedes: [<older>]` (both retained; a `## Supersession`
  body line is added for Obsidian navigability). Larger/fragmented clusters, near
  ties, undated members, and time-slices are **left for a human curator** and
  listed in `docs/supersession-candidates.md` (regenerated every run).
- **Health sweep.** Finds **new orphans** (processed/entities notes with no inbound
  wikilink) and **new broken wikilinks** ( `[[target]]` with no matching note) and
  appends them to a running **`docs/health.md`**. "New" = not seen on a prior run
  (state in `docs/.health-state.json`), so the log never repeats itself.
- **`as_of` flag.** Reports how many notes lack `as_of` and lists the genuinely
  **undateable** ones (no `as_of`/`date`/`ingested`) — the actionable subset for
  temporal ranking.

```
python3 scripts/maintain.py nightly          # dry-run (recommended default)
python3 scripts/maintain.py nightly --apply   # apply supersession + append health.md
```

> **Shipping recommendation:** run nightly **dry-run** at first. The clustering is a
> *candidate generator*: even clean 2-note pairs can be semantically adjacent but
> distinct (e.g. a PyTorch-profiler note vs. an FX-graphs note) that must **not** be
> auto-superseded. Enable `--apply` only once you've watched a few dry-runs and are
> comfortable with what it proposes, or after tightening the auto gate further. The
> frontmatter edits are additive, idempotent, and never clobber an already
> superseded/historical/deprecated note.

## Cadence 3 — `weekly` (weekly)

`scripts/weekly-friction.py` — writes the **one artifact the owner reviews**:
`briefings/YYYY-MM-DD-friction.md`. It reports:

- **What changed this week** — notes added/modified in the last 7 days (via
  `git log`, falling back to file mtime) + count of outstanding same-topic clusters.
- **Conflicts to resolve** — candidate **contradictions**: same-topic note pairs
  (reusing the detector's tag+entity clustering) whose sentences carry **opposing
  polarity cues** (recommend vs avoid, better vs worse, faster vs slower, works vs
  fails, necessary vs unnecessary) **and share ≥2 substantive content tokens** so
  they're about the same specific subject. These are heuristic *candidates* — the
  briefing quotes both sides and asks the owner to adjudicate (CLAUDE.md
  "Contradiction Detector").

```
python3 scripts/maintain.py weekly           # dry-run: print the draft
python3 scripts/maintain.py weekly --apply    # write briefings/YYYY-MM-DD-friction.md
```

---

## Dependencies

- `maintain.py`, `finalize-ingest.py`, `nightly-reconcile.py`, `weekly-friction.py`,
  `build-search-index.py`, `detect-duplicates.py`, `append-okf-log.py` are **stdlib
  only** (`finalize` orchestrates the others via subprocess).
- `okf-frontmatter-fix.py`, `regenerate-tag-index.py`, `regenerate-processed-index.py`
  require **PyYAML** (`pip3 install pyyaml`). `finalize` calls these, so PyYAML must
  be installed on the machine that runs the cron.

## Recommended cron (owner enables — DO NOT auto-install)

Adjust `WIKI` and the Python path to your machine. Times are local. These lines are
a recommendation only; this task deliberately does **not** touch the system crontab.

```cron
WIKI=$HOME/Documents/Obsidian/wiki
PY=/usr/bin/python3
LOG=$HOME/Library/Logs/wiki-maintain.log

# 1) FINALIZE — run at the END of the existing 6-hour ingest job (id c09d51fd4ed2),
#    replacing the old manual "regenerate indexes + append log" steps it skipped.
#    Preferred: append to the ingest command so finalize always follows ingest:
#        <ingest command> && $PY $WIKI/scripts/maintain.py finalize --apply -m "Ingest batch"
#    Standalone fallback (independent 6-hour tick):
0 */6 * * *  cd $WIKI && $PY scripts/maintain.py finalize --apply -m "6h finalize" >> $LOG 2>&1

# 2) NIGHTLY — supersession reconcile + health sweep. Start in DRY-RUN (no --apply);
#    add --apply once you trust the proposals.
15 3 * * *   cd $WIKI && $PY scripts/maintain.py nightly >> $LOG 2>&1

# 3) WEEKLY — friction briefing every Monday 07:00.
0 7 * * 1    cd $WIKI && $PY scripts/maintain.py weekly --apply >> $LOG 2>&1
```

To enable: `crontab -e`, paste the block, save. To verify: `crontab -l` and watch
`$LOG`. To disable a cadence, comment its line. macOS may require granting `cron`
Full Disk Access (System Settings → Privacy & Security) to reach `~/Documents`.

## Outputs at a glance

| Cadence  | Reads                                  | Writes (under `--apply`)                                   |
|----------|----------------------------------------|------------------------------------------------------------|
| finalize | `processed/`, `entities/`              | `INDEX.tsv`, `TAG-INDEX.md`, `processed/index.md`, `log.md`, related-fixes |
| nightly  | `processed/`, `entities/`, clusters    | note frontmatter (supersession), `docs/health.md`, `docs/.health-state.json` |
| weekly   | `processed/`, `entities/`, git log     | `briefings/YYYY-MM-DD-friction.md`                          |

All three refresh `docs/supersession-candidates.md` as a side effect (the detector's
read-only report). See `docs/supersession.md` for the temporal model and thresholds.
