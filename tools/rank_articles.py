#!/usr/bin/env python3
"""Gewichtung der Wiki-Artikel.

Score = 0.7 * PageRank (normalisiert) + 0.3 * RAW-Quellenzahl (log-normalisiert).
Artikel unter STUB_WORDS Wörtern (Body ohne Frontmatter-Zeilen) werden als Stub markiert.

Nur Links zwischen existierenden Wiki-Artikeln zählen für den Graphen.
Die Sources-Zeile zählt separat als RAW-Quellenzahl und fliesst nicht in den Linkgraphen ein.

Nutzung:
    python3 tools/rank_articles.py            # Top 30
    python3 tools/rank_articles.py --top 100
    python3 tools/rank_articles.py --csv Outputs/ranking.csv
"""

import argparse
import csv
import math
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

WIKI = Path(__file__).resolve().parent.parent / "Wiki"
# Basis-URL des veröffentlichten Wikis; daraus wird die url-Spalte im CSV gebaut
WIKI_URL = "https://github.com/TLausZ/Bitcoin-Knowledge-Base-WIKI/blob/main/Wiki/"
NAV_FILES = {"INDEX.md", "QUESTIONS.md", "CLAUDE.md", "CHANGELOG.md", "_INGESTED.md"}
STUB_WORDS = 150
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")


def norm(s: str) -> str:
    return unicodedata.normalize("NFC", s.strip().removesuffix(".md"))


def parse_article(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    sources, body_lines = [], []
    for line in lines:
        if line.startswith("**Sources:**"):
            sources = [norm(m) for m in LINK_RE.findall(line)]
        else:
            body_lines.append(line)
    body = "\n".join(body_lines)
    outgoing = [norm(m) for m in LINK_RE.findall(body)]
    words = len(body.split())
    return sources, outgoing, words


def pagerank(graph: dict, damping=0.85, iterations=50):
    nodes = list(graph)
    n = len(nodes)
    rank = {node: 1.0 / n for node in nodes}
    incoming = {node: [] for node in nodes}
    for src, targets in graph.items():
        for t in targets:
            incoming[t].append(src)
    for _ in range(iterations):
        new = {}
        dangling = sum(rank[x] for x in nodes if not graph[x]) / n
        for node in nodes:
            s = sum(rank[src] / len(graph[src]) for src in incoming[node])
            new[node] = (1 - damping) / n + damping * (s + dangling)
        rank = new
    return rank


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--csv", type=str, default=None)
    args = ap.parse_args()

    articles = {}
    for path in sorted(WIKI.glob("*.md")):
        if path.name in NAV_FILES:
            continue
        name = norm(path.stem)
        sources, outgoing, words = parse_article(path)
        articles[name] = {"sources": sources, "outgoing": outgoing, "words": words}

    known = set(articles)
    graph = {
        name: [t for t in set(a["outgoing"]) if t in known and t != name]
        for name, a in articles.items()
    }
    incoming_count = {name: 0 for name in known}
    for targets in graph.values():
        for t in targets:
            incoming_count[t] += 1

    pr = pagerank(graph)
    max_pr = max(pr.values()) or 1.0
    max_src = max(math.log1p(len(a["sources"])) for a in articles.values()) or 1.0

    rows = []
    for name, a in articles.items():
        score = 0.7 * (pr[name] / max_pr) + 0.3 * (math.log1p(len(a["sources"])) / max_src)
        rows.append({
            "artikel": name,
            "score": round(score, 4),
            "pagerank": round(pr[name] / max_pr, 4),
            "eingehend": incoming_count[name],
            "quellen": len(a["sources"]),
            "woerter": a["words"],
            "stub": "ja" if a["words"] < STUB_WORDS else "",
            "url": WIKI_URL + quote(name) + ".md",
        })
    rows.sort(key=lambda r: r["score"], reverse=True)

    if args.csv:
        out = Path(args.csv)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
        print(f"{len(rows)} Artikel nach {out} geschrieben.")
        return

    fmt = "{:<52} {:>6} {:>8} {:>9} {:>7} {:>7} {:>5}"
    print(fmt.format("Artikel", "Score", "PageRank", "eingehend", "Quellen", "Wörter", "Stub"))
    for r in rows[: args.top]:
        print(fmt.format(r["artikel"][:52], f"{r['score']:.3f}", f"{r['pagerank']:.3f}",
                         r["eingehend"], r["quellen"], r["woerter"], r["stub"]))
    stubs = sum(1 for r in rows if r["stub"])
    print(f"\n{len(rows)} Artikel gesamt, davon {stubs} Stubs (<{STUB_WORDS} Wörter).",
          file=sys.stderr)


if __name__ == "__main__":
    main()
