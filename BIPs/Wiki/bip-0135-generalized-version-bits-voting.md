# BIP-0135: Generalized version bits voting

**Status:** speculative
**Last updated:** 2026-06-07
**Sources:** [[bip-0135]]

Typ: Informational · Status: Closed · Datum: 2017-03-29
**Autoren:** Sancho Panza

## Summary

BIP9 introduced a mechanism for using the version bits to signal support for backwards-compatible changes (soft-forks) using a tally over the previous 2016 blocks computed at re-targeting intervals. It provided for a fixed threshold and non-configurable lock-in interval applicable to all deployments on a chain. This document describes a generalized signaling scheme which allows each signaling bit to have its own configurable threshold, window size (number of blocks over which it is tallied) and a configurable lock-in period. It extends the semantics of the signaling bits to cover arbitrary con

## Body

### Zweck

BIP-0135 ist ein Informational-BIP. Es wurde am 2017-03-29 eingereicht und hat den Status **Closed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0135.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0135.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
