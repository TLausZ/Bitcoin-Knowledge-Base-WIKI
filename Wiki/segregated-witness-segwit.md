# Segregated Witness (SegWit)

**Status:** established
**Themen:** protokoll, lightning
**Last updated:** 2026-06-28
**Sources:** [[20151221_bip-0141]], [[learnmeabitcoin-beginners-guide-segwit]], [[learnmeabitcoin-technical-upgrades-segregated-witness]], [[blocksizewar]], [[2018_Grokking-Bitcoin_Rosenbaum]], [[alex-waltz-first-block-over-1mb]]

## Summary

Segregated Witness (BIP-141, aktiviert August 2017) ist ein Soft Fork, der Signaturdaten aus dem Transaktionskörper in eine separate Witness-Struktur auslagert. Das löst Transaction Malleability fundamental, erhöht effektiv die Blockkapazität durch Block Weight, und war die technische Voraussetzung für den Lightning Network-Aufbau. Die neuen Adresstypen P2WPKH und P2WSH ermöglichen native SegWit-Transaktionen mit niedrigeren Gebühren.

## Body

### Das Malleability-Problem

Vor SegWit war die Transaction-ID (txid) ein Hash aller Transaktionsdaten inklusive Signaturen. Signaturen können in bestimmten Fällen leicht modifiziert werden, ohne die Gültigkeit zu verändern — was die txid ändert. Das verhinderte zuverlässige unbestätigte Transaktionsketten, die für Payment Channels und Lightning Network notwendig sind: Wenn die txid eines Funding-Transactions noch vor Bestätigung verändert wird, werden darauf aufbauende Spending-Transactions ungültig.

### Die SegWit-Lösung

SegWit trennt den Witness (Signaturen, Scripts) vom Transaktionskörper. Die txid wird nur aus den nicht-Witness-Daten berechnet — sie ist damit nicht mehr durch Signatur-Änderungen veränderbar. Zusätzlich gibt es eine neue `wtxid` (Witness Transaction ID), die alle Daten einschliesst.

**Commitment:** Der Witness-Merkle-Root wird in der Coinbase-Transaktion per OP_RETURN verankert — kompatibel als Soft Fork, da alte Nodes diesen Commitment ignorieren.

### Block Weight statt 1-MB-Limit

Statt des einfachen 1-MB-Blocklimits führt SegWit ein Block-Weight-Konzept ein:

`Block Weight = Base Size × 3 + Total Size ≤ 4.000.000`

Witness-Daten werden effektiv mit einem Discount von 75% gewertet (1 Weight Unit statt 4). Das erhöht die effektive Kapazität auf ~1,7–2 MB für typische Transaktionen, ohne das 1-MB-Limit formal aufzuheben — Non-Upgraded-Nodes sehen nach wie vor Blöcke unter 1 MB.

### Neue Adresstypen

**P2WPKH (Pay-to-Witness-Public-Key-Hash):** Native SegWit für Einzelschlüssel. Erkennbar an Adressen beginnend mit `bc1q`. Signature und Public Key wandern in den Witness. ~25% kleiner als P2PKH.

**P2WSH (Pay-to-Witness-Script-Hash):** Native SegWit für komplexe Scripts (Multisig etc.). 32-byte Scripthash statt 20-byte, höhere Kollisionssicherheit. Witness Script bis 10.000 Bytes möglich.

**Nested SegWit (P2SH-P2WPKH / P2SH-P2WSH):** SegWit verpackt in P2SH für Rückwärtskompatibilität. Erkennbar an Adressen beginnend mit `3`. Weniger effizient, aber kompatibel mit älteren Wallets.

### Quadratisches Hashing-Problem (O(n²))

SegWit löst neben Malleability ein zweites Problem, das bei grossen Transaktionen kritisch wurde (Rosenbaum, Kap. 10):

Das Legacy-Signaturverfahren hasht für jeden Input die gesamte Transaktion. Bei einer Transaktion mit n Inputs wird die Transaktion also n-mal gehasht — bei Transaktion mit 100 Inputs wird dieselbe Datenmenge 100-mal durchgearbeitet. Die Gesamtarbeit steigt quadratisch: O(n²). Ein Angreifer kann eine grosse Transaktion mit vielen Inputs erzeugen, die Nodes für die Validierung unverhältnismässig viel Zeit kostet.

SegWit (BIP143) führt ein neues Signature-Hashing-Verfahren ein, das jede Transaktion nur einmal hasht und die relevanten Teile pro Input effizient extrahiert. Die Validierungsarbeit wird linear: O(n). Das macht SegWit-Transaktionen nicht nur kleiner, sondern auch schneller zu validieren. [[2018_Grokking-Bitcoin_Rosenbaum]]

### Lightning Network als direkte Folge

Die Malleability-Lösung war die fehlende Voraussetzung für zuverlässige Payment Channels. Lightning Network nutzt unbestätigte Transaktionsketten, die jetzt vertrauensfrei funktionieren: Alice und Bob können eine Spending-Transaction signieren, bevor die Funding-Transaction on-chain ist, ohne dass Bob die Funding-Transaction durch Malleability invalidieren kann.

### Aktivierung

SegWit wurde durch Miner-Signaling aktiviert: 95% der Blöcke in einem 2016-Block-Fenster mussten Bereitschaft signalisieren. Dieser Schwellenwert wurde im Fenster 477.792–479.807 erreicht (100% Signaling). SegWit aktivierte bei Block **481.824** am 24. August 2017, 01:57:37 UTC.

Dass Miner (nicht Nutzer oder Entwickler) die Entscheidung treffen, liegt an der Netzwerkdynamik: Bei einem Soft Fork müssen Miner die neuen Blöcke produzieren. 95% Signaling stellt sicher, dass die neue Chain die alte überholt, bevor irgendjemand auf einen veralteten Fork weiterbaut.

### Backward Compatibility

Als Soft Fork betrachten Non-Upgraded-Nodes alle Witness-Programme als "anyone-can-spend" — technisch gültig, aber gefährlich, weshalb ein Upgrade stark empfohlen wird. Nicht-upgegradete Wallets können Bitcoin von SegWit-Adressen empfangen und über P2SH-Adressen senden, aber keine Native-SegWit-Adressen validieren.

SegWit-Nodes streifen für nicht-upgegradete Nachbar-Nodes die Witness-Daten aus Transaktionen — diese sehen eine "abgespeckte" Version ohne Signaturen, bleiben aber synchron.

### Block 481.947: Erster Block über 1 MB

SegWit wurde am 24. August 2017 in Block 481.824 aktiviert. Dieser enthielt 2 SegWit-Transaktionen, erkennbar an Adressen mit „bc1q"-Präfix. Der erste Block, der die 1-MB-Grenze tatsächlich überschritt, war Block 481.947, gemined am 25. August 2017 von BitFury mit 1,03 MB.

Der Witness-Merkle-Root wird im Coinbase-Script als `OP_RETURN` committet — erkennbar am String `aa21a9ed`. Es sind nicht die Signaturen selbst, sondern ihr Merkle Root, der dort gespeichert wird (die Signaturen würden schlicht nicht passen).

## Related

- [[soft-fork-und-hard-fork]]
- [[skalierung-lightning-ark-statechains]]
- [[taproot-musig2-frost]]
- [[bitcoin-whitepaper]]
- [[konsensregeln-und-mempool-richtlinien]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch
- [[blocksize-war|The Blocksize War (Jonathan Bier)]] ← Buch

## Open Questions

- Wie hoch ist der aktuelle SegWit-Adoptionsgrad auf dem Netzwerk?
- Wann wird P2SH-Nested-SegWit als veraltet eingestuft?
