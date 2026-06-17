# BIP-0079: Bustapay :: a practical coinjoin protocol

**Status:** speculative
**Last updated:** 2026-06-07
**Sources:** [[bip-0079]]

Layer: Applications · Typ: Informational · Status: Closed · Datum: 2018-10-05
**Autoren:** Ryan Havar

## Summary

The way bitcoin transactions are normally created leaks more information than desirable, and as a result has been exploited by unreasonably effective blockchain analysis techniques to jeopardize important properties that are expected of a useful currency. Bustapay is a simple and practical protocol for the sender and receiver of a payment to collaboratively sign a bitcoin transaction in such a way that busts some analysis assumptions to the immediate benefit of the sender and receiver. It also gives a significant amount of control to the receiver to help manage their UTXO set size.

## Body

### Zweck

BIP-0079 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2018-10-05 eingereicht und hat den Status **Closed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
