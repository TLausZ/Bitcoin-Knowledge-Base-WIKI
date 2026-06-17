# BIP-0451: Dust UTXO Disposal Protocol

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0451]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2026-04-28
**Autoren:** bubb1es <bubb1es71@proton.me>, haris <harismuzaffer@gmail.com>

## Summary

This BIP specifies a standardized protocol for safely disposing of dust UTXOs by spending them to an OP_RETURN output with the entire value going to transaction fees. The protocol describes how wallet software should remove unwanted small-value UTXOs received in dust attacks without degrading user privacy. The specification includes transaction format requirements, signature conventions enabling third-party batching, and validation rules for compliant implementations.

## Body

### Zweck

BIP-0451 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2026-04-28 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0451.md](https://github.com/bitcoin/bips/blob/master/bip-0451.md)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
