# Bitcoin Pay-to-IP

**Status:** established
**Themen:** protokoll, satoshi
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bitcoin-ip-transactions]]

## Summary

Im originalen Bitcoin-Client war das Senden an eine IP-Adresse die Standard-Zahlmethode — wichtiger als das Senden an eine Bitcoin-Adresse. Ein Empfänger gab seine IP-Adresse weiter, der Sender verband sich damit, bekam einen Public Key zurück, signierte die Transaktion und broadcastete sie. Das Feature wurde entfernt, weil IP-Adressen schlechte Identifier sind und das Protokoll Man-in-the-Middle-Angriffe nicht verhinderte.

## Body

### Wie es funktionierte

Pay-to-IP (auch bekannt als IP Transaction) lief wie folgt: Empfänger gibt IP-Adresse weiter. Sender verbindet sich, der Node des Empfängers liefert einen Public Key. Sender baut die Transaktion, signiert sie, sendet sie an den Empfänger — der die Möglichkeit hatte, sie abzulehnen. Erst dann wurde die TX ins Netzwerk gebroadcastet.

Satoshi und Hal Finney nutzten in der ersten bekannten Bitcoin-Transaktion (10 BTC, Block 170) noch bare Public Keys — nicht Adressen. Adressen als Standard kamen danach.

### Der Name „Bitcoin-Adresse"

Dass wir Bitcoin-Zahlungsadressen überhaupt „Adressen" nennen, kommt von Pay-to-IP: IP-Adresse → Bitcoin-Adresse. Die Analogie war ursprünglich technisch sinnvoll, wurde aber auf ein abstrakteres Konzept übertragen. Das ist auch der Grund, warum manche argumentieren, „Rechnung" (Invoice) wäre der treffendere Begriff — es beschreibt besser, was eine Bitcoin-Adresse tut, und würde Adresswiederverwendung unattraktiver wirken lassen.

### Warum es entfernt wurde

IP-Adressen sind schlechte Identifier für Personen. Seit ~2009 wurden statische IPs seltener; DHCP gibt Adressen dynamisch. Die wichtigere Schwäche war fehlende Authentifizierung: Jemand zwischen Sender und Empfänger konnte den gelieferten Public Key ersetzen — ein klassischer Man-in-the-Middle. Zudem lief der Traffic unverschlüsselt.

Satoshi hatte Verbesserungen geplant, aber bevor diese umgesetzt wurden, wurde Pay-to-IP wegen der Nachteile ganz entfernt.

### Moderne Nachfolger

Einige Ideen aus Pay-to-IP leben weiter, alle mit Datenschutzfokus:

- **BIP47 (Reusable Payment Codes):** Ermöglicht Zahlungen an einen statischen Code, ohne die Adresse zu wiederholen.
- **BIP78 (PayJoin):** Interaktives Protokoll, bei dem Sender und Empfänger gemeinsam eine Transaktion bauen.
- **BIP352 (Silent Payments):** Ermöglicht Zahlungen an einen statischen Identifier, ohne on-chain Verknüpfbarkeit.
- **BTCPay Server:** Reifste Implementierung des ursprünglichen Pay-to-IP-Gedankens — Server des Empfängers koordiniert die Transaktion interaktiv.

## Related

- [[kryptografische-schlussel-und-adressen]]
- [[payment-codes-und-adressaustausch]]
- [[silent-payments]]
- [[bitcoin-adresstypen]]

## Open Questions

- Könnte ein modernes, authentifiziertes Pay-to-IP-ähnliches Protokoll (z.B. mit Nostr) die ursprünglichen UX-Vorteile bringen?
