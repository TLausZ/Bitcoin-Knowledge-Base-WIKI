# BIP-0147: Dealing with dummy stack element malleability

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0147]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Deployed · Datum: 2016-09-02
**Autoren:** Johnson Lau

## Summary

This document specifies proposed changes to the Bitcoin transaction validity rules to fix a malleability vector in the extra stack element consumed by OP_CHECKMULTISIG and OP_CHECKMULTISIGVERIFY.

## Body

### Zweck

BIP-0147 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2016-09-02 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
