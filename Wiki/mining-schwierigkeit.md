# Mining-Schwierigkeit

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[learnmeabitcoin-beginners-guide-difficulty]], [[alex-waltz-difficulty-adjustment]]

## Summary

Die Mining-Schwierigkeit steuert, wie schwer es ist, einen gültigen Block zu finden. Sie passt sich alle 2016 Blöcke (~2 Wochen) automatisch an, um die durchschnittliche Blockzeit bei 10 Minuten zu halten. Wenn mehr Miner einsteigen und Blöcke schneller gefunden werden, steigt die Schwierigkeit; wenn Miner das Netzwerk verlassen, sinkt sie. Der Anpassungsfaktor ist auf ×4 (nach oben wie unten) pro Periode begrenzt. Seit dem Genesis-Block wurde die Schwierigkeit über 370 Mal angepasst; der größte Anstieg betrug 302 %, der größte Rückgang 27 %.

## Body

### Was die Schwierigkeit misst

Die Schwierigkeit ist eine Zahl, die ausdrückt, wie viele Hashes ein Miner im Durchschnitt berechnen muss, bevor er einen gültigen Block findet. Technisch gesehen bestimmt sie den Target-Wert: Je kleiner der Target, desto unwahrscheinlicher ist ein gültiger Hash, desto mehr Versuche sind nötig.

```
Target = Max_Target / Difficulty
```

Der Max_Target ist die größtmögliche Zielzahl (Difficulty = 1 = leichteste Stufe). Er wurde von Satoshi im Genesis-Block hardcodiert. Jeder SHA-256-Hash eines Block-Headers wird mit dem aktuellen Target verglichen: liegt der Hash darunter, ist der Block gültig.

Der Target selbst wird im Block-Header im Feld `Bits` in komprimierter Form gespeichert. Weil der Target Teil der Blockdaten ist, die gehasht werden, lässt er sich nachträglich nicht fälschen — Difficulty-Manipulation ist protokollintern unmöglich.

### Automatische Anpassung alle 2016 Blöcke

Bitcoin misst alle 2016 Blöcke die tatsächlich verstrichene Zeit und vergleicht sie mit der erwarteten Zeit:

```
Neue Difficulty = Aktuelle Difficulty × (Erwartete Zeit / Tatsächliche Zeit)
```

Erwartete Zeit: 2016 Blöcke × 10 Minuten = 20.160 Minuten (~2 Wochen)

Die Begrenzung auf Faktor 4 pro Periode schützt gegen extreme Sprünge — und begrenzt auch den Schaden bei einem Isolation-Angriff (ein Node, der von falschen Zeitstempeln getäuscht wird, kann die Schwierigkeit nur um maximal Faktor 4 senken).

### Der Off-by-1-Bug und seine Konsequenzen

Obwohl die Anpassung alle 2016 Blöcke stattfindet, vergleicht der Code nur 2015 Lücken — weil er den Zeitstempel des ersten und des letzten Blocks der Periode vergleicht, nicht die Zeit aller 2016 Abstände. Das führt dazu, dass Blöcke im Schnitt nicht genau 10 Minuten, sondern etwa 10,005 Minuten benötigen. Satoshi kannte diesen Bug; er ist bis heute im Code, weil eine Korrektur einen Hard Fork erfordern würde.

Der Bug ermöglicht theoretisch einen **Time Warp Attack**: Ein Angreifer mit Miner-Mehrheit könnte die Zeitstempel so manipulieren, dass die Schwierigkeit dauerhaft gegen 1 gedrückt wird. In der Praxis wäre das im Chain-Explorer sofort sichtbar und erforderte erhebliche Miner-Koordination. Mehr dazu: [[bitcoin-block-zeitregeln]].

### Zeitstempel-Manipulation: Warum Miner lügen würden

Miner fügen bei jedem Block einen Zeitstempel hinzu. Wenn dieser zu weit in der Vergangenheit liegt (weniger Blöcke scheinbar schneller) oder zu weit in der Zukunft (mehr Zeit vorgespiegelt), verändert das die Difficulty-Berechnung. Bitcoin schützt dagegen mit drei Regeln:

- Block-Zeitstempel muss größer sein als der Median der letzten 11 Blöcke (Konsensregel)
- Block-Zeitstempel darf nicht mehr als 2 Stunden in der Zukunft liegen (Policy-Regel)
- Lokale Systemuhr darf maximal 90 Minuten vom Peer-Median abweichen (Client-Regel)

### Hex-Darstellung von Hash und Target

Block-Hashes und Targets werden in Hexadezimal angezeigt. Da kleinere Zahlen mit mehr führenden Nullen beginnen, ist es einfach zu erkennen, ob ein Hash den Target unterschreitet.

Beispiel Block 100.000 (Difficulty 14.484):
```
Hash:   000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506
Target: 00000000000404CB000000000000000000000000000000000000000000000000
```
Der Hash unterschreitet den Target → gültiger Block.

### Warum 10 Minuten?

Zehn Minuten ist ein Kompromiss zwischen schneller Bestätigung und ausreichend Zeit für die Blockverbreitung im Netzwerk. Würden Blöcke sekündlich produziert, käme es ständig zu Konflikten zwischen gleichzeitig gefundenen Blöcken. Der Wert `2016` (Anzahl Blöcke pro Periode) ergibt sich direkt: 2 Wochen / 10 Minuten = 2016.

Zur Grössenordnung: Ein Apple M1 Max schafft ~5,8 MH/s. Bei der Schwierigkeit von Anfang 2024 würde es 727 Millionen Jahre dauern, einen Block zu finden. 2010 konnte Thymos (damals bekannt) mit einem Pentium-Prozessor in einer Woche 5 Blöcke minen.

### bitcoin-cli

```
bitcoin-cli getdifficulty
```

Gibt die aktuelle Schwierigkeit als Dezimalzahl zurück.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-block-zeitregeln]]
- [[bitcoin-chainwork]]
- [[bitcoin-blockchain-struktur]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-whitepaper-errata]] ← Paper beschreibt Moving Average, implementiert ist der 2016-Blöcke-Vergleich

## Open Questions

- Wie entwickelt sich die Schwierigkeit nach dem nächsten Halving?
- Könnte der Time Warp Attack durch einen Soft Fork geschlossen werden?
