# Elliptische Kurven-Kryptographie in Bitcoin

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-27
**Sources:** [[learnmeabitcoin-technical-cryptography-overview]], [[learnmeabitcoin-technical-cryptography-hash-function]], [[learnmeabitcoin-technical-cryptography-elliptic-curve]], [[learnmeabitcoin-technical-cryptography-elliptic-curve-ecdsa]], [[learnmeabitcoin-technical-cryptography-elliptic-curve-schnorr]], [[2018_Grokking-Bitcoin_Rosenbaum]], [[waltz-bitcoin-facts]]

## Summary

Bitcoin verwendet zwei kryptografische Werkzeuge: Hash-Funktionen (SHA-256, RIPEMD-160) und Public-Key-Kryptographie (ECDSA, Schnorr). Die Basis beider Signaturverfahren ist die secp256k1-Kurve. ECDSA ist das klassische Signaturverfahren (1998); Schnorr-Signaturen (BIP 340) wurden 2021 mit Taproot eingeführt und sind einfacher, effizienter und ermöglichen Schlüsselaggregation.

## Body

### Hash-Funktionen in Bitcoin

Eine Hash-Funktion erzeugt einen "Fingerabdruck" für beliebige Daten — immer gleich gross, einzigartig pro Eingabe, nicht umkehrbar.

Bitcoin verwendet:
- **SHA-256** (2001): Primäre Hash-Funktion. Überall in Bitcoin: TXIDs, Block-Hashes, Mining-Basis.
- **RIPEMD-160** (1996): Nur für das Kürzen von Public Keys (HASH160 = RIPEMD160(SHA256(pk))).

Wichtige kombinierte Formen:
- **HASH256** = SHA256(SHA256(data)) — für Block-Hashes, TXIDs
- **HASH160** = RIPEMD160(SHA256(data)) — für Public-Key-Hashes und Script-Hashes

**Drei Sicherheitseigenschaften:** Kryptografische Hash-Funktionen müssen alle drei erfüllen (Rosenbaum, Kap. 2):

- **Preimage Resistance:** Gegeben ein Hash-Wert H, ist es praktisch unmöglich, eine Eingabe m zu finden, sodass hash(m) = H. Man kann den Hash nicht "rückwärts" rechnen.
- **Second Preimage Resistance:** Gegeben eine Eingabe m1, ist es praktisch unmöglich, eine zweite Eingabe m2 ≠ m1 zu finden, sodass hash(m1) = hash(m2). Man kann keine alternative Nachricht mit demselben Fingerabdruck erzeugen.
- **Collision Resistance:** Es ist praktisch unmöglich, irgendein Paar m1, m2 (m1 ≠ m2) zu finden, sodass hash(m1) = hash(m2). Keine zwei Nachrichten teilen denselben Hash — auch wenn man aktiv sucht.

Collision Resistance ist die stärkste Eigenschaft und impliziert Second Preimage Resistance. Second Preimage Resistance impliziert Preimage Resistance — nicht umgekehrt. Eine Funktion kann also preimage resistant sein, ohne collision resistant zu sein.

Für Bitcoin ist Preimage Resistance entscheidend beim Mining (niemand kann das Ziel rückwärts berechnen), Second Preimage Resistance bei der Blockchain-Integrität (niemand kann eine Transaktion fälschen), Collision Resistance beim Signieren (niemand kann zwei verschiedene Transaktionen mit derselben Signatur validieren).

**Weitere Eigenschaften:** Deterministisch, Avalanche-Effekt (1-Bit-Änderung → völlig anderes Ergebnis). [[2018_Grokking-Bitcoin_Rosenbaum]]

Das clevere an Bitcoin: Die Unvorhersehbarkeit des Hash-Ergebnisses ist die Grundlage des Minings. Satoshi erkannte, dass man damit eine dezentrale Lotterie bauen kann — kein Block-Ersteller ist je sicher, bevor er den Hash berechnet.

### secp256k1 — Die Elliptische Kurve Bitcoins

Bitcoin war das erste Projekt überhaupt, das secp256k1 in der Praxis einsetzte. Zum Zeitpunkt der Veröffentlichung empfahlen NIST und ANSI die Kurve secp256**r1** (auch bekannt als P-256). Satoshis Wahl von secp256**k1** gilt bis heute als ungewöhnlich — einige spekulieren, er misstraute der NIST-Empfehlung (möglicherweise wegen NSA-Einfluss), andere verweisen auf theoretische Effizienzvorteile der Koblitz-Kurve, die 2009 praktisch noch nicht realisiert waren. Heute ist secp256k1 wegen Bitcoin weit verbreitet und gut analysiert. [[waltz-fact-26-secp256k1-elliptic-curve]]

Die Kurvengleichung: `y² = x³ + 7` über einem endlichen Feld.

Parameter:
```
p (Primzahl): 2^256 - 2^32 - 977
              = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
n (Ordnung):  0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G (Generator): x = 79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
               y = 483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
```

### EC-Mathematik: Drei Grundoperationen

**Modular Inverse:** `a^(-1) mod p` — Gibt die Zahl zurück, die mit a multipliziert 1 ergibt (mod p).

**EC-Double:** Punkt P auf sich selbst addiert: Tangente an P berechnen, Schnittpunkt mit Kurve finden, y-Koordinate spiegeln.

**EC-Add:** Punkt P + Q: Linie durch P und Q berechnen, Schnittpunkt mit Kurve finden, y-Koordinate spiegeln.

**EC-Multiply** (k × G): Effizient via **Double-and-Add-Algorithmus**: Binärdarstellung von k — für jedes Bit doubling, für jede 1 zusätzlich addition. 256-bit-Zahl = max. 256 doublings + 256 additions statt 2^256 Additionen.

### Trapdoor-Funktion

`Public Key = Private Key × G` — vorwärts trivial berechenbar, rückwärts praktisch unmöglich. Das ist der Kern der elliptischen Kurven-Kryptographie.

### ECDSA — Elliptic Curve Digital Signature Algorithm

Eingeführt 1998 (aus DSA 1991 + EC-Mathematik), verwendet in Bitcoin seit dem ersten Block.

**Signatur erstellen (Sign):**
1. Wähle zufällige Nonce `k` (kryptografisch sicher!)
2. Berechne `R = k × G` → nimm x-Koordinate als `r`
3. Berechne `s = k^(-1) × (hash(tx) + r × private_key) mod n`
4. Signatur = `(r, s)`, kodiert als DER

**Signatur verifizieren (Verify):**
1. Berechne `u1 = s^(-1) × hash(tx) mod n`
2. Berechne `u2 = s^(-1) × r mod n`
3. Berechne `R' = u1×G + u2×PublicKey`
4. Signatur gültig wenn `R'.x == r`

**DER-Kodierung:** Gängiges Format für ECDSA-Signaturen in Bitcoin (~71 Bytes). Im Witness der SegWit-v0-Transaktionen.

**Kritische Sicherheitsregel:** Die Nonce `k` muss für jede Signatur neu zufällig gewählt werden. Wird dieselbe Nonce zweimal verwendet, kann der Private Key mathematisch abgeleitet werden. Dieser Fehler hat in der Vergangenheit zu gestohlenen Coins geführt (z.B. Sony PS3, bestimmte Android-Wallets).

### Schnorr-Signaturen (BIP 340)

Eingeführt mit Taproot (BIP 341, November 2021). Basiert auf dem Schnorr-Algorithmus (1990, Patentablauf 2010).

**Vorteile gegenüber ECDSA:**
- Einfachere Mathematik (lineare Gleichung statt inverser Produkte)
- Kompakter (64 Bytes statt ~71 Bytes DER)
- **Lineare Eigenschaft:** Signaturen können addiert werden → MuSig2-Schlüsselaggregation
- **Batch-Verifikation:** N Signaturen gleichzeitig verifizieren (für Nodes effizienter)

**Schnorr-Signatur (s, R):**
```
s = k + e × private_key  (mod n)
e = hash(R || public_key || message)
```

**Verifikation:**
```
s × G =? R + e × PublicKey
```

**Bitcoin-spezifische Änderungen (BIP 340):**
- Nur x-only Public Keys (32 Bytes statt 33) — y wird implizit als gerade angenommen
- Tagged Hashes: `SHA256(SHA256(tag) || SHA256(tag) || data)` — verhindert Hash-Wiederverwendung über Protokollkontexte hinweg
- Deterministische Nonce-Generierung (kein Random-k nötig; basiert auf Private Key + Message + optionalem aux_rand)

**Batch-Verifikation:** Mehrere Signaturen gleichzeitig prüfen. Für Nodes beim Block-Validieren effizienter. Einzel-Verifikation und Batch-Verifikation geben dasselbe Ergebnis.

## Related

- [[kryptografische-schlussel-und-adressen]]
- [[digitale-signaturen-ecdsa]]
- [[taproot-musig2-frost]]
- [[bitcoin-mining-und-proof-of-work]]
- [[hd-wallets-und-schluesselableitung]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch

## Open Questions

- Wie sicher ist secp256k1 gegenüber Quantencomputern (Grover, Shor)?
- Wann wird Schnorr-Batch-Verifikation flächendeckend von Nodes genutzt?
- Wie funktioniert FROST (Threshold Schnorr) im Vergleich zu MuSig2?
