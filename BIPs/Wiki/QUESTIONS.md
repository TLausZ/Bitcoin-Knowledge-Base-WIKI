# BIPs Wiki — Open Questions

Stand: 2026-06-08

## Corpus-Überblick

- 96 BIPs deployed/complete/final
- 59 BIPs im Draft-Status (aktive Entwicklung)
- 54 BIPs closed/withdrawn/replaced/deferred

## Offene Fragen und Spannungsfelder

### Aktivierungs-Kontroversen
- BIP-8 vs. BIP-9: Welche Aktivierungsmethode setzt sich langfristig durch? BIP-8 (Lock-in by height) vs. BIP-9 (timeout and delay) — Taproot nutzte eine Kombination.
- Welche Draft-BIPs für Consensus-Änderungen haben realistische Aktivierungs-Chancen (OP_CTV/BIP-119, CSFS/BIP-348, OP_INTERNALKEY/BIP-349)?

### Kovarianten und Script-Erweiterungen
- BIP-119 (CTV) vs. BIP-346 (TXHASH) vs. BIP-443 (OP_CHECKCONTRACTVERIFY): Welcher Covenant-Ansatz setzt sich durch?
- BIP-448 bündelt BIP-446+348+349 — werden diese einzeln oder gebündelt aktiviert?

### Wallet-Standards
- BIP-84 (Native SegWit) vs. BIP-86 (Taproot): Wie schnell wird die Migration zu Taproot?
- PSBT: BIP-174 (v0) vs. BIP-370 (v2) — Migrationsstatus in der Wallet-Landschaft?

### Privatsphäre
- BIP-352 (Silent Payments) vs. BIP-47 (PayNyms): Silent Payments benötigt mehr Scanning-Aufwand, aber kein Notification-UTXO. Wie entwickelt sich die Adoption?
- BIP-379 (MiniScript): Wie weit ist die Wallet-Unterstützung?

### Veraltete und ersetzte BIPs
- BIP-16 (P2SH) vs. BIP-17 (OP_CHECKHASHVERIFY) — warum BIP-17 verloren?
- BIP-62 (Dealing with malleability) — durch SegWit (BIP-141) gelöst?
- Welche Closed-BIPs haben historischen Erkenntniswert, der noch nicht im Wiki aufgearbeitet ist?

## Artikel-Kandidaten für Tiefenanalyse
- Soft-Fork-Aktivierungs-Geschichte: BIP-34 → BIP-66 → BIP-65 → BIP-9/SegWit → BIP-8/Taproot
- PSBT-Ökosystem (BIP-174, 370, 371, 372, 373, 374, 375, 376)
- Descriptor-Ökosystem (BIP-380–393)
- Die Lightning-Grundlagen-BIPs (341/342/340 als Taproot-Bundle)
