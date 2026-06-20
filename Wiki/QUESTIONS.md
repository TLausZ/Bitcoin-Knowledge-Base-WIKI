# Open Questions & Gaps

Offene Fragen, Lücken und Themen, die mehr Quellen benötigen. Stand: 2026-06-20 (nach Health Check 1 Follow-up)

## Fehlende Wiki-Artikel

- **Coin Control** → erledigt: `coin-control-und-utxo-auswahl.md` erstellt
- **Lightning-Grundlagen** → erledigt: `lightning-netzwerk-grundlagen.md` erstellt
- **WalletConnect / DApps** → erledigt: `walletconnect-und-dapps.md` erstellt

Derzeit keine bekannten Lücken ausser den Kandidaten unten.

## Offene Spannungen und Fragen

**Miner-Incentives nach Halving:** → beantwortet (2026-06-20). Beide RAW-Quellen ingested (Carlsten et al. CCS 2016, Budish QJE 2024). Wiki-Artikel erweitert. Ausgang bleibt offen — empirisch unentschieden.

**OP_RETURN-Limit (Bitcoin Core 29+):** Wurde das 80-Byte-Standardlimit abgeschafft? `op-return-und-datenspeicherung.md` hält die Frage offen. Neue RAW-Quellen erforderlich.

**AOPP-Nachfolge:** Mehrere Schweizer Hersteller haben AOPP 2022 entfernt. Gibt es eine datenschutzkonforme Adressverifizierungslösung? `regulierung-tofr-aopp.md` deckt den Rückzug ab, aber keine Nachfolgelösung.

**FROST-Implementierungen:** Wann werden MuSig2/FROST in gängigen Hardware-Wallet-Softwares breit verfügbar? `schnorr-und-taproot.md` und `multisig-grundlagen.md` erwähnen FROST als emerging — kein Update seit 2024.

**EU-Regulierung (MiCA/AML):** Stand nach März 2024? `eu-regulierung-und-datenschutz.md` endet dort. Neue Entwicklungen in `regulierung-tofr-aopp.md` partiell abgedeckt.

**Ark-Reifegrad:** `skalierung-lightning-ark-statechains.md` hat Stand Dez. 2025. Aktuelle Implementierungsfortschritte unklar.

**BOLT 12 / Offers:** `lightning-netzwerk-grundlagen.md` erwähnt BOLT 12 als offene Frage. Welche Wallets unterstützen es produktiv, und wie verändert es die Privatsphäre gegenüber BOLT 11?

**Multi-Path-Payments (MPP):** Privatsphäre-Implikationen gegenüber Single-Path in `lightning-netzwerk-grundlagen.md` als offene Frage markiert. Keine RAW-Quellen vorhanden.

## Artikel-Kandidaten (Held — zu wenig Evidenz)

- **Bitcoin-Einsteigerleitfaden** — 3 Blocktrainer-Quellen in RAW vorhanden, aber `bitcoin-fehlannahmen.md` und `bitcoin-kaufen-und-dca.md` decken die meisten Punkte bereits ab. Kandidat halten bis neue RAW-Quellen den Artikel deutlich bereichern würden.

- **bitcoin-als-inflationsschutz** — Referenziert aus `bitcoin-als-strategische-reserve.md` (Related-Link). Bitcoin als Inflationsschutz (empirische Evidenz, Vergleich Gold/TIPS) verdient einen eigenständigen Artikel. Quellenlage im KB nach Compile-Pass 31 gut genug für einen Entwurf. Nächster Pass.

- **bitcoin-kiosk-regulierung** — `Bitcoin_Kiosk_Paper_July_ 2025.pdf` (Eric Peterson, Satoshi Action, Juli 2025) in RAW vorhanden. US-spezifisches Nischenthema; Artikel erst dann, wenn weitere Policy-Quellen verfügbar.
