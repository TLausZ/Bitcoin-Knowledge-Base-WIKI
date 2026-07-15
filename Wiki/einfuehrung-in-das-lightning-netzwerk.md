# Einführung in das Lightning-Netzwerk (Antonopoulos, Osuntokun & Pickhardt)

**Status:** established
**Themen:** protokoll, lightning, buecher
**Last updated:** 2026-07-15
**Sources:** [[einfuehrung-in-das-lightning-netzwerk]]

## Summary

Das technische Standardwerk zum Lightning-Netzwerk, hier in der deutschen Ausgabe (O'Reilly/dpunkt 2022/2023, Übersetzung Peter Klicman) des englischen Originals «Mastering the Lightning Network» von Andreas M. Antonopoulos, Olaoluwa Osuntokun und René Pickhardt. Es erklärt Lightning als Second-Layer-Protokoll auf Bitcoin: von den ersten Schritten mit einer Wallet über den Betrieb einer eigenen Node bis zu Zahlungskanälen, Routing, Onion-Routing und dem Wire-Protokoll. Wie [[mastering-bitcoin]] ist es zweigeteilt — die ersten Kapitel für alle, die späteren für Entwickler. Als Kurzeintrag geführt: die Substanz liegt in den einzelnen Lightning-Konzept-Artikeln, dieser Eintrag ordnet das Buch ein und verlinkt sie.

## Body

### Einordnung

Das Buch ist das Referenzwerk zur Implementierungsebene von Lightning, analog zu [[mastering-bitcoin]] auf der Basisschicht. Es setzt Bitcoin-Grundwissen voraus (Anhang A holt das Nötigste nach) und führt vom Nutzerhandwerk bis zur Protokollmechanik.

**Original frei verfügbar:** Das englische «Mastering the Lightning Network» liegt vollständig auf GitHub ([github.com/lnbook/lnbook](https://github.com/lnbook/lnbook)) und steht unter der Lizenz Creative Commons CC-BY-SA 4.0. Die hier ingestierte deutsche dpunkt-Ausgabe trägt einen restriktiveren Verlags-Copyright-Vermerk; das offen lizenzierte Werk ist das englische Original.

### Kapitelübersicht

1. Einführung (Begriffe, Vertrauen, Geschichte und Zukunft) → [[lightning-netzwerk-grundlagen]]
2. Erste Schritte (erste Wallet, erste Zahlung)
3. Wie das Lightning-Netzwerk funktioniert → [[lightning-netzwerk-grundlagen]]
4. Lightning-Node-Software → [[core-lightning-26-06]]
5. Eine Lightning-Netzwerk-Node betreiben
6. Architektur des Lightning-Netzwerks
7. Zahlungskanäle
8. Routing in einem Netzwerk aus Zahlungskanälen → [[lightning-rebalancing]]
9. Kanalbetrieb und Zahlungsweiterleitung → [[lightning-splicing]]
10. Onion-Routing
11. Gossip und der Kanal-Graph
12. Wegfindung und Zustellung der Zahlung
13. Wire-Protokoll: Framing und Erweiterbarkeit
14. Lightnings verschlüsselter Nachrichtentransport
15. Lightning-Zahlungsanforderungen → [[lightning-address-datenschutz]]
16. Sicherheit und Privatsphäre im Lightning-Netzwerk → [[lightning-address-datenschutz]]
17. Fazit

Anhänge: A Bitcoin-Grundlagen, B Docker-Installation und -Nutzung, C Nachrichten des Wire-Protokolls, D Quellen und Lizenzinformationen.

### Nutzen

Für tiefe Fragen zur Lightning-Mechanik — HTLCs, Onion-Routing, Wegfindung, Wire-Protokoll — ist das Buch die massgebliche Buchquelle im Wiki. Es ergänzt die anwendungsnahen Artikel zu Skalierung ([[skalierung-lightning-ark-statechains]]), Rebalancing ([[lightning-rebalancing]]), Splicing ([[lightning-splicing]]) und Wallet-Praxis ([[phoenix-wallet-lightning]]) um die Protokollgrundlage.

## Related

- [[mastering-bitcoin]]
- [[lightning-netzwerk-grundlagen]]
- [[lightning-rebalancing]]
- [[lightning-splicing]]
- [[skalierung-lightning-ark-statechains]]
- [[lightning-address-datenschutz]]
- [[core-lightning-26-06]]
- [[phoenix-wallet-lightning]]

## Open Questions

- Stand 2021/2022 geschrieben: wie stark sind einzelne Kapitel (etwa Wegfindung, Gebührenmodelle) durch neuere Lightning-Entwicklungen überholt?
