# BIP-0449: OP_TWEAKADD - x-only key tweak addition

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0449]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2026-03-05
**Autoren:** Jeremy Rubin <jeremy@char.network>

## Summary

This proposal defines a new tapscript opcode, `OP_TWEAKADD`, that takes an x-only public key and a 32-byte integer `t` on the stack and pushes the x-only public key corresponding to `P + t*G`, where `P` is the lifted point for the input x-coordinate and `G` is the secp256k1 generator. The operation mirrors the Taproot tweak used by BIP340 signers and enables simple, verifiable key modifications inside script without revealing private keys or relying on hash locks.

## Body

### Zweck

BIP-0449 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2026-03-05 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0449.md](https://github.com/bitcoin/bips/blob/master/bip-0449.md)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
