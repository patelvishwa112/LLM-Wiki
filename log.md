# Changelog

OKF bundle history (newest sections at top).

## 2026-06-30

- Ingest: Dynamic Subagents in Deep Agents (sydneyrunkle 2071629451712983319)

## 2026-06-30

- OKF: fix append-okf-log dedupe; backfill raw sha256 on dunik ingest

## 2026-06-30

- Ingest: Design good ML experiments (iamgrigorev 2071688181628678468)

## 2026-06-30

- Ingest: Loop engineering quietly ate prompt engineering (dunik_7 2071584492804784468)

## 2026-06-28

- OKF Tier 1: bundle `index.md`, `CLAUDE.md` alignment, ingest skills + agent memory for `type` + `description`.
- Vault hygiene: fixed invalid YAML (`related` in frontmatter), backfilled `description` on all processed concepts, `scripts/okf-frontmatter-fix.py`.
- OKF Tier 2 (partial): auto-generated `processed/index.md`, `log.md`, `regenerate-okf-indexes.py` wired into ingest SOP.