# Soft Fork und Hard Fork

**Status:** established
**Last updated:** 2026-06-04
**Sources:** [[20241114_soft-fork-oder-hard-fork-was-ist-der-unterschied]]

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

**Beispiele:** Bitcoin Cash (2017, permanenter Chainsplit → eigenes Netzwerk)

### Was Soft Forks nicht automatisch bedeuten

Soft Forks sind nicht automatisch sicherer oder harmloser. Ein Soft Fork kann theoretisch jede Änderung implementieren — SegWit hat die effektive Blockgröße durch cleveres Redesign erhöht, ohne das eigentliche Limit zu ändern. Debatten über Bitcoin-Upgrades sollten sich auf die tatsächliche Änderung und ihre Auswirkungen konzentrieren, nicht auf die Fork-Bezeichnung.

### Zufällige Chainsplits

Chainsplits passieren alle paar Wochen natürlich, wenn zwei Miner gleichzeitig einen gültigen Block auf derselben Höhe finden. Das Netzwerk löst das automatisch auf: Die längere Chain gewinnt. Kein böswilliger Hintergrund — Teil der normalen Spieltheorie des Minings.

## Related

- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]

## Open Questions

- Welche Covenant-Proposals (CTV, etc.) werden in zukünftigen Soft Forks aktiviert?
- Wie entwickelt sich der Prozess der Konsensfindung bei künftigen Upgrades?
