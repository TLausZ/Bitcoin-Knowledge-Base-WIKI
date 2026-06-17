# BIP-0116: MERKLEBRANCHVERIFY

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0116]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2017-08-25
**Autoren:** Mark Friedenbach, Kalle Alm, BtcDrak

## Summary

A general approach to bitcoin contracts is to fully enumerate possible spending conditions in a single script. This exposes all program pathways including unused ones, wastes block space, restricts script size due to push limits, and impacts privacy and fungibility. This BIP proposes MERKLEBRANCHVERIFY, a new soft-fork upgradeable opcode which allows script writers to commit to a set of data elements and have one or more of these elements provided at redemption without revealing the entire set. As these elements can encode policy (public keys or validation subscripts), MERKLEBRANCHVERIFY can o

## Body

### Zweck

BIP-0116 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-08-25 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0116.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0116.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
