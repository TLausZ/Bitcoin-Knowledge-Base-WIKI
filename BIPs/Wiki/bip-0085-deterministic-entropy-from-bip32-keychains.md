# BIP-0085: Deterministic Entropy From BIP32 Keychains

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0085]]

Layer: Applications · Typ: Informational · Status: Deployed · Datum: 2020-03-20
**Autoren:** Ethan Kosakovsky, Aneesh Karve

## Summary

"One Seed to rule them all, One Key to find them, One Path to bring them all, And in cryptography bind them." It is not possible to maintain one single (mnemonic) seed backup for all keychains used across various wallets because there are a variety of incompatible standards. Sharing of seeds across multiple wallets is not desirable for security reasons. Physical storage of multiple seeds is difficult depending on the security and redundancy required. As HD keychains are essentially derived from initial entropy, this proposal provides a way to derive entropy from the keychain which can be fed i

## Body

### Zweck

BIP-0085 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2020-03-20 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
