# On-Chain-Indikatoren und Anlegerverhalten

**Status:** established
**Themen:** protokoll, oekonomie, studien
**Last updated:** 2026-07-17
**Sources:** [[20230221_bmi-ausgabe-21-onchain-update-de]], [[20230509_bmi-ausgabe-22-sentiment-paper-de]], [[20230221_bmi-issue-21-onchain-update-en]], [[20230509_bmi-issue-22-sentiment-paper-en]], [[2024-03-16_Wie weiss ich, wann ich zum besten Zeitpunkt verkaufen muss]], [[2024-05-10_Was du jetzt wissen musst Eine ausführliche Analyse zur Bitcoin-Marktlage]], [[2024-09-20_The On-Chain Analyst James Check - Trying to predict the price You’re Doing It All Wrong]]

## Summary

Jan Wüstenfeld nutzt On-Chain-Daten, um das Verhalten von Bitcoin-Haltern zu lesen. Sein On-Chain-Update vom Februar 2023 zeigt, dass die jüngste Preiserholung eher von bestehenden Nutzern (verstärktes Stacking) als von neuen getragen wurde: Adressen und Transaktionszahl stiegen deutlich, das ökonomisch relevante Transfervolumen kaum. Sein im Mai 2023 veröffentlichtes Working Paper (mit Teo Geldner und Joscha Beckmann) untermauert das empirisch: Kleinanleger reagieren stark auf öffentliche Informationen und Mediennarrative, Grossanleger deutlich schwächer und teils gegenläufig. Beide Quellen behandeln die Bitcoin-Blockchain als Datenquelle für ökonomische Forschung.

## Body

### On-Chain-Update Februar 2023: Stacking statt neuer Nutzer

Nach der Seitwärts-/Abwärtsbewegung im Dezember 2022 stiegen die Adressen mit Guthaben ungleich Null gegen Ende Januar 2023 wieder deutlich. Wüstenfeld betont die Unschärfe der Metrik: Adressen sind keine Nutzer. Sein Urteil: Der Anstieg dürfte überwiegend bestehende Marktteilnehmer widerspiegeln, die wieder Satoshis kaufen und auf neue Adressen senden, weniger neue Nutzer — denn neue Kohorten springen typischerweise erst spät im Bullenmarkt auf, wenn der Hype gross ist.

Die wöchentlichen Transaktionen stiegen von rund 1,7 Millionen (Ende Dezember) auf über 2,1 Millionen. Ordinals (damals rund 130.000 im Netzwerk) trugen zum Anstieg bei, der Grossteil jedoch in den Wochen davor. Entscheidend: Der Gesamtwert der on-chain abgewickelten Transaktionen legte kaum zu, und das nach Alter aufgeschlüsselte ausgegebene Volumen (Spent Volume) blieb weitgehend unverändert. Der Anteil der seit über einem Jahr unbewegten Bitcoin lag nahe einem Allzeithoch bei etwa 67 % — langfristige Halter hielten fest.

Sein Fazit: viel Aktivität in Adressen und Transaktionszahl, aber geringe ökonomische Relevanz. Ob dies der Beginn des nächsten Bullenmarktes war, liess er offen und verwies auf unterschätzte Fed-Entschlossenheit und ausgeblendete Rezessionsrisiken. [[20230221_bmi-ausgabe-21-onchain-update-de]]

### Working Paper: Sentiment, Medienaufmerksamkeit und Entitätsgrösse

Im Mai 2023 veröffentlichte Wüstenfeld mit Teo Geldner und Joscha Beckmann das Working Paper «The relevance of sentiment and media attention for bitcoin holdings across entities» (SSRN 4436838). Datenbasis: Entitätsdaten von Glassnode und Sentimentdaten von Thomson Reuters MarketPsych. Methodik: lineare Breakpoint-Regressionen, um Verschiebungen in der Halterzusammensetzung und im Umgang mit Bitcoin über die Zeit zu erfassen.

Kernergebnisse:

- Kleinanleger reagieren stark auf öffentliche Informationen und Mediennarrative; sie erhöhen ihre Positionen, wenn der Preis steigt, die Stimmung positiv und die Aufmerksamkeit hoch ist.
- Grossanleger reagieren deutlich schwächer, teils in die entgegengesetzte Richtung.
- Erklärung: Grossanleger verlassen sich vermutlich stärker auf nicht-öffentliche Informationen und verfolgen andere Anlageziele.

Die Autoren ordnen ihre Arbeit als Beitrag zu einer noch dünnen Literatur ein und heben die Bitcoin-Blockchain als wertvolle, in den Wirtschaftswissenschaften bislang kaum genutzte Datenquelle hervor. [[20230509_bmi-ausgabe-22-sentiment-paper-de]]

### Verbindung der beiden Befunde

Das On-Chain-Update und das Paper greifen ineinander: Beide unterscheiden Halter nach Verhalten und Grösse. Die Beobachtung, dass die Erholung 2023 von bestehenden Stackern und nicht von hype-getriebenen Neueinsteigern getragen wurde, ist die anekdotische Entsprechung des empirischen Befunds, dass kleinere Anleger prozyklisch auf Narrative reagieren, während grössere Bestände ruhiger bleiben. Das ergänzt das Bild der langfristigen Halter aus [[selbstverwahrung-und-boersenrisiken]] (FTX-Analyse: LTH-Anteil kaum gesunken) um eine methodische Grundlage.

### Langzeithalter-Verteilung als Zyklus-Signal (LNMS, 2024)

Pascal Hügli (Less Noise More Signal) wendet dieselbe Halter-Logik auf den ETF-Zyklus 2024 an und liefert damit eine anekdotische Antwort auf die Frage, ob das Muster «prozyklische Kleinanleger, ruhige Grossbestände» weiter gilt. Sein wiederkehrendes Timing-Muster: Nach einem neuen Allzeithoch beginnt die «Euphoriephase», in der Langzeithalter (LTH) in die Stärke hinein verteilen, während neue Spekulanten einsteigen. Von Januar bis Mitte März 2024 verkauften die LTH ins neue Hoch; im Mai 2024 hatten sie ihre Abverkäufe reduziert, und die prozentuale LTH-Netto-Veränderung lag bei null (zugeführte und abgehende Coins im Gleichgewicht). Historisch, so Hügli, markierte der Punkt, an dem starke LTH-Abverkäufe nach einem Hoch abflachen, den Zyklushöchststand — im Mai 2024 deutete das Bild eher auf einen ausgeglichenen als einen überhitzten Markt. [[2024-05-10_Was du jetzt wissen musst Eine ausführliche Analyse zur Bitcoin-Marktlage]], [[2024-03-16_Wie weiss ich, wann ich zum besten Zeitpunkt verkaufen muss]]

Sein Interviewgast James Check («Checkmate») ergänzt die Verhaltensseite: Anleger sollten zuerst klären, ob sie Trader, Investor oder Sparer sind; das Muster «verkaufen und billiger zurückkaufen» sei für die meisten ein Verlustgeschäft gegenüber «enhanced DCA», und On-Chain-Metriken dienten der Einordnung von Bärenmarkt-Böden und lokalen Bullen-Tops, nicht der Preisprognose. Das stützt Wüstenfelds Befund, dass mediengetriebenes prozyklisches Handeln vor allem Kleinanleger trifft. [[2024-09-20_The On-Chain Analyst James Check - Trying to predict the price You’re Doing It All Wrong]] → gebündelt in [[bitcoin-marktkommentar-lnms]].

### Einordnung

Das On-Chain-Update ist zeitgebundener Marktkommentar; die Metriken (Adressen, Spent Volume, Supply-Alter) stammen von Glassnode, messari und Bytetree. Das Working Paper ist begutachtungsfähige Forschung, aber ein Preprint-Stand von 2023 — die zitierten Kausalrichtungen sind Regressionsbefunde, keine bewiesenen Mechanismen. Wüstenfeld selbst weist auf die Adressen-≠-Nutzer-Unschärfe hin. Hüglis LNMS-Beiträge sind ebenfalls zeitgebundener Kommentar mit Pro-Bitcoin-Bias; die Interview-Ausgaben liegen nur als Podcast-Zusammenfassungen vor.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[makro-zinskurve-fed-und-rezession]]
- [[bitcoin-volatilitaet-und-preisfindung]]
- [[bitcoin-und-psychologie]]
- [[op-return-und-datenspeicherung]]
- [[bitcoin-marktkommentar-lnms]]

## Open Questions

- Wurde das Working Paper seit 2023 in einer Fachzeitschrift veröffentlicht (peer-reviewed Endfassung)? Falls ja, als aktualisierte RAW-Quelle nachziehen.
- Hält der Befund «Kleinanleger prozyklisch, Grossanleger antizyklisch» auch für den ETF-getriebenen Zyklus 2024–2026, in dem Institutionen früh kauften (vgl. [[bitcoin-monetarisierung]])?
- Wie robust ist die Adressen-als-Proxy-Metrik angesichts von Ordinals und Adress-Wiederverwendung?
