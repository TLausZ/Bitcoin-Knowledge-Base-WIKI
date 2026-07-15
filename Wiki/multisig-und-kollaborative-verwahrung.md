# Multisig und kollaborative Verwahrung

**Status:** established
**Themen:** self-custody
**Last updated:** 2026-06-06
**Sources:** [[20260326_sichere-deine-bitcoin-mit-bitbox-und-unchained]], [[20240919_was-ist-multisig-alles-was-du-wissen-musst]], [[20220623_bitcoin-multisig-sparrow-bitbox02-de]], [[20220309_bitbox02-multisig-specter-desktop-de]]

## Summary

Multisig-Wallets erfordern mehrere Signaturen von verschiedenen Schlüsseln, um Bitcoin ausgeben zu können. Das reduziert den Single Point of Failure einer einzelnen Hardware-Wallet und ermöglicht Redundanz, Vererbungsplanung und kollaborative Setups. Kollaborative Verwahrung (z.B. über Unchained) kombiniert selbst gehaltene Schlüssel mit einem Backup-Schlüssel eines vertrauenswürdigen Dienstleisters.

## Body

### Warum Multisig?

Eine einzelne Hardware-Wallet mit einem Backup ist für die meisten Nutzer ausreichend. Multisig wird sinnvoll, wenn:
- Große Bitcoin-Bestände mehr Redundanz erfordern
- Die Abhängigkeit von einem einzelnen Gerät oder Standort reduziert werden soll
- Vererbungsplanung strukturiert werden soll
- Ein Setup für Familie oder Unternehmen aufgebaut wird

### Wie Multisig funktioniert

Ein m-von-n-Multisig-Setup erfordert, dass mindestens m von n möglichen Schlüsseln eine Transaktion signieren. Beispiel: 2-von-3 bedeutet, dass 2 beliebige der 3 Schlüssel ausreichen — einer kann verloren gehen, ohne dass die Bitcoin verloren sind.

Jeder Schlüssel wird unabhängig verwaltet — typischerweise auf separaten Hardware-Wallets, an verschiedenen Standorten. Die Multisig-Wallet ist die Summe dieser Teile.

### Kollaborative Verwahrung (Unchained-Modell)

Kollaborative Verwahrung ist ein Mittelweg zwischen vollständiger Selbstverwahrung und Custodial-Lösungen. Im Unchained-Modell (2-von-3):
- Der Nutzer hält **zwei** der drei Schlüssel selbst
- Unchained hält **einen** Backup-Schlüssel
- Für eine Transaktion werden 2 beliebige Schlüssel benötigt

Das bedeutet: Unchained kann die Bitcoin des Nutzers nicht ohne Kooperation bewegen. Wenn ein Nutzerschlüssel verloren geht, hilft der Unchained-Backup-Schlüssel bei der Wiederherstellung. Wenn Unchained ausfällt oder nicht kooperiert, kann der Nutzer mit seinen eigenen zwei Schlüsseln trotzdem ausgeben.

Für Nutzer, die Redundanz und geführten Support wollen, ohne die Kontrolle abzugeben, ist dieses Modell eine sinnvolle Option.

### Wichtige Hinweise

Multisig ist komplexer als eine einzelne Hardware-Wallet. Risiken:
- **Setup-Komplexität:** Die Konfiguration (xpubs aller Schlüssel) muss sicher gespeichert werden — ohne sie kann man die Multisig-Wallet nicht wiederherstellen
- **Interoperabilität:** Nicht alle Wallets unterstützen Multisig gleich gut
- **Überengineering:** Für kleine Beträge oder unerfahrene Nutzer kann Multisig mehr Probleme schaffen als lösen

### Praxis: Multisig mit Specter Desktop + BitBox02

Eine weitere bewährte Koordinationssoftware ist Specter Desktop. Das Setup läuft ähnlich wie mit Sparrow: Geräte einzeln hinzufügen (per USB), eine Multisig-Wallet erstellen, Signierquorum festlegen. Der zentrale Unterschied zum Sparrow-Workflow liegt beim Backup: Specter exportiert die Wallet-Konfiguration als PDF-Datei, die alle xpubs der Cosigner enthält (aber keinen Private Key). Dieses PDF ist kritisch für die Wiederherstellung — es muss sicher aufbewahrt und in mehreren Kopien an verschiedenen Orten verwahrt werden.

Die Multisig-Registrierung auf der BitBox02 funktioniert in beiden Workflows identisch: Das Gerät zeigt beim ersten Empfang einer Adresse die Co-Signierer-xpubs an, die der Nutzer mit dem Backup abgleicht und bestätigt.

### Praxis: Multisig mit Sparrow + BitBox02

Ein bewährtes Setup für Privatnutzer ist 2-von-3 Native-SegWit mit drei BitBox02-Geräten und Sparrow Wallet als Koordinations-Software. Sparrow übernimmt das Erstellen der Wallet, das Vorbereiten von Transaktionen und die Koordination des Signierens — die BitBox02-Geräte halten die privaten Schlüssel und signieren auf Anfrage.

Beim ersten Empfang einer Adresse registriert die BitBox02 das Multisig-Setup: Das Gerät speichert eine Prüfsumme der xpubs aller Co-Signierer. Bei jeder späteren Aktion verifiziert es die Adresse unabhängig — eine Manipulation durch die Software ist damit erkennbar.

**Sicherungsdatei:** Sparrow kann die Wallet-Konfiguration (alle xpubs, aber keine privaten Schlüssel) als Datei exportieren. Diese Datei ist die kritische Ergänzung zu den Seed-Backups — ohne alle xpubs lässt sich die Wallet nicht wiederherstellen, selbst wenn genug Geräte physisch vorhanden sind.

### Wichtige Fallstricke (aus Praxiserfahrung)

**Cosigner-Verifizierung:** Beim ersten Setup müssen alle xpubs aller Cosigner auf allen Geräten manuell geprüft werden — alle Hardware-Wallets müssen dafür ein eigenes Display haben. Die BitBox02 kann bis zu 25 Multisig-Setups direkt registrieren und erkennt nachträgliche Änderungen.

**Unvollständige Backups:** Um eine Multisig-Wallet wiederherzustellen, benötigt die Software alle xpubs aller Cosigner — nicht nur das eigene Backup. Diese müssen separat gesichert werden (nicht geheim, aber wichtig).

**Bösartige Cosigner:** Ein einzelner Cosigner könnte einen manipulierten xpub übermitteln und das Vermögen „einfrieren". Deshalb: Keine Hot Wallets zusammen mit Hardware-Wallets mischen.

## Related

- [[taproot-musig2-frost]]
- [[bitcoin-vaults]]
- [[wallet-backup-strategien]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wann ist Multisig sinnvoller als eine gute Einzelwallet mit optionaler Passphrase?
- Wie entwickeln sich kollaborative Verwahrungsmodelle in Europa nach der ToFR?
