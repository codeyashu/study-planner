"""Check external links in data/resources/*.yml (and optionally all docs) -> build/link-report.md.

Exit code 1 if any link is definitely broken (404/410/DNS failure). 403/429/timeouts are reported as 'unverified'
because many sites block bots.
Usage: uv run python scripts/check_links.py [--docs] [--workers 16]
"""

from __future__ import annotations

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))

from common import BUILD, DATA, DOCS, load_yaml  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
MD_LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
BROKEN = {404, 410}


def collect(include_docs: bool) -> dict[str, set[str]]:
    urls: dict[str, set[str]] = {}
    for f in sorted((DATA / "resources").glob("*.yml")):
        loaded = load_yaml(f, []) or []
        if isinstance(loaded, dict):  # tolerate {resources: [...]} shape
            loaded = loaded.get("resources", [])
        for item in loaded:
            if isinstance(item, dict) and item.get("url"):
                urls.setdefault(item["url"], set()).add(f"data/resources/{f.name}")
    if include_docs:
        for md in DOCS.rglob("*.md"):
            if md.name == "feed.md" or "digest" in md.parts:
                continue
            for url in MD_LINK.findall(md.read_text(encoding="utf-8")):
                urls.setdefault(url.rstrip(".,"), set()).add(str(md.relative_to(DOCS.parent)))
    return urls


def check(url: str) -> tuple[str, int | None, str]:
    try:
        r = requests.head(url, headers={"User-Agent": UA}, timeout=15, allow_redirects=True)
        if r.status_code in (405, 403, 400) or r.status_code >= 500:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=20, allow_redirects=True, stream=True)
        return url, r.status_code, ""
    except requests.exceptions.ConnectionError as exc:
        return url, None, f"connection: {str(exc)[:80]}"
    except Exception as exc:  # noqa: BLE001
        return url, None, f"{type(exc).__name__}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", action="store_true", help="also scan all markdown pages")
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()
    urls = collect(args.docs)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(check, sorted(urls)))
    broken = [(u, s, e) for u, s, e in results if (s in BROKEN) or (s is None and e.startswith("connection"))]
    unverified = [(u, s, e) for u, s, e in results if (u, s, e) not in broken and (s is None or s >= 400)]
    lines = ["# Link report", "", f"Checked {len(results)} URLs · broken {len(broken)} · unverified {len(unverified)}", ""]
    if broken:
        lines += ["## Broken", ""] + [f"- {u} — {s or e} — in {', '.join(sorted(urls[u]))}" for u, s, e in broken] + [""]
    if unverified:
        lines += ["## Unverified (blocked/timeouts)", ""] + [f"- {u} — {s or e}" for u, s, e in unverified]
    BUILD.mkdir(exist_ok=True)
    (BUILD / "link-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(lines[2])
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
