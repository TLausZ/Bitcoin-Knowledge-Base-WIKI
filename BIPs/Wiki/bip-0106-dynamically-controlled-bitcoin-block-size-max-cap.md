# BIP-0106: Dynamically Controlled Bitcoin Block Size Max Cap

**Status:** speculative
**Last updated:** 2026-06-07
**Sources:** [[bip-0106]]

Layer: Consensus (hard fork) · Typ: Specification · Status: Closed · Datum: 2015-08-24
**Autoren:** Upal Chakraborty

## Summary

This BIP proposes replacing the fixed one megabyte maximum block size with a dynamically controlled maximum block size that may increase or decrease with difficulty change depending on various network factors. I have two proposals regarding this: i. Depending only on previous block size calculation. ii. Depending on previous block size calculation and previous Tx fee collected by miners.

## Body

### Zweck

BIP-0106 ist ein Specification-BIP für die Schicht Consensus (hard fork). Es wurde am 2015-08-24 eingereicht und hat den Status **Closed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0106.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0106.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
