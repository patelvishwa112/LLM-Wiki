#!/usr/bin/env python3
"""Append a dated entry to vault log.md (OKF changelog)."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path("/Users/vishwapatel/Documents/Obsidian/wiki")
LOG = WIKI / "log.md"
HEADER = "# Changelog\n\nOKF bundle history (newest sections at top).\n\n"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: append-okf-log.py <message>", file=sys.stderr)
        sys.exit(1)
    message = " ".join(sys.argv[1:]).strip()
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    section = f"## {day}\n\n- {message}\n\n"

    if LOG.is_file():
        text = LOG.read_text(encoding="utf-8")
        if not text.startswith("# Changelog"):
            text = HEADER + text
    else:
        text = HEADER

    # Insert new section after header block
    parts = text.split("\n\n", 2)
    if len(parts) >= 2 and parts[0].startswith("# Changelog"):
        rest = text[len(parts[0]) :].lstrip("\n")
        if rest.startswith("OKF bundle"):
            idx = text.find("\n\n", text.find("OKF bundle"))
            if idx == -1:
                new_text = text.rstrip() + "\n\n" + section
            else:
                new_text = text[: idx + 2] + section + text[idx + 2 :]
        else:
            new_text = parts[0] + "\n\n" + section + text[len(parts[0]) + 2 :]
    else:
        new_text = HEADER + section + text

    # Dedupe same-day duplicate message
    if f"- {message}\n" in new_text and new_text.count(f"## {day}") >= 1:
        print("log.md: entry already present")
        return

    LOG.write_text(new_text, encoding="utf-8")
    print(f"log.md: appended ({day})")


if __name__ == "__main__":
    main()