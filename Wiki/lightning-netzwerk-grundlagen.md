# Lightning Netzwerk: Grundlagen

**Status:** established
**Themen:** grundlagen, protokoll, lightning
**Last updated:** 2026-06-20
**Sources:** [[The Inbound Capacity Problem in the Lightning Network]], [[A Closer Look at Submarine Swaps in the Lightning Network]], [[20251218_die-skalierung-von-bitcoin-lightning-und-der-weg-zu-ark]], [[20231018_lightning-in-der-bitboxapp]], [[Eine Vision für wertaktivierendes Web.md]], [[bitcoin-ratgeber_kapitel-04-das-lightning-netzwerk]]

## Summary

Das Lightning Network ist eine Schicht über Bitcoin, die schnelle und günstige Zahlungen ermöglicht, ohne für jede Transaktion die Blockchain zu nutzen. Die Grundbausteine sind Zahlungskanäle zwischen zwei Parteien — sie halten Bitcoin in einem gemeinsamen On-Chain-Output gesperrt und erlauben beliebig viele Off-Chain-Saldenaktualisierungen. Mehrere Kanäle bilden ein Netzwerk, durch das Zahlungen geroutet werden.

## Body

### Zahlungskanäle

Ein Kanal öffnet mit einer On-Chain-Transaktion, die Bitcoin in einem 2-of-2-Multisig-Output sperrt. Die **Kanalkapazität** ist die Gesamtmenge der gesperrten Bitcoin — sie ändert sich nur durch Schliessen oder Splicing.

Innerhalb des Kanals gibt es jederzeit eine **lokale Balance** (eigene Seite) und eine **Remote Balance** (Gegenseite). Jede Zahlung verschiebt Satoshis von einer Seite zur anderen, ohne eine On-Chain-Transaktion zu erzeugen. Die Kanalkapazität bleibt konstant; nur die Verteilung ändert sich.

Zum Schliessen veröffentlichen beide Parteien den aktuellen Zustand on-chain. Kooperatives Schliessen (beide einig) braucht eine Transaktion; erzwungenes Schliessen (eine Partei nicht erreichbar) ist teurer und langsamer.

### Inbound- und Outbound-Kapazität

Der Betrag, den man senden kann, ist durch die lokale Balance begrenzt (**Outbound-Kapazität**). Der Betrag, den man empfangen kann, ist durch die Remote Balance begrenzt (**Inbound-Kapazität**).

Öffnet jemand einen neuen Kanal, fliesst die gesamte Kapazität zunächst auf die eigene Seite. Man kann sofort senden, aber nichts empfangen — weil die Remote Balance Null ist. Inbound-Kapazität entsteht durch empfangene Zahlungen oder dadurch, dass Gegenstellen eigene Kanäle mit genug Remote Balance öffnen. Das ist das **Inbound-Kapazitätsproblem** für neue Empfänger im Netzwerk. Lightning Service Provider (LSP) lösen es, indem sie dem Nutzer eingehende Liquidität bereitstellen.

### Routing und HTLCs

Zwei Nodes müssen keinen direkten Kanal teilen, um sich zu bezahlen. Eine Zahlung kann über mehrere Zwischenknoten geroutet werden. Der Mechanismus dafür heisst **HTLC (Hash Time-Locked Contract)**.

Funktionsprinzip: Der Empfänger erzeugt ein Geheimnis (`preimage`) und teilt dessen Hash mit dem Sender. Der Sender sperrt Satoshis mit der Bedingung: „Wer das Preimage kennt, bekommt die Coins; nach Timeout gehen sie zurück." Jeder Hop in der Route setzt dasselbe HTLC weiter, mit leicht kürzer werdendem Timeout. Der Empfänger löst das letzte HTLC auf — dadurch deckt er das Geheimnis auf, was kettenartig alle vorherigen HTLCs löst. Kein Zwischenknoten kann das Geld stehlen, weil er das Preimage nicht kennt, bevor der Empfänger es enthüllt.

### Onion Routing

Lightning nutzt **Onion Routing**: Der Sender verschlüsselt die Route so, dass jeder Knoten nur seinen direkten Vorgänger und Nachfolger kennt, nicht den vollständigen Pfad. Das schützt die Privatsphäre des Senders und Empfängers vor Routing-Knoten.

### Selbstbetrieb vs. LSP

Wer einen eigenen Lightning-Node betreibt, kontrolliert seine Kanäle vollständig, muss aber Liquidität manuell verwalten, Peers sorgfältig auswählen und seinen Node dauerhaft online halten.

LSPs wie Phoenix oder Breez abstrahieren diese Komplexität. Sie stellen Liquidität bereit, übernehmen Kanalverwaltung und routen Zahlungen. Der Nutzer gibt einen Teil der Kontrolle ab, zahlt aber keine Kanalöffnungsgebühren selbst und hat sofort Inbound-Kapazität. [[skalierung-lightning-ark-statechains]]

### Submarine Swaps

Submarine Swaps nutzen HTLCs, um zwischen On-Chain-Bitcoin und Lightning zu wechseln, ohne einem Custodian zu vertrauen. Durch die HTLC-Bedingung ist die Atomizität garantiert: Entweder erhält der Empfänger das Geld und der Sender bekommt sein Preimage, oder beide erhalten ihr Geld zurück nach Timeout. Kein Teilausfall ist möglich.

### Lightning als Grundlage des wertaktivierenden Webs

Gigi formuliert Lightning nicht nur als Zahlungskanal, sondern als Infrastruktur für eine neue Internetökonomie. Das Problem des heutigen Webs ist strukturell: Konventionelle Währungen existieren im Cyberspace nur als Kredit (IOUs), nicht als Bargeld. Das macht Micropayments unwirtschaftlich (Minimum ~$5 mit Kreditkartensystem) und erzwingt Werbemodelle.

Lightning löst das: Es ist das erste digitale Inhaberinstrument — digitales Bargeld mit echtem Peer-to-Peer-Charakter, ohne Gegenparteirisiko. Satoshi-Beträge (Bruchteile eines Cents) können in Echtzeit und nahezu kostenlos fliessen.

**Value-Streaming:** Nutzer können Sats im laufenden Podcast-Konsum streamen — nicht nach Abschluss zahlen, sondern während des Hörens, proportional zur konsumierten Zeit. Das ist mit keinem konventionellen Zahlungssystem realisierbar.

**Podcasting 2.0 / Value4Value:** Der „Value Block" im Podcast-Namespace definiert, wie eingehende Sats aufgeteilt werden (Host, Gäste, Produzenten, App). Apps wie Fountain und Breez implementieren das. Der Mechanismus funktioniert erlaubnisfrei — kein Plattformkonto, kein Registrierungsprozess.

**Reale Kosten für Cyberspace-Aktionen:** Lightning ermöglicht, Aktionen mit echten Kosten zu verknüpfen. Bot-Farmen und Spam werden unrentabel, wenn jede Aktion eine Sat-Gebühr kostet. KYC ist nicht nötig — Reputation entsteht durch Staking von Sats, nicht durch Identitätsnachweis.

Gigi: „Sobald du deine ersten Streaming-Zahlungen erhalten hast, fühlt es sich mehr als antiquiert an, mit den alten Zahlungsschienen unserer Fiat-Welt zu arbeiten." [[Eine Vision für wertaktivierendes Web.md]] → Ausführlicher in [[value4value-und-wertaktivierendes-web]]

### Einsteiger-Wallets und das Custodial-Limit

Für den Alltag trennt Michael Wolfs "Bitcoin-Ratgeber" die Spar-Wallet (grössere Beträge, on-chain) klar von der Lightning-Wallet (Alltagsbeträge, Sekundenzahlungen). Non-Custodial-Optionen halten den Schlüssel beim Nutzer: Phoenix (automatisches Kanalmanagement, einsteigerfreundlich), Breez (mit integriertem Point-of-Sale), Zeus (fortgeschritten, an eigene Node koppelbar) und Aqua (Hybrid). Custodial-Wallets wie Blink oder Wallet of Satoshi sind einfacher, verwahren aber die Schlüssel für den Nutzer. Die Faustregel: Custodial Lightning nur für Kleingeld; alles über ein paar Euro gehört in eine Non-Custodial-Wallet. Aufgeladen wird eine Lightning-Wallet, indem man on-chain Bitcoin an ihre Empfangsadresse sendet — Lightning-Adressen beginnen mit „ln…", on-chain-Adressen mit „bc1…", „1…" oder „3…".

## Related

- [[skalierung-lightning-ark-statechains]]
- [[phoenix-wallet-lightning]]
- [[lightning-splicing]]
- [[lightning-rebalancing]]
- [[lightning-address-datenschutz]]
- [[bitcoin-transaktionsstruktur]]

- [[einfuehrung-in-das-lightning-netzwerk|Einführung in das Lightning-Netzwerk (Antonopoulos/Osuntokun/Pickhardt)]] ← Buch
- [[internet-of-money-vol2|The Internet of Money Vol. 2 (Andreas Antonopoulos)]] ← Buch

## Open Questions

- Wie verändert sich die Privatsphäre durch Multi-Path-Payments (MPP) gegenüber Single-Path?
- Wie reif ist die BOLT 12-Implementierung für Offers, und welche Wallets unterstützen es bereits?
