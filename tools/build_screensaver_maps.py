#!/usr/bin/env python3
"""Backt die Höhenkarten für Visualizer/screensaver.html in eine JS-Datei.

Der Screensaver parst seine Karten sonst zur Laufzeit per fetch() aus
index.html und themen/*.html — unter file:// blockt der Browser das (Origin
null). Dieses Skript zieht dieselben Daten vorab raus und schreibt sie nach
Visualizer/screensaver-maps.js; die wird per <script src> geladen und ist
damit CORS-frei. Fehlt die Datei, fällt der Screensaver auf fetch zurück.

Nach jedem layout_map.py oder build_theme_cards.py neu laufen lassen, sonst
zeigt der Screensaver die alten Karten.

Nutzung:
    python3 tools/build_screensaver_maps.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIS = ROOT / "Visualizer"
OUT = VIS / "screensaver-maps.js"

# identisch zu PARAM_NAMES in screensaver.html
PARAM_NAMES = ["SEED", "BETA", "L", "ZMAX", "BASE", "TERW", "RIDGE", "DBIAS",
               "SPREAD", "IRAD", "COASTW", "BASECUT", "LIFT"]


def parse_map(src):
    """Python-Port von parseMap() in screensaver.html — Logik dort ändern heisst hier auch."""
    arr = json.loads(re.search(r"const PEAKS = (\[.*?\])(?:;|\.filter)", src, re.S).group(1))
    tm = re.search(r"""const THEME\s*=\s*["']([\w-]+)["']""", src)
    peaks = [p for p in arr if tm[1] in p.get("t", [])] if tm else arr
    # Themenkarten überschreiben die Defaults in einer zweiten Zeile — letzte Zuweisung zählt
    block = src[src.index("let SEED"):src.index("let yaw")]
    params = {}
    for n in PARAM_NAMES:
        m = re.findall(r"\b" + n + r"\s*=\s*(-?[\d.]+)", block)
        if m:
            params[n] = float(m[-1])
    name = re.search(r"<title>Bitcoin-Wiki · (.*?)</title>", src)
    return {"peaks": peaks, "params": params, "name": name[1] if name else "Karte"}


def main():
    files = [VIS / "index.html"] + sorted((VIS / "themen").glob("*.html"))
    maps = [parse_map(f.read_text(encoding="utf-8")) for f in files]
    OUT.write_text(
        "// generiert von tools/build_screensaver_maps.py — nicht von Hand editieren\n"
        "window.MAPDATA_EMBED=" + json.dumps(maps, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {len(maps)} Karten, {OUT.stat().st_size // 1024} KB")
    for m, f in zip(maps, files):
        print(f"  {f.name:24} {len(m['peaks']):4} Gipfel  {m['name']}")


if __name__ == "__main__":
    main()
