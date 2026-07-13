# Soft Fork und Hard Fork

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-20
**Sources:** [[20241114_soft-fork-oder-hard-fork-was-ist-der-unterschied]], [[blocksizewar]], [[2018_Grokking-Bitcoin_Rosenbaum]]

## Summary

Änderungen an den Konsensregeln von Bitcoin lassen sich in zwei Typen einteilen: Hard Forks entfernen bestehende Regeln, sodass zuvor ungültige Blöcke gültig werden. Soft Forks fügen Regeln hinzu, sodass zuvor gültige Blöcke ungültig werden. Hard Forks brechen die Vorwärtskompatibilität; Soft Forks behalten sie. Weder Typ ist automatisch sicherer als der andere — entscheidend ist die konkrete Änderung, nicht die Bezeichnung.

## Body

### Konsensregeln als Grundlage

Bitcoin besteht aus Regeln, von denen einige bestimmen, ob ein Block gültig ist. Diese Konsensregeln bilden die Grundlage des Netzwerk-Konsenses. Alle Teilnehmer müssen dieselben Regeln anwenden, damit sie sich auf dieselbe Blockchain einigen können.

### Soft Fork: Regeln hinzufügen

Eine Soft Fork macht die Regeln strenger — der Satz gültiger Blöcke wird kleiner. Zuvor gültige Blöcke werden durch die neue Regel ungültig.

**Analogie:** Ein vegetarisches Restaurant stellt auf vegane Küche um. Jeder, der vorher dort gegessen hat, kann auch vegan essen (vorwärts kompatibel). Aber ein Veganer hätte früher nicht im vegetarischen Restaurant essen können (nicht rückwärts kompatibel).

**Vorwärtskompatibilität:** Nodes mit der alten Version akzeptieren Blöcke, die von der neuen Version erstellt wurden — weil die neuen Blöcke unter den strengeren Regeln auch unter den alten Regeln gültig sind.

**Chainsplit-Risiko:** Trotzdem möglich. Ohne eine Mehrheit der Rechenleistung auf der neuen Version können Nodes der alten Version größere Blöcke ablehnen, was zu einem Chainsplit führt.

**Beispiele:** SegWit (2017), Taproot (2021)

### Hard Fork: Regeln entfernen

Eine Hard Fork lockert die Regeln — der Satz gültiger Blöcke wird größer. Zuvor ungültige Blöcke werden durch die geänderte Regel gültig.

**Analogie:** Das vegetarische Restaurant erlaubt plötzlich Fleisch. Vegetarier haben einen Konflikt mit dem neuen Menü (nicht vorwärts kompatibel).

**Keine Vorwärtskompatibilität:** Nodes der alten Version lehnen neue (z.B. größere) Blöcke ab. Nodes der neuen Version akzeptieren alte Blöcke weiterhin.

**Chainsplit-Risiko:** Hoch, wenn ein Teil der Community die neue Version ablehnt. Das führt zu zwei parallelen Blockchains — mit unterschiedlichen Coins.

**Beispiele:** Bitcoin Cash (2017, permanenter Chainsplit → eigenes Netzwerk). Der Blocksize-Krieg zeigt, warum Hard Forks in Bitcoin so schwer durchzusetzen sind: Bitcoin Unlimited, Bitcoin Classic und BTC1/SegWit2x scheiterten alle, weil Exchanges und Nutzer die neue Chain ablehnten und als Altcoin behandelten — unabhängig von der Mining-Hashrate.

### Was Soft Forks nicht automatisch bedeuten

Soft Forks sind nicht automatisch sicherer oder harmloser. Ein Soft Fork kann theoretisch jede Änderung implementieren — SegWit hat die effektive Blockgröße durch cleveres Redesign erhöht, ohne das eigentliche Limit zu ändern. Debatten über Bitcoin-Upgrades sollten sich auf die tatsächliche Änderung und ihre Auswirkungen konzentrieren, nicht auf die Fork-Bezeichnung.

### Deployment-Mechanismen: MASF vs. UASF

Es gibt zwei Wege, einen Soft Fork zu aktivieren (Rosenbaum, Kap. 11):

**MASF — Miner-Activated Soft Fork:** Miner signalisieren Bereitschaft durch Setzen eines Bits im Block-Versionfeld. Sobald eine ausreichende Schwelle (z.B. 95% der Blöcke in einem 2016-Block-Fenster) erreicht ist, wird der Soft Fork aktiviert. BIP9 codifiziert diesen Mechanismus. Vorteil: Keine plötzliche Chain-Trennung. Nachteil: Einzelne große Miner können ein Upgrade blockieren ("Veto"), selbst wenn die wirtschaftliche Mehrheit der Nutzer es will.

**UASF — User-Activated Soft Fork:** Nodes (nicht Miner) setzen einen fixen Aktivierungs-Zeitpunkt. Ab diesem Datum lehnen sie Blöcke ab, die die neue Regel nicht befolgen — unabhängig vom Miner-Signaling. Miner werden dadurch gezwungen, die neuen Regeln einzuhalten, wenn sie ihre Blöcke nicht verlieren wollen. BIP148 war der bekannteste UASF, der SegWit 2017 letztlich erzwang.

Kernkonzept: **Die wirtschaftliche Mehrheit bestimmt die Regeln.** Exchanges, Wallet-Anbieter und Nutzer — die zusammen den ökonomischen Wert von Bitcoin ausmachen — entscheiden durch die Wahl ihrer Software letztlich, welche Chain "Bitcoin" ist. Miner können Blöcke produzieren, aber wenn Exchanges und Nutzer diese Blöcke nicht akzeptieren, sind die Coins wertlos. Der Blocksize-Krieg ist das praktische Beweis: Die Miner-Mehrheit signalisierte SegWit2x, die Nutzer lehnten ab — SegWit2x scheiterte. [[2018_Grokking-Bitcoin_Rosenbaum]]

### Wipeout- und Replay-Schutz bei Hard Forks

Bei einem Hard Fork entstehen zwei parallele Chains. Zwei technische Schutzmaßnahmen sind nötig:

**Wipeout Protection:** Verhindert, dass Nodes der einen Chain durch die andere Chain "überschrieben" werden. Ohne Schutz könnte die längere Alt-Chain-Kette eine kürzere New-Chain-Kette reorganisieren und Transaktionen rückgängig machen. Wipeout Protection sorgt dafür, dass Blöcke der neuen Chain von alten Nodes als ungültig erkannt werden — keine Reorganisation über die Chainspaltung hinweg möglich.

**Replay Protection:** Ohne Schutz würde eine gültige Transaktion auf Chain A auch auf Chain B gültig sein — denn die Signatur deckt nicht ab, für welche Chain sie bestimmt ist. Ein Angreifer (oder auch ein unwissender Nutzer) könnte Transaktionen von Chain A auf Chain B "abspielen". Replay Protection macht Transaktionen chainspezifisch durch Einführung eines Chain-ID-Feldes (z.B. via SIGHASH-Modifikation). Bitcoin Cash implementierte Replay Protection sofort beim Fork; SegWit2x hätte sie nicht gehabt — ein weiterer Kritikpunkt. [[2018_Grokking-Bitcoin_Rosenbaum]]

### Zufällige Chainsplits

Chainsplits passieren alle paar Wochen natürlich, wenn zwei Miner gleichzeitig einen gültigen Block auf derselben Höhe finden. Das Netzwerk löst das automatisch auf: Die längere Chain gewinnt. Kein böswilliger Hintergrund — Teil der normalen Spieltheorie des Minings.

## Related

- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[blocksize-war]]

## Open Questions

- Welche Covenant-Proposals (CTV, etc.) werden in zukünftigen Soft Forks aktiviert?
- Wie entwickelt sich der Prozess der Konsensfindung bei künftigen Upgrades?
