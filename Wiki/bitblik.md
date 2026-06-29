# bitblik — BLIK–Bitcoin Bridge

**Status:** established
**Last updated:** 2026-06-09
**Sources:** [[2026-06-09_bitblik-faq]]

## Summary

bitblik ist eine freie, quelloffene App, die Bitcoin-Halter mit Menschen verbindet, die Zugang zum polnischen BLIK-Zahlungssystem haben. Das Kernprinzip: Bitcoin wird in einer Lightning Hold-Invoice eingesperrt, bis der BLIK-Code eingelöst ist — kein Verwahrer, kein KYC, kein Mittelsmann. Die Settlement-Zeit beträgt durchschnittlich ~2 Minuten. bitblik macht Bitcoin-Zahlungen überall möglich, wo BLIK akzeptiert wird — also fast im gesamten polnischen Einzelhandel, an Geldautomaten und im Online-Handel.

## Body

### Was ist BLIK?

BLIK ist das dominierende mobile Zahlungssystem in Polen. Die Banking-App generiert einen 6-stelligen Code, der ~2 Minuten gültig ist. Der Nutzer gibt diesen Code am Kassenterminal, im Online-Checkout oder am Geldautomaten ein und bestätigt die Zahlung anschließend per Popup in der Banking-App. Nahezu jede polnische Bank und jeder Händler unterstützt BLIK.

### Das Protokoll: Hold-Invoice als Escrow

Das technische Herzstück ist die **Lightning Hold-Invoice**:

1. Der Bitcoin-Halter erstellt ein Angebot für einen PLN-Betrag; Kurs und Gebühren werden vorab angezeigt.
2. Er zahlt eine Lightning Hold-Invoice — die Mittel werden damit eingesperrt (escrowed), aber nicht übertragen. Sie bleiben beim Zahler, bis der BLIK-Code eingelöst wird.
3. Die Gegenpartei (mit BLIK-Zugang) gibt den 6-stelligen Code am Terminal oder online ein.
4. Wenn die Bank die Zahlung bestätigt, löst sich die Hold-Invoice auf — Bitcoin geht an die Gegenpartei, BLIK-Zahlung ist abgeschlossen.

Falls irgendetwas fehlschlägt (Code abgelaufen, BLIK-Zahlung abgebrochen), verfällt die Invoice und die Bitcoin verbleiben beim ursprünglichen Halter. Das System ist trustless by design.

### Fraud-Schutz ohne Verwahrer

Streitigkeiten werden mit Bank-App-Beweisen beigelegt: Ohne Zahlungsnachweis der Bank bleibt der Bitcoin eingesperrt. Das macht Betrug strukturell unattraktiv — Lügen verliert jedes Mal.

### Non-Custodial, kein KYC, P2P

bitblik hält zu keinem Zeitpunkt Bitcoin oder Fiat. Es gibt keine Unternehmensinstanz zwischen den Handelspartnern — nur das Lightning-Protokoll und die Hold-Invoice. Kein KYC, keine Kontoregistrierung, keine Identitätsprüfung.

### Kein App Store — bewusste Entscheidung

bitblik ist bewusst nicht im Apple App Store oder Google Play verfügbar. Begründung: Beide Plattformen entfernen regelmäßig Bitcoin- und Datenschutz-Apps. Installation:

- **iOS**: über AltStore PAL (nur EU-registrierte Geräte; basiert auf EU Digital Markets Act)
- **Android**: über Zapstore (Nostr-nativer App Store) oder direktes APK von GitHub
- **Web**: experimenteller Client unter `app.bitblik.app`

### Angebote finden

Neue Angebote werden über Benachrichtigungskanäle gepusht: SimpleX, Matrix, Telegram, Signal. Jedes neue Angebot erscheint mit einem Ein-Tap-Accept-Link im jeweiligen Kanal.

### Anwendungsfälle

Überall wo BLIK funktioniert: Supermarktkassen (Żabka, Biedronka, Lidl), Cafés, Geldautomaten (Cash-out), Kassenterminals, Online-Checkout (Allegro u.a.).

### Einordnung im Lightning-Ökosystem

bitblik löst ein konkretes lokales Problem: In Polen ist BLIK allgegenwärtig, aber Bitcoin-Zahlungen an Kassen kaum möglich. bitblik überbrückt diese Lücke ohne Kompromisse bei Verwahrung oder Datenschutz — ein Beispiel für lokale P2P-Bitcoin-Infrastruktur, die ohne zentrale Gatekeeper auskommt.

Im Vergleich zu [[phoenix-wallet-lightning]] oder [[wallet-of-satoshi]] ist bitblik kein allgemeines Lightning-Wallet, sondern ein spezialisiertes P2P-Tauschprotokoll für einen spezifischen geografischen Kontext.

## Related

- [[phoenix-wallet-lightning]]
- [[wallet-of-satoshi]]
- [[skalierung-lightning-ark-statechains]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Ist bitblik auf andere Länder erweiterbar, die ähnliche Instant-Payment-Systeme haben (z.B. Swish in Schweden, Twint in der Schweiz)?
- Wie verhält sich die Hold-Invoice bei sehr langen BLIK-Bestätigungszeiten oder Bankausfällen?
- Gibt es Pläne für ein dezentrales Matching (z.B. über Nostr), um die Abhängigkeit von zentralisierten Benachrichtigungskanälen zu reduzieren?
