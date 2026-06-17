# BIP-0037: Connection Bloom filtering

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0037]]

Layer: Peer Services · Typ: Specification · Status: Deployed · Datum: 2012-10-24
**Autoren:** Mike Hearn, Matt Corallo

## Summary

This BIP adds new support to the peer-to-peer protocol that allows peers to reduce the amount of transaction data they are sent. Peers have the option of setting filters on each connection they make after the version handshake has completed. A filter is defined as a Bloom filter on data derived from transactions. A Bloom filter is a probabilistic data structure which allows for testing set membership - they can have false positives but not false negatives.

## Body

### Zweck

BIP-0037 ist ein Specification-BIP für die Schicht Peer Services. Es wurde am 2012-10-24 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
