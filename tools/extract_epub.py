#!/usr/bin/env python3
"""Extrahiert epub-Volltext verbatim in Spine-Reihenfolge.

Leaf-Block-Logik: Block-Tags {h1-6,p,li,blockquote,div}, nur Elemente OHNE
verschachtelten Block ausgeben (sonst Div-Prosa doppelt/verloren). Überschriften
als Markdown-#. Div nötig, weil manche Epubs Prosa in <div> statt <p> legen.

    python3 tools/extract_epub.py "RAW/<datei>.epub"        # nach stdout
    python3 tools/extract_epub.py "RAW/<datei>.epub" out.md  # in Datei
"""
import sys
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

BLOCK = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "div"]
HEAD = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}


def extract(path):
    book = epub.read_epub(path)
    id_order = [i[0] for i in book.spine]
    items = {it.id: it for it in book.get_items_of_type(ITEM_DOCUMENT)}
    out = []
    for iid in id_order:
        it = items.get(iid)
        if not it:
            continue
        soup = BeautifulSoup(it.get_content(), "html.parser")
        for el in soup.find_all(BLOCK):
            if el.find(BLOCK):  # ponytail: nur Leaf-Blöcke, sonst Div-Prosa doppelt
                continue
            text = el.get_text(" ", strip=True)
            if not text:
                continue
            out.append(HEAD.get(el.name, "") + text)
    return "\n\n".join(out)


if __name__ == "__main__":
    text = extract(sys.argv[1])
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f:
            f.write(text)
        print(f"{len(text.split())} Wörter -> {sys.argv[2]}")
    else:
        print(text)
