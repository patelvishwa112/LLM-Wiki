#!/usr/bin/env python3
"""Build INDEX.tsv — a compact, greppable retrieval index for the vault.

Walks processed/*.md and entities/*.md, reads YAML frontmatter with a tiny
stdlib-only parser (no PyYAML dependency), and emits one tab-separated row per
note. This TSV is the grep/score target for the retrieval protocol
(see docs/retrieval-protocol.md); the agent scores rows here instead of
opening 500+ note files.

Columns:  slug \\t type \\t status \\t date \\t tags \\t description

- slug        vault-relative path, ready to open (e.g. processed/foo.md)
- type        frontmatter `type` (bookmark|article|concept|entity|...)
- status      T3 temporal field; empty == unspecified (treat as current)
- date        `date` else `ingested` else `as_of` else ""  (YYYY-MM-DD)
- tags        comma-joined tag list (controlled set once T2 lands; free today)
- description `description` else `summary` else `title` else slug, one line

Idempotent: overwrites INDEX.tsv each run. Stdlib only. Run:
    python3 scripts/build-search-index.py
"""
from __future__ import annotations

import re
from pathlib import Path

# Vault root = parent of this scripts/ dir. Portable: works wherever the vault
# is checked out, no hardcoded absolute path.
WIKI = Path(__file__).resolve().parent.parent
SOURCES = ["processed", "entities"]
OUTPUT = WIKI / "INDEX.tsv"

DESC_MAX = 160
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s?(.*)$")
LIST_RE = re.compile(r"^\s*-\s+(.*)$")


def dequote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.strip()


def parse_frontmatter(text: str) -> dict:
    """Minimal YAML-frontmatter parser: top-level scalars, block lists, and
    folded multi-line plain scalars. Good enough for this vault's schema."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm: dict = {}
    cur_key: str | None = None
    cur_is_scalar = False
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        km = KEY_RE.match(line)
        if km and not line[0].isspace():
            key, rest = km.group(1), km.group(2)
            if rest == "":
                fm[key] = []           # pending: list or nested map
                cur_key, cur_is_scalar = key, False
            else:
                fm[key] = dequote(rest)
                cur_key, cur_is_scalar = key, True
            continue
        lm = LIST_RE.match(line)
        if lm and cur_key is not None and not cur_is_scalar:
            item = dequote(lm.group(1))
            if item and not item.startswith("-"):   # skip malformed `- - -`
                fm[cur_key].append(item)             # type: ignore[union-attr]
            continue
        if line[0].isspace() and cur_key is not None and cur_is_scalar:
            fm[cur_key] = (str(fm[cur_key]) + " " + line.strip()).strip()
    return fm


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", str(s)).replace("\t", " ").strip()


def row_for(path: Path) -> tuple[str, str, str, str, str, str] | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if not fm:
        return None
    slug = str(path.relative_to(WIKI))
    typ = clean(fm.get("type") or ("entity" if path.parent.name == "entities" else "concept"))
    status = clean(fm.get("status") or "")
    date = clean(fm.get("date") or fm.get("ingested") or fm.get("as_of") or "")
    tags_val = fm.get("tags") or []
    if isinstance(tags_val, str):
        # inline flow list, e.g. "[models, deepseek]"
        s_ = tags_val.strip()
        tags_val = [dequote(t) for t in s_[1:-1].split(",")] if s_.startswith("[") and s_.endswith("]") else ([dequote(s_)] if s_ else [])
    tags = ",".join(clean(t) for t in tags_val if clean(t))
    desc = fm.get("description") or fm.get("summary") or fm.get("title") or slug
    desc = clean(desc)
    if len(desc) > DESC_MAX:
        desc = desc[: DESC_MAX - 1].rstrip() + "…"
    return slug, typ, status, date, tags, desc


def main() -> None:
    rows = []
    for sub in SOURCES:
        d = WIKI / sub
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            if path.name in {"index.md", "TAG-INDEX.md"}:
                continue
            r = row_for(path)
            if r:
                rows.append(r)
    lines = ["# slug\ttype\tstatus\tdate\ttags\tdescription  (grep -v '^#' to skip this header; regen: python3 scripts/build-search-index.py)"]
    lines += ["\t".join(r) for r in rows]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"INDEX.tsv: {len(rows)} rows, {OUTPUT.stat().st_size} bytes -> {OUTPUT}")


if __name__ == "__main__":
    main()
