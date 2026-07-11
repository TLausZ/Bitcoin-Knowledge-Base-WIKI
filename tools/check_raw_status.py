#!/usr/bin/env python3
"""Abgleich RAW/ gegen RAW/_INGESTED.md mit robuster Unicode-Normalisierung.

Verhindert Fehlalarme durch Apostroph-/Anführungszeichen-Varianten (' vs '),
geschützte Leerzeichen und Gedankenstrich-Varianten in Dateinamen.

Aufruf:  python3 tools/check_raw_status.py  (vom KB-Root aus)

Ausgabe:
  NEU        - RAW-Dateien ohne Registry-Eintrag (einzige Quelle für "neu")
  VERWAIST   - Registry-Einträge ohne RAW-Datei
  STALE-LINK - "Compiliert in:"-Ziele, die es in Wiki/ nicht (mehr) gibt
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "RAW")
WIKI = os.path.join(ROOT, "Wiki")
REGISTRY = os.path.join(RAW, "_INGESTED.md")

IGNORE = {"_INGESTED.md", ".DS_Store"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    for a, b in [(" ", " "), ("’", "'"), ("‘", "'"),
                 ("“", '"'), ("”", '"'), ("„", '"'),
                 ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().casefold()


def raw_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(RAW):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f in IGNORE or f.startswith(".fuse"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), RAW)
            out.append(rel)
    return out


def registry_entries():
    """Liefert (Dateiname, Compiliert-Ziele, entfernt-Marker) je Eintrag.

    Compiliert-Ziele: Abschnitts-Zusätze wie "(D)" oder "(Abschnitt K)" werden
    entfernt, bevor gesplittet wird, damit Kommas in Klammern nicht stören.
    entfernt-Marker: Einträge mit "[Datei ..." beschreiben bewusst entfernte
    oder ersetzte Dateien und zählen nicht als verwaist.
    """
    entries = []
    for line in open(REGISTRY, encoding="utf-8"):
        m = re.match(r"\|\s*(.+?)\s*\|\s*(\d{4}-\d{2}-\d{2})", line)
        if m:
            targets = re.findall(r"Compiliert in:\s*([^|]+)", line)
            arts = []
            if targets:
                clause = re.sub(r"\([^)]*\)", "", targets[0])
                for a in re.split(r",|\s+und\s+", clause):
                    a = a.strip().rstrip(".").strip()
                    if a:
                        arts.append(a)
            removed = "[Datei" in line or "[Duplikat-Datei" in line
            entries.append((m.group(1), arts, removed))
    return entries


def main():
    files = raw_files()
    entries = registry_entries()
    ingested = {norm(name) for name, _, _ in entries}
    wiki = {os.path.splitext(f)[0] for f in os.listdir(WIKI)}

    new = [f for f in sorted(files) if norm(f) not in ingested]
    file_set = {norm(f) for f in files}
    orphaned = sorted({name for name, _, removed in entries
                       if norm(name) not in file_set and not removed})
    stale = sorted({(name, a) for name, arts, _ in entries for a in arts
                    if a not in wiki})

    print(f"RAW-Dateien: {len(files)} | Registry-Einträge: {len(entries)}")
    print(f"\nNEU ({len(new)}):")
    for f in new:
        print(f"  {f}")
    print(f"\nVERWAIST ({len(orphaned)}):")
    for f in orphaned:
        print(f"  {f}")
    print(f"\nSTALE-LINK ({len(stale)}):")
    for name, a in stale:
        print(f"  {a}  <-  {name}")
    return 0 if not new else 1


if __name__ == "__main__":
    sys.exit(main())
