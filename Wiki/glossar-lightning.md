# Glossar — Lightning

**Status:** established
**Themen:** lightning, glossar
**Last updated:** 2026-07-15
**Sources:** [[glossary-lightning]], [[glossary-lnbook]], [[Glossary – aantonop]], [[Glossary-bitcoindesign]]

## Summary

Nachschlage-Glossar für das Lightning-Netzwerk, die Zahlungsschicht auf Bitcoin. Es deckt Kanäle, Routing, Liquidität und die Sicherheitsmechanik ab. Protokollbegriffe der Basisschicht (Script, Timelocks, SegWit) stehen im [[glossar-bitcoin-technik]], allgemeine Begriffe im [[glossar-allgemein]]. Fachbegriffe behalten ihre englische Bezeichnung. Rein produktspezifische Werkzeuge einzelner Anbieter sind bewusst weggelassen; die Node-Software steht gesammelt unter «Implementierungen». Die Einordnung ins Gesamtbild liefert [[lightning-netzwerk-grundlagen]].

## Body

### Anchor Channel

Kanaltyp mit zwei Zusatzausgängen («Anchors»), über die sich die Gebühr einer erzwungenen Kanalschliessung nachträglich per [[glossar-bitcoin-technik|CPFP]] anheben lässt. Löst das Problem, dass die Commitment-Transaktion ihre Gebühr lange im Voraus festlegen muss.

### Balance (Kanalguthaben)

Die Aufteilung des Kanalguthabens zwischen den beiden Partnern. Sie verschiebt sich mit jeder Zahlung und bestimmt, wie viel jede Seite noch senden bzw. empfangen kann. Nicht mit der Kapazität verwechseln.

### Base Fee / Fee Rate

Die zwei Teile der Weiterleitungsgebühr eines Knotens: die Base Fee ist ein fester Betrag pro weitergeleiteter Zahlung (oft 1 Satoshi), die Fee Rate ein Anteil am Betrag, gemessen in Millionstel (ppm).

### BOLT (Basis of Lightning Technology)

Die formale Spezifikation des Lightning-Protokolls. Anders als Bitcoin hat Lightning keine einzelne Referenz-Implementierung; alle Implementierungen folgen den BOLTs, damit sie zusammen ein Netz bilden.

### Capacity (Kapazität)

Die Gesamtmenge Bitcoin in einem Kanal, festgelegt durch die Funding-Transaktion. Öffentlich sichtbar, sagt aber nichts über die aktuelle Aufteilung (die Balance) aus.

### Channel Breach / Penalty Transaction

Ein Betrugsversuch, bei dem ein Partner einen veralteten Kanalzustand veröffentlicht, um sich mehr Guthaben zu erschleichen. Der andere kann das mit einer Penalty-Transaktion bestrafen und das gesamte Kanalguthaben beanspruchen — sofern er den Betrug rechtzeitig bemerkt (siehe Watchtower).

### Channel Reserve

Ein Mindestguthaben, das jeder Partner im Kanal halten muss. Es sorgt dafür, dass im Betrugsfall immer etwas da ist, das die Penalty-Transaktion einziehen kann — ein Anreiz gegen Betrug.

### Circular Rebalance

Eine Zahlung eines Knotens an sich selbst über einen äusseren Pfad, um Guthaben von einem Kanal in einen anderen zu verschieben. Teil des Liquiditätsmanagements.

### Closing Transaction (Mutual Close)

Wenn beide Partner einverstanden sind, schliessen sie den Kanal kooperativ mit einer Closing-Transaktion, die den letzten Stand abbildet. Günstiger und schneller verfügbar als ein Force Close.

### Commitment Transaction

Die von beiden Partnern signierte Transaktion, die den aktuellen Kanalstand festhält. Jede Zahlung erzeugt eine neue Version; jeder Partner hält seine eigene. Sie kann jederzeit auf die Kette gebracht werden, um den Kanal einseitig zu schliessen — ein veralteter Stand gilt aber als Betrug.

### Eltoo

Vorgeschlagene Vereinfachung der Kanalmechanik, die den Strafmechanismus durch ein Update-Modell ersetzt. Setzt eine Änderung an Bitcoins Basisschicht voraus.

### Force Close

Einseitige Kanalschliessung, wenn ein Partner nicht erreichbar ist oder Uneinigkeit über den Zustand herrscht. Dabei wird die Commitment-Transaktion veröffentlicht; die eigenen Mittel sind erst nach einem Timelock verfügbar.

### Funding Transaction

Die On-Chain-Transaktion, die einen Kanal öffnet. Ihr Ausgang ist eine 2-von-2-Multisig-Adresse beider Partner; ihr Wert ist die Kapazität des Kanals.

### Gossip Protocol / Graph

Über das Gossip-Protokoll tauschen Knoten Informationen über öffentliche Kanäle und Knoten aus. Daraus entsteht der Graph des Netzwerks, den ein Absender fürs Routing nutzt. Unangekündigte Kanäle bleiben darin unsichtbar.

### Hodl Invoice

Eine Rechnung, bei der der Empfänger das Preimage zurückhält und die Zahlung so in der Schwebe hält, bis er sie einlöst oder verfallen lässt. Nützlich etwa für rückerstattbare Anzahlungen.

### HTLC (Hash Time-Locked Contract)

Der Vertrag, der eine Zahlung über mehrere Kanäle vertrauenslos macht: Der Empfänger bekommt das Geld nur, wenn er vor Ablauf eines Timelocks das Preimage preisgibt; sonst geht es an den Sender zurück. Baut auf Hashlock und Timelock der Basisschicht auf (siehe [[glossar-bitcoin-technik|Hashlock]]).

### Inbound / Outbound Capacity

Outbound Capacity ist der Betrag, den ein Knoten über einen Kanal senden kann, Inbound Capacity der, den er empfangen kann. Zusammen ergeben sie die Gesamtkapazität; ihre Verteilung entspricht der Balance.

### Invoice (Rechnung, BOLT-11)

Die vom Empfänger erstellte Zahlungsanforderung. Sie enthält Betrag, Payment Hash, Beschreibung und eine Ablauffrist. Anders als eine Bitcoin-Adresse verfällt sie nach einer gewissen Zeit.

### Implementierungen (LND, Core Lightning, Eclair, LDK)

Die gängige Node-Software, die den BOLT-Standard umsetzt: LND (Go, Lightning Labs), Core Lightning (C, Blockstream), Eclair (Scala, ACINQ) und das Baukasten-LDK. Weil alle denselben BOLTs folgen, sind sie interoperabel.

### Keysend

Verfahren, um Bitcoin direkt an den öffentlichen Schlüssel eines Knotens zu senden, ohne dass dieser vorher eine Rechnung ausstellt.

### Liquidity Management (Liquiditätsmanagement)

Das Steuern, wo im eigenen Knoten Guthaben liegt, damit Zahlungen in beide Richtungen gelingen. Umfasst das Öffnen und Schliessen von Kanälen sowie Rebalancing.

### LNURL

Ein in Bech32 kodierter URL-Standard, der Zahlungen, Auszahlungen und Anmeldungen über Lightning vereinfacht.

### Millisatoshi (msat)

Die kleinste Recheneinheit auf Lightning: ein Tausendstel [[glossar-allgemein|Satoshi]], ein Hundertmilliardstel Bitcoin. Existiert nur innerhalb von Lightning und lässt sich nicht direkt auf der Kette abrechnen.

### MPP / AMP (Multi-Path Payments)

Aufteilen einer Zahlung in mehrere Teile («Shards»), die parallel über verschiedene Routen laufen und beim Empfänger wieder zusammenkommen. So lassen sich Beträge senden, die in keinen einzelnen Kanal passen. AMP ist eine Variante, bei der jeder Teil seinen eigenen Payment Hash trägt.

### Neutrino

Leichtes Client-Verfahren (BIP-157), mit dem eine Lightning-Node einen entfernten Bitcoin-Full-Node als Backend nutzt — so läuft ein Knoten auch auf schwacher Hardware wie dem Smartphone, ohne die Privatsphäre von SPV-Abfragen zu opfern.

### Onion Routing / Sphinx

Die Technik, mit der eine Zahlung durchs Netz geleitet wird: Die Route steckt in verschachtelten Verschlüsselungsschichten, und jeder Knoten schält nur seine eigene ab. Er kennt jeweils nur Vorgänger und Nachfolger, nicht Absender oder Ziel. Lightning nutzt dafür das Sphinx-Format.

### Peer

Ein anderer Knoten, mit dem man direkt verbunden ist — über eine verschlüsselte Verbindung, mit oder ohne gemeinsamen Kanal.

### Preimage / Payment Hash

Der Empfänger wählt eine Zufallszahl (Preimage), bildet ihren Hash (Payment Hash) und setzt ihn in die Rechnung. Die Zahlung wird an diesen Hash geleistet; das Offenlegen des Preimage beim Einlösen gilt als Zahlungsbeweis und löst die HTLCs entlang der Route.

### Private Channel (unangekündigter Kanal)

Ein Kanal, der nicht im Gossip veröffentlicht wird. Er lässt sich normal nutzen, taucht aber nicht im öffentlichen Graphen auf; für Zahlungseingänge müssen seine Daten in die Rechnung eingebettet werden.

### Probing

Das Absenden von Test-Zahlungen ohne Einlösung, um Routen zu finden oder die Kapazität von Kanälen abzuschätzen.

### PTLC (Point Time-Locked Contract)

Vorgeschlagene Verbesserung der HTLCs, die statt eines gemeinsamen Hashes je Sprung ein eigenes kryptografisches Geheimnis nutzt. Das erschwert das Nachverfolgen einer Zahlung entlang der Route. Setzt Schnorr voraus.

### Revocation Key / RSMC

Der Mechanismus hinter dem Strafsystem: Beim Aktualisieren des Kanalstands geben die Partner die Schlüssel des alten Zustands frei und «widerrufen» ihn damit. Wer später einen widerrufenen Zustand veröffentlicht, verliert sein Kanalguthaben (siehe Channel Breach).

### Routing / Pathfinding

Der Weg einer Zahlung vom Sender zum Empfänger über eine Kette von Kanälen. Bei Lightning wählt der Sender die Route selbst (Source-based Routing) — das senkt die Erfolgsquote gegenüber netzgesteuertem Routing, erhöht aber die Privatsphäre.

### Satoshi / Bitcoin auf Lightning

Auf Lightning werden dieselben Bitcoin bewegt wie auf der Kette, nur in Kanälen und feiner teilbar (bis Millisatoshi). Es gibt keine eigene «Lightning-Münze».

### SCB (Static Channel Backup)

Ein Backup, das nicht den aktuellen Kanalstand enthält, wohl aber genug Information, um im Notfall die Gegenseite zur Schliessung der Kanäle aufzufordern und die Mittel zurückzuholen.

### Short Channel ID (scid)

Eine kompakte Kennung eines Kanals, abgeleitet aus der Position seiner Funding-Transaktion in der Blockchain (Blockhöhe, Index, Ausgang).

### Submarine Swap

Ein vertrauensloser Tausch zwischen On-Chain-Bitcoin und einer Lightning-Zahlung, abgesichert über denselben Preimage-Mechanismus wie ein HTLC. Der umgekehrte Weg (Lightning zu On-Chain) heisst Reverse Submarine Swap.

### Time Lock Delta

Der zeitliche Puffer (in Blöcken), den ein weiterleitender Knoten für seine HTLCs verlangt, damit er im Streitfall genug Zeit hat, seine Ansprüche durchzusetzen. Beruht auf den Timelocks CLTV/CSV der Basisschicht (siehe [[glossar-bitcoin-technik|Timelock]]).

### Turbo Channel (Zero-Conf)

Ein Kanal, der schon mit null Bestätigungen der Funding-Transaktion als nutzbar gilt. Bequem, verlangt aber Vertrauen in den Eröffner.

### Watchtower

Ein Wächterdienst, der Kanäle auf Betrugsversuche überwacht und im Fall der Fälle die Penalty-Transaktion einreicht — auch wenn der eigene Knoten offline ist. Er hat keinen Zugriff auf die Mittel.

### Wumbo Channel

Ein Kanal über der früheren Obergrenze von rund 0,168 BTC (2^24 − 1 Satoshi). Heute sind grössere Kanäle üblich.

### Zombie Channel

Ein Kanal, der zwar noch on-chain und im Graphen existiert, aber lange inaktiv ist und wohl nicht mehr aktiv wird. Solche Kanäle schliesst man besser.

## Related

- [[lightning-netzwerk-grundlagen]]
- [[skalierung-lightning-ark-statechains]]
- [[glossar-bitcoin-technik]]
- [[glossar-allgemein]]

## Open Questions

Keine offenen Punkte. Neue Lightning-Begriffe (etwa rund um Taproot-Kanäle oder PTLCs, sobald aktiv) kommen hier dazu.
