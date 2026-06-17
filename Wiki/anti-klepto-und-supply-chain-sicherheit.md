# Anti-Klepto und Supply-Chain-Sicherheit

**Status:** established
**Last updated:** 2026-06-05
**Sources:** [[20230713_anti-klepto-wie-die-bitbox02-versteckte-seed-extraktion-verhindert]], [[20230810_verteidigung-in-der-tiefe-seed-verschlüsselung-im-arbeitsspeicher]], [[20230629_bitbox-06-2023-bellinzona-update-de]], [[20221130_hardware-wallets-seed-stehlen-de]], [[20221222_supply-chain-angriffe-verhindern-de]]

## Summary

Das Anti-Klepto-Protokoll schützt gegen einen der heimtückischsten Angriffe auf Hardware-Wallets: Die Extraktion des Wallet-Seeds über manipulierte Signaturen. Eine böswillige Hardware-Wallet kann Teile des Seeds in den Nonces von Signaturen verstecken — unsichtbar auf der Blockchain, für den Angreifer aber lesbar. Die BitBox02 war die erste Hardware-Wallet, die diesen Angriff durch das Anti-Klepto-Protokoll verhindert. Ergänzt wird dies durch die Seed-Verschlüsselung im RAM als weitere Sicherheitsebene.

## Body

### Der Nonce Covert Channel Angriff

Teil jeder digitalen Bitcoin-Signatur ist eine **Nonce** — eine geheime Zahl, die frei gewählt werden kann. Eine böswillige Hardware-Wallet könnte Teile des Wallet-Seeds in diesen Nonces verstecken.

Da alle Signaturen öffentlich in der Blockchain gespeichert werden, kann der Angreifer (z.B. der Hersteller einer kompromittierten Firmware) diese Daten auslesen, die privaten Schlüssel rekonstruieren und alle Coins stehlen.

**Besonders heimtückisch:** Dieser Angriff funktioniert unabhängig davon, ob der Computer des Nutzers kompromittiert ist. Selbst mit Air-Gap und sorgfältiger Transaktionsverifikation bleibt man ohne Schutz verwundbar.

Das Ausmaß ist kleiner als oft angenommen: Das **Dark Skippy**-Paper zeigte, dass nur **zwei Signaturen** genügen, um eine komplette 12-Wörter-Seedphrase zu leaken, und **vier Signaturen** für 24 Wörter. Jede Transaktion, die eine Signatur erzeugt, ist also ein potenzieller Datenpunkt für einen böswilligen Hersteller.

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

Als komplementäre Maßnahme (eingeführt im Bellinzona-Update, August 2023) bleibt der Seed im RAM der BitBox02 verschlüsselt, auch wenn das Gerät entsperrt ist:

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

Nur ein echtes Gerät kann die Signatur korrekt erzeugen. Schlägt die Prüfung fehl, zeigt die BitBoxApp eine große rote Warnung.

**Einschränkung:** Attestation beweist, dass das Gerät ursprünglich von Shift Crypto hergestellt wurde — nicht, dass es danach nicht manipuliert wurde. Ein Evil-Maid-Angriff, der nur die Host-Software (nicht das Gerät) kompromittiert, wird davon nicht abgedeckt.

**Wichtige Warnung:** Kein echtes Hardware-Wallet bittet jemals darum, den Seed am Computer einzugeben. Eine solche Aufforderung ist ein sicheres Zeichen für ein gefälschtes oder kompromittiertes Gerät.

### Warum mehrere Schichten?

Beide Mechanismen sind Beispiele für **Defense in Depth**: Kein einzelner Angriff reicht aus, um das System zu kompromittieren. Anti-Klepto schützt gegen Software-Kompromittierung der Hardware-Wallet; RAM-Verschlüsselung schützt gegen physische Angriffe auf entsperrte Geräte.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[payment-requests]]

## Open Questions

- Werden andere Hardware-Wallet-Hersteller Anti-Klepto implementieren?
- Wie entwickeln sich physische Angriffsmethoden auf Hardware-Wallets?
