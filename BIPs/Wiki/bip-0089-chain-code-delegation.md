# BIP-0089: Chain Code Delegation

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0089]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2025-12-03
**Autoren:** Jesse Posner, Jurvis Tan

## Summary

Chain Code Delegation (CCD) is a method for multi-signature wallets in which a privileged participant withholds BIP32 chain codes from one or more non-privileged participants, and supplies per-input scalar tweaks at signing time. This allows non-privileged participants to co-sign transactions without learning wallet-wide derivations, balances, or signing activity from other spending combinations. CCD defines the tweak exchange needed for verification and signing behavior when the signer does not possess a chain code.

## Body

### Zweck

BIP-0089 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2025-12-03 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
