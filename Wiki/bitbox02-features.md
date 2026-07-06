# BitBox02 Features

**Status:** established
**Last updated:** 2026-07-06
**Sources:** [[Feature Highlights of the BitBox02 - EN]]

## Summary

Katalog der Funktionen von BitBox02 und BitBoxApp, wie sie der Hersteller (Shift Crypto/BitBox) in seiner Feature-Highlights-Tabelle auflistet. 33 Einträge, von Datenschutz-Werkzeugen (Coin Control, Silent Payments, eigener Full Node) über Sicherheitsmechanismen (Anti-Klepto, verschlüsselter Seed im RAM, reproduzierbare Builds) bis zu Komfort- und Integrationsfunktionen (WalletConnect, U2F, In-App-Kauf/-Verkauf). Die Angaben stammen aus Herstellermarketing und sind hier zusammengefasst, nicht bewertet. Einzelne Themen haben eigene Artikel mit mehr Tiefe (siehe Related).

## Body

### Schlüssel, Seed und Backups

**Child keys (BIP-85):** Aus dem BitBox02-Seed lassen sich abgeleitete, eigenständige Seed-Phrasen erzeugen. Nutzen etwa für Hot Wallets oder um Freunde und Familie ohne Verlustrisiko an eine eigene Wallet heranzuführen. Siehe [[hd-wallets-und-schluesselableitung]], [[bip-0085]].

**12-Wort-Mnemonics:** Über das erweiterte Setup-Menü der BitBoxApp kann man statt 24 nur 12 Wörter wählen. Praktisch etwa bei Steel-Backups.

**Roll your own seed:** Man erzeugt den Seed selbst mit Würfeln und importiert ihn — Entropie ohne Vertrauen in den Zufallsgenerator des Geräts. Siehe [[diceware-und-seed-generierung]], [[seedphrase-entropie-und-sicherheit]].

**Easy/Instant Backups:** Backup und Wiederherstellung laufen über eine microSD-Karte. Siehe [[wallet-backup-strategien]].

### Datenschutz

**Coin Control:** Manuelle UTXO-Auswahl beim Senden. Siehe [[coin-control-und-utxo-auswahl]].

**Silent Payments:** Die BitBox02 war laut Hersteller die erste Hardware-Wallet, die an Silent-Payment-Adressen senden kann. Eine solche Adresse lässt sich beliebig oft wiederverwenden und erzeugt trotzdem für jede Zahlung eine neue On-Chain-Adresse. Eingeführt mit dem Lugano-Update (10/2024). Siehe [[silent-payments]], [[payment-codes-und-adressaustausch]].

**Hide amounts:** Über „Allow hiding amounts" lassen sich Guthaben in der App per Klick ausblenden.

**Eigener Full Node:** Verbindung zum eigenen Electrum-Node statt zu fremden Servern. Siehe [[electrum-wallet]].

**Multiple accounts:** Mehrere getrennte Konten, etwa um KYC- und Non-KYC-Coins nicht zu vermischen. Siehe [[no-kyc-bitcoin]].

### Sicherheitsarchitektur

**Anti-Klepto:** Protokoll gegen das Ausleiten des privaten Schlüssels über manipulierte Signaturen (Nonce-Kanäle). Kryptografisch beweisbar, dass beim Signieren nichts leakt. Siehe [[anti-klepto-und-supply-chain-sicherheit]].

**Verschlüsselter Seed im RAM:** Der Seed bleibt auch im Arbeitsspeicher verschlüsselt und wird nur kurz entschlüsselt, wenn er gebraucht wird (etwa zum Signieren). Teil des Defense-in-Depth-Ansatzes.

**Firmware-Hash beim Start:** Optional zeigt das Gerät bei jedem Einstecken einen Hash der Firmware an, mit dem sich die Integrität prüfen lässt.

**Reproducible Builds:** Die Open-Source-Firmware lässt sich selbst kompilieren und Bit für Bit mit dem offiziellen Release vergleichen. Von WalletScrutiny geprüft. Siehe [[firmware-verifikation-und-reproduzierbarkeit]].

**Device authenticity check:** BitBoxApp und Drittanbieter-Apps prüfen die Echtheit des Geräts; bei Fehlschlag erscheint eine Warnung. Status einsehbar in den Geräteeinstellungen.

**Verschlüsselte USB-Kommunikation:** Ende-zu-Ende-Verschlüsselung zwischen BitBoxApp und Gerät. Siehe [[hardware-wallet-sicherheitsarchitektur]].

### Transaktionen und Konten

**Taproot:** Seit dem Glärnisch-Update kann die BitBox02 an Taproot-Adressen senden und empfangen. Siehe [[taproot-musig2-frost]], [[bitcoin-adresstypen]].

**Unified accounts:** Die App vereint Adresstypen (wrapped/native SegWit, Taproot) in einem Konto; verschiedene Typen lassen sich in einer Transaktion ausgeben.

**Custom fees:** Feineinstellung der Gebühren statt fester Stufen. Siehe [[transaktionsgebuehren-und-mempool]].

**Payment requests:** Sichere Auszahlung von Börsen durch Verifikation signierter Adressen direkt auf dem Gerät. Siehe [[payment-requests]].

**Automatische Konten-Synchronisation:** Beim Anschluss an ein neues Gerät oder nach einem Backup-Restore scannt die App die ersten fünf Bitcoin- und Litecoin-Konten und zeigt weitere mit Transaktionshistorie an.

### Fortgeschrittene Wallet-Setups

**Miniscript:** Erlaubt komplexere Spending-Bedingungen, aktuell vor allem zeitbasierte Pfade (Recovery-Keys, die erst nach einer Frist ausgeben können). Siehe [[miniscript-und-liana]].

**Secure Multisig:** Mehrere Hardware-Wallets sichern einen Seed. Die BitBox02 adressiert bekannte Schwächen unsicherer Multisig-Umsetzungen. Siehe [[multisig-und-kollaborative-verwahrung]].

### Integrationen und Konnektivität

**WalletConnect:** Offenes Protokoll, um DApps mit der BitBoxApp (Desktop, Android) zu verbinden, ohne Web-Wallet wie Rabby. Siehe [[walletconnect-und-dapps]].

**U2F-Authentifizierung:** Die BitBox02 Multi Edition funktioniert als FIDO-U2F-Authenticator zum Login bei Online-Diensten, auch als Backup zu einem bestehenden Security Key. Siehe [[bitcoin-only-vs-multi-edition]].

**Bitcoin kaufen in der App:** Sats direkt auf die Hardware-Wallet stapeln.

**Verkauf über Pocket Bitcoin:** Beim Verkauf geht der Fiat-Betrag direkt aufs Bankkonto, nach genügend Bestätigungen. Mit SEPA-Instant teils unter 30 Minuten; unter 950 EUR/Tag ohne aufwändige Verifikation. Eingeführt mit dem Livigno-Update (10/2024).

**Android-App:** BitBoxApp für Android, Anbindung der BitBox02 per USB-C.

### Versicherung

**Bitsurance:** Optionaler Schutz der Coins gegen bestimmte Szenarien (Diebstahl, Erpressung, Naturkatastrophen) unter Beibehaltung der Selbstverwahrung. Siehe [[bitcoin-versicherung]].

### Komfort und Darstellung

**Remember wallet (watch-only):** Watch-only-Ansicht der Guthaben, ohne das Gerät jedes Mal anzustecken und zu entsperren.

**Dark Mode:** Dunkle Darstellung der BitBoxApp.

**Satoshi Mode:** Guthaben in Satoshis statt BTC anzeigen.

**In-App-Guides:** Kontextsensitive Hilfe je nach App-Seite.

**Mehrsprachigkeit:** Unter anderem Deutsch, Englisch, Französisch, Italienisch, Spanisch, Portugiesisch, Russisch, Japanisch, Chinesisch, Hebräisch, Hindi, Persisch, Türkisch, Malaiisch, Slowenisch, Bulgarisch.

## Related

- [[bitbox02-nova]] — zweite Gerätegeneration (Bluetooth/Whisper, EAL6+, OLED-Glas)
- [[hardware-wallet-sicherheitsarchitektur]] — Dual-Chip, Secure Chip, Display-Verifikation
- [[bitcoin-only-vs-multi-edition]] — Bitcoin-only- vs. Multi-Edition (U2F, Altcoins)
- [[firmware-verifikation-und-reproduzierbarkeit]], [[anti-klepto-und-supply-chain-sicherheit]] — Sicherheitsdetails
- [[coin-control-und-utxo-auswahl]], [[silent-payments]] — Datenschutz-Features im Detail

## Open Questions

- Herstellerquelle ohne Datumsstempel: Der Feature-Stand entspricht etwa Ende 2024 (letzte referenzierte Updates: Lugano/Livigno 10/2024). Einzelne Features können inzwischen verändert oder erweitert sein.
- „Erste/einzige Hardware-Wallet"-Aussagen (Silent Payments, Anti-Klepto) stammen aus Marketing und wären gegen unabhängige Quellen zu prüfen.
