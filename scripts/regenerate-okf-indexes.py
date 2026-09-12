#!/usr/bin/env python3
"""Regenerate OKF navigation artifacts: TAG-INDEX + processed/index.md.

Portable: derives vault root from this file and calls the vault-local
regenerators (no external ~/.hermes dependency).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def main() -> int:
    for label, script in [
        ("TAG-INDEX", SCRIPTS / "regenerate-tag-index.py"),
        ("processed/index", SCRIPTS / "regenerate-processed-index.py"),
    ]:
        if not script.is_file():
            print(f"Missing {script}", file=sys.stderr)
            return 1
        print(f"Running {label}...")
        r = subprocess.run([sys.executable, str(script)])
        if r.returncode != 0:
            return r.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
