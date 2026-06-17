# BIP-0443: OP_CHECKCONTRACTVERIFY

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0443]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2025-05-08
**Autoren:** Salvatore Ingala <salvatoshi@protonmail.com>

## Summary

This BIP proposes to add consensus support for a new tapscript opcode that enables a new type of output restrictions: OP_CHECKCONTRACTVERIFY (OP_CCV). This opcode enables users to create UTXOs that carry a dynamic commitment to a piece of data. The commitment can be validated during the execution of the script, allowing introspection to the committed data. Moreover, a script can constrain the internal public key and taptree of one or more outputs, and possibly the committed data. In conjunction with an opcode for vector commitmentsVector commitments are cryptographic primitives that allow to c

## Body

### Zweck

BIP-0443 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2025-05-08 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0443.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0443.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
