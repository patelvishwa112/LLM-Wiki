#!/usr/bin/env python3
"""maintain.py — single entry point for the self-maintaining vault loop.

Three cadences, one dispatcher, so cron (and the owner) call ONE command:

    python3 scripts/maintain.py finalize [--apply] [-m MSG]   # after every ingest (6h)
    python3 scripts/maintain.py nightly  [--apply]            # nightly reconcile
    python3 scripts/maintain.py weekly   [--apply]            # weekly friction briefing

Each subcommand forwards all remaining args to the matching script, which
defaults to --dry-run and writes only under --apply. See docs/automation.md
for the recommended cron lines. Stdlib only.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

TARGETS = {
    "finalize": "finalize-ingest.py",
    "nightly": "nightly-reconcile.py",
    "weekly": "weekly-friction.py",
}

USAGE = (
    "usage: maintain.py {finalize|nightly|weekly} [--apply] [args...]\n"
    "  finalize  post-ingest SOP: INDEX.tsv + indexes + related-fix + log\n"
    "  nightly   supersession reconcile + orphan/broken-link/as_of health sweep\n"
    "  weekly    contradiction/friction briefing -> briefings/YYYY-MM-DD-friction.md"
)


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(USAGE)
        return 0 if len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help", "help") else 2
    cmd = sys.argv[1]
    if cmd not in TARGETS:
        print(f"maintain.py: unknown cadence {cmd!r}\n\n{USAGE}", file=sys.stderr)
        return 2
    script = SCRIPTS / TARGETS[cmd]
    if not script.is_file():
        print(f"maintain.py: missing {script}", file=sys.stderr)
        return 1
    argv = [sys.executable, str(script)] + sys.argv[2:]
    return subprocess.run(argv).returncode


if __name__ == "__main__":
    raise SystemExit(main())
