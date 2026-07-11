#!/usr/bin/env python3
"""Force-directed Layout für Visualizer/wiki-map-full.html.

Liest den [[Backlink]]-Graphen aus Wiki/, die Scores aus Outputs/ranking.csv,
rechnet ein Fruchterman-Reingold-Layout (verlinkte Artikel ziehen sich an)
und ersetzt die eingebettete PEAKS-Konstante in der Karte.

Nutzung:
    python3 tools/rank_articles.py --csv Outputs/ranking.csv   # zuerst Scores
    python3 tools/layout_map.py
"""

import csv
import json
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rank_articles import WIKI, NAV_FILES, norm, parse_article

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "Visualizer" / "wiki-map-full.html"
CSV = ROOT / "Outputs" / "ranking.csv"
R = 2.3          # Zielradius der Karte (DOM=2.7 im HTML, mit Rand)
DMIN = 0.22      # Mindestabstand zwischen Gipfeln
ITER = 250
SEED = 21


def load_graph():
    articles = {}
    for path in sorted(WIKI.glob("*.md")):
        if path.name in NAV_FILES:
            continue
        _, outgoing, _ = parse_article(path)
        articles[norm(path.stem)] = outgoing
    known = set(articles)
    edges = set()
    for src, targets in articles.items():
        for t in set(targets):
            if t in known and t != src:
                edges.add((min(src, t), max(src, t)))
    return sorted(known), sorted(edges)


def load_scores():
    with CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    mx = max(float(r["score"]) for r in rows) or 1.0
    return {r["artikel"]: float(r["score"]) / mx for r in rows}


def fruchterman_reingold(nodes, edges, scores):
    rng = random.Random(SEED)
    n = len(nodes)
    idx = {name: i for i, name in enumerate(nodes)}
    # Start: Goldener-Winkel-Spirale nach Score (Wichtiges innen) + Jitter
    order = sorted(nodes, key=lambda a: -scores.get(a, 0))
    pos = [None] * n
    for rank, name in enumerate(order):
        ang = rank * 2.399963
        rad = R * math.sqrt(rank / (n - 1))
        pos[idx[name]] = [rad * math.cos(ang) + rng.uniform(-.01, .01),
                          rad * math.sin(ang) + rng.uniform(-.01, .01)]
    e = [(idx[a], idx[b]) for a, b in edges]
    k = 1.5 * math.sqrt((math.pi * R * R) / n)   # Wunschabstand (grosszügig, sonst klumpt der Hub-Kern)
    t = R / 4                                     # Starttemperatur
    for it in range(ITER):
        disp = [[0.0, 0.0] for _ in range(n)]
        for i in range(n):                        # Abstossung, O(n^2)
            xi, yi = pos[i]
            for j in range(i + 1, n):
                dx = xi - pos[j][0]; dy = yi - pos[j][1]
                d2 = dx * dx + dy * dy + 1e-6
                f = k * k / d2
                disp[i][0] += dx * f; disp[i][1] += dy * f
                disp[j][0] -= dx * f; disp[j][1] -= dy * f
        for i, j in e:                            # Anziehung entlang Links
            dx = pos[i][0] - pos[j][0]; dy = pos[i][1] - pos[j][1]
            d = math.sqrt(dx * dx + dy * dy) + 1e-6
            f = d / k
            disp[i][0] -= dx * f; disp[i][1] -= dy * f
            disp[j][0] += dx * f; disp[j][1] += dy * f
        for i in range(n):                        # Schritt mit Temperatur-Limit
            dx, dy = disp[i]
            d = math.sqrt(dx * dx + dy * dy) + 1e-6
            s = min(d, t) / d
            pos[i][0] += dx * s; pos[i][1] += dy * s
        t *= 0.97                                 # kein Kreis-Clamp: natürliche Form behalten
    cx = sum(p[0] for p in pos) / n               # zentrieren und einheitlich einpassen:
    cy = sum(p[1] for p in pos) / n               # Form bleibt erhalten, nichts wird auf
    rmax = max(math.hypot(p[0] - cx, p[1] - cy) for p in pos) or 1  # den Rand projiziert
    s = R * 0.98 / rmax
    for p in pos:
        p[0] = (p[0] - cx) * s; p[1] = (p[1] - cy) * s
    for _ in range(40):                           # Mindestabstand ausschütteln
        for i in range(n):
            for j in range(i + 1, n):
                dx = pos[i][0] - pos[j][0]; dy = pos[i][1] - pos[j][1]
                d = math.sqrt(dx * dx + dy * dy) + 1e-9
                if d < DMIN:
                    push = (DMIN - d) / 2 / d
                    pos[i][0] += dx * push; pos[i][1] += dy * push
                    pos[j][0] -= dx * push; pos[j][1] -= dy * push
    for p in pos:                                 # zurück in den Kreis (Grid-Grenze im HTML)
        r = math.sqrt(p[0] ** 2 + p[1] ** 2)
        if r > R:
            p[0] *= R / r; p[1] *= R / r
    return {name: pos[idx[name]] for name in nodes}


def main():
    nodes, edges = load_graph()
    scores = load_scores()
    print(f"{len(nodes)} Artikel, {len(edges)} Links — Layout rechnet …")
    layout = fruchterman_reingold(nodes, edges, scores)
    peaks = [{"n": a, "s": round(scores.get(a, 0.01), 3),
              "x": round(layout[a][0], 3), "y": round(layout[a][1], 3)}
             for a in sorted(nodes, key=lambda a: -scores.get(a, 0))]
    js = "const PEAKS = " + json.dumps(peaks, ensure_ascii=False, separators=(",", ":")) + ";"
    html = HTML.read_text(encoding="utf-8")
    html, cnt = re.subn(r"const PEAKS = \[.*?\];", js, html, count=1, flags=re.S)
    if cnt != 1:
        sys.exit("PEAKS-Konstante nicht gefunden.")
    HTML.write_text(html, encoding="utf-8")
    print(f"{HTML.name} aktualisiert ({len(peaks)} Artikel).")


if __name__ == "__main__":
    main()
