# BIP-0111: NODE_BLOOM service bit

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0111]]

Layer: Peer Services · Typ: Specification · Status: Deployed · Datum: 2015-08-20
**Autoren:** Matt Corallo, Peter Todd

## Summary

This BIP extends BIP 37, Connection Bloom filtering, by defining a service bit to allow peers to advertise that they support bloom filters explicitly. It also bumps the protocol version to allow peers to identify old nodes which allow bloom filtering of the connection despite lacking the new service bit.

## Body

### Zweck

BIP-0111 ist ein Specification-BIP für die Schicht Peer Services. Es wurde am 2015-08-20 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
