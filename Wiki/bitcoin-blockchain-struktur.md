# Bitcoin Blockchain: Struktur und Aufbau

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-guide-blockchain]], [[learnmeabitcoin-beginners-guide-blocks]], [[learnmeabitcoin-technical-blockchain-overview]], [[learnmeabitcoin-technical-blockchain-height]], [[learnmeabitcoin-technical-blockchain-longest-chain]], [[learnmeabitcoin-technical-blockchain-chain-reorganization]], [[learnmeabitcoin-technical-blockchain-51-attack]]

## Summary

Die Blockchain ist eine Datei auf jedem Node, die alle Bitcoin-Transaktionen seit dem Genesis-Block enthält. Blöcke sind durch kryptografische Hashes verkettet — wer einen alten Block ändert, bricht alle nachfolgenden Blöcke. Der "längste Chain" ist nicht der mit den meisten Blöcken, sondern der mit der meisten kumulierten Arbeit (Chainwork). Nodes wechseln bei Bedarf automatisch auf die längste Chain (Chain Reorganization). Die aktuell ~852 GB große Blockchain wird als `blk*.dat`-Dateien gespeichert.

## Body

### Die Blockchain als geteilte Datei

Die Blockchain ist eine Datei — genauer eine Folge von Dateien — die alle jemals durchgeführten Bitcoin-Transaktionen enthält. Jeder Full Node hat eine vollständige Kopie. Neue Nodes laden beim ersten Start alle Blöcke von anderen Nodes herunter (Initial Block Download, IBD). Nodes teilen einander beim Verbindungsaufbau die Höhe ihrer Chain mit und gleichen Differenzen automatisch aus.

Es gibt keine einzelne "offizielle" Version der Blockchain. Jeder Node führt seine eigene lokale Kopie, die sich zwischen Computern kurzfristig unterscheiden kann.

**Speicherorte lokal:**
- Linux: `~/.bitcoin/blocks/`
- Windows: `C:\Users\[user]\AppData\Roaming\Bitcoin\blocks\`
- Mac: `~/Library/Application Support/Bitcoin/blocks/`

Dateien: `blk00000.dat`, `blk00001.dat` usw.

### Was ist ein Block?

Ein Block ist ein Bündel von Transaktionen, das durch Mining dauerhaft auf die Blockchain gebracht wurde. Jeder Block enthält:

1. Einen **Block-Header** (80 Bytes Metadaten)
2. Eine **Liste von Transaktionen**

### Block-Header im Überblick

Der Block-Header hat sechs Felder:

| Feld | Größe | Bedeutung |
|------|-------|-----------|
| Version | 4 Bytes | Protokollversion des Miners |
| Previous Block | 32 Bytes | Hash des vorherigen Blocks — erzeugt die Kette |
| Merkle Root | 32 Bytes | Hash aller Transaktionen dieses Blocks |
| Time | 4 Bytes | Unix-Timestamp |
| Bits | 4 Bytes | Aktuelles Mining-Ziel (komprimiert) |
| Nonce | 4 Bytes | Die Zahl, die der Miner durch Probieren gefunden hat |

Durch das Feld "Previous Block" verweist jeder Block auf seinen Vorgänger. Wird ein alter Block geändert, ändert sich sein Hash — und alle nachfolgenden Blöcke werden ungültig.

### Block-Höhe (Height)

Die Höhe eines Blocks gibt seine Position in der Blockchain an. Der Genesis-Block hat Höhe 0, der nächste Höhe 1 usw.

Zwei kritische Ereignisse in Bitcoin sind an bestimmte Höhenintervalle gebunden:

**Difficulty-Anpassung:** alle 2.016 Blöcke (~2 Wochen). Hält den 10-Minuten-Rhythmus aufrecht, wenn Miner dem Netzwerk beitreten oder es verlassen.

**Block-Subsidy-Halving:** alle 210.000 Blöcke (~4 Jahre). Das Halving halbiert die neu erzeugten Bitcoin pro Block und erzeugt so das fixe Angebot von 21 Millionen. Die Subsidy startete bei 50 BTC, sinkt bei jeder Halbierung weiter; bei Höhe 6.930.000 (nach 33 Halvings) erreicht sie null.

Die Höhe wird auch für Locktime und Relative Locktime verwendet, um Transaktionen erst ab einer bestimmten Block-Höhe minebar zu machen.

### Längste Chain: Chainwork, nicht Blockanzahl

Wenn Nodes über die aktive Blockchain uneins sind, wählen sie immer die **Kette mit der meisten Arbeit** — nicht die mit den meisten Blöcken.

Die Arbeit pro Block errechnet sich als:

```
work = 2^256 / (target + 1)
```

Ein niedrigeres Target bedeutet mehr Arbeit pro Block. Die **Chainwork** ist die Summe der Arbeit aller Blöcke. In der Praxis sind konkurrierende Chains fast immer gleich schwer, weshalb "mehr Blöcke" und "mehr Arbeit" meist dasselbe bedeuten — aber es ist technisch nicht dasselbe.

### Chain Reorganization (Reorg)

Es ist normal, dass zwei Miner gleichzeitig einen gültigen Block finden. Das erzeugt einen temporären Fork: manche Nodes übernehmen Block 101a, andere Block 101b. Sobald ein Miner auf einer der beiden Seiten einen weiteren Block findet (z.B. 102a auf 101a), entsteht eine längere Chain. Alle Nodes wechseln darauf — auch jene, die zuvor 101b bevorzugten.

Bei diesem Wechsel (Chain Reorganization):
1. Werden die alten Blöcke ab der gemeinsamen Wurzel abgekoppelt.
2. Werden die neuen Blöcke verbunden.
3. Kommen Transaktionen aus den abgekoppelten Blöcken zurück in den Mempool.

Ersetzte Blöcke heißen **Stale Blocks** (manchmal fälschlicherweise "Orphan Blocks"). Sie werden gespeichert, gehören aber nicht mehr zur aktiven Chain. Reorgs sind fast immer 1 Block tief — tiefere Reorgs werden exponentiell unwahrscheinlicher. Seit März 2021 gab es laut blockchain-Explorern 42 Reorgs im Bitcoin-Netzwerk.

### Merkle Root: Transaktionen komprimiert

Die Merkle Root ist ein einzelner Hash, der alle Transaktionen im Block repräsentiert. Ändert man eine Transaktion, ändert sich die Merkle Root — und damit der gesamte Block-Header. → [[merkle-baeume]]

## Related

- [[wie-funktioniert-bitcoin]]
- [[bitcoin-mining-und-proof-of-work]]
- [[mining-schwierigkeit]]
- [[merkle-baeume]]
- [[bitcoin-netzwerk-und-nodes]]
- [[utxo-modell-und-konsolidierung]]
- [[soft-fork-und-hard-fork]]
- [[bitcoin-rechtliche-angriffe]]

## Open Questions

- Wie wird die Blockchain-Größe langfristig gehandhabt (Pruning, Archive Nodes)?
- Welcher Mechanismus bestimmt die initiale Chainwork eines Nodes beim IBD?
