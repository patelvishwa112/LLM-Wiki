#!/usr/bin/env python3
"""Generate processed/index.md — OKF progressive-disclosure catalog for all concepts."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr)
    sys.exit(1)

WIKI = Path("/Users/vishwapatel/Documents/Obsidian/wiki")
PROCESSED = WIKI / "processed"
OUTPUT = PROCESSED / "index.md"


def load_concept(path: Path) -> tuple[str, str, str] | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    slug = path.name
    desc = fm.get("description") or fm.get("summary") or fm.get("title") or slug
    if isinstance(desc, str):
        desc = desc.strip().replace("\n", " ")
    else:
        desc = str(desc)
    if len(desc) > 220:
        desc = desc[:217] + "..."
    typ = str(fm.get("type") or "concept")
    return slug, typ, desc


def main() -> None:
    rows: list[tuple[str, str, str]] = []
    for path in sorted(PROCESSED.glob("*.md")):
        if path.name == "index.md":
            continue
        row = load_concept(path)
        if row:
            rows.append(row)

    lines = [
        "# Processed concepts",
        "",
        f"> Auto-generated OKF catalog. {len(rows)} concepts. Regenerate: "
        "`python3 scripts/regenerate-processed-index.py`",
        "",
        "Markdown paths are bundle-root absolute (`/processed/...`). "
        "Open a concept only when needed.",
        "",
    ]
    for slug, typ, desc in rows:
        # OKF-style path link; escape parens in desc for markdown safety
        safe_desc = desc.replace("]", "\\]")
        lines.append(f"- [{slug}](/processed/{slug}) — *{typ}* — {safe_desc}")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"processed/index.md: {len(rows)} concepts")


if __name__ == "__main__":
    main()