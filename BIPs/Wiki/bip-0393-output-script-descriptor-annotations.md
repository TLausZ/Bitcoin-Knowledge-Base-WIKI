# BIP-0393: Output Script Descriptor Annotations

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0393]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2026-03-17
**Autoren:** Craig Raw <craig@sparrowwallet.com>

## Summary

This document specifies an optional annotation syntax for output script descriptors as defined in BIP 380. Annotations are key/value pairs appended to a descriptor expression using URL-like query string delimiters (?, &, =). They convey operational metadata (such as a blockchain scan start height or gap limit) to aid recovery of funds without altering the scripts produced by the descriptor.

## Body

### Zweck

BIP-0393 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2026-03-17 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0393.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0393.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
