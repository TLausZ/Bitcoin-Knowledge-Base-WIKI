# OP_RETURN und Datenspeicherung auf der Blockchain

**Status:** established
**Last updated:** 2026-06-04
**Sources:** [[20250508_daten-speichern-auf-der-blockchain-wie-funktioniert-op-return]]

## Summary

OP_RETURN ist ein Bitcoin-Skriptbefehl, der einen Output sofort als ungültig markiert. Er wird verwendet, um Coins nachweislich zu verbrennen oder beliebige Daten auf der Blockchain zu speichern und dabei Nodes zu signalisieren, dass der Output ignoriert werden kann. Das 80-Byte-Standardlimit für OP_RETURN ist eine Mempool-Richtlinie, keine Konsensregel — und schützt nicht wirklich vor Datenspeicherung auf der Blockchain.

## Body

### Datenspeicherung auf der Blockchain ist unvermeidlich

Die Idee, beliebige Daten auf der Bitcoin-Blockchain zu speichern, ist so alt wie das Netzwerk. Satoshi Nakamoto selbst hinterließ im Genesis-Block die Nachricht *„The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"*.

Es gibt mehrere Methoden:
- **STAMP-Protokoll:** Kodiert Bilder in öffentliche Schlüssel — die Outputs können nie ausgegeben werden und blähen das UTXO-Set permanent auf
- **Ordinals/Inscriptions:** Speichert große Datenmengen im Witness-Teil von SegWit-Transaktionen
- **OP_RETURN:** Daten als explizit ungültige Outputs — Nodes können sie verwerfen

Das Speichern beliebiger Daten kann praktisch nicht verhindert werden. Die Frage ist, welche Methode am wenigsten Schaden anrichtet.

### Wie OP_RETURN funktioniert

OP_RETURN ist einer der einfachsten Skriptbefehle. Eine Node, die auf einen OP_RETURN Output stößt, markiert ihn sofort als ungültig und macht weiter.

**Zwei Verwendungszwecke:**

1. **Coins verbrennen:** Bitcoin, die an einen OP_RETURN Output gesendet werden, sind für immer gesperrt. Niemand kann sie jemals ausgeben — nachweisbar, irreversibel.

2. **Daten als irrelevant markieren:** Der OP_RETURN-Befehl ist eine Botschaft an das Netzwerk: *„Ignoriere diesen Output."* Nodes müssen OP_RETURN-Outputs nicht ins UTXO-Set aufnehmen und können sie verwerfen. Pruned Nodes (Nodes ohne vollständige Blockchain) profitieren davon besonders.

Im Vergleich zu STAMP oder Inscriptions ist OP_RETURN die „sauberste" Methode, Daten on-chain zu speichern — die Outputs belasten das Netzwerk weniger dauerhaft.

### Das 80-Byte-Limit und die Debatte 2025

Bitcoin Core setzt standardmäßig ein Limit von 80 Bytes für Daten in OP_RETURN Outputs durch. Das ist eine **Mempool-Richtlinie**, keine Konsensregel.

Das Limit verhindert nicht wirklich das Speichern größerer Datenmengen: Ein einziger Miner kann Transaktionen mit größeren OP_RETURN Outputs direkt in Blöcke aufnehmen. Und für wirklich große Datenmengen werden sowieso alternative Methoden (Inscriptions) verwendet.

2025 schlug ein Bitcoin Core Entwickler vor, das 80-Byte-Limit abzuschaffen. Das Hauptargument: Das Limit ist ineffektiv und fördert aktiv die Nutzung von Alternativen wie Inscriptions, die das UTXO-Set aufblähen. Gegner sahen darin eine Normalisierung von Nicht-Finanztransaktionen und bemängelten den Prozess.

### Der natürliche Spam-Schutz: Gebührenmarkt

Bitcoin hat einen effektiven langfristigen Schutzmechanismus gegen Daten-Spam: den Gebührenmarkt. Wenn der Blockspace knapp ist (viele Transaktionen), steigen die Gebühren. Da niemand unendlich viele Bitcoin hat, um dauerhaft Daten zu speichern, reguliert sich das von selbst.

## Related

- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]

## Open Questions

- Wird das 80-Byte-OP_RETURN-Limit in Bitcoin Core 29+ abgeschafft?
- Wie entwickelt sich die Nutzung von Ordinals/Inscriptions bei steigenden Gebühren?
