# Book ingestion — bitcoin_kb

The full procedure lives in `../_BOOK_INGESTION.md` (depth tiers, extraction, pipeline, naming and licence rules, back-linking, pitfalls). This file records only what bitcoin_kb adds. Precedence: `CLAUDE.md` beats both runbooks where they conflict.

## Additional pipeline steps

After step 4 of the generic runbook (wiki article written):

1. Add the slug to `BUECHER_SET` in `tools/classify_topics.py`. Without that entry the book never gets the `buecher` tag — the list is a curated allowlist, not a keyword match.
2. Put the INDEX line in the book block (at the top, ahead of the other articles) and bump the compile pass number in the header.
3. Recompute, in this order:

```
python3 tools/classify_topics.py --write
python3 ../_tools/rank_articles.py \
  --wiki-url "https://github.com/TLausZ/Bitcoin-Knowledge-Base-WIKI/blob/main/Wiki/" \
  --csv Outputs/ranking.csv
python3 tools/layout_map.py
```

Sanity-check the tags from the report and fix wrong hits via `OVERRIDES`, never by hand-editing the `**Themen:**` line.

4. Verify: `python3 ../_tools/check_raw_status.py` reports 0/0/0, the slug appears in `PEAKS` (visualizer), no broken backlinks.
5. Ask whether the theme cards should be rebuilt (`python3 tools/build_theme_cards.py`) — never automatically, see compile protocol step 7 in `CLAUDE.md`.

## Status convention for work-referat articles

Lives in `../_BOOK_INGESTION.md` §1a (workspace-wide since 27 July 2026; originally decided here). bitcoin_kb note: the convention also covers `bitcoin-core-relay-statement` — a signed authoritative document rendered as its own article.

## Precedents in the corpus

When placing a new book, the ones already processed help:

| Case | Example |
|---|---|
| Tier A, fiction special case | `magic-future-money` — premise and themes instead of "the thesis" |
| Tier C, technical book | `mastering-bitcoin`, `einfuehrung-in-das-lightning-netzwerk` |
| epub and PDF both present, PDF marked DUPLIKAT | `bitcoins-verwahren-und-vererben` (Steiner) |
| PDF only, processed directly via `pypdf` | `softwar` (pass 96) |
| open licence recorded | `einfuehrung-in-das-lightning-netzwerk` (lnbook, CC-BY-SA 4.0), `magic-future-money` (CC BY-NC-ND 4.0), `bitcoin-development-philosophy` (CC BY 4.0) |

## Where the rules came from

The requirement to register both the `.md` extract and the `.epub` source file in `_INGESTED.md` comes out of the 15 July 2026 cleanup: 19 books were being reported as NEU indefinitely because only the extract had been registered.
