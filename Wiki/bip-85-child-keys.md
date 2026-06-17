# BIP-85 Child Keys

**Status:** emerging
**Last updated:** 2026-06-04
**Sources:** [[20250814_ein-backup-unendliche-möglichkeiten-bip-85-child-keys-erklärt]]

## Summary

BIP-85 ermöglicht es, aus einem einzigen Wallet-Backup beliebig viele unabhängige Wiederherstellungswörter abzuleiten. Die abgeleiteten „Child Keys" können für separate Hot Wallets, Geschenk-Wallets oder sogar starke Passwörter verwendet werden — ohne dass das ursprüngliche Backup gefährdet wird. Child Keys sind primär eine Komfortfunktion und bieten keine zusätzliche Sicherheit.

## Body

### Technisches Prinzip

Bitcoin-Wallets leiten bereits viele Schlüssel aus einem einzigen Seed ab, über sogenannte Ableitungspfade und kryptografische Hashfunktionen. BIP-85 nutzt dasselbe Prinzip, aber für einen anderen Zweck: Anstatt neue Schlüssel für Konten abzuleiten, wird ein abgeleiteter Schlüssel als Basis für **neue Wiederherstellungswörter** verwendet.

Das Entscheidende: Hashfunktionen sind nicht umkehrbar. Wer die Child Keys kennt, kann das ursprüngliche Backup **nicht** zurückrechnen. Deshalb ist es sicher, Child Keys außerhalb der sicheren Umgebung der Hardware-Wallet einzusetzen.

BIP-85 ist ein offener Standard: Egal welche BIP-85-fähige Wallet man verwendet, dieselben Parameter (Wortanzahl + Index) erzeugen immer dieselben Child Keys.

### Anwendungsfälle

**Persönliche Hot Wallets:** Wer seinen Großteil der Bitcoin sicher auf einer Hardware-Wallet hält, aber für alltägliche Zahlungen eine Hot Wallet auf dem Smartphone nutzt, kann diese mit Child Keys verknüpfen. Kein separates Backup nötig — bei Verlust des Smartphones einfach neu ableiten.

**Geschenk-Wallets:** Child Keys für Freunde oder Familienmitglieder erstellen. Die Person hat eine funktionierende Wallet; der Ersteller behält als „Notfallnetz" die Kontrolle über das ursprüngliche Backup.

**Passwörter:** Ein Child Key ist im Grunde eine große Zufallszahl — verwendbar als starkes Passwort für verschlüsselte Festplatten oder andere Zwecke.

### Wichtige Einschränkungen

- **Keine zusätzliche Sicherheit:** Child Keys sind genau so sicher wie das ursprüngliche Backup. Wer das Backup hat, hat Zugriff auf alle Child Keys.
- **Hauptbackup schützen:** Der Fokus sollte immer auf dem sicheren Verwahren des Originalbackups liegen, nicht auf einer Vielzahl abgeleiteter Wallets.
- **Dokumentation:** Wortanzahl und Index müssen notiert werden, um einen bestimmten Child Key reproduzieren zu können.

## Related

- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Gibt es sinnvolle Anwendungsfälle für „Grandchild Keys" (Child Keys aus Child Keys)?
- Welche anderen Standards (z.B. für Passwort-Ableitung) könnten von BIP-85 profitieren?
