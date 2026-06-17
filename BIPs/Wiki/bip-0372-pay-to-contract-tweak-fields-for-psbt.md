# BIP-0372: Pay-to-contract tweak fields for PSBT

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0372]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2022-01-16
**Autoren:** Maxim Orlovsky

## Summary

This document proposes additional fields for BIP 174 PSBTv0 and BIP 370 PSBTv2 that allow for pay-to-contract (P2C) key tweaking data to be included in a PSBT of any version. These will represent extra-transaction information required for the signer to produce valid signatures spending previous outputs.

## Body

### Zweck

BIP-0372 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2022-01-16 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0372.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0372.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
