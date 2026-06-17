# BIP-0140: Normalized TXID

**Status:** speculative
**Last updated:** 2026-06-07
**Sources:** [[bip-0140]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Closed · Datum: 2015-10-14
**Autoren:** Christian Decker

## Summary

This BIP describes the use of normalized transaction IDs (NTXIDs) in order to eliminate transaction malleability, both in the third-party modification scenario as well as the participant modification scenario. The transaction ID is normalized by removing the signature scripts from transactions before computing its hash. The normalized transaction hashes are then used during the signature creation and signature verification of dependent transactions.

## Body

### Zweck

BIP-0140 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2015-10-14 eingereicht und hat den Status **Closed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0140.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0140.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
