# BIP-0113: Median time-past as endpoint for lock-time calculations

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0113]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Deployed · Datum: 2015-08-10
**Autoren:** Thomas Kerin, Mark Friedenbach

## Summary

This BIP is a proposal to redefine the semantics used in determining a time-locked transaction's eligibility for inclusion in a block. The median of the last 11 blocks is used instead of the block's timestamp, ensuring that it increases monotonically with each block.

## Body

### Zweck

BIP-0113 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2015-08-10 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
