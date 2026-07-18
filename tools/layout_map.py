#!/usr/bin/env python3
"""Multi-Kamm-Layout für Visualizer/index.html.

Python-Port des Karten-WIP-Layouts (Visualizer/karten-wip/layout-multi.js,
Portierung 18.07.2026 auf User-Freigabe): die grössten Themen werden zufällig
platzierte Gebirgszüge, der Rest Füller-Einzelgipfel. Der Zufallsgenerator
(mulberry32) ist bit-genau nachgebaut, damit derselbe Layout-Seed dieselbe
Insel ergibt wie im WIP. Parameter-Änderungen zuerst im WIP erproben, dann
LAY unten nachziehen — die JS-Datei bleibt die Spielwiese, diese hier die
scharfe Kopie.

Liest Scores aus Outputs/ranking.csv und Themen aus den Wiki-Artikeln,
ersetzt die eingebettete PEAKS-Konstante in der Karte.

Nutzung:
    python3 tools/rank_articles.py --csv Outputs/ranking.csv   # zuerst Scores
    python3 tools/layout_map.py
"""

import csv
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rank_articles import WIKI, NAV_FILES, norm, parse_article
from classify_topics import KEEP_PRIORITY

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "Visualizer" / "index.html"
CSV = ROOT / "Outputs" / "ranking.csv"
R = 2.3          # Zielradius der Karte (DOM=2.7 im HTML, mit Rand)

# Finale User-Insel 18.07.2026 — identisch zu MK.params in layout-multi.js
LAY = {"seed": 8, "ridges": 7, "len": 1.70, "bow": 1.50,
       "flank": 0.75, "dmin": 0.09, "fill": 0.60}

# Themen-Mapping auf Layout-Gruppen (identisch zu ARM_OF in layout-multi.js);
# Ungemapptes (grundlagen/glossar/sonstiges) landet in der Gruppe "grundlagen".
ARM_OF = {"protokoll": "protokoll", "bips": "protokoll",
          "self-custody": "self-custody", "wallets": "self-custody",
          "privacy": "privacy", "mining": "mining", "lightning": "lightning",
          "oekonomie": "oekonomie", "studien": "oekonomie",
          "philosophie": "philosophie", "zitate": "philosophie",
          "satoshi": "philosophie", "geschichte": "philosophie",
          "buecher": "philosophie", "adoption": "adoption", "kritik": "adoption"}


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


def load_topics():
    """slug -> Themenliste aus der **Themen:**-Zeile jedes Artikels."""
    topics = {}
    for path in WIKI.glob("*.md"):
        if path.name in NAV_FILES:
            continue
        m = re.search(r"^\*\*Themen:\*\* (.+)$", path.read_text(encoding="utf-8"), flags=re.M)
        topics[norm(path.stem)] = [t.strip() for t in m.group(1).split(",")] if m else []
    return topics


def load_scores():
    with CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    mx = max(float(r["score"]) for r in rows) or 1.0
    return {r["artikel"]: float(r["score"]) / mx for r in rows}


def mulberry32(a):
    """Bit-genauer Nachbau des JS-mulberry32 (layout-multi.js): gleiche
    Seeds liefern exakt dieselbe Zufallsfolge wie im Browser-WIP."""
    a &= 0xFFFFFFFF
    def rnd():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = ((a ^ (a >> 15)) * (1 | a)) & 0xFFFFFFFF
        t = (((t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ t) & 0xFFFFFFFF
        return (t ^ (t >> 14)) / 4294967296
    return rnd


def multi_kamm(nodes, topics, scores):
    """Port von MK.compute: gleiche Aufruf-Reihenfolge des RNG, gleiche
    (stabilen) Sortierungen — Ergebnis deckt sich mit dem WIP-Layout."""
    order = sorted(nodes, key=lambda a: -scores.get(a, 0))   # = PEAKS-Reihenfolge
    rnd = mulberry32(((LAY["seed"] * 2246822519) & 0xFFFFFFFF) ^ 0x3ADE68B1)
    groups = {}
    for name in order:
        prim = next((t for t in KEEP_PRIORITY if t in topics.get(name, [])), None)
        groups.setdefault(ARM_OF.get(prim, "grundlagen"), []).append(name)
    # grösste Gruppen zuerst: die ersten LAY["ridges"] werden Kämme, Rest Füller.
    # JS sortiert nach dem gerundeten Score aus der PEAKS-Tabelle — hier gleich.
    gl = sorted((sorted(m, key=lambda a: -round(scores.get(a, 0.01), 3))
                 for m in groups.values()), key=lambda m: -len(m))
    centers = []

    def place(rad):
        """Kandidaten würfeln, den mit max. Abstand zum schon Platzierten nehmen."""
        best, bd = [0.0, 0.0], -1.0
        for _ in range(32):
            a = rnd() * 2 * math.pi
            rr = math.sqrt(rnd()) * max(0.0, 0.92 * R - rad)
            c = [rr * math.cos(a), rr * math.sin(a)]
            d = 9.0
            for q in centers:
                d = min(d, math.hypot(c[0] - q[0], c[1] - q[1]))
            if d > bd:
                bd, best = d, c
        centers.append(best)
        return best

    pos = {}
    mmax = len(gl[0])
    for gi, m in enumerate(gl):
        cnt = len(m)
        if gi < LAY["ridges"]:
            ln = LAY["len"] * R * (0.5 + 0.5 * math.sqrt(cnt / mmax))
            ang = rnd() * 2 * math.pi
            ux, uy = math.cos(ang), math.sin(ang)
            qx, qy = -uy, ux
            c = place(ln / 2)
            pm = (0, 0.5, 1)[int(rnd() * 3)]     # Gipfel am Anfang/Mitte/Ende
            bsign = -1 if rnd() < 0.5 else 1
            slots = sorted(((i + 0.5) / cnt for i in range(cnt)),
                           key=lambda t: abs(t - pm))
            for j, name in enumerate(m):         # Score hoch = Grat nahe pm
                t = slots[j]
                side = 1 if j % 2 else -1
                off = (bsign * LAY["bow"] * 0.25 * ln * math.sin(math.pi * t)
                       + side * (j / cnt) ** 0.7 * LAY["flank"] * (0.35 + 0.65 * rnd()))
                pos[name] = [c[0] + (t - 0.5) * ln * ux + off * qx,
                             c[1] + (t - 0.5) * ln * uy + off * qy]
        else:                                    # Füller: Spirale, Top im Zentrum
            rad = min(0.7, LAY["fill"] * 0.16 * math.sqrt(cnt))
            c = place(rad + 0.15)
            for j, name in enumerate(m):
                rr = rad * math.sqrt((j + 0.5) / cnt)
                a2 = j * 2.399963
                pos[name] = [c[0] + rr * math.cos(a2), c[1] + rr * math.sin(a2)]

    plist = [pos[n] for n in order]              # Shake in PEAKS-Reihenfolge wie im JS
    for _ in range(25):
        for i in range(len(plist)):
            for j in range(i + 1, len(plist)):
                dx = plist[i][0] - plist[j][0]; dy = plist[i][1] - plist[j][1]
                d = math.hypot(dx, dy) + 1e-9
                if d < LAY["dmin"]:
                    push = (LAY["dmin"] - d) / 2 / d
                    plist[i][0] += dx * push; plist[i][1] += dy * push
                    plist[j][0] -= dx * push; plist[j][1] -= dy * push
    rmx = max(math.hypot(x, y) for x, y in plist)
    if rmx > 0.98 * R:                           # in den Kreis einpassen
        s = 0.98 * R / rmx
        plist = [[x * s, y * s] for x, y in plist]
    return {n: p for n, p in zip(order, plist)}


def main():
    nodes, edges = load_graph()
    scores = load_scores()
    topics = load_topics()
    print(f"{len(nodes)} Artikel, {len(edges)} Links — Multi-Kamm-Layout rechnet …")
    layout = multi_kamm(nodes, topics, scores)
    peaks = [{"n": a, "s": round(scores.get(a, 0.01), 3),
              "x": round(layout[a][0], 3), "y": round(layout[a][1], 3),
              "t": topics.get(a, [])}
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
