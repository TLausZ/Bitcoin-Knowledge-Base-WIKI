# Silent Payments (BIP-352)

**Status:** emerging
**Themen:** protokoll, self-custody, privacy
**Last updated:** 2026-06-04
**Sources:** [[20240905_silent-payments-erklärt-teil-1]], [[20241017_silent-payments-erklärt-teil-2]], [[20241023_bitbox-10-2024-lugano-update]]

## Summary

Silent Payments (BIP-352) ermöglichen es, eine einzige statische Adresse (Präfix `sp1q…`) öffentlich zu teilen — ohne Privatsphäre-Verlust. Jede Zahlung an diese Adresse erzeugt on-chain einen anderen, einmaligen Output. Nur Sender und Empfänger können die Transaktion erkennen. Die BitBox02 war die erste Hardware-Wallet, die das Versenden an Silent-Payment-Adressen unterstützte (Lugano-Update, Oktober 2024).

## Body

### Das Problem mit statischen Adressen

Bei normalen Bitcoin-Adressen sollte für jede Transaktion eine neue Adresse verwendet werden — sonst können alle zugehörigen Transaktionen öffentlich eingesehen und verknüpft werden. Das erfordert aber ständige Interaktion: Wer Spenden sammeln oder regelmässig Zahlungen empfangen möchte, muss für jede neue Zahlung eine neue Adresse kommunizieren.

### Lösung: ECDH-basierte Adressableitung

Silent Payments nutzen **Elliptic-Curve Diffie-Hellman (ECDH)**: Sender und Empfänger berechnen unabhängig ein gemeinsames Geheimnis, ohne private Schlüssel zu teilen.

Eine Silent Payment Adresse enthält zwei öffentliche Schlüssel:
- `B_scan` — zum Scannen eingehender Zahlungen
- `B_spend` — zum Ausgeben empfangener Coins

**Sender (Alice) berechnet den Output:**
`P = B_spend + hash(input_hash × S) × G`

Dabei ist `S = a × B_scan` (Alices privater Schlüssel × Bobs Scan-Schlüssel).

**Einzigartigkeit:** Der `input_hash` enthält einen Outpoint (einmalige UTXO-Kennung) — da UTXOs nie doppelt ausgegeben werden, ist jeder Output garantiert einmalig, selbst bei mehreren Zahlungen an dieselbe Silent Payment Adresse.

**Empfänger (Bob):** Berechnet denselben Output-Schlüssel mit `b_scan` und `b_spend`. Nur er kann die Coins ausgeben.

### Herausforderung: Scanning-Aufwand

Da keine Benachrichtigungs-Transaktion (wie bei BIP-47) existiert, muss der Empfänger alle Taproot-Transaktionen im Netzwerk scannen, um eingehende Zahlungen zu erkennen. Das erfordert erheblich mehr Rechenaufwand als eine normale Wallet.

### Silent Payments und Hardware-Wallets (DLEQ-Beweise)

Bei normalen Transaktionen erstellt die App die Transaktion, die Hardware-Wallet signiert nur. Bei Silent Payments muss die Hardware-Wallet den Output selbst erstellen (weil der private Schlüssel benötigt wird) — was neue Risiken einführt.

**Lösung: DLEQ-Beweise** (Discrete Logarithm Equality proof)

1. Hardware-Wallet erstellt den Silent Payment Output und einen DLEQ-Beweis, dass der korrekte private Schlüssel verwendet wurde
2. BitBoxApp verifiziert den Beweis unabhängig
3. BitBoxApp rekonstruiert den Output selbst und prüft, ob er mit dem der Hardware-Wallet übereinstimmt

Selbst eine kompromittierte Hardware-Wallet kann die Transaktion nicht manipulieren — die App verifiziert alles eigenständig.

### Einschränkungen

Nur bestimmte Input-Typen sind erlaubt: P2TR (keypath), P2WPKH, P2WPKH-P2SH, P2PKH — also Single-Signature-Typen. Native Multisig ohne Aggregation ist nicht kompatibel.

## Related

- [[payment-codes-und-adressaustausch]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[taproot-musig2-frost]]

## Open Questions

- Wann unterstützen weitere Wallets das Empfangen von Silent Payments (Henne-Ei-Problem)?
- Wie entwickelt sich der Scanning-Aufwand mit der Verbreitung von Light-Client-Protokollen?
