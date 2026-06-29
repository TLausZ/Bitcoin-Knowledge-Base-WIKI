# Open Questions & Gaps

Offene Fragen, Lücken und Themen, die mehr Quellen benötigen. Stand: 2026-06-29 (Health Check 2)

## Fehlende Wiki-Artikel

- **Coin Control** → erledigt: `coin-control-und-utxo-auswahl.md` erstellt
- **Lightning-Grundlagen** → erledigt: `lightning-netzwerk-grundlagen.md` erstellt
- **WalletConnect / DApps** → erledigt: `walletconnect-und-dapps.md` erstellt

Derzeit keine bekannten Lücken ausser den Kandidaten unten.

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

- **Bitcoin-Einsteigerleitfaden** — 3 Blocktrainer-Quellen in RAW vorhanden, aber `bitcoin-fehlannahmen.md` und `bitcoin-kaufen-und-dca.md` decken die meisten Punkte bereits ab. Kandidat halten bis neue RAW-Quellen den Artikel deutlich bereichern würden.

- **bitcoin-als-inflationsschutz** — erledigt: Artikel existiert.

- **bitcoin-kiosk-regulierung** — `Bitcoin_Kiosk_Paper_July_ 2025.pdf` (Eric Peterson, Satoshi Action, Juli 2025) in RAW vorhanden. US-spezifisches Nischenthema; Artikel erst dann, wenn weitere Policy-Quellen verfügbar.
