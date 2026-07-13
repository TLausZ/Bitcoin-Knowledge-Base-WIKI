# Coinbase-Transaktions-Duplikate

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-transaction-in-two-blocks]]

## Summary

Es gibt genau zwei Transaktionen in der Bitcoin-Geschichte, die in zwei verschiedenen Blöcken gleichzeitig auftauchen — beide aus dem Jahr 2010. Möglich war das, weil frühe Coinbase-Transaktionen keine Block-Höhe enthielten. Wenn zwei Miner denselben Output verwendeten, hatten beide Coinbase-Transaktionen identische Daten und damit dieselbe Transaktions-ID. BIP30 und BIP34 schlossen diese Lücke.

## Body

### Was eine Coinbase-Transaktion ist

Jeder Block beginnt mit einer Coinbase-Transaktion (nicht zu verwechseln mit der Börse): ein spezieller Eintrag, mit dem der Miner sich selbst die Block-Belohnung und die Transaktionsgebühren auszahlt. Diese TX hat keinen echten Input; das Geld entsteht aus dem Nichts, erlaubt durch die Konsensregeln.

### Warum TX-IDs kollidieren konnten

Eine Transaktions-ID (TXID) ist der Double-SHA256-Hash der gesamten Transaktionsdaten. Wenn zwei Coinbase-Transaktionen identische Outputs haben (z.B. beide zahlen an denselben Public Key und denselben Betrag), sind ihre Daten identisch — und damit auch ihre Hash-Werte. Genau das passierte in zwei Fällen 2010.

Für normale Transaktionen ist das praktisch unmöglich, weil Inputs (UTXOs aus vorherigen Transaktionen) immer unterschiedlich sind. Aber Coinbase-Transaktionen haben keinen echten Input.

### Die Fixes

**BIP30** (2012): Kein Block darf eine Transaktion enthalten, deren TXID mit einer noch nicht ausgegebenen Transaktion in einem früheren Block übereinstimmt. Das verhindert, dass neue Duplikate entstehen. Für die zwei bereits existierenden Fälle gibt es hartcodierte Ausnahmen im Bitcoin Core Code.

**BIP34** (2012): Jede Coinbase-Transaktion muss die aktuelle Block-Höhe als erstes Element des Coinbase-Feldes enthalten. Da jede Block-Höhe einmalig ist, sind Coinbase-TXIDs seitdem garantiert eindeutig. Der letzte Block ohne diese Regel (Version 1) war Block 227.835, gemined 2013.

### Warum das ein echtes Problem war

Doppelte TXIDs konnten in seltenen Fällen zu unerwünschtem Verhalten führen: Ein Node könnte eine ältere Transaktion durch eine neuere mit gleicher ID ersetzen, was die Confirmations effektiv auf 1 reduziert und Double-Spend-Risiken erhöht. Zudem drohten potenzielle Chain-Splits, wenn Nodes unterschiedlich auf die Duplikate reagierten.

## Related

- [[bitcoin-transaktionsstruktur]]
- [[bitcoin-mining-und-proof-of-work]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bip-0030]]
- [[bip-0034]]
