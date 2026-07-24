# Hardware-Wallet-Angriffsvektoren

**Status:** established
**Themen:** self-custody, kritik
**Last updated:** 2026-06-05
**Sources:** [[20230406_die-funf-grossten-schwachstellen-in-hardware-wallets-und-wie-die-bitbox02-sie-behebt]]

## Summary

Hardware-Wallets schützen private Schlüssel vor direktem Zugriff — aber ein kompromittiertes Host-Gerät kann über das Protokoll zwischen App und Wallet angreifen. Fünf klassische Angriffsvektoren wurden im Laufe der Hardware-Wallet-Geschichte entdeckt und behoben: nicht-validierter Change-Output, Passphrase-Eingabe am Hostgerät, manipulierte Multisig-Cosigner, überhöhte Transaktionsgebühr und Isolations-Bypass. Alle fünf sind gelöst, wenn die Wallet die relevanten Daten selbst prüft und auf ihrem eigenen Display anzeigt.

## Body

### Bedrohungsmodell: kompromittiertes Host-Gerät

Hardware-Wallets isolieren private Schlüssel. Sie verhindern, dass der Seed das Gerät verlässt. Was sie nicht verhindern können: ein infizierter Computer oder ein Angreifer mit Zugriff darauf, der die Transaktionsdaten manipuliert, bevor sie zur Wallet gesendet werden. Die Wallet signiert dann etwas anderes als der Nutzer glaubt.

### 1. Nicht-validierter Change-Output

Bitcoin-Transaktionen nutzen das UTXO-Modell: ein UTXO wird vollständig ausgegeben, der Rest geht als Change-Output zurück an den Sender. Frühe Hardware-Wallets zeigten nur den Sendebetrag an, prüften aber nicht, ob der Change-Output auch wirklich an eine eigene Adresse geht. Ein Angreifer konnte den Change-Output auf eine fremde Adresse umleiten — die Wallet zeigte den Sendebetrag korrekt an, der Rest verschwand.

Lösung: Die Wallet prüft, ob der Change-Output zu ihrer eigenen Wallet gehört. Gehört er nicht dazu, wird die Transaktion abgelehnt.

### 2. Passphrase-Eingabe am Hostgerät

BIP-39-Passphrasen sind ein zweiter Faktor. Geräte mit wenigen Tasten (wie frühe Modelle mit zwei Buttons) liessen die Passphrase-Eingabe über das Host-Gerät zu. Das hat zwei Probleme: Das Host-Gerät kennt die Passphrase. Und ein Angreifer kann eine andere Passphrase an die Wallet weiterleiten — die Wallet öffnet eine andere Hidden Wallet, alles scheint normal, bis der Nutzer senden will. Der Angreifer hält das Lösegeld: Gib mir Bitcoin, ich verrate dir die richtige Passphrase.

Lösung: Die BitBox02 hat genug physische Buttons, um die Passphrase direkt am Gerät einzugeben. Das Host-Gerät erfährt die Passphrase nie.

### 3. Manipulierte Multisig-Cosigner

Multisig-Wallets benötigen für jede Adresse die xpubs aller Cosigner. Frühe Implementierungen fragten das Host-Gerät nach den Cosigner-xpubs — ohne sie zu speichern oder zu validieren. Ein Angreifer konnte seine eigenen xpubs einschleusen. Die angezeigte Adresse war technisch gültig, gehörte aber dem Angreifer.

Lösung: Die Wallet speichert die Multisig-Parameter (inkl. aller Cosigner-xpubs) auf dem Gerät selbst. Bei jeder Adressanfrage prüft sie, ob die Cosigner unverändert sind. Veränderte xpubs werden gemeldet.

### 4. Überhöhte Transaktionsgebühr

Das Host-Gerät übermittelt die Transaktionsdaten zur Signatur. Wenn es eine überhöhte Gebühr einschleust (theoretisch bis zum gesamten Wallet-Inhalt), signiert die Wallet brav. Der Angreifer erpresst das Opfer: Zahle mir X, sonst broadcaste ich die Transaktion und du verlierst alles.

Lösung: Die Wallet zeigt die Gebühr auf ihrem eigenen Display an. Übersteigt die Gebühr 10% des Transaktionsbetrags, erscheint eine explizite Warnung.

### 5. Isolations-Bypass

Multi-Asset-Wallets verwalten Währungen mit ähnlichen Adressformaten und Ableitungspfaden. Ein Angreifer kann eine Transaktion als Testnet-Bitcoin ausgeben — der Nutzer signiert Mainnet-Bitcoin. Oder Ethereum statt einer nahezu wertlosen Fork.

Lösung: Unterschiedliche Ableitungspfade pro Währung, Anzeige der Währung auf dem Gerät-Display vor jeder Signatur.

### Warum keine der Schwachstellen ausgenutzt wurde

Obwohl alle fünf Angriffe dokumentiert sind, gibt es keine öffentlichen Berichte über tatsächliche Opfer. Solange die Mehrheit der Bitcoin auf Börsen liegt, ist ein gezielter Angriff auf einzelne Hardware-Wallets ineffizient. Die Angriffe wurden durch Sicherheitsforscher entdeckt und verantwortungsvoll gemeldet.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[phishing-und-angriffsmethoden]]
- [[multisig-und-kollaborative-verwahrung]]
- [[optionale-passphrase]]
- [[utxo-modell-und-konsolidierung]]
- [[bitcoin-seed-cracking]]
- [[specter-diy]]

## Open Questions

- Gibt es neue Angriffsvektoren, die mit Tapscript oder Silent Payments entstehen?
- Wie schützen Hardware-Wallets bei Verwendung externer Signer-Protokolle (z.B. PSBT via QR)?
