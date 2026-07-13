# Payment Codes und Adressaustausch

**Status:** emerging
**Themen:** protokoll, privacy
**Last updated:** 2026-06-04
**Sources:** [[20240606_payment-codes-bitcoin-adressen-privat-austauschen]]

## Summary

Um Privatsphäre zu wahren, sollte für jede Bitcoin-Transaktion eine neue Adresse verwendet werden — was regelmäßigen manuellen Austausch erfordert. Payment Codes lösen dieses Problem: Eine einzige statische Adresse ermöglicht es, beliebig viele neue, einmalige Empfangsadressen abzuleiten, ohne für jede Zahlung zu interagieren. Die zwei wichtigsten Ansätze sind BIP-47 (mit einmaliger Benachrichtigungs-Transaktion) und Silent Payments (ohne Overhead, aber mit höherem Scanning-Aufwand).

## Body

### Das Grundproblem

Bitcoin-Adressen sind öffentlich einsehbar. Wer dieselbe Adresse mehrfach verwendet, erlaubt es jedem, alle zugehörigen Transaktionen zu verfolgen. Die Lösung — für jede Zahlung eine neue Adresse verwenden — erfordert aber ständige Interaktion: manuelles Teilen neuer Adressen.

### Bestehende Lösungsansätze und ihre Grenzen

| Methode | Privatsphäre | Benutzerfreundlichkeit |
|---------|-------------|----------------------|
| Adresse wiederverwenden | Schlecht | Sehr gut |
| Manuelles Teilen | Gut | Schlecht |
| Extended Public Key (xpub) | Mittel | Mittel |
| BTCPay Server | Sehr gut | Nur für Unternehmen |

### BIP-47 Payment Codes (PayNyms)

Payment Codes (Präfix `PM8T`) enthalten eine **Benachrichtigungs-Adresse**.

**Ablauf:**
1. Einmalige **Benachrichtigungs-Transaktion** an Bobs Adresse — tauscht Schlüsselinformation aus
2. Sender und Empfänger vereinbaren via Diffie-Hellman ein gemeinsames Geheimnis
3. Sender kann ab sofort beliebig viele neue Adressen ableiten — ohne weitere Interaktion

**Nachteil:** Die Benachrichtigungs-Transaktion kostet Gebühren und hinterlässt Metadaten (erkennbar, dass zwei Parteien einen Kanal eingerichtet haben).

### Silent Payments (BIP-352)

Dasselbe Prinzip, aber **ohne Benachrichtigungs-Transaktion**. Jeder kann sofort an eine Silent Payment Adresse zahlen.

**Problem:** Ohne Benachrichtigung muss der Empfänger alle Taproot-Transaktionen im Netzwerk scannen — hoher Rechenaufwand.

### Vergleich

| | BIP-47 | Silent Payments |
|---|---|---|
| Benachrichtigungs-Transaktion | Einmalig | Keine |
| Scanning-Aufwand Empfänger | Gering | Hoch |
| Privatsphäre | Gut | Sehr gut |
| Interaktivität | Einmalig | Keine |
| Kosten | 1 On-Chain-Tx | Keine |

## Related

- [[silent-payments]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Wird BIP-47 durch Silent Payments vollständig ersetzt werden?
- Wie entwickeln sich Light-Client-Protokolle für effizienteres Silent-Payment-Scanning?
