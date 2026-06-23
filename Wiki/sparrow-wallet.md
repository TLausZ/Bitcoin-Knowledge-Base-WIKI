# Sparrow Wallet

**Status:** established
**Last updated:** 2026-06-22 (Pass 34: 7 offizielle Sparrow-Docs)
**Sources:** [[20210714_einblick-bitcoin-internals-sparrow-wallet-bitbox02-de]], [[20220623_bitcoin-multisig-sparrow-bitbox02-de]], [[sparrowwallet-Best Practices]], [[sparrowwallet-Quick Start Guide]], [[sparrowwallet-Connect to Bitcoin Core]], [[sparrowwallet-Server Performance]], [[sparrowwallet-Setup a Coldcard wallet]], [[sparrowwallet-Spending Privately]], [[sparrowwallet-Frequently Asked Questions]]

## Summary

Sparrow Wallet ist eine quelloffene Bitcoin-Desktop-Wallet (Windows, macOS, Linux), entwickelt von Craig Raw, mit vollem Einblick in UTXO-Details, Coin Selection, Multisig, PSBT und flexibler Server-Wahl. Der offizielle Best-Practices-Guide teilt den Bitcoin-Weg in drei Stufen: Beginner (Public Server + Singlesig HW-Wallet), Intermediate (eigener Bitcoin Core Node), Expert (privater Electrum Server + Multisig). Privacy-Funktionen umfassen Coin Control, Stonewall-Fake-Coinjoin, Whirlpool und BIP47/PayNym.

## Body

---

### Philosophie: "Cold-Storage Sweating"

Craig Raw (Sparrow-Entwickler) beschreibt das Ziel seiner Wallet als «cold-storage sweating»: Das leichte Unbehagen beim Senden einer Bitcoin-Transaktion ist ein Feature. Sparrow zeigt alle technischen Details, damit man bei jeder Transaktion inne hält und prüft, ob alles stimmt — im Gegensatz zu Wallets, die Einfachheit über Transparenz stellen.

---

### Server-Wahl

Sparrow bietet vier Server-Optionen:

- **Public Server:** Einfachste Option; der Server kennt alle Adressen und die IP-Adresse des Nutzers. Nur für kleine Beträge empfohlen.
- **Bitcoin Core:** Eigener Node mit integriertem Wallet-Index. Volle Selbstständigkeit, aber Bitcoin Core speichert Public Keys und Saldo unverschlüsselt auf der Festplatte.
- **Private Electrum Server:** Fulcrum, Electrs oder ElectrumX auf eigenem Raspberry Pi oder Fertigknoten. Speichert keine Wallet-spezifischen Daten — nur einen allgemeinen Blockchain-Index. Beste Kombination aus Privatsphäre und Performance.
- **BitBox-Server:** Shift Cryptos Electrum-Angebot, als Kompromiss für BitBox02-Nutzer.

Wie bei [[electrum-wallet]] gilt: Der Server kennt alle Adressen und Transaktionen der Wallet. Eigener Electrum Server = maximale Privatsphäre.

---

### Best Practices: Drei Stufen der Selbstverwahrung

Craig Raws offizielle Empfehlung teilt den Bitcoin-Weg nach Betrag in drei Stufen. [[sparrowwallet-Best Practices]]

**Stufe 1 — Beginner (bis ca. $10.000)**

Public Server oder der vertrauenswürdige Node eines Freundes. Singlesig-Wallet mit Hardware-Wallet via USB oder QR-Codes. Seed-Backup sicher verwahren, idealerweise an zweitem Ort. Coins von der Börse nehmen ist der erste Schritt — mehr Sicherheit ist zu diesem Zeitpunkt unrealistisch zu erwarten, aber auch nicht nötig.

**Stufe 2 — Intermediate (bis ca. $100.000)**

Eigener Bitcoin Core Node. Wer seinen Kontostand mit einem Public Server teilt, macht sich zum Ziel — je nach Jurisdiktion früher als gedacht. Bitcoin Core kann im Pruned Mode laufen (reduzierter Speicher). Der Nutzer validiert Transaktionen selbst und trägt zur Dezentralisierung des Netzwerks bei.

*Wichtige Einschränkung:* Bitcoin Core speichert Public Keys und Saldo unverschlüsselt auf dem Rechner. Bei dauerhafter Internetverbindung ist der Rechner dadurch ein Angriffsziel, sobald das Guthaben entdeckt wird.

**Stufe 3 — Expert (bedeutende Teile des Vermögens)**

Echter Cold-Storage-Anforderungen:
- Privater Electrum Server (Fulcrum empfohlen) — kein Wallet-Record auf dem Server
- Starkes Wallet-Passwort
- Mindestens 2-von-3 Multisig
- Hardware-Wallets von mehreren Herstellern (damit eine Sicherheitslücke beim Hersteller kein vollständiges Kompromiss bedeutet)
- Hardware-Wallets und Backups an verschiedenen, sicheren Orten
- Kalte Wallet so wenig wie möglich in Sparrow geöffnet

---

### Coldcard-Integration (Air-Gapped Setup)

Sparrow unterstützt Coldcard vollständig, einschließlich des vollständig air-gapped Workflows via microSD-Karte. [[sparrowwallet-Setup a Coldcard wallet]]

**Setup-Ablauf (Air-Gapped):**

1. Coldcard mit Batterie oder Wandstecker betreiben — nie mit dem Computer verbinden.
2. PIN einrichten (zweiteilig, z.B. `1234-5678`). Anti-Phishing-Wörter merken — sie verifizieren, dass die Coldcard echt ist.
3. Neues Wallet anlegen, 24-Wort-Seed schreiben. Optionale Zufallserhöhung: 100× Würfeln mit `4`-Taste.
4. Export: `Advanced > MicroSD Card > Export Wallet > Generic JSON` → `coldcard-export.json` auf SD-Karte.
5. In Sparrow: Datei > Neues Wallet > Airgapped Hardware Wallet > Coldcard > Import File > `coldcard-export.json`.

Sparrow importiert damit nur den Public Key (xpub) — Private Keys verlassen die Coldcard nie. Saldo und Adressen werden in Sparrow angezeigt, Signaturen erfolgen auf der Coldcard.

**PSBT-Workflow für Transaktionen:**
- In Sparrow Transaktion erstellen → als PSBT auf SD-Karte exportieren
- Auf Coldcard laden, Details auf Coldcard-Display prüfen und signieren
- Signiertes PSBT zurück auf SD-Karte → in Sparrow laden und broadcasten

Der USB-Workflow (Connected Hardware Wallet) ist auch möglich, falls kein vollständiges Air-Gap benötigt wird.

---

### UTXO-Ansicht und Coin Control

Sparrow zeigt alle UTXOs der Wallet direkt — nicht nur den Gesamtsaldo. Das ermöglicht gezielte Auswahl der Coins bei einer Transaktion (Coin Control). Mehrere Algorithmen stehen zur Wahl: Branch and Bound (minimale Gebühren), manuelle Auswahl, oder Optimierung für Privatsphäre.

UTXOs lassen sich mit Labels versehen und einfrieren — «freeze» verhindert, dass ein UTXO versehentlich in einer Transaktion verwendet wird.

---

### Privacy-Funktionen

Sparrow implementiert mehrere Techniken für privateres Transaktieren. [[sparrowwallet-Spending Privately]]

**Stonewall (Fake Coinjoin):** Eine Transaktion, die allein erstellt wird, aber für externe Beobachter wie ein Zwei-Personen-Coinjoin aussieht. Funktioniert mit Hardware-Wallets. Voraussetzung: Das Wallet muss mehr als das Doppelte des Zahlbetrags als Saldo haben. Aktivierung: Im Send-Tab „Privacy" Toggle auswählen.

**Whirlpool Coinjoin:** Sparrow integriert Samourai Wallets Whirlpool-Protokoll direkt. UTXOs werden in eine Pool-Größe (0,01 BTC, 0,05 BTC, etc.) eingebracht, dann in mehreren Mixes mit anderen Teilnehmern versehen, bis die Verbindung zur Herkunft kryptographisch gebrochen ist. Post-Mix-UTXOs werden in einem separaten Konto verwaltet.

**PayNym / BIP47:** Jede Wallet kann einen Payment Code (analog zu einem xpub, aber ohne Wallet-Informationen preiszugeben) erstellen. Payment Codes ermöglichen es, wiederholt an dieselbe Person zu zahlen, ohne jedes Mal eine neue Adresse anfragen zu müssen — und ohne die Privatsphäre des Empfängers zu verletzen. PayNyms sind kurze Aliases für Payment Codes (z.B. `+roundgrass881`). Eine einmalige Notification-Transaktion (546 sats + Fee) verknüpft Sender und Empfänger.

**Payjoin:** Transaktionstechnik, bei der Sender und Empfänger gemeinsam Inputs einbringen, was die Common-Input-Ownership-Heuristik (alle Inputs gehören demselben Besitzer) durchbricht.

---

### Pay-to-many

Sparrow unterstützt Ausgaben an mehrere Empfänger in einer einzigen Transaktion — spart Gebühren und Blockplatz für Batch-Auszahlungen.

---

### Multisig

Sparrow ist eine bevorzugte Desktop-Oberfläche für Bitcoin-Multisig. Extended Public Keys (xpubs) aller beteiligten Hardware-Wallets werden in Sparrow konfiguriert; Transaktionen werden via PSBT nacheinander auf den Devices signiert. Für echten Cold Storage empfiehlt Craig Raw 2-von-3 mit Hardware-Wallets verschiedener Hersteller. [[20220623_bitcoin-multisig-sparrow-bitbox02-de]]

---

### Bitcoin Core verbinden

Für die Anbindung an einen lokalen Bitcoin Core Node muss `bitcoin.conf` die Zeile `server=1` enthalten. Danach in Sparrow unter Einstellungen > Server > Bitcoin Core die RPC-Credentials oder Cookie-Authentifizierung konfigurieren. [[sparrowwallet-Connect to Bitcoin Core]]

Für Pruned Nodes: Sparrow kann auch mit prunierten Nodes arbeiten; Transaktionshistorie wird jedoch nur ab dem Pruning-Zeitpunkt angezeigt.

---

### Electrum Server: Implementierungsvergleich

Wer einen eigenen Electrum Server betreiben will, hat drei relevante Optionen (Benchmark auf Raspberry Pi 4, 8 GB RAM, 1 TB USB-SSD, Stand Feb 2022): [[sparrowwallet-Server Performance]]

| Implementierung | Sync-Dauer (Pi 4) | DB-Größe | txindex nötig? | Stärke |
|---|---|---|---|---|
| **Fulcrum** | 2–3 Tage | ~102 GB | Ja | Beste Query-Performance, C++ |
| **Electrs** | 12–24 Stunden | ~32 GB | Nein | Kleinster Footprint, auf Prebuilt-Nodes verbreitet |
| **ElectrumX** | ~1 Woche | ~75 GB | Ja | Öffentliche Server; für persönlichen Einsatz überdimensioniert |

**Sparrow-Empfehlung:** Fulcrum für beste Performance. Electrs für minimalen Speicherbedarf oder Raspberry Pi mit knappem Speicher. ElectrumX ist für öffentliche Server gedacht und auf Heimhardware kaum sinnvoll.

Ein Electrum Server speichert — anders als Bitcoin Core mit Wallet — keine nutzerspezifischen Daten. Alle Wallet-Details bleiben ausschließlich in der Sparrow-Wallet-Datei.

---

## Related

- [[electrum-wallet]]
- [[multisig-und-kollaborative-verwahrung]]
- [[utxo-modell-und-konsolidierung]]
- [[coinjoin-und-on-chain-privatsphäre]]
- [[hd-wallets-und-schluesselableitung]]
- [[airgap-und-kommunikationskanaele]]
- [[hardware-wallet-einstieg]]
- [[bitcoin-netzwerk-und-nodes]]

## Open Questions

- Wie verhält sich Sparrow zu Silent Payments (BIP352) — ist Integration geplant?
- Whirlpool-Status nach Samourai-Verhaftung (April 2024): Ist der Coordinator noch aktiv, oder muss ein eigener betrieben werden?
- Payjoin v2 (serverless) — wann kommt Support in Sparrow?
