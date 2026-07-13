# Bitcoin-Transaktionsstruktur

**Status:** established
**Themen:** protokoll, oekonomie
**Last updated:** 2026-06-20
**Sources:** [[learnmeabitcoin-beginners-guide-transactions]], [[2018_Grokking-Bitcoin_Rosenbaum]], [[learnmeabitcoin-beginners-guide-outputs]], [[learnmeabitcoin-technical-transaction-overview]], [[learnmeabitcoin-technical-transaction-input]], [[learnmeabitcoin-technical-transaction-output]], [[learnmeabitcoin-technical-transaction-fee]], [[learnmeabitcoin-technical-transaction-size]], [[learnmeabitcoin-technical-transaction-locktime]], [[learnmeabitcoin-technical-transaction-utxo]], [[learnmeabitcoin-technical-transaction-witness]], [[learnmeabitcoin-technical-transaction-wtxid]], [[learnmeabitcoin-technical-transaction-psbt]], [[learnmeabitcoin-technical-transaction-input-txid]], [[learnmeabitcoin-technical-transaction-input-vout]], [[learnmeabitcoin-technical-transaction-input-scriptsig]], [[learnmeabitcoin-technical-transaction-input-sequence]], [[learnmeabitcoin-technical-transaction-output-scriptpubkey]]

## Summary

Eine Bitcoin-Transaktion ist ein Datensatz, der bestehende Outputs (UTXOs) entsperrt und neue Outputs mit neuen Locks erzeugt. Sie besteht aus Inputs (Verweise auf UTXOs + Unlocking Code), Outputs (Betrag + Locking Script), Locktime und optional Witness-Daten (SegWit). Die Gebühr ist implizit: Summe(Inputs) − Summe(Outputs). Transaktionsgröße wird in Bytes, Weight Units und Virtual Bytes gemessen.

## Body

### Grundprinzip: Outputs entsperren und neu sperren

Eine Transaktion entsperrt bestehende Batches von Bitcoin (Inputs) und erzeugt neue Batches mit neuen Locks (Outputs). Man kann mehrere Inputs und Outputs in einer Transaktion haben. Outputs sind in voller Höhe zu verwenden — "anbrechen" ist nicht möglich; stattdessen erstellt man einen Wechselgeld-Output zurück an sich selbst.

### Serialisiertes Format (Legacy)

```
[version]           4 Bytes, Little-Endian
[input count]       compact size
[inputs...]
  [txid]            32 Bytes, natural byte order
  [vout]            4 Bytes, Little-Endian
  [scriptsig size]  compact size
  [scriptsig]       variable
  [sequence]        4 Bytes, Little-Endian
[output count]      compact size
[outputs...]
  [amount]          8 Bytes, Little-Endian (Satoshi)
  [scriptpubkey size] compact size
  [scriptpubkey]    variable
[locktime]          4 Bytes, Little-Endian
```

SegWit-Transaktionen fügen nach `[input count]` die Felder `[marker: 00][flag: 01]` ein und einen `[witness]`-Block vor `[locktime]`.

### Inputs

Ein Input verweist auf einen vorhandenen unverbrauchten Output (UTXO) und stellt den Unlocking Code bereit.

**TXID (32 Bytes):** Unique Reference der Transaktion, die den Output erstellt hat. Intern in natural byte order, in Explorern in reverse byte order angezeigt. Berechnet als HASH256 aller Transaktionsdaten (ohne Witness). Der erste Bitcoin-Transfer hatte die TXID `f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16`.

**VOUT (4 Bytes):** Index-Nummer des Outputs innerhalb der referenzierten Transaktion. Zählung beginnt bei 0.

**ScriptSig:** Unlocking Code für Legacy-Locking-Scripts (P2PK, P2PKH, P2MS, P2SH). Bei SegWit-Inputs leer (0x00) — der Unlocking Code liegt dann im Witness-Feld.

**Sequence (4 Bytes):** Steuert Finalisierung und Minability der Transaktion:
- `0xFFFFFFFE` oder kleiner → Locktime aktiviert
- `0xFFFFFFFD` oder kleiner → Replace By Fee (RBF) aktiviert: Transaktion kann im Mempool durch höhere Gebühr ersetzt werden
- `0xEFFFFFFF` oder kleiner → Relative Locktime (BIP 68): Transaktion kann erst nach N Blöcken oder N×512 Sekunden nach dem Minen des referenzierten Outputs gemint werden

### Outputs

Ein Output enthält einen Betrag (in Satoshi) und einen Locking Script (ScriptPubKey).

**Amount (8 Bytes):** Betrag in Satoshi (1 BTC = 100.000.000 Satoshi), Little-Endian.

**ScriptPubKey:** Der Locking Code — ein Script-Programm, das festlegt, wer diesen Output entsperren darf. Standardformen: P2PKH, P2WPKH, P2TR usw. ScriptPubKeys werden meistens als Adressen dargestellt. → [[bitcoin-script-und-output-locks]]

### Transaktionsgebühr

Die Gebühr hat keinen eigenen Output — sie ist implizit:

```
Gebühr (Satoshi) = Summe aller Input-Werte − Summe aller Output-Werte
```

Miner nehmen die Gebühr in ihrer Coinbase-Transaktion mit. Miner wählen Transaktionen nach **sat/vByte** aus — höchste Gebühr pro virtuellem Byte zuerst. → [[transaktionsgebuehren-und-mempool]]

### Locktime (4 Bytes)

Verhindert, dass eine Transaktion vor einem bestimmten Block oder Zeitpunkt gemint wird:
- Wert 0–499.999.999 → Block-Höhe
- Wert ≥500.000.000 → Unix-Timestamp

Locktime wird nur berücksichtigt wenn die Sequence mindestens eines Inputs ≤ 0xFFFFFFFE ist.

### Transaktionsgröße: Bytes, Weight Units, Virtual Bytes

Seit SegWit gibt es drei Maßeinheiten:

| Einheit | Bedeutung |
|---------|-----------|
| **Bytes (b)** | Physische Größe auf Disk |
| **Weight Units (wu)** | Für Block-Limit-Berechnung; Non-Witness-Daten × 4, Witness-Daten × 1 |
| **Virtual Bytes (vB)** | wu / 4; für Feerate-Vergleiche (sat/vByte) |

Ein Block hat ein Limit von 4 Millionen Weight Units (~1 MB non-witness, ~4 MB gesamt). Legacy-Transaktionen: `size_in_bytes × 4` wu. SegWit-Transaktionen profitieren vom Witness-Discount.

### UTXO-Modell

Alle unverbrauchten Outputs bilden das **UTXO-Set** — ein vom Node im RAM gehaltener Index für schnelle Validierung. Jedes Mal wenn eine Transaktion bestätigt wird, werden Inputs aus dem UTXO-Set entfernt und neue Outputs hinzugefügt. Das UTXO-Set ist aktuell ~10 GB. → [[utxo-modell-und-konsolidierung]]

### Witness (SegWit)

Das Witness-Feld enthält den Unlocking Code für SegWit-Inputs (P2WPKH, P2WSH, P2TR). Es ist vom Rest der Transaktionsdaten getrennt, weshalb es nicht in die TXID einfließt, wohl aber in die wTXID.

**wTXID:** HASH256 aller Transaktionsdaten inklusive Marker, Flag und Witness. Die wTXID wird im Witness-Commitment der Coinbase-Transaktion eines SegWit-Blocks verwendet. → [[segregated-witness-segwit]]

### SIGHASH-Typen: Was eine Signatur abdeckt

Jede Signatur in einer Transaktion committet nicht notwendigerweise auf die gesamte Transaktion. Der SIGHASH-Typ bestimmt, welche Teile der Transaktion in den signierten Hash einfließen. Das gibt Spielraum für flexible Multi-Party-Protokolle.

Drei Basis-Typen:

**SIGHASH_ALL (0x01, Standard):** Signiert alle Inputs und alle Outputs. Jede Änderung an der Transaktion macht die Signatur ungültig. Für normale Zahlungen.

**SIGHASH_NONE (0x02):** Signiert alle Inputs, aber keinen Output. Der Unterzeichner sagt: "Ich gebe die Coins frei, egal wohin sie gehen." Outputs können von jemand anderem ergänzt werden — riskant ohne weiteren Kontext.

**SIGHASH_SINGLE (0x03):** Signiert alle Inputs und den Output mit demselben Index wie der signierte Input. Wer Input 0 signiert, committet auf Output 0; alle anderen Outputs können noch verändert werden.

Dazu kommt ein Modifikator:

**ANYONECANPAY (0x80):** Kombinierbar mit jedem der drei Basis-Typen. Signiert nur den eigenen Input, nicht alle anderen. Das erlaubt anderen Parteien, weitere Inputs zur Transaktion hinzuzufügen.

Die sechs Kombinationen: ALL, NONE, SINGLE, ALL|ANYONECANPAY, NONE|ANYONECANPAY, SINGLE|ANYONECANPAY.

Praktisches Beispiel für NONE|ANYONECANPAY: Eine Crowdfunding-Transaktion, bei der jeder Teilnehmer seinen eigenen Input signiert, aber keinen Output festlegt. Erst wenn genug Inputs gesammelt sind, wird ein gemeinsamer Output für die Zielsumme ergänzt. Jeder Teilnehmer kann seine Unterschrift zurückziehen, solange die Transaktion noch nicht gesendet wurde. [[2018_Grokking-Bitcoin_Rosenbaum]]

### TXID: Warum doppeltes SHA256?

Die TXID einer Transaktion ist HASH256 = SHA256(SHA256(tx_data)). Das doppelte SHA256 schützt gegen sogenannte **Length Extension Attacks**: Ein Angreifer, der SHA256(m) kennt, kann in bestimmten Umständen SHA256(m || extension) für beliebige Anhänge berechnen, ohne die ursprüngliche Nachricht m zu kennen. Das doppelte Hashing verhindert diesen Angriffsvektor, weil der innere Hash nicht in den äußeren weitergeführt werden kann. Satoshi hat dies offenbar als Vorsichtsmaßnahme eingebaut, ohne sich mit Length Extension Attacks im Detail auseinanderzusetzen. [[2018_Grokking-Bitcoin_Rosenbaum]]

### PSBT — Partially Signed Bitcoin Transaction

PSBT (BIP 174 / BIP 370) ist ein Datenformat für den Umlauf von Transaktionen zum Signieren. Es enthält rohe unsignierte Transaktionsdaten plus alle Zusatzinformationen, die zum Signieren benötigt werden (UTXOs, ScriptPubKeys, Derivation Paths). Unterstützt von Electrum, Sparrow, Coldcard, Trezor. Unverzichtbar für Multisig-Workflows und Air-Gap-Signaturen.

### Coinbase-Transaktion

Die erste Transaktion in jedem Block hat keine Inputs. Der Miner erstellt sie selbst und enthält den Block-Reward plus alle Transaktionsgebühren des Blocks. Das ist die einzige Quelle neuer Bitcoin. → [[bitcoin-geldpolitik-und-21-millionen-limit]]

## Related

- [[utxo-modell-und-konsolidierung]]
- [[bitcoin-script-und-output-locks]]
- [[transaktionsgebuehren-und-mempool]]
- [[kryptografische-schlussel-und-adressen]]
- [[digitale-signaturen-ecdsa]]
- [[segregated-witness-segwit]]
- [[bitcoin-datenformate]]

## Open Questions

- Wie verändert Taproot die Transaktionsstruktur bei Multisig?
- Was sind die genauen Regeln für RBF-Erkennung durch Nodes?
- Wie funktioniert Pinning als Angriff auf RBF?
