# Buch-Ingestion — Runbook

Voller Ablauf für Bücher (epub/pdf) in bitcoin_kb. Die Hard-Rules (Buch = eigener Wiki-Artikel, Tag `buecher`, kein Autor im Wiki-Slug) stehen in `CLAUDE.md`; dieses File ist die Schritt-für-Schritt-Anleitung. Präzedenz wie überall: `CLAUDE.md` schlägt dieses File bei Widerspruch.

## 1. Tiefe (Tier A/B/C)

Pro Buch mit dem User abstimmbar:

- **Tier A** — Ideen-/Ökonomie-/Philosophiebücher: tiefe Zusammenfassung (~800–1000 Wörter), Argument im Zentrum.
  - Belletristik-Sonderfall: Prämisse, durchziehende Themen und markante Stellen statt «der These» (vgl. `magic-future-money`).
- **Tier B** — praktische Ratgeber: Methode/Checkliste statt Prosa, Bullet-Listen erlaubt.
- **Tier C** — technische Bücher: Kurzeintrag (~300 Wörter), Kapitelübersicht plus Backlinks zu bestehenden Konzept-Artikeln, keine Kapitel-für-Kapitel-Tiefe (vgl. `mastering-bitcoin`, `einfuehrung-in-das-lightning-netzwerk`).

**Sprach-Dubletten** (EN+DE desselben Werks) = ein Artikel, beide Editionen als Quelle — gilt für alle Bücher. **Mehrbänder** (Vol 1–3) = je ein Artikel.

## 2. Extraktion

**epub** — Tool: `tools/extract_epub.py` (ebooklib in Spine-Reihenfolge + BeautifulSoup, Leaf-Block-Logik inkl. `<div>` — sonst geht Prosa verloren, die manche Epubs in `<div>` statt `<p>` legen).

```
python3 tools/extract_epub.py "RAW/<datei>.epub" "<scratchpad>/<slug>.md"
```

**PDF** — `pypdf` (seit Pass 96 installiert). Volltext in den Scratchpad extrahieren, dann wie beim epub-Extrakt lesen:

```
python3 -c "import pypdf,sys; r=pypdf.PdfReader(sys.argv[1]); open(sys.argv[2],'w').write('\n'.join(p.extract_text() or '' for p in r.pages))" "RAW/<datei>.pdf" "<scratchpad>/<slug>.txt"
```

Ziel in den Scratchpad schreiben, nicht nach `/tmp` (Sandbox blockt `/tmp`). Die Read-Tool-PDF-Anzeige braucht poppler (nicht installiert) — der `pypdf`-Weg umgeht das.

**Format-Vorrang: epub.** epub ist die saubere Quelle und bleibt erste Wahl. Liegt für ein Buch **keine epub** vor (nur PDF/mobi/o. Ä.), **vor** dem Verarbeiten beim User nachfragen, ob er noch eine epub-Version ins RAW legen kann. Will er nicht oder gibt es keine: PDF direkt via `pypdf` verarbeiten (vgl. `softwar`, Pass 96) — dann ist die PDF selbst die verbatim-Quelle in `_INGESTED`, kein separater `.md`-Extrakt nötig. Liegen epub **und** PDF vor: epub extrahieren, die PDF in `_INGESTED` als `DUPLIKAT` markieren (vgl. Steiner, `bitcoins-verwahren-und-vererben`).

## 3. Pipeline (Schritt für Schritt)

1. Extrahieren → Scratchpad (Schritt 2 oben).
2. `RAW/<slug>.md` anlegen: Frontmatter (`title` / `author` / `source_url` / `date_added` / `date_published` / `type: Book` / `tags: [buecher]`) + Volltext.
3. `RAW/_INGESTED.md`: **beide** Zeilen registrieren — den `.md`-Extrakt **und** die `.epub`-Quelle («Quell-EPUB für Ingest … Compiliert in: `<slug>`»). Das doppelte Registrieren ist Pflicht, sonst driftet `check_raw_status.py` (die 19-NEU-Aufräumung vom 15.7.2026 kam genau von fehlenden epub-Zeilen).
4. `Wiki/<slug>.md` schreiben: Struktur nach `../CLAUDE.md` (*Wiki article standard*), Schweizer Hochdeutsch, eigenformuliert — **kein Buchtext reproduzieren** (Copyright).
5. Slug in `BUECHER_SET` (`tools/classify_topics.py`).
6. INDEX-Zeile im Buch-Block (oben, vor den übrigen Artikeln); Compile-Pass-Nr. im Header hochziehen.
7. Regen: `classify_topics.py --write` → `rank_articles.py --csv Outputs/ranking.csv` → `layout_map.py`. Tags per Report sanity-checken, Fehltreffer über `OVERRIDES` fixen (nie die `**Themen:**`-Zeile von Hand).
8. Verifizieren: `check_raw_status.py` = 0/0/0, Slug in `PEAKS` (Visualizer), keine kaputten Backlinks.
9. CHANGELOG als `## YYYY-MM-DD — Compile pass N`.
10. Fragen, ob die Themenkarten neu gebaut werden sollen (`python3 tools/build_theme_cards.py`) — nie automatisch (vgl. Compile-Protokoll Schritt 7 in `CLAUDE.md`).

## 4. Namensregeln

- **Wiki-Slug:** kein Autor, deskriptiv kebab-case (`der-bitcoin-standard`, nicht `der-bitcoin-standard-ammous`). Autor in Überschrift und INDEX-Beschreibung.
- **RAW-Extrakt-Dateiname:** darf den Autor tragen (`Der-Bitcoin-Standard_Ammous.md`, `2016_Internet-of-Money-Vol1_Antonopoulos.md`). RAW behält Herkunft; die «kein Autor»-Regel gilt nur fürs Wiki-Slug, nicht für RAW-Dateien.

## 5. Lizenz-Konvention

Offene Lizenz des Originals im Wiki-Artikel **und** in der `_INGESTED`-Zeile nennen. Beispiele: `einfuehrung-in-das-lightning-netzwerk` → Original lnbook, CC-BY-SA 4.0; `magic-future-money` → CC BY-NC-ND 4.0; `bitcoin-development-philosophy` → CC BY 4.0. Trägt die verarbeitete Ausgabe einen restriktiveren Verlags-Copyright als das offen lizenzierte Original, beides vermerken (welche Ausgabe extrahiert, welche offen ist).

## 6. Rückverlinkung aus Konzept-Artikeln

Nicht-Buch-Artikel verlinken 1–2 thematisch passende Bücher unter `## Related`, **zuunterst**, mit `← Buch`-Marker. Format (Alias-Syntax, damit der Backlink funktioniert und lesbar bleibt):

```
## Related
- [[opsec-und-privatsphaere]]
- [[das-privacy-handbuch|Das Privacy Handbuch (Timo Volkov)]] ← Buch
```

Beim Schreiben oder Anfassen eines Konzept-Artikels prüfen, ob ein Buch aus `BUECHER_SET` thematisch passt, und ggf. so verlinken. Umgekehrt bleibt es bei den normalen `[[slug]]`-Backlinks.

## 7. Fallstricke

- **Ordner-Epubs** (`buch.epub/` als entpackter Ordner) blähen `check_raw_status.py` mit hunderten Interna auf. Als einzelne `.epub`-Datei ablegen, diese eine Datei registrieren.
- **`_INGESTED` doppelt** (md + epub) — sonst NEU-Drift.
- **Belletristik** nicht als «These» zusammenfassen (Tier A Sonderfall, Schritt 1).
- **Extraktor-Ziel** in den Scratchpad, nicht `/tmp` (Sandbox).
