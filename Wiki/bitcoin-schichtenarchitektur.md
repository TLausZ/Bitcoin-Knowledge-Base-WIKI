# Bitcoin-Schichtenarchitektur und das Gall'sche Gesetz

**Status:** established
**Themen:** lightning
**Last updated:** 2026-06-22
**Sources:** [[aprycot-nur-die-staerksten-5-schichtenarchitektur]]

## Summary

Allen Farrington und Big Al argumentieren in Teil 5 von "Only the Strong Survive", dass Bitcoins mehrschichtige Architektur kein Notbehelf ist, sondern optimale Systemtechnik. Das Gall'sche Gesetz — kein komplexes System, das von Grund auf neu entworfen wurde, funktioniert jemals — erklärt sowohl Bitcoins Vorgehensweise (langsam wachsendes Fundament) als auch den Misserfolg von Kryptowährungen (Komplexität von Tag eins). Die heute als "DeFi-Versprechen" geltenden Eigenschaften werden nach Farrington bei Bitcoin schon bald auftauchen, und zwar auf einem belastbaren Fundament.

## Body

### Das Gall'sche Gesetz

John Gall formulierte: "Ein komplexes System, das funktioniert, hat sich ausnahmslos aus einem einfachen, funktionierenden System entwickelt." Der Umkehrschluss gilt ebenfalls: Ein komplexes System, das von Grund auf neu gebaut wurde, funktioniert nicht und kann nicht zum Funktionieren gebracht werden.

Ethereum und andere Kryptowährungen ignorierten diesen Grundsatz. Sie versuchten, Programmierbarkeit, Smart Contracts, Governance und Finanzinstrumente von Anfang an auf einer Ebene zu implementieren — und erkauften sich dadurch eine systemische Anfälligkeit, die an einem einzigen Punkt auftritt: wenn es wirklich darauf ankommt. Bitcoin bewegte sich langsamer und machte dabei nichts kaputt. Das ist eine Designentscheidung, kein Defizit.

### Die Schichten

**Lightning:** Zahlungskanäle auf der Bitcoin-Timechain. Zwei Parteien hinterlegen Bitcoin in einem Smart Contract und tauschen Off-Chain-Quittungen aus. Jede Partei kann den Kanal jederzeit "schließen", indem sie die neueste Quittung on-chain einreicht. Das Clever an der Weiterleitung: Quittungen können über mehrere Kanäle geroutet werden — Alice zahlt Bob, der Carol kennt, ohne dass Alice Carol einen Kanal öffnen muss.

Aus einer anderen Perspektive ist Lightning noch interessanter: Zahlungen sind Daten, die verschlüsselt über Onion-Routing weitergeleitet werden. Oder: Daten sind Zahlungen — Onion-Routing wird direkt monetarisiert (Sphinx Chat). Das löst ein klassisches Problem verteilter Systeme: Wer hat Anreiz, Infrastruktur für Datenschutz zu betreiben? Lightning bezahlt Routing-Nodes dafür automatisch. [[aprycot-nur-die-staerksten-5-schichtenarchitektur]]

**Liquid:** Eine Sidechain von Blockstream. Blockzeiten von einer Minute, Finalität nach zwei Bestätigungen. Liquid ermöglicht vertrauliche Transaktionen und die Ausgabe anderer Vermögenswerte (L-BTC = 1:1 mit BTC). Die Sidechain tauscht bewusst Dezentralisierung gegen Geschwindigkeit und Programmierbarkeit — ein Kompromiss, der für bestimmte Anwendungsfälle (professioneller Handel, Börsen) sinnvoll ist.

**Discrete Log Contracts (DLCs):** Ermöglichen beliebig definierte Verträge direkt auf der Bitcoin-Basisschicht. Ein oder mehrere Orakel bestätigen ein reales Ereignis (Sportresultat, Wechselkurs, Wetterdaten), und diese Bestätigung löst die Vertragserfüllung aus. DLCs benötigen keinen eigenen Token und kein Sidechain-Vertrauen.

**RGB:** Ein Versuch, Vermögensübertragungen und Finanzverträge aus dem globalen Konsens der Timechain herauszuhalten. Die Validierung geschieht clientseitig, nur zwischen den direkt beteiligten Parteien. Das Mining muss nur prüfen, ob eine Transaktion gültig ist — die semantische Last (was überträgt die Transaktion, unter welchen Bedingungen) liegt beim Empfänger.

**Stacks und RSK:** Stacks verankert Smart Contract-Ergebnisse in der Bitcoin-Blockchain und hat einen eigenen Token (STX). RSK ist Ethereum-kompatibel, nutzt R-BTC im 1:1-Verhältnis zu BTC und richtet sich an Entwickler, die Ethereum-Tools kennen.

### Schichtenarchitektur ist Technik-Philosophie

Das Gegenargument — "Das sind nur Umgehungen der Bitcoin-Limitierungen" — verwechselt Feature und Bug. TCP/IP, das für Videostreaming konfiguriert worden wäre, hätte nie funktioniert. Das Internet skalierte, weil jede Schicht genau eine Aufgabe macht und die anderen Schichten respektiert. Thibaud Maréchal: "Diese klare Spezialisierung stellt die Leistung, Zuverlässigkeit und Skalierbarkeit des Internets sicher." Dasselbe gilt für Bitcoin.

Alle Schichten in die Mainchain zu packen ist nicht nur technisch wahrscheinlich unmöglich — es wäre auch strukturell falsch. Unbekannte Angriffsvektoren entstehen durch unbeabsichtigte Interaktionen zwischen Teilsystemen. Deshalb ist "Nothing is systemically important" der richtige Maßstab: Wenn Lightning ausfällt, bleibt die Timechain intakt. Wenn ein DLC-Orakel versagt, betrifft das nur die Parteien des Vertrags. Das System als Ganzes kann nicht durch einen Schwachpunkt kollabieren.

### Das historische Vorbild

Das florentinische Kreditsystem des 15. Jahrhunderts kannte Zahlungskanäle avant la lettre: Kaufleute überwiesen Guthaben durch schriftliche Aufträge, die an Dritte und Vierte weitergegeben wurden — ohne Bargeld, ohne Bank als Intermediär. Gold diente der Endabrechnung, nicht der Zahlung. Bitcoin spielt dieselbe Rolle in einer globalen Version dieses Systems — nur mit unvergänglich überprüfbarer Endabrechnung statt des physischen Metalls.

### Das Pfeffer'sche Argument gegen Token

Jesse Pfeffer argumentierte, dass Nicht-Bitcoin-Token — selbst wenn sie technisch funktionieren — einer strukturellen Schwäche unterliegen: Sie haben eine praktisch unbegrenzte Umlaufgeschwindigkeit und eine vernachlässigbare Haltedauer, also keinen Grund, ihren Wert zu erhalten. Geld ist universeller Kredit; ein Casino-Token ist hochspezifischer Kredit. Auf dem Markt verliert hochspezifischer Kredit gegen universellen — solange die technologische Konkurrenz vergleichbar ist.

Für die meisten Krypto-Projekte gilt: Die Ideen sind nicht notwendigerweise schlecht. Die Architektur, die die aktuelle Umsetzung trägt, ist schlecht konzipiert. Das meiste davon lässt sich auf Bitcoin aufbauen — ohne eigenen Token, mit Bitcoin als universeller Abrechnungsschicht.

## Related

- [[lightning-netzwerk-grundlagen]]
- [[bitcoin-commons-und-governance]]
- [[bitcoin-vs-krypto]]
- [[segregated-witness-segwit]]
- [[bitcoin-covenants]]
- [[kapital-und-bitcoin]]

## Open Questions

- Welcher der Bitcoin-Layers (Lightning, Liquid, DLCs, RGB) hat bis 2026 die meiste Adoption erreicht?
- Wie verhält sich Stacks nach der PoX-Konsensänderung zu Bitcoins Sicherheitsmodell?
- Hat RGB genügend Traktion, um RSK oder Stacks langfristig zu verdrängen?
