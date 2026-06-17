# BIP-0009: Version bits with timeout and delay

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0009]]

Layer: Consensus (soft fork) · Typ: Informational · Status: Deployed · Datum: 2015-10-04
**Autoren:** Pieter Wuille, Peter Todd, Greg Maxwell, Rusty Russell

## Summary

This document specifies a proposed change to the semantics of the 'version' field in Bitcoin blocks, allowing multiple backward-compatible changes (further called "soft forks") to be deployed in parallel. It relies on interpreting the version field as a bit vector, where each bit can be used to track an independent change. These are tallied each retarget period. Once the consensus change succeeds or times out, there is a "fallow" pause after which the bit can be reused for later changes.

## Body

### Zweck

BIP-0009 ist ein Informational-BIP für die Schicht Consensus (soft fork). Es wurde am 2015-10-04 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
