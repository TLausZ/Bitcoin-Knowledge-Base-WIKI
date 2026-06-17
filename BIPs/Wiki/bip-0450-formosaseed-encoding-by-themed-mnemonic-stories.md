# BIP-0450: Formosa—Seed encoding by themed mnemonic stories

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0450]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2026-05-15
**Autoren:** Yuri S Villas Boas <yuri@t3infosecurity.com>, André Fidencio Gonçalves <andre7c4@gmail.com>

## Summary

This BIP describes Formosa, an expansion of BIP-0039 for the generation of deterministic wallets. Where BIP-0039 maps each 11 bits of entropy to one word drawn from a single 2048-word list, Formosa maps each 33 bits of entropy to a short themed sentence built from several smaller, syntactically-typed wordlists. The sentences carry grammatical structure and semantic coherence, substantially improving memorability while retaining all cryptographic properties of the original scheme. The proposal is fully forward- and backward-compatible with BIP-0039: BIP-0039 is itself a Formosa theme, and seed

## Body

### Zweck

BIP-0450 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2026-05-15 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0450.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0450.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
