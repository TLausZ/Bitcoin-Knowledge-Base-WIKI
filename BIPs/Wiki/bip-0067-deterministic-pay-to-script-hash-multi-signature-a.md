# BIP-0067: Deterministic Pay-to-script-hash multi-signature addresses through public key sorting

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0067]]

Layer: Applications · Typ: Specification · Status: Complete · Datum: 2015-02-08
**Autoren:** Thomas Kerin, Jean-Pierre Rupp, Ruben de Vries

## Summary

This BIP describes a method to deterministically generate multi-signature pay-to-script-hash transaction scripts. It focuses on defining how the public keys must be encoded and sorted so that the redeem script and corresponding P2SH address are always the same for a given set of keys and number of required signatures.

## Body

### Zweck

BIP-0067 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2015-02-08 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
