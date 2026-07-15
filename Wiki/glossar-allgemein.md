# Glossar — Allgemein

**Status:** established
**Themen:** oekonomie, adoption, glossar
**Last updated:** 2026-07-15
**Sources:** [[Glossary - HoS]], [[Glossary – aantonop]], [[glossary-bitcoinbook]], [[Glossary-bitcoindesign]]

## Summary

Nachschlage-Glossar für allgemeine Bitcoin-Begriffe: Geld und Ökonomie, Markt und Adoption, Verwahrung als Praxis, Akteure und Einheiten. Wer die Protokoll-Interna sucht (Transaktionen, Script, Adresstypen), findet sie im [[glossar-bitcoin-technik]]; Lightning-Begriffe stehen im [[glossar-lightning]]. Fachbegriffe behalten ihre englische Bezeichnung, weil sie so gebraucht werden. Begriffe mit eigenem Konzeptartikel sind mit einem Pfeil auf diesen verlinkt.

## Body

### Altcoin

Sammelbegriff für alle Kryptowährungen ausser Bitcoin. Die meisten versuchen, sich über zusätzliche Funktionen zu differenzieren; ein Grossteil der Projekte verschwindet über die Zeit wieder.

### AML (Anti-Money Laundering)

Gesetzliche Vorschriften gegen Geldwäsche. Sie verpflichten Börsen und andere Finanzdienstleister, Herkunft und Identität bei Transaktionen zu prüfen. Eng verwandt mit KYC.

### ATH (All-Time High)

Der höchste Preis, den Bitcoin je erreicht hat. Analog steht ATL (All-Time Low) für den tiefsten.

### Bear Market / Bull Market

Bear Market bezeichnet eine längere Phase fallender Kurse, Bull Market eine Phase steigender Kurse. Die Begriffe stammen aus dem klassischen Börsenjargon.

### Bitcoin (BTC)

Je nach Zusammenhang die Währungseinheit, das Netzwerk oder das Protokoll. Konvention: «Bitcoin» mit grossem B meint System und Netzwerk, «bitcoin» mit kleinem b die Geldeinheit. BTC ist das gängige Kürzel der Einheit.

### Bitcoin-Einheiten

1 Bitcoin (BTC) teilt sich in 100 Millionen Satoshi. Gängige Zwischengrössen sind Millibitcoin (mBTC, ein Tausendstel BTC) und «Bit» (ein Millionstel BTC). Kleinere Beträge werden zunehmend direkt in Sat angegeben.

### Börse (Exchange)

Handelsplattform zum Kaufen und Verkaufen von Bitcoin gegen Fiat oder andere Kryptowährungen. Börsen sind meist custodial — die Bitcoin liegen dort in fremder Verwahrung, bis man sie abhebt. Zu den Risiken siehe [[selbstverwahrung-und-boersenrisiken]].

### Cold Storage vs. Hot Wallet

Cold Storage heisst, die privaten Schlüssel offline zu halten (Hardware Wallet, Papier), fern von jedem mit dem Internet verbundenen Gerät. Eine Hot Wallet ist dauerhaft online und dadurch bequemer, aber angreifbarer. Details: [[hardware-wallet-sicherheitsarchitektur]].

### Corporate Treasury

Die Praxis von Unternehmen, Bitcoin als Reserve in der Firmenbilanz zu halten, statt nur Fiat-Liquidität vorzuhalten.

### Custodial / Non-Custodial

Custodial bedeutet, eine Drittpartei verwahrt die Schlüssel und damit die Bitcoin. Non-Custodial (Selbstverwahrung) bedeutet, man hält die Schlüssel selbst — siehe Self-Custody.

### DCA (Dollar Cost Averaging)

Anlagestrategie, bei der man regelmässig einen festen Betrag investiert, unabhängig vom Kurs. Das glättet den Einstiegspreis über die Zeit und nimmt das Markt-Timing aus der Entscheidung. → [[bitcoin-kaufen-und-dca]]

### Dezentralisierung

Das Prinzip, dass kein einzelner Akteur das Netzwerk kontrolliert. Regeln und Transaktionshistorie werden von tausenden unabhängigen Nodes durchgesetzt, nicht von einer zentralen Stelle.

### Double-Spending

Der Versuch, dieselbe Geldeinheit zweimal auszugeben. Bitcoins zentrale Erfindung ist, dieses Problem ohne vertrauenswürdige Mittelinstanz zu lösen — jede Transaktion wird gegen die Blockchain geprüft.

### ETF (Exchange Traded Fund)

Börsengehandelter Fonds, der den Bitcoin-Preis abbildet. Anleger bekommen Preis-Exposure über ihr Wertpapierdepot, ohne selbst Bitcoin zu verwahren — und ohne eigene Schlüssel.

### Fiat-Geld

Staatlich herausgegebenes Geld ohne Deckung durch ein Gut wie Gold. Sein Wert beruht auf gesetzlicher Anerkennung und dem Vertrauen in den Herausgeber. Beispiele: Franken, Euro, Dollar.

### FOMO (Fear of Missing Out)

Die Angst, eine Kursbewegung zu verpassen, die zu übereiltem Kaufen bei hohen Preisen verleitet.

### FUD (Fear, Uncertainty, Doubt)

Angst, Unsicherheit und Zweifel — meist als Kürzel für negative Nachrichten oder Behauptungen, ob berechtigt oder gezielt gestreut.

### Geldentwertung

Der Verlust der Kaufkraft von Geld über die Zeit, typisch bei laufend ausgeweiteter Geldmenge. Zentrales Motiv hinter Bitcoins festem Angebot. → [[bitcoin-als-inflationsschutz]]

### Halving

Alle rund vier Jahre (exakt alle 210'000 Blöcke) halbiert sich die Bitcoin-Belohnung pro Block. Dieser fest programmierte Schritt drosselt die Neuausgabe bis zur Obergrenze von 21 Millionen. → [[bitcoin-geldpolitik-und-21-millionen-limit]]

### Hardware Wallet

Ein spezialisiertes Gerät, das die privaten Schlüssel isoliert speichert und Transaktionen signiert, ohne die Schlüssel je preiszugeben. → [[hardware-wallet-sicherheitsarchitektur]]

### HODL

Verschreiber von «hold», rückgedeutet als «Hold On for Dear Life». Bezeichnet die Strategie, Bitcoin langfristig zu halten und Kursschwankungen auszusitzen.

### Kalte Progression

Schleichende Steuererhöhung: Bei Inflation rückt das Nominaleinkommen in höhere Steuerstufen, obwohl die reale Kaufkraft nicht gestiegen ist.

### KYC (Know Your Customer)

Identifikationspflicht bei regulierten Anbietern: Börsen müssen Kunden identifizieren und Transaktionen erfassen. Der Gegenpol dazu ist [[no-kyc-bitcoin|No-KYC-Bitcoin]].

### Liquidität

Mass dafür, wie schnell ein Gut ohne grossen Preisabschlag ge- oder verkauft werden kann. Auf Lightning bezeichnet der Begriff die Kapazität in Zahlungskanälen — siehe [[glossar-lightning]].

### Marktkapitalisierung

Gesamtwert aller im Umlauf befindlichen Bitcoin, berechnet als Preis mal Umlaufmenge.

### Mining

Der Prozess, bei dem spezialisierte Rechner unter Energieeinsatz nach einem gültigen Proof of Work suchen, neue Blöcke erzeugen und dafür Bitcoin erhalten. → [[bitcoin-mining-und-proof-of-work]]

### Multisig (Multi-Signatur)

Verwahrform, bei der mehrere Schlüssel nötig sind, um Bitcoin auszugeben (etwa 2 von 3). Kein einzelner kompromittierter Schlüssel genügt für einen Diebstahl. → [[multisig-und-kollaborative-verwahrung]]

### Node (Full Node)

Ein Rechner mit vollständiger Kopie der Blockchain, der jede Transaktion und jeden Block eigenständig gegen die Konsensregeln prüft. → [[bitcoin-netzwerk-und-nodes]]

### Passphrase

Ein optionales, selbst gewähltes Wort zusätzlich zur Seed Phrase («13. bzw. 25. Wort»). Es erzeugt eine völlig andere Wallet und schützt selbst dann, wenn der Seed in falsche Hände gerät. Nicht mit der Seed Phrase verwechseln. → [[optionale-passphrase]]

### Peer-to-Peer (P2P)

Direkte Übertragung zwischen Teilnehmern ohne Mittelsmann. Das Bitcoin-Netzwerk verteilt Transaktionen und Blöcke über gleichberechtigte Knoten.

### Phishing

Betrugsversuch über gefälschte Nachrichten, Websites oder Apps, die zur Herausgabe von Seed, Passwort oder Schlüsseln verleiten sollen.

### Private Key

Die geheime Zahl, die den Zugriff auf Bitcoin an einer Adresse kontrolliert und Transaktionen signiert. Wer sie kennt, kontrolliert die Coins. → [[kryptografische-schlussel-und-adressen]]

### Proof of Work (PoW)

Der Konsensmechanismus von Bitcoin: Miner müssen rechenintensiv eine Zahl finden, die den Netzwerkvorgaben genügt. Der Aufwand sichert die Blockchain gegen nachträgliche Änderung. → [[bitcoin-mining-und-proof-of-work]]

### Public Key

Der aus dem Private Key abgeleitete öffentliche Schlüssel, aus dem sich die Empfangsadresse ergibt. Er darf geteilt werden; aus ihm lässt sich der Private Key nicht zurückrechnen.

### Satoshi (Sat)

Die kleinste Bitcoin-Einheit: 1 BTC = 100'000'000 Satoshi. Benannt nach dem Erfinder.

### Satoshi Nakamoto

Das Pseudonym der bis heute unbekannten Person oder Gruppe, die Bitcoin entworfen und 2009 die erste Version veröffentlicht hat.

### Seed Phrase (Recovery Phrase, Mnemonic)

Eine Folge von meist 12 oder 24 Wörtern aus einer standardisierten Liste, aus der alle Schlüssel einer Wallet abgeleitet werden. Sie ist das vollständige Backup — wer sie hat, hat die Bitcoin.

Die Begriffe **Seed Phrase**, **Recovery Phrase**, **Mnemonic** und **Backup Phrase** meinen dasselbe: die Wörterliste. Streng genommen ist der **Seed** der daraus errechnete binäre Wert, aus dem die Schlüssel entstehen — die Wörter sind nur seine menschenlesbare Kodierung (nach BIP-39). Nicht mit der Passphrase verwechseln, die als optionaler Zusatz obendrauf kommt. → [[wallet-backup-strategien]], [[seedphrase-entropie-und-sicherheit]]

### Self-Custody (Selbstverwahrung)

Die eigenen Bitcoin selbst verwahren, mit eigenen Schlüsseln, ohne Bank oder Börse dazwischen. Kehrseite der Kontrolle ist die volle Eigenverantwortung. → [[selbstverwahrung-und-boersenrisiken]]

### Spread

Die Differenz zwischen Kauf- und Verkaufskurs auf einer Handelsplattform. Ein enger Spread deutet auf hohe Liquidität.

### Stablecoin

Kryptowährung, deren Wert an eine Fiat-Währung gekoppelt ist, meist an den Dollar. Dient als wertstabile Recheneinheit im Kryptohandel; die Deckung hängt vom jeweiligen Herausgeber ab.

### Token vs. Coin

Ein Coin hat eine eigene Blockchain (wie Bitcoin). Ein Token wird bloss auf einer fremden Blockchain ausgegeben und hat keine eigene.

### Volatilität

Mass für die Stärke der Preisschwankungen. Bitcoin ist historisch volatil; die Ausschläge nehmen mit wachsender Marktgrösse tendenziell ab.

### Wallet

Software oder Gerät, das die Schlüssel verwahrt und Transaktionen erstellt und signiert. Der Begriff wird uneinheitlich gebraucht — mal für die App, mal für den einzelnen Schlüsselbund, mal für ein Konto bei einem Anbieter. Wichtig: Eine Wallet «enthält» keine Bitcoin, sondern die Schlüssel dazu.

### Whale

Ein Marktteilnehmer mit sehr grossem Bitcoin-Bestand, dessen Transaktionen den Preis spürbar bewegen können.

## Related

- [[glossar-bitcoin-technik]]
- [[glossar-lightning]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-kaufen-und-dca]]

## Open Questions

Keine offenen Punkte. Neue Einsteigerbegriffe aus künftigen Quellen kommen hier dazu.
