# Bitcoin-Maximalisten: Profil aus US-Repräsentativdaten

**Status:** emerging
**Themen:** studien, adoption, oekonomie
**Last updated:** 2026-09-03
**Sources:** [[ssrn-7368018.pdf]]

## Summary

Das SSRN-Working-Paper «All in on Bitcoin: Are maximalists really different?» (Tercero-Lucas, Trabelsi Karoui, Vaquero-Lafuente; Comillas Pontifical University, 2026) ist die erste Profilstudie zu Bitcoin-only-Haltern auf repräsentativer Basis. Sie nutzt den Survey and Diary of Consumer Payment Choice der Fed Atlanta (2021 bis 2024) und vergleicht Personen, die ausschliesslich Bitcoin halten, mit allen anderen Krypto-Haltern. Ergebnis: Bitcoin-only-Halter sind älter, häufiger männlich und haben ein tieferes Haushaltseinkommen. Der stärkste Unterschied ist aber das Verhalten. Wer Krypto primär als Investment sieht oder im letzten Jahr verkauft hat, ist deutlich seltener Maximalist. Die Autoren lesen das als Beleg für ein Halter-Profil mit langem Horizont, warnen aber selbst davor, aus Portfoliozusammensetzung auf Ideologie zu schliessen.

## Body

### Was gemessen wird

Die Studie trennt zwei Bedeutungen von «Maximalismus». Verhaltens-Maximalismus ist das ausschliessliche Halten von Bitcoin, ein in Finanzdaten beobachtbarer Zustand. Ideologischer Maximalismus ist ein Wertesystem (Dezentralisierung, Zensurresistenz, monetäre Souveränität). Der Datensatz erlaubt nur die erste Messung. «Maximalist» heisst im Paper deshalb: hält nur Bitcoin. Wer 99 Prozent Bitcoin und einen Rest Altcoins hält, zählt nicht dazu. Die Autoren nennen das bewusst streng und lesen ihre Ergebnisse als Aussagen über Bitcoin-only-Investoren, mit nur vorsichtigen Rückschlüssen auf die Ideologie.

Stablecoins kann der Datensatz nicht von anderen Kryptowährungen unterscheiden. Auch Zeitpunkt des Markteintritts und Haltedauer sind nicht erfasst; als Proxy dient die Frage, ob in den letzten zwölf Monaten Krypto verkauft wurde.

### Daten und Methode

Grundlage ist der SDCPC der Federal Reserve Bank of Atlanta, eine repräsentative Panel-Erhebung zu Zahlungsverhalten in den USA. Die Wellen 2021 bis 2024 liefern 1'481 Beobachtungen von Krypto-Haltern (359, 382, 331 und 409 pro Jahr; Person-Jahre, keine eindeutigen Personen). Frühere Jahre hatten zu wenige Krypto-Halter, 2020 wurde wegen COVID ausgeschlossen.

Die Zusammensetzung verschiebt sich über die vier Jahre. Der Anteil der Bitcoin-only-Halter steigt von 18,1 Prozent (2021) auf 28,4 Prozent (2024). Altcoin-only-Halter fallen von 39,0 auf 30,8 Prozent. Die Gruppe, die Bitcoin zusammen mit anderen Coins hält, bleibt mit rund 40 Prozent die grösste.

Geschätzt werden gepoolte logistische Regressionen mit Jahres-Fixed-Effects und auf Personenebene geclusterten Standardfehlern. Berichtet werden durchschnittliche Marginaleffekte, also die Veränderung der Wahrscheinlichkeit, Bitcoin-only zu sein, pro Einheit der erklärenden Variable. Die Pseudo-R²-Werte liegen zwischen 0,04 und 0,08. Die Modelle erklären also nur einen kleinen Teil der Varianz, was die Autoren für Verhaltensmodelle auf Umfragedaten als normal bezeichnen. Alle Ergebnisse sind Assoziationen, keine Kausalaussagen.

### Ergebnisse: Wer hält nur Bitcoin

Die Effekte aus der Basisspezifikation (Tabelle 3 des Papers), jeweils bei Kontrolle der übrigen Variablen:

| Merkmal | Effekt auf Wahrscheinlichkeit «Bitcoin-only» |
|---|---|
| Alter | +0,3 bis +0,4 Prozentpunkte pro Lebensjahr (30 → 60 Jahre: +9 bis +12 PP) |
| Geschlecht | Männer +9 bis +10 PP gegenüber Frauen |
| Haushaltseinkommen | −1 PP pro Einkommenskategorie; 25. → 75. Perzentil (ca. 30'000 → 100'000 USD): −8 PP |
| Erwerbstätig | −5 bis −8 PP (nicht in allen Spezifikationen signifikant) |
| Investment als Hauptmotiv | −11 PP |
| Krypto in den letzten 12 Monaten verkauft | −14 bis −16 PP |
| Bildung, Krypto-Zahlungen, Mobile Payment | kein signifikanter Effekt |

Die Autoren deuten den Alterseffekt über den Zeitpunkt des Markteintritts: Wer früher kam, kam in eine Welt, in der Bitcoin die einzige oder dominante Option war, und blieb dabei. Sie nennen Status-quo-Bias und Endowment-Effekt als verhaltensökonomische Erklärungen. Der Geschlechtereffekt passt zur breiteren Literatur über Männer und riskante oder neue Finanzprodukte. Beim Einkommen greift die Standardlogik der Diversifikation: Wer mehr hat, streut mehr, auch innerhalb von Krypto.

Das Investment- und Verkaufsergebnis ist für die Autoren der Kern. Es widerspricht der Annahme, Krypto-Beteiligung sei generell spekulationsgetrieben. Für den Gesamtmarkt mag das gelten, für Bitcoin-only-Halter passt es nicht.

### Vertiefungen

**Generationen.** Ein quadratischer Altersterm zeigt keine Nichtlinearität. Nach Kohorten aufgeteilt sind Millennials (Jahrgänge 1981 bis 1996) um 12 bis 15 Prozentpunkte und Generation X (1965 bis 1980) um 9 bis 11 Prozentpunkte seltener Bitcoin-only als die vor 1965 Geborenen. Generation Z unterscheidet sich nicht signifikant von den Ältesten. Die Autoren vermuten, dass junge Neueinsteiger mit Bitcoin als sichtbarstem Coin beginnen, bevor sie sich breiter umsehen, und markieren das ausdrücklich als Spekulation.

**Bildung.** Weder die 16-stufige noch eine fünfstufige Bildungsskala hat einen Effekt. Mit Dummies gegenüber der Referenz «kein High-School-Abschluss» zeigen «Some College» und Bachelor schwache negative Koeffizienten.

**Interaktionen.** Der Alterseffekt existiert nur bei Männern (rund 0,3 Prozentpunkte pro Jahr, ein 50-jähriger Mann gegenüber einem 30-jährigen rund 6 PP). Bei Frauen ist er nicht signifikant. Der negative Effekt des Investmentmotivs ist bei tiefem Einkommen am stärksten (−15,8 PP), in der Mitte −12,0 PP, oben −8,5 PP. Ob jemand verkauft hat oder nicht, ändert am Investmentmotiv-Effekt nichts (−11,7 gegenüber −10,8 PP).

**Selbsteingeschätzte Krypto-Kenntnis.** Nur für 2023 und 2024 erhoben (740 Beobachtungen). Entgegen der Erwartung der Autoren unterscheiden sich Maximalisten hier nicht vom Rest.

### Robustheit und die Ethereum-Kontrolle

Die Ergebnisse halten bei Bootstrap-Standardfehlern (1'000 Replikationen), bei Probit- und linearen Wahrscheinlichkeitsmodellen und im Vergleich von Bitcoin-only mit Personen ganz ohne Bitcoin. Jahresweise Regressionen zeigen zwei Nuancen: Einkommen wird erst in den späteren Jahren relevant, und der Verkaufseffekt ist 2023, im «Krypto-Winter», nicht signifikant.

Aufschlussreich ist der Vergleich mit Ethereum-only-Haltern (461 Beobachtungen). Dort bleibt nur das Geschlecht als Unterschied (Männer +9 PP). Alter, Einkommen, Motive und Verkaufsverhalten trennen die beiden Puristengruppen nicht. Die Autoren schliessen daraus, dass Single-Asset-Konzentration allein kein scharf abweichendes Profil erzeugt und dass die Unterschiede zwischen den Puristengruppen eher in Zugehörigkeit und Überzeugung liegen als in Demografie oder Finanzverhalten. Das begrenzt, wie sie selbst schreiben, zu starke Thesen über Bitcoin-Exzeptionalismus.

### Einordnung im Korpus

Für Bitcoin-Kreise ist das Paper eher Bestätigung mit Datenunterlegung: Das HODL-Verhalten, das [[bitcoin-vs-krypto]] und [[bitcoin-fehlannahmen]] als Haltung beschreiben, erscheint hier als messbare Abweichung vom übrigen Krypto-Markt. Neu ist die Einkommensrichtung: Innerhalb der Krypto-Halter sind die Bitcoin-only-Personen die weniger wohlhabenden. Das steht quer zur häufigen Annahme, Bitcoin-Halter seien die finanziell sophistiziertere Gruppe, und lässt sich gleichzeitig mit der Diversifikationslogik erklären.

Der Geschlechtereffekt ergänzt [[frauen-und-bitcoin]] um eine Zahl: Der Männerüberhang besteht auch innerhalb der Krypto-Halter, und die Bindung an Bitcoin mit dem Alter ist ein Männerphänomen. Die qualitativen Käufersegmente in [[bitcoin-adoptionsstudie-2026-dach]] und die Adoptionszahlen in [[bitcoin-adoption-report-river-2026]] liefern den DACH- und den Ownership-Kontext, der in der US-Umfrage fehlt.

Als Grenze bleibt, was das Paper selbst betont: Es misst Portfolios, keine Überzeugungen. Ob jemand aus Prinzip nur Bitcoin hält oder aus Trägheit, Einfachheit oder Unkenntnis anderer Coins, bleibt offen.

## Related

- [[bitcoin-vs-krypto]]
- [[bitcoin-fehlannahmen]]
- [[frauen-und-bitcoin]]
- [[bitcoin-adoptionsstudie-2026-dach]]
- [[bitcoin-adoption-report-river-2026]]
- [[crypto-adaption-europa-bsd-2026]]
- [[bitcoin-akademische-forschung-bbr]]
- [[bitcoin-volatilitaet-und-preisfindung]]

## Open Questions

- Gilt das US-Profil (älter, männlich, tieferes Einkommen) auch in Europa? Die DACH-Studie ist qualitativ, der Crypto Compass krypto-breit; eine repräsentative Bitcoin-only-Auswertung für Europa fehlt.
- Die Autoren fordern Daten, die Portfolios mit direkt gemessenen Überzeugungen verbinden. Gibt es dazu bereits Erhebungen?
- Der steigende Bitcoin-only-Anteil 2021 bis 2024 (18 → 28 Prozent) fällt mit ETF-Zulassung und Altcoin-Bärenmarkt zusammen. Kohorteneffekt oder Marktzyklus?
