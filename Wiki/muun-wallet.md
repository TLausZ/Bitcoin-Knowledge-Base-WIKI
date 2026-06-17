# Muun Wallet

**Status:** established
**Last updated:** 2026-06-09
**Sources:** [[Self-Custody in Muun__Why Not just a Mnemonic_]], [[Muun Releases Non-Custodial Bitcoin and Lightning Wallet for iOS]], [[A Deep Dive into LND_ Overview and Channel Funding Process]], [[A Closer Look at Submarine Swaps in the Lightning Network]], [[How to Build a Bulletproof Lightning Node]], [[Designing a foolproof script upgrading mechanism]]

## Summary

Muun ist eine non-custodial Bitcoin+Lightning-Wallet für iOS und Android, die auf LND basiert und eine einheitliche Balance für On-Chain und Lightning präsentiert. Das Kernmerkmal ist das "Emergency Kit" — ein Backup-System mit Output Descriptors, das vollständige Selbstverwahrung ohne App-Abhängigkeit garantiert. Muun nutzt Submarine Swaps, um Lightning- und On-Chain-Zahlungen transparent zu verbinden, ohne dass der Nutzer Kanäle manuell verwalten muss.

## Body

### Architektur: Einheitliche Balance

Muun präsentiert dem Nutzer eine einzige Wallet-Balance für On-Chain und Lightning. Intern nutzt Muun LND (Lightning Labs, Go) und verbindet beide Zahlungsschichten via Submarine Swaps. Der Nutzer muss weder Channels öffnen, noch Liquidität verwalten, noch zwischen zwei Balancen wechseln — das Wallet übernimmt das automatisch.

### Warum Mnemonic allein nicht reicht

Die meisten Wallets sichern private Schlüssel als 12-Wort-Mnemonic. Das genügt für einfache P2PKH-Wallets. Muun nutzt aber Multisig-Scripts und Lightning — und hier versagt das klassische Mnemonic:

- **Multisig** erfordert nicht nur den privaten Schlüssel, sondern alle beteiligten Schlüssel und den vollständigen Script (als Output Descriptor). Ohne diese Infos kann der Mnemonic-Seed die UTXOs nicht finden, geschweige denn ausgeben.
- **Lightning** speichert Channel-Zustände lokal. Ein reiner Seed-Import stellt keine aktiven Channels wieder her.

Das Muun Emergency Kit löst das durch Output Descriptors (Standard für portable Wallet-Beschreibungen): Es enthält alle Schlüssel, Scripts und Wallet-Metadaten, die nötig sind, um Funds unabhängig von der Muun-App zurückzubekommen — mit einem Open-Source Recovery Tool auf GitHub.

### Submarine Swaps: HTLC-Brücke zwischen On-Chain und Lightning

Submarine Swaps verbinden On-Chain Bitcoin mit Lightning-Netzwerk-Zahlungen über HTLCs (Hashed Time-Locked Contracts):

1. Alice will On-Chain Bitcoin in einen Lightning-Kanal einzahlen, ohne einen neuen Channel zu öffnen.
2. Sie sendet On-Chain Bitcoin an einen Swap-Dienst, der eine Lightning-Zahlung vorab festlegt (mit Hash-Lock).
3. Der Swap-Dienst bezahlt die Lightning-Zahlung; Alice beweist den Empfang durch Reveal des Preimages.
4. Das Preimage entsperrt auch die On-Chain-Transaktion — beide Seiten sind trustless an das gleiche Geheimnis gebunden.

In Muun passiert das unsichtbar: Eingehende On-Chain-Zahlungen landen via Submarine Swap im Lightning-Kanal, ohne dass der Nutzer etwas konfiguriert.

### LND-Internals: Channel Funding

Muun basiert auf LND (Lightning Labs). Der Channel-Funding-Prozess:

1. **Open Channel**: Funding Transaction wird on-chain gebroadcastet und bestätigt.
2. **Commitment Transactions**: Beide Parteien halten jederzeit eine gültige, aber nicht gebroadcastete Transaktion, die den aktuellen Channel-Zustand repräsentiert.
3. **HTLC**: Jede Lightning-Zahlung ist ein temporärer Script auf der Commitment Transaction, der nach Reveal des Preimages oder Timeout auflöst.

### Node-Sicherheit: Linux-Härtung für LND

Muun betreibt LND als Hot-Wallet-Backend. Sicherheitsanforderungen:

- Automatische Security-Updates für Linux-Kernel und LND
- Secret Management: Private Schlüssel nicht im Klartext im Filesystem
- Monitoring: Unerwartetes Verhalten (Channel-Force-Closes, ungewöhnliche Outputs) früh erkennen
- Principle of Least Privilege: LND-Prozess läuft ohne Root-Rechte

### Taproot und Script-Upgrades

Muun hat früh auf Taproot (2021) hingewiesen, weil Taproot die letzten Barrieren für beliebige Scripts entfernt. Zuvor limitierte P2SH die Effizienz und Privatsphäre von Multisig-Wallets. Mit Taproot:

- Key-Path-Spend: Alle Schlüssel aggregieren zu einem einzelnen Schnorr-Schlüssel — sieht aus wie eine normale Zahlung
- Script-Path-Spend: Komplexe Recovery-Pfade bleiben versteckt bis zur Nutzung
- Output Descriptors + MiniScript erlauben portable, prüfbare Script-Beschreibungen

### Einordnung

Muun ist zwischen einfachen Wallets (Wallet of Satoshi) und professionellen Setups (eigener Lightning-Node) positioniert: Non-custodial, technisch leistungsfähig, aber mit UX-Fokus. Der Kompromiss: Der Backup-Mechanismus (Emergency Kit + Output Descriptors) ist komplexer als ein einfacher 12-Wort-Seed.

## Related

- [[phoenix-wallet-lightning]]
- [[wallet-of-satoshi]]
- [[skalierung-lightning-ark-statechains]]
- [[lightning-splicing]]
- [[hd-wallets-und-schluesselableitung]]
- [[taproot-musig2-frost]]
- [[selbstverwahrung-und-boersenrisiken]]

## Open Questions

- Wie hat Muun die Umstellung auf Taproot in der Praxis umgesetzt — nutzt die aktuelle Version MuSig2 oder klassisches Multisig?
- Wie verhält sich Muun bei sehr hohen on-chain Gebühren, wenn Submarine Swaps teuer werden?
- Gibt es Pläne für eine Muun-Version ohne LND-Backend (z.B. mit CLN oder LDK)?
