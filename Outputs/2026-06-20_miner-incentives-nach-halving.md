# Miner-Incentives nach dem Halving: Reichen Gebühren allein für Netzwerksicherheit?

**Datum:** 2026-06-20
**Quelle:** Nutzer-Synthese (kein RAW-Dokument; Wissen aus Budish 2018 und Carlsten et al. 2016)
**Status:** offene Frage — Synthese Stand 2026

---

## Frage

Wie wird die Netzwerksicherheit gewährleistet, wenn die Block Subsidy gegen Null geht und nur noch Transaktionsgebühren bleiben?

---

## Antwort

Es gibt keine Garantie. Bitcoin verlässt sich darauf, dass Transaktionsgebühren rechtzeitig gross genug werden, um die wegfallende Subsidy zu ersetzen — ob das zuverlässig passiert, ist unter Ökonomen umstritten.

### Grundmechanik

Netzwerksicherheit kostet Geld. Ein Angreifer müsste mehr Hashrate aufbauen als das ehrliche Netzwerk; Hashrate folgt dem Mining-Ertrag. Entscheidend ist nicht der nominale BTC-Betrag, sondern seine Kaufkraft. Solange das Sicherheitsbudget (Subsidy + Gebühren) in Fiat gemessen hoch bleibt, bleiben Angriffskosten hoch.

Die Subsidy fällt sehr langsam. Aktuell 3,125 BTC pro Block, gegen null erst um ~2140. Es gibt Jahrzehnte Zeit, in denen sich ein Gebührenmarkt entwickeln kann.

### Optimistische Sicht: knapper Blockplatz

Blockplatz ist begrenzt. Wächst die Nutzung, entsteht ein Bietwettbewerb, und die Gebührensumme pro Block steigt entsprechend. Second-Layer-Protokolle wie Lightning bündeln viele Zahlungen in wenige On-Chain-Transaktionen — der Wert pro Blockplatz steigt tendenziell, weil nur settlement-kritische Transaktionen on-chain landen.

### Kritische Sicht: zwei ernste Argumente

**1. Budget-Argument (Budish):** Gebühren könnten in der Summe schlicht zu klein bleiben, um ein angemessenes Sicherheitsniveau zu finanzieren. Niemand hat einen direkten Anreiz, freiwillig hohe Gebühren zu zahlen — das Sicherheitsbudget ist ein Public Good mit klassischem Trittbrettfahrer-Problem.

**2. Stabilitätsargument (Carlsten et al., «On the Instability of Bitcoin Without the Block Reward»):** Ohne gleichmässige Subsidy kommen Erträge stossweise — je nachdem, wie viele Gebühren im Mempool warten. Das macht Strategien wie Undercutting (Miner bauen auf einem Block mit weniger Gebühren auf, um die Gebühren im vorherigen Block zu «stehlen») und Selfish Mining attraktiver. Die Anreize, ehrlich auf der längsten Kette aufzubauen, könnten gestört werden.

### Ausblick

Wie das ausgeht, ist unbekannt. Es hängt davon ab, ob Bitcoin genug Zahlungsnachfrage anzieht, bevor die Subsidy zu klein wird. Als letzter Ausweg wären Protokolländerungen denkbar — etwa eine permanente Mini-Inflation — aber jede davon widerspricht dem 21-Millionen-Versprechen und wäre politisch hochumstritten.

---

## Spannungen

- `bitcoin-mining-und-proof-of-work.md` beschreibt die Grundmechanik (Subsidy + Fees) ohne die ökonomischen Gegenargumente. → Artikel erweitert.
- Keine RAW-Quellen zu Budish oder Carlsten et al. vorhanden. Behauptungen als speculative markiert.

## Nächste Schritte

- Budish (2018): «The Economic Limits of Bitcoin and the Blockchain» als RAW-Quelle beschaffen
- Carlsten et al. (2016): «On the Instability of Bitcoin Without the Block Reward» als RAW-Quelle beschaffen
- Nach Ingest: Artikel-Status von speculative auf emerging heben
