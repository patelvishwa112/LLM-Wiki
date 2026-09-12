#!/usr/bin/env python3
"""Fix OKF-related frontmatter on wiki processed notes.

- Moves any `related:` wikilinks OUT of YAML frontmatter into a body `## Related`
  section (frontmatter `related:` breaks PyYAML/TAG-INDEX per CLAUDE.md / SCHEMA.v2).
  Handles every observed form: inline `related: [[a]], [[b]]`, block lists of
  quoted `- '[[a]]'`, and malformed nested lists `- - - slug` (no brackets).
- Backfills `description` from `summary`/H1 when missing.
- Backfills `type` when missing.

Portable: vault root derived from this file's location (works on any checkout).
Idempotent: re-running makes no further changes once frontmatter is clean.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr)
    sys.exit(1)

VAULT = Path(__file__).resolve().parent.parent
PROCESSED = VAULT / "processed"

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def slug_from_leaf(leaf: str) -> str | None:
    """Extract a link target from a related-list leaf scalar.

    "[[wtf-is-a-loop]]" -> "wtf-is-a-loop"; "[[Bookmarks Index]]" -> "Bookmarks Index";
    bare "claude-artifacts" -> "claude-artifacts". Strips path prefixes and #/| suffixes.
    """
    if leaf is None:
        return None
    s = str(leaf).strip().strip("'\"").strip()
    if not s:
        return None
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1)
    s = s.split("|")[0].split("#")[0].strip()
    # drop a processed/ or raw/ path prefix if present, keep the note name
    if "/" in s:
        s = s.rsplit("/", 1)[-1]
    if s.endswith(".md"):
        s = s[:-3]
    s = s.strip()
    return s or None


def collect_leaves(val) -> list[str]:
    """Recursively collect leaf strings from a parsed `related` value
    (str, list, or nested list)."""
    out: list[str] = []
    if val is None:
        return out
    if isinstance(val, str):
        # inline could hold multiple [[..]] links
        links = WIKILINK_RE.findall(val)
        if links:
            out.extend(links)
        else:
            out.append(val)
    elif isinstance(val, (list, tuple)):
        for item in val:
            out.extend(collect_leaves(item))
    else:
        out.append(str(val))
    return out


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text, "no opening ---"
    end = text.find("\n---", 3)
    if end < 0:
        return None, text, "no closing ---"
    return text[3:end], text[end + 4:], None


def rebuild_file(fm: dict, body: str) -> str:
    dumped = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    if not dumped.endswith("\n"):
        dumped += "\n"
    return "---\n" + dumped + "---" + body


def ensure_related_in_body(body: str, slugs: list[str]) -> str:
    if not slugs:
        return body
    existing = set(WIKILINK_RE.findall(body))
    to_add = [s for s in slugs if s and s not in existing]
    # dedupe preserving order
    seen = set()
    to_add = [s for s in to_add if not (s in seen or seen.add(s))]
    if not to_add:
        return body
    additions = "\n".join(f"- [[{s}]]" for s in to_add)
    if "## Related" in body:
        return body.rstrip() + "\n" + additions + "\n"
    return body.rstrip() + "\n\n## Related\n\n" + additions + "\n"


def infer_description(fm: dict, body: str) -> str | None:
    if fm.get("description") and str(fm.get("description")).strip():
        return None
    if fm.get("summary") and str(fm.get("summary")).strip():
        return str(fm["summary"]).strip()
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()[:500]
    return None


def infer_type(fm: dict) -> str:
    t = fm.get("type")
    if t:
        return str(t)
    return "bookmark"


def main() -> None:
    stats = {"moved_related": 0, "backfilled_desc": 0, "added_type": 0, "files_written": 0}
    parse_errors: list[str] = []

    for path in sorted(PROCESSED.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm_text, body, err = split_frontmatter(text)
        if err:
            parse_errors.append(f"{path.name}: {err}")
            continue
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError as e:
            parse_errors.append(f"{path.name}: yaml: {str(e).splitlines()[0][:80]}")
            continue
        if fm is None:
            fm = {}
        if not isinstance(fm, dict):
            parse_errors.append(f"{path.name}: frontmatter not a dict")
            continue

        changed = False

        if "related" in fm:
            leaves = collect_leaves(fm.pop("related"))
            slugs = [s for s in (slug_from_leaf(l) for l in leaves) if s]
            new_body = ensure_related_in_body(body, slugs)
            if new_body != body:
                body = new_body
            stats["moved_related"] += 1
            changed = True

        if not fm.get("type"):
            fm["type"] = infer_type(fm)
            stats["added_type"] += 1
            changed = True

        desc = infer_description(fm, body)
        if desc:
            fm["description"] = desc
            stats["backfilled_desc"] += 1
            changed = True

        if changed:
            path.write_text(rebuild_file(fm, body), encoding="utf-8")
            stats["files_written"] += 1

    print(stats)
    print("parse_errors", len(parse_errors))
    for line in parse_errors:
        print(" ", line)

    # verify: no remaining related: in frontmatter, all parse clean
    still_related = still_bad = 0
    for path in sorted(PROCESSED.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm_text, _, err = split_frontmatter(text)
        if err:
            still_bad += 1
            continue
        try:
            fm = yaml.safe_load(fm_text) or {}
        except yaml.YAMLError:
            still_bad += 1
            continue
        if isinstance(fm, dict) and "related" in fm:
            still_related += 1
    print("remaining related-in-frontmatter:", still_related)
    print("remaining parse-errors:", still_bad)


if __name__ == "__main__":
    main()
