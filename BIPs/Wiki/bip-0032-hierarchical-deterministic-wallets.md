# BIP-0032: Hierarchical Deterministic Wallets

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0032]]

Layer: Applications · Typ: Informational · Status: Deployed · Datum: 2012-02-11
**Autoren:** Pieter Wuille

## Summary

This document describes hierarchical deterministic wallets (or "HD Wallets"): wallets which can be shared partially or entirely with different systems, each with or without the ability to spend coins. The specification is intended to set a standard for deterministic wallets that can be interchanged between different clients. Although the wallets described here have many features, not all are required by supporting clients. The specification consists of two parts. In the first part, a system for deriving a tree of keypairs from a single seed is presented. The second part demonstrates how to bui

## Body

### Zweck

BIP-0032 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2012-02-11 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)

## Related

- [[bip-0039]]
- [[bip-0043]]
- [[bip-0044]]

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
