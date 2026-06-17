# BIP-0125: Opt-in Full Replace-by-Fee Signaling

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0125]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2015-12-04
**Autoren:** David A. Harding, Peter Todd

## Summary

Many nodes will not replace any transaction in their mempool with another transaction spending the same inputs, making it difficult for spenders to adjust previously-sent transactions. Opt-in full Replace-by-Fee (RBF) signaling allows spenders to signal that they want to be able to replace a transaction in the future. In response to this signal: * Nodes may allow transactions with this signal to be replaced in their mempools. * Recipients may choose not to treat signaling transactions as payment until confirmed, eliminating fraud risk. Transactions without the signal continue to be treated as

## Body

### Zweck

BIP-0125 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2015-12-04 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
