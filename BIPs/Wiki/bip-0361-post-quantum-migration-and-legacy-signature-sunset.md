# BIP-0361: Post Quantum Migration and Legacy Signature Sunset

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0361]]

Layer: Consensus (soft fork) · Typ: Informational · Status: Draft · Datum: 2026-02-11
**Autoren:** Jameson Lopp, Christian Papathanasiou, Ian Smith, Joe Ross, Steve Vaile, Pierre-Luc Dallaire-Demers

## Summary

This proposal follows the implementation of any post-quantum (PQ) output type and introduces a pre-announced sunset of legacy ECDSA/Schnorr signatures. It turns quantum security into a private incentive: fail to upgrade and you will encounter additional friction to access your funds, creating a certainty where none previously existed. Phase A: Disallows sending of any funds to quantum-vulnerable addresses, hastening the adoption of PQ address types. Phase B: Renders ECDSA/Schnorr spends invalid, preventing all spending of funds in quantum-vulnerable UTXOs. This is triggered by a well-publici

## Body

### Zweck

BIP-0361 ist ein Informational-BIP für die Schicht Consensus (soft fork). Es wurde am 2026-02-11 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0361.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0361.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
