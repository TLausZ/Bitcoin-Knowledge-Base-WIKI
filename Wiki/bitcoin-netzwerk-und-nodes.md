# Bitcoin-Netzwerk und Nodes

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[learnmeabitcoin-beginners-guide-network]], [[learnmeabitcoin-beginners-guide-node]], [[learnmeabitcoin-technical-networking-overview]], [[learnmeabitcoin-technical-networking-node]], [[learnmeabitcoin-technical-networking-magic-bytes]], [[2018_Grokking-Bitcoin_Rosenbaum]]

## Summary

Das Bitcoin-Netzwerk ist ein Peer-to-Peer-Netzwerk aus tausenden von Computern (Nodes), die alle dasselbe Programm ausführen und direkt miteinander kommunizieren — ohne zentrale Server. Jeder mit einem Internetzugang kann teilnehmen. Nodes haben drei Aufgaben: Regeln einhalten, Informationen weitergeben und die Blockchain speichern. Das Netzwerk ist so dezentral, dass kein einzelner Akteur es abschalten oder kontrollieren kann.

## Body

### Was ist das Bitcoin-Netzwerk?

Das Bitcoin-Netzwerk besteht aus allen Computern, die gerade das Bitcoin-Programm laufen lassen. Diese Computer heißen Nodes (Knotenpunkte). Sie sind direkt miteinander verbunden — es gibt keine zentrale Instanz, die Transaktionen koordiniert oder genehmigt.

Jeder mit einem Computer und Internetanschluss kann dem Netzwerk beitreten, indem er Bitcoin Core (oder ein anderes kompatibles Programm) herunterlädt. Das Netzwerk ist offen und erlaubnisfrei.

### Wie Informationen sich verbreiten

Wenn jemand eine Bitcoin-Transaktion erstellt, sendet er sie an die Nodes, mit denen er verbunden ist. Diese Nodes prüfen die Transaktion auf Gültigkeit und leiten sie an ihre Nachbar-Nodes weiter. Innerhalb von Sekunden kennt das gesamte Netzwerk die neue Transaktion.

Dasselbe gilt für neue Blöcke: Sobald ein Miner einen gültigen Block findet, verbreitet er sich im gesamten Netzwerk innerhalb weniger Sekunden.

### Die drei Jobs eines Nodes

1. **Regeln befolgen:** Jeder Node prüft jede Transaktion und jeden Block gegen die Bitcoin-Konsensregeln. Ungültige Transaktionen werden abgelehnt und nicht weitergeleitet.
2. **Informationen teilen:** Nodes leiten gültige Transaktionen und Blöcke an ihre Peers weiter — so bleibt das gesamte Netzwerk synchron.
3. **Blockchain speichern:** Jeder Full Node hält eine vollständige Kopie der gesamten Blockchain (aktuell ~852 GB). Das macht das System redundant — selbst wenn viele Nodes ausfallen, bleibt die Blockchain erhalten.

### Welche Transaktionen ein Node sieht

Nodes unterscheiden zwischen zwei Arten von Transaktionen:
- **Neue Transaktionen (Fresh):** Gerade ins Netzwerk gesendet, noch nicht in einem Block. Landen im Mempool.
- **Bestätigte Transaktionen:** Bereits in einem Block auf der Blockchain. Dauerhaft und unveränderlich.

### Brauche ich einen eigenen Node?

Nein. Man kann Bitcoin empfangen und senden ohne eigenen Node, indem man einem öffentlichen Node (z.B. über ein Wallet) vertraut. Aber: Wer seinen eigenen Node betreibt, muss niemandem vertrauen — er prüft alle Regeln selbst. Das ist die konsequenteste Form der Selbstverwahrung.

### Technisches Protokoll: Wie Nodes kommunizieren

Nodes verbinden sich über **TCP auf Port 8333** (Mainnet). Seit Bitcoin Core v27 ist BIP 324 (verschlüsseltes v2-Protokoll) Standard; ältere Nodes verwenden v1 (unverschlüsselt).

**Nachrichtenstruktur:**
```
[Magic Bytes 4B] [Command 12B] [Payload Size 4B] [Checksum 4B] [Payload ...]
```

- **Magic Bytes:** Trennzeichen am Anfang jeder Nachricht. Mainnet: `f9beb4d9`, Testnet3: `0b110907`, Regtest: `fabfb5da`.
- **Command:** ASCII-codierter Befehlsname (auf 12 Bytes mit Nullen aufgefüllt), z.B. `version`, `tx`, `block`
- **Checksum:** Erste 4 Bytes von SHA256(SHA256(payload))

**Verbindungsaufbau (Handshake):**
1. Verbindender Node sendet `version`-Nachricht (enthält Protokollversion, Services, Block-Höhe, User-Agent)
2. Empfangender Node antwortet mit eigenem `version`
3. Beide senden `verack` (Version acknowledged) → Verbindung aktiv

**Transaktionen und Blöcke synchronisieren:**
- Node kündigt neue Objekte mit `inv`-Nachricht an (Inventar: Liste von TXIDs/Block-Hashes)
- Empfänger, der das Objekt noch nicht kennt, antwortet mit `getdata`
- Sender schickt `tx`- oder `block`-Nachricht mit dem eigentlichen Inhalt
- `ping`/`pong` halten die Verbindung aktiv

**v2 Transport (BIP 324):** Verschlüsselt den gesamten Nachrichteninhalt mit ChaCha20-Poly1305. Verhindert Traffic-Analyse durch ISPs und passive Überwacher. Seit Bitcoin Core v27.0 Standard.

### Node-Bootstrapping: Wie ein neuer Node Peers findet

Ein frisch installierter Node kennt keine anderen Nodes. Bitcoin löst das in drei Stufen (Rosenbaum, Kap. 8):

**DNS Seeds (erste Wahl):** Bitcoin Core hat mehrere hartcodierte DNS-Hostnamen eingebaut (z.B. `seed.bitcoin.sipa.be`, `dnsseed.bluematt.me`). Diese DNS-Server antworten mit IP-Adressen aktiver Nodes. Das ist die schnellste Methode für neue Nodes.

**Hartcodierte IPs (Fallback):** Wenn DNS Seeds nicht erreichbar sind, enthält Bitcoin Core eine Liste hartcodierter IP-Adressen als Startpunkt.

**Addr-Gossip (laufender Betrieb):** Sobald ein Node verbunden ist, teilen Peers ihre bekannten Adressen über `addr`-Nachrichten. Nodes speichern eine lokale Datenbank (`peers.dat`) mit bis zu tausenden bekannter Adressen. Bei einem Neustart nutzt der Node diese gespeicherten Adressen statt DNS Seeds.

Ein Node verbindet sich typischerweise mit 8–16 Peers gleichzeitig, um Zensurresistenz zu erhöhen: Ein einzelner bösartiger Peer kann keine Informationen zurückhalten, wenn der Node viele unabhängige Verbindungen hat. [[2018_Grokking-Bitcoin_Rosenbaum]]

### Initial Block Download (IBD) und Signatur-Skipping

Ein neuer Node muss die gesamte Blockchain herunterladen und validieren — das dauert Stunden bis Tage. Bitcoin Core optimiert diesen Prozess:

**Signatur-Skipping:** Signaturen in Blöcken bis zu einem bestimmten "assumed valid block" (tief in der Vergangenheit) werden nicht validiert. Da diese Blöcke Teil der längsten Chain sind und bereits von tausenden Nodes bestätigt wurden, ist das Risiko einer Fälschung praktisch null. Das spart bei IBD erheblich Zeit.

**Parallel-Download:** Blöcke werden von mehreren Peers gleichzeitig heruntergeladen, nicht sequenziell.

**Assumeutxo (neuere Optimierung):** Ermöglicht, nur das aktuelle UTXO-Set zu laden (statt die gesamte Blockchain) und die Validierung der Vergangenheit im Hintergrund nachzuholen. [[2018_Grokking-Bitcoin_Rosenbaum]]

### SPV-Nodes: Lightweight Wallets

Ein **SPV-Node** (Simplified Payment Verification, Satoshi Whitepaper §8) lädt nur Block-Header, nicht die vollständigen Blöcke. Das spart Bandbreite und Speicher drastisch.

Block-Header sind 80 Bytes pro Block — für die gesamte Blockchain bis 2024 ca. 60 MB statt ~852 GB für die volle Chain.

Ein SPV-Node kann nicht selbst prüfen, ob eine Transaktion gültig ist — er prüft nur, dass der Block-Header in der längsten Chain liegt und dass die Transaktion per Merkle-Proof im entsprechenden Block enthalten ist. Das bedeutet: Er vertraut darauf, dass Miner keine ungültigen Transaktionen bestätigen.

SPV-Nodes müssen Peers nach Transaktionen fragen, die für ihre Adressen relevant sind. Das führt zu Privatsphäre-Problemen: Welche Adressen abgefragt werden, verrät den Peers viel. Bloom-Filter (BIP37) sollten dieses Problem lösen, leaken aber immer noch Information. Neuere SPV-Implementierungen nutzen neuronale Filteransätze oder vermeiden das Problem durch neuere Protokoll-Designs. [[2018_Grokking-Bitcoin_Rosenbaum]]

### Dezentralisierung als Kernmerkmal

Die Stärke des Netzwerks liegt darin, dass kein zentraler Punkt existiert, den man abschalten könnte. Selbst wenn eine große Anzahl von Nodes gleichzeitig ausfällt, bleibt das Netzwerk funktionsfähig — es gibt immer noch andere Nodes, die die Blockchain halten und Transaktionen weitergeben.

## Related

- [[wie-funktioniert-bitcoin]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-blockchain-struktur]]
- [[transaktionsgebuehren-und-mempool]]
- [[hardware-wallet-einstieg]]

## Open Questions

- Wie viele aktive Full Nodes gibt es aktuell im Bitcoin-Netzwerk?
- Wie wirkt sich die wachsende Blockchain-Größe auf die Node-Dezentralisierung aus?
