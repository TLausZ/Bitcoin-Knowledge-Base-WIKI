# MVRV und Realized Cap

**Status:** established
**Themen:** oekonomie, protokoll
**Last updated:** 2026-07-18
**Sources:** [[20181214_realized-capitalization-coinmetrics]], [[20181001_mvrv-ratio-mahmudov-puell]], [[20260717_wuestenfeld-btc-dashboard]]

## Summary

Die Realized Cap bewertet jeden UTXO zum Kurs seiner letzten Bewegung statt zum Tagespreis und nähert sich so der aggregierten Kostenbasis aller Bitcoin-Halter an. Das MVRV-Ratio (Market Value / Realized Value) setzt die Marktkapitalisierung dagegen und misst, wie weit der spekulative Preis von dieser Kostenbasis entfernt ist. Historisch markierten Werte über 3,7 Zyklustops und Werte unter 1,0 Kapitulationsböden. Moderne Varianten wie Wüstenfelds MVRV-z normalisieren die Serie statistisch, weil die rohen Schwellen mit wachsendem Markt an Trennschärfe verlieren.

## Body

### Realized Cap: die Kostenbasis des Netzwerks

Die Marktkapitalisierung multipliziert den letzten Börsenpreis mit allen je geschürften Coins — sie bewertet damit auch Coins zum Tagespreis, die seit 2010 unbewegt oder längst verloren sind; bei Bitcoin gelten grob 15 % der Supply als dauerhaft verloren. Die Realized Cap korrigiert das: Jeder UTXO geht mit dem Kurs in die Summe ein, der bei seiner letzten On-Chain-Bewegung galt. Verlorene Frühzeit-Coins zählen so mit Cent-Beträgen statt Zehntausenden Dollar, und lange gehaltene Positionen stehen mit ihrem Einstandskurs im Aggregat. Die Realized Cap liest sich darum als On-Chain-Schätzung dessen, was der Markt insgesamt für seine Coins bezahlt hat. [[20181214_realized-capitalization-coinmetrics]]

Entwickelt wurde die Metrik bei Coin Metrics: Pierre Rochard fragte nach einer historisch gewichteten UTXO-Market-Cap, Engineer Antoine Le Calvez baute die Methodik und prägte den Namen (Arbeitstitel war «Effective Cap»); Nic Carter stellte das Konzept im September 2018 an der Baltic-Honeybadger-Konferenz vor, im Dezember folgte der Blog-Artikel. Bei der ersten Berechnung stand die Realized Cap bei 88 Mrd. USD gegenüber einer Market Cap von 115 Mrd. USD. Der Artikel benennt die Grenzen selbst: Die Metrik unterscheidet nicht zwischen wirklich verlorenen Coins und jahrelangem Deep Cold Storage (Satoshis ~1M Coins zählen faktisch mit null), und bei Chains mit wenig Turnover kann eine hohe Realized Cap ein Artefakt der Inaktivität sein statt einer fairen Bewertung. [[20181214_realized-capitalization-coinmetrics]]

### Das MVRV-Ratio

Murad Mahmudov und David Puell teilten im Oktober 2018 die Market Cap durch die Realized Cap und erhielten einen Zyklus-Indikator: Das Verhältnis misst die Spannung zwischen kurzfristigen Spekulanten (Marktpreis) und langfristigen Haltern (Kostenbasis). Über die Historie von Oktober 2010 bis September 2018 fielen die Extremwerte mit den Zykluswenden zusammen — MVRV über 3,7 bei den Tops 2011, 2013 und 2017, MVRV unter 1,0 an den Kapitulationsböden. Ein Wert unter 1,0 heisst konkret: Der Markt handelt im Aggregat unter der eigenen Kostenbasis. Die Autoren verstehen den Ratio als mehrjähriges Zyklusinstrument, kombiniert mit anderen Indikatoren, nicht als Timing-Signal. [[20181001_mvrv-ratio-mahmudov-puell]]

### MVRV-z: statistische Normalisierung statt fester Schwellen

Feste Schwellen wie 3,7 tragen historische Zufälligkeit in sich, und wie beim Power Law komprimieren sich die Ausschläge mit wachsender Marktgrösse. Jan Wüstenfelds Market Structure Dashboard rechnet darum mit MVRV-z: dem z-Score des logarithmierten MVRV über ein rollierendes Zwei-Jahres-Fenster, ohne Zugriff auf spätere Daten («leak-free»). Gemessen wird also die Abweichung von der jüngeren eigenen Norm statt von einer festen Linie. Das unterscheidet sich vom verbreiteten vollhistorischen «MVRV Z-Score» der Chart-Anbieter. Die Serie bewegt sich träge, weil sich die aggregierte Kostenbasis nur graduell durch tatsächliche Coin-Bewegungen aktualisiert — eine Eigenschaft, die MVRV eher zum Bewertungsanker als zum schnellen Signal macht. [[20260717_wuestenfeld-btc-dashboard]]

### Einordnung

MVRV gehört zur selben Familie standardisierter Zyklusmetriken wie die Power-Law-Sigma-Abweichung: Beide messen Distanz zu einem Anker (Kostenbasis bzw. Wachstumstrend) und beide verlieren an Amplitude, je grösser der Markt wird. Wüstenfeld kombiniert beide im selben Dashboard als Bewertungsteil seiner Marktstruktur-Analyse. Grenzen: Die Realized Cap kennt nur On-Chain-Bewegungen — Börsen-interne Käufe ändern die Kostenbasis nicht, und Custody-Umschichtungen (etwa ETF-Bestände) können sie verzerren, ohne dass sich wirtschaftlich etwas ändert. [[20260717_wuestenfeld-btc-dashboard]]

## Related

- [[bitcoin-powerlaw-und-preismodelle]]
- [[onchain-indikatoren-und-anlegerverhalten]]
- [[bitcoin-volatilitaet-und-preisfindung]]
- [[bitcoin-marktkommentar-lnms]]
- [[bitcoin-akademische-forschung-bbr]]

## Open Questions

- Wie stark verzerren ETF-Custody-Umschichtungen seit 2024 die Realized Cap? Gibt es bereinigte Varianten (Entity-adjusted)? Der Coin-Metrics-Artikel skizziert mit dem «Virtual UTXO»-Ansatz für Account-Chains eine verwandte Technik.
- Historische MVRV-Zeitreihe seit 2018: Hielten die Schwellen 3,7 / 1,0 in den Zyklen 2021 und 2025/26?
