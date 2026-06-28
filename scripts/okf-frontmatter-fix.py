#!/usr/bin/env python3
"""Fix OKF-related frontmatter on wiki processed notes."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr)
    sys.exit(1)

VAULT = Path("/Users/vishwapatel/Documents/Obsidian/wiki")
PROCESSED = VAULT / "processed"

RELATED_RE = re.compile(r"^\s*related:\s*(.+)$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def strip_related_from_fm(fm_text: str) -> tuple[str, list[str]]:
    links: list[str] = []
    lines_out = []
    for line in fm_text.splitlines():
        m = re.match(r"^\s*related:\s*(.+)$", line)
        if m:
            val = m.group(1).strip()
            for slug in WIKILINK_RE.findall(val):
                links.append(slug.strip())
            continue
        lines_out.append(line)
    return "\n".join(lines_out), links


def quote_risky_scalar_lines(fm_text: str, keys: tuple[str, ...] = ("summary", "description")) -> str:
    lines = fm_text.splitlines()
    out = []
    for line in lines:
        matched = False
        for key in keys:
            m = re.match(rf"^(\s*{re.escape(key)}:\s*)(.+)$", line)
            if m:
                prefix, val = m.group(1), m.group(2).strip()
                if val and val[0] not in "\"'":
                    if ":" in val or val.startswith("[") or ">" in val:
                        val = val.replace("\\", "\\\\").replace('"', '\\"')
                        line = f'{prefix}"{val}"'
                matched = True
                break
        out.append(line)
    return "\n".join(out)


def parse_frontmatter(text: str) -> tuple[dict | None, str, str | None, list[str]]:
    if not text.startswith("---"):
        return None, text, "no opening ---", []
    end = text.find("---", 3)
    if end < 0:
        return None, text, "no closing ---", []
    fm_text = text[3:end]
    body = text[end + 3 :]
    extracted_links, fm_text = [], fm_text
    fm_text, extracted_links = strip_related_from_fm(fm_text)
    fm_text = quote_risky_scalar_lines(fm_text)
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return None, text, f"yaml: {e}", extracted_links
    if fm is None:
        fm = {}
    if not isinstance(fm, dict):
        return None, text, "frontmatter not a dict", extracted_links
    return fm, body, None, extracted_links


def rebuild_file(fm: dict, body: str) -> str:
    dumped = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    if not dumped.endswith("\n"):
        dumped += "\n"
    return "---\n" + dumped + "---" + body


def ensure_related_in_body(body: str, slugs: list[str]) -> str:
    if not slugs:
        return body
    existing = set(WIKILINK_RE.findall(body))
    to_add = [s for s in slugs if s not in existing]
    if not to_add:
        return body
    block = "## Related\n\n" + "\n".join(f"- [[{s}]]" for s in to_add) + "\n"
    if "## Related" in body:
        return body + "\n" + "\n".join(f"- [[{s}]]" for s in to_add) + "\n"
    return body.rstrip() + "\n\n" + block


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
    tags = fm.get("tags") or []
    if isinstance(tags, list):
        tagset = {str(x).lower() for x in tags}
        if "personal-project" in tagset or "experiment" in tagset:
            return "concept"
    return "bookmark"


def main() -> None:
    stats = {
        "fixed_related": 0,
        "fixed_quote": 0,
        "backfilled_desc": 0,
        "added_type": 0,
        "files_written": 0,
    }
    parse_errors: list[str] = []

    for path in sorted(PROCESSED.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body, err, related_links = parse_frontmatter(text)

        if err:
            parse_errors.append(f"{path.name}: {err}")
            continue

        changed = False
        if related_links:
            new_body = ensure_related_in_body(body, related_links)
            if new_body != body:
                body = new_body
                stats["fixed_related"] += 1
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
    print("remaining_parse_errors", len(parse_errors))
    for line in parse_errors:
        print(" ", line)

    still_bad = missing_both = 0
    for path in sorted(PROCESSED.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, _, err, _ = parse_frontmatter(text)
        if err:
            still_bad += 1
        elif fm and not (fm.get("description") or fm.get("summary")):
            missing_both += 1
    print("still_parse_errors", still_bad)
    print("missing_description_and_summary", missing_both)


if __name__ == "__main__":
    main()