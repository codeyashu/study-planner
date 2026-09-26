"""Export vocabulary and idiom tables from the communication drills to an Anki-importable CSV.

Reads docs/tracks/communication/drills/week-NN.md, finds tables whose header starts with
"Word" (Word | Part of speech | Meaning | Example) or "Expression" (Expression | Meaning | Example),
and writes build/vocab.csv with columns: front, back, tags.
Import in Anki: File > Import, allow HTML, field 1 = front, field 2 = back, field 3 = tags.

Usage: uv run python scripts/export_vocab.py [--up-to-week N]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from common import BUILD, DOCS  # noqa: E402

WEEK_FILE = re.compile(r"week-(\d{2})\.md$")


def split_row(line: str) -> list[str]:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return [re.sub(r"\*\*|`", "", c) for c in cells]


def parse_tables(text: str) -> list[tuple[str, list[list[str]]]]:
    """Return [(kind, rows)] where kind is 'word' or 'expression'."""
    out: list[tuple[str, list[list[str]]]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append(split_row(lines[j]))
                j += 1
            first = header[0].lower() if header else ""
            if first == "word" and len(header) >= 4:
                out.append(("word", [r for r in rows if len(r) >= 4]))
            elif first == "expression" and len(header) >= 3:
                out.append(("expression", [r for r in rows if len(r) >= 3]))
            i = j
        else:
            i += 1
    return out


def cards_from(text: str, week: int) -> list[tuple[str, str, str]]:
    cards = []
    for kind, rows in parse_tables(text):
        for r in rows:
            if kind == "word":
                word, pos, meaning, example = r[:4]
                back = f"<i>{pos}</i> — {meaning}<br><br>e.g. {example}"
                tags = f"comm word week{week:02d}"
            else:
                expr, meaning, example = r[:3]
                word, back = expr, f"{meaning}<br><br>e.g. {example}"
                tags = f"comm idiom week{week:02d}"
            if word and not set(word) <= set("-: "):
                cards.append((word, back, tags))
    return cards


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--up-to-week", type=int, default=99)
    args = ap.parse_args()
    cards: list[tuple[str, str, str]] = []
    for path in sorted((DOCS / "tracks" / "communication" / "drills").glob("week-*.md")):
        m = WEEK_FILE.search(path.name)
        if not m or int(m.group(1)) > args.up_to_week:
            continue
        cards += cards_from(path.read_text(encoding="utf-8"), int(m.group(1)))
    BUILD.mkdir(exist_ok=True)
    out = BUILD / "vocab.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(cards)
    print(f"vocab: {len(cards)} cards -> {out}")


if __name__ == "__main__":
    main()
