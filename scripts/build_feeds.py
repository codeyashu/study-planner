"""Aggregate RSS feeds from data/feeds.yml into docs/reading/feed.md.

Fail-soft: a broken feed is reported on the page, never fails the build.
Usage: uv run python scripts/build_feeds.py [--hours 72]
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import html
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import feedparser
import requests

sys.path.insert(0, str(Path(__file__).parent))

from common import DATA, DOCS, TZ, load_yaml  # noqa: E402

UA = "study-planner-feed/1.0 (+https://github.com/codeyashu/study-planner)"
TAG_LABEL = {
    "ai": "AI engineering",
    "sd": "System design",
    "arch": "Architecture",
    "python": "Python",
    "java": "Java / Spring",
    "career": "Career & leadership",
    "news": "News",
}


def entry_time(e) -> dt.datetime | None:
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        t = e.get(key)
        if t:
            return dt.datetime.fromtimestamp(calendar.timegm(t), tz=dt.UTC)
    return None


def clean_title(title: str) -> str:
    title = html.unescape(re.sub(r"<[^>]+>", "", title or "")).strip()
    return title.replace("[", "(").replace("]", ")").replace("|", "/") or "(untitled)"


def fetch(feed: dict, since: dt.datetime) -> tuple[dict, list[dict], str | None]:
    try:
        resp = requests.get(feed["url"], headers={"User-Agent": UA}, timeout=20)
        resp.raise_for_status()
        parsed = feedparser.parse(resp.content)
    except Exception as exc:  # noqa: BLE001 — fail-soft by design
        return feed, [], f"{type(exc).__name__}: {exc}"[:160]
    items = []
    for e in parsed.entries:
        ts = entry_time(e)
        if ts is None or ts < since:
            continue
        link = e.get("link")
        if not link:
            continue
        items.append({"title": clean_title(e.get("title", "")), "link": link, "time": ts, "source": feed["name"]})
    items.sort(key=lambda i: i["time"], reverse=True)
    return feed, items[: int(feed.get("max", 3))], None


def render(results, hours: int, now: dt.datetime) -> str:
    seen: set[str] = set()
    groups: dict[str, list[dict]] = {k: [] for k in TAG_LABEL}
    errors = []
    for feed, items, err in results:
        if err:
            errors.append((feed["name"], err))
        primary = (feed.get("tags") or ["news"])[0]
        for it in items:
            key = it["link"].split("?")[0].rstrip("/")
            if key in seen:
                continue
            seen.add(key)
            groups.setdefault(primary, []).append(it)
    total = sum(len(v) for v in groups.values())
    out = [
        "---",
        "title: Today's feed",
        "generated: true",
        "---",
        "",
        "# Today's feed",
        "",
        f'!!! info "{total} items from the last {hours} h · built {now.astimezone(TZ):%a %d %b %Y %H:%M} IST"',
        "    Auto-aggregated from [data/feeds.yml](https://github.com/codeyashu/study-planner/blob/main/data/feeds.yml)."
        " Skim titles; open at most 3. The curated picks live in the [digest](../digest/index.md).",
        "",
    ]
    for tag, label in TAG_LABEL.items():
        items = sorted(groups.get(tag, []), key=lambda i: i["time"], reverse=True)
        if not items:
            continue
        out += [f"## {label}", ""]
        for it in items:
            out.append(f"- [{it['title']}]({it['link']}) — *{it['source']}* · {it['time'].astimezone(TZ):%d %b %H:%M}")
        out.append("")
    if errors:
        out += ['??? warning "Feeds that failed this run"', ""]
        out += [f"    - **{name}** — `{err}`" for name, err in errors]
        out.append("")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=72)
    args = ap.parse_args()
    now = dt.datetime.now(dt.UTC)
    since = now - dt.timedelta(hours=args.hours)
    feeds = (load_yaml(DATA / "feeds.yml", {"feeds": []}) or {}).get("feeds", [])
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(lambda f: fetch(f, since), feeds))
    page = render(results, args.hours, now)
    out = DOCS / "reading" / "feed.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    ok = sum(1 for _, _, e in results if not e)
    print(f"feeds: {ok}/{len(feeds)} ok")


if __name__ == "__main__":
    main()
