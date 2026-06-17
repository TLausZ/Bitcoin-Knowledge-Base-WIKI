# BIP-0053: Disallow 64-byte transactions

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0053]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2025-04-11
**Autoren:** Chris Stewart <stewart.chris1234@gmail.com>

## Summary

This BIP describes the rationale for disallowing transactions that are serialized to 64 bytes without the transaction's witness. We describe the weaknesses to the Merkle tree included in Bitcoin block headers, and various exploits for those weaknesses.

## Body

### Zweck

BIP-0053 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2025-04-11 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0053.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0053.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
