# BIP-0114: Merkelized Abstract Syntax Tree

**Status:** speculative
**Last updated:** 2026-06-07
**Sources:** [[bip-0114]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Closed · Datum: 2016-04-02
**Autoren:** Johnson Lau

## Summary

This BIP defines a new witness program type that uses a Merkle tree to encode mutually exclusive branches in a script. This enables complicated redemption conditions that are currently not possible, improves privacy by hiding unexecuted scripts, and allows inclusion of non-consensus enforced data with very low or no additional cost.

## Body

### Zweck

BIP-0114 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2016-04-02 eingereicht und hat den Status **Closed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0114.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0114.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
