# BIP-0158: Compact Block Filters for Light Clients

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0158]]

Layer: Peer Services · Typ: Specification · Status: Deployed · Datum: 2017-05-24
**Autoren:** Olaoluwa Osuntokun, Alex Akselrod

## Summary

This BIP describes a structure for compact filters on block data, for use in the BIP 157 light client protocol. The filter construction uses Golomb-Rice coding for compression, minimizing filter size. One initial filter type ("basic") is defined for regular wallets.

## Body

### Zweck

BIP-0158 ist ein Specification-BIP für die Schicht Peer Services. Es wurde am 2017-05-24 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
