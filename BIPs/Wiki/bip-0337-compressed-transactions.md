# BIP-0337: Compressed Transactions

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0337]]

Layer: API/RPC · Typ: Specification · Status: Draft · Datum: 2024-02-01
**Autoren:** Tom Briar <tombriar11@protonmail.com>

## Summary

This document proposes a serialization scheme for compressing Bitcoin transactions. The compressed Bitcoin transactions can reach a serialized size of less than 50% of the original serialized transaction. One method for compressing involves reducing the transaction outpoints in a potentially lossy way. Therefore, it is an optional path for compression. Compressing the outpoints is necessary for compressed transactions to reach less than 70% of the original size.

## Body

### Zweck

BIP-0337 ist ein Specification-BIP für die Schicht API/RPC. Es wurde am 2024-02-01 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0337.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0337.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
