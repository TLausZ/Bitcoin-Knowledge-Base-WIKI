# Bitcoin-ETF und institutionelle Verwahrung

**Status:** established
**Themen:** self-custody, oekonomie, adoption
**Last updated:** 2026-06-22
**Sources:** [[aprycot-vertrau-mir-bruder]]

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

**1. Der ETF wird genehmigt.** BlackRocks Genehmigungsquote war historisch außergewöhnlich hoch. Faktisch bestätigt: Der Spot-Bitcoin-ETF wurde im Januar 2024 genehmigt.

**2. Coinbase wird einziger Authorized Participant.** Als Verwahrer tätig, mit tiefen Beziehungen zu institutionellen Anlegern. Das verschafft Coinbase eine Monopolstellung bei der Erstellung und Rücknahme von ETF-Anteilen. Jeder institutionelle Zugang zu Bitcoin läuft damit über einen einzigen Kontrollpunkt.

**3. FUD über "markierte Coins" wird entstehen.** Wenn Transaktionen über Coinbase gebündelt werden, können Coins aufgrund ihrer Geschichte bewertet oder diskriminiert werden. Befürworter von "tainted coins" erhalten einen neuen Hebel.

**4. JPMorgan Cascade.** Wenn JPMorgan oder eine vergleichbare Institution beginnt, über ETF-Anteile mehr Bitcoin zu repräsentieren, als physisch vorhanden ist, entsteht Fraktionalreserve auf Bitcoin — ohne das Bitcoin-Protokoll zu ändern. Das ist das klassische Gold-Problem, das zum Fiat-System führte.

**5. Preiskontrolle durch Futures-Märkte.** Wenn die Preisfindung primär über Derivate stattfindet, können große Akteure den Spotpreis beeinflussen, ohne physisches Bitcoin zu bewegen.

**6. New York Agreement 2.0.** Der erste NY Agreement (2017) versuchte, Bitcoin über einen Konsens der Unternehmen zu verändern. Ein institutionell gestützter zweiter Versuch hätte mehr Ressourcen — und könnte auf andere Protokolländerungen abzielen (z.B. KYC-Anforderungen in Layer-2, Inflation).

**7. ETF-Schutzmaßnahmen gelten nicht.** Wer über einen ETF in Bitcoin investiert, hat die gleichen Gegenparteirisiken wie beim direkten Kauf, aber ohne die Möglichkeit, Bitcoin in einer Krise zu verwenden. Im Black-Swan-Szenario — Bankrott des ETF-Anbieters, staatliche Einfrierung — hält der ETF-Investor wertlose Anteile.

**8. Bitcoin zu Papier-Bitcoin.** Analog zum Goldstandard: Echtes Bitcoin wird in Verwahrung konzentriert; Papierversprechen auf Bitcoin zirkulieren statt der eigentlichen Coins. Der Prozess, den Hoppe für Gold beschreibt, beginnt sich zu wiederholen. [[aprycot-vertrau-mir-bruder]]

### Institutionelle Verwahrung ist strukturell schwierig

Farrington hält fest: Institutionelle Anleger — Pensionsfonds, Versicherungen, Stiftungen — sind rechtlich und praktisch nicht in der Lage, Bitcoin in Selbstverwahrung zu halten. Sie haben treuhänderische Pflichten, benötigen geprüfte Verwahrungsstrukturen und können nicht mit einer 24-Seed-Phrase operieren.

Das ist kein Vorwurf, sondern ein strukturelles Problem. Bitcoin wurde für Individuen entworfen, nicht für Rechtseinheiten mit Audit-Anforderungen. Wenn Bitcoin globale Reservefunktion übernehmen soll, muss es Lösungen geben, die institutionellen Anforderungen genügen, ohne Bitcoins Kerneigenschaften (Selbstverwahrung, Zensurresistenz, finale Abrechnung) aufzugeben.

Farrington nennt vier Ansätze, die diese Lücke angehen könnten:

**Fedi:** Federated eCash-Protokoll, das Gemeinschaftsverwahrung ermöglicht, ohne eine einzige Vertrauensparty zu schaffen.

**OP_VAULT:** Protokollerweiterung, die zeitverzögerte Auszahlungen mit Wiederrufungsoption ermöglicht — relevant für institutionelle Compliance-Anforderungen.

**Unchained Capital:** Kollaborative Multisig-Verwahrung, bei der Unchained einen Key hält, der Kunde zwei — keine vollständige Selbstverwahrung, aber dezentraler als ein einzelner Custodian.

**AnchorWatch:** Versicherung und Überwachung für Multisig-Setups, die institutionelle Anforderungen an Audit-Trails und Versicherungsschutz erfüllt. [[aprycot-vertrau-mir-bruder]]

### "Vertraue, aber überprüfe"

Farrington schließt mit dem Hinweis, dass die eigentliche Frage nicht "Soll man dem ETF vertrauen?" ist, sondern "Wie baut man Systeme, die Vertrauen überprüfbar machen?" Bitcoin selbst ist die Antwort auf diese Frage für Einzelpersonen. Für Institutionen fehlt die Infrastruktur noch. Bis sie existiert, tragen institutionelle ETF-Nutzer Risiken, die Bitcoin-Nutzer mit Selbstverwahrung nicht haben.

Das Goldparadox ist lehrreich: Gold war dezentral, aber seine physischen Eigenschaften erzwangen Verwahrung durch Dritte, was schließlich zur Zentralbank führte. Bitcoin hat das physische Verwahrungsproblem gelöst. Das soziale und rechtliche Problem — wie Institutionen Bitcoin halten ohne Kontrolle aufzugeben — ist noch offen.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-silent-ipo]]
- [[geld-staat-und-fiat-monopol]]
- [[multisig-und-kollaborative-verwahrung]]
- [[bitcoin-netzwerk-und-nodes]]
- [[regulierung-tofr-aopp]]
- [[eu-regulierung-selbstverwahrung]]
- [[miniscript-und-liana]]

## Open Questions

- Hat sich Prognose 4 (JPMorgan Cascade) nach der ETF-Genehmigung 2024 materialisiert?
- Welche regulatorischen Anforderungen müsste OP_VAULT erfüllen, um als institutioneller Custody-Standard akzeptiert zu werden?
- Gibt es eine kritische ETF-AUM-Grenze, ab der der Einfluss auf die Bitcoin-Preisfindung messbar wird?
