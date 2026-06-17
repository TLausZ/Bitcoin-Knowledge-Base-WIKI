# BIP-0157: Client Side Block Filtering

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0157]]

Layer: Peer Services · Typ: Specification · Status: Deployed · Datum: 2017-05-24
**Autoren:** Olaoluwa Osuntokun, Alex Akselrod, Jim Posen

## Summary

This BIP describes a new light client protocol that improves upon BIP 37. Instead of clients sending Bloom filters to full nodes, full nodes generate deterministic compact filters of block content (defined in BIP 158) that are served to clients. A light client can then download an entire block if the filter matches relevant data.

## Body

### Zweck

BIP-0157 ist ein Specification-BIP für die Schicht Peer Services. Es wurde am 2017-05-24 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
