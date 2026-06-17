# BIP-0387: Tapscript Multisig Output Script Descriptors

**Status:** established
**Last updated:** 2026-06-08
**Sources:** [[bip-0387]]

Layer: Applications · Typ: Informational · Status: Deployed · Datum: 2024-04-17
**Autoren:** Pieter Wuille <pieter@wuille.net>, Ava Chow <me@achow101.com>

## Summary

This document specifies multi_a() and sortedmulti_a() output script descriptors. Like BIP 383's multi() and sortedmulti(), both functions take a threshold and one or more public keys and produce a multisig script. The primary distinction is that multi_a() and sortedmulti_a() only produce tapscripts and are only allowed in a tapscript context.

## Body

### Zweck

BIP-0387 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2024-04-17 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
