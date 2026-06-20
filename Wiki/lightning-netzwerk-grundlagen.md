# Lightning Netzwerk: Grundlagen

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[The Inbound Capacity Problem in the Lightning Network]], [[A Closer Look at Submarine Swaps in the Lightning Network]], [[20251218_die-skalierung-von-bitcoin-lightning-und-der-weg-zu-ark]], [[20231018_lightning-in-der-bitboxapp]]

## Summary

Das Lightning Network ist eine Schicht über Bitcoin, die schnelle und günstige Zahlungen ermöglicht, ohne für jede Transaktion die Blockchain zu nutzen. Die Grundbausteine sind Zahlungskanäle zwischen zwei Parteien — sie halten Bitcoin in einem gemeinsamen On-Chain-Output gesperrt und erlauben beliebig viele Off-Chain-Saldenaktualisierungen. Mehrere Kanäle bilden ein Netzwerk, durch das Zahlungen geroutet werden.

## Body

### Zahlungskanäle

Ein Kanal öffnet mit einer On-Chain-Transaktion, die Bitcoin in einem 2-of-2-Multisig-Output sperrt. Die **Kanalkapazität** ist die Gesamtmenge der gesperrten Bitcoin — sie ändert sich nur durch Schließen oder Splicing.

Innerhalb des Kanals gibt es jederzeit eine **lokale Balance** (eigene Seite) und eine **Remote Balance** (Gegenseite). Jede Zahlung verschiebt Satoshis von einer Seite zur anderen, ohne eine On-Chain-Transaktion zu erzeugen. Die Kanalkapazität bleibt konstant; nur die Verteilung ändert sich.

Zum Schließen veröffentlichen beide Parteien den aktuellen Zustand on-chain. Kooperatives Schließen (beide einig) braucht eine Transaktion; erzwungenes Schließen (eine Partei nicht erreichbar) ist teurer und langsamer.

### Inbound- und Outbound-Kapazität

Der Betrag, den man senden kann, ist durch die lokale Balance begrenzt (**Outbound-Kapazität**). Der Betrag, den man empfangen kann, ist durch die Remote Balance begrenzt (**Inbound-Kapazität**).

Öffnet jemand einen neuen Kanal, fließt die gesamte Kapazität zunächst auf die eigene Seite. Man kann sofort senden, aber nichts empfangen — weil die Remote Balance Null ist. Inbound-Kapazität entsteht durch empfangene Zahlungen oder dadurch, dass Gegenstellen eigene Kanäle mit genug Remote Balance öffnen. Das ist das **Inbound-Kapazitätsproblem** für neue Empfänger im Netzwerk. Lightning Service Provider (LSP) lösen es, indem sie dem Nutzer eingehende Liquidität bereitstellen.

### Routing und HTLCs

Zwei Nodes müssen keinen direkten Kanal teilen, um sich zu bezahlen. Eine Zahlung kann über mehrere Zwischenknoten geroutet werden. Der Mechanismus dafür heißt **HTLC (Hash Time-Locked Contract)**.

Funktionsprinzip: Der Empfänger erzeugt ein Geheimnis (`preimage`) und teilt dessen Hash mit dem Sender. Der Sender sperrt Satoshis mit der Bedingung: „Wer das Preimage kennt, bekommt die Coins; nach Timeout gehen sie zurück." Jeder Hop in der Route setzt dasselbe HTLC weiter, mit leicht kürzer werdendem Timeout. Der Empfänger löst das letzte HTLC auf — dadurch deckt er das Geheimnis auf, was kettenartig alle vorherigen HTLCs löst. Kein Zwischenknoten kann das Geld stehlen, weil er das Preimage nicht kennt, bevor der Empfänger es enthüllt.

### Onion Routing

Lightning nutzt **Onion Routing**: Der Sender verschlüsselt die Route so, dass jeder Knoten nur seinen direkten Vorgänger und Nachfolger kennt, nicht den vollständigen Pfad. Das schützt die Privatsphäre des Senders und Empfängers vor Routing-Knoten.

### Selbstbetrieb vs. LSP

Wer einen eigenen Lightning-Node betreibt, kontrolliert seine Kanäle vollständig, muss aber Liquidität manuell verwalten, Peers sorgfältig auswählen und seinen Node dauerhaft online halten.

LSPs wie Phoenix oder Breez abstrahieren diese Komplexität. Sie stellen Liquidität bereit, übernehmen Kanalverwaltung und routen Zahlungen. Der Nutzer gibt einen Teil der Kontrolle ab, zahlt aber keine Kanalöffnungsgebühren selbst und hat sofort Inbound-Kapazität. [[skalierung-lightning-ark-statechains]]

### Submarine Swaps

Submarine Swaps nutzen HTLCs, um zwischen On-Chain-Bitcoin und Lightning zu wechseln, ohne einem Custodian zu vertrauen. Durch die HTLC-Bedingung ist die Atomizität garantiert: Entweder erhält der Empfänger das Geld und der Sender bekommt sein Preimage, oder beide erhalten ihr Geld zurück nach Timeout. Kein Teilausfall ist möglich.

## Related

- [[skalierung-lightning-ark-statechains]]
- [[phoenix-wallet-lightning]]
- [[lightning-splicing]]
- [[lightning-rebalancing]]
- [[lightning-address-datenschutz]]
- [[bitcoin-transaktionsstruktur]]

## Open Questions

- Wie verändert sich die Privatsphäre durch Multi-Path-Payments (MPP) gegenüber Single-Path?
- Wie reif ist die BOLT 12-Implementierung für Offers, und welche Wallets unterstützen es bereits?
