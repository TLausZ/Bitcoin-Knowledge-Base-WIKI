# Electrum Wallet

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20210107_bitbox02-electrum-anleitung-de]], [[20210531_erweiterte-electrum-funktionen-de]]

## Summary

Electrum ist die bevorzugte Bitcoin-Wallet für Power-User: voller Funktionsumfang (Coin Control, RBF, Pay-to-many, Tor, Watch-only), kompatibel mit Hardware-Wallets und konfigurierbarer Server-Anbindung. In Kombination mit der BitBox02 bleiben private Schlüssel immer auf dem Gerät — Electrum übernimmt nur die Benutzeroberfläche und die Netzwerkkommunikation.

## Body

### Was Electrum ist

Electrum ist eine freie, quelloffene Bitcoin-Software für Windows, Mac und Linux. Sie verbindet sich mit einem Electrum-Server, der die Blockchain indexiert und relevante Daten liefert (Adressen, Salden, Gebührenschätzungen). Electrum kann als reine Software-Wallet (private Schlüssel auf dem PC) oder als Begleit-App für Hardware-Wallets laufen.

**Installation:** Ausschließlich von [electrum.org](https://www.electrum.org) herunterladen. Die Domain genau prüfen — Fake-Domains verbreiten Malware. Die PGP-Signatur der heruntergeladenen Datei lässt sich auf der offiziellen Website verifizieren.

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

**Replace-by-Fee (RBF):** Macht eine Transaktion nachträglich austauschbar. Nützlich wenn der Mempool sich füllt und eine Transaktion mit zu niedriger Gebühr steckt. Die BitBoxApp kennzeichnet Transaktionen standardmäßig mit RBF, damit sie später in Electrum erhöht werden können. Einstellungen → Transaktionen → "Replace-by-fee aktivieren".

**Pay-to-many:** "Werkzeuge → Zahle an mehrere" — mehrere Empfängeradressen und Beträge in Zeilen oder CSV-Import. Spart Blockplatz und Gebühren gegenüber mehreren Einzeltransaktionen.

**Coin Control:** "Ansicht → Coins anzeigen" zeigt alle UTXOs. Per Kontextmenü kann ein UTXO direkt ausgegeben oder eingefroren werden. Nützlich für CoinJoin-Vorbereitung oder um Coins aus verschiedenen Quellen nicht zu vermischen.

**Watch-only Wallets:** Wallet mit dem Extended Public Key (xpub) einrichten, ohne private Schlüssel. Ermöglicht Saldoüberwachung ohne Ausgabemöglichkeit. xpub in der BitBoxApp unter "Kontoinformationen" einsehen. In Electrum: "Datei → Neu → Standard → Einen Generalschlüssel verwenden → xpub einfügen". Achtung: Empfangsadressen können bei Watch-only nicht auf dem BitBox02-Display verifiziert werden — nur für kleine Beträge geeignet.

**Paper-Wallet entleeren:** "Geldbörse → Private Schlüssel → Entleeren" erstellt eine Transaktion, die den gesamten Betrag in die aktuelle Wallet überträgt. Hot-Wallet-Operation: Die privaten Schlüssel des Paper-Wallets sind kurzzeitig auf dem Computer sichtbar.

**Tor-Integration:** "Werkzeuge → Netzwerk → Proxy → Tor Proxy auf Port 9150 nutzen". LED wechselt von grün zu blau. Schützt die IP-Adresse bei öffentlichen Servern und erlaubt bei eigenem Server den Zugang ohne spezielle Netzwerkkonfiguration (kein Port-Forwarding nötig).

## Related

- [[hd-wallets-und-schluesselableitung]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[utxo-modell-und-konsolidierung]]
- [[coinjoin-und-on-chain-privatsphäre]]
- [[transaktionsgebuehren-und-mempool]]

## Open Questions

- Wie verhält sich Electrum zu neuen Bitcoin-Protokollfunktionen wie Silent Payments oder Taproot-basierten Multisig-Setups?
