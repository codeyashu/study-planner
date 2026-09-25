import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_plan  # noqa: E402
import gen_today  # noqa: E402
import stats  # noqa: E402
import sync_progress  # noqa: E402
from common import SLOTS  # noqa: E402

CURRICULUM = {
    "meta": {"start_date": "2026-09-26", "week1_monday": "2026-09-28", "timezone": "Asia/Kolkata"},
    "phases": [{"id": 0, "name": "Baseline", "weeks": [0]}, {"id": 1, "name": "Foundations", "weeks": [1]}],
    "weeks": [
        {
            "week": 0,
            "phase": 0,
            "theme": "Baseline",
            "tasks": {
                "system-design": [{"title": "Baseline mock", "minutes": 60, "topic": "framework-and-estimation"}],
                "dsa": [{"title": "3 mediums", "minutes": 60}],
                "review": [{"title": "Goals", "minutes": 30}],
            },
        },
        {
            "week": 1,
            "phase": 1,
            "theme": "Foundations",
            "tasks": {
                "agentic-ai": [{"title": f"ai {i}", "minutes": m, "topic": "agent-patterns"} for i, m in enumerate([60, 60, 120])],
                "system-design": [{"title": f"sd {i}", "minutes": 45} for i in range(3)],
                "dsa": [{"title": f"dsa {i}", "minutes": 25} for i in range(5)],
                "architecture": [{"title": "arch", "minutes": 45}, {"title": "adr", "minutes": 30}],
                "python": [{"title": f"py {i}", "minutes": 20} for i in range(3)],
                "java-spring-ai": [{"title": "j1", "minutes": 30}, {"title": "j2", "minutes": 30}],
                "staff-skills": [{"title": "staff", "minutes": 30}],
                "review": [{"title": "review", "minutes": 60}],
            },
        },
    ],
}


def test_assign_days_exact_slots():
    for track, slots in SLOTS.items():
        assert build_plan.assign_days(track, [{}] * len(slots), 1) == slots


def test_assign_days_week0_weekend_only():
    assert set(build_plan.assign_days("dsa", [{}] * 3, 0)) <= {5, 6}


def test_build_plan_ids_dates_and_topics():
    result = build_plan.build(CURRICULUM)
    days = {d["date"]: d for d in result["days"]}
    assert "2026-09-26" in days and days["2026-09-26"]["day_number"] == 1
    # week 1 Saturday carries the 120-min AI build
    sat = days["2026-10-03"]
    assert any(t["id"] == "w01-ai-3" and t["minutes"] == 120 for t in sat["tasks"])
    ids = [t["id"] for d in result["days"] for t in d["tasks"]]
    assert len(ids) == len(set(ids)) == 3 + 20
    ai = next(t for t in sat["tasks"] if t["id"] == "w01-ai-3")
    assert ai["topic_path"] == "tracks/agentic-ai/agent-patterns.md"
    # every weekday of week 1 has work
    assert {dt.date.fromisoformat(d).weekday() for d in days if d >= "2026-09-28"} == set(range(7))


def test_sync_progress_parse_and_apply():
    body = "- [x] `w01-ai-1` **Agentic AI** · 60m\n- [ ] `w01-sd-1` SD\n* [X] `w01-dsa-2` DSA\n- [x] not an id"
    checked, unchecked = sync_progress.parse_issue(body)
    assert checked == {"w01-ai-1", "w01-dsa-2"} and unchecked == {"w01-sd-1"}
    progress, added, removed = sync_progress.apply({"completed": {"w01-sd-1": "2026-09-27"}}, checked, unchecked, "2026-09-28")
    assert added == 2 and removed == 1
    assert progress["completed"] == {"w01-ai-1": "2026-09-28", "w01-dsa-2": "2026-09-28"}


def test_stats_streak_and_totals():
    days = build_plan.build(CURRICULUM)["days"]
    completed = {"w00-sd-1": "2026-09-26", "w00-dsa-1": "2026-09-27", "w01-ai-1": "2026-09-28"}
    s = stats.compute(days, completed, dt.date(2026, 9, 28))
    assert s["streak"] == 3 and s["longest_streak"] == 3
    assert s["total"]["done"] == 3 and s["total"]["planned"] == 23
    assert s["by_track"]["agentic-ai"]["done"] == 1


def test_gen_today_before_start_and_carry_over():
    days = build_plan.build(CURRICULUM)["days"]
    before = gen_today.render(dt.date(2026, 9, 25), days, {})
    assert "next session in 1 day" in before["page"] and before["issue_title"] == ""
    mon = gen_today.render(dt.date(2026, 9, 28), days, {"w00-sd-1": "2026-09-26"})
    assert mon["issue_title"].startswith("Day 3 ")
    assert "`w01-sd-1`" in mon["issue_body"]
    # unfinished week-0 tasks carried over, completed one not
    assert "w00-dsa-1" in mon["issue_body"] and "w00-sd-1" not in mon["issue_body"]
