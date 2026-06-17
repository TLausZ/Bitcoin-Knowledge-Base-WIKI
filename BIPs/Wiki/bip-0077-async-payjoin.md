# BIP-0077: Async Payjoin

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0077]]

Layer: Applications · Typ: Specification · Status: Draft · Datum: 2023-08-08
**Autoren:** Dan Gould <d@ngould.dev>, Yuval Kogman <nothingmuch@woobling.org>

## Summary

Payjoin lets Bitcoin senders and receivers interact to make batched transactions. This document proposes a second, backwards-compatible, asynchronous version of the Payjoin protocol ("Version 2") relative to and described in [BIP 78](bip-0078.mediawiki) ("Version 1"). An untrusted third-party "directory server" replaces the requirement for a receiver to host a secure public endpoint for interactions. HTTP clients access the directory server using an asynchronous protocol and authenticated, encrypted payloads. The design preserves complete Payjoin receiver functionality, including payment outpu

## Body

### Zweck

BIP-0077 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2023-08-08 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0077.md](https://github.com/bitcoin/bips/blob/master/bip-0077.md)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
