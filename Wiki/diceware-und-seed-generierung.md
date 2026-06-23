# Diceware und eigene Seed-Generierung

**Status:** established
**Last updated:** 2026-06-22
**Sources:** [[20210203_wuerfle-bitcoin-wallet-diceware-de]], [[aprycot-diy-private-schluessel-bitcoin]]

## Summary

Wer seinem Hardware-Wallet bezüglich Zufallszahlengenerierung nicht blind vertrauen will, kann seinen eigenen Bitcoin-Seed mit Würfeln erzeugen. Die BitBox02 unterstützt das direkt: Die ersten 23 Wörter werden gewürfelt und eingegeben, das Gerät berechnet alle gültigen Optionen für das 24. Wort (Prüfsumme) und lässt den Nutzer auswählen. Das Ergebnis ist ein vollständiger BIP-39-Seed, der mit jeder kompatiblen Wallet verifiziert und wiederhergestellt werden kann.

## Body

### Warum selbst würfeln?

Ein gut konzipiertes Hardware-Wallet nutzt mehrere unabhängige Entropiequellen (bei der BitBox02 fünf), sodass eine einzelne kompromittierte Quelle nichts ausmacht. Die Open-Source-Firmware ermöglicht externe Überprüfung. Für die meisten Nutzer ist das ausreichend.

Das Würfeln ist dennoch kein Overkill: Wer selbst würfelt, muss der Hardware-Wallet in Bezug auf Zufälligkeit gar nicht vertrauen. Der Prozess ist außerdem transparent und von jedem nachvollziehbar.

Was Diceware nicht ersetzt: ein sicheres Gerät zum Signieren von Transaktionen. Selbst ein perfekter Seed nützt nichts, wenn der private Schlüssel später auf einem unsicheren Computer landet.

### Warum Menschen schlecht in Zufälligkeit sind

Menschen erzeugen beim freien Auswählen keine echten Zufallszahlen — sie bevorzugen bestimmte Muster, vermeiden Wiederholungen oder wählen "intuitiv". Würfel sind mechanisch unvoreingenommen.

### Das Problem mit dem 24. Wort

Die 24 BIP-39-Wörter sind nicht vollständig unabhängig. Das letzte Wort enthält eine Prüfsumme über die ersten 23 Wörter. Man kann zwar beliebige Wörter für die ersten 23 wählen, das 24. muss aber berechnet werden — ein falsches 24. Wort ergibt einen ungültigen Seed.

Die BitBox02 löst das: Man gibt die ersten 23 Wörter ein, das Gerät zeigt alle 8 gültigen Optionen für das 24. Wort an. Man wählt eine per Würfelwurf oder Münzwurf.

### Benötigte Materialien

- BitBox02 Diceware-Anleitung (PDF von bitbox.swiss)
- Faltbare Backup-Karte (PDF zum Ausdrucken)
- BitBox02 Diceware-Wörtertabelle (alle 2048 BIP-39-Wörter als Matrix)
- 5 Casino-Würfel (ein einzelner geht auch — dauert länger)
- Münze (oder ein sechster Würfel)
- BitBox02 Hardware-Wallet

### Sicherheitsvorkehrungen

Vor dem Start: Alle elektronischen Geräte ausschalten, Mobiltelefon weglegen. Wörter nicht laut aussprechen. Nichts auf der Wörtertabelle markieren. Wörter ausschließlich auf die Backup-Karte schreiben — kein digitales Gerät außer der BitBox02 darf je damit in Kontakt kommen.

### Würfelmethode (Schritt für Schritt)

Eine klare, vorab festgelegte Methode ist wichtig — spontane Entscheidungen im Prozess wären keine echte Zufälligkeit.

Empfohlene Methode: Alle 5 Würfel und eine Münze gleichzeitig werfen. Würfel mit Ergebnis 1–4 von links nach rechts aufreihen; Würfel mit 5 oder 6 nochmals werfen, bis sie 1–4 zeigen und dann einreihen. Münze daneben legen.

Aus den 5 Würfelzahlen und dem Münzwurf wird in der Wörtertabelle ein Wort nachgeschlagen: Würfel 1 gibt die Seitenzahl, Würfel 2–4 die Zeile, Würfel 5 und Münze die Spalte. Das Wort auf die Backup-Karte schreiben.

Für jedes der ersten 23 Wörter wiederholen. Das 24. Wort dann auf der BitBox02 auswählen.

### Prozess auf der BitBox02

Falls die BitBox02 bereits eingerichtet ist: Aktuelles Backup verifizieren, dann Gerät zurücksetzen. Dann im Einrichtungsassistenten "Von Recovery-Wörtern wiederherstellen" → "24 Wörter" wählen → 23 Wörter eingeben → Gerät zeigt gültige Optionen für das 24. Wort → per Münzwurf oder Würfel eine auswählen → auf Backup-Karte notieren → auf BitBox02 bestätigen.

### Backup verifizieren

Nach dem Setup sofort verifizieren: In der BitBoxApp "Gerät verwalten → Recovery-Wörter anzeigen". Das Gerät zeigt alle 24 Wörter und stellt anschließend Auswahl-Quizfragen. Wenn die Backup-Karte korrekt ist, besteht der Test ohne Warnungen.

### Kompatibilität

Der resultierende Seed ist BIP-39-Standard und funktioniert mit jeder kompatiblen Wallet (Electrum, Sparrow, Green, usw.) zur unabhängigen Verifikation oder Wiederherstellung.

### Vollständig manuelle Methode ohne Hardware-Wallet

Wer keine Hardware-Wallet hat oder ihr komplett misstrauen will, kann einen Seed auch rein manuell erzeugen — mit Würfeln, Papier und einem (air-gapped) Computer. Arman the Parman beschreibt das Verfahren:

**Schritt 1 — 256 Bit Entropie würfeln.** Vier Würfel gleichzeitig: 1–3 = Null, 4–6 = Eins. 23 Zeilen à 11 Ziffern plus drei Ziffern für die 24. Zeile ergeben 256 Bit.

**Schritt 2 — Prüfsumme berechnen.** Die 256 Bit werden mit SHA-256 gehasht (Terminalbefehl: `echo <bits> | shasum -a 256 -0`). Die ersten zwei Hexzeichen des Hash werden in 8 Binärstellen umgewandelt — das vervollständigt die 24. Zeile auf 11 Bit. Ohne diesen Schritt ergibt der Seed keinen gültigen BIP-39-Seed.

**Schritt 3 — Binär → Dezimal.** Jede der 24 Gruppen à 11 Bit wird in eine Dezimalzahl umgerechnet (0–2047). Am Terminal: `echo "$((2#10101111001))"`.

**Schritt 4 — BIP-39-Wortliste.** Jede Dezimalzahl + 1 ergibt die Zeilennummer in der GitHub-Wortliste (Computer zählt ab 0, die Liste ab 1). Das ergibt die 24 Seed-Wörter.

Für echte Bitcoin muss dieser Prozess auf einem Air-Gap-Computer ohne Netzwerkverbindung laufen — ein temporär getrennter Laptop reicht nicht; Hardware ohne WLAN/Bluetooth ist die einzig sichere Option. Eine Raspberry Pi Zero ohne Funkmodule kostet etwa 10 USD. [[aprycot-diy-private-schluessel-bitcoin]]

Der Vorteil dieser Methode: Man muss keinem Gerät in Bezug auf Zufälligkeit vertrauen. Der Nachteil: Rechenaufwand, Fehleranfälligkeit, und das 24. Wort muss rechnergestützt bestimmt werden.

## Related

- [[seedphrase-entropie-und-sicherheit]]
- [[wallet-backup-strategien]]
- [[hd-wallets-und-schluesselableitung]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Wie viele Würfelwürfe pro Wort sind nötig, damit die Entropie nicht durch den Prozess selbst reduziert wird?
- Ab welcher Bitcoin-Menge lohnt sich der Aufwand eines Air-Gap-Computers gegenüber einer seriösen Hardware-Wallet?
