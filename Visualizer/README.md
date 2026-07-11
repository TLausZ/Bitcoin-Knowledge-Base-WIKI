# Visualizer

Interaktive 3D-Konturkarten der Wiki-Artikel. Jeder Artikel ist ein Hügel;
die Höhe entspricht seinem Gewicht aus `tools/rank_articles.py`
(0.7 · PageRank im Backlink-Graph + 0.3 · log-normierte RAW-Quellenzahl).

Alles sind einzelne HTML-Dateien ohne Abhängigkeiten — Doppelklick genügt.
Rendering: Canvas 2D mit eigener orthografischer Projektion und
Marching-Squares-Konturen, kein WebGL.

## Dateien

| Datei | Inhalt |
|---|---|
| `wiki-map-full.html` | Gesamtkarte: alle Artikel (Stand 2026-07-11: 410), Positionen force-directed aus dem Backlink-Graphen — verlinkte Artikel liegen beieinander, thematische Cluster werden zu Gebirgszügen. Linkes Panel mit sortierbarer Artikelliste (Gewicht ↓/↑, A–Z/Z–A); der Hintergrundbalken jeder Zeile zeigt das Gewicht. Hover in der Liste markiert den Hügel auf der Karte, Klick hält die Markierung fest; Hover auf der Karte zeigt jeden Titel. Top 22 dauerhaft beschriftet. |
| `wiki-topographie.html` | Kompakte Karte der Top-14-Artikel, jeder Gipfel beschriftet. |
| `kontur-demo.html` | Ursprünglicher Prototyp mit Zufallsterrain. Leertaste würfelt neu. |

Bedienung überall gleich: ziehen dreht und kippt, Scrollrad zoomt.
Alle Linien sind durchsichtig gezeichnet (kein Verdecken), und jede Kontur
wirft einen flachen Schatten auf die Bodenebene.

Beide Wiki-Karten sind deterministisch: Terrain-Rauschen und Layout laufen
mit festem Seed, dieselben Daten ergeben also bei jedem Laden exakt
dieselbe Karte. Andere Terrain-Variante: Seed in `buildField()` ändern
(`let s=21`); anderes Layout: `SEED` in `tools/layout_map.py`.

## Daten aktualisieren

Die Artikeldaten (Name, Score, Position) sind als `PEAKS`-Konstante in die
HTML-Dateien eingebettet. Nach größeren Wiki-Änderungen neu erzeugen:

```
python3 tools/rank_articles.py --csv Outputs/ranking.csv
python3 tools/layout_map.py
```

`layout_map.py` liest den `[[Backlink]]`-Graphen aus `Wiki/`, rechnet ein
Fruchterman-Reingold-Layout (verlinkte Artikel ziehen sich an, fester Seed,
Mindestabstand zwischen Gipfeln) und ersetzt die `PEAKS`-Konstante in der
Gesamtkarte. Nähe auf der Karte bedeutet dort also Linkstruktur.
Artikelzahl und Label-Anzahl im Untertitel der Karte werden zur Laufzeit
aus den Daten erzeugt und müssen nicht gepflegt werden.
`wiki-topographie.html` (Top 14) nutzt weiterhin die einfache
Goldener-Winkel-Spirale nach Ranking; ihre `PEAKS`-Liste wird nicht von
`layout_map.py` aktualisiert.

## Stellschrauben (im Quelltext)

- `SIG` / `SKIRT` — Breite von Gipfel und Sockel; SKIRT verbindet Nachbarhügel zu Graten
- `waves`-Schleife — Anzahl und Amplitude der Rausch-Oktaven (Zackigkeit der Linien)
- `L` — Anzahl Höhenlinien
- `LABEL_TOP` — wie viele Artikel dauerhaft beschriftet werden (nur Gesamtkarte)
