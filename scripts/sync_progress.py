"""Sync ticked task ids from a daily GitHub issue body into data/progress.yml.

The issue body contains lines like:  - [x] `w01-ai-1` **Agentic AI** · 60m — ...
Usage (Action): ISSUE_BODY="$BODY" ISSUE_DATE=2026-09-28 uv run python scripts/sync_progress.py
       (local): uv run python scripts/sync_progress.py --body-file issue.md --date 2026-09-28
       (manual): uv run python scripts/sync_progress.py --done w01-ai-1 w01-sd-1
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from common import DATA, dump_yaml, load_yaml, today_ist  # noqa: E402

LINE = re.compile(r"^\s*[-*]\s+\[(?P<box>[ xX])\]\s+`(?P<id>w\d{2}-[a-z]+-\d+)`", re.MULTILINE)


def parse_issue(body: str) -> tuple[set[str], set[str]]:
    """Return (checked_ids, unchecked_ids)."""
    checked, unchecked = set(), set()
    for m in LINE.finditer(body or ""):
        (checked if m.group("box").lower() == "x" else unchecked).add(m.group("id"))
    return checked, unchecked


def apply(progress: dict, checked: set[str], unchecked: set[str], date: str) -> tuple[dict, int, int]:
    completed = dict(progress.get("completed") or {})
    added = removed = 0
    for tid in sorted(checked):
        if tid not in completed:
            completed[tid] = date
            added += 1
    for tid in sorted(unchecked):
        if tid in completed:
            del completed[tid]
            removed += 1
    progress = {**progress, "completed": dict(sorted(completed.items()))}
    return progress, added, removed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--body-file")
    ap.add_argument("--date")
    ap.add_argument("--done", nargs="*", default=[])
    args = ap.parse_args()
    date = args.date or os.environ.get("ISSUE_DATE") or today_ist().isoformat()
    date = date[:10]
    body = Path(args.body_file).read_text(encoding="utf-8") if args.body_file else os.environ.get("ISSUE_BODY", "")
    checked, unchecked = parse_issue(body)
    checked |= set(args.done)
    path = DATA / "progress.yml"
    progress = load_yaml(path, {}) or {}
    progress.setdefault("notes", "Completed task ids -> date (YYYY-MM-DD). Synced from daily issues.")
    progress, added, removed = apply(progress, checked, unchecked, date)
    dump_yaml(path, progress)
    print(f"progress: +{added} -{removed} (total {len(progress['completed'])})")


if __name__ == "__main__":
    main()
