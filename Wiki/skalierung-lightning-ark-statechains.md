# Skalierung: Lightning, Ark und Statechains

**Status:** emerging
**Last updated:** 2026-06-08
**Sources:** [[20251218_die-skalierung-von-bitcoin-lightning-und-der-weg-zu-ark]], [[20260212_bitcoin-senden-ohne-sie-zu-bewegen-statechains-erklärt]], [[20231018_lightning-in-der-bitboxapp]], [[20240314_wie-die-bitbox02-den-seed-für-die-lightning-wallet-sicher-ableitet]]

## Summary

Bitcoin skaliert nicht durch größere Blöcke, sondern durch Second-Layer-Protokolle, die den größten Teil der Aktivität außerhalb der Hauptkette abwickeln. Lightning ist das etablierte Netzwerk für schnelle Peer-to-Peer-Zahlungen, leidet aber am Last-Mile-Problem für technisch weniger erfahrene Nutzer. Ark adressiert dieses Problem mit einem geteilten UTXO-Modell (VTXOs). Statechains gehen einen anderen Weg: Eigentum wird übertragen, ohne Bitcoin zu bewegen.

## Body

### Lightning

Lightning ist ein Netzwerk aus Multisignatur-Verträgen, die einen gemeinsamen Bitcoin-Betrag sperren. Zwei Parteien können ihren gemeinsamen Kontostand unbegrenzt oft aktualisieren, ohne für jede Änderung eine On-Chain-Transaktion zu erstellen. Die Transaktionskapazität ist praktisch unbegrenzt.

Lightning eignet sich hervorragend für schnelle, private Peer-to-Peer-Zahlungen. Das **Last-Mile-Problem** ist der Haken: Um Lightning selbst zu betreiben, braucht man eine eigene Node und muss Liquidität verwalten. Lightning Service Provider (LSP) wie Phoenix oder Breez abstrahieren diese Komplexität, sind aber nicht vollständig vertrauenslos.

### Ark

Ark (2023 vorgestellt, erste öffentliche Implementierungen 2024/2025) löst das Last-Mile-Problem mit einer anderen Architektur. Das Bild: Lightning ist ein Kurierdienst, Ark ist ein Zug — Nutzer steigen ein und können sofort mit allen anderen Passagieren im selben Zug transagieren.

**Wie Ark funktioniert:**
- Nutzer senden Bitcoin an eine Ark-kompatible Wallet und erhalten **VTXOs** (Virtual Transaction Outputs) — Guthaben, das noch nicht on-chain verankert ist
- Alle VTXOs werden in geteilten Containern (shared UTXOs) gehalten, die im Bitcoin-Netzwerk verankert sind
- Ein **Ark Server (Operator)** koordiniert Transaktionen, hat aber keine Verwahrung über die Gelder
- In regelmäßigen Abständen veröffentlicht der Server einen neuen „Schnappschuss" aller Guthaben on-chain

**Vertrauensmodell:** Nutzer müssen dem Operator für Bequemlichkeit vertrauen, nicht für Verwahrung. Jederzeit kann man einseitig aussteigen und Gelder direkt on-chain zurückholen (Exit-Transaktion).

### Statechains

Statechains gehen einen konzeptionell anderen Weg: Statt Bitcoin zu versenden, wird das **Eigentum** über Bitcoin übertragen — ohne dass sich die Coins on-chain bewegen.

**Das Grundprinzip:** Ein Bitcoin-Output (UTXO) bleibt an einer festen on-chain Adresse. Um das Eigentum zu übertragen, führen der aktuelle Besitzer und eine Statechain-Entity eine „Key Rotation" durch: Der neue Besitzer erhält einen neuen kryptografischen Schlüssel, die Entity löscht das Fragment des alten Besitzers.

**Schutzmechanismus gegen Betrug:** Jede Übertragung enthält eine vorab signierte Exit-Transaktion. Um zu verhindern, dass frühere Besitzer betrügen, verwendet das System **abnehmende Timelocks** — der aktuelle Besitzer hat immer den kürzesten Timelock und gewinnt deshalb das „Rennen zum Ausgang".

**Einschränkung:** Man muss der Statechain-Entity vertrauen, dass sie alte Schlüsselanteile wirklich löscht. Projekte wie Mercury Layer und Spark setzen dieses Modell bereits produktiv ein.

### Lightning in Wallet-Apps (BitBoxApp + Breez)

Das Last-Mile-Problem für Endnutzer adressiert die BitBoxApp mit einer eingebetteten Lightning-Wallet über das Breez SDK. Der Node läuft auf Blockstream Greenlight-Infrastruktur in der Cloud; die privaten Schlüssel bleiben auf dem Gerät des Nutzers. Kein Channel-Management, keine manuelle Liquiditätsverwaltung — Breez stellt eingehende Liquidität bereit.

Sicherheitskonzept: Die Lightning-Schlüssel sind eine Hot Wallet (auf dem Smartphone/Computer), nicht auf der BitBox02 gespeichert. Das ist ein bewusster Kompromiss — Lightning ist für kleinere Beträge konzipiert, und die Bequemlichkeit erfordert permanenten Online-Zugang der Schlüssel. Als Schutz: Der Lightning-Seed wird via BIP-85 aus dem Haupt-Seed abgeleitet. Ein einziges Backup der 24 Wörter deckt Cold Storage und Lightning — kein separates Backup nötig.

### Vergleich

| | Lightning | Ark | Statechains |
|---|---|---|---|
| Analogie | Kurierdienst | Eisenbahn | Grundbuchamt |
| Routing nötig? | Ja | Nein | Nein |
| Vertrauen | LSP-Option | Operator (kein Custody) | Entity (löscht Schlüssel) |
| Reife | Produktiv | Frühe Phase | Frühe Phase |

Ark und Lightning schließen sich nicht aus — Ark kann als „Onramp" für Lightning dienen.

## Related

- [[bitcoin-vaults]]
- [[taproot-musig2-frost]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]

## Open Questions

- Wie reif wird Ark für Endnutzer in den nächsten Jahren?
- Können Statechains mit Teilbeträgen (Spark) Lightning als Zahlungskanal ersetzen?
- Welche Rolle spielen Covenants für bessere Ark-Implementierungen?
