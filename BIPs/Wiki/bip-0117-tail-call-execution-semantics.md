# BIP-0117: Tail Call Execution Semantics

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0117]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2017-08-25
**Autoren:** Mark Friedenbach, Kalle Alm, BtcDrak

## Summary

BIP16 (Pay to Script Hash) and BIP141 (Segregated Witness) allow a single script to be committed to by the construct. This BIP, in conjunction with BIP116 (MERKLEBRANCHVERIFY), allows a script to commit to a practically unbounded number of code pathways, and then reveal only the actual code pathway used at spend time. This achieves a form of generalized MAST enabling decomposition of complex branching scripts into non-branching flat execution pathways.

## Body

### Zweck

BIP-0117 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-08-25 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0117.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0117.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
