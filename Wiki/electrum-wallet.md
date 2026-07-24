# Electrum Wallet

**Status:** established
**Themen:** protokoll, privacy, wallets
**Last updated:** 2026-06-28
**Sources:** [[20210107_bitbox02-electrum-anleitung-de]], [[20210531_erweiterte-electrum-funktionen-de]], [[sparrowwallet-Server Performance]], [[alex-waltz-electrum-first-deterministic-wallet]]

## Summary

Electrum ist die bevorzugte Bitcoin-Wallet für Power-User: voller Funktionsumfang (Coin Control, RBF, Pay-to-many, Tor, Watch-only), kompatibel mit Hardware-Wallets und konfigurierbarer Server-Anbindung. In Kombination mit der BitBox02 bleiben private Schlüssel immer auf dem Gerät — Electrum übernimmt nur die Benutzeroberfläche und die Netzwerkkommunikation.

## Body

### Was Electrum ist

Electrum ist eine freie, quelloffene Bitcoin-Software für Windows, Mac und Linux. Sie verbindet sich mit einem Electrum-Server, der die Blockchain indexiert und relevante Daten liefert (Adressen, Salden, Gebührenschätzungen). Electrum kann als reine Software-Wallet (private Schlüssel auf dem PC) oder als Begleit-App für Hardware-Wallets laufen.

**Installation:** Ausschliesslich von [electrum.org](https://www.electrum.org) herunterladen. Die Domain genau prüfen — Fake-Domains verbreiten Malware. Die PGP-Signatur der heruntergeladenen Datei lässt sich auf der offiziellen Website verifizieren.

### Server-Wahl ist eine Datenschutzentscheidung

Electrum kommuniziert nicht direkt mit dem Bitcoin-Netzwerk, sondern immer über einen Electrum-Server. Dieser Server kennt alle Transaktionen und Adressen der Wallet — und damit faktisch das vollständige Finanzverhalten. Es ist anzunehmen, dass Blockchain-Analyse-Firmen öffentliche Electrum-Server betreiben, um genau diese Daten zu sammeln.

Deshalb gilt: Electrum nur dann einsetzen, wenn man sich mit einem vertrauenswürdigen Server verbindet. Die beste Option ist der eigene Server — entweder via Electrum Personal Server auf einem laufenden Bitcoin-Node oder als eigenständiges Gerät (z.B. RaspiBolt auf einem Raspberry Pi).

Optionen im Überblick:
- **Automatisch (öffentlicher Server):** Einfach, aber datenschutzproblematisch
- **Manuell (eigener Server):** Beste Privatsphäre, erfordert eigenen Node
- **Tor:** Verbirgt IP-Adresse auch bei öffentlichem Server (Port 9150 in den Proxy-Einstellungen)

### Wallet mit BitBox02 einrichten

1. BitBox02 anschliessen; Bildschirm zeigt "See the BitBoxApp". BitBoxApp darf nicht gleichzeitig laufen.
2. Electrum: "Datei → Neu/Wiederherstellen", Wallet benennen.
3. Wallet-Typ: "Standard" → Schlüsselspeicher: "Hardware-Gerät".
4. BitBox02 aus der Liste wählen; Gerätepasswort eingeben.
5. Paarungscode vergleichen: Der Code auf dem BitBox02-Display muss mit dem in Electrum übereinstimmen. Bestätigen.

### Adressformate und Ableitungspfade

Electrum fragt beim Einrichten nach dem Adressformat:

- **p2sh-segwit (BIP49):** Adressen beginnen mit "3". Rückwärtskompatibel mit Legacy-Empfängern. Spart Gebühren gegenüber Legacy.
- **Native Segwit / bech32 (BIP84):** Adressen beginnen mit "bc1". Günstigste Option. Nicht alle älteren Wallets unterstützen dieses Format als Zieladresse, aber Senden an alle Formate ist problemlos.

Der **Ableitungspfad** (`m / Zweck' / Coin_Typ' / Konto'`) bestimmt, welches Konto geöffnet wird. Beispiele für Native Segwit: `m/84'/0'/0'` (Konto 0, identisch mit dem BitBoxApp-Bitcoin-Konto), `m/84'/0'/1'` (Konto 1, nur Electrum). Kontonummern fortlaufend halten — ein verlorener Ableitungspfad macht das Konto unauffindbar.

**Empfehlung:** BitBoxApp und Electrum über unterschiedliche Konten laufen lassen, damit Salden nicht vermengt werden.

### Empfangen

Im "Empfangen"-Reiter eine neue Adresse generieren. **Entscheidend:** Das Augensymbol klicken, damit die BitBox02 die Adresse auf ihrem Display anzeigt. Diese mit der Anzeige in Electrum vergleichen. Schadsoftware kann die Adresse in Electrum manipulieren — das Hardware-Wallet-Display zeigt immer die korrekte Adresse.

### Senden

Electrum übergibt eine unsignierte Transaktion an die BitBox02. Das Gerät zeigt die Details auf dem Display (Betrag, Empfangsadresse). Nach Bestätigung auf dem Gerät signiert die BitBox02 und gibt die signierte Transaktion zurück. Private Schlüssel verlassen das Gerät nie.

### Erweiterte Funktionen

**Replace-by-Fee (RBF):** Macht eine Transaktion nachträglich austauschbar. Nützlich wenn der Mempool sich füllt und eine Transaktion mit zu niedriger Gebühr steckt. Die BitBoxApp kennzeichnet Transaktionen standardmässig mit RBF, damit sie später in Electrum erhöht werden können. Einstellungen → Transaktionen → "Replace-by-fee aktivieren".

**Pay-to-many:** "Werkzeuge → Zahle an mehrere" — mehrere Empfängeradressen und Beträge in Zeilen oder CSV-Import. Spart Blockplatz und Gebühren gegenüber mehreren Einzeltransaktionen.

**Coin Control:** "Ansicht → Coins anzeigen" zeigt alle UTXOs. Per Kontextmenü kann ein UTXO direkt ausgegeben oder eingefroren werden. Nützlich für CoinJoin-Vorbereitung oder um Coins aus verschiedenen Quellen nicht zu vermischen.

**Watch-only Wallets:** Wallet mit dem Extended Public Key (xpub) einrichten, ohne private Schlüssel. Ermöglicht Saldoüberwachung ohne Ausgabemöglichkeit. xpub in der BitBoxApp unter "Kontoinformationen" einsehen. In Electrum: "Datei → Neu → Standard → Einen Generalschlüssel verwenden → xpub einfügen". Achtung: Empfangsadressen können bei Watch-only nicht auf dem BitBox02-Display verifiziert werden — nur für kleine Beträge geeignet.

**Paper-Wallet entleeren:** "Geldbörse → Private Schlüssel → Entleeren" erstellt eine Transaktion, die den gesamten Betrag in die aktuelle Wallet überträgt. Hot-Wallet-Operation: Die privaten Schlüssel des Paper-Wallets sind kurzzeitig auf dem Computer sichtbar.

**Tor-Integration:** "Werkzeuge → Netzwerk → Proxy → Tor Proxy auf Port 9150 nutzen". LED wechselt von grün zu blau. Schützt die IP-Adresse bei öffentlichen Servern und erlaubt bei eigenem Server den Zugang ohne spezielle Netzwerkkonfiguration (kein Port-Forwarding nötig).

### Eigener Electrum Server: Implementierungsvergleich

Wer Sparrow oder Electrum an einen eigenen privaten Server anbinden will, hat drei relevante Implementierungen (Benchmark auf Raspberry Pi 4, 8 GB RAM, 1 TB USB-SSD, Stand Feb 2022): [[sparrowwallet-Server Performance]]

| Implementierung | Index-Aufbau (Pi 4) | DB-Grösse | txindex nötig? | Stärke |
|---|---|---|---|---|
| **Fulcrum** | 2–3 Tage | ~102 GB | Ja | Schnellste Query-Performance; C++; Binaries verfügbar |
| **Electrs** | 12–24 Stunden | ~32 GB | Nein | Kleinster Footprint; auf Fertigknoten (Umbrel, MyNode) verbreitet |
| **ElectrumX** | ~1 Woche | ~75 GB | Ja | Für öffentliche Server konzipiert; auf Heimhardware kaum sinnvoll |

Fulcrum ist für persönlichen Einsatz die stärkste Wahl. Electrs ist die schnellste Option für den ersten Start und auf Speicher-limitierter Hardware. ElectrumX lohnt sich nur bei öffentlichem Serverbetrieb.

Ein wichtiger Unterschied zu Bitcoin Core mit Wallet: Electrum-Server speichern keine nutzerspezifischen Daten — nur einen allgemeinen Adress-Index aller Bitcoin-Transaktionen. Wallet-Details verbleiben ausschliesslich in der lokalen Wallet-Datei. Das macht einen eigenen Electrum Server datenschutztechnisch überlegen gegenüber Bitcoin Core im Wallet-Modus (der Public Keys und Saldo unverschlüsselt auf der Festplatte hält).

### Geschichte: Erstes deterministisches Bitcoin-Wallet

Electrum erschien am 5. November 2011 als erstes modernes Bitcoin-Wallet. Davor gab es nur Bitcoin Core (damals noch nicht so genannt) und einige verwahrerische Wallets. Electrum war das erste Wallet, das deterministische Schlüsselableitung bot.

Vor Electrum generierte ein Wallet bei jedem Start neue, unabhängige private Schlüssel. Keine Verbindung zwischen ihnen, kein Restore-Mechanismus. Wer 100 Adressen genutzt hatte, musste 100 private Schlüssel sichern — und bei jedem neuen Wechsel der Schlüssel mehr.

Electrums erster Seed nutzte ein eigenes 1.626-Wörter-Wörterbuch (aus Poesielisten auf Wikipedia gewählt, um Patent-Konflikte zu vermeiden) — das war 2011, zwei Jahre vor BIP39. In Electrum 2.0 (2015) wurde das System überarbeitet: Seitdem enthält der Seed selbst ein Versions-System, das kodiert, um welche Art von Wallet es sich handelt. Das macht Electrum-Seeds bei der Recovery weniger mehrdeutig als BIP39-Seeds, weil der Derivationspfad nicht separat aufbewahrt werden muss.

BIP39 wurde trotzdem De-facto-Standard, weil es von nahezu allen anderen Wallets übernommen wurde. Electrum unterstützt BIP39-Seeds seit Version 4 optional — empfiehlt aber weiterhin den eigenen Seed-Typ. Mehr zu den Schwächen von BIP39: [[bip39-schwache-seeds]].

## Related

- [[hd-wallets-und-schluesselableitung]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[utxo-modell-und-konsolidierung]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[transaktionsgebuehren-und-mempool]]
- [[bip39-schwache-seeds]]
- [[sparrow-wallet]]

## Open Questions

- Wie verhält sich Electrum zu neuen Bitcoin-Protokollfunktionen wie Silent Payments oder Taproot-basierten Multisig-Setups?
- Warum hat BIP39 trotz seiner Schwächen beim Derivationspfad den Electrum-Seed-Standard verdrängt?
