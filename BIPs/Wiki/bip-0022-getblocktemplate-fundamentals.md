# BIP-0022: getblocktemplate - Fundamentals

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0022]]

Layer: API/RPC · Typ: Specification · Status: Deployed · Datum: 2012-02-28
**Autoren:** Luke Dashjr

## Summary

This BIP describes a new JSON-RPC method for "smart" Bitcoin miners and proxies. Instead of sending a simple block header for hashing, the entire block structure is sent, and left to the miner to (optionally) customize and assemble.

## Body

### Zweck

BIP-0022 ist ein Specification-BIP für die Schicht API/RPC. Es wurde am 2012-02-28 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
