# Payment Requests (SLIP-24)

**Status:** established
**Last updated:** 2026-06-04
**Sources:** [[20240822_bitcoin-sicher-an-eine-börse-versenden-mit-payment-requests]], [[20240711_bitbox-07-2024-ritom-update]], [[20241002_bitbox-10-2024-livigno-update]]

## Summary

Payment Requests (basierend auf SLIP-24) lösen das Problem der Adress-Manipulation beim Senden von Bitcoin an externe Dienste. Ein öffentlicher Schlüssel des Empfängers (z.B. einer Börse) wird direkt in der Hardware-Wallet-Firmware registriert. Der Dienst signiert seine Einzahlungsadressen mit dem zugehörigen privaten Schlüssel — die Hardware-Wallet verifiziert die Signatur kryptografisch, unabhängig vom verbundenen Computer.

## Body

### Das Problem: Address Spoofing

Beim Senden von Bitcoin an eine Börse zeigt der Browser eine Einzahlungsadresse an — auf einem potenziell kompromittierten Computer. Ein Angreifer könnte diese Adresse durch seine eigene ersetzen. Die Hardware-Wallet hatte bisher keine Möglichkeit, die Authentizität einer solchen „von außen kommenden" Adresse zu prüfen.

Die traditionelle Lösung (Adresse auf einem zweiten Gerät prüfen) hat Schwächen: Sie ist umständlich, wird oft vernachlässigt, und manche Dienste generieren bei jeder Anfrage neue Adressen.

### Wie Payment Requests funktionieren

1. **Registrierung:** Der öffentliche Schlüssel des Dienstes wird durch die BitBox-Entwickler direkt in der Firmware registriert — außerhalb der Reichweite von Angreifern
2. **Signierung:** Der Dienst signiert seine Einzahlungsadresse (und optional weitere Daten) mit seinem privaten Schlüssel
3. **Verifikation:** Die Hardware-Wallet prüft die Signatur eigenständig — unabhängig vom verbundenen Gerät
4. **Alarm bei Manipulation:** Wenn ein Angreifer die Payment Request manipuliert, schlägt die Verifikation fehl

### Erweiterung: Vollständige Transaktionsverifikation

Payment Requests können mehr als nur die Adresse absichern. Beim Verkauf von Bitcoin mit Pocket Bitcoin enthält die signierte Payment Request auch die IBAN des Bankkontos, auf das der Fiat-Betrag überwiesen wird. Die BitBox02 zeigt Adresse, Betrag UND IBAN auf dem Display — der Nutzer bestätigt alle Angaben direkt auf dem Gerät, ohne dem Computer vertrauen zu müssen.

### Implementierung in BitBox

- **Ritom-Update (Juli 2024):** Technische Grundlage in der Firmware implementiert
- **Livigno-Update (Oktober 2024):** Erste produktive Nutzung — Verkauf von Bitcoin mit Pocket Bitcoin
- **Geneva-Update (Mai 2026):** Nutzung auch für dezentrale Swaps

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[regulierung-tofr-aopp]]
- [[multisig-und-kollaborative-verwahrung]]

## Open Questions

- Welche anderen Dienste werden Payment Requests in der BitBox-Firmware registrieren?
- Kann das Protokoll auf weitere Anwendungsfälle (z.B. Lightning-Auszahlungen) ausgeweitet werden?
