# Sparrow Wallet

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20210714_einblick-bitcoin-internals-sparrow-wallet-bitbox02-de]]

## Summary

Sparrow Wallet ist eine Bitcoin-Desktop-Wallet für fortgeschrittene Nutzer mit vollem Einblick in Bitcoin-Internals: UTXO-Darstellung, Coin Selection, Pay-to-many, Multisig-Unterstützung und flexible Server-Wahl. In Kombination mit der BitBox02 bietet Sparrow eine der transparentesten Transaktionsoberflächen — Craig Raw, der Entwickler, nennt das Prinzip "cold-storage sweating": Man soll beim Senden von Bitcoin leicht schwitzen — aus gutem Grund.

## Body

### Was Sparrow ist

Sparrow Wallet ist eine quelloffene Bitcoin-only Wallet für Windows, Mac und Linux. Der Fokus liegt auf Transparenz: Sparrow zeigt alle technischen Details einer Wallet und jeder Transaktion, anstatt sie vor dem Nutzer zu verstecken. Das ist gewollt — wer verstehen will, was Bitcoin tatsächlich tut, findet hier alle Informationen.

### Server-Wahl

Sparrow bietet vier Server-Optionen:

- **Public Server:** Einfachste Option, aber Datenschutzprobleme (der Server kennt alle Adressen)
- **Bitcoin Core:** Eigener Node mit integriertem Electrum-Index — beste Kombination aus Dezentralisierung und Privatsphäre
- **Private Electrum Server:** Eigener Electrum Server (z.B. Electrum Personal Server oder Fulcrum), flexibler als Bitcoin Core
- **BitBox-Server:** Shift Cryptos eigener Electrum-Server als Kompromiss zwischen Einfachheit und Datenschutz

Wie bei [[electrum-wallet]] gilt: Der Server, mit dem man sich verbindet, kennt alle Adressen und Transaktionen. Eigener Node = maximale Selbstständigkeit.

### UTXO-Ansicht und Coin Selection

Sparrow zeigt alle UTXOs der Wallet direkt an — nicht nur den Gesamtsaldo. Das gibt vollständige Kontrolle darüber, welche Coins in einer Transaktion verwendet werden (Coin Control).

**Coin Selection:** Sparrow bietet mehrere Algorithmen zum Auswählen von UTXOs (z.B. Branch and Bound für minimale Gebühren oder manuelle Auswahl). Wer UTXOs aus verschiedenen Quellen (z.B. Börse und privater Kauf) nicht vermischen will, kann gezielt nur bestimmte auswählen.

### Pay-to-many

Sparrow unterstützt die Ausgabe an mehrere Empfänger in einer einzigen Transaktion. Nützlich für Batch-Auszahlungen und spart Gebühren und Blockplatz gegenüber mehreren Einzeltransaktionen.

### Multisig-Wallets

Sparrow ist eine der bevorzugten Desktops für Bitcoin-Multisig-Setups. Für eine 2-von-3-Multisig-Wallet werden die Extended Public Keys (xpubs) aller beteiligten Hardware-Wallets eingerichtet. Die BitBox02 zeigt xpubs im Electrum-Format direkt auf ihrem Display an — was wichtig ist, damit der Nutzer die Schlüssel verifizieren kann, ohne dem Computer blind zu vertrauen.

Für eine Anleitung zur Erstellung einer Multisig-Wallet mit Sparrow und der BitBox02 existiert eine eigene Schritt-für-Schritt-Dokumentation auf dem BitBox-Blog.

### "Cold-Storage Sweating"

Craig Raw (Sparrow-Entwickler) beschreibt das Ziel seiner Wallet als "cold-storage sweating": Das leichte Unbehagen beim Senden einer Bitcoin-Transaktion gilt Raw als Feature. Sparrow zeigt so viele Details, dass man bei jeder Transaktion kurz innehält und prüft, ob wirklich alles stimmt.

Das steht im Kontrast zu Wallets, die den Prozess so einfach wie möglich machen und dabei Transparenz opfern. Für kleinere Beträge ist das ok; für significante Mengen Bitcoin ist Sparrows Ansatz passender.

## Related

- [[electrum-wallet]]
- [[multisig-und-kollaborative-verwahrung]]
- [[utxo-modell-und-konsolidierung]]
- [[coinjoin-und-on-chain-privatsphäre]]
- [[hd-wallets-und-schluesselableitung]]

## Open Questions

- Wie verhält sich Sparrow zu neuen Standards wie Silent Payments oder Payjoin?
