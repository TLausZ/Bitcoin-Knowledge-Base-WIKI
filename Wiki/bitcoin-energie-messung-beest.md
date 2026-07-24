# Bitcoin-Energiemessung und das BEEST-Modell

**Status:** established
**Themen:** mining, oekonomie, studien
**Last updated:** 2026-06-30
**Sources:** [[BEEST (Bitcoin Energy & Emissions Sustainability Tracker)]], [[Bitcoin By Energy Source]], [[The Bitcoin Facts that Every Investment Committee Must Know]], [[Why Bitcoin is an essential part of every ESG Fund]], [[7 Renewables Misconceptions]], [[Positive Press ABOUT BITCOIN & ESG outnumbers negatives 4_1 so far in 2023]], [[Improving OUR ESTIMATE of Bitcoin ENERGY CONSUMPTION]], [[Accurately, dynamically calculating Bitcoin Network Emissions]], [[Comparing Bitcoin Mining to other Industries’ energy mix]], [[New Insights on Bitcoin Mining and Sustainability]], [[Bitcoin Mining Now Uses 10.9% More Renewables, Goes Unreported]], [[Quantifying the EMISSION NEGATIVE COMPONENT OF the Bitcoin Network]]

## Summary

Die meistzitierte Zahl zum Bitcoin-Energieverbrauch stammte jahrelang vom Cambridge Centre for Alternative Finance (CCAF). Daniel Batten baute ab 2022 ein eigenes Bottom-up-Modell namens BEEST (Bitcoin Energy and Emissions Sustainability Tracker), das jeden bekannten grösseren Mining-Betrieb einzeln erfasst und so auch Off-Grid-Mining einrechnet, das CCAF ausschliesst. Ergebnis: CCAF überschätzt den Energieverbrauch um mindestens 23,7% und die Emissionen um über 100%. Mit Off-Grid-Mining liegt der nachhaltige Energieanteil über 50%, die grösste Einzelquelle ist Wasserkraft. Bitcoin ist damit der Industriesektor mit dem höchsten Anteil nachhaltiger Energie und der einzige, dessen Wachstum nicht zu höheren Emissionen führte. Diese Datenlage ist die Grundlage des ESG-Investmentarguments: Rund 23 Billionen USD ESG-Kapital meiden Bitcoin auf Basis von vier Behauptungen, die alle auf eine einzige veraltete Studie zurückgehen.

## Body

### A — Warum CCAF zu hoch lag

CCAF war über Jahre die Standardquelle für Bitcoins Strom- und Emissionsschätzungen. Batten identifiziert zwei strukturelle Fehlerquellen im Cambridge-Modell (CBECI).

Erstens die Energieschätzung. CBECI leitet den Miner-Mix aus dem Bitcoin-Preis ab, was das tatsächliche Abschaltverhalten heutiger Miner nicht mehr abbildet, und arbeitet mit einem Datensatz, der die Effizienzgewinne der aktuellen ASIC-Generation nicht erfasst. Batten verglich fünf Methodiken, darunter die von Blockware, Luxor und Marathon. Alle lagen unter CBECI, der nächste Wert 23,7%, der niedrigste 37,1% darunter. BEEST übernahm die konservativste Schätzung (Blockware), woraus folgt, dass CBECI den Verbrauch konsistent um mindestens 23,7% überschätzt. Cambridge selbst räumte am 31. August 2023 ein, den Verbrauch über zwei Jahre lang zu hoch angesetzt zu haben. [[Improving OUR ESTIMATE of Bitcoin ENERGY CONSUMPTION]]

Zweitens die Emissionsintensität. Emissionen ergeben sich aus Emissionsintensität mal Energieverbrauch, analog zu BIP gleich Pro-Kopf-BIP mal Bevölkerung. Beide Faktoren waren bei CCAF überhöht. Stand 9. Juni 2023 rechnete BEEST mit 299 g/kWh statt CCAFs 506,7 g/kWh und 115 TWh statt 138,6 TWh Jahresverbrauch. Das Produkt: 34,07 Mt CO2e gegenüber CCAFs 70,22 Mt, eine Überschätzung um 106%. [[Accurately, dynamically calculating Bitcoin Network Emissions]]

### B — Off-Grid-Mining, der blinde Fleck

Der entscheidende Unterschied zwischen BEEST und CCAF ist Off-Grid-Mining. Das Cambridge-Modell erfasst es laut eigener Methodik-Seite nicht. BEEST ist ein Bottom-up-Modell, das jeden bekannten relevanten Betrieb einzeln aggregiert und damit geschätzte 98% der globalen Hashrate abdeckt. [[New Insights on Bitcoin Mining and Sustainability]]

52 bekannte Off-Grid-Mining-Firmen stehen für 28% der gesamten Hashrate und laufen zu fast 80% auf nachhaltiger Energie. Das überrascht nicht: Wer off-grid mint, sucht den billigsten Strom, und der ist meist erneuerbar oder gestrandet. Diese Gruppe aus dem Modell zu streichen, vergleicht Batten mit einer Wahlumfrage, die nur Stadtbewohner befragt. Zwei Wochen nach Cambridges Eingeständnis vom August 2023 wechselte Bloomberg Intelligence am 14. September 2023 von CCAF auf BEEST. [[The Bitcoin Facts that Every Investment Committee Must Know]]

### C — Die Energiequellen des Netzwerks

Cambridge hatte zuvor Kohle als Hauptenergiequelle des Bitcoin-Netzwerks angegeben. Mit eingerechnetem Off-Grid-Mining verschiebt sich das Bild deutlich. Grösste Einzelquelle ist Wasserkraft mit rund 23% des gesamten Minings; on-grid liefert Hydro nur 15,8%, doch mehr als die Hälfte des nachhaltigen Off-Grid-Minings ist wasserbetrieben (OceanFalls, Blockfusion, Hive, Gridshare und weitere). Zweitstärkste nachhaltige Quelle ist Wind mit fast 14%, getragen unter anderem von Marathons Behind-the-Meter-Windparks und dem hohen Windanteil im texanischen ERCOT-Netz, wo rund ein Viertel des Netzwerks sitzt. [[Bitcoin By Energy Source]]

Der Kohleanteil liegt bei 22,92%, Gas bei 21,14%. Batten zieht den Vergleich zu Elektroautos: Beide Technologien haben keine direkten Emissionen, beide beziehen ihre Scope-2-Emissionen aus dem Strommix. Ein vollständig ans Netz gebundenes E-Auto spiegelt den globalen Grid-Mix mit Kohle als grösster Quelle (36,7%). Bitcoin-Mining ist nicht ans lokale Netz gebunden und nutzt daher 38% weniger Kohle als ein durchschnittliches E-Auto. Der nachhaltige Anteil des Netzwerks wuchs laut BEEST zuletzt um 6,2% pro Jahr. [[Bitcoin By Energy Source]]

US-spezifisch lässt sich das Modell ebenfalls auswerten, indem alle Nicht-US-Aktivitäten auf null gesetzt werden. Die USA stellten Anfang 2023 rund 47,7% der Hashrate, verursachten aber wegen geringerer Kohlenutzung nur 39,7% der globalen Emissionen, bei 52,76% nachhaltigem Anteil. [[New Insights on Bitcoin Mining and Sustainability]]

### D — Bitcoin gegen andere Industrien

BEEST erlaubt den Vergleich mit anderen Sektoren über den Zeitraum Juli 2019 bis Juni 2023. Bitcoin-Mining ist mit 52,6% der höchste Nutzer nachhaltiger Energie und verzeichnete mit +38% zugleich den stärksten Zuwachs aller verglichenen Industrien. Zum Vergleich: Bankensektor 39,2% (Annahme: vollständig Grid-Mix), Industrie 32%, Eisen und Stahl 9,8%, Goldindustrie 12,8%. Bei den meisten anderen Sektoren stammt der gesamte Zuwachs allein aus dem allgemeinen «Greening» des Netzes (rund 2,6% über vier Jahre), nicht aus eigener Anstrengung. [[Comparing Bitcoin Mining to other Industries’ energy mix]]

Die Renewable-Adoption des Minings ging schnell: 58,4% nachhaltiger Anteil nach 14 Jahren, Wachstumsrate 59% seit Q1 2021 und rund 383% seit 2013. Batten nennt das einen «Roger-Bannister-Effekt»: ein Sektor zeigt, dass ein vermeintlich unmögliches Tempo erreichbar ist, und nimmt damit anderen Industrien die Ausrede, ein schneller Umstieg sei unmöglich. [[Why Bitcoin is an essential part of every ESG Fund]]

### E — Der Mythos vom grüner werdenden China-Verbot

Nach dem chinesischen Mining-Verbot 2021 berichteten unter anderem die New York Times, das Netzwerk sei fossiler geworden. Diese Berichte stützten sich auf eine einzige Studie mit mehreren Fehlern: falsche Analyse von Hashrate und Energiemix vor und nach dem Verbot, und die unterschlagene Verlagerung von Mining aus dem Iran (98% fossil) nach Kanada (67% erneuerbar). Batten rechnete mit Worst-Case-Annahmen unabhängig nach und fand einen Anstieg der erneuerbaren Nutzung um mindestens 10,9%. Das chinesische Verbot wirkte faktisch als reines Kohle-Verbot: In China lief Bitcoin-Mining überwiegend nur in der Regenzeit auf billiger, sonst abgeregelter Wasserkraft, in der Trockenzeit dagegen auf Kohle. Die Verlagerung dieses Kohleanteils nach Nordamerika entkohlte das Netzwerk spürbar. Kasachstans Hashrate (99% fossil) fiel bis August 2022 wieder auf das Niveau vor dem Verbot. [[Bitcoin Mining Now Uses 10.9% More Renewables, Goes Unreported]]

### F — Der emissionsnegative Anteil

Über den nachhaltigen Anteil hinaus misst BEEST einen emissionsnegativen Anteil: Mining auf zuvor atmosphärengebundenem Methan, das ohne den Miner geflart oder geentlüftet worden wäre. Stand 21. Juli 2023 liefen 1,3% des Netzwerks auf solchen Quellen, fast ausschliesslich geflartes Gas der Öl- und Gasindustrie. Wegen des hohen GWP20 von Methan (84× CO2) entspricht das einer Gutschrift von rund −2,3 Mt CO2e gegen damals 40,5 Mt Netzwerkemissionen, also einer Netto-Emissionsminderung von 5,7%. Generatoren entfernen Methan effektiver als Flares: Crusoes Generatoren beseitigen 99,89% statt der 91,1% einer Flare. Die 180,35 MW geflarten Methans mindern rund 2,04 Mt CO2e pro Jahr, vergleichbar mit 30 Millionen über zehn Jahre wachsenden Bäumen. [[Quantifying the EMISSION NEGATIVE COMPONENT OF the Bitcoin Network]]

Die Quantifizierung der Methanminderung nach Quelle (geflart −63%, geentlüftet −95%, gemischte Deponie −88%) und die Szenarien zum UNEP-Methanziel sind in [[bitcoin-mining-energiequellen]] ausgeführt.

### G — Die vier ESG-Firsts

Mit dem korrigierten Datensatz lassen sich vier Aussagen belegen, die kein anderer Industriesektor für sich beanspruchen kann:

Erstens, über 50% nachhaltige Energie macht Bitcoin zum führenden Industrienutzer nachhaltigen Stroms. Zweitens, die Emissionen sind über vier Jahre nicht gestiegen, obwohl die Hashrate um über 400% und der Preis um 160% wuchsen. Bitcoin ist damit der einzige globale Sektor, dessen Wachstum nicht zu Emissionswachstum führte. Drittens, die Emissionsintensität hat sich halbiert und liegt nun unter der anderer Industrien. Viertens, die grösste Energiequelle ist Wasserkraft, nicht fossiler Brennstoff, was ebenfalls einzigartig ist. [[The Bitcoin Facts that Every Investment Committee Must Know]]

Diese Datenlage ist policy-relevant: Das Weisse Haus hatte für eine günstige Mining-Regulierung Daten verlangt, die zeigen, dass Emissionen mit dem Netzwachstum nicht aus dem Ruder laufen. Genau diese Daten liefert BEEST. [[The Bitcoin Facts that Every Investment Committee Must Know]]

### H — Das ESG-Investmentargument

Rund 23 Billionen USD stecken in ESG-Fonds, die wegen des bestehenden ESG-Narrativs keinen höheren Anteil in Bitcoin allokieren. Die vier ESG-Argumente gegen Bitcoin (überwiegend fossil, grosse und exponentiell wachsende Emissionen, steigende Emissionsintensität, Kohle als Hauptquelle) gehen sämtlich auf eine einzige CCAF-Auswertung zurück, deren «Herzschlag», die kontinuierlich aktualisierte Mining-Map, im Januar 2022 stehenblieb. [[The Bitcoin Facts that Every Investment Committee Must Know]]

Batten rechnet den Hebel vor: Würden ESG-Fonds 1% ihres verwalteten Vermögens in Bitcoin allokieren, stiege die Marktkapitalisierung (von damals 724 Mrd. USD) auf rund 1,76 Bio.; bei 2,5% auf rund 3,3 Bio. Daraus entsteht eine positive Rückkopplung zwischen ESG- und Bitcoin-Community. Battens eigener Hintergrund stützt das Argument: 19 Jahre Impact-Investment, über 200 geprüfte Cleantech-Vorschläge, von denen er Bitcoin den «am schnellsten wirkenden, am weitesten reichenden und am besten messbaren» nennt. [[The Bitcoin Facts that Every Investment Committee Must Know]]

Daten allein bringen Bitcoin laut Batten bis zur 1%-Marke; darüber hinaus braucht es konkrete Klimawirkung. Hier setzt die Methanminderung an: Der White-House-OSTP-Bericht nannte Mining auf geentlüftetem Methan «eher hilfreich als hinderlich» für die US-Klimaziele, der IMF-Policy-Lead nannte die Methanminderung «das mit Abstand überzeugendste ESG-Argument für Bitcoin». Wenn Bitcoin auf 35 mittelgrossen geentlüfteten Deponien minen würde, würde es laut Battens Rechnung die erste Industrie der Welt, die ohne Offsets treibhausgasnegativ wird. Die nötige Infrastrukturinvestition dafür schätzt er auf rund 421 Mio. USD, gegenüber 12,1 Mrd., wenn man Crusoes flaring-basierten Ansatz (505 Mio. für 4% Minderung) einfach hochskalierte. Die menschliche Seite dieser Deponien ist in [[bitcoin-humanitaere-anwendungen]] beschrieben. [[The Bitcoin Facts that Every Investment Committee Must Know]]

### I — Der Narrativwandel in der Presse

Dass sich diese Datenlage durchsetzt, zeigt sich am Verhältnis positiver zu negativer Presse. Bis zum ersten Drittel 2023 kippte die Berichterstattung zu Bitcoin und Umwelt auf fast 4:1 zugunsten positiver Artikel (23 positiv, 5 neutral, 6 negativ), nach strenger Zählung ohne Krypto-interne Quellen und ohne Doppelungen desselben Ereignisses. Batten ordnet das in das wiederkehrende Muster disruptiver Technologien ein: Fahrrad, Buch, Radio und Internet wurden anfangs aus Angst vor dem Unbekannten attackiert, bevor sich der Nutzen durchsetzte. [[Positive Press ABOUT BITCOIN & ESG outnumbers negatives 4_1 so far in 2023]]

## Related

- [[bitcoin-mining-energiequellen]]
- [[bitcoin-mining-narrativ-und-kritik]]
- [[greenpeace-vs-bitcoin]]
- [[bitcoin-kommunikation-und-orange-pilling]]
- [[bitcoin-humanitaere-anwendungen]]
- [[bitcoin-etf-und-institutionelle-verwahrung]]

- [[softwar|Softwar (Jason P. Lowery)]] ← Buch

## Open Questions

- BEEST ist ein bottom-up gepflegtes Modell einer Einzelperson. Wer übernimmt die Pflege und Validierung, falls Batten aussteigt, und gibt es eine unabhängige Reproduktion der Ergebnisse?
- Die ESG-Firsts beruhen auf Daten bis 2023/2025. Hält die Aussage «Wachstum ohne Emissionswachstum», nachdem KI-Rechenzentren und Mining um denselben Strom konkurrieren?
- Wie verlässlich ist die 98%-Hashrate-Abdeckung, wenn neue Off-Grid-Betriebe bewusst unsichtbar bleiben?
