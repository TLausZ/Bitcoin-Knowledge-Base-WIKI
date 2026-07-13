# Bitcoin-Mining-Dezentralisierung und Transaktionszensur

**Status:** established
**Themen:** grundlagen, protokoll, self-custody, mining
**Last updated:** 2026-07-05
**Sources:** [[aprycot-bitcoin-transaktionskriege-home-mining]], [[20250914_heartmoney-bitcoin-online-bananen-offline]], [[20250615_heartmoney-hitze-hoffnung-hashrate]]

## Summary

Michael Schmid beschreibt in "Bitcoin-Transaktionskriege" ein strukturelles Risiko: Sobald eine kritische Menge des Mining in regulierbaren Jurisdiktionen konzentriert ist, können Regierungen Miner zur Transaktionszensur zwingen — so wie sie Kryptobörsen bereits zur Sanktionseinhaltung gezwungen haben. Die Analogie zu den Blocksize-Wars ist strukturell: Damals ging es um die Kapazität der Blöcke, jetzt um ihren Inhalt. Die Antwort ist Home-Mining: "Not your miner, not your block."

## Body

### Wie Zensur technisch funktioniert

Ein Miner — und nur ein Miner — entscheidet, welche Transaktionen in einen Block kommen. Spieltheoretisch ist es für einen Miner rational, die Transaktionen mit den höchsten Gebühren zu wählen. Aber nichts hindert ihn daran, bestimmte Transaktionen auszuschließen, auch gebührenreiche.

Wenn genug Miner gemeinsam zensieren, entstehen zwei Druckmittel:
1. Zensierte Transaktionen kommen nur sehr langsam oder gar nicht in die Chain.
2. Zensierende Miner könnten nicht-konforme Blöcke verwaisen lassen — Blöcke, die eine sanktionierte Adresse enthalten, werden nicht auf dem zensierenden Teil der Chain weitergebaut.

Wenn die zensierenden Miner mehr als 50 % der Hashrate halten, können sie die längere Chain erzwingen. Selbst unterhalb dieser Schwelle machen sie Bitcoin für bestimmte Adressen faktisch unbrauchbar.

Präzedenzfälle existieren bereits: Ein Mining-Pool startete im März 2021 mit der Blockierung bestimmter Adressen und hörte im Juni 2021 wieder auf — aber das Modell ist bewiesen. Chainalysis und TRM Labs vergeben bereits Risikoratings für jede UTXO im Netzwerk. Zksnacks schloss bestimmte Adressen von seinem Coinjoin-Koordinator aus. [[aprycot-bitcoin-transaktionskriege-home-mining]]

### Warum die USA eine strukturelle Gefahr darstellen

Zum Zeitpunkt des Artikels (2022) entfielen rund 35 % der globalen Hashrate auf US-amerikanische Miner — mit stark steigender Tendenz. US-Kryptobörsen halten bereits OFAC-Sanktionen ein: russische Bitcoin-Adressen werden geblockt. Bitriver, ein russischer Mining-Betreiber, wurde 2022 direkt sanktioniert.

Der nächste logische Schritt ist, dass Regierungen US-Mining-Unternehmen zur Sanktionseinhaltung verpflichten — so wie sie es mit Börsen getan haben. Je weniger Mining-Entitäten es gibt, desto weniger Angriffsfläche braucht eine Regierung. Ein Szenario, in dem die NATO-Mitgliedstaaten koordiniert ihre heimischen Miner zur Zensur verpflichten, ist keine Spekulation, sondern eine politische Verlängerung bestehender Präzedenzfälle.

### Stratum V2: Miner kontrollieren Transaktionsauswahl

Stratum V1, das Protokoll zwischen Minern und Mining-Pools, lässt die Transaktionsauswahl beim Pool. Stratum V2 führt "Job Selection" ein: Der Miner selbst wählt, welche Transaktionen er in seinen Kandidatenblock aufnimmt — der Pool validiert und broadcastet nur noch. Damit verliert eine Regierung, die einen Pool reguliert, den Hebel über die Transaktionsauswahl. Die Unterstützung für Stratum V2 wächst, auch wenn die Adoption 2022 noch begrenzt war.

### "Not your miner, not your block"

Das Argument für Home-Mining folgt der Logik der anderen Selbstverwahrungsmaximen:
- "Not your keys, not your coins" → Selbstverwahrung statt Börse
- "Not your node, not your validation" → eigener Node statt fremder Infrastruktur
- "Not your miner, not your block" → wenn jeder Block über die eigene Hashrate auch zensierte Transaktionen einschließen kann, ist Zensur nur durchsetzbar, wenn die zensierenden Miner eine Mehrheit bilden

Für jeden einzelnen Home-Miner ist die Wahrscheinlichkeit, einen Block zu finden, gering. Die Wirkung ist nicht individuell, sondern systemisch: Jede Hashrate in privaten Händen ist Hashrate, die kein Regulierer kontrollieren kann.

### Praktische Home-Mining-Anwendungsfälle

**ASIC als Heizung:** Bitcoin-Miner wandeln Energie zu 100 % in Wärme um — genau wie elektrische Heizkörper, Wasserkocher oder Infrarotheizungen. Ein ASIC ersetzt die Heizung nicht nur, er produziert dabei Bitcoin. Der Mehraufwand sind die Anschaffungskosten, die sich über die erzeugte Bitcoin amortisieren. Wer die Energie ohnehin verbrauchen würde, zahlt effektiv nichts extra.

**Solarüberschuss:** Wer eine Solaranlage überdimensioniert, speist überschüssigen Strom zu schlechten Konditionen ins Netz ein. Ein ASIC kann seinen Energieverbrauch in Sekunden hochfahren und drosseln — er monetarisiert den Überschuss in Bitcoin, ohne Netzeinspeisung.

Unternehmen wie FutureBit und Coinmine bieten Plug-and-Play-Miner für Haushalte an, ohne technisches Vorwissen.

**Lotto-Mining:** Die unterste Einstiegsstufe sind Kleinstgeräte wie der NerdAxe Gamma (ca. 1,4 TH/s, Hersteller Nerdminer.de aus Deutschland), dokumentiert im DACH-Community-Alltag 2025. Profitabel schürfen können sie nicht; der Reiz ist die Lotterie-Chance, selbst einen Block zu finden und die volle Belohnung (2025: 3,125 BTC) zu kassieren. Installation in Minuten, Betrieb nebenher im Wohnzimmer. Der systemische Wert entspricht der Home-Mining-Logik oben, im Miniaturformat: Hashrate in privater Hand plus ein Bildungseffekt — wer einen Lotto-Miner betreibt, versteht Blockbelohnung, Hashrate und Wahrscheinlichkeit aus erster Hand. [[20250914_heartmoney-bitcoin-online-bananen-offline]], [[20250615_heartmoney-hitze-hoffnung-hashrate]]

## Related

- [[bitcoin-schichtenarchitektur]]
- [[bitcoin-netzwerk-und-nodes]]
- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-mining-netz-und-oekonomie]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-als-organismus]]

## Open Questions

- Wie weit ist Stratum V2 bis 2026 in großen Pools implementiert?
- Hat die US-Regulierung tatsächlich Mining-Entitäten zur Transaktionszensur verpflichtet?
- Welche Hashrate-Konzentration gilt als kritische Schwelle für Zensuranfälligkeit?
