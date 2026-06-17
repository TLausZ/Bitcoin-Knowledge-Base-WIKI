# BIP-0013: Address Format for pay-to-script-hash

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0013]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2011-10-18
**Autoren:** Gavin Andresen

## Summary

This BIP describes a new type of Bitcoin address to support arbitrarily complex transactions. Complexity in this context is defined as what information is needed by the recipient to respend the received coins, in contrast to needing a single ECDSA private key as in current implementations of Bitcoin. In essence, an address encoded under this proposal represents the encoded hash of a script, rather than the encoded hash of an ECDSA public key.

## Body

### Zweck

BIP-0013 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2011-10-18 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
