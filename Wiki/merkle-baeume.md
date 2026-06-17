# Merkle-Bäume

**Status:** established
**Last updated:** 2026-06-17
**Sources:** [[Protocols for Public Key Cryptosystems]], [[Improving the Efficiency and Reliability of Digital Time-Stamping ]], [[bitcoin-whitepaper]]

## Summary

Ein Merkle-Baum ist eine Baumstruktur aus Hashes, bei der jeder innere Knoten der Hash seiner beiden Kinder ist. Die Wurzel (Root Hash) repräsentiert damit kryptografisch den gesamten Inhalt aller Blätter. Ralph Merkle entwickelte das Konzept 1980 für Public-Key-Kryptografie; Bayer, Haber und Stornetta wendeten es 1992 auf Timestamping an. Bitcoin nutzt Merkle-Bäume an zwei zentralen Stellen: zur effizienten Transaktionsverifikation im Block (Transaction Merkle Tree) und als Grundlage für SPV (Simplified Payment Verification). Der Merkle-Baum macht es möglich, die Existenz einer einzelnen Transaktion in einem Block mit minimalem Datenaustausch zu beweisen.

## Body

### Grundstruktur

```
        Merkle Root
        /          \
   Hash(AB)      Hash(CD)
   /     \       /     \
Hash(A) Hash(B) Hash(C) Hash(D)
   |       |       |       |
  TxA    TxB     TxC     TxD
```

Jedes Blatt ist der Hash einer Transaktion (oder eines Dokuments). Jeder innere Knoten ist `Hash(linkes_Kind + rechtes_Kind)`. Die Wurzel fasst den gesamten Inhalt zusammen.

**Eigenschaft:** Ändert man eine Transaktion, ändert sich ihr Hash, dann der Hash des Elternknotens, dann des Großelternknotens — bis zur Wurzel. Der Root Hash ändert sich deterministisch. Eine manipulierte Transaktion kann den Root Hash nicht unverändert lassen.

### Merkles Ursprung: Public-Key-Kryptografie (1980)

Ralph Merkle entwickelte den Merkle-Baum ursprünglich für ein anderes Problem: effiziente Authentifizierung in Public-Key-Systemen. Das Paper "Protocols for Public Key Cryptosystems" (1980) beschreibt, wie man mit Einweg-Hash-Funktionen Bäume aufbaut, um viele Elemente mit einem einzigen vertrauenswürdigen Wurzel-Wert zu authentifizieren.

Das Grundproblem: Wenn ein Server tausend öffentliche Schlüssel verwaltet, muss ein Client nicht alle tausend kennen — nur den Merkle-Root. Jeder einzelne Schlüssel kann mit einem Merkle-Beweis (einer Folge von Geschwister-Hashes entlang des Pfades zur Wurzel) verifiziert werden.

### Anwendung auf Timestamping (Bayer, Haber & Stornetta, 1992)

Haber und Stornetta (1991) hatten Dokumente sequenziell in einer Hash-Kette verknüpft. Das Problem: Bei tausenden Dokumenten täglich wächst die Kette linear — Verifikation wird aufwendig.

Bayer, Haber und Stornetta lösten das 1992 mit Merkle-Bäumen:
- Alle Dokumente einer Periode werden in einem Merkle-Baum zusammengefasst
- Nur der Root-Hash muss publiziert werden (z.B. in einer Zeitung)
- Ein einzelnes Dokument kann mit einem logarithmisch kleinen Beweis verifiziert werden

**Exponentieller Effizienzgewinn:** Bei 1 Million Dokumenten braucht der Merkle-Beweis nur 20 Hashes (log₂(1.000.000) ≈ 20) statt die gesamte Kette.

### Bitcoin: Transaction Merkle Tree

Im Bitcoin-Block-Header steht der Merkle-Root aller Transaktionen des Blocks. Das ermöglicht zwei wichtige Eigenschaften:

**1. Unveränderlichkeit:** Eine einzige veränderte Transaktion ändert den Merkle-Root — und damit den Block-Header-Hash. Da jeder Block-Header den Hash des vorherigen Blocks enthält, würde eine Änderung die gesamte Kette nach hinten ungültig machen.

**2. SPV (Simplified Payment Verification):** Ein SPV-Client (z.B. ein mobiles Wallet) muss nicht alle Transaktionen kennen — nur die Block-Header. Will er prüfen, ob Transaktion X in Block Y enthalten ist, fragt er einen Full-Node nach dem Merkle-Pfad von X zur Wurzel. Mit ~log(n) Hashes kann er die Existenz der Transaktion beweisen, ohne den gesamten Block herunterzuladen.

```
Merkle Proof für TxC:
- Hash(TxD) (Geschwister von TxC)
- Hash(AB) (Geschwister von Hash(CD))
→ Daraus lässt sich Root rekonstruieren und mit Block-Header vergleichen
```

### Merkle-Bäume in anderen Bitcoin-Kontexten

- **Taproot/MAST:** Merkle-Bäume für Script-Pfade — statt alle möglichen Ausgabebedingungen zu offenbaren, wird nur der ausgeführte Pfad enthüllt
- **BIP-158 (Compact Block Filters):** Bloom-Filter-ähnliche Strukturen für SPV-Verbesserungen
- **Lightning Network:** Commitment-Transaktionen verwenden Hash-Strukturen, die von Merkle-Bäumen inspiriert sind

## Related

- [[digitales-zeitstempel]]
- [[bitcoin-whitepaper]]
- [[segregated-witness-segwit]]
- [[taproot-musig2-frost]]
- [[hashcash]]

## Open Questions

- Wie verändert sich die SPV-Sicherheit mit zunehmender Miner-Zentralisierung?
- Sind Merkle-Bäume durch bessere Datenstrukturen (z.B. Verkle Trees, wie in Ethereum diskutiert) ersetzbar?
