# Bitcoin Script und Output-Locks

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-guide-locks]], [[learnmeabitcoin-technical-script-overview]], [[learnmeabitcoin-technical-script-p2pk]], [[learnmeabitcoin-technical-script-p2pkh]], [[learnmeabitcoin-technical-script-p2ms]], [[learnmeabitcoin-technical-script-p2sh]], [[learnmeabitcoin-technical-script-p2wpkh]], [[learnmeabitcoin-technical-script-p2wsh]], [[learnmeabitcoin-technical-script-p2tr]], [[learnmeabitcoin-technical-script-return]], [[learnmeabitcoin-technical-script-p2sh-p2wpkh]], [[learnmeabitcoin-technical-script-p2sh-p2wsh]]

## Summary

Bitcoin Script ist eine stapelbasierte Mini-Programmiersprache, die Outputs mit Locking Scripts versieht. Jeder Input muss ein passendes Unlocking Script liefern. Es gibt 5 Legacy-Typen (P2PK, P2PKH, P2MS, P2SH, OP_RETURN) und 3 moderne SegWit-Typen (P2WPKH, P2WSH, P2TR). Legacy-Outputs werden über ScriptSig entsperrt, SegWit-Outputs über das Witness-Feld.

## Body

### Bitcoin Script: Stapelsprache

Script ist eine einfache, stapelbasierte Sprache (ähnlich Forth). Sie hat keine Schleifen — das verhindert Angriffe durch Endlosschleifen. Jedes Script besteht aus Opcodes und Datenelementen. Ausführung von links nach rechts:
- **Daten** werden auf den Stack gepusht
- **Opcodes** nehmen Elemente vom Stack, führen Operationen aus, und pushen ggf. Ergebnisse zurück

Ein Script ist **valid** wenn nach der Ausführung genau ein non-zero Element auf dem Stack liegt.

**Vollständige Opcode-Liste:** [[learnmeabitcoin-technical-script-overview]] — Push-Data (97), Control Flow (10), Stack-Operatoren (19), Strings (5), Bitwise Logic (8), Numeric (27), Cryptography (10), Other (80).

### Legacy Script-Typen (2009–2016)

Werden über das **ScriptSig**-Feld entsperrt. Noch gültig und nutzbar, aber SegWit-Typen sind effizienter.

#### P2PK — Pay To Public Key

Das älteste Muster. Sperrt direkt auf einen Public Key.

```
ScriptPubKey:  <pubkey> OP_CHECKSIG
ScriptSig:     <signature>
```

Kaum noch in Verwendung — P2PKH hat es weitgehend abgelöst. Die ersten Bitcoin-Transaktionen (u.a. Satoshis Blöcke) verwenden P2PK.

#### P2PKH — Pay To Public Key Hash

Das bis 2016 meistgenutzte Muster. Sperrt auf den Hash eines Public Keys.

```
ScriptPubKey:  OP_DUP OP_HASH160 <pubkey-hash> OP_EQUALVERIFY OP_CHECKSIG
ScriptSig:     <signature> <pubkey>
```

Vorteil gegenüber P2PK: Der Public Key wird erst beim Ausgeben offenbart. Adressformat: `1...` (Base58Check). Heute ersetzt durch P2WPKH.

#### P2MS — Pay To Multisig

m-of-n Multisig: m Signaturen von n Public Keys erforderlich.

```
ScriptPubKey:  OP_<m> <pubkey1> ... <pubkeyN> OP_<n> OP_CHECKMULTISIG
ScriptSig:     OP_0 <sig1> ... <sigM>
```

Das OP_0 am Anfang des ScriptSig ist ein bekannter Off-by-One-Fehler in der ursprünglichen Implementierung — er muss trotzdem da sein. Heute wird P2MS in P2SH oder P2WSH eingebettet statt direkt verwendet.

#### P2SH — Pay To Script Hash

Sperrt auf den Hash eines beliebigen Scripts (Redeem Script). Der Sender muss nur den Hash kennen; der Empfänger legt beim Ausgeben das eigentliche Script offen.

```
ScriptPubKey:  OP_HASH160 <script-hash> OP_EQUAL
ScriptSig:     ... <redeem-script>
```

Adressformat: `3...` (Base58Check). Häufige Verwendung: P2SH-Multisig. Heute ersetzt durch P2WSH.

**Wichtig:** Das Redeem Script wird nur beim Ausgeben öffentlich — der Sender sieht bei der Sperrung nur den Hash.

#### OP_RETURN

Erzeugt einen unausgebaren Output für das Speichern beliebiger Daten auf der Blockchain.

```
ScriptPubKey:  OP_RETURN <data>
```

Bitcoins in einem OP_RETURN-Output sind **permanent unausgebar** (Burned Coins). Genutzt für: Timestamping, Token-Protokolle (Ordinals, Runes), Messenger-Protokolle. Standardlimit: 83 Bytes Daten. → [[op-return-und-datenspeicherung]]

### SegWit Script-Typen (ab 2016 / 2021)

Werden über das **Witness**-Feld entsperrt. Witness-Daten haben niedrigeres Gewicht (1 wu statt 4 wu), was zu niedrigeren Gebühren führt. Eingeführt mit SegWit (2016) und Taproot (2021).

#### P2WPKH — Pay To Witness Public Key Hash

Entspricht P2PKH, aber Unlocking via Witness. Adressformat: `bc1q...` (Bech32).

```
ScriptPubKey:  OP_0 <20-byte-pubkey-hash>     (hex: 0014...)
Witness:       [<signature>, <pubkey>]
ScriptSig:     (leer)
```

#### P2WSH — Pay To Witness Script Hash

Entspricht P2SH, aber mit Witness und SHA256 statt HASH160. Witness-Script-Hash ist 32 Bytes. Adressformat: `bc1q...` (Bech32, 62 Zeichen).

```
ScriptPubKey:  OP_0 <32-byte-script-hash>     (hex: 0020...)
Witness:       [... <witness-script>]
ScriptSig:     (leer)
```

Hauptanwendung: Multisig im Witness-Feld. Das Witness-Script kann beliebige Script-Logik enthalten.

#### P2TR — Pay To Taproot

Das modernste Script-Muster (BIP 341, November 2021). Ermöglicht Key-Path-Spend (einfache Schnorr-Signatur) oder Script-Path-Spend (Script aus einem versteckten Merkle-Baum).

```
ScriptPubKey:  OP_1 <32-byte-tweaked-pubkey>  (hex: 5120...)
```

Adressformat: `bc1p...` (Bech32m, 62 Zeichen).

- **Key Path:** Witness enthält eine einzelne Schnorr-Signatur. Sieht von außen wie jede andere Zahlung aus.
- **Script Path:** Witness enthält Script-Inputs + Leaf-Script + Control-Block (Merkle-Proof).

Taproot gibt maximale Privacy: Man sieht von außen nicht, ob und welche Scripts verfügbar wären. → [[taproot-musig2-frost]]

### Verschachtelte SegWit-Typen (Übergangsformat)

**P2SH-P2WPKH** (Nested P2WPKH): P2WPKH in P2SH verpackt. Adresse: `3...`. Nutzt Witness-Discount, aber über Legacy-Adressformat. Nur sinnvoll wenn Wallet/Exchange keine nativen bc1q-Adressen unterstützt.

**P2SH-P2WSH** (Nested P2WSH): P2WSH in P2SH verpackt. Gleiche Logik. Kein Grund mehr zur Nutzung wenn P2WSH direkt möglich ist.

### Standard vs. Non-Standard Scripts

Nodes relayieren nur Standard-Scripts (oben beschrieben). Custom Scripts können gemint werden, werden aber nicht von Nodes weitergeleitet — man müsste sie direkt an einen Miner übermitteln.

**Limits für Valid Scripts:**
- Max. Script-Größe: 10.000 Bytes
- Max. Anzahl Opcodes: 201
- Max. Element-Größe: 520 Bytes
- Max. Stack-Elemente: 1.000

**Standardness-Limits (Relay):**
- Max. ScriptSig: 1.650 Bytes

## Related

- [[bitcoin-transaktionsstruktur]]
- [[kryptografische-schlussel-und-adressen]]
- [[digitale-signaturen-ecdsa]]
- [[bitcoin-adresstypen]]
- [[multisig-und-kollaborative-verwahrung]]
- [[miniscript-und-liana]]
- [[op-return-und-datenspeicherung]]
- [[segregated-witness-segwit]]
- [[taproot-musig2-frost]]

## Open Questions

- Wie unterscheidet sich Miniscript von Raw Bitcoin Script?
- Welche neuen Script-Möglichkeiten würden Covenants (CTV, CSFS) eröffnen?
- Wie funktioniert CHECKSIGADD (OP_CSADD) für Schnorr-Multisig in Tapscript?
