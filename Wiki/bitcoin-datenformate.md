# Bitcoin-Datenformate

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-technical-general-hexadecimal]], [[learnmeabitcoin-technical-general-bytes]], [[learnmeabitcoin-technical-general-little-endian]], [[learnmeabitcoin-technical-general-byte-order]], [[learnmeabitcoin-technical-general-compact-size]]

## Summary

Bitcoin-Daten werden konsequent in Hexadezimal (Bytes) dargestellt. Nahezu alle Integer in Bitcoin sind Little-Endian — also mit dem niedrigstwertigen Byte zuerst. TXIDs und Block-Hashes werden in Reverse Byte Order angezeigt, intern aber in Natural Order gespeichert. CompactSize ist das variable-Längen-Format für Zählfelder in Bitcoin-Daten.

## Body

### Hexadezimal

Bitcoin-Daten werden immer als Hex-Strings dargestellt. Hexadezimal (Basis 16) verwendet die Zeichen `0-9` und `A-F` (Groß- oder Kleinschreibung gleichwertig). Ein Byte = 2 Hex-Zeichen = 8 Bits.

Präfixe zur Unterscheidung von Zahlensystemen:
- `0x` = Hexadezimal (z.B. `0xFF` = 255)
- `0b` = Binär (z.B. `0b11111111` = 255)
- Ohne Präfix = Dezimal

Bitcoin Private Keys, TXIDs, Block-Hashes — alles wird als Hex-String ausgegeben, weil Hex eine kompakte Darstellung von Bytes ist: 32-Byte Private Key = 64 Hex-Zeichen.

### Bytes

Ein **Byte** = 8 Bits = 2 Hex-Zeichen. Wichtige Größen in Bitcoin:

| Daten | Bytes |
|-------|-------|
| Private Key | 32 |
| Public Key (compressed) | 33 |
| Public Key Hash (HASH160) | 20 |
| Schnorr-Signatur | 64 |
| ECDSA-Signatur (DER) | ~71 |
| TXID / Block-Hash | 32 |
| Block-Header | 80 |

**Bit:** Kleinstes Datenelement (0 oder 1). 8 Bits = 1 Byte. Wird u.a. für Entropie-Angaben verwendet (128 Bit = 16 Bytes = minimale BIP 39 Entropy).

### Little-Endian

Fast alle Integer in Bitcoin-Rohdaten sind in **Little-Endian** (LE): das niederwertigste Byte kommt zuerst (im Gegensatz zu Big-Endian, wo das höchste Byte zuerst steht).

Beispiel: Zahl `500` = `0x01F4` in Big-Endian. In Little-Endian (2 Bytes): `F401`.

**LE in Bitcoin:**
- Version: 4 Bytes LE
- VOUT: 4 Bytes LE
- Amount (Satoshi): 8 Bytes LE
- Locktime: 4 Bytes LE
- Sequence: 4 Bytes LE

In der Praxis: Wenn man Transaktionsdaten manuell parst oder erstellt, muss man Integer zuerst in LE umwandeln.

**Ausnahmen (nicht LE):** Public Keys, Hash-Werte, Signatures — diese sind Byte-Arrays, keine Integer, und werden in Natural Order gespeichert.

### Byte Order: Natural vs. Reverse

TXIDs und Block-Hashes kommen aus der Hash-Funktion in einer bestimmten Reihenfolge — das ist die **Natural Byte Order** (oder interne Darstellung).

Wenn Block Explorer und Bitcoin-Tools diese Hashes anzeigen, **kehren sie die Byte-Reihenfolge um** (Reverse Byte Order). Das ist rein konventionell und geht auf frühe Bitcoin-Core-Implementierungen zurück.

**Genesis-Block Hash:**
```
Natural (aus Hash-Funktion):   6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000
Reverse (Block Explorer):      000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Das bedeutet: Wenn man einen TXID aus einer API oder Explorer bekommt, ist er in Reverse Order. Wenn man ihn für die interne Berechnung (z.B. Merkle Tree) braucht, muss man ihn umkehren.

**Faustregel:**
- **Anzeigen / Suchen:** Reverse Byte Order (wie im Explorer)
- **Interne Berechnung (Merkle Tree, Block-Header):** Natural Byte Order

### CompactSize

**CompactSize** (auch "var_int") ist ein variables Längenformat für Integer in Bitcoin-Datenpaketen. Kleine Zahlen brauchen weniger Bytes.

**Encoding-Tabelle:**

| Wert | Länge | Präfix-Byte |
|------|-------|-------------|
| 0 – 252 | 1 Byte | Kein Präfix (Wert direkt) |
| 253 – 65.535 | 3 Bytes | `FD` + 2 Bytes LE |
| 65.536 – 4.294.967.295 | 5 Bytes | `FE` + 4 Bytes LE |
| 4.294.967.296+ | 9 Bytes | `FF` + 8 Bytes LE |

**Beispiele:**
- 3 Inputs → `03` (1 Byte)
- 253 Transaktionen → `FD FD00` (3 Bytes)

CompactSize erscheint in Transaktionen für: Input Count, Output Count, ScriptSig Size, ScriptPubKey Size, Witness Stack Item Sizes.

## Related

- [[bitcoin-transaktionsstruktur]]
- [[bitcoin-block-header]]
- [[bitcoin-blockchain-struktur]]
- [[kryptografische-schlussel-und-adressen]]

## Open Questions

- Warum wurde Reverse Byte Order für TXIDs eingeführt — historischer Zufall oder bewusste Entscheidung?
- Gibt es Pläne, CompactSize durch ein moderneres Format zu ersetzen?
