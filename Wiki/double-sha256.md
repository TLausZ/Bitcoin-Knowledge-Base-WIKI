# Double-SHA256 in Bitcoin

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-double-sha256]]

## Summary

Bitcoin hasht fast überall doppelt: SHA256(SHA256(x)). Satoshi begründete das damit, dass es gegen Length-Extension-Attacks schütze. Ob das stimmt, ist umstritten — SHA-256 ist gegen diesen Angriff anders anfällig als SHA-1, und 2024 besteht Konsens, dass Double-SHA256 keinen wesentlichen Sicherheitsvorteil bringt. Weil die Wahl konsensrelevant ist, bleibt sie dauerhaft im Protokoll.

## Body

### Wo Double-SHA256 vorkommt

Proof-of-Work (Block-Header-Hash), Merkle-Bäume, Transaktions-IDs, Script-Hashes bei P2SH — überall im ursprünglichen Bitcoin-Protokoll. Satoshi verwendete es als Standard, weil kurz vor Bitcoins Launch ein Length-Extension-Angriff gegen SHA-1 veröffentlicht worden war, und er entsprechend vorsichtig war.

### War es sinnvoll?

SHA-256 ist nicht anfällig für Length-Extension-Attacks in der gleichen Weise wie SHA-1. Moderne Analyse zeigt, dass Double-SHA256 keinen messbaren Sicherheitsvorteil gegenüber einfachem SHA-256 bietet. Neuere Protokollteile (Taproot, Schnorr-Signaturen) nutzen einfaches SHA-256 oder sogar Tagged Hashes ohne Dopplung.

Eine alternative Erklärung: Doppeltes Hashing erlaubt es, einen Besitz einer Datei zu beweisen, ohne die Datei selbst zu offenbaren — da der erste Hash als Commitment fungiert. Das hat Anwendungen bei SPV-Clients und verteiltem Mining, war aber vermutlich nicht Satoshis primäre Motivation.

### Warum es sich nicht ändert

Die Wahl ist konsensrelevant: Alle Nodes müssen denselben Block-Header-Hash berechnen. Eine Änderung zu Single-SHA256 würde alle bisherigen Block-Hashes ungültig machen — ein Hard Fork, der das gesamte Netzwerk spalten würde. Double-SHA256 wird also für immer Teil von Bitcoins Basis-Protokoll bleiben.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[merkle-baeume]]
- [[bitcoin-transaktionsstruktur]]
- [[taproot-musig2-frost]]
