# BIP-0327: MuSig2 for BIP340-compatible Multi-Signatures

**Status:** established
**Last updated:** 2026-06-08
**Sources:** [[bip-0327]]

Typ: Informational · Status: Deployed · Datum: 2022-03-22
**Autoren:** Jonas Nick <jonasd.nick@gmail.com>, Tim Ruffing <crypto@timruffing.de>, Elliott Jin <elliott.jin@...

## Summary

This document proposes a standard for the MuSig2 multi-signature scheme. The standard is compatible with BIP340 public keys and signatures. It supports tweaking, which allows deriving BIP32 child keys from aggregate public keys and creating BIP341 Taproot outputs with key and script paths.

## Body

### Zweck

BIP-0327 ist ein Informational-BIP. Es wurde am 2022-03-22 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
