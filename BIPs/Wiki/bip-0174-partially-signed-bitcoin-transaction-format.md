# BIP-0174: Partially Signed Bitcoin Transaction Format

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0174]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2017-07-12
**Autoren:** Ava Chow

## Summary

This document proposes a binary transaction format (PSBT) which contains the information necessary for a signer to produce signatures for a transaction, and holds signatures while the transaction does not yet have a complete set. Signers can be offline, as all necessary information is provided in the transaction.

## Body

### Zweck

BIP-0174 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2017-07-12 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

## Related

- [[bip-0370]]
- [[bip-0371]]

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
