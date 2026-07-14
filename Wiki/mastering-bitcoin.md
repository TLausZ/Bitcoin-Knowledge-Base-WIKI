# Mastering Bitcoin (Antonopoulos & Harding)

**Status:** established
**Themen:** protokoll, mining, lightning, buecher
**Last updated:** 2026-07-13
**Sources:** [[2023_Mastering-Bitcoin_Antonopoulos-Harding]]

## Summary

Das technische Standardwerk zu Bitcoin, hier in der dritten Auflage (2023) von Andreas M. Antonopoulos und David A. Harding (O'Reilly). Es beschreibt das Protokoll auf Ingenieursniveau, mit Code, Serialisierungsformaten und Kommandozeilen-Beispielen, und richtet sich an Entwickler und technisch versierte Leser. Die dritte Auflage ist stark überarbeitet und deckt SegWit, Taproot, Schnorr-Signaturen und Gebühren-Mechaniken ab.

## Body

### Einordnung

*Mastering Bitcoin* ist das Referenzbuch für die Implementierungsebene: nicht warum Bitcoin zählt (dafür Antonopoulos' *Internet of Money*), sondern wie es intern funktioniert. Als Kurzeintrag geführt, weil die Substanz in den einzelnen technischen Wiki-Artikeln liegt; dieser Eintrag ordnet das Buch ein und verlinkt seine Kapitel.

### Kapitelübersicht

1. Introduction
2. How Bitcoin Works → [[utxo-modell-und-konsolidierung]]
3. Bitcoin Core: The Reference Implementation → [[bitcoin-netzwerk-und-nodes]]
4. Keys and Addresses → [[kryptografische-schlussel-und-adressen]]
5. Wallet Recovery (HD-Wallets, BIP32/39) → [[hd-wallets-und-schluesselableitung]]
6. Transactions (Serialisierung, Witness) → [[utxo-modell-und-konsolidierung]]
7. Authorization and Authentication (Script, P2SH, MAST, Taproot) → [[bitcoin-script-und-output-locks]]
8. Digital Signatures (Schnorr, ECDSA, SIGHASH) → [[digitale-signaturen-ecdsa]]
9. Transaction Fees (RBF, CPFP, Package Relay)
10. The Bitcoin Network (Nodes, Compact Blocks, Bloom-/Block-Filter) → [[bitcoin-netzwerk-und-nodes]]
11. The Blockchain (Block-Header, Merkle-Trees, Testnets) → [[bitcoin-blockchain-struktur]]
12. Mining and Consensus → [[bitcoin-mining-und-proof-of-work]]
13. Bitcoin Security (Hardware-Signing, Multisig, Survivability)
14. Second-Layer Applications (Payment Channels, HTLCs, Lightning) → [[lightning-netzwerk-grundlagen]]

Anhang: Bitcoin-Whitepaper, Errata zum Whitepaper, Übersicht der Bitcoin Improvement Proposals.

### Nutzen

Die dritte Auflage ist der aktuellste Referenzpunkt für die neueren Protokoll-Bausteine (Taproot, Schnorr, Bech32m, Gebühren-Bumping). Für tiefe technische Detailfragen ist sie im Wiki die maßgebliche Buchquelle neben [[grokking-bitcoin]].

## Related

- [[grokking-bitcoin]]
- [[bitcoin-script-und-output-locks]]
- [[digitale-signaturen-ecdsa]]
- [[segregated-witness-segwit]]
- [[lightning-netzwerk-grundlagen]]

## Open Questions

- Wie schnell veralten die Code-Beispiele gegenüber laufenden Bitcoin-Core-Releases?
