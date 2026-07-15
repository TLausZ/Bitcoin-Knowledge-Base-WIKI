# Hardware-Wallet-Migration

**Status:** established
**Themen:** self-custody, wallets
**Last updated:** 2026-06-05
**Sources:** [[20230517_wechsel-vom-ledger-nano-auf-bitbox02-ist-super-einfach]], [[20230517_der-wechsel-von-trezor-auf-die-bitbox02-ist-super-einfach]], [[20230118_die-bitbox01-ist-am-ende-ihrer-reise-de]]

## Summary

Der Wechsel zwischen Hardware-Wallets erfordert keine Blockchain-Transaktionen, wenn beide Geräte denselben BIP-39-Standard unterstützen. Die 12 oder 24 Wiederherstellungswörter (Seed) werden einfach auf der neuen Wallet wiederhergestellt — die Coins bewegen sich nicht, nur die kontrollierende Hardware wechselt. Die wichtigste Fußnote: Trezors neuerer SLIP-39-Standard (20 Wörter) ist mit praktisch keiner anderen Wallet kompatibel.

## Body

### Zwei Migrationswege

**Weg 1: Backup auf neuer Wallet wiederherstellen.** Die Seed-Phrase der alten Wallet wird auf der neuen Wallet eingegeben. Keine Blockchain-Transaktionen, keine Gebühren. Beide Geräte haben danach identischen Seed-Zugriff. Nachteil: man vertraut darauf, dass der originale Seed-Erstellungsprozess der alten Wallet sicher war.

**Weg 2: Neue Wallet erstellen, Coins senden.** Eine frische Wallet wird auf dem neuen Gerät erstellt, dann werden Coins per Bitcoin-Transaktion übertragen. Saubererer Neuanfang, höchste Sicherheit. Erfordert Transaktionsgebühren und Aufwand bei vielen Coins und Accounts.

Empfehlung: Wer von einem Gerät mit bekannter Sicherheitslücke wechselt (z.B. nach einem Vorfall), sollte immer Weg 2 nehmen.

### SLIP-39 vs. BIP-39: das wichtigste Kompatibilitätsproblem

BIP-39 ist der Industriestandard: 12 oder 24 englische Wörter aus einer festgelegten 2048-Wort-Liste. Nahezu jede Hardware-Wallet, Software-Wallet und Recovery-Lösung unterstützt ihn.

Trezor hat für neuere Geräte SLIP-39 eingeführt: 20 Wörter in einem anderen Schema, das Shamir's Secret Sharing ermöglicht. SLIP-39 ist mit BIP-39 **nicht kompatibel** — eine auf SLIP-39 erstellte Trezor-Wallet kann auf einer BitBox02, Ledger, oder nahezu jeder anderen Wallet nicht wiederhergestellt werden.

Wer ein SLIP-39-Backup hat und migrieren möchte, muss zwingend Weg 2 nehmen (Coins senden).

### Besonderheiten bei Ledger

Ledger-Ethereum-Konten nutzen einen nicht standardisierten Derivationspfad. Eine Wiederherstellung des Backup auf einer anderen Wallet öffnet die Bitcoin-Konten korrekt, aber die ETH-Konten können unter einem anderen Pfad liegen als erwartet. Empfehlung für ETH-Nutzer mit mehreren Konten: neue Wallet erstellen und ETH explizit übertragen.

Alte Bitcoin-Legacy-Adressen (beginnen mit `1`) werden von der BitBox02 nicht unterstützt — diese wurden schon beim Release der BitBox02 als veraltet betrachtet. Falls vorhanden: zuerst an eine neue Adresse senden.

### Passphrase bei Migration

Wer auf der alten Wallet eine optionale BIP-39-Passphrase (25. Wort, Hidden Wallet) verwendet hat, muss diese auf der neuen Wallet explizit aktivieren und bei jedem Entsperren eingeben. Die Passphrase ist Teil des Backups und darf nicht vergessen werden.

### Nach der Migration

Nach einer Backup-Wiederherstellung sollte die neue Wallet als einzige aktive Wallet verwendet werden. Das alte Gerät dient als Backup — man kann es aufbewahren, aber sollte es nicht parallel aktiv halten, um Konfusion zu vermeiden.

## Related

- [[wallet-backup-strategien]]
- [[optionale-passphrase]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[seedphrase-entropie-und-sicherheit]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie entwickelt sich SLIP-39-Unterstützung bei anderen Wallet-Herstellern?
- Gibt es sichere Tools, um SLIP-39-Backups in BIP-39 zu konvertieren?
