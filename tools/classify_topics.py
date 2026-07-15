#!/usr/bin/env python3
"""Ordnet jedem Wiki-Artikel 1-3 Themen zu (Signal: Slug + INDEX-Beschreibung).

Schreibt/aktualisiert eine `**Themen:** ...`-Zeile direkt nach `**Status:**`.
Ohne --write nur Report. Manuelle Korrekturen in OVERRIDES gewinnen immer.
"""
import re
import sys
import unicodedata
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "Wiki"
NAV = {"INDEX.md", "QUESTIONS.md", "CLAUDE.md", "CHANGELOG.md", "_INGESTED.md"}

# Kanonische Tag-Tokens -> Anzeigename (Anzeigename lebt sonst im HTML)
CATS = ["grundlagen", "protokoll", "bips", "self-custody", "privacy", "mining",
        "lightning", "oekonomie", "philosophie", "adoption", "kritik",
        "geschichte", "satoshi", "zitate", "studien", "buecher", "wallets",
        "sonstiges"]

# Beim Kappen zuerst behalten: spezifische/Leaf-Themen. Breite Sammelthemen
# (protokoll, grundlagen) fliegen zuerst raus, damit z.B. 'geschichte' bleibt.
# Kuratierte Tags (satoshi/zitate/studien/buecher) stehen zuoberst -> nie gekappt.
KEEP_PRIORITY = ["satoshi", "zitate", "studien", "buecher", "kritik", "geschichte",
                 "wallets", "mining", "lightning", "privacy", "self-custody",
                 "adoption", "oekonomie", "philosophie", "protokoll", "grundlagen",
                 "bips"]
MAX_TAGS = 6

# Satoshi: nur direkter persönlicher Einfluss (sein Paper, seine Zitate, sein
# Code, Identitätsdebatte). Bewusst kuratiert statt Keyword — sonst würde alles
# als "Satoshi" landen, weil ganz Bitcoin von ihm stammt. wallet-of-satoshi,
# cypherpunk-manifest etc. gehören NICHT rein.
SATOSHI_SET = {
    "bitcoin-whitepaper", "bitcoin-whitepaper-errata", "satoshi-zitate",
    "satoshi-ankuendigung-2009", "bitcoin-launch-januar-2009",
    "craig-wright-faketoshi", "bitcoin-fruehgeschichte",
    "bitcoin-ip-transaktionen",
}

# Zitate: nur echte Zitatsammlungen, nicht Artikel die jemanden zitieren.
ZITATE_SET = {"satoshi-zitate", "zitate"}

# Studien: nur Artikel die selbst eine Studie/ein Report/Forschung sind,
# nicht solche die eine Studie bloss zitieren (greenpeace, volatilitaet …).
STUDIEN_SET = {
    "bitcoin-adoption-report-river-2026", "bitcoin-adoptionsstudie-2026-dach",
    "bitcoin-akademische-forschung-bbr", "crypto-adaption-europa-bsd-2026",
    "crypto-assets-study-ifz-2021-2025", "kryptoanlagen-schweiz-hslu-2026",
    "bitcoin-energie-messung-beest", "onchain-indikatoren-und-anlegerverhalten",
    # Mining/Energie-Evidenzblock (Studien-/Datensynthesen)
    "bitcoin-mining-narrativ-und-kritik", "bitcoin-mining-energiequellen",
    "bitcoin-mining-netz-und-oekonomie", "greenpeace-vs-bitcoin",
}

# Bücher: nur Artikel die ein konkretes Buch zusammenfassen, nicht solche die
# eines bloss zitieren. Wächst, sobald Buch-Zusammenfassungen als eigene
# Artikel angelegt werden (siehe Wiki/QUESTIONS.md).
BUECHER_SET = {
    "bitcoin-alles-geteilt-durch-21-millionen",
    "bitcoin-inverse-of-clown-world", "praxeology",
    "bitcoin-unabhaengigkeit-neu-gedacht",
    "internet-of-money-vol1", "internet-of-money-vol2", "internet-of-money-vol3",
    "origins-of-money", "blocksize-war",
    "bitcoins-verwahren-und-vererben", "das-privacy-handbuch",
    "grokking-bitcoin", "mastering-bitcoin",
    "bitcoin-development-philosophy",
    "der-bitcoin-standard", "der-fiat-standard", "gesetze-der-wirtschaft",
    "the-bitcoin-handbook", "goldene-zukunft", "das-buch-satoshis",
    "das-kleine-bitcoin-buch", "das-trojanische-pferd-der-freiheit",
    "hidden-repression_how-the-imf-and-world-bank-sell-exploitation-as-development",
    "einfuehrung-in-das-lightning-netzwerk", "magic-future-money",
}

# (tag, regex) — trifft gegen slug + " " + beschreibung (lowercase, ascii-gefaltet)
RULES = [
    ("self-custody", r"hardware.?wallet|seed|backup|multisig|passphrase|airgap|anti.?klepto|phishing|diceware|shamir|vererbung|selbstverwahr|selbstverant|cold.?storage|fortego|vault|firmware|supply.?chain|evil.?maid|migration|einstieg|onboard|hardware.?wallet.?angriff"),
    ("wallets", r"sparrow|electrum|specter|nunchuk|muun|phoenix|wallet.?of.?satoshi|bitbox02|liana|joinmarket|walletconnect|bitblik|core.?lightning|blockstream"),
    ("privacy", r"privat|opsec|coinjoin|coin.?control|utxo|no.?kyc|silent.?payment|joinmarket|payment.?code|nostr|biometrie|ueberwach|zensurresist|redefreiheit|lightning.?address.?datenschutz"),
    ("mining", r"mining|proof.?of.?work|hashcash|energie|energy|hashrate|schwierigkeit|difficulty|chainwork|greenpeace|beest|energiestandard|double.?sha256"),
    ("lightning", r"lightning|\bark\b|statechain|fedimint|splicing|rebalancing|phoenix|schichtenarchitektur|skalierung|zahlungen|payment.?request"),
    ("oekonomie", r"geld|inflation|oesterreich|monetae|monetar|fiat|schulden|knappheit|kapital|deflation|\bzins|makro|reserve|hyperbitcoin|\betf\b|kredit|steuer|volatil|preis|finanzial|entfinanz|dollar|cbdc|stablecoin|s2f|basisgeld|power.?law|werttheorie|praxeolog|inflationsschutz|spekulation|schuldenzykl|quantitativ|silent.?ipo"),
    ("protokoll", r"transaktion|\bblock|merkle|sha256|script|segwit|taproot|musig|frost|schnorr|elliptische|signatur|ecdsa|adress|schluessel|schlussel|konsens|mempool|\bnode|netzwerk|fork|covenant|starks|op.?return|datenformat|zeitstempel|whitepaper|hd.?wallet|derivation|quanten|miniscript|chainwork|block.?header|witness|nicht.?blockchain|nicht.?kopierbar|datenspeicher|burn.?address|nonce"),
    ("philosophie", r"cypherpunk|kryptoanarch|philosoph|spiritual|\bgigi|szabo|manifest|hacker|freiheit|naturrecht|menschenrecht|antifragil|organismus|psycholog|kommunikation|orange|\bbildung|konferenz|community|spieltheorie|amerikan|recht.?sprache|commons|frauen|\bidee\b|selbsteigentum|selbstverantwortung|informationstheorie|entropie|value4value|wolf|breedlove|gigi|nicht.?blockchain|trojanisch|paradigmen|fiktion|hoffnung"),
    ("adoption", r"adoption|regulier|el.?salvador|humanitaer|unternehmen|strategie|institutionell|kolonial|\biwf|weltbank|neofeudal|studie|europa|dach|schweiz|hslu|\bifz|menschenrecht|reserve|etf|silent.?ipo|onboarding|island|nation"),
    ("kritik", r"kritik|fehlannahmen|fehlwahrnehmung|greenpeace|faketoshi|craig.?wright|rechtliche.?angriffe|proof.?of.?stake.?kritik|narrativ.?und.?kritik|ponzi|angriff|mt.?gox|missverstaendnis|widerleg"),
    ("geschichte", r"fruehgeschichte|launch|ankuendigung.?2009|januar.?2009|\bmt.?gox|blocksize.?war|core.?client.?history|hashcash|digitales.?zeitstempel|satoshi.?zitate|satoshi.?ankuend|cypherpunk.?manifest|silk.?road|history|1998|2009|whitepaper|faketoshi|craig.?wright"),
    ("grundlagen", r"wie.?funktioniert|whitepaper|einsteiger|einstieg|grundlagen|was.?ist|\bnodes|netzwerk.?und.?nodes|kaufen.?und.?dca|adresstypen|adoption.?reise|bitcoin.?vs.?krypto|bitcoin.?bildung|schluessel.?und.?adressen"),
]

# BIP-Titel-Keywords -> Zweit-Tag (BIPs sind immer bips+protokoll)
BIP_SECOND = [
    ("self-custody", r"mnemonic|seed|hd wallet|deterministic|key derivation|multisig|multi-sig|passphrase|backup|hardware|descriptor|output script|wallet"),
    ("privacy", r"payment code|reusable|silent payment|bloom|privacy|dandelion|tor|prevent"),
    ("lightning", r"lightning|payment|invoice|bolt|channel"),
    ("mining", r"mining|version bits|difficulty|block reward|coinbase"),
]

OVERRIDES = {
    # gezielte Korrekturen nach Report-Review, slug -> Themenliste
    "bitcoin-versicherung": ["oekonomie", "self-custody"],
    "zitate": ["zitate", "philosophie"],
    "mt-gox": ["geschichte", "kritik", "self-custody"],
    # Gigi-Essay: Geld-Ethik + Selbstverwahrung, nicht "protokoll"/"adoption" (Trigger: node)
    "bitcoin-ist-die-wiederentdeckung-des-geldes": ["oekonomie", "philosophie", "self-custody"],
    # Menger 1892: Geldursprung/Werttheorie, nicht "kritik" (Trigger war "Widerlegung")
    "origins-of-money": ["oekonomie", "philosophie", "buecher"],
    # SciFi-Anthologie: Geld-Zukunftsszenarien, nicht "mining" (Trigger war Energie-Story «Xtra Watt»)
    "magic-future-money": ["oekonomie", "philosophie", "buecher"],
}


def norm(s):
    return unicodedata.normalize("NFC", s.strip().removesuffix(".md"))


def fold(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.replace("ß", "ss")


def parse_index():
    """slug -> beschreibungstext (aus beiden INDEX-Tabellen)."""
    desc = {}
    for line in (WIKI / "INDEX.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*\[\[([^\]]+)\]\]\s*\|(.*)", line)
        if m:
            desc[norm(m.group(1))] = m.group(2)
    return desc


def classify(slug, desc):
    if slug in OVERRIDES:
        return OVERRIDES[slug]
    is_bip = bool(re.match(r"bip-?\d", slug))
    hay = fold(slug.replace("-", " ") + " " + desc)
    tags = []
    if is_bip:
        # BIPs bleiben in ihrem eigenen Bucket, damit sie 'protokoll' nicht fluten.
        tags = ["bips"]
        for tag, pat in BIP_SECOND:
            if re.search(pat, hay) and tag not in tags:
                tags.append(tag)
        return tags[:3]
    for tag, pat in RULES:
        if re.search(pat, hay):
            tags.append(tag)
    if slug in SATOSHI_SET:
        tags.append("satoshi")
    if slug in ZITATE_SET:
        tags.append("zitate")
    if slug in STUDIEN_SET:
        tags.append("studien")
    if slug in BUECHER_SET:
        tags.append("buecher")
    tags = set(tags)
    if not tags:
        return ["sonstiges"]
    # nach Spezifitaet kappen, dann nach CATS fuer die Anzeige sortieren
    kept = [t for t in KEEP_PRIORITY if t in tags][:MAX_TAGS]
    return [t for t in CATS if t in kept]


def main():
    write = "--write" in sys.argv
    desc = parse_index()
    slugs = sorted(norm(p.stem) for p in WIKI.glob("*.md") if p.name not in NAV)
    dist = Counter()
    per = {}
    missing_desc = 0
    for slug in slugs:
        d = desc.get(slug, "")
        if not d:
            missing_desc += 1
        tags = classify(slug, d)
        per[slug] = tags
        for t in tags:
            dist[t] += 1
    print(f"{len(slugs)} Artikel, {missing_desc} ohne INDEX-Beschreibung\n")
    for c in CATS:
        print(f"{dist[c]:>4}  {c}")
    print(f"\nSchnitt Tags/Artikel: {sum(len(v) for v in per.values())/len(per):.2f}")
    # kuratierte/kleine Kategorien voll auflisten zur Kontrolle
    for cat in ("satoshi", "zitate", "studien", "buecher", "sonstiges"):
        members = [s for s, t in per.items() if cat in t]
        print(f"\n{cat} ({len(members)}): {', '.join(members)}")
    if write:
        n = 0
        for p in WIKI.glob("*.md"):
            if p.name in NAV:
                continue
            slug = norm(p.stem)
            line = "**Themen:** " + ", ".join(per[slug])
            txt = p.read_text(encoding="utf-8")
            if re.search(r"^\*\*Themen:\*\* .*$", txt, flags=re.M):
                txt = re.sub(r"^\*\*Themen:\*\* .*$", line, txt, count=1, flags=re.M)
            else:
                # nach **Status:**-Zeile einfuegen
                txt, c = re.subn(r"(^\*\*Status:\*\* .*$)", r"\1\n" + line.replace("\\", "\\\\"), txt, count=1, flags=re.M)
                if c == 0:
                    print("  WARN kein Status-Feld:", slug)
                    continue
            p.write_text(txt, encoding="utf-8")
            n += 1
        print(f"\n{n} Artikel mit **Themen:** geschrieben.")


if __name__ == "__main__":
    main()
