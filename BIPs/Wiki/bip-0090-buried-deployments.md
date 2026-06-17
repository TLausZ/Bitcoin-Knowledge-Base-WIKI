# BIP-0090: Buried Deployments

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0090]]

Typ: Informational · Status: Deployed · Datum: 2016-11-08
**Autoren:** Suhas Daftuar

## Summary

Prior soft forks (BIP 34, BIP 65, and BIP 66) were activated via miner signaling in block version numbers. Now that the chain has long since passed the blocks at which those consensus rules have triggered, we can (as a simplification) replace the trigger mechanism by caching the block heights at which those consensus rules became enforced.

## Body

### Zweck

BIP-0090 ist ein Informational-BIP. Es wurde am 2016-11-08 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0090.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0090.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
