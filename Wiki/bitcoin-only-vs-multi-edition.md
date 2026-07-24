# Bitcoin-only vs. Multi Edition

**Status:** established
**Themen:** self-custody
**Last updated:** 2026-06-05
**Sources:** [[20251002_warum-gibt-es-eine-bitcoin-only-edition-der-bitbox]]

## Summary

Die BitBox02 gibt es in zwei Firmware-Editionen: Bitcoin-only (nur Bitcoin) und Multi (Bitcoin + Altcoins + U2F). Gleiche Hardware, unterschiedliche Firmware — und die Entscheidung ist nach dem Kauf unwiderruflich. Die Bitcoin-only Edition hat ~25% weniger Code und damit eine kleinere Angriffsfläche. Wer ausschliesslich Bitcoin verwalten will, wählt Bitcoin-only; wer Flexibilität braucht oder noch andere Coins hält, wählt Multi.

## Body

### Gleiche Hardware, andere Firmware

Beide Editionen verwenden exakt dieselbe Hardware — gleiche Materialien, gleiche Komponenten, gleicher Preis. Der Unterschied liegt ausschliesslich in der Firmware. Das bedeutet: Das Sicherheitsniveau der Hardware ist identisch. Die Firmware-Edition wird vom Bootloader kryptografisch erzwungen und kann nach dem Kauf nicht mehr gewechselt werden.

### Sicherheitsargument für Bitcoin-only

Die Bitcoin-only Firmware ist etwa 25% kleiner und enthält über 100.000 Zeilen weniger Code. Weniger Code und weniger Abhängigkeiten bedeuten generell weniger potenzielle Schwachstellen — auch wenn das Gerät für Bitcoin-Zwecke gleich sicher ist. Die Analogie: Je grösser ein Gebäude, desto höher das theoretische Brandrisiko. Das Gebäude ist nicht unsicher, aber wer Brandsicherheit optimieren und den Platz ohnehin nicht braucht, wählt das kleinere.

Alle für Bitcoin sicherheitsrelevanten Funktionen sind in beiden Editionen vollständig vorhanden.

### Was die Multi Edition bietet

Multi unterstützt neben Bitcoin auch Litecoin, Ethereum (inkl. ERC20-Token) und Cardano sowie Zwei-Faktor-Authentifizierung (U2F/FIDO2). Die U2F-Schlüssel werden aus dem Wallet-Backup abgeleitet und sind damit wiederherstellbar — ein Vorteil gegenüber anderen Hardware-Sicherheitsschlüsseln wie YubiKeys, die nicht backup-basiert sind.

### Warum es die Multi Edition gibt

Viele Einsteiger verwalten noch Coins über Börsen und wollen beim Wechsel zur Selbstverwahrung nicht sofort alles umstellen. Die Multi Edition senkt die Einstiegshürde. Der wichtigste Schritt ist der Wechsel zu Selbstverwahrung — unabhängig davon, ob man bereits ein reines Bitcoin-Setup anstrebt.

### Entscheidungshilfe

- **Bitcoin-only wählen:** Wer ausschliesslich Bitcoin verwaltet und keine Altcoins hält.
- **Multi wählen:** Wer noch andere Coins hält, die Altcoin-Unterstützung aktuell braucht, oder U2F als zweiten Faktor nutzen möchte.

**Wichtig:** Die Entscheidung ist permanent. Eine Bitcoin-only Edition läuft für immer mit Bitcoin-only Firmware.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[bitbox02-nova]]
- [[wallet-backup-strategien]]
- [[firmware-verifikation-und-reproduzierbarkeit]]
- [[bitbox02-features]]

## Open Questions

- Gibt es valide Szenarien, wo die Altcoin-Unterstützung der Multi Edition einen Sicherheitsvorteil gegenüber separaten Geräten bietet?
- Wie entwickelt sich die Nutzung von U2F/FIDO2 im Kontext von Bitcoin-Sicherheitskonzepten?
