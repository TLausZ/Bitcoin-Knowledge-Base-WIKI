# BIP-0347: OP_CAT in Tapscript

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0347]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Complete · Datum: 2023-12-11
**Autoren:** Ethan Heilman, Armin Sabouri

## Summary

This BIP introduces OP_CAT as a tapscript opcode which allows the concatenation of two values on the stack. OP_CAT would be activated via a soft fork by redefining the opcode OP_SUCCESS126 (126 in decimal and 0x7e in hexadecimal). This is the same opcode value used by the original OP_CAT.

## Body

### Zweck

BIP-0347 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2023-12-11 eingereicht und hat den Status **Complete**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0347.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0347.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
