# BIP-0136: Bech32 Encoded Tx Position References

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0136]]

Layer: Applications · Typ: Informational · Status: Draft · Datum: 2017-07-09
**Autoren:** Велеслав, Jonas Schnelli, Daniel Pape

## Summary

This document proposes a convenient, human usable encoding to refer to a confirmed transaction position within the Bitcoin blockchain--known as "TxRef". The primary purpose of this encoding is to allow users to refer to a confirmed transaction (and optionally, a particular outpoint index within the transaction) in a standard, reliable, and concise way. Please note: Unlike a transaction ID, "TxID", where there is a strong cryptographic link between the ID and the actual transaction, a TxRef only provides a weak link to a particular transaction. A TxRef locates an offset within a blockchain fo

## Body

### Zweck

BIP-0136 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2017-07-09 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0136.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0136.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
