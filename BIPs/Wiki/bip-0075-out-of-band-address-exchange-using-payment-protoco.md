# BIP-0075: Out of Band Address Exchange using Payment Protocol Encryption

**Status:** established
**Last updated:** 2026-06-07
**Sources:** [[bip-0075]]

Layer: Applications · Typ: Specification · Status: Deployed · Datum: 2015-11-20
**Autoren:** Justin Newton, Matt David, Aaron Voisine, James MacWhyte

## Summary

This BIP is an extension to BIP 70 that provides two enhancements to the existing Payment Protocol. # It allows the requester (Sender) of a PaymentRequest to voluntarily sign the original request and provide a certificate to allow the payee to know the identity of who they are transacting with. # It encrypts the PaymentRequest that is returned, before handing it off to the SSL/TLS layer to prevent man in the middle viewing of the Payment Request details.

## Body

### Zweck

BIP-0075 ist ein Specification-BIP für die Schicht Applications. Es wurde am 2015-11-20 eingereicht und hat den Status **Deployed**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0075.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0075.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
