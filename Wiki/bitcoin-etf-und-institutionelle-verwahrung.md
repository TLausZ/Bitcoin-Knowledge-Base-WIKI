# Bitcoin-ETF und institutionelle Verwahrung

**Status:** established
**Themen:** self-custody, oekonomie, adoption
**Last updated:** 2026-07-18
**Sources:** [[aprycot-vertrau-mir-bruder]], [[2024-01-20_Ein Blick in die Glaskugel - Praktische Tipps zum Bitcoin-Kauf]], [[2026_Q2_Bitcoin Finance Report]]

## Summary

Allen Farrington analysiert den BlackRock Bitcoin ETF-Antrag von 2023 als möglicherweise bedeutendstes Ereignis in Bitcoins Geschichte seit dem Blocksize War. Der entscheidende rechtliche Unterschied: Ein Trust (Gesetz von 1933) hat kein Rücknahmerecht; ein ETF (Gesetz von 1940) hat eines. Dieser Unterschied erklärt den GBTC-Diskont. Farrington entwickelt acht Prognosen zu den Folgen des ETF — von Coinbases Monopolstellung bis zum Risiko einer "JPMorgan Cascade". Die eigentliche Herausforderung: Institutionelle Investoren können keine Selbstverwahrung betreiben, und bitcoin-native Custody-Alternativen für institutionelle Skala sind noch unausgereift.

## Body

### Der Unterschied, auf den es ankommt

Das US-amerikanische Wertpapierrecht unterscheidet zwei relevante Strukturen für Bitcoin-Finanzprodukte:

**Trust nach dem Securities Act von 1933 (1933er-Gesetz):** Kein Rücknahmerecht. Anleger können ihre Anteile nicht gegen Bargeld oder den zugrunde liegenden Vermögenswert eintauschen. GBTC ist ein solcher Trust. Das erklärt, warum GBTC jahrelang mit erheblichem Abschlag gegenüber seinem Nettoinventarwert gehandelt wurde: Wer GBTC kaufte, kaufte eine Forderung ohne Einlösungsrecht.

**ETF nach dem Investment Company Act von 1940 (1940er-Gesetz):** Hat autorisierte Teilnehmer (Authorized Participants), die Anteile gegen den Basiswert oder Bargeld eintauschen können. Dieser Mechanismus hält den Kurs nahe am Nettoinventarwert. [[aprycot-vertrau-mir-bruder]]

Der BlackRock-Antrag von 2023 war ein 1940er-ETF. Farrington hält das für die wichtigste Weichenstellung seit dem Blocksize War von 2017.

### Acht Prognosen

Farrington entwickelt acht Erwartungen, die er explizit zur Falsifizierbarkeit offenlegt:

**1. Der ETF wird genehmigt.** BlackRocks Genehmigungsquote war historisch aussergewöhnlich hoch. Faktisch bestätigt: Der Spot-Bitcoin-ETF wurde im Januar 2024 genehmigt.

**2. Coinbase wird einziger Authorized Participant.** Als Verwahrer tätig, mit tiefen Beziehungen zu institutionellen Anlegern. Das verschafft Coinbase eine Monopolstellung bei der Erstellung und Rücknahme von ETF-Anteilen. Jeder institutionelle Zugang zu Bitcoin läuft damit über einen einzigen Kontrollpunkt.

**3. FUD über "markierte Coins" wird entstehen.** Wenn Transaktionen über Coinbase gebündelt werden, können Coins aufgrund ihrer Geschichte bewertet oder diskriminiert werden. Befürworter von "tainted coins" erhalten einen neuen Hebel.

**4. JPMorgan Cascade.** Wenn JPMorgan oder eine vergleichbare Institution beginnt, über ETF-Anteile mehr Bitcoin zu repräsentieren, als physisch vorhanden ist, entsteht Fraktionalreserve auf Bitcoin — ohne das Bitcoin-Protokoll zu ändern. Das ist das klassische Gold-Problem, das zum Fiat-System führte.

**5. Preiskontrolle durch Futures-Märkte.** Wenn die Preisfindung primär über Derivate stattfindet, können grosse Akteure den Spotpreis beeinflussen, ohne physisches Bitcoin zu bewegen.

**6. New York Agreement 2.0.** Der erste NY Agreement (2017) versuchte, Bitcoin über einen Konsens der Unternehmen zu verändern. Ein institutionell gestützter zweiter Versuch hätte mehr Ressourcen — und könnte auf andere Protokolländerungen abzielen (z.B. KYC-Anforderungen in Layer-2, Inflation).

**7. ETF-Schutzmassnahmen gelten nicht.** Wer über einen ETF in Bitcoin investiert, hat die gleichen Gegenparteirisiken wie beim direkten Kauf, aber ohne die Möglichkeit, Bitcoin in einer Krise zu verwenden. Im Black-Swan-Szenario — Bankrott des ETF-Anbieters, staatliche Einfrierung — hält der ETF-Investor wertlose Anteile.

**8. Bitcoin zu Papier-Bitcoin.** Analog zum Goldstandard: Echtes Bitcoin wird in Verwahrung konzentriert; Papierversprechen auf Bitcoin zirkulieren statt der eigentlichen Coins. Der Prozess, den Hoppe für Gold beschreibt, beginnt sich zu wiederholen. [[aprycot-vertrau-mir-bruder]]

### Der GBTC-Diskont in der Praxis (Januar 2024)

Der Marktstart der Spot-ETFs im Januar 2024 bestätigte Farringtons Punkt zur fehlenden Rücknahme empirisch. Pascal Hügli (Less Noise More Signal) dokumentierte, dass aus Grayscales GBTC — dem ehemaligen 1933er-Trust, der mit der Umwandlung in einen ETF erstmals einlösbar wurde — in den ersten fünf Handelstagen über 2,2 Mrd. USD abflossen; JPMorgan rechnete mit bis zu 10 Mrd. USD. Die jahrelang im Trust gefangenen Anleger realisierten ihr «Geld», sobald sie konnten, verstärkt durch GBTCs mit 1,5 % höchste Gebühr. Der Abfluss war zunächst Verkaufsdruck, sollte laut Hügli aber versiegen — danach würden Netto-Zuflüsse in die günstigeren ETFs preisstützend wirken. [[2024-01-20_Ein Blick in die Glaskugel - Praktische Tipps zum Bitcoin-Kauf]]

Aus Anlegersicht ergänzt Hügli eine praktische Warnung: Spot-ETF nicht mit dem seit Oktober 2021 handelbaren Futures-ETF verwechseln. Letzterer muss seine Terminkontrakte monatlich rollen, was bei Contango zu schleichendem Wertverlust («Contango-Bleed») führt; die ISIN identifiziert das gewünschte Produkt eindeutig. → gebündelt in [[bitcoin-marktkommentar-lnms]], vgl. [[bitcoin-kaufen-und-dca]].

### Institutionelle Verwahrung ist strukturell schwierig

Farrington hält fest: Institutionelle Anleger — Pensionsfonds, Versicherungen, Stiftungen — sind rechtlich und praktisch nicht in der Lage, Bitcoin in Selbstverwahrung zu halten. Sie haben treuhänderische Pflichten, benötigen geprüfte Verwahrungsstrukturen und können nicht mit einer 24-Seed-Phrase operieren.

Das ist kein Vorwurf, sondern ein strukturelles Problem. Bitcoin wurde für Individuen entworfen, nicht für Rechtseinheiten mit Audit-Anforderungen. Wenn Bitcoin globale Reservefunktion übernehmen soll, muss es Lösungen geben, die institutionellen Anforderungen genügen, ohne Bitcoins Kerneigenschaften (Selbstverwahrung, Zensurresistenz, finale Abrechnung) aufzugeben.

Farrington nennt vier Ansätze, die diese Lücke angehen könnten:

**Fedi:** Federated eCash-Protokoll, das Gemeinschaftsverwahrung ermöglicht, ohne eine einzige Vertrauensparty zu schaffen.

**OP_VAULT:** Protokollerweiterung, die zeitverzögerte Auszahlungen mit Wiederrufungsoption ermöglicht — relevant für institutionelle Compliance-Anforderungen.

**Unchained Capital:** Kollaborative Multisig-Verwahrung, bei der Unchained einen Key hält, der Kunde zwei — keine vollständige Selbstverwahrung, aber dezentraler als ein einzelner Custodian.

**AnchorWatch:** Versicherung und Überwachung für Multisig-Setups, die institutionelle Anforderungen an Audit-Trails und Versicherungsschutz erfüllt. [[aprycot-vertrau-mir-bruder]]

### Europa: ETPs und die Frage «Wallet oder Depot?» (2026)

Was in den USA der Spot-ETF ist, sind in Europa Bitcoin-ETPs: börsengehandelte Produkte von Anbietern wie 21Shares, Bitwise oder VanEck. Rechtlich sind sie keine Fonds, sondern fast immer besicherte Schuldverschreibungen (ETNs oder ETCs), abgesichert durch physisch hinterlegte Bitcoin. Der Investor hält damit kein natives Bitcoin-Asset, sondern einen wertpapierbasierten Anspruch gegen den Emittenten — auch bei physischer Besicherung. Unterschiede zwischen Produkten bestehen bei Besicherungsstruktur, Verwahrung der hinterlegten Bitcoin, Emittentenrisiken und der rechtlichen Ausgestaltung im Insolvenzfall.

Der Bitcoin Finance Report Q2/2026 stellt die beiden Zugangswege systematisch gegenüber: Direkter Besitz bedeutet Verwahrung in der eigenen Wallet, direkte Verfügungsgewalt, 24/7-Übertragbarkeit und native Nutzung des Netzwerks; das ETP bedeutet Depotverwahrung, Anspruch gegen die Produktstruktur, Abhängigkeit von Börsenhandelszeiten und höhere Intermediationsabhängigkeit. Für CFOs und Treasury-Verantwortliche ist das ETP dennoch oft der gangbare Weg, weil es in bestehende Depot-, Reporting- und Compliance-Prozesse passt, ohne eigene Schlüsselverwaltung, Zugriffstrennungen und Notfallkonzepte aufbauen zu müssen — genau das Farrington-Problem der institutionellen Verwahrung (oben) aus der Praxisperspektive.

Der Report nennt diese Entwicklung Re-Intermediation: Bitcoin wurde als nativ digitales Eigentumsasset ohne zentrale Intermediäre konzipiert; ETPs übertragen es zurück in Emittentenstrukturen, Depotbanken und Verwahrketten. Für Institutionen ist das vermutlich der dominante Adoptionspfad, es trennt aber Bitcoin als monetäres Asset von Bitcoin als Eigentumsmodell. Ein sichtbares Signal der institutionellen Vertiefung im selben Quartal: Morgan Stanley lancierte einen eigenen Spot-Bitcoin-ETF. Nebenbefund zur MiCAR-Abgrenzung: Wer zum ETP berät, bleibt im MiFID-II-Regime; wer zu Bitcoin direkt berät, braucht eine MiCAR-Lizenz ([[bitcoin-beratung-und-micar]]). [[2026_Q2_Bitcoin Finance Report]]

### "Vertraue, aber überprüfe"

Farrington schliesst mit dem Hinweis, dass die eigentliche Frage nicht "Soll man dem ETF vertrauen?" ist, sondern "Wie baut man Systeme, die Vertrauen überprüfbar machen?" Bitcoin selbst ist die Antwort auf diese Frage für Einzelpersonen. Für Institutionen fehlt die Infrastruktur noch. Bis sie existiert, tragen institutionelle ETF-Nutzer Risiken, die Bitcoin-Nutzer mit Selbstverwahrung nicht haben.

Das Goldparadox ist lehrreich: Gold war dezentral, aber seine physischen Eigenschaften erzwangen Verwahrung durch Dritte, was schliesslich zur Zentralbank führte. Bitcoin hat das physische Verwahrungsproblem gelöst. Das soziale und rechtliche Problem — wie Institutionen Bitcoin halten ohne Kontrolle aufzugeben — ist noch offen.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-silent-ipo]]
- [[geld-staat-und-fiat-monopol]]
- [[multisig-und-kollaborative-verwahrung]]
- [[bitcoin-netzwerk-und-nodes]]
- [[regulierung-tofr-aopp]]
- [[eu-regulierung-selbstverwahrung]]
- [[miniscript-und-liana]]
- [[bitcoin-marktkommentar-lnms]]
- [[bitcoin-treasury-companies]]
- [[bitcoin-beratung-und-micar]]

## Open Questions

- Hat sich Prognose 4 (JPMorgan Cascade) nach der ETF-Genehmigung 2024 materialisiert?
- Welche regulatorischen Anforderungen müsste OP_VAULT erfüllen, um als institutioneller Custody-Standard akzeptiert zu werden?
- Gibt es eine kritische ETF-AUM-Grenze, ab der der Einfluss auf die Bitcoin-Preisfindung messbar wird?
