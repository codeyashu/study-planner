"""Build the day-by-day plan and generated roadmap pages from data/curriculum.yml.

Outputs:
  data/plan.yml                      day-by-day tasks with stable ids
  docs/roadmap/weeks/week-NN.md      one page per week
  docs/roadmap/weeks/.nav.yml        week ordering
  includes/weeks-table.md            overview table (snippet for roadmap/index.md)
  includes/phases.md                 phase goals + gates (snippet for roadmap/phases.md)
  docs/tracks/<track>/.nav.yml       topic ordering from data/topics.yml
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from common import (  # noqa: E402
    DATA,
    DAY_NAMES,
    DOCS,
    INCLUDES,
    SLOTS,
    TRACK_ABBR,
    TRACK_LABEL,
    TRACK_ORDER,
    dump_yaml,
    load_yaml,
    parse_date,
    resolve_topic,
)


def assign_days(track: str, tasks: list[dict], week: int) -> list[int]:
    """Return a weekday index for each task of a track."""
    n = len(tasks)
    if week == 0:
        # Week 0 is the Sat/Sun baseline weekend: alternate Saturday / Sunday.
        return [5 if i % 2 == 0 else 6 for i in range(n)]
    slots = SLOTS.get(track, [6])
    if n <= len(slots):
        # Spread fewer tasks evenly over the available slots.
        if n == len(slots):
            return list(slots)
        step = len(slots) / n
        return [slots[int(i * step)] for i in range(n)]
    # More tasks than slots: cycle through them.
    return [slots[i % len(slots)] for i in range(n)]


def week_start(meta: dict, week: int) -> dt.date:
    monday1 = parse_date(meta["week1_monday"])
    return monday1 + dt.timedelta(weeks=week - 1)


def build(curriculum: dict) -> dict:
    meta = curriculum["meta"]
    start = parse_date(meta["start_date"])
    days: dict[str, dict] = {}
    weeks_out = []
    for w in curriculum["weeks"]:
        wk = int(w["week"])
        monday = week_start(meta, wk)
        week_tasks = []
        for track in TRACK_ORDER:
            tasks = (w.get("tasks") or {}).get(track) or []
            for i, (task, wd) in enumerate(zip(tasks, assign_days(track, tasks, wk)), start=1):
                date = monday + dt.timedelta(days=wd)
                tid = f"w{wk:02d}-{TRACK_ABBR[track]}-{i}"
                topic_meta = resolve_topic(track, task.get("topic"))
                item = {
                    "id": tid,
                    "track": track,
                    "title": task["title"],
                    "minutes": int(task.get("minutes", 30)),
                    "kind": task.get("kind", "learn"),
                }
                if task.get("topic"):
                    item["topic"] = task["topic"]
                if topic_meta:
                    item["topic_path"] = topic_meta["path"]
                    item["topic_title"] = topic_meta["title"]
                if task.get("resource"):
                    item["resource"] = task["resource"]
                key = date.isoformat()
                day = days.setdefault(
                    key,
                    {
                        "date": key,
                        "week": wk,
                        "weekday": DAY_NAMES[date.weekday()],
                        "day_number": (date - start).days + 1,
                        "phase": w.get("phase"),
                        "theme": w.get("theme", ""),
                        "tasks": [],
                    },
                )
                day["tasks"].append(item)
                week_tasks.append({**item, "date": key})
        weeks_out.append({**{k: v for k, v in w.items() if k != "tasks"}, "monday": monday, "items": week_tasks})
    ordered = [days[k] for k in sorted(days)]
    for d in ordered:
        d["tasks"].sort(key=lambda t: TRACK_ORDER.index(t["track"]))
        d["total_minutes"] = sum(t["minutes"] for t in d["tasks"])
    return {"days": ordered, "weeks": weeks_out}


def task_line(t: dict, rel_prefix: str) -> str:
    parts = [f"- [ ] **{TRACK_LABEL[t['track']]}** · {t['minutes']} min · {t['title']}"]
    if t.get("topic_path"):
        parts.append(f"→ [{t['topic_title']}]({rel_prefix}{t['topic_path']})")
    if t.get("resource"):
        parts.append(f"· [resource]({t['resource']})")
    parts.append(f"<small>`{t['id']}`</small>")
    return " ".join(parts)


def fmt_minutes(m: int) -> str:
    return f"{m // 60}h {m % 60:02d}m" if m >= 60 else f"{m}m"


def render_week(w: dict, phases: dict[int, dict]) -> str:
    wk = int(w["week"])
    phase = phases.get(w.get("phase"), {})
    total = sum(t["minutes"] for t in w["items"])
    lines = [
        "---",
        f"title: Week {wk:02d} — {w.get('theme', '')}",
        f"week: {wk}",
        "generated: true",
        "---",
        "",
        f"# Week {wk:02d} — {w.get('theme', '')}",
        "",
        '!!! abstract "At a glance"',
        f"    **Phase {w.get('phase')}:** {phase.get('name', '')} · **Starts:** {w['monday']:%a %d %b %Y}"
        f" · **Planned:** {fmt_minutes(total)}{' · **Light week**' if w.get('light') else ''}",
        "",
        f"    **Build:** {w.get('project', '—')}",
    ]
    if w.get("checkpoint"):
        lines += ["", f'!!! warning "Interview checkpoint: {w["checkpoint"]}"',
                  "    Run the full mock loop and score it with the [rubric](../../interviews/rubric.md)."]
    lines += ["", "## By day", ""]
    by_date: dict[str, list[dict]] = {}
    for t in w["items"]:
        by_date.setdefault(t["date"], []).append(t)
    for date in sorted(by_date):
        d = dt.date.fromisoformat(date)
        items = sorted(by_date[date], key=lambda t: TRACK_ORDER.index(t["track"]))
        lines.append(f"### {DAY_NAMES[d.weekday()]} {d:%d %b} · {fmt_minutes(sum(t['minutes'] for t in items))}")
        lines.append("")
        lines += [task_line(t, "../../") for t in items]
        lines.append("")
    lines += ["## By track", "", "| Track | Tasks | Time |", "|---|---|---|"]
    for track in TRACK_ORDER:
        its = [t for t in w["items"] if t["track"] == track]
        if its:
            lines.append(f"| {TRACK_LABEL[track]} | {len(its)} | {fmt_minutes(sum(t['minutes'] for t in its))} |")
    lines += [
        "",
        "## End-of-week",
        "",
        "- [ ] Weekly retro written in `docs/log/retros/` (template: [retro](../../log/retro-template.md))",
        "- [ ] Flashcards / explain-it-back done for this week's topics",
        "- [ ] Progress synced (close the daily GitHub issues)",
        "",
    ]
    return "\n".join(lines)


def render_weeks_table(weeks: list[dict], phases: dict[int, dict]) -> str:
    rows = ["| Week | Starts | Phase | Theme | Build | Checkpoint |", "|---|---|---|---|---|---|"]
    for w in weeks:
        wk = int(w["week"])
        rows.append(
            f"| [W{wk:02d}](weeks/week-{wk:02d}.md) | {w['monday']:%d %b} | {w.get('phase')} · "
            f"{phases.get(w.get('phase'), {}).get('name', '')} | {w.get('theme', '')}{' *(light)*' if w.get('light') else ''} | "
            f"{w.get('project', '')} | {w.get('checkpoint') or ''} |"
        )
    return "\n".join(rows) + "\n"


def render_phases(curriculum: dict) -> str:
    out = []
    for p in curriculum.get("phases", []):
        weeks = p.get("weeks", [])
        span = f"Week {weeks[0]}" if len(weeks) == 1 else f"Weeks {weeks[0]}–{weeks[-1]}"
        out += [f"## Phase {p['id']} — {p['name']}", "", f"**{span}** · {p.get('goal', '')}", "", "**Gate (exit criteria):**", ""]
        out += [f"- [ ] {g}" for g in p.get("gate", [])]
        out.append("")
    return "\n".join(out)


def build_track_navs() -> None:
    topics = load_yaml(DATA / "topics.yml", {"tracks": {}})
    for track, spec in topics["tracks"].items():
        tdir = DOCS / "tracks" / track
        tdir.mkdir(parents=True, exist_ok=True)
        nav = ["index.md"] + [f"{t['slug']}.md" for t in spec.get("topics", [])]
        if spec.get("case_studies"):
            (tdir / "case-studies").mkdir(exist_ok=True)
            nav.append({"Case studies": "case-studies"})
            cs_nav = [f"{t['slug']}.md" for t in spec["case_studies"]]
            dump_yaml(tdir / "case-studies" / ".nav.yml", {"nav": cs_nav})
        nav.append({"Question bank": "questions.md"})
        dump_yaml(tdir / ".nav.yml", {"nav": nav})


def main() -> None:
    curriculum = load_yaml(DATA / "curriculum.yml")
    if not curriculum:
        sys.exit("data/curriculum.yml missing")
    result = build(curriculum)
    phases = {p["id"]: p for p in curriculum.get("phases", [])}
    dump_yaml(DATA / "plan.yml", {"generated": True, "meta": curriculum["meta"], "days": result["days"]})

    weeks_dir = DOCS / "roadmap" / "weeks"
    weeks_dir.mkdir(parents=True, exist_ok=True)
    for old in weeks_dir.glob("week-*.md"):
        old.unlink()
    for w in result["weeks"]:
        (weeks_dir / f"week-{int(w['week']):02d}.md").write_text(render_week(w, phases), encoding="utf-8")
    dump_yaml(weeks_dir / ".nav.yml", {"nav": [f"week-{int(w['week']):02d}.md" for w in result["weeks"]]})

    INCLUDES.mkdir(exist_ok=True)
    (INCLUDES / "weeks-table.md").write_text(render_weeks_table(result["weeks"], phases), encoding="utf-8")
    (INCLUDES / "phases.md").write_text(render_phases(curriculum), encoding="utf-8")
    build_track_navs()
    n_tasks = sum(len(d["tasks"]) for d in result["days"])
    print(f"plan: {len(result['days'])} days, {len(result['weeks'])} weeks, {n_tasks} tasks")


if __name__ == "__main__":
    main()
