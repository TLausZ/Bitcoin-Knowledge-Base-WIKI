# Bitcoin Geldpolitik und das 21-Millionen-Limit

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20260424_wie-das-21-millionen-limit-von-bitcoin-tatsächlich-durchgesetzt-wird]], [[20220620_warum-ist-bitcoin-wichtig-de]]

## Summary

Das Bitcoin-Angebot ist auf knapp 21 Millionen Coins begrenzt — nicht durch eine externe Instanz, sondern durch Konsensregeln, die jede Node unabhängig durchsetzt. Neue Bitcoin entstehen ausschließlich durch die Block Subsidy, die sich alle 210.000 Blöcke halbiert (Halving). Das 21-Millionen-Limit ergibt sich mathematisch aus der geometrischen Summe dieser Halbierungen und wird nie exakt erreicht — nur annäherungsweise.

## Body

### Wie neue Bitcoin entstehen

Neue Bitcoin werden ausschließlich dann erzeugt, wenn ein Miner einen gültigen Block findet. Jeder neue Block enthält eine feste Belohnung (Block Subsidy) nach folgendem Zeitplan:

- 0 Halvings: 50 BTC pro Block → 10.500.000 BTC gesamt
- 1 Halving: 25 BTC → 5.250.000 BTC
- 2 Halvings: 12,5 BTC → 2.625.000 BTC
- 3 Halvings: 6,25 BTC → 1.312.500 BTC
- 4 Halvings: 3,125 BTC → 656.250 BTC *(aktuell)*
- …und so weiter für 32 Halvings insgesamt

Die geometrische Summe dieser Reihe ergibt knapp 21 Millionen. Da die Belohnung asymptotisch gegen Null geht, wird die Zahl 21 Millionen nie exakt erreicht — die letzten Bruchteile entstehen um das Jahr 2140.

### Der Bitcoin Core Code

Die Regel ist direkt im Quellcode von Bitcoin Core verankert. In `src/validation.cpp` berechnet `GetBlockSubsidy()` die aktuelle Blockbelohnung:

```
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
if (halvings >= 64) return 0;
CAmount nSubsidy = 50 * COIN;
nSubsidy >>= halvings;
return nSubsidy;
```

- `nSubsidyHalvingInterval` ist in `chainparams.cpp` auf **210.000 Blöcke** festgelegt
- `nSubsidy >>= halvings` bedeutet binäre Rechtsverschiebung = Halbierung
- `if (halvings >= 64) return 0` verhindert einen Memory-Overflow-Bug, der nach 64 Halvings die Ausgabe auf 0 zurücksetzen würde und die Geldmenge sonst erneut hochlaufen ließe

In `src/consensus/amount.h` gibt es zusätzlich `MAX_MONEY` als Sicherheitsschranke — kein Single-Point-of-Truth für das Limit, sondern ein Schutz gegen Bugs wie den Value Overflow Bug von 2010, bei dem jemand 184 Milliarden Bitcoin erzeugte.

### Dezentrale Durchsetzung

Das Limit wird nicht von einer zentralen Instanz kontrolliert, sondern durch **gegenseitige Verifikation** aller Nodes. Wenn ein Miner versucht, mehr Bitcoin auszuschütten als erlaubt, lehnen alle Nodes den Block sofort als ungültig ab. Da kein einziger Administrator existiert, der diese Regel außer Kraft setzen könnte, ist die Geldpolitik durch Konsens gesichert.

Jeder kann die Implementierung selbst prüfen: Bitcoin Core ist Open-Source, die Formel ist nachvollziehbar, und wer eine Node betreibt, verifiziert die Ausgabe neuer Coins in Echtzeit.

### Könnten sich die Regeln ändern?

Technisch kann jeder den Code verändern. Praktisch wäre eine Inflations-Änderung nur durchsetzbar, wenn die überwältigende Mehrheit der Nutzer, Nodes und Miner die neue Version freiwillig übernimmt. Da das 21-Millionen-Limit zum Kernversprechen von Bitcoin gehört, würde eine inflationäre Gabel höchstwahrscheinlich zu einem Fork führen, bei dem der originale Bitcoin im Wettbewerb gewinnt.

### Warum das Limit politisch relevant ist: Der Cantillon-Effekt

Das 21-Millionen-Limit ist nicht nur eine technische Konstante — es ist eine bewusste Reaktion auf ein strukturelles Problem staatlicher Geldpolitik.

Traditionelle Zentralbanken können Geld drucken. Die Bilanz der Europäischen Zentralbank wuchs von einer Billion Euro im Jahr 2000 auf fast neun Billionen bis 2022. 80% aller je existierenden US-Dollars wurden zwischen 2020 und 2022 gedruckt. Geldmengenwachstum entwerte bestehende Ersparnisse — wer Geld hält, verliert Kaufkraft.

Dazu kommt der **Cantillon-Effekt**: Neu gedrucktes Geld kommt zuerst bei bestimmten Akteuren an — Banken, staatlichen Auftragnehmern, Finanzinstitutionen. Diese können es ausgeben, bevor die Inflation die Preise angehoben hat. Spätere Empfänger (Lohnempfänger, Sparer) erhalten das Geld erst, wenn es real weniger wert ist. Das Gelddrucken ist also keine neutrale Operation, sondern eine Vermögensumverteilung.

Satoshi Nakamoto kodierte das Limit — und damit die Lösung — direkt in den Genesis-Block: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks." Bitcoin sollte nicht stabilen Wert, sondern stabile Menge haben.

Das 21-Millionen-Limit macht Bitcoin auch zensurresistent: Wer eigene Keys hält und Bitcoin direkt sendet, braucht keine Bank als Mittler. Das Netz hat keinen Schalter, den eine Behörde umlegen könnte — anders als Bankkonten, die eingefroren werden können.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[selbstverwahrung-und-boersenrisiken]]

## Open Questions

- Wie entwickeln sich die Miner-Anreize, wenn die Block Subsidy gegen Null geht und nur noch Transaktionsgebühren verbleiben?
- Wird die Halving-Formel jemals politisch angefochten werden?
