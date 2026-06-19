# Mining-Schwierigkeit

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-guide-difficulty]]

## Summary

Die Mining-Schwierigkeit steuert, wie schwer es ist, einen gültigen Block zu finden. Sie passt sich alle 2016 Blöcke (~2 Wochen) automatisch an, um die durchschnittliche Blockzeit bei 10 Minuten zu halten. Wenn mehr Miner einsteigen und Blöcke schneller gefunden werden, steigt die Schwierigkeit; wenn Miner das Netzwerk verlassen, sinkt sie. Der Anpassungsfaktor ist auf ×4 (nach oben wie unten) pro Periode begrenzt.

## Body

### Was die Schwierigkeit misst

Die Schwierigkeit ist eine Zahl, die ausdrückt, wie viele Hashes ein Miner im Durchschnitt berechnen muss, bevor er einen gültigen Block findet. Technisch gesehen bestimmt sie den **Target-Wert**: Je kleiner der Target, desto unwahrscheinlicher ist ein gültiger Hash, desto mehr Versuche sind nötig.

```
Target = Max_Target / Difficulty
```

Der Max_Target ist die größtmögliche Zielzahl (d.h. Difficulty = 1 = leichteste Stufe). Jeder SHA-256-Hash eines Block-Headers wird mit dem aktuellen Target verglichen: liegt der Hash darunter, ist der Block gültig.

### Automatische Anpassung alle 2016 Blöcke

Bitcoin misst alle 2016 Blöcke die tatsächlich verstrichene Zeit und vergleicht sie mit der erwarteten Zeit:

```
Neue Difficulty = Aktuelle Difficulty × (Erwartete Zeit / Tatsächliche Zeit)
```

**Erwartete Zeit:** 2016 Blöcke × 10 Minuten = 20160 Minuten (~2 Wochen)

- Blöcke kamen schneller als erwartet → Schwierigkeit steigt
- Blöcke kamen langsamer als erwartet → Schwierigkeit sinkt

**Begrenzung:** Die Schwierigkeit kann sich pro Periode maximal um Faktor 4 ändern — ein Schutz gegen extreme Sprünge.

### Hex-Darstellung von Hash und Target

Block-Hashes und Targets werden in Hexadezimal angezeigt. Da kleinere Zahlen mit mehr führenden Nullen beginnen, ist es einfach zu erkennen, ob ein Hash den Target unterschreitet: Ein gültiger Block-Hash hat viele führende Nullen.

**Beispiel Block 100.000 (Difficulty 14.484):**
```
Hash:   000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506
Target: 00000000000404CB000000000000000000000000000000000000000000000000
```
Der Hash unterschreitet den Target → gültiger Block.

### Warum 10 Minuten?

Zehn Minuten ist ein Kompromiss zwischen schneller Bestätigung und ausreichend Zeit für die Blockverbreitung im Netzwerk. Würden Blöcke sekündlich produziert, käme es ständig zu Konflikten zwischen gleichzeitig gefundenen Blöcken, weil das Netzwerk nicht schnell genug synchronisieren könnte.

### bitcoin-cli

```
bitcoin-cli getdifficulty
```

Gibt die aktuelle Schwierigkeit als Dezimalzahl zurück.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-blockchain-struktur]]
- [[konsensregeln-und-mempool-richtlinien]]

## Open Questions

- Wie entwickelt sich die Schwierigkeit nach dem nächsten Halving?
- Welchen Einfluss hat die Schwierigkeit auf den Bitcoin-Preis (und umgekehrt)?
