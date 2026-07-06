# Können Bitcoin gefälscht werden?

**Frage:** Können Bitcoin gefälscht werden? Kann man gefälschte Bitcoin bekommen?

**Datum:** 2026-06-20
**Quellen:** [[bitcoin-whitepaper]], [[bitcoin-transaktionsstruktur]], [[elliptische-kurven-kryptographie]], [[bitcoin-netzwerk-und-nodes]], [[bitcoin-mining-und-proof-of-work]], [[bitcoin-blockchain-struktur]]

---

## Kurze Antwort

Nein. Ein Bitcoin kann technisch nicht gefälscht werden. Jede Transaktion ist kryptografisch signiert und wird von tausenden unabhängigen Nodes gegen identische Regeln geprüft. Eine gefälschte Transaktion — ohne gültige Signatur des Besitzers — wird von jedem Node sofort abgelehnt und nie in die Blockchain aufgenommen.

---

## Warum Fälschung unmöglich ist

### 1. Das UTXO-Modell

Bitcoin funktioniert nicht wie Kontostände, sondern wie nummerierte Geldscheine. Jeder Bitcoin ist ein unverbrauchter Transaktionsoutput (UTXO) — ein konkreter Eintrag in der Blockchain, der genau festhält: wie viel, an welche Adresse, aus welcher Vorgeschichte.

Um einen UTXO ausgeben zu können, muss der Sender eine gültige kryptografische Signatur vorlegen, die beweist, dass er den zugehörigen Private Key besitzt. Wer den Key nicht hat, kann nicht signieren — und ohne gültige Signatur lehnt jeder Node die Transaktion ab. [[bitcoin-transaktionsstruktur]]

### 2. Kryptografische Signaturen (ECDSA / Schnorr)

Bitcoin nutzt elliptische Kurven-Kryptographie (secp256k1). Eine Signatur ist mathematisch an Transaktion und Private Key gebunden:

- Wer den Private Key nicht kennt, kann keine gültige Signatur erzeugen.
- Wer eine gültige Signatur sieht, kann daraus den Private Key nicht rückrechnen.
- Eine Signatur gilt nur für genau diese Transaktion — sie kann nicht auf eine andere übertragen werden.

Die einzige Ausnahme wäre, wenn jemand denselben Private Key benutzt oder die Signatur-Nonce wiederholt (das hat historisch zu Diebstählen geführt, nicht zu Fälschungen). Kein Node akzeptiert eine Transaktion mit gefälschter oder fehlender Signatur. [[elliptische-kurven-kryptographie]]

### 3. Dezentrale Verifikation durch alle Nodes

Das Netzwerk besteht aus tausenden unabhängigen Full Nodes, die jede Transaktion und jeden Block gegen exakt dieselben Konsensregeln prüfen:

- Kommt der Input aus einem real existierenden, noch nicht ausgegebenen UTXO?
- Stimmt die Signatur?
- Überschreitet der Output-Betrag nicht den Input-Betrag?

Kein einzelner Akteur entscheidet. Jede Node entscheidet unabhängig — und ungültige Transaktionen werden schlicht nicht weitergeleitet. [[bitcoin-netzwerk-und-nodes]]

### 4. Die Blockchain als manipulationssichere Geschichte

Jeder Block enthält den Hash seines Vorgängers. Wer einen alten Block nachträglich ändert — um eine Transaktion zu fälschen oder rückgängig zu machen — muss diesen Block und alle Nachfolgeblöcke neu berechnen, während das gesamte Netzwerk gleichzeitig weitermacht. Das ist prohibitiv teuer. [[bitcoin-blockchain-struktur]]

---

## Das einzige reale Szenario: Double-Spend via 51%-Angriff

Das Äquivalent zur «Fälschung» in der digitalen Welt ist der **Double-Spend**: dieselben Bitcoin zweimal ausgeben. Satoshi Nakamoto baute Bitcoin explizit als Lösung für dieses Problem — es war die zentrale Innovation des Whitepapers.

Ein Angreifer könnte theoretisch:

1. Mehr als 50% der gesamten Mining-Hashrate kontrollieren
2. Heimlich eine alternative Chain berechnen, in der eine Zahlung nicht existiert
3. Diese Chain veröffentlichen und so eine bereits erhaltene Zahlung rückgängig machen

In der Praxis ist das für Bitcoin bei aktueller Hashrate ökonomisch selbstzerstörerisch: Der Angriff würde das Vertrauen in Bitcoin zerstören und den Wert der eigenen Mining-Hardware plus Coins des Angreifers vernichten. Außerdem: 6 Bestätigungen abzuwarten (ca. 1 Stunde) macht einen erfolgreichen Double-Spend exponentiell teurer. [[bitcoin-mining-und-proof-of-work]]

---

## Kann man «gefälschte Bitcoin» bekommen?

Technisch nein. Aber es gibt Szenarien, in denen man glaubt, Bitcoin zu bekommen, es aber nicht tut:

**Betrug mit Custodians (häufigster Fall)**
Wer Bitcoin auf einer Börse oder einem Zahlungsdienst hält, hält oft nur eine Forderung gegen den Anbieter — keine echten Bitcoin auf der Blockchain. Wenn der Anbieter insolvent wird oder betrügt (Mt. Gox, FTX), sind diese «Bitcoin» weg. Das sind keine gefälschten Bitcoin — es gab sie als eigenständige UTXOs nie. Lösung: Selbstverwahrung in einer eigenen Wallet.

**Zero-Confirmation-Betrug (für grosse Beträge)**
Eine Transaktion, die noch nicht in einem Block bestätigt ist, kann theoretisch ersetzt werden (RBF). Wer eine Ware gegen eine unbestätigte Transaktion herausgibt, riskiert, dass der Sender die Transaktion zurückzieht. Für kleine Beträge ist das tolerierbar; für grössere gilt: auf Bestätigungen warten.

**Altcoins als «Bitcoin» verkauft**
Jemand könnte versuchen, Litecoin, Bitcoin Cash oder einen anderen Coin als «echten Bitcoin» zu verkaufen. Das ist kein technisches Problem, sondern Betrug. Wer die eigene Wallet-Adresse kontrolliert und Transaktionen auf einer Bitcoin-Node prüft, sieht sofort, ob es sich um BTC handelt.

**Wrapped Bitcoin / Paper Bitcoin**
Tokenisierte Bitcoin auf anderen Blockchains (wBTC auf Ethereum) sind Derivate mit Gegenparteirisiko — kein Bitcoin-Konsens sichert sie ab.

---

## Fazit

Bitcoin kann nicht gefälscht werden. Die Kombination aus UTXO-Modell, kryptografischen Signaturen, dezentraler Verifikation und Proof-of-Work macht eine technische Fälschung praktisch unmöglich. Das Risiko liegt nicht in der Technologie, sondern in der Verwahrung: Wer echte Bitcoin in eigener Custody hält und Transaktionen mit Bestätigungen abwartet, ist gegen alle bekannten Angriffe geschützt.
