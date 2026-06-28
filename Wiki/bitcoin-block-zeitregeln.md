# Bitcoin Block-Zeitregeln

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bitcoin-block-time-anomaly]], [[alex-waltz-difficulty-adjustment]]

## Summary

Bitcoin verwaltet Zeit bewusst unpräzise. Miner setzen Zeitstempel in jeden Block, aber da sie Anreize haben, diese zu fälschen, gibt es drei Schutzregeln. Die Regeln lassen genug Spielraum für echte Netzwerk-Latenz, aber verhindern extreme Manipulationen. Blocks mit einem Zeitstempel „aus der Zukunft" sind deshalb gelegentlich möglich und kein Fehler.

## Body

### Die drei Zeitregeln

**MedianPast Time Rule (Konsensregel):** Ein Block wird nur akzeptiert, wenn sein Zeitstempel größer ist als der Median der letzten 11 Blöcke. Das verhindert, dass die Blockchain zeitlich rückwärts läuft. Weil es ein Median ist, müsste ein Angreifer sechs der letzten elf Blöcke kontrollieren, um es zu umgehen. Blöcke, die diese Regel verletzen, werden von allen Nodes abgelehnt.

**Future Block Time Rule (Policy-Regel):** Der Zeitstempel darf nicht mehr als zwei Stunden über der Median-Zeit der Peer-Nodes liegen. Das ist eine Policy-Regel, keine Konsensregel — ein Block kann lokal als „zu weit in der Zukunft" abgelehnt werden, bleibt aber potenziell gültig. Sobald die lokale Zeit aufholt, kann er akzeptiert werden. Das erklärt, warum Block 2.289 früher abgebaut wurde als Block 2.297: Dessen Zeitstempel lag innerhalb der 2-Stunden-Grenze, kam aber früher ins Netzwerk.

**Local Client Rule:** Die maximale Abweichung zwischen dem Zeitstempel eines Peers und der lokalen Systemuhr beträgt 90 Minuten. Das ist die lockerste der drei Regeln.

### Warum Miner den Zeitstempel fälschen würden

Die Schwierigkeitsanpassung basiert auf Zeitstempeln. Wenn Miner behaupten könnten, ein Block habe länger gedauert als er tatsächlich hat, würde das die Schwierigkeit für die nächste Periode senken — einfacheres Mining, mehr Coins. Gleichzeitig ist der Zeitstempel selbst Teil der Blockdaten, die gehasht werden; er kann also nicht nachträglich gefälscht werden, ohne den Hash zu brechen.

### Das Off-by-1-Problem und die Time Warp Attack

Die Difficulty-Anpassung vergleicht den Zeitstempel des ersten und des letzten Blocks einer 2016-Block-Periode. Zwischen 2016 Blöcken gibt es aber nur 2015 Lücken — Satoshi hatte einen Off-by-1-Bug eingebaut. Dieser ist bis heute im Code, weil eine Korrektur einen Hard Fork erfordern würde.

Der Bug ermöglicht theoretisch einen Time Warp Attack: Da der letzte Block einer Periode nicht mit dem ersten Block der nächsten Periode überlappen muss, könnte ein gut koordinierter Angriff den letzten Block mit einem weit in der Vergangenheit liegenden Zeitstempel versehen — innerhalb der erlaubten Grenzen. Das würde die Difficulty auf nahezu 1 sinken lassen, wenn es wiederholt wird. Praktisch erfordert das Miner-Koordination und wäre sofort im Chain-Explorer sichtbar.

Satoshi wollte ursprünglich NTP (Network Time Protocol) einbauen — das ist im Originalcode kommentiert. NTP ist jedoch zentral genug, dass es nicht sinnvoll mit Bitcoins Dezentralisierungsziel vereinbar ist. Deshalb wurde es nie implementiert.

### Warum das kein Problem ist

In Bitcoin ist Reihenfolge wichtiger als exakte Zeit. Blöcke müssen in einer definierten Sequenz stehen (für Double-Spend-Schutz), aber ob Block 2.289 exakt eine Minute vor Block 2.297 gemined wurde oder zehn Minuten, ist egal. Das System lässt bewusst Spielraum für Netzwerk-Latenz, unterschiedliche Systemuhren und ehrliche Messungenauigkeit.

## Related

- [[mining-schwierigkeit]]
- [[bitcoin-mining-und-proof-of-work]]
- [[konsensregeln-und-mempool-richtlinien]]

## Open Questions

- Würde ein Soft Fork den Off-by-1-Bug schliessen können, ohne den Chainwork zu beeinflussen?
- Wie reagiert das Netzwerk, wenn ein grosser Miner-Pool konsistent zu weit in die Zukunft datiert?
