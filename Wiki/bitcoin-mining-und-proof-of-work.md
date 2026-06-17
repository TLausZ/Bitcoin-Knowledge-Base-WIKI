# Bitcoin Mining und Proof of Work

**Status:** established
**Last updated:** 2026-06-04
**Sources:** [[20250327_wie-funktioniert-bitcoin-mining-eigentlich]], [[20260424_wie-das-21-millionen-limit-von-bitcoin-tatsächlich-durchgesetzt-wird]]

## Summary

Bitcoin-Mining ist der Prozess, durch den neue Blöcke zur Blockchain hinzugefügt werden. Miner berechnen Millionen von Hashwerten in der Hoffnung, einen zu finden, der kleiner als ein vorgegebener Zielwert ist. Dieser Aufwand — Proof of Work — sichert das Netzwerk, weil Angriffe real Geld und Energie kosten. Das Netzwerk passt die Schwierigkeit alle zwei Wochen an, um die Blockzeit bei etwa zehn Minuten zu halten.

## Body

### Das Grundprinzip: Würfeln mit riesigen Zahlen

Bitcoin-Mining ist kein „Lösen komplexer mathematischer Rätsel" im klassischen Sinne. Es ist im Grunde ein Würfelspiel: Miner müssen eine Zahl würfeln, die kleiner als ein vorgegebener Zielwert ist. Da Würfelergebnisse zufällig und unvorhersehbar sind, ist Erfolg eine Frage der Wahrscheinlichkeit und der Anzahl der Versuche pro Sekunde.

Der Zielwert bestimmt den Schwierigkeitsgrad: Niedriger Zielwert → schwieriger (nur wenige Ergebnisse gelten); hoher Zielwert → leichter.

### Hashfunktionen statt Würfel

Statt echter Würfel verwenden Miner die kryptografische Hashfunktion **SHA-256**. Sie hat für diesen Zweck ideale Eigenschaften:

- **Zufällig wirkend:** Das Ergebnis lässt sich nicht vorhersagen — man muss einfach rechnen
- **Verifizierbar:** Derselbe Input erzeugt immer denselben Output; jeder kann das Ergebnis nachprüfen
- **Nicht umkehrbar:** Man kann aus einem Hashwert nicht auf den Input schließen
- **Riesiger Wertebereich:** 2^256 mögliche Ergebnisse — weit mehr als genug für beliebig hohe Schwierigkeit

### Was Miner konkret tun

Miner bauen den nächsten Block: Sie sammeln ausstehende Transaktionen aus dem Mempool, fügen einen Verweis auf den vorherigen Block ein (was die „Blockchain" bildet), und verändern dann immer wieder eine kleine Zahl im Block-Header (den Nonce), um neue Hashwerte zu erzeugen. Moderne ASIC-Hardware schafft mehrere Billionen Hash-Berechnungen pro Sekunde.

Wenn ein Hashwert kleiner als der aktuelle Zielwert ist, hat der Miner einen gültigen Block gefunden. Er erhält dafür die Block Subsidy (neue Bitcoin) plus alle Transaktionsgebühren des Blocks.

### Schwierigkeitsanpassung

Alle 2016 Blöcke (~zwei Wochen) passt das Bitcoin-Netzwerk den Zielwert automatisch an, sodass die durchschnittliche Blockzeit bei zehn Minuten bleibt. Wächst die globale Hashrate (mehr Miner, schnellere Hardware), sinkt der Zielwert → schwieriger. Verlässt Hashrate das Netzwerk, steigt er → leichter.

Diese Regelung sorgt für einen stabilen Takt der Blockchain, unabhängig davon, wie viel Hardware global eingesetzt wird.

### Warum Proof of Work das Netzwerk sichert

Der physische Aufwand — Strom, Hardware, Grundstücke — ist der eigentliche Sicherheitsmechanismus. Um einen Block rückwirkend zu verändern, müsste ein Angreifer mehr Rechenleistung aufbringen als alle ehrlichen Miner zusammen. Das ist wirtschaftlich prohibitiv teuer.

Ohne Proof of Work wäre Bitcoin nichts weiter als eine leicht manipulierbare Datenbank. Mit PoW ist Angriff teurer als ehrliches Mining.

## Related

- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[konsensregeln-und-mempool-richtlinien]]

## Open Questions

- Wie entwickeln sich die Sicherheitsanreize, wenn die Block Subsidy ausläuft und nur Transaktionsgebühren verbleiben?
- Gibt es Alternativen zu Proof of Work, die vergleichbare Sicherheitsgarantien bieten?
