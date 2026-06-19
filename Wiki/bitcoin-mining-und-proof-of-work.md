# Bitcoin Mining und Proof of Work

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[20250327_wie-funktioniert-bitcoin-mining-eigentlich]], [[20260424_wie-das-21-millionen-limit-von-bitcoin-tatsächlich-durchgesetzt-wird]], [[learnmeabitcoin-beginners-guide-mining]], [[learnmeabitcoin-beginners-guide-difficulty]], [[learnmeabitcoin-technical-mining-overview]], [[learnmeabitcoin-technical-mining-candidate-block]], [[learnmeabitcoin-technical-mining-target]], [[learnmeabitcoin-technical-mining-coinbase-transaction]], [[learnmeabitcoin-technical-mining-block-reward]], [[learnmeabitcoin-technical-mining-memory-pool]]

## Summary

Bitcoin-Mining ist der Prozess, durch den neue Blöcke zur Blockchain hinzugefügt und neue Bitcoin in Umlauf gebracht werden. Miner berechnen Billionen von Hashwerten pro Sekunde und suchen nach einem, der einen vorgegebenen Zielwert unterschreitet. Dieser physische Aufwand — Proof of Work — sichert das Netzwerk, weil Angriffe real Geld und Energie kosten. Das Netzwerk passt die Schwierigkeit alle zwei Wochen automatisch an, um die Blockzeit bei zehn Minuten zu halten. Zur Umweltwirkung des Minings: → [[bitcoin-mining-umwelt]]

## Body

### Candidate Block und Coinbase-Transaktion

Bevor ein Miner anfängt zu hashen, baut er einen **Candidate Block**:

1. Transaktionen aus dem Mempool auswählen (nach sat/vByte sortiert)
2. **Coinbase-Transaktion** als erste Transaktion erstellen — spezielles Format: kein echter Input (TXID = 32 Nullbytes, VOUT = 0xFFFFFFFF), beliebige Outputs die Block-Reward + Gebühren einsammeln. Das ScriptSig beginnt mit der Block-Höhe (BIP 34) und kann beliebige Daten enthalten (z.B. Botschaft von Satoshi in Block 0: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks").
3. Merkle Root aller Transaktionen berechnen
4. Block-Header zusammenstellen
5. Nonce von 0 bis 4.294.967.295 iterieren — Hash nach jedem Versuch prüfen

**Coinbase-Regeln (BIP-Anforderungen):**
- Genau 1 Input (TXID = 0, VOUT = 0xFFFFFFFF)
- BIP 34: ScriptSig beginnt mit Block-Höhe
- BIP 141 (SegWit): Witness-Feld enthält 32-Byte reserved value; einer der Outputs enthält wTXID-Commitment
- Outputs dürfen Block-Reward (Subsidy + Fees) nicht überschreiten

**Memory Pool (Mempool):** Jeder Node hält einen lokalen Wartebereich für unbestätigte Transaktionen im Arbeitsspeicher. Wenn ein neuer Block ankommt, werden alle darin enthaltenen Transaktionen aus dem Mempool entfernt; konfliktende Transaktionen werden ebenfalls entfernt. Transaktionen, die im Mempool abgelaufen sind oder nie genug Gebühr zahlen, werden nie gemined — keine Garantie für Aufnahme in die Blockchain.

### Das Grundprinzip: Würfeln mit riesigen Zahlen

Bitcoin-Mining ist kein "Lösen komplexer mathematischer Rätsel". Es ist ein Würfelspiel: Miner suchen eine Zufallszahl (Nonce), sodass der SHA-256-Hash des Block-Headers kleiner als ein vorgegebener Zielwert ist. Hashwerte sind nicht vorhersagbar — man muss einfach probieren, Milliarden mal pro Sekunde.

**SHA-256** hat vier Eigenschaften, die es dafür ideal machen:
- **Deterministisch:** Gleicher Input → immer gleicher Output; jeder kann prüfen
- **Nicht umkehrbar:** Aus dem Hash kann man nicht auf den Input schließen
- **Chaotisch-sensitiv:** Jede minimale Input-Änderung ändert den Output vollständig
- **Riesiger Wertebereich:** 2^256 mögliche Ergebnisse — mehr als Atome im Universum

Der Zielwert bestimmt den Schwierigkeitsgrad: Niedriger Zielwert → sehr wenige gültige Hashes → schwieriger; hoher Zielwert → mehr gültige Hashes → leichter.

### Was Miner konkret tun

Ein Miner baut den nächsten Block:
1. Ausstehende Transaktionen aus dem Mempool auswählen (Priorität: hohe Gebühren)
2. Block-Header zusammenstellen: Referenz auf vorherigen Block (prev_hash), Merkle-Root aller Transaktionen, Timestamp, Schwierigkeitsziel, Nonce
3. Nonce variieren → SHA-256-Hash berechnen → Zielwert unterschritten? → Block gefunden
4. Block ans Netzwerk senden → alle Nodes prüfen den Hash (trivial schnell) und akzeptieren bei Gültigkeit

Moderne ASIC-Hardware schafft mehrere **Hundert Terahash pro Sekunde** (10^14 Hashes/s). Das gesamte Bitcoin-Netzwerk erreicht mehrere Hundert Exahash (10^20 Hashes/s) — ein Ausmaß an physischer Rechenarbeit ohne Vergleich in der Geschichte.

### Schwierigkeitsanpassung

Alle 2016 Blöcke (~zwei Wochen) passt das Bitcoin-Protokoll den Zielwert automatisch an, um die durchschnittliche Blockzeit bei **zehn Minuten** zu halten:

- Wächst die globale Hashrate (mehr Miner, schnellere Hardware) → Schwierigkeit steigt
- Verlässt Hashrate das Netzwerk (Mining-Verbote, Preisabsturz) → Schwierigkeit sinkt automatisch

Die Schwierigkeitsanpassung ist eine der elegantesten Selbstregulierungen im Protokoll: stabile Blockzeit, egal ob 100 oder 1.000.000 Miner aktiv sind.

### Warum Proof of Work das Netzwerk sichert

Der physische Aufwand ist der eigentliche Sicherheitsmechanismus. Um einen Block rückwirkend zu verändern — z.B. eine Zahlung rückgängig zu machen — müsste ein Angreifer:
- Mehr Hashrate als alle ehrlichen Miner zusammen aufbringen (51%-Angriff)
- Alle Folgeblöcke neu berechnen, schneller als das Netzwerk neue produziert
- Das Netzwerk davon überzeugen, auf den manipulierten Chain zu wechseln

Bei aktueller Hashrate ist ein 51%-Angriff prohibitiv teuer. Und selbst bei Erfolg: Ein glaubwürdiger Angriff zerstörte das Vertrauen in Bitcoin — und damit den Wert der eigenen Coins des Angreifers. Der Incentive-Mechanismus macht ehrliches Mining strukturell profitabler als Angriff.

Proof of Work ist der einzige bekannte Konsensmechanismus, der Sybil-Resistenz (Schutz vor gefälschten Identitäten) ohne zentralen Gatekeeper bietet. Mehr Hashrate = mehr Einfluss — aber Hashrate kostet echte Ressourcen, die man nicht fälschen kann.

### Hardware-Evolution: CPU → GPU → FPGA → ASIC

**CPU-Mining (2009–2010):** Satoshi und die ersten Nutzer minen auf normalen Prozessoren. Einstiegskosten: null. Jeder PC kann mitmachen.

**GPU-Mining (2010–2012):** Grafikkarten sind für parallele Berechnungen optimiert — ~100× effizienter als CPUs bei SHA-256. Mining wird zur Spezialaufgabe; normale PCs fallen heraus.

**FPGA-Mining (2011–2012):** Field Programmable Gate Arrays — konfigurierbare Chips, ~10× effizienter als GPUs. Kurze Übergangsphase.

**ASIC-Mining (2013–heute):** Application-Specific Integrated Circuits — Chips, die ausschließlich SHA-256 berechnen können, nichts sonst. Milliarden-fach effizienter als CPUs. Ein moderner ASIC (Bitmain Antminer S21, 2024) schafft ~200 Terahash/s bei ~17 Joule/Terahash. ASICs machen Mining irreversibel industriell: nur noch große Operatoren mit günstiger Energie und neuester Hardware sind langfristig profitabel.

Die ASIC-Ära hat zwei Konsequenzen: Das Netzwerk ist sicherer (mehr Kapitalinvestition pro Hashrate), aber Mining ist zentralisierter (weniger Akteure, größere Anlagen).

### Mining Pools

Einzelne Miner mit wenig Hashrate würden statistisch Monate oder Jahre auf einen Block warten. Mining Pools aggregieren viele Miner: Jeder liefert proportionalen Hashrate-Beitrag und erhält proportionalen Anteil der Block-Rewards — häufige kleine Auszahlungen statt seltener Volltreffer.

Größte Pools (2025): Foundry USA, AntPool, F2Pool, ViaBTC — zusammen über 60% der globalen Hashrate. Pool-Zentralisierung ist ein diskutiertes Risiko, da ein Pool theoretisch Transaktionen zensieren könnte. Die wirtschaftlichen Anreize sprechen dagegen: Wer zensiert, verliert Miner sofort an konkurrierende Pools.

### Mining-Ökonomie: Block-Subsidy und Halving

Miner verdienen zwei Einnahmeströme:

**Block Subsidy:** Neu erzeugte Bitcoin pro Block. Halbiert sich alle 210.000 Blöcke (~4 Jahre) im **Halving**:
- 2009: 50 BTC / Block
- 2012: 25 BTC
- 2016: 12,5 BTC
- 2020: 6,25 BTC
- 2024: 3,125 BTC
- ~2140: letzte Satoshi gemined — keine Subsidy mehr

**Transaktionsgebühren:** Jede Transaktion enthält eine Gebühr, die der Miner-des-Blocks einstreicht. Langfristig — wenn die Subsidy gegen null geht — müssen Gebühren allein die Mining-Profitabilität und damit die Netzwerksicherheit tragen. Das ist eine offene, wichtige Frage.

### Geographische Verteilung

Bis 2021 war China mit ~65% globaler Hashrate dominant. Das chinesische Mining-Verbot (Mai 2021) löste eine massive Migration aus — innerhalb weniger Monate verlagerten Miner ihre Hardware nach USA, Kasachstan, Russland, Kanada und Nordics. Bitcoin überlebte die Disruption ohne Unterbrechung: Die Schwierigkeitsanpassung kompensierte den Hashrate-Einbruch automatisch.

Heute (2025): USA dominiert mit ~35–40% (Texas als Zentrum), gefolgt von Nordics (Geothermie/Hydro), Kanada, VAE. Mining folgt günstiger Energie — das Protokoll erzwingt diese Dezentralisierung strukturell, weil kein Staat alle günstigen Energiequellen der Welt kontrolliert.

## Related

- [[bitcoin-mining-umwelt]] ← Vollständige Umwelt- und Energieevidenz (14 peer-reviewed Papers)
- [[bitcoin-whitepaper]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[transaktionsgebuehren-und-mempool]]
- [[hashcash]]

## Open Questions

- Wie entwickeln sich Mining-Anreize, wenn Block-Subsidy ausläuft — reichen Gebühren allein für ausreichende Netzwerksicherheit?
- Führt ASIC-Dominanz zur dauerhaften Mining-Zentralisierung, oder entstehen neue Dezentralisierungsmechanismen?
- Wie lange bleibt das 51%-Angriffs-Modell sicher bei fortschreitender Pool-Konzentration?
- Sind Alternativen zu Proof of Work (Proof of Stake, etc.) vergleichbar sicher — oder tauschen sie Energieaufwand gegen andere Schwachstellen?
