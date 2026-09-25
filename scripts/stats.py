"""Compute progress stats -> docs/assets/stats.json (read by the dashboard heatmap)."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from common import DATA, DOCS, TRACK_LABEL, TRACK_ORDER, load_yaml, today_ist  # noqa: E402


def compute(days: list[dict], completed: dict[str, str], today: dt.date) -> dict:
    all_tasks = [(d, t) for d in days for t in d["tasks"]]
    due = [(d, t) for d, t in all_tasks if d["date"] <= today.isoformat()]
    by_track = {}
    for track in TRACK_ORDER:
        planned = [t for _, t in all_tasks if t["track"] == track]
        due_t = [t for d, t in due if t["track"] == track]
        done = [t for t in planned if t["id"] in completed]
        by_track[track] = {
            "label": TRACK_LABEL[track],
            "planned": len(planned),
            "due": len(due_t),
            "done": len(done),
            "minutes_done": sum(t["minutes"] for t in done),
        }
    heat = Counter(str(v)[:10] for v in completed.values())
    # streak: consecutive days (ending today or yesterday) with >= 1 completion
    streak = 0
    cursor = today if heat.get(today.isoformat()) else today - dt.timedelta(days=1)
    while heat.get(cursor.isoformat()):
        streak += 1
        cursor -= dt.timedelta(days=1)
    longest = run = 0
    prev = None
    for day in sorted(heat):
        d = dt.date.fromisoformat(day)
        run = run + 1 if prev and (d - prev).days == 1 else 1
        longest = max(longest, run)
        prev = d
    weeks: dict[int, dict] = {}
    for d, t in all_tasks:
        w = weeks.setdefault(d["week"], {"planned": 0, "done": 0})
        w["planned"] += 1
        w["done"] += t["id"] in completed
    current_week = next((d["week"] for d in days if d["date"] >= today.isoformat()), days[-1]["week"] if days else 0)
    return {
        "generated": today.isoformat(),
        "start": days[0]["date"] if days else None,
        "end": days[-1]["date"] if days else None,
        "current_week": current_week,
        "total": {
            "planned": len(all_tasks),
            "due": len(due),
            "done": sum(1 for _, t in all_tasks if t["id"] in completed),
            "behind": sum(1 for _, t in due if t["id"] not in completed),
        },
        "streak": streak,
        "longest_streak": longest,
        "by_track": by_track,
        "weeks": {str(k): v for k, v in sorted(weeks.items())},
        "heatmap": dict(sorted(heat.items())),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    args = ap.parse_args()
    today = dt.date.fromisoformat(args.date) if args.date else today_ist()
    days = (load_yaml(DATA / "plan.yml", {"days": []}) or {}).get("days", [])
    completed = (load_yaml(DATA / "progress.yml", {}) or {}).get("completed", {}) or {}
    stats = compute(days, completed, today)
    out = DOCS / "assets" / "stats.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(stats, indent=1), encoding="utf-8")
    t = stats["total"]
    print(f"stats: {t['done']}/{t['planned']} done, behind {t['behind']}, streak {stats['streak']}")


if __name__ == "__main__":
    main()
