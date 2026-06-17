# BIP-0008: Version bits with lock-in by height

**Status:** emerging
**Last updated:** 2026-06-07
**Sources:** [[bip-0008]]

Layer: Consensus (soft fork) · Typ: Informational · Status: Draft · Datum: 2017-02-01
**Autoren:** Shaolin Fry, Luke Dashjr

## Summary

This document specifies an alternative to BIP9 that corrects for a number of perceived mistakes. Block heights are used for start and timeout rather than POSIX timestamps. It additionally introduces an activation parameter that can guarantee activation of backward-compatible changes (further called "soft forks"). The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## Body

### Zweck

BIP-0008 ist ein Informational-BIP für die Schicht Consensus (soft fork). Es wurde am 2017-02-01 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0008.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0008.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
