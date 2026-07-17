# Konsensregeln und Mempool-Richtlinien

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-04
**Sources:** [[20251023_der-unterschied-zwischen-bitcoin-konsensregeln-und-mempool-richtlinien]], [[20250508_daten-speichern-auf-der-blockchain-wie-funktioniert-op-return]]

## Summary

Bitcoin-Nodes setzen zwei grundlegend verschiedene Arten von Regeln durch. Konsensregeln bestimmen, ob ein Block gültig ist — sie sind unveränderlich ohne Netzwerk-Fork und werden von allen Nodes identisch durchgesetzt. Mempool-Richtlinien hingegen sind lokale Einstellungen einzelner Nodes, die beeinflussen, welche Transaktionen gespeichert und weitergeleitet werden — sie sind individuell konfigurierbar und können nicht netzwerkweit erzwungen werden.

## Body

### Konsensregeln

Konsensregeln legen fest, was einen gültigen Block ausmacht. Sie sind die Grundlage des Netzwerk-Konsenses: Alle Nodes müssen dieselben Regeln anwenden, damit sie sich auf die „echte" Bitcoin-Blockchain einigen können.

Typische Konsensregeln:
- Transaktionen dürfen keine Bitcoin doppelt ausgeben
- Miner dürfen nicht mehr neue Bitcoin erzeugen als aktuell erlaubt (Block Subsidy)
- Die Blockgrösse darf das festgelegte Maximum nicht überschreiten

Konsensregeln ändern sich nur durch Hard Fork oder Soft Fork — koordinierte Prozesse mit jahrelanger Entwicklung und breitem Konsens (Beispiele: SegWit 2017, Taproot 2021). Unilateral kann man Konsensregeln nicht ändern: Wer seine Node so konfiguriert, dass sie engere Regeln hat als der Rest des Netzwerks, schliesst sich selbst aus.

### Mempool-Richtlinien

Mempool-Richtlinien sind lokale Node-Einstellungen, die beeinflussen, welche Transaktionen im lokalen Mempool gespeichert und an andere weitergeleitet werden. Sie berühren nicht die Frage der Blockgültigkeit.

Typische Mempool-Richtlinien:
- Mindestgebühr (Fee Rate) für die Weiterleitung
- Maximale Datenmenge in OP_RETURN Outputs (Standard: 80 Bytes)
- Maximale Mempool-Grösse
- Ob nicht-standardisierte Transaktionen weitergeleitet werden

Mempool-Richtlinien sind jederzeit konfigurierbar. Selbst wenn eine Node eine Transaktion ablehnt und aus ihrem Mempool entfernt, kann dieselbe Transaktion im nächsten Block auftauchen — und die Node akzeptiert sie trotzdem als gültig, weil keine Konsensregel verletzt wurde.

### Der entscheidende Unterschied

Mempool-Richtlinien können **nicht netzwerkweit erzwungen** werden. Selbst wenn 99,9 % aller Nodes ein bestimmtes Limit durchsetzen, reicht ein einziger Miner aus, der eine abweichende Transaktion in einen Block aufnimmt. Der Gebührenmarkt entscheidet dann, ob Miner diese Transaktion überhaupt wollen.

Beispiel: Das 80-Byte-Limit für OP_RETURN ist eine weit verbreitete Mempool-Richtlinie. Transaktionen mit grösseren OP_RETURN Outputs tauchen dennoch regelmässig in Blöcken auf, weil Miner sie direkt akzeptieren können.

### Praktische Implikationen für Node-Betreiber

Nodes mit unterschiedlichen Ressourcen können Mempool-Richtlinien anpassen:
- Leistungsstarke Node: grösserer Mempool, mehr ältere Transaktionen gespeichert
- Raspberry Pi Node: kleinerer Mempool, Fokus auf aktuelle Transaktionen mit hohen Gebühren

Mempool-Richtlinien schützen auch vor Spam: Eine Mindestgebühr verhindert, dass Nodes mit kostenlosen Transaktionen geflutet und überlastet werden.

## Related

- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-mining-und-proof-of-work]]
- [[op-return-und-datenspeicherung]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch

## Open Questions

- Wo verläuft die sinnvolle Grenze zwischen individuell konfigurierbaren Mempool-Richtlinien und Konsensregeln?
- Wie entwickelt sich die Debatte um OP_RETURN-Limits weiter?
