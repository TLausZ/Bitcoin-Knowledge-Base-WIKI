# BIP-0300: Hashrate Escrows (Consensus layer)

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0300]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2017-08-14
**Autoren:** Paul Sztorc <truthcoin@gmail.com>, CryptAxe <cryptaxe@gmail.com>

## Summary

BIP-300 enables a new type of L2, where "withdrawals" (the L2-to-L1 txns) are governed by proof-of-work -- instead of a federation or fixed set of pubkeys. BIP-300 emphasizes slow, transparent, and auditable withdrawals that are easy for honest users to get right and hard for dishonest miners to abuse. The main design goal for BIP-300 is partitioning -- users can ignore BIP-300 txns if they wish; it makes no difference to L1 if the user validates all, some, or none of them. The second design goal is security -- users of the L2 should feel confident that, if the L2 network is paying a lot of fe

## Body

### Zweck

BIP-0300 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-08-14 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0300.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0300.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
