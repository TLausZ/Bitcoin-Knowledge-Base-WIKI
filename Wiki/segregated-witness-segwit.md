# Segregated Witness (SegWit)

**Status:** established
**Last updated:** 2026-06-05
**Sources:** [[20151221_bip-0141]]

## Summary

Segregated Witness (BIP-141, aktiviert August 2017) ist ein Soft Fork, der Signaturdaten aus dem Transaktionskörper in eine separate Witness-Struktur auslagert. Das löst Transaction Malleability fundamental, erhöht effektiv die Blockkapazität durch Block Weight, und war die technische Voraussetzung für den Lightning Network-Aufbau. Die neuen Adresstypen P2WPKH und P2WSH ermöglichen native SegWit-Transaktionen mit niedrigeren Gebühren.

## Body

### Das Malleability-Problem

Vor SegWit war die Transaction-ID (txid) ein Hash aller Transaktionsdaten inklusive Signaturen. Signaturen können in bestimmten Fällen leicht modifiziert werden, ohne die Gültigkeit zu verändern — was die txid ändert. Das verhinderte zuverlässige unbestätigte Transaktionsketten, die für Payment Channels und Lightning Network notwendig sind: Wenn die txid eines Funding-Transactions noch vor Bestätigung verändert wird, werden darauf aufbauende Spending-Transactions ungültig.

### Die SegWit-Lösung

SegWit trennt den Witness (Signaturen, Scripts) vom Transaktionskörper. Die txid wird nur aus den nicht-Witness-Daten berechnet — sie ist damit nicht mehr durch Signatur-Änderungen veränderbar. Zusätzlich gibt es eine neue `wtxid` (Witness Transaction ID), die alle Daten einschließt.

**Commitment:** Der Witness-Merkle-Root wird in der Coinbase-Transaktion per OP_RETURN verankert — kompatibel als Soft Fork, da alte Nodes diesen Commitment ignorieren.

### Block Weight statt 1-MB-Limit

Statt des einfachen 1-MB-Blocklimits führt SegWit ein Block-Weight-Konzept ein:

`Block Weight = Base Size × 3 + Total Size ≤ 4.000.000`

Witness-Daten werden effektiv mit einem Discount von 75% gewertet (1 Weight Unit statt 4). Das erhöht die effektive Kapazität auf ~1,7–2 MB für typische Transaktionen, ohne das 1-MB-Limit formal aufzuheben — Non-Upgraded-Nodes sehen nach wie vor Blöcke unter 1 MB.

### Neue Adresstypen

**P2WPKH (Pay-to-Witness-Public-Key-Hash):** Native SegWit für Einzelschlüssel. Erkennbar an Adressen beginnend mit `bc1q`. Signature und Public Key wandern in den Witness. ~25% kleiner als P2PKH.

**P2WSH (Pay-to-Witness-Script-Hash):** Native SegWit für komplexe Scripts (Multisig etc.). 32-byte Scripthash statt 20-byte, höhere Kollisionssicherheit. Witness Script bis 10.000 Bytes möglich.

**Nested SegWit (P2SH-P2WPKH / P2SH-P2WSH):** SegWit verpackt in P2SH für Rückwärtskompatibilität. Erkennbar an Adressen beginnend mit `3`. Weniger effizient, aber kompatibel mit älteren Wallets.

### Lightning Network als direkte Folge

Die Malleability-Lösung war die fehlende Voraussetzung für zuverlässige Payment Channels. Lightning Network nutzt unbestätigte Transaktionsketten, die jetzt vertrauensfrei funktionieren: Alice und Bob können eine Spending-Transaction signieren, bevor die Funding-Transaction on-chain ist, ohne dass Bob die Funding-Transaction durch Malleability invalidieren kann.

### Backward Compatibility

Als Soft Fork betrachten Non-Upgraded-Nodes alle Witness-Programme als "anyone-can-spend" — technisch gültig, aber gefährlich, weshalb ein Upgrade stark empfohlen wird. Nicht-upgegradete Wallets können Bitcoin von SegWit-Adressen empfangen und über P2SH-Adressen senden, aber keine Native-SegWit-Adressen validieren.

## Related

- [[soft-fork-und-hard-fork]]
- [[skalierung-lightning-ark-statechains]]
- [[taproot-musig2-frost]]
- [[bitcoin-whitepaper]]
- [[konsensregeln-und-mempool-richtlinien]]

## Open Questions

- Wie hoch ist der aktuelle SegWit-Adoptionsgrad auf dem Netzwerk?
- Wann wird P2SH-Nested-SegWit als veraltet eingestuft?
