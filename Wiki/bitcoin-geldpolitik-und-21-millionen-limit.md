# Bitcoin Geldpolitik und das 21-Millionen-Limit

**Status:** established
**Themen:** grundlagen, protokoll, oekonomie
**Last updated:** 2026-07-05
**Sources:** [[20260424_wie-das-21-millionen-limit-von-bitcoin-tatsächlich-durchgesetzt-wird]], [[20220620_warum-ist-bitcoin-wichtig-de]], [[Die andere Seite der Medaille.md]], [[Bitcoin ist die Wiederentdeckung des Geldes.md]], [[aprycot-rochard-perfekte-geldpolitik-bitcoin]], [[waltz-bitcoin-facts]], [[20260308_heartmoney-nur-noch-1-million-bitcoin]]

## Summary

Das Bitcoin-Angebot ist auf knapp 21 Millionen Coins begrenzt — nicht durch eine externe Instanz, sondern durch Konsensregeln, die jede Node unabhängig durchsetzt. Neue Bitcoin entstehen ausschliesslich durch die Block Subsidy, die sich alle 210.000 Blöcke halbiert (Halving). Das 21-Millionen-Limit ergibt sich mathematisch aus der geometrischen Summe dieser Halbierungen und wird nie exakt erreicht — nur annäherungsweise.

## Body

### Wie neue Bitcoin entstehen

Neue Bitcoin werden ausschliesslich dann erzeugt, wenn ein Miner einen gültigen Block findet. Jeder neue Block enthält eine feste Belohnung (Block Subsidy) nach folgendem Zeitplan:

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
- `if (halvings >= 64) return 0` verhindert einen Memory-Overflow-Bug, der nach 64 Halvings die Ausgabe auf 0 zurücksetzen würde und die Geldmenge sonst erneut hochlaufen liesse

In `src/consensus/amount.h` gibt es zusätzlich `MAX_MONEY` als Sicherheitsschranke — kein Single-Point-of-Truth für das Limit, sondern ein Schutz gegen Bugs wie den Value Overflow Bug von 2010, bei dem jemand 184 Milliarden Bitcoin erzeugte.

### Dezentrale Durchsetzung

Das Limit wird nicht von einer zentralen Instanz kontrolliert, sondern durch **gegenseitige Verifikation** aller Nodes. Wenn ein Miner versucht, mehr Bitcoin auszuschütten als erlaubt, lehnen alle Nodes den Block sofort als ungültig ab. Da kein einziger Administrator existiert, der diese Regel ausser Kraft setzen könnte, ist die Geldpolitik durch Konsens gesichert.

Jeder kann die Implementierung selbst prüfen: Bitcoin Core ist Open-Source, die Formel ist nachvollziehbar, und wer eine Node betreibt, verifiziert die Ausgabe neuer Coins in Echtzeit.

### Könnten sich die Regeln ändern?

Technisch kann jeder den Code verändern. Praktisch wäre eine Inflations-Änderung nur durchsetzbar, wenn die überwältigende Mehrheit der Nutzer, Nodes und Miner die neue Version freiwillig übernimmt. Da das 21-Millionen-Limit zum Kernversprechen von Bitcoin gehört, würde eine inflationäre Gabel höchstwahrscheinlich zu einem Fork führen, bei dem der originale Bitcoin im Wettbewerb gewinnt.

### Warum das Limit politisch relevant ist: Der Cantillon-Effekt

Das 21-Millionen-Limit ist eine technische Konstante mit politischer Absicht: eine Reaktion auf ein strukturelles Problem staatlicher Geldpolitik.

Traditionelle Zentralbanken können Geld drucken. Die Bilanz der Europäischen Zentralbank wuchs von einer Billion Euro im Jahr 2000 auf fast neun Billionen bis 2022. 80% aller je existierenden US-Dollars wurden zwischen 2020 und 2022 gedruckt. Geldmengenwachstum entwerte bestehende Ersparnisse — wer Geld hält, verliert Kaufkraft.

Dazu kommt der **Cantillon-Effekt**: Neu gedrucktes Geld kommt zuerst bei bestimmten Akteuren an — Banken, staatlichen Auftragnehmern, Finanzinstitutionen. Diese können es ausgeben, bevor die Inflation die Preise angehoben hat. Spätere Empfänger (Lohnempfänger, Sparer) erhalten das Geld erst, wenn es real weniger wert ist. Das Gelddrucken ist also keine neutrale Operation, sondern eine Vermögensumverteilung.

Satoshi Nakamoto kodierte das Limit — und damit die Lösung — direkt in den Genesis-Block: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks." Bitcoin sollte nicht stabilen Wert, sondern stabile Menge haben.

Das 21-Millionen-Limit macht Bitcoin auch zensurresistent: Wer eigene Keys hält und Bitcoin direkt sendet, braucht keine Bank als Mittler. Das Netz hat keinen Schalter, den eine Behörde umlegen könnte — anders als Bankkonten, die eingefroren werden können.

### Satoshi über Knappheit und Deflation

Nakamoto stellte das feste Angebot ausdrücklich gegen das Gelddrucken. Verlorene Coins behandelte er als Umverteilung zugunsten aller anderen Halter:

> Those coins can never be recovered, and the total circulation is less. Since the effective circulation is reduced, all the remaining coins are worth slightly more. It's the opposite of when a government prints money and the value of existing money goes down.

([BitcoinTalk, 10.12.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/17/); Sammlung: [[the-quotable-satoshi]])

Kürzer, ein halbes Jahr später: «Lost coins only make everyone else's coins worth slightly more. Think of it as a donation to everyone.» ([21.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/131/))

Das Angebotsmodell verglich er mit einem Edelmetall, dessen Menge feststeht und dessen Wert sich bewegt:

> Instead of the supply changing to keep the value the same, the supply is predetermined and the value changes. As the number of users grows, the value per coin increases. It has the potential for a positive feedback loop.

([P2P Foundation, 18.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/3/))

Zur Teilbarkeit bei künftiger Deflation verwies er auf die acht internen Nachkommastellen: 21 Millionen Coins bei damals 6,8 Milliarden Menschen, intern aber `1.00000000` statt `1.00`, mit der Option, mehr Stellen anzuzeigen, «if there's massive deflation in the future». ([06.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/46/)) Ganze Sammlung in [[satoshi-zitate]].

### „21 Millionen: nie mehr" — Node als Verifikationsinstanz

Gigi präzisiert: Das 21-Millionen-Limit gilt nur dann für einen Nutzer, wenn er einen eigenen Full Node betreibt. Ein Full Node ist die rechnerische Seite der Medaille — er prüft nicht nur Transaktionen, sondern auch, ob die Geldmenge den Konsensregeln entspricht. Wer keinen eigenen Node betreibt, verlässt sich auf die Ehrlichkeit eines fremden Nodes für die wichtigste Eigenschaft von Bitcoin.

„21 Millionen: nie mehr" ist deshalb keine blosse Aussage über Bitcoins Design — es ist eine Aussage, die jeder Node-Betreiber individuell verifiziert. Das macht das Limit systemisch robust: Kein Miner und keine Firma kann es ändern, solange genug Nodes es ablehnen. [[Die andere Seite der Medaille.md]]

Gigi: „Die Geldpolitik von Bitcoin ist zeitlich festgelegt, nicht per Dekret. Sie kann nicht geändert werden. Mit ihr kann nicht gestritten werden. Sie ist unabhängig von der Nachfrage, unabhängig vom Energieverbrauch und unabhängig von der Politik." [[Bitcoin ist die Wiederentdeckung des Geldes.md]]

### Asymptotische Geldmengenvorgabe: Rochards Rahmen (2013)

Pierre Rochard beschreibt Bitcoins Geldpolitik mit dem Begriff AMST — Asymptotic Money Supply Targeting (deutsch: asymptotische Geldmengenvorgabe, AGMV). Die Bezeichnung ist präziser als „21 Millionen Limit": Das Angebot wächst asymptotisch gegen einen Maximalwert, erreicht ihn aber nie exakt. Diese Geldpolitik ist bei der Gründung festgelegt worden und wird durch die dezentrale Natur des Netzwerks unabhängig von jedem Emittenten gehalten. [[aprycot-rochard-perfekte-geldpolitik-bitcoin]]

Rochard formuliert das Bild einer „Bitcoin-Zentralbank" (BZB) — eine Analogie mit Absicht. Die BZB gibt Bitcoin an Miner aus (die Berechnungen als Proof-of-Work leisten), und diese Seigniorage fliesst nicht an den Emittenten, sondern subventioniert das Zahlungssystem selbst. Damit unterscheidet sich die Struktur fundamental von einer klassischen Zentralbank, bei der Seigniorage dem Herausgeber zugutekommt: Hier zahlt das Netzwerk diejenigen, die es absichern.

AMST und PoW-Seigniorage kombiniert erzeugen laut Rochard drei strukturelle Eigenschaften:

Erstens: Rationale Marktteilnehmer halten Bitcoin, auch wenn sie keine in Bitcoin denominierten Schulden haben. Der Wettbewerbsvorteil des Bitcoin-Zahlungssystems gegenüber Alternativen rechtfertigt das Halten allein schon aus Liquiditätserwägungen.

Zweitens: Wechselkurse und Zinssätze werden ausschliesslich durch den Markt gesetzt. Die BZB interveniert nicht, um Adoptionswellen oder Hype-Zyklen zu glätten — wäre das der Fall, würde sie das Vertrauen verlieren, das AMST langfristigen Haltern gibt.

Drittens: Mindestreservesysteme können sich nicht entwickeln. Bitcoin erzwingt strukturell Vollreserve: Es ist nicht möglich, mehr Bitcoin auszugeben als vorhanden, weil jede Node jede Transaktion verifiziert. Das entspricht dem österreichischen 100%-Reserve-Goldstandard oder dem Chicago Plan. In einem Vollreservesystem führt erhöhte Geldhaltung nicht zu Liquiditätsfallen, sondern zu steigenden Realzinsen und sinkenden Konsumentenpreisen — ein sich selbst stabilisierender Kreislauf, weil höhere Zinsen Hortende zu Investitionen anreizen und günstigere Preise den Konsum stützen.

Rochard schliesst mit einer Langzeitprognose: „Die Bitcoin-Zentralbank wird dank ihrer antifragilen Geldpolitik die langfristigste Institution ihrer Art werden." [[aprycot-rochard-perfekte-geldpolitik-bitcoin]]

### Die 21 Millionen: ein educated guess — und ein Codebug

Satoshi hat das 21-Millionen-Limit nicht aus einer ökonomischen Theorie abgeleitet, sondern nach eigenen Worten „geraten" — ein *educated guess*. In einer E-Mail an Martti Malmi erklärte er, er wollte eine Zahl wählen, die sowohl für ein Nischen-Experiment als auch für ein globales Währungssystem skalieren würde. Die genaue Zahl war sekundär; die Unveränderlichkeit des Ausgabeplans war der eigentliche Punkt. [[waltz-fact-05-21m-limit-educated-guess]]

Paradoxerweise existierte das harte 21-Millionen-Limit im Code zunächst gar nicht. Aufgrund einer C++-Eigenheit hätte der Halving-Algorithmus nach dem letzten Halving (~Jahr 2214) von vorne begonnen — die Subventionen wären wieder gestiegen. BIP42 (2014) schloss diese Lücke explizit, indem es die Ausgabe nach 64 Halvings auf null setzt (`if (halvings >= 64) return 0`). Technisch gesehen wurde das 21-Millionen-Limit erst 2014 im Code verankert. [[waltz-fact-12-bitcoin-21m-cap-bip42]]

### Meilenstein: der 20-millionste Bitcoin (März 2026)

Am 9. März 2026 wurde mit Block 940.000 rechnerisch der 20-millionste Bitcoin geschürft. Seither verbleiben weniger als eine Million Coins — unter fünf Prozent der Gesamtmenge — für die Zeit bis etwa 2140. Der Ausgabeplan ist damit zu über 95 Prozent abgearbeitet, obwohl das Netzwerk erst 17 Jahre alt war.

Eine Feinheit am Rande: Streng genommen waren zu diesem Zeitpunkt keine vollen 20 Millionen im Umlauf, weil einzelne Miner in der Vergangenheit ihre Blockbelohnung nicht vollständig beansprucht haben (ob Softwarefehler, Absicht oder Experiment, ist ungeklärt). Diese liegengelassenen Beträge entstehen nie nachträglich — die Subsidy eines Blocks ist eine einmalige Ausgabeerlaubnis, kein Guthaben. Die tatsächliche Endmenge liegt dadurch geringfügig unter dem theoretischen Maximum; an der Obergrenze ändert das nichts. [[20260308_heartmoney-nur-noch-1-million-bitcoin]]

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[satoshi-zitate]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[selbstverwahrung-und-boersenrisiken]]

- [[der-bitcoin-standard|Der Bitcoin-Standard (Saifedean Ammous)]] ← Buch
- [[bitcoin-treasury-companies]]

## Open Questions

- Wie entwickeln sich die Miner-Anreize, wenn die Block Subsidy gegen Null geht und nur noch Transaktionsgebühren verbleiben?
- Wird die Halving-Formel jemals politisch angefochten werden?
