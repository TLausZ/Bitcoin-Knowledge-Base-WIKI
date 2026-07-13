# Wallet of Satoshi

**Status:** established
**Themen:** self-custody, lightning, wallets
**Last updated:** 2026-06-09
**Sources:** [[2026-06-09_wallet-of-satoshi-faq]]

## Summary

Wallet of Satoshi (WoS) ist eine Bitcoin-Lightning-Wallet für iOS und Android, die maximale Einfachheit über alle anderen Ziele stellt. Sie existiert in zwei Modi: custodial (WoS hält die Schlüssel, verfügbar nur in bestimmten Regionen) und self-custodial (Nutzer hält die Schlüssel, weltweit verfügbar). Das zentrale Designziel ist der sofortige Einstieg ohne technisches Vorwissen — auf Kosten von Kontrolle und Datenschutz im custodial Modus.

## Body

### Zwei Modi: Custodial und Self-Custodial

WoS bietet zwei klar unterschiedliche Betriebsmodi:

**Custodial**: WoS hält die privaten Schlüssel im Namen des Nutzers. Vorteile: sofortige Einrichtung, einfache Wiederherstellung per E-Mail-Login (inkl. Zahlungshistorie). Nachteil: WoS kontrolliert die Gelder; der Nutzer ist auf das Vertrauen in das Unternehmen angewiesen. Nur in unterstützten Regionen verfügbar.

**Self-Custodial**: Der Nutzer hält die privaten Schlüssel selbst. Wiederherstellung über ein Seed-Backup (in-App-Anleitung). Zahlungshistorie ist nicht in der Cloud gesichert. Weltweit verfügbar. Der Nutzer ist für die Sicherung des Seeds verantwortlich.

Die App erkennt automatisch die richtige Version für die Region des Nutzers. Wechsel zwischen den Modi ist möglich; Mittel können dabei transferiert werden.

### Lightning Address

Jeder WoS-Nutzer erhält beim Download automatisch eine **Lightning Address** — eine menschenlesbare Adresse im E-Mail-Format (z.B. `satoshi@walletofsatoshi.com`). Sie kann für eingehende Lightning-Zahlungen genutzt werden, ohne jedes Mal eine neue Invoice erstellen zu müssen. Eine individuelle Adresse kann in der App gewählt werden.

### Zahlungen: Lightning und On-Chain

WoS erkennt beim Scannen eines QR-Codes automatisch den Zahlungstyp:

- **Lightning**: sofort, günstig
- **On-Chain**: möglich, aber mit variablen Mining-Gebühren; wird vor der Bestätigung angezeigt

Für alltägliche Zahlungen empfiehlt WoS explizit Lightning statt on-chain, da on-chain bei hoher Mempool-Auslastung teuer und langsam werden kann.

### Backup und Wiederherstellung

- **Custodial**: E-Mail-Login stellt Guthaben und Zahlungshistorie wieder her
- **Self-Custodial**: Seed-Backup nötig; Zahlungshistorie ist lokal und nicht wiederherstellbar

### Einordnung: Custodial vs. Self-Custodial Lightning

WoS steht stellvertretend für den Kompromiss im Lightning-Ökosystem: Custodial Wallets wie WoS sind extrem einfach zu benutzen, geben aber Kontrolle ab. Self-Custodial Wallets wie [[phoenix-wallet-lightning]] bieten echte Selbstverwahrung, erfordern aber mehr technisches Verständnis (Liquiditätsmanagement, Channel-Gebühren).

Der entscheidende Unterschied: Im custodial Modus ist WoS eine Kontonummer beim Anbieter, der die Lightning-Zahlungen verarbeitet, kein echter Node des Nutzers. Im self-custodial Modus hält der Nutzer die Schlüssel, aber die Architektur ist weniger transparent als bei Phoenix.

## Related

- [[phoenix-wallet-lightning]]
- [[skalierung-lightning-ark-statechains]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[payment-codes-und-adressaustausch]]
- [[hardware-wallet-einstieg]]

## Open Questions

- Wie ist die genaue technische Architektur des self-custodial Modus von WoS — echter eigener Node oder nur Schlüsselverwaltung?
- Welche Regionen unterstützen den custodial Modus, und welche regulatorischen Bedingungen bestimmen das?
- Wie verhält sich WoS bei einem Unternehmensausfall im custodial Modus — gibt es einen Recovery-Mechanismus für Nutzer?
