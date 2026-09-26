"""Shared helpers for the study-planner generators."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
INCLUDES = ROOT / "includes"
BUILD = ROOT / "build"
TZ = ZoneInfo("Asia/Kolkata")

TRACK_ORDER = [
    "agentic-ai",
    "system-design",
    "dsa",
    "architecture",
    "python",
    "java-spring-ai",
    "staff-skills",
    "communication",
    "review",
]

TRACK_LABEL = {
    "agentic-ai": "Agentic AI",
    "system-design": "System Design",
    "ai-system-design": "AI System Design",
    "dsa": "DSA",
    "architecture": "Architecture",
    "python": "Python",
    "java-spring-ai": "Java/Spring AI",
    "staff-skills": "Staff+",
    "communication": "Communication",
    "review": "Review",
}

TRACK_ABBR = {
    "agentic-ai": "ai",
    "system-design": "sd",
    "ai-system-design": "aisd",
    "dsa": "dsa",
    "architecture": "arch",
    "python": "py",
    "java-spring-ai": "java",
    "staff-skills": "staff",
    "communication": "comm",
    "review": "rev",
}

# Fixed weekly slots: track -> weekday indexes (0=Mon .. 6=Sun), one per task in order.
SLOTS = {
    "system-design": [0, 4, 6],
    "dsa": [0, 1, 2, 4, 5],
    "python": [0, 2, 4],
    "agentic-ai": [1, 3, 5],
    "architecture": [2, 6],
    "java-spring-ai": [3, 5],
    "staff-skills": [6],
    "communication": [0, 1, 2, 3, 4, 5, 6],
    "review": [6],
}

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def load_yaml(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return default if data is None else data


def dump_yaml(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True, width=120)


def today_ist() -> dt.date:
    return dt.datetime.now(TZ).date()


def parse_date(value) -> dt.date:
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def topic_index() -> dict[str, dict]:
    """Map 'track/slug' and 'track/case-studies/slug' -> topic metadata incl. doc path."""
    topics = load_yaml(DATA / "topics.yml", {"tracks": {}})
    index: dict[str, dict] = {}
    for track, spec in topics["tracks"].items():
        for t in spec.get("topics", []):
            index[f"{track}/{t['slug']}"] = {**t, "track": track, "path": f"tracks/{track}/{t['slug']}.md"}
        for t in spec.get("case_studies", []):
            key = f"{track}/case-studies/{t['slug']}"
            index[key] = {**t, "track": track, "path": f"tracks/{track}/case-studies/{t['slug']}.md"}
    return index


def resolve_topic(track: str, topic: str | None) -> dict | None:
    if not topic:
        return None
    idx = topic_index()
    for key in (f"{track}/{topic}", topic):
        if key in idx:
            return idx[key]
    # topic may belong to another track (e.g. review task pointing at a DSA topic)
    for key, meta in idx.items():
        if key.endswith("/" + topic):
            return meta
    return None
