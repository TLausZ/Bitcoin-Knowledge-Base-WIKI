# BIP-0441: Restoration of disabled script (Tapleaf 0xC2)

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0441]]

Layer: Consensus (soft fork) · Typ: Specification · Status: Draft · Datum: 2026-03-25
**Autoren:** Rusty Russell <rusty@rustcorp.com.au>, Julian Moik <julianmoik@gmail.com>

## Summary

This BIP introduces a new tapleaf version (0xc2) which restores Bitcoin script to its pre-0.3.1 capability, relying on the Varops Budget in BIP440 to prevent the excessive computational time which caused CVE-2010-5137. In particular, this BIP: * Reenables disabled opcodes. * Increases the maximum stack object size from 520 bytes to 4,000,000 bytes. * Introduces a total stack byte limit of 8,000,000 bytes. * Increases the maximum total number of stack objects from 1,000 to 32,768. * Removes the 32-bit size restriction on numerical values. * Treats all numerical values as unsigned. All opcodes

## Body

### Zweck

BIP-0441 ist ein Specification-BIP für die Schicht Consensus (soft fork). Es wurde am 2026-03-25 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0441.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0441.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
