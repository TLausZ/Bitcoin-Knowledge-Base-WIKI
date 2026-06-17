# BIP-0360: Pay-to-Merkle-Root (P2MR)

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0360]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2024-12-18
**Autoren:** Hunter Beast, Ethan Heilman, Isabel Foxen Duke

## Summary

This document proposes a new output type: Pay-to-Merkle-Root (P2MR), via a soft fork. P2MR outputs operate with nearly the same functionality as P2TR (Pay-to-Taproot) outputs, but with the key path spend removed. Through this modification, P2MR outputs allow developers to use script trees and tapscript in a manner that is: # resistant to long exposure attacks by Cryptographically Relevant Quantum Computers (CRQCs), and # resistant to future cryptanalytic approaches that may compromise the elliptic curve cryptography (ECC) used by Bitcoin. It is worth noting that proposed P2MR outputs are onl

## Body

### Zweck

BIP-0360 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2024-12-18 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
