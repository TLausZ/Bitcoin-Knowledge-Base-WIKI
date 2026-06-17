# BIP-0388: Wallet Policies for Descriptor Wallets

**Status:** established
**Last updated:** 2026-06-08
**Sources:** [[bip-0388]]

Layer: Applications · Typ: Specification · Status: Complete · Datum: 2023-12-26
**Autoren:** Salvatore Ingala <salvatoshi@protonmail.com>

## Summary

Software wallets and hardware signing devices typically partition funds into separate "accounts". When signing or visualizing a transaction, aggregate flows of funds of all accounts affected by the transaction may (and should) be displayed to the user. Wallet policies build on top of output script descriptors to represent such accounts in a compact, reviewable way. An account encompasses a logical group of receive and change addresses, and each wallet policy represents all descriptors necessary to describe an account in its entirety. We simplify the language to suit devices with limited memory

## Body

### Zweck

BIP-0388 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2023-12-26 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
