#!/usr/bin/env python3
"""finalize-ingest.py — the post-ingest SOP as ONE idempotent command.

Every ingest MUST end by calling this so indexes and the changelog never drift
again (the historical 6h cron ingested but skipped these steps — the root
problem this solves). Runs, in order:

  1. okf-frontmatter-fix.py         — move any stray invalid `related:` YAML
                                       out of frontmatter into a body ## Related
  2. build-search-index.py          — rebuild INDEX.tsv (the retrieval index)
  3. regenerate-tag-index.py        — rebuild entities/TAG-INDEX.md
  4. regenerate-processed-index.py  — rebuild processed/index.md
  5. append-okf-log.py "<message>"  — append a dated changelog entry to log.md

That is: rebuild INDEX.tsv + regenerate all three index artifacts
(INDEX.tsv, TAG-INDEX.md, processed/index.md) + fix stray related YAML + log.

Idempotent: safe to run repeatedly; a clean vault is a no-op except the log
dedupes on message. Stdlib only itself — it *orchestrates* the existing vault
scripts via subprocess. Those helpers (okf-frontmatter-fix / regenerate-*)
require PyYAML on the machine that runs the cron (see docs/automation.md).

Default is --dry-run (prints the ordered plan, writes NOTHING). Pass --apply to
execute. Optional --message/-m sets the changelog line.

    python3 scripts/finalize-ingest.py            # dry-run: show the plan
    python3 scripts/finalize-ingest.py --apply -m "Ingest: <title> (<source>)"
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
VAULT = SCRIPTS.parent

DEFAULT_MESSAGE = "Maintenance: finalize-ingest (INDEX.tsv + TAG-INDEX + processed/index + log)"


def steps(message: str) -> list[tuple[str, list[str]]]:
    py = sys.executable
    return [
        ("Fix stray related: YAML -> body ## Related",
         [py, str(SCRIPTS / "okf-frontmatter-fix.py")]),
        ("Rebuild INDEX.tsv (retrieval index)",
         [py, str(SCRIPTS / "build-search-index.py")]),
        ("Regenerate entities/TAG-INDEX.md",
         [py, str(SCRIPTS / "regenerate-tag-index.py")]),
        ("Regenerate processed/index.md",
         [py, str(SCRIPTS / "regenerate-processed-index.py")]),
        ("Append changelog entry to log.md",
         [py, str(SCRIPTS / "append-okf-log.py"), message]),
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description="Post-ingest SOP as one idempotent command.")
    ap.add_argument("--apply", action="store_true", help="execute the steps (default: dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan, write nothing (default)")
    ap.add_argument("-m", "--message", default=DEFAULT_MESSAGE, help="changelog line for log.md")
    args = ap.parse_args()
    apply = args.apply and not args.dry_run

    plan = steps(args.message)
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"finalize-ingest [{mode}] — {len(plan)} steps, vault={VAULT}")
    for i, (label, argv) in enumerate(plan, 1):
        print(f"  {i}. {label}")
        print(f"       $ {' '.join(argv[1:] if argv[0]==sys.executable else argv)}")

    if not apply:
        print("\nDRY-RUN: nothing was written. Re-run with --apply to execute.")
        return 0

    print()
    for i, (label, argv) in enumerate(plan, 1):
        print(f"==> [{i}/{len(plan)}] {label}")
        r = subprocess.run(argv)
        if r.returncode != 0:
            print(f"STEP FAILED (exit {r.returncode}): {label}", file=sys.stderr)
            return r.returncode
    print("\nfinalize-ingest: all steps complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
