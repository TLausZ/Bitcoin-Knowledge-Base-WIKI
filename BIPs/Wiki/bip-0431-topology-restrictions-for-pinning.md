# BIP-0431: Topology Restrictions for Pinning

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[bip-0431]]

Layer: Applications · Typ: Informational · Status: Draft · Datum: 2024-01-10
**Autoren:** Gloria Zhao <gloriajzhao@gmail.com>

## Summary

This document describes pinning problems that can arise from limitations in mempool policy. It also describes a type of policy with adjusted topology limits which, combined with other policy rules, helps minimize the potential pinning problems. These restrictions simplify the assessment of incentive compatibility of accepting or replacing such transactions, thus helping ensure any replacements are more profitable for the node. Within the context of nodes that implement this policy, fee-bumping is more reliable for users.

## Body

### Zweck

BIP-0431 ist ein Informational-BIP für die Schicht Applications. Es wurde am 2024-01-10 eingereicht und hat den Status **Draft**.

Vollständige Spezifikation: [https://github.com/bitcoin/bips/blob/master/bip-0431.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0431.mediawiki)

## Open Questions

- Wie verhält sich dieser BIP zu den nachfolgenden oder verwandten Vorschlägen?
