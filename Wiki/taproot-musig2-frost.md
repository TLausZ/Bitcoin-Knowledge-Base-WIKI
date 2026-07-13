# Taproot, MuSig2 und FROST

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-06
**Sources:** [[20250206_musig2-und-frost-multisignaturverfahren-auf-taproot-erklärt]], [[20220818_taproot-keim-bitcoin-anwendungen-de]], [[20220118_bitbox-01-2022-maighels-update-de]], [[20220331_bitbox-03-2022-glaernisch-update-de]], [[learnmeabitcoin-technical-upgrades-taproot]]

## Summary

Taproot (aktiviert 2021) verbessert Privatsphäre und Effizienz von Bitcoin-Transaktionen, indem es zwei Ausgabewege bietet: Key-Path (eine einzige Signatur, alle Details versteckt) und Script-Path (alternative Bedingungen, nur teils offengelegt). MuSig2 nutzt Schnorr-Linearität, um mehrere Signaturen zu einer aggregierten Signatur zu kombinieren — Multisig-Transaktionen werden dadurch unsichtbar. FROST erweitert das auf Threshold-Signaturen (z.B. beliebige 2 von 4).

## Body

### Was Taproot ist: Kontext und Einführung

Taproot ist eine **Soft Fork** — eine rückwärtskompatible Regeländerung des Bitcoin-Protokolls. Sie wurde im November 2021 aktiviert (Block 709.632). Ältere Nodes akzeptieren Taproot-Transaktionen weiterhin, können aber die neuen Privatsphäre-Vorteile nicht vollständig validieren.

Taproot kombiniert drei Verbesserungen in einem Upgrade: **Schnorr-Signaturen** (neuer kryptografischer Algorithmus), **MAST** (Merkelized Abstract Syntax Trees, für effizientere Ausgabebedingungen) und **Tapscript** (überarbeitetes Scripting-System). Zusammen legen sie den Grundstein für MuSig2 und FROST.

**Schnorr vs. ECDSA:** Bis Taproot verwendete Bitcoin ECDSA-Signaturen. Schnorr hat eine wichtige Eigenschaft, die ECDSA fehlt: **Linearität**. Mehrere Schnorr-Signaturen können addiert werden, was Signatur-Aggregation (MuSig2, FROST) überhaupt erst möglich macht.

**MAST:** Ausgabebedingungen (Timelock, Multisig-Backup, etc.) werden als Merkle-Baum kodiert. Beim Ausgeben wird nur der tatsächlich verwendete Pfad offengelegt — nicht alle anderen Bedingungen. Das verbessert sowohl Privatsphäre als auch Effizienz (weniger Daten on-chain).

**Nachteile:** Einfache Taproot-Transaktionen kosten etwas mehr als entsprechende SegWit-Transaktionen, weil das Adressformat mehr Daten enthält. Bei komplexen Transaktionen (Multisig, Lightning) ist Taproot günstiger. Außerdem fehlte zum Zeitpunkt der Einführung Anti-Klepto-Unterstützung für Taproot-Signaturen, da die zugrundeliegende Bibliothek (libsecp256k1) das Protokoll noch nicht implementiert hatte.

**Rollout in Hardware-Wallets:** Die schrittweise Taproot-Implementierung zeigt, wie neue Bitcoin-Protokoll-Features in Hardware-Wallets integriert werden. Bei der BitBox02 erschien das Senden an Taproot-Adressen (bc1p) im Januar 2022 (Maighels-Update); das Empfangen auf Taproot-Adressen folgte im März 2022 (Glärnisch-Update, Firmware v9.10.0). Der Standardadresstyp blieb Native SegWit, da noch viele andere Wallets Taproot nicht unterstützten. Anti-Klepto für Schnorr-Signaturen war zum Zeitpunkt des Glärnisch-Updates noch nicht verfügbar.

### Bitcoin-Scripting: Das Problem

Herkömmliche Multisig-Wallets müssen beim Ausgeben ihr volles Skript offenlegen — wie viele Schlüssel beteiligt sind, welche Konfiguration. Das hat zwei Nachteile: schlechte Privatsphäre (jeder sieht die Konfiguration) und höhere Transaktionsgebühren (mehr Daten on-chain).

### Taproot: Key-Path und Script-Path

Ein Taproot-Output enthält immer einen einzigen öffentlichen Schlüssel. Beim Ausgeben gibt es zwei Wege:

**Key-Path:** Eine einzige gültige Signatur reicht — keine weiteren Details werden offengelegt. Alle Key-Path-Transaktionen sehen identisch aus, unabhängig davon, ob dahinter eine einfache Wallet, Multisig oder ein Lightning-Kanal steckt.

**Script-Path:** Für alternative Ausgabebedingungen (z.B. Notfall-Backup). Nur die tatsächlich verwendeten Teile des Skripts werden offengelegt — nicht alle möglichen Pfade.

### MuSig2: Signatur-Aggregation

Schnorr-Signaturen sind linear: Mehrere Signaturen können addiert werden. MuSig2 nutzt das, um eine **aggregierte Signatur** aus n Unterzeichnern zu erstellen, die wie eine einzelne Signatur aussieht.

Ergebnis: Ein 4-von-4 Multisig-Setup erzeugt eine on-chain Transaktion, die von einer 1-von-1 Wallet nicht zu unterscheiden ist. Bessere Privatsphäre und niedrigere Gebühren (weniger Daten on-chain).

**Kompromiss:** MuSig2 erfordert 2 Kommunikationsrunden zwischen den Unterzeichnern und ist auf n-von-n beschränkt — kein nativer Schwellenwert.

### FROST: Threshold-Signaturen

FROST (*Flexible Round-Optimized Schnorr Threshold*) ermöglicht Schwellenwert-Signaturen: Beliebige k von n Unterzeichnern können gemeinsam eine gültige aggregierte Signatur erstellen (z.B. 2 von 4).

Dafür braucht es eine besondere Schlüsselerzeugung:
- **Vertrauenswürdige Partei** generiert und verteilt Schlüsselanteile (einfach, erfordert Vertrauen)
- **Distributed Key Generation (DKG):** Alle Parteien erzeugen Schlüssel gemeinsam in einer interaktiven Sitzung (sicherer, komplexer)

Eine FROST Key-Path Ausgabe sieht ebenfalls wie jede andere Taproot-Transaktion aus — niemand kann erkennen, welche Kombination der Unterzeichner die Coins ausgegeben hat.

### Zusammenfassung: Was es bringt

| | Herkömmliches Multisig | MuSig2 (n-von-n) | FROST (k-von-n) |
|---|---|---|---|
| Privatsphäre | Schlecht (sichtbar) | Sehr gut | Sehr gut |
| Gebühren | Höher | Niedriger | Niedriger |
| Schwellenwert | Ja | Nein | Ja |
| Interaktivität | Gering | Mittel (2 Runden) | Hoch (DKG) |

Die Technologien skalieren besonders für größere Organisationen mit komplexeren Anforderungen — sind aber auch für Privatnutzer interessant, die Gebühren sparen und Privatsphäre verbessern wollen.

## Related

- [[shamir-secret-sharing]]
- [[multisig-und-kollaborative-verwahrung]]
- [[bitcoin-vaults]]
- [[skalierung-lightning-ark-statechains]]

## Open Questions

- Wann werden MuSig2 und FROST in gängigen Wallet-Software-Implementierungen (inkl. Hardware-Wallets) verfügbar sein?
- Wie entwickelt sich die Komplexität für Endnutzer bei DKG?
