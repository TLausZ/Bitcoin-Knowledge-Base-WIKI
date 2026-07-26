# Specter Desktop

**Status:** established
**Themen:** protokoll, self-custody, privacy, wallets
**Last updated:** 2026-07-25
**Sources:** [[specter-desktop-introduction]], [[specter-desktop-faq]], [[specter-desktop-installation]], [[specter-desktop-device-creation]], [[specter-desktop-wallet-creation]], [[specter-desktop-multisig-guide]], [[specter-desktop-tor]], [[specter-desktop-connect-node]], [[specter-desktop-hwibridge]], [[specter-desktop-ssl]], [[specter-desktop-daemon]]

## Summary

Specter Desktop ist eine Watch-only-Koordinationssoftware für Bitcoin, entwickelt von CryptoAdvance (heute Specter Association) mit dem Ziel, Multisig-Setups mit airgapped Hardware-Wallets alltagstauglich zu machen. Es hält keine privaten Schlüssel: Signiert wird immer auf dem Hardware-Wallet, Specter baut nur die unsignierte Transaktion (PSBT) und verfolgt Adressen und UTXOs über ein eigenes Backend. Als Backend dient ein Bitcoin-Core-Node oder ein Electrum-Server, womit die eigene Verifikation und die Privatsphäre beim Nutzer bleiben. Der Name spielt auf Timothy Mays «Crypto Anarchist Manifesto» an («A specter is haunting the modern world»). Specter Desktop ist das Companion-Gegenstück zur DIY-Hardware-Wallet [[specter-diy]], funktioniert aber mit allen gängigen Signiergeräten.

## Body

### Zweck und Einordnung

Bitcoin Core kann über PSBT und die [HWI](https://github.com/bitcoin-core/HWI) mit Hardware-Wallets arbeiten und Multisig aufsetzen, aber nur über die Kommandozeile. Specter Desktop legt eine grafische Oberfläche darüber, mit Schwerpunkt auf Multisig und airgapped Signieren. Das Gerät speichert die Schlüssel, Specter koordiniert. Diese Rollenteilung ist der Kern: Specter ist watch-only und mit Multisig in Electrum kompatibel, sodass bei einem Fehler in Specter immer ein Fallback bleibt. Aus demselben Grund verwendet es Standard-Descriptors und -Derivationspfade.

Unterstützt werden alle grösseren Hardware-Wallets, darunter BitBox02, ColdCard, Blockstream Jade, SeedSigner, Passport, Keystone, Trezor, Ledger und KeepKey sowie [[specter-diy]] selbst. Bitcoin Core lässt sich experimentell als Hot Wallet nutzen (importierte oder generierte BIP39-Mnemonic), was die Entwickler aber nicht empfehlen.

### Backend: Node oder Electrum

Seit Version 2.0 ist kein Bitcoin-Core-Node mehr zwingend. Specter spricht wahlweise einen Core-Node (via RPC) oder einen Electrum-Server an. Öffentliche Electrum-Server sind möglich, für die Privatsphäre wird aber der eigene Node oder ein selbst gehosteter Electrum-Server empfohlen — sonst sieht der fremde Server alle Adressen der Wallet. Anders als vor 2.0 verwaltet Specter den Node nicht mehr selbst.

Für die RPC-Verbindung zieht Specter `rpcuser` und `rpcpassword` aus der `bitcoin.conf` oder aus den App-Einstellungen. Bei bitcoin-qt (GUI) muss `server=1` gesetzt sein, damit fremde Programme den RPC-Server ansprechen dürfen; bei `bitcoind` ist das automatisch aktiv. Wallet-Funktionalität muss eingeschaltet sein (`disablewallet=0`), ein `txindex=1` ist dagegen nicht nötig. Laufen Node und Specter auf getrennten Maschinen, braucht Core passende `rpcbind`- und `rpcallowip`-Regeln; eine offene `0.0.0.0/0`-Regel taugt nur zum Testen und wird danach auf das konkrete Subnetz eingeschränkt. Der HTTP-Zugang liegt standardmässig auf `http://127.0.0.1:25441/`.

### Installation

Es gibt sechs Wege, gestaffelt nach technischem Anspruch:

- **OS-Binary** von der [GitHub-Release-Seite](https://github.com/cryptoadvance/specter-desktop/releases) — installiert sich wie eine normale Desktop-App, erkennt Core automatisch, Updates aber manuell.
- **pip** (`pip3 install cryptoadvance.specter`) — für Python-Nutzer, verlangt Python 3.9–3.10.
- **Docker** — isolierte, reproduzierbare Umgebung, setzt Docker-Kenntnisse voraus.
- **Paketmanager** (Homebrew) — automatische Updates, nur macOS/Linux, hinkt der neuesten Version teils hinterher.
- **Node-in-a-Box** — als fertige App in Raspiblitz, Umbrel, Citadel, Start9 und myNode (Premium).
- **Aus dem Quellcode** — volle Kontrolle für Beitragende, aufwendig.

Das Binary lässt sich über SHA256SUMS und die GPG-signierte `SHA256SUMS.asc` verifizieren. Wer über Raspiblitz, Umbrel und Co. geht, bekommt Specter meist direkt aus dem jeweiligen App-Menü.

### Geräte und Wallets

Der Ablauf trennt Geräte von Wallets: Ein Gerät speichert Schlüssel, dieselben Schlüssel lassen sich in mehreren Wallets kombinieren (Single-Sig oder Multisig, verschachteltes oder natives SegWit). Einzige Bedingung im Multisig: Alle Cosigner müssen unterschiedliche Geräte sein. Der xpub-Import läuft je nach Gerät über USB (via HWI), QR-Code oder SD-Karte.

Die Derivationspfade bestimmen, welche Adressen aus einem Seed entstehen; ein falscher Pfad erzeugt in Specter andere Adressen als auf dem Gerät. Specter nutzt BIP 44 (`m/44'/0'/0'`) für klassisches Multisig und BIP 49 oder BIP 84 (`m/84'/0'/0'`) für SegWit-Single-Sig; natives SegWit-Multisig läuft über `m/48h/1h/0h/2h`. Wer eine Wallet aus anderer Software importiert, gleicht den Pfad idealerweise über [walletsrecovery.org](https://walletsrecovery.org/) ab.

Beim Single-Sig gilt: verlorener Seed heisst verlorenes Geld, deshalb empfiehlt Specter Stahl-Backups. Der Backup-PDF von Specter enthält nur Master-Public-Keys und Fingerprints, nicht den Seed — er erlaubt aber, die Watch-only-Wallet und damit den Kontostand nachzubauen, und gehört darum vertraulich zu jedem Seed-Backup.

### Multisig in vier Schritten

Der empfohlene Weg zu einer 2-von-3-Multisig-Wallet:

1. **Seed-Erzeugung.** Drei Seeds auf drei Signiergeräten, idealerweise von drei verschiedenen Herstellern (gegen Lieferketten- und RNG-Risiko). Alle drei auf Stahl sichern, je Standort höchstens ein Seed. Minimum sind drei sichere Orte mit Gerät plus Stahl-Backup; ideal sind getrennte Orte für Backups und Geräte, weil die PIN-geschützten Geräte weniger Schutz brauchen als die ungeschützten Stahlplatten.
2. **Wallet-Erstellung in Specter.** Jedes Gerät liefert einen xpub und einen BIP32-Root-Fingerprint. Specter baut daraus die Watch-only-Wallet. Die Sammlung aller Master-Public-Keys und Fingerprints (der «Printable PDF backup») muss jedes Seed-Backup begleiten.
3. **Registrierung auf den Geräten.** Die Wallet-Datei aus Specter (Settings → Export) wird auf jedes Gerät importiert, damit es seine Empfangsadressen anzeigen und prüfen kann, dass Change-Outputs zurück in dieselbe Multisig gehen — der Schutz gegen Adress-Substitutions-Angriffe. Nicht jedes Gerät kann das: BitBox02, ColdCard, Keystone/Cobo und Specter DIY registrieren Cosigner-xpubs im Gerät, Ledger und Trezor können das nur eingeschränkt oder gar nicht.
4. **Test des ganzen Setups.** Kleiner Betrag an die Wallet; alle Geräte zurücksetzen und aus den Stahl-Backups wiederherstellen; die Watch-only-Wallet zusätzlich in fremder Software (etwa [[sparrow-wallet]]) aus den frisch exportierten xpubs nachbauen; zum Schluss den kleinen Betrag an eine ganz andere Wallet senden. Erst wenn dieser volle Durchlauf klappt, kommen grössere Beträge dazu.

Zum Backup-Modell gehört eine harte Bedingung: Geht der `~/.specter`-Ordner verloren **und** fehlt gleichzeitig eines der Geräte ohne Backup, sind die Mittel selbst bei einer 1-von-4-Multisig verloren. Die Wiederherstellung braucht immer alle Master-Public-Keys, exportierbar als JSON über die Wallet-Einstellungen.

### Fernzugriff und Betriebsvarianten

Für den Betrieb auf einem entfernten Node gibt es mehrere Bausteine, die sich kombinieren lassen:

- **HWIBridge.** Die HWI erreicht nur USB-Geräte an der Maschine, auf der sie läuft. Sitzt Specter auf einem entfernten Node, macht eine zweite, lokale Specter-Instanz im `--hwibridge`-Modus die USB-Wallets am Laptop für den Remote-Server sichtbar. Steht der Node physisch greifbar (Raspberry Pi zuhause), steckt man das Gerät direkt an — dann braucht es keine Bridge. Airgapped-Geräte (ColdCard per SD, Specter DIY und Keystone per QR) brauchen sie ohnehin nie.
- **Tor.** Zwei Anwendungsfälle: externe Aufrufe über Tor routen (Privatsphäre) oder Specter als `.onion`-Hidden-Service erreichbar machen (Fernzugriff ohne Portfreigabe). In Version 2.0 unterstützt Specter den Hidden Service nicht nativ; dafür dient ein Node-in-a-Box wie Raspiblitz, der Specter standardmässig als Hidden Service anbietet.
- **SSL.** Browser erlauben Kamerazugriff nur über HTTPS. Ohne SSL funktioniert das QR-Scannen nicht, was den Signierfluss für Specter DIY und andere QR-Geräte bricht. Der Schalter `--ssl` erzeugt ein selbstsigniertes Zertifikat automatisch; im lokalen Netz muss dieses Zertifikat im Browser als vertrauenswürdig hinterlegt werden, auf einem VPS nimmt man Let's Encrypt.
- **Daemon.** Unter Linux läuft Specter als systemd-Service (pip- oder Tarball-Variante), optional zusammen mit `bitcoind` als eigenem Service, sodass beide beim Booten starten.

### Grenzen und offene Punkte

Specter unterstützt Coin Control (Send → Advanced → Coin selection), womit sich UTXOs manuell wählen lassen, die Basis für UTXO-bewusstes Ausgeben (siehe [[coin-control-und-utxo-auswahl]]). CoinJoin ist dagegen nicht integriert; es soll erst kommen, wenn CoinJoin-Server und Hardware-Wallets Proof of Ownership (SLIP-0019) unterstützen. Beim Wallet-Export liefert Specter xpubs statt der von SatoshiLabs geprägten zpubs, weil es den Descriptor im Bitcoin-Core-Format ausgibt. Das Standard-Gap-Limit liegt bei 20 Adressen; ältere Wallets brauchen einen höheren Import plus Rescan, was die Sync-Zeit verlängert. Pruned Nodes liefern keine volle Transaktionshistorie. Die App selbst trägt seit je einen Disclaimer, dass sie auf eigenes Risiko genutzt wird.

## Related

- [[specter-diy]]
- [[multisig-und-kollaborative-verwahrung]]
- [[sparrow-wallet]]
- [[coin-control-und-utxo-auswahl]]
- [[bitcoin-netzwerk-und-nodes]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Status der Specter Association und der Weiterentwicklung nach Version 2.0 (die Quellen dokumentieren den Stand um v1.7–2.0, ohne Datum der jüngsten Releases).
- Reifegrad der Miniscript-Unterstützung, die die FAQ als geplante Erweiterung nennt.
