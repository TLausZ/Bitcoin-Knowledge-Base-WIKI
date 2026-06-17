														# BIP-329 Wallet Labels

**Status:** emerging
**Last updated:** 2026-06-04
**Sources:** [[20250424_import-und-export-von-wallet-labels-mit-bip-329]]

## Summary

BIP-329 ist ein offener Standard für den Export und Import von Wallet-Labels (Transaktionsnotizen, Kontonamen, Adress-Tags) zwischen verschiedenen Bitcoin-Wallet-Softwareprogrammen. Die BitBoxApp unterstützt BIP-329 seit dem Ritom-Update (Juli 2024). Ohne solche Standards gehen selbst beschriftete Transaktionen beim Wechsel der Wallet-Software verloren.

## Body

### Das Problem

Mit steigender Transaktionszahl werden Bitcoin-Wallets unübersichtlich. Rohe Transaktions-IDs und Adressen verraten nichts über ihren Kontext. Persönliche Labels (z.B. „Gehalt Februar 2025", „Pocket Bitcoin Kauf", „Rückgabe von Markus") machen eine Wallet erst wirklich nutzbar.

Das Problem: Labels wurden bisher wallet-intern gespeichert und sind bei einem Softwarewechsel verloren gegangen.

### Wie BIP-329 funktioniert

BIP-329 definiert ein einheitliches Dateiformat (JSON Lines / `.jsonl`) für den Export von Labels. Jeder Eintrag enthält:
- Typ (Transaktion, Adresse, öffentlicher Schlüssel, Input, Output)
- Referenz auf die tatsächlichen Daten (z.B. Transaktions-ID)
- Das Label selbst

Das Format ist menschenlesbar: Eine exportierte Datei kann in einem Texteditor geöffnet und verstanden werden.

**Interoperabilität:** Kompatible Wallets können Labels untereinander austauschen. Aktuelle Unterstützung u.a. in BitBoxApp und Sparrow Wallet. Eine aktuelle Liste kompatibler Software findet sich auf [bip329.org](https://bip329.org/).

### Datenschutz beim Export

Exportierte Label-Dateien enthalten nicht nur Transaktionsnotizen, sondern auch Bitcoin-Adressen und öffentliche Schlüssel der Wallet. Sie sollten nur mit vertrauenswürdigen Geräten und Personen geteilt werden.

### Nutzung in der BitBoxApp

- Export: In den Kontoinformationen → Transaktionshistorie exportieren
- Import: Textdatei (`.txt` oder `.jsonl`) auswählen
- Manche Wallets erfordern die Endung `.jsonl` — ggf. Datei umbenennen

Labels werden nicht in Echtzeit zwischen Wallets synchronisiert — das ist eine bewusste Designentscheidung, da Wallet-Software-Instanzen grundsätzlich nicht kommunizieren.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[opsec-und-privatsphäre]]

## Open Questions

- Wird BIP-329 von mehr Wallets übernommen?
- Gibt es sinnvolle Erweiterungen des Standards (z.B. verschlüsselte Labels)?
