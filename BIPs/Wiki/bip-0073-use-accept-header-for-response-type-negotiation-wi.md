# BIP-0073: Use \"Accept\" header for response type negotiation with Payment Request URLs

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0073]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2013-08-27
**Autoren:** Stephen Pair

## Summary

This BIP describes an enhancement to the payment protocol (BIP 70) that addresses the need for short URLs when scanning from QR codes. It generalizes the specification for the behavior of a payment request URL in a way that allows the client and server to negotiate the content of the response using the HTTP Accept: header field. Specifically, the client can indicate to the server whether it prefers to receive a bitcoin URI or a payment request. Implementation of this BIP does not require full payment request (BIP 70) support.

## Body

### Zweck

BIP-0073 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2013-08-27 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0073.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0073.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
