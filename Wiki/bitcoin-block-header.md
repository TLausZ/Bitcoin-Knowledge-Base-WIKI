# Bitcoin Block-Header

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-technical-block-overview]], [[learnmeabitcoin-technical-block-version]], [[learnmeabitcoin-technical-block-previous-block]], [[learnmeabitcoin-technical-block-merkle-root]], [[learnmeabitcoin-technical-block-time]], [[learnmeabitcoin-technical-block-bits]], [[learnmeabitcoin-technical-block-nonce]], [[learnmeabitcoin-technical-block-hash]], [[learnmeabitcoin-technical-block-blkdat]]

## Summary

Der Block-Header ist ein 80-Byte-Datensatz am Anfang jedes Bitcoin-Blocks. Er enthält sechs Felder: Version, Previous Block Hash, Merkle Root, Timestamp, Bits (komprimiertes Target) und Nonce. Miner hashen diesen Header (HASH256 = doppeltes SHA-256) und suchen einen Wert unter dem aktuellen Target. Der Block-Hash ist kein Feld im Header, sondern wird aus ihm berechnet.

## Body

### Struktur eines Blocks

Ein Block besteht aus dem Header (80 Bytes) gefolgt von einer Liste von Transaktionen:

```
[Block Header 80 Bytes] [Tx-Anzahl (compact size)] [Transaktionen...]
```

Beispiel: Block 1 (erster Block nach dem Genesis-Block):
```
01000000                                                 ← version
6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d619000000000 ← previous block
982051fd1e4ba744bbbe680e1fee14677ba1a3c3540bf7b1cdb606e857233e0e ← merkle root
61bc6649                                                 ← time
ffff001d                                                 ← bits
01e36299                                                 ← nonce
01                                                       ← tx count
01000000...                                              ← transaction data
```

### 1. Version (4 Bytes, Little-Endian)

Das Versionsfeld signalisiert Miner-Bereitschaft für vorgeschlagene Soft Forks.

Bis 2015 wurde die Versionsnummer für jedes Upgrade inkrementiert:
- `0x00000001` — Original-Software (Höhe 0)
- `0x00000002` — BIP 34: Block-Höhe in Coinbase (Höhe 227.931)
- `0x00000003` — BIP 66: Strict DER-Signaturen (Höhe 363.725)
- `0x00000004` — BIP 65: OP_CHECKLOCKTIMEVERIFY (Höhe 388.381)

Ab 2015 wurde das Feld auf **Version Bits (BIP 9)** umgestellt: Die ersten 3 Bits werden auf `001` gesetzt, die restlichen 29 Bits können für paralleles Signaling verschiedener Upgrades genutzt werden. Heute ist `0x20000000` der Basiswert, einzelne Bits werden dazu addiert.

### 2. Previous Block Hash (32 Bytes)

Enthält den HASH256 des direkt vorherigen Blocks — das erzeugt die "Kette". Ein Miner trägt hier immer den Hash des aktuellen Kettenendpunkts (Tip) ein, um auf der längsten bekannten Chain weiterzubauen.

Block 1 zeigt als Previous Block den Genesis-Block-Hash (in natural byte order):
```
6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000
```

Im Block-Explorer erscheint dieser in reverse byte order: `000000000019d668...`

### 3. Merkle Root (32 Bytes)

Ein einzelner Hash, der alle Transaktionen im Block repräsentiert. Wird durch paarweises Hashen der TXIDs in einem Merkle Tree berechnet. Ändert sich eine Transaktion, ändert sich die Merkle Root — und damit der gesamte Header.

- TXIDs werden in **natural byte order** für die Berechnung verwendet.
- Bei nur einer Transaktion im Block entspricht die Merkle Root direkt der TXID dieser Transaktion.
- → [[merkle-baeume]]

### 4. Time (4 Bytes, Unix-Timestamp)

Der ungefähre Zeitpunkt, zu dem der Miner den Kandidaten-Block gebaut hat. Kein exakter Wert — Timestamps müssen nur:
- Grösser sein als der **Median der letzten 11 Blöcke** (Median Time Past)
- Nicht mehr als **2 Stunden in der Zukunft** liegen

Blöcke können deshalb "aus der Reihe" sein: Block 156.113 hat z.B. einen Timestamp der 2 Stunden nach Block 156.114 liegt. Das ist erlaubt. Der Timestamp beeinflusst nicht die Reihenfolge der Blöcke.

### 5. Bits (4 Bytes) — Komprimiertes Target

Enthält das aktuelle Mining-Target in komprimierter Form. Das Feld besteht aus:
- **Exponent (1. Byte):** Wie weit (in Bytes) der Koeffizient nach links verschoben wird
- **Koeffizient (3 Bytes):** Präzision des Target-Werts

Beispiel: `1705dd01`
- Koeffizient: `05dd01`
- Exponent: `0x17` = 23 Bytes

→ Target: `00000000000000000005dd010000000000000000000000000000000000000000`

Der Block-Hash muss **unter** diesem Target liegen, damit der Block gültig ist. Das Bits-Feld wird alle 2.016 Blöcke angepasst. → [[mining-schwierigkeit]]

### 6. Nonce (4 Bytes)

Das "Mining-Feld". Miner variieren die Nonce von 0 bis 4.294.967.295, um verschiedene Hashes für denselben Header zu erzeugen. Kein mathematischer Trick — nur Probieren.

Wichtige Eigenschaften:
- Jeder Hash-Versuch ist unabhängig. Man kommt nicht "näher" ans Ziel.
- Bei modernen Hash-Raten (z.B. ~977 EH/s im Netzwerk) sind alle 4 Milliarden Nonce-Werte in unter einer Sekunde erschöpft.
- Wenn alle Nonce-Werte versucht wurden ohne Treffer, muss der Miner etwas anderes ändern (Timestamp, Transaktionen, Extra-Nonce im Coinbase-Feld).

### Block-Hash

Der Block-Hash ist **kein Feld im Header** — er wird aus dem Header berechnet:

```
block_hash = SHA256(SHA256(block_header))
```

Der Block-Hash muss unter dem Target (aus dem Bits-Feld) liegen. Deshalb beginnen gültige Block-Hashes immer mit vielen Nullen:

```
Genesis-Block: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
Block 123.456: 0000000000002917ed80650c6174aac8dfc46f5fe36480aaef682ff6cd83c3ca
```

Block-Hashes werden **in reverse byte order** angezeigt (so wie man sie in Block-Explorern sieht), sind aber intern in natural byte order gespeichert.

### blk.dat — Speicherung auf Disk

Bitcoin Core speichert die Blockchain als `blk*.dat`-Dateien:

| OS | Standardpfad |
|----|-------------|
| Linux | `~/.bitcoin/blocks/` |
| Mac | `~/Library/Application Support/Bitcoin/blocks/` |
| Windows ≤27.2 | `C:\Users\[name]\AppData\Roaming\Bitcoin\blocks\` |
| Windows ≥28.0 | `C:\Users\[name]\AppData\Local\Bitcoin\blocks\` |

Die Blöcke werden auf Dateien von maximal 128 MB verteilt (`blk00000.dat`, `blk00001.dat` usw.). Neben den Block-Daten gibt es `rev*.dat`-Dateien (Undo-Daten für Chain Reorgs) und `index/`-Verzeichnisse (LevelDB-Index für schnelles Lookup).

## Related

- [[bitcoin-blockchain-struktur]]
- [[merkle-baeume]]
- [[mining-schwierigkeit]]
- [[bitcoin-mining-und-proof-of-work]]
- [[soft-fork-und-hard-fork]]
- [[bitcoin-datenformate]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch

## Open Questions

- Wie funktioniert Extra-Nonce in der Coinbase-Transaktion wenn die Nonce-Range erschöpft ist?
- Was passiert mit blk.dat bei aktiviertem Pruning-Modus?
