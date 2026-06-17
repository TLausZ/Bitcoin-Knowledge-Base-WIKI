# BIP-0373: MuSig2 PSBT Fields

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0373]]

Layer: Applications · Typ: Specification · Status: Complete · Datum: 2024-06-04
**Autoren:** Ava Chow

## Summary

This document proposes additional fields for BIP 174 PSBTv0 and BIP 370 PSBTv2 that allow for BIP 327 MuSig2 Multi-Signature data to be included in a PSBT of any version. These will be fields for the participants' keys, the public nonces, and the partial signatures produced with MuSig2.

## Body

### Zweck

BIP-0373 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2024-06-04 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
