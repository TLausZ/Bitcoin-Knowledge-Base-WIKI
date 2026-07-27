# tools/

KB-specific Python scripts for bitcoin_kb: topic tagging and visualizer layout.
All run on the standard library (Python 3.9+).

**Every command in this file is run from the KB root** (`bitcoin_kb/`), not from
this folder. Read the paths accordingly: `tools/x.py` lives here, `../_tools/x.py`
one level above the KB root.

The shared scripts live in `KNOWLEDGE/_tools/` and serve every knowledge base:

| Script | Call from the KB root | Purpose |
|---|---|---|
| check_raw_status.py | `python3 ../_tools/check_raw_status.py` | Reconciles `RAW/` against `RAW/_INGESTED.md`, the only valid source of "new" |
| rank_articles.py | `python3 ../_tools/rank_articles.py` | Weights wiki articles, produces `Outputs/ranking.csv` |
| extract_epub.py | `python3 ../_tools/extract_epub.py` | epub full-text extraction for book ingestion |

Details in the README next to those scripts (`KNOWLEDGE/_tools/README.md`).

## classify_topics.py

Assigns one to six visualizer topics to each wiki article (signal: slug plus
INDEX description) and writes a `**Themen:**` line directly below `**Status:**`.
Without `--write` it only reports.

```
python3 tools/classify_topics.py            # report
python3 tools/classify_topics.py --write    # writes the topic lines
```

Corrections belong in the `OVERRIDES` map at the top of the script, never in the
`**Themen:**` line inside an article — the next `--write` overwrites it.
`satoshi`, `zitate` and `buecher` are curated allowlists (`SATOSHI_SET`,
`ZITATE_SET`, `BUECHER_SET`); a slug joins one only by being entered there.

## layout_map.py

Computes the layout for the topographic map `Visualizer/index.html`. Reads the
link graph from `Wiki/` and the scores from `Outputs/ranking.csv`, runs a
Fruchterman-Reingold layout (linked articles attract each other, fixed seed, so
it's reproducible) and replaces the embedded `PEAKS` constant in the HTML.

## build_theme_cards.py

Rebuilds the theme cards `Visualizer/themen/*.html`. Never runs automatically —
after a compile pass, ask whether the cards should be updated.

## build_screensaver_maps.py

Rewrites `Visualizer/screensaver-maps.js`. Under `file://` the screensaver reads
that file and would otherwise show the old cards. Always run it together with
`build_theme_cards.py`.

## Typical sequence after a compile pass

```
python3 tools/classify_topics.py --write
python3 ../_tools/rank_articles.py \
  --wiki-url "https://github.com/TLausZ/Bitcoin-Knowledge-Base-WIKI/blob/main/Wiki/" \
  --csv Outputs/ranking.csv
python3 tools/layout_map.py
```

After that the main map reflects the current state. To bring the theme cards and
the screensaver along:

```
python3 tools/build_theme_cards.py
python3 tools/build_screensaver_maps.py
```
