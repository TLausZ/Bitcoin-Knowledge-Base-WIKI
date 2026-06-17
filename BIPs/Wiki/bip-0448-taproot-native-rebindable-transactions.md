# BIP-0448: Taproot-native (Re)bindable Transactions

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0448]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2026-03-11
**Autoren:** Gregory Sanders <gsanders87@gmail.com>, Antoine Poinsot <mail@antoinep.com>, Steven Roose <steven...

## Summary

This document proposes deploying three new operations for [Tapscript][tapscript-bip]: [BIP 446 `OP_TEMPLATEHASH`][templatehash-bip], [BIP 348 `OP_CHECKSIGFROMSTACK`][csfs-bip], and [BIP 349 `OP_INTERNALKEY`][internalkey-bip]. These minimal operations introduce modular functionalities which improve existing second layer protocols and make new ones possible through plausible interactivity requirements.

## Body

### Zweck

BIP-0448 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2026-03-11 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0448.md](https://github.com/bitcoin/bips/blob/master/bip-0448.md)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
