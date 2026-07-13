# Open Questions & Gaps

Offene Fragen, Lücken und Themen, die mehr Quellen benötigen. Stand: 2026-07-05 (Health Check 3)

## Gebrochene Backlinks (Health Check 3, 2026-07-05)

Related-Links auf Artikel, die nie erstellt wurden. Pro Link: erstellen, auf bestehenden Artikel umbiegen oder entfernen?

- `[[bitcoin-als-reserve-und-anlagegut]]` ← iwf-weltbank-strukturanpassung, value4value-und-wertaktivierendes-web (Kandidaten: bitcoin-als-strategische-reserve, bitcoin-etf-und-institutionelle-verwahrung)
- `[[bitcoin-als-zahlungsmittel]]` ← value4value-und-wertaktivierendes-web (Kandidat: bitcoin-skalierung-und-zahlungen)
- `[[bitcoin-fuer-entwicklungslaender]]` ← iwf-weltbank-strukturanpassung (Kandidaten: monetaerer-kolonialismus-cfa-franc, bitcoin-humanitaere-anwendungen)
- `[[proof-of-work-grundlagen]]` ← iwf-weltbank-strukturanpassung, value4value-und-wertaktivierendes-web (Kandidaten: bitcoin-mining-und-proof-of-work, energiestandard-und-proof-of-work)
- `[[cantillon-effekt]]` ← bitcoin-menschenrechte (im Fliesstext bereits mit Fallback auf geldpolitik-und-inflation markiert)
- `[[cantillon-effekt-und-geldpolitik]]` ← iwf-weltbank-strukturanpassung (Kandidat: geldpolitik-und-inflation)
- `[[geldgeschichte-und-sound-money]]` ← energiestandard-und-proof-of-work (Kandidat: szabo-geldursprung)
- `[[gigi-bitcoin-als-naturgewalt]]`, `[[bitcoin-ist-die-wiederentdeckung-des-geldes]]` ← gigi-philosophische-essays (geplante Essay-Artikel; RAW-Quellen vorhanden)

Stale Source-Zitate (Ziel-Datei existiert nicht mehr in RAW):

- `[[2026-06-09_nunchuk-faq]]` und `[[Recover a Nunchuk Wallet with Sparrow (2026)]]` ← nunchuk-wallet.md. Erstere laut Registry ersetzt durch die zwei zitierten FAQ-Dateien, letztere Datei wurde entfernt. Zitate löschen?
- `[[2026-06-29_bitcoin-gespraechsskript-fehlannahmen]]` ← bitcoin-fehlannahmen.md zeigt auf eine Datei in Outputs/ statt RAW. Als Eigenproduktion kennzeichnen oder Zitat entfernen?

## Fehlende Wiki-Artikel

- **Coin Control** → erledigt: `coin-control-und-utxo-auswahl.md` erstellt
- **Lightning-Grundlagen** → erledigt: `lightning-netzwerk-grundlagen.md` erstellt
- **WalletConnect / DApps** → erledigt: `walletconnect-und-dapps.md` erstellt

Derzeit keine bekannten Lücken ausser den Kandidaten unten.

## Geplant: einzelne Studien und Bücher als eigene Wiki-Artikel (später)

Viele Studien und Bücher leben aktuell nur *innerhalb* von Artikeln (v.a. der BBR-Hub `bitcoin-akademische-forschung-bbr` bündelt >40 Studien) oder als RAW-Quellen — sie sind keine eigenen Knoten auf der Karte. Plan (vom User bestätigt 2026-07-13): echte Studien-Papers und Bücher als je eigene, zusammengefasste Wiki-Artikel anlegen, strukturell ähnlich der BIP-Sammlung. Jeder bekäme dann automatisch sein `studien`- bzw. `buecher`-Tag (via STUDIEN_SET/BUECHER_SET in classify_topics.py, oder bei grösserer Menge ein Slug-Muster + Regel). Priorität laut User: Mining/Energie-Studien zuerst. Buch-Artikel bisher nur `wolf-21-lektionen` und `bitcoin-alles-geteilt-durch-21-millionen`. Noch nicht begonnen.

Bücher-Quellen bereits im RAW (verifizierte Inventur 2026-07-13: 8 EPUB-Dateien + 1 MOBI = 7 verschiedene Bücher; Dubletten durch EN/DE-Ausgaben und Formatkopien) als Material für eigene Buch-Artikel:

- Knut Svanholm — *Bitcoin: Everything Divided by 21 Million* (2022, EN) — Artikel existiert (`bitcoin-alles-geteilt-durch-21-millionen`); Dubletten: DE-Ausgabe *Alles durch 21 Millionen* (2023) als EPUB **und** MOBI — alles dasselbe Buch, ein Artikel
- Knut Svanholm / Volker Herminghaus — *Bitcoin: Unabhängigkeit neu gedacht* (2020, DE)
- Knut Svanholm, Luke de Wolf — *Bitcoin: The Inverse of Clown World* (2024, EN)
- Knut Svanholm — *Praxeology: The Invisible Hand That Feeds You* (2023, EN)
- Marc Steiner — *Bitcoins verwahren und vererben: Ein praktischer Ratgeber* (2020, DE)
- *Das Privacy Handbuch: Ein Ratgeber für digitale Sicherheit und Privatsphäre*
- Kalle Rosenbaum — *Grokking Bitcoin* (2018, Manning)

Beim späteren Anlegen der Buch-Artikel: eine Datei pro Buch als Quelle wählen (bevorzugt die Originalsprache), die übrigen Ausgaben/Formate als weitere Sources nennen, nicht je einen eigenen Artikel.

**Harte Regel (Urheberrecht): Bücher nie reproduzieren.** Der Artikel ist eine eigene, deutlich kürzere Synthese in eigenen Worten — kein Volltext, keine langen Passagen, keine kapitelweise Nacherzählung, die das Buch ersetzt. Verbatim-Zitate nur sehr sparsam und mit Quellenangabe. Wie tief gelesen wird (ganzes Buch vs. ausgewählte Kapitel), wird pro Buch beim Schreiben entschieden — nicht vorab festgelegt.

## Offene Spannungen und Fragen

**Miner-Incentives nach Halving:** → beantwortet (2026-06-20). Beide RAW-Quellen ingested (Carlsten et al. CCS 2016, Budish QJE 2024). Wiki-Artikel erweitert. Ausgang bleibt offen — empirisch unentschieden.

**OP_RETURN-Limit (Bitcoin Core 29+):** Wurde das 80-Byte-Standardlimit abgeschafft? `op-return-und-datenspeicherung.md` hält die Frage offen. Neue RAW-Quellen erforderlich.

**AOPP-Nachfolge:** Mehrere Schweizer Hersteller haben AOPP 2022 entfernt. Gibt es eine datenschutzkonforme Adressverifizierungslösung? `regulierung-tofr-aopp.md` deckt den Rückzug ab, aber keine Nachfolgelösung.

**FROST-Implementierungen:** Wann werden MuSig2/FROST in gängigen Hardware-Wallet-Softwares breit verfügbar? `taproot-musig2-frost.md` und `multisig-und-kollaborative-verwahrung.md` erwähnen FROST als emerging — kein Update seit 2024.

**EU-Regulierung (MiCA/AML):** Stand nach März 2024? `eu-regulierung-selbstverwahrung.md` und `regulierung-tofr-aopp.md` enden dort. Neue Entwicklungen ausstehend.

**Ark-Reifegrad:** `skalierung-lightning-ark-statechains.md` hat Stand Dez. 2025. Aktuelle Implementierungsfortschritte unklar.

**BOLT 12 / Offers:** `lightning-netzwerk-grundlagen.md` erwähnt BOLT 12 als offene Frage. Welche Wallets unterstützen es produktiv, und wie verändert es die Privatsphäre gegenüber BOLT 11?

**Multi-Path-Payments (MPP):** Privatsphäre-Implikationen gegenüber Single-Path in `lightning-netzwerk-grundlagen.md` als offene Frage markiert. Keine RAW-Quellen vorhanden.

## Artikel-Kandidaten (Held — zu wenig Evidenz)

- **Bitcoin-Einsteigerleitfaden** → erledigt (2026-07-05): Michael Wolfs «Bitcoin-Ratgeber» (10 Kapitel in RAW) liefert den praktischen Onboarding-Weg, der bisher fehlte. Artikel `bitcoin-einsteiger-onboarding.md` erstellt (Fünf-Schritte-Umzug, Testbetrag), plus `wolf-21-lektionen.md`.

- **bitcoin-als-inflationsschutz** — erledigt: Artikel existiert.

- **bitcoin-kiosk-regulierung** — `Bitcoin_Kiosk_Paper_July_ 2025.pdf` (Eric Peterson, Satoshi Action, Juli 2025) in RAW vorhanden. US-spezifisches Nischenthema; Artikel erst dann, wenn weitere Policy-Quellen verfügbar.

- **bitcoin-kommunikation / Orange-Pilling** → erledigt (2026-06-30): Mit `Bitcoin's Most Important Fork: The Influence Upgrade` (Daniel Batten) liegt die zweite Quelle vor. Artikel `bitcoin-kommunikation-und-orange-pilling.md` erstellt (OrangePilling + Influence Upgrade: 7 Prinzipien, Sector Ambassadors, Crossing the Chasm).

## Heart-Money-Kompilierung (Etappe A, 2026-07-04)

**Perrenod: log-periodisch vs. mechanistisch:** Das log-periodische Zyklusmodell (Peak-These 2027) ist nur aus zweiter Hand belegt (Newsletter referiert Interview/Video). Wie verhält es sich formal zur mechanistischen Power-Law-Herleitung von Santostasi & Perrenod? Primärquelle für RAW gesucht (Perrenod-Substack oder Original-Interview).

**Nowaks Medium-Artikel 2023:** «Lohnt sich ein Konsumentenkredit, um Bitcoin zu kaufen?» ist die Vorgängeranalyse zur Sonderausgabe #02 und fehlt in RAW. Kandidat für Nachingest (nicoleenowak.medium.com).

**Kredit-Rückrechnung 2022–2026:** Nowaks Datenreihe endet mit Einstiegsmonat Okt 2021. Wie schneiden Kredit-Einstiege 2022–2026 ab, insbesondere nach dem Zyklusbruch? Eigene Nachrechnung möglich (Excel-Sheet verlinkt).

**Volksbank/21bitcoin-Kreditprodukt:** Ankündigung Okt 2025, Produktdetails (LTV-Grenzen, Verwahrung, Zins) ausstehend — beobachten.

**Spannung Entfinanzialisierung vs. Buy-Borrow-Die:** Parker Lewis' These (Bitcoin befreit vom Zwang, Geld arbeiten zu lassen) und die Beleihungsstrategie refinanzialisieren denselben Bestand. Konzeptioneller Widerspruch oder Phasenfrage (Aufbau vs. Entnahme)?

**Ausstehende Etappen:** → erledigt (2026-07-05): Alle vier Etappen kompiliert, alle 51 Heart-Money-Dateien in _INGESTED.md final vermerkt.

## Heart-Money-Kompilierung (Etappen C+D, 2026-07-05)

**Iran/Hormus (FT, April 2026):** Nur als Sekundärbezug im Newsletter belegt. FT-Primärartikel als RAW-Kandidat; beobachten, ob die Bitcoin-Gebühren tatsächlich eingeführt wurden (andere Berichte nannten auch den Yuan).

**Bundestagspetition Haltefrist:** Ausgang offen (Stand Juni 2026). Petitionstext von prohaltefrist.de, Mitzeichnungszahlen und ggf. Anhörung nachverfolgen; §23 EStG und österreichische Regelung 2022 als Primärquellen für RAW.

**Michigan-State-Paper + Quittem-Primärquellen:** «The Most Trustworthy Coin» (rickwash.com) und Quittems Persönlichkeits-Untersuchung liegen nur aus zweiter Hand vor — Nachingest-Kandidaten (siehe Open Questions in bitcoin-und-psychologie).

**Benners «The Frequency of Money»:** Buch war 2026 angekündigt; nach Erscheinen als RAW-Kandidat zur Prüfung der Frequenz-These aus erster Hand.

**Milgram 85/15:** Die Verallgemeinerung ist eine Praktikerin-Faustformel, keine Studienlage — im Artikel so gekennzeichnet; bei Gelegenheit gegen die Replikationsliteratur zu Milgram prüfen.

## Bitcoin-Ratgeber-Kompilierung (2026-07-05)

**Kapitel 1 (Was ist Geld?) breit verlinkbar:** Der Ratgeber deckt Geldeigenschaften, Goldstandard, Petrodollar, Cantillon-Effekt und Proof-of-Work-als-Vertrauen ab. Kompiliert wurde nur nach `szabo-geldursprung`. Bei Gelegenheit prüfen, ob `geldpolitik-und-inflation` (Cantillon), `geld-staat-und-fiat-monopol` (Petrodollar) und `bitcoin-mining-und-proof-of-work` (PoW als Vertrauen) den Ratgeber ebenfalls als Beleg aufnehmen sollten.

**Michael Wolf / Bitcoinlighthouse als Quelle:** Bislang nur der Ratgeber ingestiert. Workshops, Newsletter und die Vererbungs-Beratungsseite (bitcoinlighthouse.de) sind Werbung im Buch, keine eigenständigen Quellen — kein Nachingest nötig, solange keine inhaltlichen Texte vorliegen.
