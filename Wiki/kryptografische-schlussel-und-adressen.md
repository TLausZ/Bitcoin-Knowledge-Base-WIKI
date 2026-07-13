# Kryptografische Schlüssel und Adressen

**Status:** established
**Themen:** protokoll, privacy
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-guide-keys-addresses]], [[learnmeabitcoin-beginners-guide-private-keys]], [[learnmeabitcoin-beginners-guide-public-keys]], [[learnmeabitcoin-technical-keys-overview]], [[learnmeabitcoin-technical-keys-private-key]], [[learnmeabitcoin-technical-keys-public-key]], [[learnmeabitcoin-technical-keys-public-key-hash]], [[learnmeabitcoin-technical-keys-address]], [[learnmeabitcoin-technical-keys-checksum]], [[learnmeabitcoin-technical-keys-base58]], [[learnmeabitcoin-technical-keys-bech32]], [[learnmeabitcoin-technical-keys-signature]], [[learnmeabitcoin-technical-keys-private-key-wif]]

## Summary

Bitcoin-Schlüssel entstehen aus einem zufällig generierten 256-Bit-Private-Key. Per elliptischer Kurven-Multiplikation (secp256k1) entsteht der Public Key — eine Einwegfunktion, nicht umkehrbar. Adressen sind komprimierte, fehlergeprüfte Darstellungen des Public Keys oder eines Script-Hashes. Signaturen beweisen Inhaberschaft des Private Keys ohne ihn preiszugeben. WIF kodiert Private Keys für portablen Import; Base58 und Bech32 sind die zwei Adress-Kodierformate.

## Body

### Die Kette: Private Key → Public Key → Adresse

| Ebene | Inhalt | Beispiel |
|-------|--------|---------|
| Private Key | 256-Bit-Zufallszahl | `ef235aac...013db2` (32 Bytes hex) |
| Public Key | EC-Punkt (x,y) auf secp256k1 | `02b4632d...8737` (33 Bytes compressed) |
| Public Key Hash | RIPEMD160(SHA256(pubkey)) | 20 Bytes |
| Adresse | Kodiertes PK-Hash mit Prüfsumme | `1EUXSxuU...MHuem` oder `bc1q...` |

Alle Ebenen sind **einseitig**: Von der Adresse nicht zum Public Key, vom Public Key nicht zum Private Key.

### Private Key

Ein Private Key ist eine zufällig generierte 256-Bit-Zahl. Gültiger Bereich: 1 bis `n-1`, wobei `n` die secp256k1-Gruppenordnung ist:

```
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
```

Der Schlüsselraum hat ~2^256 ≈ 10^77 Möglichkeiten — Brute-Force ist praktisch unmöglich. Wird als 32 Bytes (64 Hex-Zeichen) dargestellt.

**WIF (Wallet Import Format):** Base58Check-kodierte Version für portablen Import zwischen Wallets. Format: `Base58Check(version + privkey + [compression_flag])`. Erstellt von Pieter Wuille (2011). Erkennung: Beginnt mit `K`/`L` (compressed mainnet), `5` (uncompressed mainnet), `c`/`9` (testnet).

### Public Key

Berechnet durch EC-Multiplikation des Private Keys mit dem Generator-Punkt G:

```
Public Key = Private Key × G
```

Das Ergebnis ist ein Punkt (x, y) auf der secp256k1-Kurve. Trapdoor-Funktion: einfach vorwärts, unmöglich rückwärts.

**Uncompressed** (65 Bytes): `04` + x (32 Bytes) + y (32 Bytes)

**Compressed** (33 Bytes): `02` (y gerade) oder `03` (y ungerade) + x (32 Bytes). Die y-Koordinate ist aus x und der Parität rekonstruierbar.

Moderne Wallets verwenden ausschließlich Compressed Public Keys. P2WPKH und P2TR verlangen Compressed Keys.

### Public Key Hash

```
pubkey_hash = RIPEMD160(SHA256(public_key))    [= HASH160]
```

Immer 20 Bytes, unabhängig ob compressed oder uncompressed. Verwendet in P2PKH und P2WPKH. Nicht umkehrbar — aus der Adresse lässt sich der Public Key nicht rekonstruieren (zusätzlicher Privatsphäreschutz).

### Adressen

Eine Adresse ist ein benutzerfreundliches Encoding eines Locking-Scripts. Sie enthält eine Prüfsumme zur Fehlererkennung (verhindert Bitcoin-Verlust durch Tippfehler).

#### Base58 / Base58Check

Zeichensatz: `123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz` — ohne `0`, `O`, `I`, `l` (leicht verwechselbar). Erstellt von Satoshi für Legacy-Adressen, WIF-Private-Keys und Extended Keys.

**Prüfsumme:** Erste 4 Bytes von `SHA256(SHA256(data))`, angehängt vor dem Kodieren.

| Typ | Präfix | Version Byte | Länge |
|-----|--------|-------------|-------|
| P2PKH | `1` | `00` | 34 Zeichen |
| P2SH | `3` | `05` | 34 Zeichen |
| WIF compressed | `K`/`L` | `80` + flag `01` | 52 Zeichen |

#### Bech32 / Bech32m

Modernes Format für SegWit-Adressen. Eingeführt mit SegWit (BIP 173 = Bech32, BIP 350 = Bech32m für Taproot). Erkennbar am `bc1`-Präfix.

| Typ | Präfix | Länge |
|-----|--------|-------|
| P2WPKH | `bc1q` | 42 Zeichen |
| P2WSH | `bc1q` | 62 Zeichen |
| P2TR | `bc1p` | 62 Zeichen |

**Vorteile gegenüber Base58:**
- Nur Kleinbuchstaben → keine Verwechslung von Groß-/Kleinschreibung
- Bessere Fehlererkennung (BCH-Code statt einfachem Checksum)
- Kein Checksummen-Berechungsschritt für QR-Codes nötig
- Kompatibel mit SegWit-Versionsbytes

### Signaturen

Eine Signatur beweist Inhaberschaft des Private Keys, ohne ihn zu enthüllen. Erstellt indem man die Transaktionsdaten (den zu entsperrenden Input) mit dem Private Key "signiert". Die Signatur hat eine mathematische Verbindung zum Public Key — nur der richtige Private Key kann eine Signatur erzeugen, die zur Public-Key-Verifikation passt.

**ECDSA:** Klassisches Signaturformat (r, s), kodiert als DER. Verwendet für Legacy-Scripts und SegWit-v0. → [[digitale-signaturen-ecdsa]]

**Schnorr:** Moderneres Format seit Taproot. Einfacher, kompakter (64 Bytes statt ~71 Bytes), unterstützt Schlüsselaggregation (MuSig2). → [[taproot-musig2-frost]]

### Was gesichert werden muss

Weil Public Key und Adresse deterministisch aus dem Private Key berechnet werden: **nur der Private Key muss gesichert werden**. In der Praxis sichert man den Seed einer HD-Wallet, aus dem alle Private Keys deterministisch abgeleitet werden. → [[hd-wallets-und-schluesselableitung]]

Kein Backdoor, kein Passwort-Reset: Wer den Private Key verliert, verliert die Bitcoin dauerhaft.

## Related

- [[hd-wallets-und-schluesselableitung]]
- [[digitale-signaturen-ecdsa]]
- [[bitcoin-script-und-output-locks]]
- [[bitcoin-adresstypen]]
- [[seedphrase-entropie-und-sicherheit]]
- [[diceware-und-seed-generierung]]
- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[taproot-musig2-frost]]

## Open Questions

- Wie schützt Taproot (Schlüsselaggregation) die Privatsphäre auf Adressebene?
- Welches Risiko entsteht durch Quantencomputer für ECDSA/secp256k1?
- Wann wird der Public Key für P2PKH/P2PK-Outputs erstmals öffentlich (erst beim Ausgeben)?
