# Bitcoin Chainwork und kumulativer Proof-of-Work

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bitcoin-total-hash-computations]]

## Summary

Der Chainwork ist die Summe des erwarteten Proof-of-Work für alle Blöcke in der längsten Kette — ausgedrückt als Anzahl berechneter Hashes. Stand Anfang 2024 betrug er ~3 × 10²⁸. Das Wachstum ist exponentiell: In den letzten 24 Stunden werden heute mehr Hashes berechnet als in den ersten sieben Jahren von Bitcoins Geschichte zusammen.

## Body

### Was Chainwork bedeutet

Die Formulierung „längste Kette gewinnt" aus dem ursprünglichen Whitepaper war ungenau. Bitcoin folgt tatsächlich der Kette mit dem meisten kumulativen Proof-of-Work — nicht der mit den meisten Blöcken. Chainwork ist diese Messgröße: die Summe der erwarteten Hashes über alle Blöcke.

„Erwartet" deswegen, weil Mining stochastisch ist. Man weiss nicht, wie viele Hashes ein Miner tatsächlich berechnet hat, um einen Block zu finden. Man weiss nur, wie schwer es war (Difficulty × Anzahl Blöcke) — und daraus lässt sich der statistische Erwartungswert berechnen.

### Wie man ihn abfragt

```
bitcoin-cli getblock <blockhash>
```

Gibt u.a. das Feld `chainwork` zurück — eine Hexadezimalzahl. Für Block 824.611:
```
00000000000000000000000000000000000000006461840778f581d008176064
```

Konvertiert zu Dezimal ergibt das ~3 × 10²⁸ Hashes.

### Warum die Zahl bedeutsam ist

Zum Vergleich: die Anzahl der Sandkörner auf der Erde liegt schätzungsweise bei 10¹⁸ bis 10¹⁹. Die Anzahl der Atome im sichtbaren Universum beträgt ~10⁸⁰. 3 × 10²⁸ liegt dazwischen — es ist eine astronomische, aber nicht unvorstellbare Zahl.

Das exponenzielle Wachstum zeigt die Vertrauenswürdigkeit der Kette: Je mehr kumulativer Work dahinter steckt, desto teurer wird es, sie umzuschreiben. Ein Angreifer, der die letzten 1.000 Blöcke neu berechnen wollte, müsste mehr elektrische Energie aufwenden als die Hälfte der globalen Energieproduktion.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[mining-schwierigkeit]]
- [[bitcoin-blockchain-struktur]]
