#!/usr/bin/env python3
"""Stanzt aus Visualizer/index.html je eine Themenkarte pro Thema.

Eine Themenkarte = Gesamtkarte, aber (a) PEAKS auf Artikel dieses Themas
gefiltert und (b) SEED = Themennummer (Position in CATS, 1-basiert). index.html
bleibt der einzige Wartungspunkt: nach jeder Renderer-/Daten-Aenderung neu laufen.

    python3 tools/build_theme_cards.py

Schreibt Visualizer/themen/<slug>.html (nur Themen mit >0 Artikeln).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Visualizer" / "index.html"
OUT = ROOT / "Visualizer" / "themen"

# Reihenfolge = tools/classify_topics.py CATS = Dropdown-Reihenfolge. Nummer = Index+1.
CATS = [
    ("grundlagen",   "Grundlagen"),
    ("protokoll",    "Protokoll & Technik"),
    ("bips",         "BIPs"),
    ("self-custody", "Self-Custody & Sicherheit"),
    ("privacy",      "Privacy"),
    ("mining",       "Mining & Energie"),
    ("lightning",    "Layer 2 & Lightning"),
    ("oekonomie",    "Ökonomie & Geld"),
    ("philosophie",  "Philosophie & Kultur"),
    ("adoption",     "Adoption & Regulierung"),
    ("kritik",       "Kritik"),
    ("geschichte",   "Geschichte"),
    ("satoshi",      "Satoshi"),
    ("zitate",       "Zitate"),
    ("studien",      "Studien"),
    ("buecher",      "Bücher"),
    ("wallets",      "Wallets & Software"),
    ("glossar",      "Glossar"),
    ("sonstiges",    "Sonstiges"),
]

# Pro-Thema-Overrides der FFT-Parameter. Leer = jede Karte nutzt die v6-Defaults
# aus index.html, nur SEED = Themennummer. Werte kommen aus dem versteckten
# Admin-Panel (Taste 0): die untere Zeile dort kopieren und hier eintragen, z.B.
#   "privacy": {"SEED": 5, "BETA": 5.2, "RIDGE": 0.35},
# Nur die genannten Keys werden überschrieben; der Rest bleibt Default.
# Können sich nach jedem Compile ändern (Layout/Daten verschieben sich).
OVERRIDES = {
    "grundlagen":  {"SEED": 1,  "BETA": 4.35, "L": 32, "BASECUT": 0.46, "ZMAX": 0.6,  "BASE": 0.15, "TERW": 0.46, "RIDGE": 0.8,  "DBIAS": 0.6, "SPREAD": 0.8,  "IRAD": 2.4,  "COASTW": 1.1,  "LIFT": -0.36},
    "protokoll":   {"SEED": 2,  "BETA": 3.5,  "L": 32, "BASECUT": 0.14, "ZMAX": 0.55, "BASE": 0.29, "TERW": 1.92, "RIDGE": 0.95, "DBIAS": 1,   "SPREAD": 0.95, "IRAD": 2.7,  "COASTW": 0.05, "LIFT": -0.3},
    "bips":        {"SEED": 3,  "BETA": 3.5,  "L": 32, "BASECUT": 0.14, "ZMAX": 0.45, "BASE": 0.27, "TERW": 1.92, "RIDGE": 0.8,  "DBIAS": 1,   "SPREAD": 0.95, "IRAD": 2.7,  "COASTW": 0.55, "LIFT": -0.3},
    "self-custody":{"SEED": 4,  "BETA": 3.5,  "L": 26, "BASECUT": 0.12, "ZMAX": 0.4,  "BASE": 0.11, "TERW": 1.92, "RIDGE": 0.95, "DBIAS": 1,   "SPREAD": 0.9,  "IRAD": 2.7,  "COASTW": 0.05, "LIFT": -0.3},
    "privacy":     {"SEED": 5,  "BETA": 6,    "L": 35, "BASECUT": 0.24, "ZMAX": 0.35, "BASE": 0.25, "TERW": 2,    "RIDGE": 0.1,  "DBIAS": 1,   "SPREAD": 0.75, "IRAD": 2.45, "COASTW": 1.3,  "LIFT": -0.36},
    "mining":      {"SEED": 6,  "BETA": 4.25, "L": 35, "BASECUT": 0.14, "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 0.35, "DBIAS": 1,   "SPREAD": 0.55, "IRAD": 2,    "COASTW": 0.55, "LIFT": -0.36},
    "lightning":   {"SEED": 7,  "BETA": 3.85, "L": 32, "BASECUT": 0.2,  "ZMAX": 0.4,  "BASE": 0.35, "TERW": 2,    "RIDGE": 0.2,  "DBIAS": 1,   "SPREAD": 0.85, "IRAD": 2.5,  "COASTW": 0.55, "LIFT": -0.36},
    "oekonomie":   {"SEED": 8,  "BETA": 3.9,  "L": 32, "BASECUT": 0.3,  "ZMAX": 0.4,  "BASE": 0.43, "TERW": 2,    "RIDGE": 0.2,  "DBIAS": 1,   "SPREAD": 0.85, "IRAD": 2.5,  "COASTW": 1.1,  "LIFT": -0.36},
    "adoption":    {"SEED": 10, "BETA": 6,    "L": 32, "BASECUT": 0.1,  "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 1,    "DBIAS": 0.95,"SPREAD": 0.75, "IRAD": 2.5,  "COASTW": 1.15, "LIFT": -0.36},
    "kritik":      {"SEED": 11, "BETA": 5,    "L": 32, "BASECUT": 0.1,  "ZMAX": 0.4,  "BASE": 0.11, "TERW": 2,    "RIDGE": 0.15, "DBIAS": 1,   "SPREAD": 0.7,  "IRAD": 2.15, "COASTW": 1.25, "LIFT": -0.36},
    "geschichte":  {"SEED": 12, "BETA": 6,    "L": 32, "BASECUT": 0.16, "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 0.65, "DBIAS": 1,   "SPREAD": 0.6,  "IRAD": 2.5,  "COASTW": 0.55, "LIFT": -0.36},
    "zitate":      {"SEED": 14, "BETA": 4,    "L": 32, "BASECUT": 0.12, "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 1,    "DBIAS": 1,   "SPREAD": 0.4,  "IRAD": 1.55, "COASTW": 1.15, "LIFT": -0.36},
    "studien":     {"SEED": 15, "BETA": 3.5,  "L": 32, "BASECUT": 0.14, "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 0.3,  "DBIAS": 1,   "SPREAD": 0.55, "IRAD": 2.1,  "COASTW": 1.35, "LIFT": -0.36},
    "buecher":     {"SEED": 16, "BETA": 3.85, "L": 32, "BASECUT": 0.22, "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 0.4,  "DBIAS": 1,   "SPREAD": 0.6,  "IRAD": 1.75, "COASTW": 0.25, "LIFT": -0.36},
    "wallets":     {"SEED": 17, "BETA": 4.5,  "L": 32, "BASECUT": 0.2,  "ZMAX": 0.4,  "BASE": 0.21, "TERW": 2,    "RIDGE": 0.25, "DBIAS": 1,   "SPREAD": 0.75, "IRAD": 2.15, "COASTW": 0.75, "LIFT": -0.36},
    "glossar":     {"SEED": 18, "BETA": 4.65, "L": 32, "BASECUT": 0.68, "ZMAX": 0.55, "BASE": 0.03, "TERW": 0.04, "RIDGE": 0.75, "DBIAS": 0.5, "SPREAD": 0,    "IRAD": 1.8,  "COASTW": 1,    "LIFT": -0.36},
}

def main():
    html = SRC.read_text(encoding="utf-8")

    m = re.search(r"const PEAKS = (\[.*?\]);", html)
    if not m:
        sys.exit("PEAKS-Tabelle in index.html nicht gefunden.")
    peaks_decl = m.group(0)          # ganze Deklaration: const PEAKS = [...];
    peaks_literal = m.group(1)       # nur das Array-Literal
    peaks = json.loads(peaks_literal)

    if "/*__THEME_CFG__*/" not in html:
        sys.exit("THEME-CFG-Marker in index.html nicht gefunden.")

    # Nur Themen mit Artikeln bekommen eine Karte; diese Liste speist auch den
    # Dropdown-Umschalter (THEME_CARDS), damit er nie auf eine 404-Karte zeigt.
    eligible = [(i, slug, name, sum(1 for p in peaks if slug in (p.get("t") or [])))
                for i, (slug, name) in enumerate(CATS, start=1)]
    eligible = [(i, slug, name, c) for (i, slug, name, c) in eligible if c > 0]
    theme_cards_json = json.dumps([[slug, name, c] for (_, slug, name, c) in eligible],
                                  ensure_ascii=False)

    for i, (slug, name) in enumerate(CATS, start=1):
        if not any(s == slug for (_, s, _, _) in eligible):
            print(f"  skip {i:2d} {slug:<13} (0 Artikel)")

    OUT.mkdir(exist_ok=True)
    made = []
    for i, slug, name, count in eligible:
        doc = html
        # 1) Konfig am Marker: SEED = Themennummer, dann optionale Overrides
        #    (aus dem Admin-Panel getunt). Override-SEED gewinnt, falls gesetzt.
        params = {"SEED": i, **OVERRIDES.get(slug, {})}
        cfg = " ".join(f"{key}={json.dumps(val)};" for key, val in params.items())
        doc = doc.replace("/*__THEME_CFG__*/", cfg, 1)
        # 2) PEAKS auf dieses Thema filtern + Umschalter-Liste einspritzen
        new_decl = (f"const THEME = {json.dumps(slug)};\n"
                    f"const TOTAL = {len(peaks)};\n"
                    f"const THEME_CARDS = {theme_cards_json};\n"
                    f"const PEAKS = {peaks_literal}"
                    ".filter(p => (p.t || []).includes(THEME));")
        doc = doc.replace(peaks_decl, new_decl, 1)
        # 3) Titel/Kopf auf das Thema
        doc = doc.replace(
            "<title>Bitcoin-Wiki · Gesamtkarte</title>",
            f"<title>Bitcoin-Wiki · {name}</title>", 1)
        doc = doc.replace(
            "<h1>Bitcoin-Wiki · Gesamtkarte</h1>",
            f"<h1>Bitcoin-Wiki · {name}</h1>", 1)

        (OUT / f"{slug}.html").write_text(doc, encoding="utf-8")
        made.append((i, slug, count))
        print(f"  ok   {i:2d} {slug:<13} {count:>3} Artikel  seed={i}")

    print(f"\n{len(made)} Themenkarten → {OUT.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
