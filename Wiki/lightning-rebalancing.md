# Lightning Rebalancing

**Status:** established
**Themen:** protokoll, lightning, adoption
**Last updated:** 2026-06-09
**Sources:** [[Rebalancing_ The Key to the Lightning Network]], [[Rebalancing in the Lightning Network_ Circular Payments, Fee Management and Splices]]

## Summary

Rebalancing bezeichnet die strategische Aktion, die ein Lightning-Routing-Node unternimmt, um seine Channel-Balances zu normalisieren. Routing-Zahlungen verbrauchen Kapazität auf einer Seite eines Channels — irgendwann kann ein Channel keine Zahlungen mehr in einer Richtung routen. Rebalancing stellt diese Fähigkeit wieder her. Drei Hauptstrategien: Circular Payments, Fee Management und Splicing.

## Body

### Warum Channels unbalanciert werden

Ein Payment Channel zwischen Carol und Alice hat eine feste Gesamtkapazität, die sich auf beide Seiten aufteilt. Wenn Carol Zahlungen von Alice zu Bob routet, fliesst Kapazität von Carols Alice-Seite zu Carols Bob-Seite. Nach vielen Zahlungen in dieselbe Richtung hat Carol auf der Alice-Seite kaum noch Kapazität — sie kann keine weiteren Zahlungen von Alice zu Bob mehr routen.

Das ist das Rebalancing-Problem: Routing ist ökonomisch sinnvoll (Fee-Einnahmen), aber es zerstört systematisch die Balance, die es ermöglicht.

### Strategie 1: Circular Payments

Carol sendet eine Zahlung an sich selbst über einen Umweg: Alice → Carol → Bob → Carol (zurück). Das kostet Routing-Gebühren an die Zwischenknoten, bringt aber Kapazität auf der Alice-Seite zurück.

**Voraussetzung**: Das Netzwerk muss ausreichend verbunden und liquidiert sein, damit der Umweg funktioniert. Bei schwachen Netzwerken (wenig Nodes, wenig Kapazität) scheitern Circular Payments häufig.

**Kosten**: Die Fees, die Carol an andere Nodes zahlt. Sie muss kalkulieren, ob ihre eigenen Routing-Einnahmen diese Kosten übersteigen.

### Strategie 2: Fee Management

Carol senkt die Gebühren auf ihrer überfinanzierten Seite (Bob-Seite), um mehr Zahlungen in dieser Richtung anzuziehen, und erhöht die Gebühren auf der depleted Seite (Alice-Seite), um Zahlungen abzuschrecken. Das balanciert sich mit der Zeit von selbst aus.

**Vorteil**: Keine extra on-chain Transaktionen, keine sofortigen Kosten.

**Nachteil**: Langsam. Hängt von externen Zahlungsflüssen ab. Funktioniert nicht, wenn der Node keine anderen Nutzer routet.

### Strategie 3: Splicing

Splice-In oder Splice-Out verändert die Kanalkapazität on-chain. Der Node kann gezielt Kapazität hinzufügen oder abziehen, unabhängig von externen Zahlungsflüssen.

**Vorteil**: Einzige Strategie, die funktioniert, wenn das Netzwerk zu wenig Liquidität hat.

**Nachteil**: Erfordert on-chain Transaktion und Bestätigungszeit. Kostet Mining-Gebühren.

→ Details: [[lightning-splicing]]

### Das Grundprinzip: Routing ist kein passives Geschäft

Ein Lightning-Routing-Node ist kein passiver Mittler. Er muss aktiv:
- Channel-Balances überwachen
- Rebalancing-Strategien auswählen und ausführen
- Fees dynamisch anpassen
- Entscheiden, welche Peers sinnvoll sind

Das ist der Grund, warum selbst betriebene Lightning-Nodes für weniger technische Nutzer komplex sind — und warum Wallet-Services wie Phoenix oder Muun das für den Nutzer abstrahieren.

### Einordnung: Intermediate Node vs. Edge Node

Rebalancing ist primär ein Problem für **Intermediate Nodes** (Routing Nodes), nicht für **Edge Nodes** (End-Nutzer). Ein End-Nutzer mit einem oder zwei Channels zu einem LSP braucht kein aktives Rebalancing — das übernimmt der LSP. Rebalancing wird relevant, wer mehrere Channels zu verschiedenen Peers hält und Zahlungen routet.

## Related

- [[lightning-splicing]]
- [[skalierung-lightning-ark-statechains]]
- [[phoenix-wallet-lightning]]
- [[transaktionsgebuehren-und-mempool]]
- [[muun-wallet]]
- [[lightning-netzwerk-grundlagen]]

- [[einfuehrung-in-das-lightning-netzwerk|Einführung in das Lightning-Netzwerk (Antonopoulos, Osuntokun & Pickhardt)]] ← Buch

## Open Questions

- Wie werden Rebalancing-Kosten langfristig in einem reifen Lightning-Netzwerk aussehen — sinken sie oder stabilisieren sie sich?
- Gibt es automatisierte Tools für effizientes Fee Management, und welche sind in der Praxis bewährt?
- Wie ändert Splicing die ökonomische Kalkulation für Routing Nodes fundamental?
