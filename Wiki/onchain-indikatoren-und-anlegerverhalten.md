# On-Chain-Indikatoren und Anlegerverhalten

**Status:** emerging
**Last updated:** 2026-07-07
**Sources:** [[20230221_bmi-ausgabe-21-onchain-update-de]], [[20230509_bmi-ausgabe-22-sentiment-paper-de]]

## Summary

Jan Wüstenfeld nutzt On-Chain-Daten, um das Verhalten von Bitcoin-Haltern zu lesen. Sein On-Chain-Update vom Februar 2023 zeigt, dass die jüngste Preiserholung eher von bestehenden Nutzern (verstärktes Stacking) als von neuen getragen wurde: Adressen und Transaktionszahl stiegen deutlich, das ökonomisch relevante Transfervolumen kaum. Sein im Mai 2023 veröffentlichtes Working Paper (mit Teo Geldner und Joscha Beckmann) untermauert das empirisch: Kleinanleger reagieren stark auf öffentliche Informationen und Mediennarrative, Großanleger deutlich schwächer und teils gegenläufig. Beide Quellen behandeln die Bitcoin-Blockchain als Datenquelle für ökonomische Forschung.

## Body

### On-Chain-Update Februar 2023: Stacking statt neuer Nutzer

Nach der Seitwärts-/Abwärtsbewegung im Dezember 2022 stiegen die Adressen mit Guthaben ungleich Null gegen Ende Januar 2023 wieder deutlich. Wüstenfeld betont die Unschärfe der Metrik: Adressen sind keine Nutzer. Sein Urteil: Der Anstieg dürfte überwiegend bestehende Marktteilnehmer widerspiegeln, die wieder Satoshis kaufen und auf neue Adressen senden, weniger neue Nutzer — denn neue Kohorten springen typischerweise erst spät im Bullenmarkt auf, wenn der Hype groß ist.

Die wöchentlichen Transaktionen stiegen von rund 1,7 Millionen (Ende Dezember) auf über 2,1 Millionen. Ordinals (damals rund 130.000 im Netzwerk) trugen zum Anstieg bei, der Großteil jedoch in den Wochen davor. Entscheidend: Der Gesamtwert der on-chain abgewickelten Transaktionen legte kaum zu, und das nach Alter aufgeschlüsselte ausgegebene Volumen (Spent Volume) blieb weitgehend unverändert. Der Anteil der seit über einem Jahr unbewegten Bitcoin lag nahe einem Allzeithoch bei etwa 67 % — langfristige Halter hielten fest.

Sein Fazit: viel Aktivität in Adressen und Transaktionszahl, aber geringe ökonomische Relevanz. Ob dies der Beginn des nächsten Bullenmarktes war, ließ er offen und verwies auf unterschätzte Fed-Entschlossenheit und ausgeblendete Rezessionsrisiken. [[20230221_bmi-ausgabe-21-onchain-update-de]]

### Working Paper: Sentiment, Medienaufmerksamkeit und Entitätsgröße

Im Mai 2023 veröffentlichte Wüstenfeld mit Teo Geldner und Joscha Beckmann das Working Paper «The relevance of sentiment and media attention for bitcoin holdings across entities» (SSRN 4436838). Datenbasis: Entitätsdaten von Glassnode und Sentimentdaten von Thomson Reuters MarketPsych. Methodik: lineare Breakpoint-Regressionen, um Verschiebungen in der Halterzusammensetzung und im Umgang mit Bitcoin über die Zeit zu erfassen.

Kernergebnisse:

- Kleinanleger reagieren stark auf öffentliche Informationen und Mediennarrative; sie erhöhen ihre Positionen, wenn der Preis steigt, die Stimmung positiv und die Aufmerksamkeit hoch ist.
- Großanleger reagieren deutlich schwächer, teils in die entgegengesetzte Richtung.
- Erklärung: Großanleger verlassen sich vermutlich stärker auf nicht-öffentliche Informationen und verfolgen andere Anlageziele.

Die Autoren ordnen ihre Arbeit als Beitrag zu einer noch dünnen Literatur ein und heben die Bitcoin-Blockchain als wertvolle, in den Wirtschaftswissenschaften bislang kaum genutzte Datenquelle hervor. [[20230509_bmi-ausgabe-22-sentiment-paper-de]]

### Verbindung der beiden Befunde

Das On-Chain-Update und das Paper greifen ineinander: Beide unterscheiden Halter nach Verhalten und Größe. Die Beobachtung, dass die Erholung 2023 von bestehenden Stackern und nicht von hype-getriebenen Neueinsteigern getragen wurde, ist die anekdotische Entsprechung des empirischen Befunds, dass kleinere Anleger prozyklisch auf Narrative reagieren, während größere Bestände ruhiger bleiben. Das ergänzt das Bild der langfristigen Halter aus [[selbstverwahrung-und-boersenrisiken]] (FTX-Analyse: LTH-Anteil kaum gesunken) um eine methodische Grundlage.

### Einordnung

Das On-Chain-Update ist zeitgebundener Marktkommentar; die Metriken (Adressen, Spent Volume, Supply-Alter) stammen von Glassnode, messari und Bytetree. Das Working Paper ist begutachtungsfähige Forschung, aber ein Preprint-Stand von 2023 — die zitierten Kausalrichtungen sind Regressionsbefunde, keine bewiesenen Mechanismen. Wüstenfeld selbst weist auf die Adressen-≠-Nutzer-Unschärfe hin.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[makro-zinskurve-fed-und-rezession]]
- [[bitcoin-volatilitaet-und-preisfindung]]
- [[bitcoin-und-psychologie]]
- [[op-return-und-datenspeicherung]]

## Open Questions

- Wurde das Working Paper seit 2023 in einer Fachzeitschrift veröffentlicht (peer-reviewed Endfassung)? Falls ja, als aktualisierte RAW-Quelle nachziehen.
- Hält der Befund «Kleinanleger prozyklisch, Großanleger antizyklisch» auch für den ETF-getriebenen Zyklus 2024–2026, in dem Institutionen früh kauften (vgl. [[bitcoin-monetarisierung]])?
- Wie robust ist die Adressen-als-Proxy-Metrik angesichts von Ordinals und Adress-Wiederverwendung?
