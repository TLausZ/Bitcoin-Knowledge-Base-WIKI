# BIP-0143: Transaction Signature Verification for Version 0 Witness Program

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0143]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Deployed · Datum: 2016-01-03
**Autoren:** Johnson Lau, Pieter Wuille

## Summary

This proposal defines a new transaction digest algorithm for signature verification in version 0 witness program, in order to minimize redundant data hashing in verification, and to cover the input value by the signature.

## Body

### Zweck

BIP-0143 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2016-01-03 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
