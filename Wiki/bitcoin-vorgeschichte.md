# Bitcoins Vorgeschichte: die 40 Jahre vor dem Whitepaper

**Status:** established
**Themen:** geschichte, philosophie, protokoll
**Last updated:** 2026-07-24
**Sources:** [[bitcoins-prehistory.jpeg]], [[aprycot-gladstein-die-suche-nach-digitalem-bargeld.md]], [[20081031_bitcoin-whitepaper.md]], [[19940910_The-Cyphernomicon.md]]

## Summary

Dan Helds Infografik «Bitcoin prehistory» ordnet rund 30 Vorläufer-Ereignisse zwischen 1974 und 2008 als Fischgräten-Diagramm an: Jede Rippe mündet in eine Zeitachse, die im Bitcoin-Logo endet. Die These steht im Untertitel: Bitcoin sei das Ergebnis von 40 Jahren Forschung, Entwicklung und Nachfrage. Die Auswahl trennt sauber zwischen kryptographischer Grundlagenforschung (1974–1985), der politischen Cypherpunk-Bewegung (1988–1994), gescheiterten zentralen Digitalwährungen (1989–2006) und den dezentralen Entwürfen, aus denen Satoshi direkt schöpfte (1997–2004). Sie enthält allerdings mehrere Tippfehler, eine falsche Jahreszahl beim Launch und lässt mit Haber und Stornetta ausgerechnet die im Whitepaper am häufigsten zitierte Arbeit weg.

## Body

### Was die Grafik ist

Erstellt von Dan Held (@danheld), inspiriert von Ansel Lindner (@anselLinder, @btcmrkts). Format: Ishikawa-/Fischgrätendiagramm, Zeitachse von −40 Jahren bis 2008, Einträge oberhalb und unterhalb der Achse. Eine Legende oder Quellenangabe zu den einzelnen Einträgen fehlt, die Grafik ist als Übersichtsposter gedacht, nicht als belegte Chronologie. [[bitcoins-prehistory.jpeg]]

Ihr Wert liegt in der Gleichzeitigkeit: Vier voneinander unabhängige Entwicklungslinien laufen über drei Jahrzehnte parallel und treffen erst 2008 aufeinander.

### Strang 1: kryptographische Grundlagen (1974–1985)

| Jahr | Eintrag der Grafik | Was es ist |
|---|---|---|
| 1974 | Cerf und Kahn, TCP/IP | «A Protocol for Packet Network Intercommunication» — das Transportnetz, ohne das kein P2P-Geld existieren kann |
| 1976 | Diffie und Hellman, «New Directions in Cryptography» | Public-Key-Kryptographie und Schlüsselaustausch ohne vorher geteiltes Geheimnis |
| 1978 | RSA | erstes praktikables Public-Key-Verfahren mit digitaler Signatur |
| 1980 | Ralph Merkle, «Protocols for Public Key Cryptosystems» | im Whitepaper als Referenz 7 zitiert, liefert die Merkle-Bäume |
| 1983 | David Chaum, «Blind Signatures for Untraceable Payments» | Signatur auf eine Nachricht, deren Inhalt der Signierende nicht sieht — Grundlage jedes anonymen E-Cash |
| 1985 | Elliptische-Kurven-Kryptographie | unabhängig von Koblitz und Miller vorgeschlagen, ab 2009 Bitcoins Signaturverfahren (secp256k1) |

Diese Linie liefert die Werkzeuge, nicht die Motivation. Siehe [[kryptografische-schlussel-und-adressen]], [[merkle-baeume]], [[elliptische-kurven-kryptographie]].

### Strang 2: die politische Bewegung (1988–1994)

Timothy C. Mays «The Crypto-Anarchist's Manifesto» (1988), die Gründung der Cypherpunks in der Bay Area 1992 durch Eric Hughes, Timothy C. May und John Gilmore, Hughes' «A Cypherpunk's Manifesto» (1993) und Mays «Cyphernomicon» (1994). Dazwischen Phil Zimmermanns PGP (1991), das Verschlüsselung erstmals aus der Behörden- und Universitätswelt in die Hände von Privatpersonen brachte. Hal Finney, später Empfänger der ersten Bitcoin-Transaktion, arbeitete an PGP mit. [[aprycot-gladstein-die-suche-nach-digitalem-bargeld.md]]

Die Grafik schreibt hier «Cyberpunks founded in SF» — gemeint sind die Cypherpunks. Ausführlich in [[kryptoanarchismus-und-cypherpunks]] und [[cypherpunk-manifest]].

### Strang 3: die Nachfrageseite, zentral gebaut und gescheitert (1989–2006)

Das ist der Teil, den der Untertitel mit «demand» meint. Chaum zog 1989 nach Amsterdam und gründete Digicash; eCash erlaubte, Bankguthaben in nicht überwachbare Token zu tauschen. Die Firma ging Ende der 1990er bankrott. Daneben CyberCash (1994), e-gold (1996), die Retailer-Währungen der Dotcom-Blase (Beenz, Flooz, 1998–2001), Ingame-Währungen und -Märkte ab 2001, Liberty Reserve (2006).

Gladstein zieht daraus die Lektion, die Adam Back und andere aus Digicash mitnahmen: Digitales Bargeld muss dezentral sein, ohne zentralen Angriffspunkt. Zentrales Digitalgeld kann im Betrieb scheitern, unter Aufsicht geraten oder pleitegehen; die grösste Schwäche ist die Geldausgabe durch eine vertrauenswürdige Drittpartei. Jeder Eintrag dieser Zeile ist ein Beleg dafür — e-gold und Liberty Reserve wurden von Behörden abgeschaltet, Beenz und Flooz verschwanden mit ihren Betreibern. Chaums Verfahren und die politische Bargeld-Argumentation dahinter in [[digitales-bargeld-und-ecash]]. [[aprycot-gladstein-die-suche-nach-digitalem-bargeld.md]]

### Strang 4: die dezentralen Entwürfe (1997–2004)

- **1996, NSA, «How To Make a Mint: The Cryptography of Anonymous Electronic Cash»** — eine Behörde beschreibt die Bauteile anonymen Digitalgelds, bevor jemand sie zusammensetzt.
- **1997, Adam Back, Hashcash** — Proof-of-Work als Anti-Spam-Massnahme. Backs eigene Schwachstelle: In einer Währung könnten schnellere Rechner Hyperinflation erzeugen. Genau diese Lücke schliesst Satoshi mit der Schwierigkeitsanpassung. [[hashcash]]
- **1997, Nick Szabo, «Formalizing and Securing Relationships on Public Networks»** — Smart Contracts als Vertragslogik ohne Vollstrecker.
- **1998, Wei Dai, B-money** — anonymes verteiltes Geldsystem, in dem nicht rückverfolgbare Pseudonyme Verträge untereinander durchsetzen. Referenz 1 im Whitepaper.
- **1998, Nick Szabo, «Secure Property Titles with Owner Authority»** und **Bit Gold** — Eigentumsregister ohne zentrale Autorität, plus die Idee, die nachweisbare Kostspieligkeit von Gold digital nachzubilden. Bit Gold wurde nie implementiert.
- **2004, Hal Finney, Reusable Proof-of-Work (RPOW)** — Bit-Gold-Token, die weitergereicht werden können. Finney betrieb den Verifikationsserver selbst und wollte ihn später dezentralisieren, kam aber nicht dazu. [[aprycot-gladstein-die-suche-nach-digitalem-bargeld.md]]

### Strang 5: P2P-Infrastruktur (2001)

Bram Cohens BitTorrent und die verteilten Hashtabellen (Chord, Pastry, CAN, Tapestry, alle 2001) zeigten, dass grosse Netze ohne Server auskommen und Angriffe auf einzelne Knoten überleben. Ohne diesen Nachweis wäre Bitcoins Gossip-Netz eine unbelegte Behauptung gewesen. [[bitcoin-netzwerk-und-nodes]]

### Was die Grafik auslässt

Das Bitcoin-Whitepaper zitiert acht Arbeiten. Drei davon stammen von Stuart Haber und W. Scott Stornetta zum kryptographischen Zeitstempeln (1991, 1993, 1997), dazu Massias, Avila und Quisquater (1999) zum Zeitstempeldienst mit minimalen Vertrauensannahmen. Keine dieser vier Referenzen taucht in der Grafik auf, obwohl Haber und Stornetta der meistzitierte Strang des Papiers sind und Bitcoin im Kern ein verteilter Zeitstempel-Server ist. Diese Linie ist in [[digitales-zeitstempel]] ausgearbeitet. [[20081031_bitcoin-whitepaper.md]]

Ebenfalls nicht vertreten: Dwork und Naor (1992), die das Proof-of-Work-Prinzip fünf Jahre vor Hashcash für Spam-Abwehr formulierten, und Szabos «Trusted third parties are security holes» (2001), die kürzeste Zusammenfassung der ganzen Strang-3-Erfahrung.

### Fehler und Ungenauigkeiten

| In der Grafik | Korrekt |
|---|---|
| «A Protocol for **Pocket** Network Intercommunication» | Packet Network Intercommunication |
| «Securing Property Titles with Owner Authority» | Secure Property Titles with Owner Authority |
| «**Cyber**punks founded in SF» | Cypherpunks |
| «**Tmothy** C. May», «**Eliptic** Curve», «Phil Zimmerman» | Timothy, Elliptic, Zimmermann |
| «Beenz, **Floor**» | Beenz, Flooz |
| «2008 Bitcoin Launched» | Whitepaper 31.10.2008, Netzstart Genesis-Block 03.01.2009, Block 1 am 09.01.2009 |
| «1998 Bit-gold» | Idee 1998, öffentlich ausformuliert erst 2005 im Szabo-Blog |

Die Launch-Angabe ist die einzige inhaltlich relevante: Sie verkürzt die Vorgeschichte um die zwei Monate zwischen Veröffentlichung und laufendem Netz, in denen sich zeigte, dass niemand ausser Satoshi und Finney das Ding überhaupt starten wollte. Zeitleiste in [[bitcoin-launch-januar-2009]].

### Warum 2008 und nicht 1998

Alle Bausteine lagen 1998 auf dem Tisch: Public-Key-Kryptographie, Merkle-Bäume, Blindsignaturen, Proof-of-Work, das Konzept eines pseudonymen Geldnetzes bei Dai, die Härtegeld-Idee bei Szabo. Was fehlte, war der Mechanismus, der eine Ausgabe-Regel ohne Prägeanstalt durchsetzt. Backs Hashcash hatte kein Gegengewicht gegen schnellere Hardware, Szabos Bit Gold blieb Entwurf, Finneys RPOW hing an einem Server.

Satoshi kombinierte die Kette von Proof-of-Work-Blöcken als Zeitstempel mit einer alle 2016 Blöcke greifenden Schwierigkeitsanpassung. Damit wird Rechenleistung zur Ausgabe-Bremse statt zum Inflationstreiber, und die Frage «welche Historie gilt» beantwortet sich über akkumulierte Arbeit statt über eine Instanz. Adam Back hielt genau diese Anpassung für den wissenschaftlichen Durchbruch. [[aprycot-gladstein-die-suche-nach-digitalem-bargeld.md]]

Gladsteins Fazit zur Rollenverteilung: Nakamoto nutzte die Grundlagen von Diffie, Chaum, Back, Dai, Szabo und Finney und erfand daraus dezentrales digitales Bargeld. Der zweite Teil des Satzes ist der, den die Grafik mit ihrer Fischgräten-Form unterschlägt: Die Rippen erklären, was verfügbar war, nicht warum es 30 Jahre lang nicht funktionierte.

## Related

- [[bitcoin-fruehgeschichte]]
- [[bitcoin-launch-januar-2009]]
- [[kryptoanarchismus-und-cypherpunks]]
- [[cypherpunk-manifest]]
- [[digitales-bargeld-und-ecash]]
- [[digitales-zeitstempel]]
- [[hashcash]]
- [[merkle-baeume]]
- [[elliptische-kurven-kryptographie]]
- [[bitcoin-whitepaper]]
- [[szabo-geldursprung]]
- [[bitcoin-mining-und-proof-of-work]]

## Open Questions

- Warum fehlen Haber und Stornetta in praktisch allen populären Vorgeschichts-Darstellungen, obwohl das Whitepaper sie dreimal zitiert? Vermutlich weil Zeitstempeln unpolitisch klingt und sich schlecht in die Cypherpunk-Erzählung fügt.
- Die Grafik ist undatiert. Der Screenshot stammt aus einer Zeit, in der Held aktiv Bitcoin-Geschichte publizierte (2018–2020), ein Erstveröffentlichungsdatum liess sich aus der Datei nicht ermitteln.
- Lässt sich «40 Jahre Nachfrage» belegen? Die zentralen Digitalwährungen der Strang-3-Zeile hatten Millionen Nutzer, aber Zahlen dazu fehlen in der KB.
