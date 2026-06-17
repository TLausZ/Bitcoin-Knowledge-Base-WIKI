# Airgap und Kommunikationskanäle bei Hardware-Wallets

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20211104_macht-airgap-bitcoin-hardware-wallets-sicherer-de]]

## Summary

"Airgap" — die physische Trennung einer Hardware-Wallet vom Computer über QR-Code oder microSD statt USB — bietet nach einer detaillierten Analyse von Shift Crypto wenig bis keinen messbaren Sicherheitsvorteil gegenüber einer USB-Verbindung. Alle elf bekannten Hardware-Wallet-Schwachstellen von 2020–2021 hätten durch Airgap nicht verhindert werden können. Die Sicherheit liegt nicht im Übertragungskanal, sondern in der Transaktionsvalidierung durch die Hardware-Wallet selbst. Airgap verschlechtert die Benutzerfreundlichkeit erheblich und macht Sicherheitsprotokolle wie Anti-Klepto aufwändiger.

## Body

### Was Airgap bei Hardware-Wallets bedeutet

"Airgap" bezeichnet die Nutzung einer Hardware-Wallet ohne direkte physische Verbindung (USB) zum Computer. Stattdessen wird Kommunikation über QR-Codes (Display auf HW-Wallet, Kamera auf Computer) oder microSD-Karten überbrückt. Die zugrundeliegenden Daten sind PSBT-Dateien (Partially Signed Bitcoin Transactions) — ein Standard für unsignierte Transaktionen, der unabhängig vom Übertragungskanal ist.

### Drei Gründe, warum Airgap keinen signifikanten Sicherheitsvorteil bietet

**1. Kommunikation findet immer noch statt.** Auch ohne USB-Kabel tauschen Hardware-Wallet und Computer Informationen aus. Der Unterschied liegt nur in der Bandbreite (QR-Codes übertragen weniger Daten als USB), nicht in der grundsätzlichen Fähigkeit, schädliche Daten zu übermitteln. Wie der Stuxnet-Angriff auf iranische Atomanlagen zeigte: Ein Kommunikationskanal allein verhindert keine bösartigen Daten. Es ist immer die Hardware-Wallet selbst, die empfangene Daten gründlich prüfen muss.

**2. Jeder Kanal kann kompromittiert werden.** Malware kann QR-Codes über Hintertüren in Kamera-Bibliotheken verändern, PSBT-Dateien auf microSD manipulieren oder USB-Daten abfangen — der Angriffsvektor wechselt, er verschwindet nicht. Die BitBox02 schützt sich dagegen durch Ende-zu-Ende-Verschlüsselung (Noise Protocol Framework) über USB, was Manipulation und Abhören deutlich erschwert. MicroSD-Karten enthalten selbst einen Mikrocontroller mit eigener Firmware — ist das wirklich "kein Computer im Spiel"?

**3. Airgap-Daten sind nicht transparenter.** PSBT-Dateien sind Binärdaten — für Menschen nicht lesbar, ob als Datei oder in QR-Code-Form. Ein normaler QR-Code-Scanner zeigt nur Zeichensalat. Die Aussagen mancher Hersteller, QR-Codes seien "kontrollierbar und transparent", halten der Realität nicht stand.

### Realitätscheck: 11 HW-Wallet-Exploits 2020–2021

Alle bekannten Schwachstellen dieser Periode hätten durch Airgap nicht verhindert werden können:

- **Lieferketten-Angriff** (Coldcard, 2020/03): physischer Angriffsvektor
- **OP_RETURN als Change-Output** (Trezor, 2020/03): Transaktionsvalidierungsproblem
- **Manipulierte Change-Adresse in Mixed Transactions** (Trezor, 2020/03): Transaktionsvalidierung
- **Hohe Gebühr via Doppel-Signierung** (alle Hersteller, 2020/03): allgemeines BIP-143-Problem
- **JTAG/SWD auf ungesichertem Prozessor** (Ledger, 2020/06): physisch
- **Altcoin-Isolations-Bypass** (Ledger/Trezor/Keepkey, 2020/08): Transaktionsvalidierung
- **Testnet/Mainnet-Bypass** (Coldcard, 2020/08): Transaktionsvalidierung
- **Passphrase-Erpressungsangriff** (Trezor/Keepkey, 2020/08): Passphrase muss unabhängig vom Kanal direkt auf dem Gerät geprüft werden
- **Remote Multisig-Diebstahl** (Coldcard, 2020/11): Bei Airgap-Setup von Hand (ohne externen Koordinator) teilweise vermeidbar — aber nicht durch Airgap selbst
- **Length-Extension-Angriff** (Ledger, 2021/05): Firmware-Ebene

Das Muster ist eindeutig: Schwachstellen liegen auf der Logik-Ebene (Transaktionsvalidierung, Schlüsselhandling), nicht auf der Transportebene.

### Wann Airgap tatsächlich nützlich ist

**PSBT und Drittanbieter-Integration.** PSBT als Standard ermöglicht Interoperabilität zwischen Hardware-Wallets und Software-Wallets — unabhängig vom Kanal. QR-Codes sind nützlich für Hardware wie SeedSigner oder Specter DIY, und für iOS-Geräte, die USB einschränken. Das ist ein legitimer Anwendungsfall, hat aber nichts mit dem Sicherheitsversprechen von "Airgap" zu tun.

**"Keine Kommunikation" als echter Schutz.** Der einzige echte Sicherheitsgewinn entsteht nicht durch "air-gapped communication", sondern durch vollständige Isolation vom nicht vertrauenswürdigen Gerät. Beispiel: Beim Einrichten einer Multisig-Wallet kann man die Geräte manuell miteinander verbinden (microSD von Gerät zu Gerät), ohne einen externen Koordinator zu involvieren. Das verhindert den Remote-Multisig-Theft-Angriff. Für laufende Transaktionen braucht man aber externe Daten — "keine Kommunikation" ist dort keine Option.

### Benutzerfreundlichkeit ist Sicherheit

Mehr Schritte = mehr Fehlerquellen. Ein Airgap-Nutzer wird zum manuellen "Man-in-the-Middle" des Kommunikationskanals — ohne die Fähigkeit, die übertragenen Daten zu prüfen. Das erhöht die Komplexität ohne nachweisbaren Sicherheitsgewinn.

Zukünftige Sicherheitsprotokolle verschärfen das Problem: Anti-Klepto (Schutz vor privatem Schlüssel-Exfiltration) benötigt eine zusätzliche Kommunikationsrunde. Mit Airgap bedeutet das eine weitere Runde manuelles QR-Code-Scannen bei jeder Transaktion.

Das Fazit der Analyse: Die Wahl des Kommunikationskanals ist primär eine Entscheidung über Benutzerfreundlichkeit und App-Integration, nicht über Sicherheit.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[komplexität-ist-keine-sicherheit]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[multisig-und-kollaborative-verwahrung]]

## Open Questions

- Hat sich die Sicherheitsbewertung von Airgap seit 2021 verändert — neue Exploits, neue Erkenntnisse?
- Wie verhält sich Airgap bei Hardware-Wallets ohne sicheren Chip (z.B. SeedSigner)?
