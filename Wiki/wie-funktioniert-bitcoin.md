# Wie funktioniert Bitcoin?

**Status:** established
**Themen:** grundlagen, protokoll, privacy, mining
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-how-does-bitcoin-work]]

## Summary

Bitcoin ist gleichzeitig ein Computerprogramm und das Netzwerk aller Geräte, die dieses Programm ausführen. Das zentrale Problem, das Bitcoin löst, ist das Double-Spend-Problem: Wie kann man digitale Dateien als Geld verwenden, wenn sie beliebig kopiert werden können? Die Lösung ist ein geteiltes Kassenbuch (Blockchain), das durch Mining gesichert wird — wer eine Transaktion rückgängig machen will, muss mehr Rechenarbeit leisten als das gesamte restliche Netzwerk.

## Body

### Bitcoin als Programm und Netzwerk

Bitcoin ist ein Programm, das jeder herunterladen und auf seinem Computer ausführen kann. Alle Computer, die dieses Programm laufen lassen, bilden das Bitcoin-Netzwerk. Innerhalb dieses Netzwerks können Daten (Bitcoin-Transaktionen) direkt von Person zu Person gesendet werden — ohne Bank oder andere Vermittler.

### Das Double-Spend-Problem

Das fundamentale Problem digitalen Geldes: Digitale Dateien lassen sich kopieren. Wenn ich eine digitale "Münze" versende, behalte ich die Originaldatei trotzdem — ich könnte sie also mehrfach ausgeben.

Die traditionelle Lösung ist eine vertrauenswürdige dritte Partei (eine Bank), die ein Kassenbuch führt. Bitcoin löst dieses Problem ohne Mittelsmann.

### Die Bitcoin-Lösung: Geteiltes Kassenbuch + Mining

Bitcoin gibt jedem im Netzwerk eine Kopie desselben Kassenbuchs (die Blockchain). Jede Transaktion wird ins Netzwerk gesendet, von den Teilnehmern weiterverbreitet, und schliesslich von Minern in Blöcken auf der Blockchain gesichert.

Das verhindert Double-Spending durch Zeitstempel: Wer zuerst sendet, gewinnt. Alle anderen Kopien der "Münze" werden abgelehnt.

### Wie Mining Sicherheit erzeugt

Mining ist der Prozess, durch den Transaktionen dauerhaft auf der Blockchain gesichert werden. Miner bündeln wartende Transaktionen in Blöcken und müssen dabei eine mathematische Aufgabe lösen: Sie müssen einen SHA-256-Hash finden, der kleiner als ein vorgegebener Zielwert ist. Das erfordert massiven Rechenaufwand (Trial and Error mit einer zufälligen Nonce-Zahl).

Der erste Miner, der einen gültigen Hash findet, fügt seinen Block der Blockchain hinzu und erhält dafür neue Bitcoin (Block Reward).

**Warum das sicher ist:** Wer eine frühere Transaktion rückgängig machen will, müsste alle Blöcke seit dieser Transaktion neu berechnen — und gleichzeitig schneller als das restliche Netzwerk sein. Das ist praktisch unmöglich, wenn kein einzelner Angreifer mehr Hashrate hat als alle ehrlichen Miner zusammen (51%-Angriff).

### Longest-Chain-Regel

Wenn zwei Miner gleichzeitig einen gültigen Block finden (temporärer Split), gilt die Regel: Die längste Kette gewinnt. Sobald der nächste Block auf einem der Chains gebaut wird, verliert der andere — alle Netzwerkteilnehmer wechseln zur längsten Kette.

### Transaktionen und UTXOs

Bitcoin-Transaktionen verschieben keine Konten-Salden, sondern verbrauchen und erzeugen "Outputs" (Geldscheine in fixen Beträgen). Eine Transaktion nimmt vorhandene Outputs als Inputs, und erzeugt neue Outputs — einen für den Empfänger, einen als Wechselgeld zurück an den Sender.

Die Summe aller unverbrauchten Outputs (UTXOs) ergibt den Kontostand einer Adresse.

### Kryptografische Sicherheit

Jede Adresse hat einen zugehörigen privaten Schlüssel. Nur wer diesen privaten Schlüssel kennt, kann eine Transaktion erstellen, die Coins von dieser Adresse bewegt. Das wird durch digitale Signaturen nachgewiesen — mathematisch sicher, ohne den privaten Schlüssel zu enthüllen.

## Related

- [[bitcoin-netzwerk-und-nodes]]
- [[bitcoin-blockchain-struktur]]
- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-transaktionsstruktur]]
- [[utxo-modell-und-konsolidierung]]
- [[kryptografische-schlussel-und-adressen]]
- [[bitcoin-whitepaper]]

## Open Questions

- Wie erklärt man Bitcoin am besten jemandem ohne technischen Hintergrund?
