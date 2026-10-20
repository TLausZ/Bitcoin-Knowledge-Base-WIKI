# Anti-Klepto und Supply-Chain-Sicherheit

**Status:** established
**Themen:** protokoll, self-custody, kritik
**Last updated:** 2026-10-20
**Sources:** [[Millionenbetrug mit manipulierten Ledger-Wallets! Versteckte Spionage-Chips stehlen Recovery Seeds]], [[Manipulierte Krypto-Wallets_ MediaMarkt zieht Ledger-Geräte aus dem Verkauf zurück]], [[20230713_anti-klepto-wie-die-bitbox02-versteckte-seed-extraktion-verhindert]], [[20230810_verteidigung-in-der-tiefe-seed-verschlüsselung-im-arbeitsspeicher]], [[20230629_bitbox-06-2023-bellinzona-update-de]], [[20221130_hardware-wallets-seed-stehlen-de]], [[20221222_supply-chain-angriffe-verhindern-de]]

## Summary

Das Anti-Klepto-Protokoll schützt gegen einen der heimtückischsten Angriffe auf Hardware-Wallets: Die Extraktion des Wallet-Seeds über manipulierte Signaturen. Eine böswillige Hardware-Wallet kann Teile des Seeds in den Nonces von Signaturen verstecken — unsichtbar auf der Blockchain, für den Angreifer aber lesbar. Die BitBox02 war die erste Hardware-Wallet, die diesen Angriff durch das Anti-Klepto-Protokoll verhindert. Ergänzt wird dies durch die Seed-Verschlüsselung im RAM als weitere Sicherheitsebene. Der Ledger-Vorfall vom Oktober 2026 zeigt den anderen Angriffspfad: Spionage-Hardware in der Lieferkette, die den Seed beim Anzeigen auf dem Display abgreift, ohne den Secure Chip anzutasten.

## Body

### Der Nonce Covert Channel Angriff

Teil jeder digitalen Bitcoin-Signatur ist eine **Nonce** — eine geheime Zahl, die frei gewählt werden kann. Eine böswillige Hardware-Wallet könnte Teile des Wallet-Seeds in diesen Nonces verstecken.

Da alle Signaturen öffentlich in der Blockchain gespeichert werden, kann der Angreifer (z.B. der Hersteller einer kompromittierten Firmware) diese Daten auslesen, die privaten Schlüssel rekonstruieren und alle Coins stehlen.

**Besonders heimtückisch:** Dieser Angriff funktioniert unabhängig davon, ob der Computer des Nutzers kompromittiert ist. Selbst mit Air-Gap und sorgfältiger Transaktionsverifikation bleibt man ohne Schutz verwundbar.

Das Ausmass ist kleiner als oft angenommen: Das **Dark Skippy**-Paper zeigte, dass nur **zwei Signaturen** genügen, um eine komplette 12-Wörter-Seedphrase zu leaken, und **vier Signaturen** für 24 Wörter. Jede Transaktion, die eine Signatur erzeugt, ist also ein potenzieller Datenpunkt für einen böswilligen Hersteller.

### Das Anti-Klepto-Protokoll

Die Lösung: Die Host-Wallet (BitBoxApp) zwingt die Hardware-Wallet, eine **zufällige Nonce des Hosts** in die finale Signatur einzubeziehen.

**Protokoll:**
1. Hardware-Wallet sendet `deviceNoncePublicKey = deviceNonce × G` — legt sich damit auf ihre Nonce fest
2. Host-Wallet wählt `hostNonce` und sendet es an die Hardware-Wallet
3. Hardware-Wallet berechnet: `nonce = deviceNonce + hostNonce`
4. Host-Wallet verifiziert via Distributivgesetz: `nonce×G = deviceNoncePublicKey + hostNonce×G`

Wenn die Verifikation fehlschlägt, bricht die Host-Wallet ab. Eine böswillige Hardware-Wallet kann die Nonce nicht frei manipulieren, ohne entdeckt zu werden.

**Implementierung:** In der BitBox02 seit Monte Rosa Update (Januar 2021), entwickelt von benma in Zusammenarbeit mit Jonas Nick und Andrew Toth als Teil der secp256k1-zkp-Bibliothek.

### Seed-Verschlüsselung im RAM (Defense in Depth)

Als komplementäre Massnahme (eingeführt im Bellinzona-Update, August 2023) bleibt der Seed im RAM der BitBox02 verschlüsselt, auch wenn das Gerät entsperrt ist:

1. Nach dem Entsperren wird ein temporärer Zufallsschlüssel erzeugt und durch den Secure Chip gestreckt
2. Der Seed wird mit diesem Schlüssel re-verschlüsselt
3. Wenn eine Signatur benötigt wird, wird der Seed kurz entschlüsselt, dann sofort wieder verschlüsselt
4. Beim Herausziehen des Geräts wird der temporäre Schlüssel gelöscht

Ein Angreifer, der den RAM ausliest (braucht physischen Zugang zu einem eingesteckten, entsperrten Gerät), erhält nur den verschlüsselten Seed — nicht den Klartext.

### Supply-Chain-Attestation: Echtheit des Geräts beweisen

Ein anderes Angriffsszenario: Was, wenn das Gerät schon vor der Ankunft beim Nutzer manipuliert wurde — durch einen Angreifer in der Lieferkette oder durch kurzzeitigen physischen Zugang (**Evil-Maid-Angriff**)?

Die BitBox02 löst das durch einen **Challenge-Response-Mechanismus**:

1. Die BitBoxApp schickt eine Zufallszahl (Challenge) an das Gerät.
2. Das Gerät signiert sie mit einem **Attestation-Schlüssel** — einem privaten Schlüssel, der bei der Herstellung in den Chip gebrannt wird und das Gerät nie verlässt.
3. Die BitBoxApp prüft die Signatur anhand des Root-Zertifikats von Shift Crypto.

Nur ein echtes Gerät kann die Signatur korrekt erzeugen. Schlägt die Prüfung fehl, zeigt die BitBoxApp eine grosse rote Warnung.

**Einschränkung:** Attestation beweist, dass das Gerät ursprünglich von Shift Crypto hergestellt wurde — nicht, dass es danach nicht manipuliert wurde. Ein Evil-Maid-Angriff, der nur die Host-Software (nicht das Gerät) kompromittiert, wird davon nicht abgedeckt.

**Wichtige Warnung:** Kein echtes Hardware-Wallet bittet jemals darum, den Seed am Computer einzugeben. Eine solche Aufforderung ist ein sicheres Zeichen für ein gefälschtes oder kompromittiertes Gerät.

### Der Ledger-Lieferkettenangriff vom Oktober 2026

Am 9. Oktober 2026 warnte Ledger vor Geräten des südostasiatischen Händlers CryptoBilis (Malaysia, Indonesien, Philippinen), der als autorisierter Reseller geführt war. Kunden berichteten von leergeräumten Wallets; Blockchain-Analysten bezifferten die Verluste auf 72 bis 86 Millionen US-Dollar, Alex Thorn (Galaxy Research) zählte am 9. Oktober rund 91 Millionen US-Dollar, davon allein 213,42 BTC (etwa 17,7 Millionen US-Dollar) auf drei Sammeladressen. Ledger riet Käufern der letzten 90 Tage, nicht eingerichtete Geräte nicht zu verwenden und bestehende Bestände auf eine neue Wallet mit frisch erzeugtem Seed zu übertragen. [[Millionenbetrug mit manipulierten Ledger-Wallets! Versteckte Spionage-Chips stehlen Recovery Seeds]]

Die Methode untersuchten Mark Karpelès (früher Mt. Gox) und die Forscher von Tibane Labs an zwei manipulierten Ledger Nano X. Der Secure Chip blieb unangetastet. Die Angreifer nutzten, dass der Seed bei der Einrichtung einmal auf dem Display erscheinen muss und das Gerät sein Display über eine SPI-Schnittstelle ansteuert. Ein zusätzlich eingebauter Chip liest die Signale auf dieser Leitung mit, rekonstruiert daraus die 24 Wörter und sendet sie über ein Mobilfunkmodem mit SIM oder eSIM an die Täter. Der Nutzer muss dafür weder einen kompromittierten Computer anschliessen noch auf Phishing hereinfallen; eine korrekte Einrichtung mit Ablesen vom Display genügt. Ob genau dieser Umbau hinter den CryptoBilis-Verlusten steckt, war am 11. Oktober noch offen; die untersuchten Geräte stammten nicht direkt von CryptoBilis, eines war aus Malaysia verschickt worden. Brisant ist der Hintergrund des Händlers: Die Gründer übergaben das Unternehmen im März 2026, seit 3. August 2026 steht eine Einzelperson mit Adresse in der chinesischen Provinz Heilongjiang als alleiniger Anteilseigner im Register. Ein Nachweis, dass die Übernahme dem Angriff diente, fehlt. [[Millionenbetrug mit manipulierten Ledger-Wallets! Versteckte Spionage-Chips stehlen Recovery Seeds]]

Kurz nach Karpelès' Post wurden Gelder von manipulierten Geräten abgezogen, was darauf hindeutet, dass die Täter eigentlich auf mehr eingerichtete Geräte warten wollten. Am 11. und 12. Oktober meldete ein deutscher Nutzer zwei bei verschiedenen MediaMarkt-Filialen gekaufte Ledger mit identischem Umbau (zusätzliche Kabel, LTE-Modul), das zweite nachweislich kein Rückläufer und mit gefilmtem Unboxing. MediaMarktSaturn nahm daraufhin alle Ledger-Produkte aus den über 1'000 Filialen in elf Ländern und dem Onlinehandel. Ledger erklärte am 13. Oktober, keinen Abfluss von einem ausserhalb CryptoBilis erworbenen Gerät verifiziert zu haben, untersuche aber weitere Fälle; auch ein autorisierter Reseller am Flughafen Singapur soll im Sommer 2026 mindestens ein manipuliertes Gerät verkauft haben. Der Fall stellt die Regel «nur direkt beim Hersteller kaufen» auf eine neue Grundlage: Betroffen waren ausgerechnet autorisierte Händler, also Ledgers eigene Vertriebskontrolle. [[Manipulierte Krypto-Wallets_ MediaMarkt zieht Ledger-Geräte aus dem Verkauf zurück]]

Für die Architektur-Diskussion folgt daraus: Ein Secure Chip und ein Air-Gap schützen nicht gegen Hardware, die zwischen Chip und Display sitzt. Zach Herbert (Foundation Devices) fordert deshalb physische Manipulationserkennung als eigenes Kriterium neben der Firmware-Verifikation. Multisig mit unabhängig gesicherten Schlüsseln ([[multisig-und-kollaborative-verwahrung]]) entwertet einen einzelnen abgegriffenen Seed. Die BitBox02 begegnet dem Umbau mit Epoxidharz über Mikrocontroller und Secure Chip und mit Sollbruch-Pins im verklebten Gehäuse, die beim Öffnen abbrechen; Blocktrainer, selbst BitBox-Affiliate, nennt diese Massnahmen als Erschwernis, nicht als Ausschluss. Der Eigenbau nach [[specter-diy]] verlagert das Vertrauen von der Lieferkette auf die Einzelbauteile. Die Attestation oben beweist in diesem Szenario nur, dass der Chip echt ist; den angelöteten Mithörer sieht sie nicht. [[Millionenbetrug mit manipulierten Ledger-Wallets! Versteckte Spionage-Chips stehlen Recovery Seeds]]

### Warum mehrere Schichten?

Beide Mechanismen sind Beispiele für **Defense in Depth**: Kein einzelner Angriff reicht aus, um das System zu kompromittieren. Anti-Klepto schützt gegen Software-Kompromittierung der Hardware-Wallet; RAM-Verschlüsselung schützt gegen physische Angriffe auf entsperrte Geräte.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[payment-requests]]
- [[phishing-und-angriffsmethoden]]
- [[hardware-wallet-angriffsvektoren]]
- [[airgap-und-kommunikationskanaele]]
- [[digitale-signaturen-ecdsa]]
- [[firmware-verifikation-und-reproduzierbarkeit]]
- [[pgp-und-verschluesselungspolitik]]
- [[specter-diy]]
- [[hardware-wallet-einstieg]]
- [[multisig-und-kollaborative-verwahrung]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Werden andere Hardware-Wallet-Hersteller Anti-Klepto implementieren?
- Ledger-Aufklärung: An welcher Stelle der Lieferkette wurden die Geräte umgebaut, folgt ein Rückruf in Europa, und bestätigt sich der SPI-Mithörer als Ursache der CryptoBilis-Verluste? (Stand: 13. Oktober 2026 offen)
- Welche Hersteller bieten nachprüfbare Manipulationserkennung am Gehäuse, und wie gut hält sie einem geübten Umbau stand?
