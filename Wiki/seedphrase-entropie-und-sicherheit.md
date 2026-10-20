# Seedphrase-Entropie und Sicherheit

**Status:** established
**Themen:** protokoll, self-custody, philosophie, adoption, wallets
**Last updated:** 2026-10-20
**Sources:** [[Was ist Entropie und wie erstellt die BitBox eine Wallet_]], [[BitBox – Sicherheit auf jeder Ebene]], [[20240523_wie-schwer-ist-es-eine-seedphrase-zu-erraten]], [[20240411_warum-backups-auf-microsd-karten-nicht-verschlüsselt-werden-sollten]]

## Summary

Eine Bitcoin-Wallet mit 24 Wörtern basiert auf einer 256-Bit-Zufallszahl — 2^256 mögliche Wallets, ungefähr vergleichbar mit der Anzahl der Atome im beobachtbaren Universum. Eine Seedphrase zufällig zu erraten ist in der Praxis unmöglich. Der einzige reale Angriffsfaktor ist schlechte Zufälligkeit: vorhersehbare Muster, schwache Generatoren oder bewusst gewählte „einfache" Seeds (Brain Wallets).

## Body

### Was Entropie bedeutet

Entropie misst, wie schwer eine Zahl zu erraten ist. Eine Münze viermal werfen = 4 Bit Entropie = 16 mögliche Ergebnisse. Eine Münze 256-mal werfen = 256 Bit Entropie = 2^256 Möglichkeiten.

Eine Bitcoin-Wallet mit 24 Wörtern basiert auf 256 Bit Entropie. 12 Wörter entsprechen 128 Bit Entropie.

### Wie unmöglich das Erraten ist

**24 Wörter (256 Bit):** Die Anzahl möglicher Wallets (~2^256) ist vergleichbar mit der Anzahl der Atome im beobachtbaren Universum. Eine zufällig erratene Wallet zu finden wäre wie eine Rundreise durch das gesamte Universum zu machen und dabei zufällig dasselbe Atom zurückzubringen, das man vorher ausgewählt hat.

**12 Wörter (128 Bit):** Immer noch vergleichbar mit dem 57 Milliarden-fachen Gewicht der Erde in Gramm. Für alle praktischen Zwecke ausreichend sicher.

### Der einzige reale Angriffsfaktor: Schlechte Zufälligkeit

Nicht alle grossen Zahlen sind sicher — entscheidend ist echte Zufälligkeit:

- **Schwache Zufallszahlengeneratoren:** Reproduzierbare oder vorhersehbare Muster (Beispiele: Trust Wallet WASM-Vulnerability 2022/2023, Coldcard-Seed-Erzeugung ab 2021, bekannt im August 2026, siehe [[coldcard-rng-schwachstelle]])
- **Brain Wallets:** Nutzer verwenden Passwörter oder bekannte Phrasen als Seed — leicht angreifbar
- **Offensichtliche Muster:** Zahlenfolgen wie 2121212121… sind keine echte Zufälligkeit

### PRNG, CSPRNG, TRNG: warum «sieht zufällig aus» nicht reicht
Nach der Coldcard-Schwachstelle erklärte BitBox im Oktober 2026, was hinter dem Begriff steckt. Entropie ist die Menge an Ungewissheit beim Raten, gemessen in Bit: Ein fairer Münzwurf ist ein Bit, 256 unabhängige Würfe sind 2^256 Möglichkeiten. Sie hängt nicht von der Länge einer Zahl ab: Eine 256-Bit-Zahl, die entweder nur aus Nullen oder nur aus Einsen besteht, hat ein Bit Entropie. Umgekehrt beweist ein Muster in den Wörtern keinen defekten Generator, Zufall erzeugt auch Muster. Entscheidend ist, wie die Zahl entstand und was ein Angreifer über diesen Vorgang weiss; an den Wiederherstellungswörtern allein lässt sich die Qualität nicht ablesen. Computer arbeiten deterministisch und brauchen deshalb externe Zufallsquellen. Ein Pseudozufallszahlengenerator (PRNG) rechnet aus einem Startwert eine Folge aus, die bei gleichem Start identisch ist; mit Datum und Uhrzeit initialisiert, lässt er sich nachbilden. Ein kryptografisch sicherer PRNG (CSPRNG) macht seine Ausgaben ohne Kenntnis des internen Zustands unvorhersagbar, kann aber keine Entropie schaffen: Mit einem 32-Bit-Seed gibt es nur 2^32 mögliche Zustände, auch wenn er 256-Bit-Zahlen ausgibt. Genau das war der Coldcard-Fehler vom August 2026: Bei der Wallet-Erstellung kam ungewollt ein CSPRNG mit zu wenig Entropie im Seed zum Einsatz. Ein echter Zufallszahlengenerator (TRNG) misst physikalische Vorgänge wie thermisches Rauschen oder Zeitschwankungen, die sich nicht reproduzieren lassen; auch er braucht Zustandsprüfungen und Konditionierung, weil Hardware verzerren oder ausfallen kann. Cloudflares Wand aus Lavalampen ist dasselbe Prinzip mit Kameras. [[Was ist Entropie und wie erstellt die BitBox eine Wallet_]]

### Mehrere Entropiequellen in der BitBox02

Zur Redundanz kombiniert die BitBox02 fünf unabhängige Quellen:

1. Zufallszahlengenerator des Secure Chips
2. Zufallszahlengenerator des Mikrocontrollers
3. Statische Zufallszahl (bei Werksinstallation gesetzt, einmalig pro Gerät)
4. Host-Entropie der BitBoxApp (vom Computer/Smartphone)
5. Kryptografischer Hash des Gerätepassworts

Die kryptografische Kombination garantiert, dass die Gesamtentropie mindestens der stärksten Quelle entspricht, nicht der schwächsten; vier der fünf Quellen dürfen verzerrt sein. Die beiden TRNGs (Mikrocontroller und Secure Chip, bei der BitBox02 der ATECC608B, bei der Nova der Optiga Trust M V3) liefern frische Zufallsdaten, der Werkswert ist pro Gerät fix und liefert nicht für jede Wallet neue Entropie, Host-Entropie und Passwort-Hash liegen ausserhalb der Hardware-Wallet. Die Wallet-Erstellung hängt damit weder davon ab, dass ein Mensch ein zufälliges Passwort wählt, noch davon, dass Computer oder ein einzelner TRNG vertrauenswürdig sind; der Code dazu ist in der Firmware öffentlich. [[Was ist Entropie und wie erstellt die BitBox eine Wallet_]] [[BitBox – Sicherheit auf jeder Ebene]]

### microSD-Backups und Verschlüsselung

microSD-Backups sind unverschlüsselt — vergleichbar mit einem Papier-Backup. Das ist eine bewusste Designentscheidung: Die BitBox01 hatte verschlüsselte Backups, was regelmässig dazu führte, dass Nutzer das Backup-Passwort vergassen und den Zugang verloren.

Wer eine zweite Sicherheitsebene möchte, sollte stattdessen die **optionale Passphrase** (BIP-39) verwenden — standardisiert, portabel, kompatibel mit jeder BIP-39-Wallet.

### Eigene Entropie einbringen: Diceware

Wer dem Gerät bezüglich Zufallsgenerierung nicht blind vertrauen will, kann seinen Seed selbst mit Würfeln erzeugen. Die BitBox02 unterstützt das: Man gibt die ersten 23 Wörter ein (aus einer Würfelwurf-Wörtertabelle nachgeschlagen), das Gerät berechnet alle gültigen Optionen für das 24. Wort (Prüfsumme) und lässt den Nutzer auswählen. Details: [[diceware-und-seed-generierung]]. Zwei Klarstellungen aus dem Oktober-Beitrag: Die Würfelmethode ersetzt die fünf Quellen vollständig, die Würfe werden nicht beigemischt, deshalb zählt die genaue Anleitung (faire Würfel, feste Reihenfolge, unbeobachtet). Wer eigene Entropie nur hinzufügen will, tut das über ein langes, unabhängig erzeugtes Gerätepasswort bei der Einrichtung, das als fünfte Quelle einfliesst und nach dem Backup durch ein alltagstaugliches ersetzt werden kann; eine spätere Änderung berührt die Entropie der Wallet nicht mehr. Eine optionale Passphrase verändert die Wiederherstellungswörter nicht und verbessert deren Entropie nicht, sie erzeugt eine separate Wallet. Und: Phishing-Kampagnen nutzen das Thema Entropie, um Angst zu erzeugen; Wiederherstellungswörter gehören in keinen «Entropie-Checker» und in keinen Support-Chat. [[Was ist Entropie und wie erstellt die BitBox eine Wallet_]]

## Related

- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[diceware-und-seed-generierung]]
- [[bitcoin-seed-cracking]]
- [[bip39-schwache-seeds]]
- [[bitcoin-entropie-und-ordnung]]
- [[bitcoin-entropy-rng]]
- [[hardware-wallet-migration]]
- [[hd-wallets-und-schluesselableitung]]
- [[kryptografische-schlussel-und-adressen]]
- [[optionale-passphrase]]
- [[coldcard-rng-schwachstelle]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie sollte man mit der zunehmenden Rechenleistung (Quantencomputer) umgehen? Ab wann wird 256-Bit-Entropie kritisch?
