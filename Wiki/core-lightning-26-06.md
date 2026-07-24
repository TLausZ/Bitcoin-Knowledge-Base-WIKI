# Core Lightning 26.06

**Status:** established
**Themen:** protokoll, lightning, wallets
**Last updated:** 2026-06-09
**Sources:** [[Core Lightning 26.06_ _Quantum-Resistant Lightning Channel”]]

## Summary

Core Lightning (CLN) 26.06 (veröffentlicht 2026-06-04, Blockstream/Rusty Russell et al.) ist ein Major Release mit drei Schwerpunkten: Konsolidierung der xpay-Architektur als neuer Standard für Zahlungen, Vorbereitung auf quantenresistente Channels, und eine fundamentale Architekturumstellung der Block-Verarbeitung via "bwatch". Das Release enthält 236 Commits von 19 Autoren in 42 Tagen.

## Body

### xpay als neuer Zahlungsstandard

Das Kernthema des Releases ist die vollständige Ablösung des Legacy-`pay`-Befehls durch `xpay`. Ab 26.06 wird `pay` intern von `xpay` übernommen (kann mit `xpay-handle-pay=false` deaktiviert werden). Gleichzeitig wurden folgende Legacy-Befehle formal depreciert: `keysend`, `pay`, `paystatus`, `getroute`.

Neue xpay-Funktionen:

- **`xkeysend`**: Nachfolger von `keysend` mit modernem Routing-Support
- **`sendamount`**: Neuer JSON-RPC-Befehl — gibt den Betrag an, den der Sender zahlen will (nicht den empfangenen Betrag); nützlich für präzises Liquiditäts- und Fee-Management
- **Shadow CLTV additions**: `xpay` maskiert das finale Zahlungsziel per Shadow-CLTV-Ergänzungen gemäss BOLT 7 — besserer Schutz gegen Netzwerkbeobachtung
- **Smarter Retries**: Bei `channel_update`-Fehlern aktualisiert `xpay` dynamisch die Route für den laufenden Zahlungsversuch

### Quantum-Resistente Channels

Der "Quantum-Resistant Lightning Channel" im Release-Titel bezieht sich auf Grundlagenarbeit für die Zukunftssicherheit des Lightning-Protokolls gegenüber Quantencomputern. Details zur technischen Implementierung liegen in den BOLT-Spezifikationen; CLN 26.06 legt die Basis dafür.

### Splicing-Verbesserungen

Splicing wurde in CLN 26.04 eingeführt; 26.06 behebt kritische Edge Cases:

- Hohe-Gebühren-Bug: `splicein`/`spliceout` brachen vorher bei bestimmten Fee-Konstellationen vorzeitig ab
- Partial-Sats-Bug: Channel-Balances mit Satoshi-Bruchteilen blockierten Splice-Operationen
- Ergebnis: Splicing ist jetzt schneller, günstiger und stabiler

**Change Output Protection**: Interne Transaktionen erstellen jetzt korrekt Change Outputs (>330 sat) für P2TR und P2WPKH. Vorher wurden kleine Change-Beträge versehentlich als Miner-Fee absorbiert.

### Graceful Shutdown

Neuer `graceful` JSON-RPC-Befehl für sauberes Node-Herunterfahren ohne Unterbrechung aktiver Prozesse. Das `systemd`-Service-Script wurde entsprechend aktualisiert.

**Protokolländerung**: CLN wartet jetzt 72 Blöcke (vorher 12) bevor Channels in bestimmten Dispute-Windows geschlossen werden — mehr Sicherheitspuffer für Routing-Umgebungen.

### BOLT12 und Monitoring

- **`createproof`** (experimentell): Erzeugt kryptographischen Zahlungsnachweis für erfolgreiche BOLT12-Zahlungen
- **`decode`**: Unterstützt jetzt nativ Payer-Proofs für externe Transaktionsverifikation
- **OpenTelemetry Unix Socket**: Enterprise-Node-Betreiber können jetzt Performance-Metriken direkt in bestehende Monitoring-Stacks (Prometheus, Grafana) pipen

### bwatch: Architekturrevolution für Block-Processing

Das wichtigste technische Fundament des Releases ist `bwatch` (experimentell) — eine fundamentale Neuarchitektur der Blockchain-Überwachung:

**Bisher**: `lightningd` pollte alle 30 Sekunden das `bcli`-Plugin, holte Roh-Block-Daten von `bitcoind` und parste jeden Block manuell nach relevanten Script Pubkeys und Outpoints. Für grosse Nodes rechenintensiv.

**Mit bwatch**:
```
[ Bitcoin D ] <—> [ BCLI Plugin ] <—> [ Bwatch Plugin ] <—> [ Lightning D ]
```

- `lightningd` registriert "Watches" bei `bwatch` statt selbst zu pollten
- `bwatch` verarbeitet Roh-Block-Daten mit O(1)-Hash-Table-Lookups im Arbeitsspeicher
- Nur bei Match wird `lightningd` benachrichtigt — kein Rauschen
- **Watch Persistence**: Watches überleben Node-Neustarts (früher: komplette Rekonstruktion)
- **Schnelles Catch-Up**: Beim Start rehydriert `bwatch` seinen State ohne 30-Sekunden-Poll-Loops
- **Crash-Resistenz**: Command-Acknowledgment-System + Pending-Operations-Queue — keine verlorenen Notifications bei Absturz
- **Reorg-Handling**: `revert_block_process`-Routine rollt Updates bei Chain-Reorganisationen präzise pro Watch zurück

bwatch öffnet die Möglichkeit, dass eine einzige Block-Watch-Engine mehrere unabhängige "Nodelets" gleichzeitig bedient — relevant für zukünftige Skalierungsarchitekturen.

## Related

- [[skalierung-lightning-ark-statechains]]
- [[lightning-splicing]]
- [[segregated-witness-segwit]]
- [[taproot-musig2-frost]]
- [[transaktionsgebuehren-und-mempool]]

- [[einfuehrung-in-das-lightning-netzwerk|Einführung in das Lightning-Netzwerk (Antonopoulos, Osuntokun & Pickhardt)]] ← Buch

## Open Questions

- Wann wird der Quantum-Resistant Channel-Mechanismus in den BOLT-Standard aufgenommen?
- Wie verhält sich bwatch bei sehr grossen Nodes mit tausenden Channels und hohem Block-Volumen?
- Wann wird `bwatch` den experimentellen Status verlassen?
