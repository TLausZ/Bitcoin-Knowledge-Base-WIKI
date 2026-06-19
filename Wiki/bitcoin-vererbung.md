# Bitcoin Vererbung

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[Bitcoins verwahren und vererben_ Ein praktischer Ratgeber -- Marc Steiner -- 1_ Auflage, Rheinfelden, 2020 -- Held, Stefan & Fabio Tröndle GbR_ -- isbn13 9783949098017 -- 6ba03ea3dd3602e370eb518e8ae1af9c -- Anna's Archive.pdf]]

## Summary

Bitcoin-Vererbung ist ein gelöstes Problem, das die meisten Nutzer ignorieren — bis es zu spät ist. Da Bitcoin in echter Selbstverwahrung ausschließlich über den privaten Schlüssel (Seedphrase) kontrollierbar ist, geht er beim Tod des Inhabers unwiderruflich verloren, wenn kein Erbe den Zugang kennt. Marc Steiners Buch (2020) bietet den vollständigsten deutschsprachigen Rahmen: Nachlassplan-Erstellung, acht konkrete Musterabläufe von einfach bis kryptografisch komplex, rechtliche Absicherung und eine separat beigefügte Erben-Kurzanleitung.

## Body

### Das fundamentale Problem

Bitcoin hat keine Kundenhotline, kein Passwort-Reset, keinen Kundendienst. Getätigte Transaktionen lassen sich nicht abfangen. Sind sie einmal in der Blockchain bestätigt, ist der Zug abgefahren — und dasselbe gilt für verlorene Schlüssel.

Jonas Schnelli, Bitcoin Core Developer, formuliert es im Vorwort zu Steiners Buch: *"Nur wer seine Bitcoins selber verwaltet, besitzt Bitcoins."* Die Kehrseite: Wer sie selber verwaltet, muss auch selber für den Nachlassfall sorgen.

Das Dilemma ist strukturell:
- **Zu wenig dokumentiert** → Erben kommen nicht an die Coins
- **Zu offen dokumentiert** → Diebstahl durch Einbrecher, neugierige Dritte, Erbstreitigkeiten

Marc Steiners Ansatz: Diese Spannung lässt sich nicht eliminieren, aber strukturieren.

### Der Nachlassplan: Zwei Schichten

Steiner unterscheidet zwei Schichten, die für jeden Nutzer notwendig sind:

**Schicht 1 — Erben vorbereiten:** Erben müssen verstehen, dass du Bitcoin besitzt und wie man grundsätzlich darauf zugreift. Ein technischer Laie, der plötzlich auf eine Hardware-Wallet trifft ohne zu wissen was das ist, ist trotz bester technischer Sicherung ohne Zugang. Eine eigene "Erben-Kurzanleitung" gehört zum Nachlassplan.

**Schicht 2 — Zugangssicherung:** Die eigentlichen Schlüssel (Seed-Phrase, optionale Passphrase) müssen so verwahrt sein, dass Erben im Erbfall rankommen, Angreifer aber nicht.

Ein vollständiger Nachlassplan enthält mindestens:
- Einen "Bitcoin-Brief" (was ist vorhanden, wo liegt der Zugang, wie kommt man ran)
- Sicher verwahrte Seed-Phrase (getrennt vom Brief)
- Optionale Passphrase (separat von der Seed-Phrase)
- Regelmäßige Überprüfung und Aktualisierung bei jedem Hardware-Wallet-Wechsel, Kurssprung oder Lebensereignis

### Kritische Sicherheitsregel: Seed-Phrase nie digital

Steiner warnt explizit: Seed-Phrases gehören **nicht in Passwort-Manager**, nicht als Smartphone-Foto, nicht als Screenshot, nicht in digitale Notizen. Ein mit Schadsoftware infiziertes Gerät — etwa ein Keylogger — würde alle Passwort-Manager-Inhalte an den Angreifer weitergeben. *"Kein Anti-Spyware-Programm, keine Firewall und auch kein Virusscanner kann deine Geräte komplett vor Schadsoftware schützen."*

Die Seed-Phrase gehört auf Papier oder Metall (Cryptosteel, Bilodeau), verwahrt auf Offline-Systemen, die nie ans Internet angeschlossen sind. Tails OS (ein schreibgeschütztes Betriebssystem auf USB-Stick, das keine Spuren hinterlässt) ist für technisch versierte Nutzer eine gute digitale Alternative.

### Die 8 Musterabläufe

Steiner's Kernbeitrag sind acht konkrete Standardlösungen — mit steigender Komplexität und steigendem Sicherheitsniveau:

**#1 — Grundvariante:** Seed-Phrase auf Papier an sicherem Ort (Tresor, Notarbüro). Bitcoin-Brief mit Anleitung separat. Niedrigschwellig, aber single-point-of-failure bei physischem Verlust.

**#2 — Zusätzliche Sicherheitshürde:** Seed-Phrase und optionale Passphrase an getrennten Orten. Selbst wenn ein Angreifer die Seed-Phrase findet, fehlt ihm die Passphrase für den tatsächlichen Zugang. Erben brauchen beide Teile — der Nachlassplan erklärt, wo was liegt.

**#3 — Volldigital umgesetzt:** Seed-Phrase verschlüsselt auf Offline-Gerät oder via Tails OS. Höheres Sicherheitsniveau, aber höhere Komplexität für Erben. Entschlüsselungsanleitung muss zwingend im Nachlassplan stehen — inklusive welche Software nötig ist.

**#4 — Kombination mit Testament:** Seed-Phrase versiegelt beim Notar, Testament verweist darauf. Rechtlich sauberste Lösung für größere Beträge. Wichtig: Testamente können von Gerichten und Erbparteien eingesehen werden — Seed-Phrase direkt im Testament ist keine gute Idee.

**#5 — Poor Man's Shamir's Secret Sharing Scheme:** Die eleganteste Low-Tech-Lösung. Drei Recovery-Karten, jede mit 16 von 24 Seed-Wörtern, so verteilt, dass jeweils zwei Karten zusammen die vollständige Phrase ergeben — eine einzelne Karte ist wertlos. Entropie einer einzelnen Karte: ~88 Bit — aktuell sicher. Langfristig (Quantencomputer) eventuell schwächer. Funktioniert **nur mit 24-Wort-Phrasen**.

**#6 — SLIP-0039 Shamir's Secret Sharing Scheme:** Kryptografisch korrekte Version mit Software-Tools. Ein Geheimnis wird mathematisch in n Shares aufgeteilt, von denen k (Threshold) benötigt werden. Beispiel: 3-von-5 — jeder der 5 Erben bekommt einen Share, drei müssen sich zusammenfinden. Sehr sicher, komplex in der Umsetzung.

**#7 — "Digitales" SSS:** SSSS-Implementierung über eine offline heruntergeladene Webseite. Einstiegsfreundlicher als SLIP-0039, aber eher für technisch versierte Nutzer.

**#8 — Multisignatur mit Hardware-Wallet:** Drei Hardware-Wallets, 2-von-3-Multisig. Schlüssel 1 beim Erblasser, Schlüssel 2 beim Erben oder Notar, Schlüssel 3 an sicherem dritten Ort. Erblasser operiert zu Lebzeiten mit Schlüsseln 1+3; der Erbe kann nach dem Tod mit 2+3 erben. Kein einzelner Schlüssel reicht für Zugang. Höchste Sicherheit, höchste Komplexität. → [[multisig-und-kollaborative-verwahrung]]

### Ergänzende technische Option: Liana Wallet

Liana Wallet nutzt Miniscript für zeitbasierte Wiederherstellungsschlüssel: Ein Erben-Schlüssel wird definiert, der nach einer konfigurierbaren Inaktivitätsperiode aktiviert wird (z.B. 5 Jahre ohne Transaktion). Der Inhaber setzt den Timer regelmäßig durch eine normale Transaktion zurück. Stirbt er, wird der Erben-Schlüssel nach Ablauf aktiv — ohne dass der Erbe irgendwie eingreifen muss. → [[miniscript-und-liana]]

### Rechtliche Absicherung

In Deutschland, Österreich und der Schweiz ist Bitcoin wie jedes andere Vermögen vererbbar. Das Testament oder der Erbvertrag muss aber die Erben tatsächlich in die Lage versetzen, an die Coins zu kommen.

**Sealed Envelope beim Notar:** Zugangsinformationen versiegelt hinterlegen, freigegeben nur bei Tod. Der Notar weiß, dass ein Umschlag existiert; nur der Erblasser kennt den Inhalt. Das schützt vor unbefugter Einsichtnahme.

**Erbschaftssteuer:** Bitcoin wird auf den Marktwert zum Todeszeitpunkt besteuert. Bei großen Beträgen kann das die Liquidität des Erben für die Steuerzahlung einschränken, wenn kein Fiatgeld vorhanden ist — ein oft übersehener Planungspunkt.

### Steiner's Leitprinzip: Einfach und langfristig denken

Komplexe Setups scheitern meistens an ihrer Komplexität. Wenn Erben für eine 2-von-3-Multisig keine Anleitung verstehen oder nicht wissen, welche Software sie brauchen, hilft das beste kryptografische Setup nichts.

Steiner empfiehlt außerdem, Zukunftsszenarien mitzudenken: Schlechtes Papier vergilbt, billige Tinte verblasst. Quantencomputer könnten aktuelle Verschlüsselungen zukünftig brechen. Hardware-Wallets werden abgekündigt, Software-Wallets enden den Support. Der Nachlassplan muss regelmäßig aktualisiert werden.

### Häufige Fehler

Keinen Plan haben ist der häufigste Fehler. Steiners Buch ist explizit für diese Menschen geschrieben.

Seed-Phrase und Passphrase zusammen aufbewahren: Wer beides an einem Ort findet, hat vollständigen Zugang.

Zu komplexe Setups für technisch unversierte Erben: Multisig nützt nichts, wenn die Erben nicht wissen, was Multisig ist.

Informationen nur im Kopf: "Ich erkläre es meiner Familie, wenn die Zeit kommt" — und dann kommt sie unerwartet.

## Related

- [[wallet-backup-strategien]]
- [[fortego-backup-sicherheit]]
- [[multisig-und-kollaborative-verwahrung]]
- [[miniscript-und-liana]]
- [[optionale-passphrase]]
- [[selbstverwahrung-und-boersenrisiken]]

## Open Questions

- Wie entwickelt sich die rechtliche Behandlung von Bitcoin in deutschen Erbschaftssteuer-Berechnungen?
- Gibt es Bitcoin-spezifische Erbschaftsdienstleister mit etablierter Reputation in Europa?
- Werden Quantencomputer die Sicherheit von Poor Man's SSS und anderen Low-Entropy-Methoden zukünftig gefährden?
- Wie löst Liana Wallet den Kompromiss zwischen Sicherheit (Inaktivitätstimer) und Privatsphäre langfristig?
