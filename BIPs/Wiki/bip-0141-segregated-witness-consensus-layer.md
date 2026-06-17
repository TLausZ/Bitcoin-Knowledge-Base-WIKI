# BIP-0141: Segregated Witness (Consensus layer)

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0141]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Deployed · Datum: 2015-12-21
**Autoren:** Eric Lombrozo, Johnson Lau, Pieter Wuille

## Summary

This BIP defines a new structure called a "witness" that is committed to blocks separately from the transaction merkle tree. This structure contains data required to check transaction validity but not required to determine transaction effects. In particular, scripts and signatures are moved into this new structure. The witness is committed in a tree that is nested into the block's existing merkle root via the coinbase transaction for the purpose of making this BIP soft fork compatible. A future hard fork can place this tree in its own branch.

## Body

### Zweck

BIP-0141 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2015-12-21 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)

## Related

- [[bip-0143]]
- [[bip-0144]]
- [[bip-0173]]

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
