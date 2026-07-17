# Bitcoin Whitepaper

**Status:** established
**Themen:** grundlagen, protokoll, privacy, geschichte, satoshi
**Last updated:** 2026-06-22
**Sources:** [[20081031_bitcoin-whitepaper]], [[aprycot-strolight-whitepaper-schwieriger-teil]]

## Summary

Satoshi Nakamotos neun Seiten vom 31. Oktober 2008 definierten ein elektronisches Peer-to-Peer-Zahlungssystem ohne vertrauenswürdige Drittpartei. Das Kernproblem — Double-Spending ohne zentrale Autorität zu verhindern — löst Nakamoto mit einem dezentralen Timestamp-Server, der Transaktionen durch Proof-of-Work in einer unveränderlichen Kette verankert. Das Whitepaper hat 12 Abschnitte und beschreibt präzise: UTXO-basierte Transaktionen, den Merkle-Tree-basierten Disk-Space-Mechanismus, den Incentive-Mechanismus für Miner, Simplified Payment Verification (SPV) und ein pseudonymes Privatsphäre-Modell. Kein Dokument der Computergeschichte hat mit so wenig Text so viel ausgelöst.

## Body

### Kontext: Oktober 2008

Das Whitepaper erschien am 31. Oktober 2008 auf der Cryptography Mailing List — sechs Wochen nach dem Zusammenbruch von Lehman Brothers, mitten in der schlimmsten Finanzkrise seit 1929. Das Timing war kein Zufall. Die erste Reaktion auf der Mailingliste war überwiegend skeptisch: Skalierungsprobleme, energiebedarf, das Prisoner's Dilemma bei Miner-Anreizen. Satoshi Nakamoto — ein Pseudonym, das keine reale Identität kannte — antwortete geduldig auf Einwände. Am 3. Januar 2009 wurde der Genesis Block gemined.

Die Coinbase-Transaktion des Genesis Blocks enthielt: *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"* — ein Timestamp und politisches Statement in einem.

**Kontext in der Cypherpunk-Tradition:** Nakamoto baute auf früheren Arbeiten auf, die im Whitepaper zitiert werden:
- **Hashcash** (Adam Back, 1997): Proof-of-Work-System gegen E-Mail-Spam; wird im Whitepaper für Mining verwendet
- **b-money** (Wei Dai, 1998): Dezentrales Geld-Konzept ohne zentrale Behörde
- **Merkle Trees** (Ralph Merkle, 1979): Effiziente kryptografische Verifikation grosser Datensätze
- Die **Kryptografie-Mailingliste** selbst: Das intellektuelle Heimatplanet der Cypherpunks, die seit den 1980ern an digitalem Privatgeld arbeiteten

### Die 12 Abschnitte des Whitepapers

Das Whitepaper ist ungewöhnlich kompakt — 9 Seiten, 12 Abschnitte, kein Padding.

**1. Introduction:** Das Problem ist benannt. Trusted Third Parties (Banken, PayPal, Visa) sind ein systemisches Risiko, nicht bloss eine Unannehmlichkeit. Rückbuchungen, Transaktionskosten und Zensurierbarkeit sind Konsequenzen der Architektur, nicht von schlechtem Management. Lösung: kryptografischer Beweis statt Vertrauen.

**2. Transactions:** Eine Münze ist eine Kette digitaler Signaturen. Jeder Eigentümer signiert den Hash der vorherigen Transaktion zusammen mit dem öffentlichen Schlüssel des Empfängers. Das ermöglicht Verifikation ohne Drittpartei — das Doppelausgabeproblem bleibt aber noch ungelöst.

**3. Timestamp Server:** Um Double-Spending zu verhindern, müssen Transaktionen öffentlich bekannt sein und in einer bestimmten Reihenfolge existieren. Ein Hash des vorherigen Blocks in jedem Block schafft eine unveränderliche Zeitordnung: Man kann keinen Block der Vergangenheit ändern, ohne alle Nachfolgeblöcke neu zu berechnen.

**4. Proof-of-Work:** Hier adaptiert Nakamoto Hashcash. Nodes suchen eine Nonce, sodass der Block-Hash mit einer bestimmten Anzahl führender Nullbits beginnt. Der Rechenaufwand macht rückwirkende Manipulation prohibitiv teuer. Die Schwierigkeit passt sich alle 2016 Blöcke an.

**5. Network:** Das Bitcoin-Netzwerk ist vollständig dezentral und permissionslos: Nodes können jederzeit beitreten oder das Netzwerk verlassen. Sie akzeptieren immer den längsten Chain (die meiste investierte Arbeit). Bei gleichzeitig gefundenen Blöcken hält jeder Node den ersten, den er sieht — der nächste Block löst den Konflikt auf.

**6. Incentive:** Der Block-Reward löst zwei Probleme zugleich: Er verteilt initiale Bitcoin ohne zentrale Behörde, und er gibt Minern einen Anreiz, ehrlich zu handeln. Nakamoto vergleicht es mit Gold-Mining: CPU-Zeit und Energie werden gegen neue Coins getauscht. Langfristig ersetzt der Incentive durch Transaktionsgebühren die schwindende Block-Subsidy.

**7. Reclaiming Disk Space:** Eine der elegantesten Lösungen des Whitepapers. Ohne Komprimierung wächst die Blockchain unbegrenzt. Nakamoto löst es mit **Merkle Trees**: Transaktionen in einem Block werden zu einem Merkle-Root komprimiert. Alte Transaktionen können gelöscht werden — nur der Merkle-Root bleibt im Block-Header erhalten. Die Integrität bleibt beweisbar, der Disk-Space-Bedarf wächst linear, nicht exponentiell.

**8. Simplified Payment Verification (SPV):** Full Nodes verifizieren alles, brauchen aber die vollständige Blockchain. SPV-Clients — z.B. mobile Wallets — laden nur Block-Header und fragen gezielt nach dem Merkle-Ast ihrer eigenen Transaktionen. Sicher, solange ehrliche Nodes die Mehrheit der Hashrate kontrollieren; anfälliger bei Netzwerkangriffen als Full Nodes.

**9. Combining and Splitting Value:** Bitcoin ist keine Münze pro Transaktion — das UTXO-Modell erlaubt beliebig viele Inputs und Outputs. Man kann mehrere kleine UTXOs zusammenfassen (Consolidation) oder einen grossen in Wechselgeld aufteilen. Das macht Bitcoin flexibel ohne Account-Modell.

**10. Privacy:** Das traditionelle Banken-Modell schützt Privatsphäre durch Zugangsbeschränkung zu Transaktionsdaten. Bitcoin ist das Gegenteil: alle Transaktionen sind öffentlich. Der Schutz entsteht durch Pseudonymität — öffentliche Schlüssel sind nicht mit Identitäten verknüpft. Nakamoto empfiehlt, für jede Transaktion ein neues Schlüsselpaar zu verwenden. *Limitation:* Multi-Input-Transaktionen enthüllen, dass die Inputs dem gleichen Besitzer gehören.

**11. Calculations:** Der formale Beweis, warum ein Angreifer mit weniger als 50% Hashrate exponentiell kleiner werdende Chancen hat, einen längeren Chain zu bauen. Nakamoto modelliert es als Binomial Random Walk / Gambler's Ruin Problem. Für praktische Sicherheit reichen in den meisten Szenarien 6 Bestätigungen.

Tomer Strolight hat die konkreten Zahlen aus Abschnitt 11 zugänglich aufbereitet: Ein Angreifer mit 10% Hashrate hat nach 6 Blöcken (~1 Stunde) nur eine Erfolgswahrscheinlichkeit von 0,02% — also etwa 1 zu 5000. Das Angreifen des Netzwerks ist damit 500-mal schwieriger als das ehrliche Weiterminern. Bei 30% Hashrate und 30 Blöcken (~5 Stunden) sinkt die Chance auf 0,015% (1 zu 2000). Selbst bei 45% Hashrate bräuchte ein Angreifer 340 Blöcke Tiefe (~2,5 Tage), um die 1-zu-1000-Schwelle zu unterschreiten.

Satoshis Lösung schliesst Doppelausgaben nicht aus — sie macht sie mit jedem bestätigten Block exponentiell unwahrscheinlicher und teuer: Der Angreifer verzichtet auf seine anteilige Blockbelohnung, während er einen erfolglosen Angriff durchführt. Das Konstruktionsprinzip: nicht Perfektion, sondern hinreichende Unwahrscheinlichkeit auf Dauer. [[aprycot-strolight-whitepaper-schwieriger-teil]]

**12. Conclusion:** Das Whitepaper endet mit dem Kern-Statement: Bitcoin ist ein System für elektronische Transaktionen ohne Vertrauen — basierend auf kryptografischem Beweis.

### Was das Whitepaper nicht beschreibt

Das Whitepaper ist kein Entwicklungshandbuch — es skizziert das Konzept. Vieles wurde erst später durch Implementierung und BIPs konkretisiert oder verändert:

- **Skript-System:** Das UTXO-Skript-System (welches P2PK, P2PKH, Multisig ermöglicht) ist im Whitepaper nicht beschrieben
- **Mining Pools:** Nicht vorhergesehen; entstanden 2010 durch Slush Pool
- **Wallets und Schlüsselverwaltung:** HD Wallets (BIP 32), BIP 39 Seedphrasen — alles spätere Entwicklungen
- **Skalierung:** Block-Size-Debatte und SegWit-Lösung sind Reaktionen auf nicht vorhergesehene Wachstumsprobleme
- **Smart Contracts:** Bitcoin Script ist absichtlich begrenzt; Turing-vollständige Contracts wurden nicht angestrebt

### Satoshi Nakamotos Abgang

Nakamoto war von 2008 bis April 2011 aktiv — in Mailinglisten, im Bitcoin Forum, per E-Mail. Die letzte bekannte Nachricht war an Gavin Andresen: *"I've moved on to other things."* Danach verschwand Nakamoto vollständig.

Die Identität ist bis heute unbekannt. Bekannte Fakten: Nakamoto schrieb fehlerfreies Englisch in britischer Orthographie, arbeitete in europäischen Zeitzonen und hatte tiefes Wissen in Kryptografie, Wirtschaft, Programmierung und verteilten Systemen. Die erste Bitcoin-Adresse (Genesis Block) enthält ~50 BTC, die noch nie bewegt wurden.

## Related

- [[satoshi-ankuendigung-2009]]
- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[utxo-modell-und-konsolidierung]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[hashcash]]
- [[segregated-witness-segwit]]
- [[bitcoin-fehlannahmen]]
- [[bitcoin-whitepaper-errata]] ← bekannte Fehler des Papers, Terminologie-Drift, Implementierungs-Abweichungen

- [[das-buch-satoshis|Das Buch Satoshis (Phil Champagne)]] ← Buch

## Open Questions

- Wer ist Satoshi Nakamoto — und würde es eine Rolle spielen, wenn es bekannt würde?
- Wie lange bleibt das 51%-Angriffs-Modell sicher bei sinkendem Block-Reward und wachsender Pool-Konzentration?
- Deckt SPV in der Praxis noch die Sicherheitsannahmen des Whitepapers ab, oder ist es de facto schwächer?
- Wurden die ~50 BTC der Genesis-Block-Adresse absichtlich gesperrt (unmined coinbase ist nicht spendbar), oder war das ein Nebeneffekt?
