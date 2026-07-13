# Bitcoin-Whitepaper: Errata und Abweichungen

**Status:** established
**Last updated:** 2026-07-13
**Sources:** [[bitcoin-paper-errata-and-details.md]]

## Summary

David A. Hardings Errata-Dokument (Gist, CC0, laufend gepflegt) sammelt die bekannten Fehler des Bitcoin-Whitepapers, die Terminologie-Verschiebungen seit 2008 und die Stellen, an denen die Implementierung vom Paper abweicht. Der Befund: Satoshi lag bei mindestens vier Annahmen nachweislich daneben — der Finney-Attacke, der Sicherheitsschwelle (Selfish Mining), dem Merkle-Pruning und den SPV-Alerts. Keiner dieser Fehler brach das System, weil Code, Forschung und Community die Lücken fanden und korrigierten. Das Dokument ist damit doppelt wertvoll: als technische Referenz und als Beleg, dass Bitcoins Stärke aus offener Selbstkritik kommt, nicht aus der Unfehlbarkeit seines Gründers.

## Body

### Was das Dokument ist

Harding, langjähriger Bitcoin-Dokumentar und Optech-Mitautor, betont im Disclaimer, dass er keines der Probleme selbst entdeckt hat — er hat sie nur an einem Ort gesammelt. Das Dokument lebt: Die Updates-Sektion kreditiert Beiträge von Gregory Maxwell, Kalle Rosenbaum, Chris Belcher und Mark «Murch» Erhardt; die Kommentarspalte hat weitere Punkte beigesteuert, die noch nicht eingearbeitet sind. Die Lizenz ist CC0, das Whitepaper selbst bleibt unangetastet — die Errata leben daneben, wie es in der wissenschaftlichen Literatur üblich ist.

### Widerlegte Annahmen

Vier Aussagen des Papers haben sich als falsch erwiesen:

**Die Finney-Attacke (Kapitel 11).** Das Paper behauptet, ein Empfänger schütze sich vor vorbereiteten Blockketten, indem er seinen Public Key erst kurz vor der Signatur herausgibt. Hal Finney widerlegte das früh: Ein Miner mined gelegentlich Blöcke mit einer Transaktion von seiner Adresse A zu seiner Adresse B, hält den gefundenen Block zurück, bezahlt im Laden von A an die Händler-Adresse C und broadcastet den Block danach — seine A→B-Transaktion verdrängt die Zahlung an den Händler. Die späte Schlüsselübergabe verhindert davon nichts. Die Attacke funktioniert gegen Zero-Confirmation-Zahlungen und trägt bis heute Finneys Namen.

**Selfish Mining (Abstract).** «Solange eine Mehrheit der CPU-Power ehrlich ist» — die reale Schwelle liegt tiefer. Wer einen Block findet, kann sofort am Nachfolger arbeiten, während alle anderen auf die Propagation warten. Diesen strukturellen Vorsprung kann ein Angreifer mit rund 30% der Hashrate ausnutzen, um andere Miner unprofitabel zu machen und sie womöglich in seine Policy zu zwingen. Die korrekte Formulierung wäre laut Harding: sicher, solange kooperierende Angreifer unter etwa 30% bleiben.

**Merkle-Pruning (Kapitel 7).** Das Paper verspricht, ausgegebene Transaktionen liessen sich nach genügend Bestätigungen verwerfen, um Speicherplatz zu sparen. Es gibt aber keinen Weg zu beweisen, dass eine Transaktion *nicht* ausgegeben wurde, ausser alle nachfolgenden Daten zu verarbeiten — neue Nodes müssen weiterhin die ganze Historie validieren. Der Kommentator andronoob verschärft den Punkt: Ein Merkle-Proof beweist Inklusion, nicht Gültigkeit. Hätten alle Nodes die Historie gepruned, wäre eine Transaktion, die nie existierende Coins ausgibt (Inflation aus dem Nichts), nicht mehr von einer gültigen zu unterscheiden. Das ist das stärkste Argument für vollständige Archive Nodes.

**SPV-Alerts (Kapitel 8).** Das Paper skizziert, dass Full Nodes SPV-Clients vor ungültigen Blöcken warnen könnten. Keine der existierenden SPV-Implementierungen hat solche Alerts je umgesetzt — was Guthaben in SPV-Wallets in der Vergangenheit real gefährdet hat.

### Stille Korrekturen im Code

Zwei Abweichungen zeigen, dass auch die Implementierung nachgebessert werden musste:

**Longest chain → most-work chain.** Bis Juli 2010 wählte der Code tatsächlich die längste Kette (`nHeight`), nicht die mit der meisten Arbeit (`bnChainWork`). Da die Proof-of-Work-Menge pro Block variiert, war das angreifbar: Eine lange Kette billiger Blöcke hätte eine kurze Kette teurer Blöcke schlagen können. Der Commit ist im Errata-Dokument verlinkt (Archäologie: Gregory Maxwell). Details zur Metrik in [[bitcoin-chainwork]].

**Difficulty-Anpassung.** Das Paper spricht von einem Moving Average mit Stundenziel. Implementiert ist etwas anderes: Alle 2.016 Blöcke wird die gemeldete Erzeugungszeit mit einem früheren Block verglichen, Zielgrösse zwei Wochen, Anpassung pro Periode auf Faktor 4 nach oben und 75% nach unten begrenzt. Sergio Demian Lerner ergänzt in den Kommentaren: Im Pre-Release-Code zählte das nBits-Feld noch echte führende Nullbits (wie bei Hashcash); erst das erste Release wechselte auf die Integer-Vergleichs-Logik, die fraktionale Difficulty erlaubt. Auch ExtraNonce-Rolling kam erst mit dem Launch dazu. Siehe [[mining-schwierigkeit]].

### Präzisierte Konzepte

**«Chain of digital signatures» → DAG of encumbrances.** Bitcoin verallgemeinert das Signatur-Modell: Ausgebbar ist, was einen deterministischen Ausdruck erfüllt («encumbrance»), nicht nur, was eine Signatur trägt. Und weil Transaktionen mehrere Inputs und Outputs haben, ist die Struktur keine Kette, sondern ein gerichteter azyklischer Graph (Murch). andronoobs Einwand präzisiert die Grenze: Ohne Signatur, die die Outputs abdeckt, wäre eine Transaktion auf dem Weg zum Miner manipulierbar — deshalb war das ursprüngliche Pay-to-Hash nutzlos, bis es als P2SH neu definiert wurde, und deshalb braucht es für ausgabebeschränkte Coins [[bitcoin-covenants]].

**«One-CPU-one-vote» ist keine Regel-Abstimmung.** Die Stimme gilt nur der Transaktionsreihenfolge, nicht den Systemregeln — das Paper selbst stellt das in Kapitel 11 klar (ein Mehrheits-Angreifer kann keine Coins aus dem Nichts schaffen, weil Nodes ungültige Blöcke verwerfen). LarryRuane führt in den Kommentaren aus, warum die Big-Blocker-Lesart der Schlusszeilen («nodes vote with their CPU power») fehlgeht: Miner wählen nur zwischen gültigen Ketten; was gültig ist, definieren die validierenden Nodes der ökonomischen Mehrheit. Ein 99%-«Votum» der Miner für eine Kette ist Abbild dieser Mehrheit, nicht ihre Ursache. Das ist rückblickend die Kernlektion des [[blocksize-war]].

**«Nodes» ≠ Miner.** 2008 meinte «node» einen mining-fähigen Vollknoten (Mining war ein Menüpunkt im GUI). Heute sind fast alle Nodes keine Miner, und viele Miner validieren nicht selbst. Die frühen Paper-Kapitel meinen mit «nodes» Miner mit Full Validation; die späteren («network nodes») meinen Validierung ohne Mining.

**Multi-Input-Privacy und CoinJoin.** Das Paper hält die Verknüpfung von Inputs desselben Eigentümers für «unavoidable». Chris Belchers Einwand: Mehrere Eigentümer können kooperativ eine Transaktion mit Inputs von allen bauen — von aussen nicht unterscheidbar. Genau darauf baut [[coinjoin-und-on-chain-privatsphaere]] auf. Eine der wenigen Stellen, an denen die Realität *besser* wurde als Satoshis Erwartung.

### Warum das Dokument in dieses Wiki gehört

Die Errata-Sammlung ist gelebte Selbstkritik: Fehler des Gründungsdokuments werden öffentlich dokumentiert, kreditiert und weiterdiskutiert, statt wegerklärt zu werden. Jeder der vier harten Fehler wurde durch die Community gefunden und durch Code (most-work chain), Betriebspraxis (Confirmations statt Zero-Conf), Forschung (Selfish-Mining-Papers) oder neue Protokolle (CoinJoin) adressiert. Wer das Whitepaper als heilige Schrift liest, versteht Bitcoin schlechter als jemand, der diese Errata daneben legt — die Robustheit liegt im Korrekturprozess, nicht im Ursprungstext. Das ergänzt [[bitcoin-whitepaper]] (Inhalt des Papers) und [[bitcoin-fehlannahmen]] (externe Fehlannahmen) um die dritte Kategorie: interne, eingestandene Fehler.

## Related

- [[bitcoin-whitepaper]]
- [[bitcoin-fehlannahmen]]
- [[blocksize-war]]
- [[bitcoin-covenants]]
- [[bitcoin-mining-und-proof-of-work]]
- [[mining-schwierigkeit]]
- [[bitcoin-chainwork]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[merkle-baeume]]
- [[bitcoin-netzwerk-und-nodes]]
- [[satoshi-zitate]]

## Open Questions

- marrukins Kommentar zur Difficulty-Berechnung (Summe der 2.016 Blockzeiten vs. 20.160 Minuten) blieb im Gist unbeantwortet; der bekannte Off-by-one-Bug (nur 2.015 Intervalle werden gemessen) fehlt im Dokument ganz.
- garlonicons Hinweis auf die Median-Time-Past-Regel (11 Blöcke) als Quasi-Moving-Average und die Timestamp-Attacken in Testnets — wie weit relativiert das Hardings «a moving average is not used»?
- «CoinJoin in use since 2015» ist konservativ datiert; die Idee stammt von Maxwell 2013. Lohnt ein Abgleich mit der Chronologie in [[coinjoin-und-on-chain-privatsphaere]]?
- andronoobs «empty block attack»-Szenario (ein übermächtiger Angreifer erstickt die Chain mit leeren Blöcken): Wo ist die beste aktuelle Analyse dazu — und gehört sie als eigener Abschnitt in [[bitcoin-regierungsresistenz]]?
