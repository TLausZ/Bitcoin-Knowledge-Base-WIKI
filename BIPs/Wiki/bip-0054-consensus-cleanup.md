# BIP-0054: Consensus Cleanup

**Status:** established
**Last updated:** 2026-06-08
**Sources:** [[bip-0054]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Complete · Datum: 2025-04-11
**Autoren:** Antoine Poinsot <mail@antoinep.com>, Matt Corallo <bips@bluematt.me>

## Summary

This document proposes new consensus rules in order to fix the timewarp attack, reduce the worst case block validation time, prevent Merkle tree weaknesses, and avoid duplicate transactions without [bip-0030][BIP30] validation.

## Body

### Zweck

BIP-0054 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2025-04-11 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0054.md](https://github.com/bitcoin/bips/blob/master/bip-0054.md)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
