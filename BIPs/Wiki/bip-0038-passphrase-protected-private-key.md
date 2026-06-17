# BIP-0038: Passphrase-protected private key

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0038]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2012-11-20
**Autoren:** Mike Caldwell, Aaron Voisine

## Summary

A method is proposed for encrypting and encoding a passphrase-protected Bitcoin private key record in the form of a 58-character Base58Check-encoded printable string. Encrypted private key records are intended for use on paper wallets and physical Bitcoins. Each record string contains all the information needed to reconstitute the private key except for a passphrase, and the methodology uses salting and scrypt to resist brute-force attacks. The method provides two encoding methodologies - one permitting any known private key to be encrypted with any passphrase, and another permitting a shared

## Body

### Zweck

BIP-0038 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2012-11-20 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
