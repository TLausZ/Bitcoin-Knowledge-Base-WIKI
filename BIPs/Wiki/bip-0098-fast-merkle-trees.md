# BIP-0098: Fast Merkle Trees

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0098]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2017-08-24
**Autoren:** Mark Friedenbach, Kalle Alm, BtcDrak

## Summary

In many applications it is useful to prove membership of a data element in a set without revealing the entire contents of that set. The Merkle hash-tree is a cryptographic tool that achieves this goal. Bitcoin uses a Merkle hash-tree construct for committing the transactions of a block into the block header. This particular design, created by Satoshi, suffers from a serious flaw related to duplicate entries (CVE-2012-2459), and also suffers from less than optimal performance due to unnecessary double-hashing. This BIP describes a more efficient Merkle hash-tree construct that is not vulnerable

## Body

### Zweck

BIP-0098 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-08-24 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0098.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0098.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
