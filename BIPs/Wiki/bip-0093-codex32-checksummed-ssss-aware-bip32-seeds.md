# BIP-0093: codex32: Checksummed SSSS-aware BIP32 seeds

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0093]]

Layer: Applications · Typ: Informational · Status: Draft · Datum: 2023-02-13
**Autoren:** Leon Olsson Curr, Pearlwort Sneed, Andrew Poelstra

## Summary

This document proposes a checksummed base32 format, "codex32", and a standard for backing up and restoring the master seed of a BIP-0032 hierarchical deterministic wallet using it. It includes an encoding format, a BCH error-correcting checksum, and optional Shamir's secret sharing algorithms for share generation and secret recovery. Secret data can be encoded directly, or split into up to 31 shares. A minimum threshold of shares, which can be between 2 and 9, is needed to recover the secret, whereas without sufficient shares, no information about the secret is recoverable.

## Body

### Zweck

BIP-0093 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2023-02-13 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0093.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0093.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
