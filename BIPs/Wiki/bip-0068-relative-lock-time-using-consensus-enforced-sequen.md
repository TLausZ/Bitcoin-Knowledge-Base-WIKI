# BIP-0068: Relative lock-time using consensus-enforced sequence numbers

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0068]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Deployed · Datum: 2015-05-28
**Autoren:** Mark Friedenbach, BtcDrak, Nicolas Dorier, kinoshitajona

## Summary

This BIP introduces relative lock-time (RLT) consensus-enforced semantics of the sequence number field to enable a signed transaction input to remain invalid for a defined period of time after confirmation of its corresponding outpoint.

## Body

### Zweck

BIP-0068 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2015-05-28 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
