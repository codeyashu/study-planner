"""Generate the Today page, the dashboard snippet and the daily GitHub issue body.

Usage: uv run python scripts/gen_today.py [--date YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from common import BUILD, DATA, DOCS, INCLUDES, TRACK_LABEL, load_yaml, today_ist  # noqa: E402

SITE = "https://codeyashu.github.io/study-planner/"
CARRY_OVER_DAYS = 7
CARRY_OVER_MAX = 8


def load_plan() -> list[dict]:
    plan = load_yaml(DATA / "plan.yml", {"days": []})
    return plan.get("days", [])


def load_completed() -> dict[str, str]:
    progress = load_yaml(DATA / "progress.yml", {}) or {}
    return progress.get("completed", {}) or {}


def site_url(path: str) -> str:
    """docs-relative .md path -> published URL (use_directory_urls)."""
    p = path[:-3] if path.endswith(".md") else path
    if p.endswith("index"):
        p = p[: -len("index")]
    return SITE + p.rstrip("/") + "/"


def latest_digest() -> tuple[str, str] | None:
    posts = sorted((DOCS / "digest" / "posts").glob("*.md"))
    if not posts:
        return None
    post = posts[-1]
    title = post.stem
    for line in post.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    return title, f"digest/{post.stem}/"


def select(days: list[dict], date: dt.date, completed: dict[str, str]):
    by_date = {d["date"]: d for d in days}
    today = by_date.get(date.isoformat())
    upcoming = None
    if today is None:
        future = [d for d in days if d["date"] > date.isoformat()]
        upcoming = future[0] if future else None
    carry = []
    for back in range(CARRY_OVER_DAYS, 0, -1):
        d = by_date.get((date - dt.timedelta(days=back)).isoformat())
        if d:
            carry += [{**t, "date": d["date"]} for t in d["tasks"] if t["id"] not in completed]
    return today, upcoming, carry[-CARRY_OVER_MAX:]


def md_task(t: dict, completed: dict[str, str], rel: str, with_date: bool = False) -> str:
    box = "x" if t["id"] in completed else " "
    s = f"- [{box}] **{TRACK_LABEL.get(t['track'], t['track'])}** · {t['minutes']} min · {t['title']}"
    if t.get("topic_path"):
        s += f" → [{t['topic_title']}]({rel}{t['topic_path']})"
    if t.get("resource"):
        s += f" · [resource]({t['resource']})"
    if with_date:
        s += f" · *from {t['date']}*"
    return s + f" <small>`{t['id']}`</small>"


def issue_task(t: dict, with_date: bool = False) -> str:
    s = f"- [ ] `{t['id']}` **{TRACK_LABEL.get(t['track'], t['track'])}** · {t['minutes']}m — {t['title']}"
    if t.get("topic_path"):
        s += f" ([topic]({site_url(t['topic_path'])}))"
    if t.get("resource"):
        s += f" ([resource]({t['resource']}))"
    if with_date:
        s += f" — *carried from {t['date']}*"
    return s


def render(date: dt.date, days: list[dict], completed: dict[str, str]) -> dict[str, str]:
    today, upcoming, carry = select(days, date, completed)
    digest = latest_digest()
    head = [
        "---",
        "title: Today",
        "hide: [navigation]",
        "generated: true",
        "---",
        "",
        f"# Today · {date:%A %d %B %Y}",
        "",
    ]
    body: list[str] = []
    snippet: list[str] = []
    if today:
        done = sum(1 for t in today["tasks"] if t["id"] in completed)
        body += [
            f'!!! abstract "Day {today["day_number"]} · Week {today["week"]} · Phase {today["phase"]} — {today["theme"]}"',
            f"    Planned **{today['total_minutes']} min** · {done}/{len(today['tasks'])} done · "
            f"[Week page](roadmap/weeks/week-{today['week']:02d}.md)",
            "",
            "## Tasks",
            "",
        ]
        body += [md_task(t, completed, "") for t in today["tasks"]]
        snippet += [f"**Day {today['day_number']} · Week {today['week']} — {today['theme']}** · {today['total_minutes']} min", ""]
        snippet += [md_task(t, completed, "") for t in today["tasks"]]
    elif upcoming:
        start = dt.date.fromisoformat(upcoming["date"])
        n = (start - date).days
        body += [
            f'!!! info "No tasks scheduled today — next session in {n} day{"s" if n != 1 else ""} ({start:%a %d %b})"',
            f"    Week {upcoming['week']} · {upcoming['theme']}",
            "",
            f"## Coming up: {upcoming['weekday']} {start:%d %b}",
            "",
        ]
        body += [md_task(t, completed, "") for t in upcoming["tasks"]]
        snippet += [f"**Next: {upcoming['weekday']} {start:%d %b} — {upcoming['theme']}**", ""]
        snippet += [md_task(t, completed, "") for t in upcoming["tasks"]]
    else:
        body += ['!!! success "Roadmap complete"', "    All scheduled weeks are behind you. Time to pick the next mountain.", ""]
        snippet += ["Roadmap complete."]
    if carry:
        body += ["", "## Catch-up (unfinished from the last 7 days)", ""]
        body += [md_task(t, completed, "", with_date=True) for t in carry]
        snippet += ["", f"*{len(carry)} unfinished task(s) from the last 7 days — see [Today](today.md).*"]
    if digest:
        body += ["", "## Today's digest", "", f"Latest: **{digest[0]}** — read it on the [digest page](digest/index.md)."]
    body += [
        "",
        "## Daily routine",
        "",
        "1. Skim the [digest](digest/index.md) and the [feed](reading/feed.md) — 10 min max.",
        "2. Do the tasks above in order; timebox each.",
        "3. Answer 3 questions from today's topic out loud (explain-it-back).",
        "4. Tick boxes in today's GitHub issue *Day N* and close it — progress syncs automatically.",
        "",
        f"<small>Generated {dt.datetime.now().astimezone():%Y-%m-%d %H:%M %Z} by `scripts/gen_today.py`.</small>",
        "",
    ]

    issue_title = ""
    issue_body = ""
    if today:
        issue_title = f"Day {today['day_number']} · {date:%a %d %b} · W{today['week']:02d} — {today['theme']}"
        lines = [
            f"**Phase {today['phase']} · Week {today['week']} · {today['total_minutes']} min planned**",
            "",
            f"Today page: {SITE}today/ · Week: {SITE}roadmap/weeks/week-{today['week']:02d}/",
            "",
            "### Tasks",
            *[issue_task(t) for t in today["tasks"]],
        ]
        if carry:
            lines += ["", "### Catch-up", *[issue_task(t, with_date=True) for t in carry]]
        lines += ["", "---", "Tick what you finished, then close the issue. Ticked ids sync to `data/progress.yml`."]
        issue_body = "\n".join(lines) + "\n"

    return {
        "page": "\n".join(head + body),
        "snippet": "\n".join(snippet) + "\n",
        "issue_title": issue_title,
        "issue_body": issue_body,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="YYYY-MM-DD (default: today in IST)")
    args = ap.parse_args()
    date = dt.date.fromisoformat(args.date) if args.date else today_ist()
    out = render(date, load_plan(), load_completed())
    (DOCS / "today.md").write_text(out["page"], encoding="utf-8")
    INCLUDES.mkdir(exist_ok=True)
    (INCLUDES / "today-snippet.md").write_text(out["snippet"], encoding="utf-8")
    BUILD.mkdir(exist_ok=True)
    (BUILD / "issue_title.txt").write_text(out["issue_title"], encoding="utf-8")
    (BUILD / "issue_body.md").write_text(out["issue_body"], encoding="utf-8")
    print(f"today: {date} · issue: {out['issue_title'] or '(none)'}")


if __name__ == "__main__":
    main()
