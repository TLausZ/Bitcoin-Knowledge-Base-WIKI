# Lightning Address und Datenschutz

**Status:** established
**Last updated:** 2026-06-12
**Sources:** [[reneaaron_spark-lnaddress-doxxer]], [[2026-06-09_wallet-of-satoshi-faq]]

## Summary

Eine Lightning Address (Format: `nutzer@domain.com`) ist bequem, aber datenschutzkritisch: Jede Zahlung an eine Lightning Address ruft via LNURL-Protokoll eine Invoice vom Server ab — der Server sieht IP-Adresse und Zahlungsabsicht. Noch gravierender: Wallets, die auf Spark aufbauen (z.B. ältere Wallet of Satoshi-Versionen), betten die permanente Spark-Adresse des Empfängers als Routing Hint in die Invoice ein. Ein einfaches Web-Tool kann diese Spark-Adresse aus jeder Lightning Address oder Invoice extrahieren und damit alle Zahlungen des Nutzers verknüpfen.

## Body

### Was ist eine Lightning Address?

Eine Lightning Address ist eine menschenlesbare Adresse im E-Mail-Format (`user@domain.com`) für Lightning-Zahlungen. Technisch steckt dahinter das **LNURL-pay-Protokoll**:

1. Sender holt via HTTP die LNURL-Metadaten von `https://domain.com/.well-known/lnurlp/user`
2. Server liefert eine frische Invoice zurück
3. Sender zahlt die Invoice

**Datenschutzproblem 1 — Server-Sichtbarkeit**: Der Server der Domain sieht jeden Zahlungsversuch: IP-Adresse des Senders, Zeitpunkt, Betrag. Bei custodial Wallets (Wallet of Satoshi, Strike, etc.) bedeutet das: Der Wallet-Anbieter kennt jeden, der dir zahlen will.

**Datenschutzproblem 2 — Spark-Doxxing**: Wallets, die auf dem Spark-Protokoll aufbauen, kodieren die permanente Spark-Adresse des Empfängers als **Routing Hint** in die Invoice. Routing Hints sind öffentlich lesbar — sie sollen Zahlern helfen, einen Weg zu finden. Aber sie enthalten hier versehentlich eine dauerhafte Kennung.

### Das Spark-Doxxing-Problem

Das Tool `spark-lnaddress-doxxer` (reneaaron, GitHub) demonstriert das Problem:

1. Eingabe: Lightning Address (z.B. `nutzer@walletofsatoshi.com`) oder BOLT11-Invoice
2. Bei einer Adresse: Tool ruft via LNURL die Invoice ab
3. Tool parst die Invoice und extrahiert die Spark-Adresse aus den Routing Hints
4. Ergebnis: Die permanente Spark-Adresse ist sichtbar — verknüpfbar mit allen anderen Spark-Transaktionen des Nutzers auf Sparkscan

Das macht **jede einzelne Invoice** zu einem Datenschutzleck, sofern die Wallet Spark-Routing-Hints einbettet. Wer die Spark-Adresse einer Person kennt, kann deren gesamten Zahlungsverlauf nachverfolgen.

Inspiriert wurde das Tool von `spark-invoice-doxxer` (benthecarman), das denselben Trick für direkte Invoices demonstriert.

### Warum Routing Hints ein Problem sind

Lightning-Zahlungen finden ihren Weg durch das Netzwerk via Gossip — Nodes veröffentlichen ihre Channels. Für Nodes, die nicht öffentlich verbunden sind (private Channels), kann der Empfänger **Routing Hints** in die Invoice einbetten: "Komm via Node X zu mir." Das ist technisch notwendig, damit Zahlungen ankommen.

Spark nutzt diesen Mechanismus, aber die eingebettete Information — die Spark-Adresse — ist permanent und eindeutig. Sie verknüpft alle Zahlungen einer Person, ähnlich wie eine Bitcoin-Adresswiederverwendung on-chain.

### Vergleich: Lightning Address Datenschutz je nach Wallet

| Wallet | Server sieht Zahler | Spark-Doxxing | Privatsphärengrad |
|--------|---------------------|---------------|-------------------|
| Wallet of Satoshi (custodial) | Ja | Ggf. (je nach Version) | Niedrig |
| Phoenix | Nein (direkte LN-Invoice) | Nein | Mittel |
| Self-hosted (BTCPay, LNbits) | Nur eigener Server | Nein | Hoch |

Phoenix (ACINQ) weist selbst darauf hin, dass die aktuelle Version keinen Datenschutzvorteil gegenüber custodial Wallets bietet — ACINQ kennt Zahlungsempfänger und -beträge. Zukünftige Versionen sollen Trampoline Payments mit Blinded Paths implementieren.

### Gegenmaßnahmen

- **Keine Lightning Address verwenden, wenn Datenschutz wichtig**: Stattdessen direkte BOLT11-Invoices oder BOLT12 Offers nutzen
- **Self-hosted Lightning Address**: Eigener LNbits- oder BTCPay-Server minimiert Server-Sichtbarkeit
- **Wallet ohne Spark-Routing-Hints wählen**: Wallets ohne Spark-Backend betten keine permanente Kennung ein
- **Blinded Paths (BOLT 12)**: Zukünftiger Standard verbirgt Empfänger-Node-Identität

## Related

- [[phoenix-wallet-lightning]]
- [[wallet-of-satoshi]]
- [[opsec-und-privatsphaere]]
- [[payment-codes-und-adressaustausch]]
- [[silent-payments]]
- [[coinjoin-und-on-chain-privatsphaere]]

## Open Questions

- Haben neuere Wallet-of-Satoshi-Versionen das Spark-Routing-Hint-Problem behoben?
- Wann implementiert Phoenix Blinded Paths, um Empfänger-Datenschutz zu verbessern?
- Gibt es andere Lightning-Wallets außer Spark-basierten, die ähnliche permanente Kennungen in Routing Hints einbetten?
- Wie schützt BOLT12 Offers die Privatsphäre im Vergleich zu LNURL-basierten Lightning Addresses?
