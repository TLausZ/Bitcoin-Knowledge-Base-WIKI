# BIP-0155: addrv2 message

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0155]]

Layer: Peer Services · Typ: Specification · Status: Deployed · Datum: 2019-02-27
**Autoren:** Wladimir J. van der Laan

## Summary

This document proposes a new P2P message to gossip longer node addresses over the P2P network. This is required to support Tor v3 hidden services, I2P, and potentially other networks that have longer endpoint addresses than fit in the 128 bits of the current addr message.

## Body

### Zweck

BIP-0155 ist ein Specification-BIP für die Schicht Peer Services. Es wurde am 2019-02-27 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
