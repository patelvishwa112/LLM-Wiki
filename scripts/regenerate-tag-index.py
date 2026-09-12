#!/usr/bin/env python3
"""Regenerate entities/TAG-INDEX.md — master tag -> processed-note cross-reference.

Portable (vault root derived from this file). Reads canonical tags from every
processed/*.md frontmatter and groups notes by tag into High (5+), Mid (2-4),
and Single-use tiers. Idempotent. Run: python3 scripts/regenerate-tag-index.py
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML required")

WIKI = Path(__file__).resolve().parent.parent
PROCESSED = WIKI / "processed"
OUTPUT = WIKI / "entities" / "TAG-INDEX.md"


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def main() -> None:
    tag_notes: dict[str, set[str]] = defaultdict(set)
    n_notes = 0
    for path in sorted(PROCESSED.glob("*.md")):
        if path.name == "index.md":
            continue
        n_notes += 1
        fm = frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        for t in tags:
            t = str(t).strip()
            if t:
                tag_notes[t].add(path.stem)

    high = sorted((t for t, s in tag_notes.items() if len(s) >= 5))
    mid = sorted((t for t, s in tag_notes.items() if 2 <= len(s) <= 4))
    single = sorted((t for t, s in tag_notes.items() if len(s) == 1))

    L: list[str] = []
    L.append("# Tag Index — Master Cross-Reference")
    L.append("")
    L.append("> Auto-generated. Maps every canonical tag to all processed notes using it.")
    L.append("> Regenerate: `python3 scripts/regenerate-tag-index.py`")
    L.append("")
    L.append(f"> {len(tag_notes)} canonical tags across {n_notes} processed notes.")
    L.append("")

    def block(tag: str) -> None:
        notes = sorted(tag_notes[tag])
        L.append(f"### {tag} ({len(notes)})")
        L.append("")
        for s in notes:
            L.append(f"- [[{s}]]")
        L.append("")

    L.append("## High-Frequency Tags (5+ notes)")
    L.append("")
    for t in high:
        block(t)
    L.append("## Mid-Frequency Tags (2-4 notes)")
    L.append("")
    for t in mid:
        block(t)
    L.append("## Single-Use Tags")
    L.append("")
    for t in single:
        s = next(iter(tag_notes[t]))
        L.append(f"- **{t}** — [[{s}]]")
    L.append("")

    OUTPUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"TAG-INDEX.md: {len(tag_notes)} tags, {n_notes} notes -> {OUTPUT}")


if __name__ == "__main__":
    main()
