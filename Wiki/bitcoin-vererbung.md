# Bitcoin Vererbung

**Status:** emerging
**Last updated:** 2026-06-09
**Sources:** [[Bitcoins verwahren und vererben_ Ein praktischer Ratgeber -- Marc Steiner -- 1_ Auflage, Rheinfelden, 2020 -- Held, Stefan & Fabio Tröndle GbR_ -- isbn13 9783949098017 -- 6ba03ea3dd3602e370eb518e8ae1af9c -- Anna's Archive.pdf]]

## Summary

Bitcoin-Vererbung ist ein gelöstes Problem, das die meisten Nutzer ignorieren — bis es zu spät ist. Da Bitcoin in echter Selbstverwahrung ausschließlich über den privaten Schlüssel (Seedphrase) kontrollierbar ist, geht er beim Tod des Inhabers unwiderruflich verloren, wenn kein Erbe den Zugang kennt. Marc Steiners Buch (2020) bietet einen praktischen Rahmen: zugängliche Dokumentation für Erben, sichere Verwahrung der Schlüssel, und testamentarische Absicherung.

## Body

### Das grundlegende Problem

Bitcoin hat keine Kundenhotline, kein Passwort-Reset, keinen Kundendienst. Wer den Seed verliert, verliert die Coins. Dieselbe Eigenschaft, die Bitcoin vor staatlichem Eingriff schützt, macht Vererbung zur aktiven Aufgabe: Der Erblasser muss die Zugangsinformationen hinterlassen — aber so, dass nur die richtigen Personen Zugang erhalten.

Das Dilemma: Zu wenig dokumentiert → Erben kommen nicht ran. Zu offen dokumentiert → Diebstahl durch Einbruch, Erbstreitigkeiten, oder böswillige Dritte.

### Grundprinzipien der Bitcoin-Vererbung

**Wissen von Zugang trennen.** Ein Erbe sollte verstehen, dass Bitcoin vorhanden ist und wie er theoretisch darauf zugreift — aber die Schlüssel selbst sollten sicher verwahrt sein, nicht im selben Umschlag wie die Anleitung.

**Dokumentation auf Papierbasis.** Ein "Bitcoin-Brief" erklärt: Was ist Bitcoin? Welche Hardware-Wallet wird benutzt? Wo liegt der Seed? Welche Passphrase gibt es? Wie kommt man technisch an die Coins? Dieser Brief sollte mit dem Testament aufbewahrt oder beim Notar hinterlegt werden.

**Vertrauensperson einbinden.** Eine dritte Person — kein direkter Erbe — kann wissen, wo der Brief liegt, aber nicht den Inhalt kennen. Das verhindert, dass Information verloren geht, wenn der Erblasser plötzlich stirbt.

**Passphrase separat.** Wenn eine BIP-39-Passphrase verwendet wird, sollte sie nie zusammen mit der Seedphrase aufbewahrt werden. Erben brauchen beides — aber ein Einbrecher, der nur eines findet, hat keinen Zugang.

### Technische Optionen für Vererbungsplanung

**2-von-3-Multisig:** Drei Schlüssel, zwei nötig für Transaktionen. Schlüssel 1 beim Erblasser, Schlüssel 2 beim Erben oder Notar, Schlüssel 3 an sicherer dritter Stelle. Der Erblasser kann zu Lebzeiten mit Schlüsseln 1 und 3 operieren. Der Erbe kann nach dem Tod mit Schlüsseln 2 und 3 erben. Niemand kann ohne Mitwirkung stehlen.

**Hardware-Wallet mit dokumentiertem Backup:** Einfachste Lösung für die meisten Nutzer. Die Seedphrase auf Steelwallet oder Papier, versiegelt in einem Briefumschlag, beim Notar oder in einem Safe. Die BitBox02-Bedienungsanleitung beilegen.

**Dedicated Inheritance Wallet:** Eine separate Hardware-Wallet nur für Erbschaftszwecke, mit einem definierten Betrag. Diese Wallet ist vollständig dokumentiert, der Rest bleibt in einer komplexer gesicherten Hauptwallet.

**Liana Wallet:** Zeitbasierte Wiederherstellungsschlüssel durch Miniscript ermöglichen es, einen Erben-Schlüssel zu definieren, der nach einer bestimmten Zeit (z.B. 5 Jahre Inaktivität) aktiviert wird. Der Hauptinhaber muss gelegentlich eine Transaktion senden, um den Timer zurückzusetzen.

### Testament und rechtliche Absicherung

In Deutschland und der Schweiz ist Bitcoin wie andere Vermögenswerte vererbbar — aber das Testament muss die Erben in die Lage versetzen, tatsächlich auf die Coins zuzugreifen. Zwei Wege:

**Erwähnung im Testament:** "Ich besitze Bitcoin. Die Zugangsinformationen befinden sich in [Ort]." Genauer Ort und Zugangsinformationen im Testament zu nennen ist problematisch, da Testamente oft von Dritten eingesehen werden können.

**Sealed Envelope beim Notar:** Die Zugangsinformationen versiegelt hinterlegen, nur mit dem Ableben des Erblassers freigegeben. Der Notar weiß, dass ein Umschlag existiert; nur der Erblasser weiß den Inhalt.

### Häufige Fehler

Keinen Plan haben. Die meisten Bitcoin-Nutzer haben keinen Notfallplan. Das ist der häufigste Fehler.

Seedphrase und Passphrase zusammen aufbewahren. Damit ist das gesamte Guthaben zugänglich für jeden, der Zugang zur Aufbewahrungsstelle hat.

Zu komplexe Setups für Erben. Wenn die Erben kein technisches Wissen haben, nützt ein Multi-Sig-Setup nichts, wenn keine verständliche Anleitung dabei ist.

Informationen nur im Kopf. "Ich erkläre es meiner Familie, wenn die Zeit kommt" — und dann kommt die Zeit unerwartet.

## Related

- [[wallet-backup-strategien]]
- [[multisig-und-kollaborative-verwahrung]]
- [[miniscript-und-liana]]
- [[optionale-passphrase]]
- [[selbstverwahrung-und-boersenrisiken]]

## Open Questions

- Wie entwickelt sich die rechtliche Behandlung von Bitcoin in deutschen Erbschaftssteuer-Berechnungen?
- Gibt es Bitcoin-spezifische Erbschaftsdienstleister (ähnlich wie kollaborative Verwahrung für Sicherheit) mit guter Reputation?
- Wie löst Liana Wallet das Kompromiss zwischen Sicherheit (Inaktivitätstimer) und Privatsphäre?
