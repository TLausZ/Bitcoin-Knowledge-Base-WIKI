# Seedphrase-Entropie und Sicherheit

**Status:** established
**Themen:** self-custody, philosophie, wallets
**Last updated:** 2026-06-04
**Sources:** [[20240523_wie-schwer-ist-es-eine-seedphrase-zu-erraten]], [[20240411_warum-backups-auf-microsd-karten-nicht-verschlüsselt-werden-sollten]]

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

- **Schwache Zufallszahlengeneratoren:** Reproduzierbare oder vorhersehbare Muster (bekanntes Beispiel: Trust Wallet WASM-Vulnerability 2022/2023)
- **Brain Wallets:** Nutzer verwenden Passwörter oder bekannte Phrasen als Seed — leicht angreifbar
- **Offensichtliche Muster:** Zahlenfolgen wie 2121212121… sind keine echte Zufälligkeit

### Mehrere Entropiequellen in der BitBox02

Zur Redundanz kombiniert die BitBox02 fünf unabhängige Quellen:

1. Zufallszahlengenerator des Secure Chips
2. Zufallszahlengenerator des Mikrocontrollers
3. Statische Zufallszahl (bei Werksinstallation gesetzt, einmalig pro Gerät)
4. Host-Entropie der BitBoxApp (vom Computer/Smartphone)
5. Kryptografischer Hash des Gerätepassworts

Selbst wenn eine Quelle kompromittiert wäre, bleiben die anderen als Sicherheitsnetz.

### microSD-Backups und Verschlüsselung

microSD-Backups sind unverschlüsselt — vergleichbar mit einem Papier-Backup. Das ist eine bewusste Designentscheidung: Die BitBox01 hatte verschlüsselte Backups, was regelmässig dazu führte, dass Nutzer das Backup-Passwort vergassen und den Zugang verloren.

Wer eine zweite Sicherheitsebene möchte, sollte stattdessen die **optionale Passphrase** (BIP-39) verwenden — standardisiert, portabel, kompatibel mit jeder BIP-39-Wallet.

### Eigene Entropie einbringen: Diceware

Wer dem Gerät bezüglich Zufallsgenerierung nicht blind vertrauen will, kann seinen Seed selbst mit Würfeln erzeugen. Die BitBox02 unterstützt das: Man gibt die ersten 23 Wörter ein (aus einer Würfelwurf-Wörtertabelle nachgeschlagen), das Gerät berechnet alle gültigen Optionen für das 24. Wort (Prüfsumme) und lässt den Nutzer auswählen. Details: [[diceware-und-seed-generierung]].

## Related

- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[diceware-und-seed-generierung]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie sollte man mit der zunehmenden Rechenleistung (Quantencomputer) umgehen? Ab wann wird 256-Bit-Entropie kritisch?
