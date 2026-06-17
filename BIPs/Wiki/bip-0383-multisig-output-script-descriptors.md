# BIP-0383: Multisig Output Script Descriptors

**Status:** established
**Last updated:** 2026-06-08
**Sources:** [[bip-0383]]

Layer: Applications · Typ: Informational · Status: Deployed · Datum: 2021-06-27
**Autoren:** Pieter Wuille <pieter@wuille.net>, Ava Chow <me@achow101.com>

## Summary

This document specifies multi(), and sortedmulti() output script descriptors. Both functions take a threshold and one or more public keys and produce a multisig output script. multi() specifies the public keys in the output script in the order given in the descriptor while sortedmulti() sorts the public keys lexicographically when the output script is produced.

## Body

### Zweck

BIP-0383 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2021-06-27 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
