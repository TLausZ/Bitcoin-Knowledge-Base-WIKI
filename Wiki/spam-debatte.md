# Die Spam-Debatte und das Scheitern von BIP-110

**Status:** emerging
**Themen:** protokoll, geschichte, philosophie
**Last updated:** 2026-08-18
**Sources:** [[BIP-110 Post Mortem]]

## Summary

Die «Spam»-Debatte dreht sich um die Frage, ob Bitcoin nicht-monetäre Daten in der Blockchain zulassen soll und mit welchen Mitteln man sie allenfalls zurückdrängt. Sie eskalierte 2026 zu [[bip-0110]], einem temporären Soft Fork, der arbiträre Daten auf Konsensebene begrenzen wollte. Im August 2026 scheiterte der Versuch: Die Miner-Signalisierung erreichte maximal 2,5 Prozent, die abgespaltene Kette kam über vier Blöcke nicht hinaus. Die einzige zusammenhängende Aufarbeitung im Korpus stammt von Jameson Lopp, der auf der Gegenseite stand; die Ereignisse sind belegt, die Wertungen sind seine.

## Body

### Was im August 2026 geschah

Der Ausgang laut Lopps Post Mortem vom 17. August 2026:

- Die Miner-Signalisierung für BIP-110 erreichte in der Spitze 2,5 Prozent. Die im BIP vorgesehene Schwelle lag bei 55 Prozent.
- OCEAN war der einzige Mining-Pool, der BIP-110 unterstützte, und machte es zur Standardvorlage seines Stratum-Templates.
- Bei Block 961'632 lief das Mandatory-Signaling-Fenster aus. Wer BIP-110-Code fuhr, fand sich damit auf einer eigenen Kette wieder.
- Auf dieser Kette entstanden insgesamt vier Blöcke, gemined von einer anonymen Gruppe namens «Roughnecks», in zwei Anläufen an zwei aufeinanderfolgenden Tagen. Danach stellte sie den Betrieb ein.
- Die Abspaltung dauerte nur wenige Stunden, weil die neuen Protokollregeln zu diesem Zeitpunkt noch nicht durchgesetzt wurden. Transaktionen der Bitcoin-Kette liessen sich deshalb auf der 110-Kette replayen.
- OCEAN entschädigte Miner, deren Hashrate auf die 110-Kette umgeleitet worden war.
- Nach dem Scheitern spaltete sich die Bewegung weiter auf. Ein Teil folgte Luke Dashjr auf einen Hard Fork, ein Teil kehrte zu Bitcoin zurück.

### Die Vorgeschichte in Etappen

Lopp zeichnet die Debatte von 2014 an nach. Die Etappen:

**2014.** OP_RETURN kommt mit Bitcoin Core 0.9 als Druckventil, nicht als Freigabe für Datenspeicherung. Vorher versteckten Protokolle beliebige Daten in Outputs, die ausgabefähig aussahen und das UTXO-Set dauerhaft aufblähten. Erlaubt waren zunächst rund 40 Bytes. Die Release Notes hielten fest, dass das Speichern arbiträrer Daten weiterhin unerwünscht sei.

**2014 bis 2015.** Counterparty und die «Bitcoin 2.0»-Protokolle legen die philosophische Bruchlinie offen. Reichte OP_RETURN nicht, kodierten sie ihre Daten über Multisig oder andere Transaktionsstrukturen. Daraus entstand die Frage, die bis heute trägt: Soll Policy nicht-monetäre Nutzung entmutigen, oder soll sie unvermeidbare Daten in die am wenigsten schädliche Form lenken?

**2015.** Core 0.11 hebt das Limit auf 80 Bytes. Parallel fluten «Stresstests» das Netzwerk mit wirtschaftlich belanglosen Transaktionen. Seither meint «Spam» zwei verwandte, aber verschiedene Dinge: das Ablegen arbiträrer Daten und jede geringwertige Nutzung, die um knappen Blockplatz konkurriert.

**2016 bis 2021.** Es bildet sich ein Kompromiss aus Gebühren und Policy. Der Konsens bleibt permissiv, die Standardness- und Relay-Regeln von Core weisen einzelne gültige Transaktionen ab. Der implizite Handel: Miner entscheiden, was in Blöcke kommt, Gebühren bepreisen die Knappheit, Relay-Policy dämpft Missbrauch, ohne den Konsens anzufassen. Diese Trennung von [[konsensregeln-und-mempool-richtlinien]] wird für jeden späteren Streit zentral.

**2017 und 2021.** SegWit gibt Witness-Bytes einen Gewichtsrabatt, Tapscript entfernt das alte Limit von 10'000 Bytes für Skriptgrössen. Beides war nicht auf Datenspeicherung angelegt: Der Witness-Rabatt sollte das Ungleichgewicht zwischen den Kosten fürs Erzeugen und fürs Ausgeben von UTXOs korrigieren. Zusammen machten [[segregated-witness-segwit]] und [[taproot-musig2-frost]] das Publizieren von Daten trotzdem billiger.

**2023.** Inscriptions kodieren Bilddaten in Taproot-Script-Path-Witnesses, verpackt in OP_FALSE-OP_IF-Hüllen. Grosse Bilder, Text und Token-Protokolle wie BRC-20 lassen sich damit vollständig on-chain ablegen und bleiben konsensgültig.

**2023 bis 2024.** Der Streit verschiebt sich zur Frage, ob Nodes Inscriptions filtern sollen. Luke Dashjr sieht darin eine Umgehung der Absicht hinter `-datacarriersize`; Bitcoin Knots setzt strengere Regeln um. Core filtert Inscriptions nicht breit, mit dem Gegenargument, dass entschlossene Nutzer direkt an Miner liefern oder ihre Daten anders verpacken.

**2025.** Die ursprüngliche OP_RETURN-Logik kehrt sich um. Core-Entwickler beobachten, dass das 83-Byte-Limit Protokolle wie Citrea zu schädlicheren Umwegen treibt, etwa zu dauerhaft unausgebbaren Outputs, die das UTXO-Set belasten. Antoine Poinsot schlägt vor, die Policy zu lockern, weil die Entmutigung nicht mehr wirke. Core 30 hebt den Default für `-datacarriersize` auf 100'000 Bytes und erlaubt mehrere OP_RETURN-Outputs; die alte Beschränkung bleibt konfigurierbar (siehe [[op-return-und-datenspeicherung]] und [[bitcoin-core-relay-statement]]).

**2026.** BIP-110 will die Datenkodierung auf Konsensebene beschränken.

Das wiederkehrende Muster über alle Etappen: Ein Datenkanal wird beschränkt, die Nutzer weichen auf einen anderen aus, und die Entwickler streiten, ob man weiter filtert oder den am wenigsten schädlichen Kanal öffnet.

### Warum die Aktivierung scheiterte

Lopps Erklärung ist ökonomisch, nicht technisch. Frühere strittige Forks hatten wirtschaftliches Gewicht hinter sich und scheiterten trotzdem: Bitcoin Cash mit Roger Ver und Jihan Wu samt dem grössten ASIC-Hersteller, Bitcoin SV mit Calvin Ayre. BIP-110 hatte nichts Vergleichbares. Die grösste beteiligte Firma war OCEAN, einer der kleinsten Pools der Branche, dessen Leitung die Beteiligung im Nachhinein als Privatmeinung einzelner Personen darstellte.

Dazu kommt der Unterschied im Angebot. Frühere Forks versprachen mehr Durchsatz, tiefere Gebühren oder zusätzliche Funktionalität. BIP-110 bot Reinheit und weniger Funktionalität, für Miner ausserdem weniger Gebühren.

Die Märkte zeigten dasselbe Bild. Fork-Futures, die 2017 das wirtschaftliche Interesse an grösseren Blöcken sichtbar gemacht hatten, kamen nicht zustande; Lopps öffentliches Angebot eines vertrauenslosen Kontrakts wurde als unmoralisches Glücksspiel abgelehnt. Der einzige laufende Prediction Market zu BIP-110 erreichte 4,6 BTC Gesamtvolumen, die Erfolgswahrscheinlichkeit blieb meist unter 20 Prozent.

### Die Argumente der Befürworter

Lopp listet über dreissig Argumente mit Belegen auf. Sie lassen sich in drei Gruppen fassen.

**Aktivierungsmechanik.** BIP-110 nutzt ein modifiziertes BIP-9-Verfahren ohne Timeout, mit 55-Prozent-Schwelle, maximaler Aktivierungshöhe und Mandatory-Signaling-Fenster. Der FAILED-Zustand ist nie erreichbar, das Lock-in also spätestens zur festgelegten Höhe erzwungen. In dieser Lesart ist Nicht-Signalisieren eine bestrafbare Handlung, weil enforcende Nodes solche Blöcke ablehnen.

**Spieltheorie.** Signalisieren koste operativ fast nichts, Nicht-Signalisieren dagegen im Ernstfall den ganzen Blockertrag; der Subsidy von 3,125 BTC wiege schwerer als der Gebührenstrom aus Inscriptions. Tiefe Signalisierung heute sage nichts aus, weil sie pro 2'016-Block-Periode gemessen wird; erwartet wurde eine späte Kaskade ab 30 bis 40 Prozent. Die Pool-Konzentration mache einen schnellen Umschwung plausibel.

**Zweck und Legitimation.** Bitcoin solle Geld sein, nicht Datenspeicher. Arbiträre Daten seien eine Externalität: Der Datennutzer zahle den Miner einmal, die Node-Betreiber tragen die laufende Last, was die Dezentralisierung und damit die Durchsetzung der Geldregeln schwäche. Die Massnahme sei temporär (52'416 Blöcke), ein Soft Fork, monetäre Anwendungsfälle blieben funktionsfähig, und eine Grandfather-Klausel schütze vor Aktivierung erzeugte UTXOs. Als Momentum galten das Wachstum der Knots-Nodes, der erste von OCEAN geminte Signalblock im März 2026 und ein Aktivierungs-Wahrscheinlichkeitsmodell, das zeitweise über 50 Prozent auswies.

Lopps Einwände dagegen: Node-Zahlen liessen sich trivial aufblähen, die Liste wirtschaftlich relevanter Unterstützer enthielt Einträge ohne Beleg, der Verweis auf den UASF von 2017 gehe fehl, weil BIP-148 nie ausgelöst wurde, sondern durch [[bip-0091]] entschärft worden war. Der Punkt «Nutzer definieren Bitcoin, nicht Miner» sei sachlich richtig und habe genau gegen BIP-110 gewirkt, weil die wirtschaftlich relevanten Akteure fehlten.

### Prognosen, die sich nicht hielten

Ursprünglich galt in der Anti-Spam-Position, Policy sei ausreichend und Konsensänderungen weder nötig noch hilfreich. Der «sub 1 sat per vbyte summer» 2025 widerlegte das aus Sicht Lopps: Nutzer umgingen die Standard-Mindestgebühr von 1 sat/vB schlicht, um zu sparen. Daraus entstand das Verständnis der «tolerant minority» in der Transaktionsweitergabe. Es braucht nicht zehn Prozent der Nodes mit lockerer Policy, um eine strengere Default-Policy wirkungslos zu machen; einige gut vernetzte Nodes genügen.

Auch die Warnungen vor Core v30 hielten nicht: Weder öffneten sich die «Schleusen», noch liess sich die grössere OP_RETURN-Kapazität nutzen, um Nodes zum Absturz zu bringen. Aus der Anti-v30-Bewegung wurde danach die Pro-BIP-110-Bewegung.

### Implementierungsprobleme

Der erste Release Candidate des BIP-110-Clients vom 10. Dezember 2025 hatte fehlschlagende Funktions- und Fuzz-Tests, Tests mit vorzeitigem Return sowie Binaries, die vor dem Signieren hochgeladen wurden. Core-Maintainer Michael Ford riet, einen späteren RC abzuwarten; Rob Hamilton hielt Konsensfehler für gut möglich.

Danach kamen weitere: ein Fund von l0rinc im Februar 2026; im Juni die Feststellung von Jonathan Bier, dass die Regeln zu OP_IF/OP_NOTIF in Tapscripts Adressen von Miniscript-Wallets nach Aktivierung unausgebbar machen können, während das Wallet des Clients solche Adressen weiterhin erzeugte; im Juli der Hinweis, dass das Einschalten der neuen Regeln bereits akzeptierte Blöcke nicht zwingend neu prüft. Zwei Wochen vor dem Mandatory Signaling fiel auf, dass die Implementierung eine undokumentierte achte Konsensregel enthielt.

### Der Nachweis der Wirkungslosigkeit

Drei Stunden nachdem Dathon Ohm das RDTS-BIP auf die Mailingliste gestellt hatte, bettete Peter Todd den vollständigen Text des BIP in eine Transaktion ein, die die vorgeschlagenen Beschränkungen einhielt. Andere legten grössere Daten über Wege ab, die die Beschränkungen gar nicht erst berühren, etwa ohne Taproot und ohne OP_RETURN. Mehrere der Protokolle, die BIP-110 vom Netzwerk fernhalten sollte, zeigten öffentlich, wie einfach sie ihre Methode anpassen. Das deckt sich mit dem Eingeständnis im BIP selbst, dass sich arbiträre Daten technisch nicht verhindern lassen, und mit Greg Maxwells Einwand, die Bewegung sei genau dann anti-Spam gewesen, wenn es rhetorisch passte.

### Der Ton der Auseinandersetzung

Die Debatte verlief mit erheblicher Schärfe auf beiden Seiten. Auf Befürworterseite verschob sich die Begründung im Verlauf von technischen Argumenten zu Rhetorik um Kindesmissbrauchsmaterial, bis hin zu Luke Dashjrs Bezeichnung von Bitcoin als «Bpedo» und zur Gleichsetzung von Gegnern mit Pädophilie-Apologeten. Lopps Entgegnung: Wer die Vergeblichkeit des Kampfs gegen arbiträre Daten in einem zensurresistenten Protokoll anerkennt, befürwortet damit so wenig deren Inhalte wie ein Befürworter des Waffenrechts Schulschiessereien. Lopp selbst schreibt durchgehend polemisch («Puritaner», «Delusion», Sammlung von Zitat-Belegen zur Blossstellung). Der Artikel hält beides fest, ohne die Wertungen zu übernehmen.

### Was die Debatte im Kern trennt

Lopp formuliert die Frage analog zum [[blocksize-war]]. Dort lautete sie, ob Bitcoin auf tiefe Transaktionskosten oder auf tiefe Validierungskosten hin optimiert werden soll. Für die Spam-Debatte schlägt er vor: Soll Bitcoin die Kosten des Transagierens und Validierens senken, indem es subjektiv missbilligte Nutzungen erschwert, oder soll es einen freien Markt für Blockplatz unabhängig vom Zweck anstreben?

Er hält die Prämisse selbst für falsch, weil nicht-monetäre Nutzung die Kosten nicht dauerhaft erhöhe. Hohe Gebührenphasen durch Datennutzung erwiesen sich als nicht tragfähig; für die Node-Last sind arbiträre Daten billiger zu verifizieren, weil der Node sie überspringt; die Speicherlast ist durch das Blockgrössenlimit gedeckelt, OP_RETURN erzeugt kleinere Blöcke und weniger UTXOs, und im schlechtesten Fall geht es um den Unterschied zwischen 2 und 4 MB pro Block bei fallenden Hardwarekosten. Diese Rechnung ist Lopps Position, keine unbestrittene Messung.

### Governance-Nachspiel

Während des Konflikts veröffentlichte der kalifornische Anwalt Asaf Fulks ein Rahmenwerk für Standards von Konsensänderungen (`consensus-change-standards`), an dem sich Vorschläge vergleichen lassen. Nach Lopps Einschätzung fällt BIP-110 darin klar durch. Als Lehren aus dem gescheiterten Fork nennt er: Ein Soft Fork lässt sich nicht herbeibluffen; ein UASF mit geringem Rückhalt braucht keinen «User Rejected Soft Fork» als Gegenmittel, um zu scheitern; und der Vorwurf der Pädophilie gegenüber Andersdenkenden baut keinen Konsens.

## Related

- [[bip-0110]]
- [[bitcoin-core-relay-statement]]
- [[op-return-und-datenspeicherung]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[blocksize-war]]
- [[soft-fork-und-hard-fork]]
- [[transaktionsgebuehren-und-mempool]]
- [[bitcoin-commons-und-governance]]

## Open Questions

- Die Darstellung stammt vollständig von einem Gegner des Vorschlags. Eine Aufarbeitung aus dem Befürworterlager fehlt im Korpus.
- Wie entwickelt sich der von Luke Dashjr angekündigte Hard Fork, und trifft Lopps Prognose zu, dass er ohne Börsenlistings und ohne Nachfrage bleibt?
- Setzt das Scheitern einen belastbaren Präzedenzfall gegen künftige inhaltsbezogene Konsensvorschläge, oder war es nur eine Frage des fehlenden wirtschaftlichen Gewichts?
- Bleibt die Frage der Node-Last durch Daten offen, solange sie niemand sauber quantifiziert hat?
