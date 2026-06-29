#!/usr/bin/env python3
"""Regenerate OKF navigation artifacts: TAG-INDEX + processed/index.md."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WIKI = Path("/Users/vishwapatel/Documents/Obsidian/wiki")
TAG_SCRIPT = Path.home() / ".hermes/skills/note-taking/content-curation/scripts/regenerate-tag-index.py"
PROC_SCRIPT = WIKI / "scripts/regenerate-processed-index.py"


def main() -> int:
    for label, script in [("TAG-INDEX", TAG_SCRIPT), ("processed/index", PROC_SCRIPT)]:
        if not script.is_file():
            print(f"Missing {script}", file=sys.stderr)
            return 1
        print(f"Running {label}...")
        r = subprocess.run([sys.executable, str(script)], cwd=str(WIKI))
        if r.returncode != 0:
            return r.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())