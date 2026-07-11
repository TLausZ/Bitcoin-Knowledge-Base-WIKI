# tools/

Python-Hilfsskripte für die Pflege des Bitcoin-Wikis. Alle Skripte laufen mit
der Standardbibliothek (Python 3.9+), keine Abhängigkeiten nötig. Aufruf
immer aus dem Wurzelverzeichnis der Knowledge Base.

## check_raw_status.py

Vergleicht den Inhalt von `RAW/` mit dem Register `RAW/_INGESTED.md` und
meldet, welche Dateien noch nicht kompiliert wurden. Der Vergleich ist
Unicode-normalisiert (NFC), damit kuriose Dateinamen mit typografischen
Anführungszeichen oder geschützten Leerzeichen keine falschen Treffer
erzeugen. Der Compile-Schritt des Librarians stützt sich ausschliesslich auf
dieses Skript.

```
python3 tools/check_raw_status.py
```

## rank_articles.py

Gewichtet alle Wiki-Artikel. Der Score setzt sich zusammen aus
0.7 × PageRank über den `[[Backlink]]`-Graphen (normalisiert) und
0.3 × Zahl der RAW-Quellen (log-normalisiert). Artikel unter 150 Wörtern
werden als Stub markiert. Die `url`-Spalte enthält den Link zum jeweiligen
Artikel im veröffentlichten GitHub-Wiki (Basis-URL: Konstante `WIKI_URL`
im Skript).

```
python3 tools/rank_articles.py                      # Top 30 im Terminal
python3 tools/rank_articles.py --top 100
python3 tools/rank_articles.py --csv Outputs/ranking.csv
```

## layout_map.py

Berechnet das Layout für die topografische Karte
`Visualizer/wiki-map-full.html`. Liest den Linkgraphen aus `Wiki/` und die
Scores aus `Outputs/ranking.csv`, rechnet ein Fruchterman-Reingold-Layout
(verlinkte Artikel ziehen sich an, fester Seed → reproduzierbar) und
ersetzt die eingebettete `PEAKS`-Konstante direkt im HTML.

```
python3 tools/rank_articles.py --csv Outputs/ranking.csv   # zuerst Scores
python3 tools/layout_map.py
```

## Typischer Ablauf nach einem Compile-Pass

```
python3 tools/rank_articles.py --csv Outputs/ranking.csv
python3 tools/layout_map.py
```

Danach zeigt die Karte den aktuellen Stand des Wikis.
