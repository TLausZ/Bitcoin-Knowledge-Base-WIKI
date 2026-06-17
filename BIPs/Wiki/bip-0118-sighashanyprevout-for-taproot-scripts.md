# BIP-0118: SIGHASH_ANYPREVOUT for Taproot Scripts

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0118]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2017-02-28
**Autoren:** Christian Decker, Anthony Towns

## Summary

This BIP describes a new type of public key for tapscript (BIP 342) transactions. It allows signatures for these public keys to not commit to the exact UTXO being spent. This enables dynamic binding of transactions to different UTXOs, provided they have compatible scripts.

## Body

### Zweck

BIP-0118 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-02-28 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0118.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0118.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
