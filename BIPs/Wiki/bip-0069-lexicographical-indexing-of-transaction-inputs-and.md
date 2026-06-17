# BIP-0069: Lexicographical Indexing of Transaction Inputs and Outputs

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0069]]

Layer: Applications · Typ: Informational · Status: Complete · Datum: 2015-06-12
**Autoren:** Kristov Atlas

## Summary

Currently there is no standard for bitcoin wallet clients when ordering transaction inputs and outputs. As a result, wallet clients often have a discernible blockchain fingerprint, and can leak private information about their users. By contrast, a standard for non-deterministic sorting could be difficult to audit. This document proposes deterministic lexicographical sorting, using hashes of previous transactions and output indices to sort transaction inputs, as well as values and scriptPubKeys to sort transaction outputs.

## Body

### Zweck

BIP-0069 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2015-06-12 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
