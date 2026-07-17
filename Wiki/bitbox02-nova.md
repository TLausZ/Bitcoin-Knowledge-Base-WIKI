# BitBox02 Nova

**Status:** established
**Themen:** wallets
**Last updated:** 2026-06-04
**Sources:** [[20250620_vorstellung-der-bitbox02-nova]], [[20250703_whisper-wie-die-sichere-bluetooth-integration-der-bitbox02-nova-funktioniert]], [[20241212_wie-sich-die-bitbox02-seit-ihrem-start-im-jahr-2019-verbessert-hat]], [[20260521_bitbox02-nova-jetzt-in-bitcoin-orange-erhältlich]]

## Summary

Die BitBox02 Nova ist die zweite Generation der BitBox Hardware-Wallet, vorgestellt im Juni 2025. Gegenüber der originalen BitBox02 bringt sie iPhone/iPad-Unterstützung via Bluetooth (Whisper-Protokoll), ein kratzfesteres OLED-Glasdisplay, einen EAL6+-zertifizierten Secure Chip und erhöhte Speicherkapazität für zukünftige Updates. Die originale BitBox02 wird weiterhin unterstützt und erhält Updates.

## Body

### Wichtigste Neuerungen

**iPhone und iPad:** Erstmals kann eine BitBox mit der BitBoxApp auf Apple-Mobilgeräten verwendet werden. Ursache: Apple erlaubt keine freie USB-Kommunikation für externe Geräte. Lösung ist das **Whisper-Protokoll** über Bluetooth Low Energy (BLE).

**Whisper-Protokoll:** Ein eigens entwickeltes Kommunikationsprotokoll für sichere Bluetooth-Kommunikation:
- Dedizierter BLE-Chip (DA14531), isoliert von der Haupt-Firmware und dem Flash-Speicher
- BLE-Chip läuft Open-Source-Firmware, reproduzierbar kompilierbar
- Doppelte Verschlüsselung: BLE-native Verschlüsselung + Ende-zu-Ende-Verschlüsselung zwischen App und Firmware
- Reduzierte Signalstärke im Pairing-Modus (sehr geringe Reichweite)
- USB hat Priorität — Bluetooth wird automatisch deaktiviert, wenn USB verbunden

**OLED-Glasdisplay:** Kratzfester und langlebiger als das Display der originalen BitBox02. Randloses Design (durchgehend schwarz auf der Vorderseite), bessere Lesbarkeit durch höheren Kontrast.

**EAL6+ Secure Chip:** Neuer Infineon Optiga Trust M V3, EAL6+ zertifiziert — höchste verfügbare Sicherheitszertifizierung für Secure Chips. NDA-frei (keine Geheimhaltungsvereinbarungen notwendig). Erzwingt das 10-Versuch-Limit für Passworteingaben per Hardware-Zähler.

**Erhöhte Speicherkapazität:** Mehr Raum für zukünftige Firmware-Features.

**Neue Farben:** Mitternacht Schwarz, Polar Weiss (seit Juni 2025) und Bitcoin Orange (seit Mai 2026).

### Dual-Chip-Architektur

Wie die originale BitBox02 verwendet die Nova eine Dual-Chip-Architektur: Ein offener Mikrocontroller mit Open-Source-Firmware plus ein separater Secure Chip für physischen Schutz. Dem Secure Chip wird nicht blind vertraut — er ergänzt, ersetzt aber nicht die transparente Firmware.

### Kompatibilität

- Windows, Mac, Linux, Android (wie originale BitBox02)
- iPhone und iPad (neu, nur via Bluetooth/Whisper)
- USB hat immer Priorität gegenüber Bluetooth
- Für Lightning mit Lightning-Anschluss: USB-C auf Lightning-Adapter im Lieferumfang

### Zwei Editionen

Auch die Nova ist in **Bitcoin-only** (reduzierte Firmware, ~25% kleiner, für Bitcoin-Puristen) und **Multi Edition** (zusätzlich Ethereum, Litecoin, Cardano, U2F) erhältlich. Die Firmware-Edition kann nach dem Kauf nicht geändert werden.

### Wechsel von BitBox02 zu Nova

Einfach möglich: Die bestehenden Wiederherstellungswörter oder das microSD-Backup auf der Nova wiederherstellen. Beide Geräte können parallel betrieben werden.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[wallet-backup-strategien]]

## Open Questions

- Wie entwickelt sich die Unterstützung weiterer Coins in der Multi Edition?
- Wann werden weitere Farb-/Designvarianten der Nova erscheinen?
