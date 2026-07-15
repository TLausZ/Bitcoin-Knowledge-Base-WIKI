# Glossar — Bitcoin-Technik

**Status:** established
**Themen:** protokoll, privacy, mining, glossar
**Last updated:** 2026-07-15
**Sources:** [[glossary-bitcoinbook]], [[Glossary – aantonop]], [[Glossary-bitcoindesign]], [[glossary-lnbook]]

## Summary

Nachschlage-Glossar für die technischen Begriffe des Bitcoin-Protokolls auf der Basisschicht: Transaktionen, Blöcke, Schlüssel und Adressen, Script, Konsens und Mining-Mechanik. Allgemeine und ökonomische Begriffe stehen im [[glossar-allgemein]], Lightning-Begriffe im [[glossar-lightning]]. Fachbegriffe behalten ihre englische Bezeichnung. Wo ein eigener Konzeptartikel existiert, verweist ein Pfeil darauf; dort steht die ausführliche Erklärung.

## Body

### Adresse (Address)

Eine kurze Zeichenfolge, die einem Absender sagt, unter welchen Bedingungen er Bitcoin an einen Empfänger sperren soll. Technisch kodiert sie ein Locking-Script, meist den Hash eines öffentlichen Schlüssels. → [[bitcoin-adresstypen]]

### Adressformate (P2PKH, P2SH, P2WPKH, P2WSH, P2TR)

Die historisch aufeinanderfolgenden Adresstypen. Legacy (P2PKH, beginnt mit 1) sperrt auf einen Public-Key-Hash; P2SH (beginnt mit 3) auf einen Script-Hash; Native SegWit (P2WPKH/P2WSH, «bc1q») legt die Signaturdaten in den Witness; Taproot (P2TR, «bc1p») fasst Signatur und komplexe Bedingungen effizient und privat zusammen. Alle sind untereinander zahlungskompatibel. → [[bitcoin-adresstypen]]

### Base58Check

Ältere Kodierung für Adressen und Schlüssel, die verwechselbare Zeichen (0, O, l, I) weglässt und eine Prüfsumme gegen Tippfehler enthält. Legacy- und P2SH-Adressen nutzen sie.

### Bech32 / Bech32m

Kodierung für SegWit-Adressen, ganz in Klein- oder Grossbuchstaben, mit starker Fehlererkennung. Bech32 kodiert SegWit v0 (P2WPKH/P2WSH), das verbesserte Bech32m die Taproot-Ausgaben (v1). Beide erzeugen die «bc1»-Adressen.

### Block

Ein Datenpaket aus Transaktionen mit einem Header, das auf den Vorgängerblock verweist. Rund alle zehn Minuten kommt ein neuer Block hinzu; einmal tief genug in der Kette gilt sein Inhalt praktisch als unumkehrbar. → [[bitcoin-blockchain-struktur]]

### Block Header

Der 80 Byte kleine Kopf eines Blocks: Version, Hash des Vorgängers, Merkle Root, Zeitstempel, Schwierigkeitsziel und Nonce. Sein Hash ist der Proof of Work. → [[bitcoin-block-header]]

### Blockchain

Die fortlaufende, von jedem Full Node geprüfte Kette validierter Blöcke, jeder verankert im vorherigen bis zurück zum Genesis-Block. → [[bitcoin-blockchain-struktur]]

### Block Reward / Block Subsidy

Die neu erzeugten Bitcoin, die ein Miner für einen gültigen Block erhält, ausgezahlt in der Coinbase-Transaktion. Das Subsidy halbiert sich alle 210'000 Blöcke (siehe Halving im [[glossar-allgemein]]); dazu kommen die Transaktionsgebühren des Blocks.

### Byzantine Generals Problem

Das Grundproblem verteilter Systeme, sich trotz möglicherweise böswilliger oder ausfallender Teilnehmer auf einen gemeinsamen Zustand zu einigen. Bitcoins Proof of Work ist eine praktische Lösung dafür.

### Coinbase / Coinbase Transaction

Die erste Transaktion jedes Blocks, vom Miner erzeugt. Sie beansprucht Block Subsidy plus Gebühren. Das Coinbase-Feld erlaubt bis zu 100 Byte beliebige Daten. Nicht mit der gleichnamigen Börse verwechseln.

### Coin Control

Das gezielte Auswählen, welche UTXOs eine Transaktion als Eingänge nutzt — für niedrigere Gebühren und bessere Privatsphäre. → [[coin-control-und-utxo-auswahl]]

### Confirmations (Bestätigungen)

Sobald eine Transaktion in einem Block steht, hat sie eine Bestätigung; jeder weitere Block darüber erhöht die Zahl. Ab etwa sechs Bestätigungen gilt eine Umkehr als praktisch ausgeschlossen.

### Consensus / Consensus Rules

Die Regeln, nach denen Full Nodes Blöcke und Transaktionen prüfen. Nur Blöcke, die allen Regeln genügen, werden akzeptiert; so bleiben unabhängige Knoten ohne zentrale Instanz im selben Zustand. → [[konsensregeln-und-mempool-richtlinien]]

### CPFP (Child Pays For Parent)

Methode, um eine festhängende unbestätigte Transaktion zu beschleunigen: Man gibt einen ihrer Ausgänge in einer neuen Transaktion mit hoher Gebühr aus. Der Miner muss beide einschliessen, um die hohe Gebühr zu bekommen. Anders als RBF kann das auch der Empfänger tun.

### Derivation Path (Ableitungspfad)

Die Pfadangabe, nach der eine HD-Wallet einzelne Schlüssel aus dem Seed ableitet (etwa `m/84h/0h/0h/0/0`). Die Standards BIP-44/49/84 legen fest, welcher Pfad zu welchem Adresstyp gehört. → [[hd-wallets-und-schluesselableitung]]

### Difficulty (Schwierigkeit)

Netzwerkweiter Wert, der bestimmt, wie viel Rechenaufwand ein gültiger Proof of Work erfordert. Alle 2016 Blöcke (rund zwei Wochen) wird sie neu justiert, damit Blöcke im Schnitt weiter alle zehn Minuten kommen — unabhängig davon, wie viel Rechenleistung im Netz ist.

### Digitale Signatur

Ein mit dem Private Key erzeugter Nachweis, dass der Inhaber eine Transaktion autorisiert hat und sie nachträglich nicht verändert wurde. Jeder kann sie mit dem passenden Public Key prüfen.

### ECDSA

Das ursprüngliche Signaturverfahren von Bitcoin auf Basis elliptischer Kurven. Es stellt sicher, dass nur der Inhaber des privaten Schlüssels die zugehörigen Bitcoin ausgeben kann. Seit Taproot ergänzt durch Schnorr. → [[elliptische-kurven-kryptographie]]

### Extended Keys (xpub / xpriv)

Der erweiterte öffentliche bzw. private Schlüssel an der Wurzel eines Wallet-Zweigs, aus dem sich alle darunterliegenden Adressen ableiten. Präfixe wie ypub/zpub zeigen an, für welchen Adresstyp der Schlüssel gedacht ist. Ein xpub verrät alle Empfangsadressen — entsprechend heikel für die Privatsphäre.

### Fees (Transaktionsgebühren)

Der Betrag, den ein Absender den Minern fürs Einschliessen zahlt. Er hängt vom Gewicht der Transaktion ab (nicht vom Betrag) und steigt, wenn viele Transaktionen um knappen Blockplatz konkurrieren. → [[transaktionsgebuehren-und-mempool]]

### Fork

Allgemein eine Verzweigung der Blockchain. Ein zufälliger Fork entsteht, wenn zwei Miner fast gleichzeitig einen Block finden; er löst sich mit dem nächsten Block auf. Bewusste Protokolländerungen heissen Soft Fork (verschärfend, abwärtskompatibel) oder Hard Fork (nicht abwärtskompatibel). → [[soft-fork-und-hard-fork]]

### Gap Limit

Wallets beobachten meist nur 20 aufeinanderfolgende ungenutzte Adressen. Zahlungseingänge jenseits dieser Lücke werden übersehen — relevant beim Importieren einer Wallet in eine andere Software.

### Genesis Block

Der allererste Block der Blockchain, fest im Code verankert, der das Netzwerk initialisiert.

### Hash / Hashfunktion

Eine Einwegfunktion, die beliebig grosse Daten auf einen kurzen Fingerabdruck fester Länge abbildet. Aus dem Hash lässt sich die Eingabe nicht zurückrechnen; die kleinste Änderung der Eingabe ändert den ganzen Hash. Grundbaustein von Blockchain und Proof of Work.

### Hashlock

Eine Script-Bedingung, die eine Ausgabe erst freigibt, wenn ein bestimmtes Geheimnis offengelegt wird. Baustein von [[glossar-lightning|HTLCs]].

### HD Wallet / HD Protocol

Hierarchisch-deterministische Wallet (BIP-32): Alle Schlüssel entstehen aus einem einzigen Seed in einer Baumstruktur. Ein Backup des Seeds sichert damit die ganze Wallet. → [[hd-wallets-und-schluesselableitung]]

### IBD (Initial Block Download)

Der erstmalige Download und die vollständige Prüfung der gesamten Blockchain, wenn ein neuer Full Node startet. Kann Stunden bis Tage dauern.

### Locktime / Timelock

Eine Bedingung, die das Ausgeben einer Ausgabe bis zu einem Zeitpunkt oder einer Blockhöhe sperrt. Absolute Timelocks nutzen CLTV (OP_CHECKLOCKTIMEVERIFY), relative Timelocks CSV (OP_CHECKSEQUENCEVERIFY). Zentral für Zahlungskanäle und HTLCs.

### Mempool

Der Zwischenspeicher gültiger, aber noch unbestätigter Transaktionen, aus dem Miner nach Gebühr auswählen. → [[transaktionsgebuehren-und-mempool]]

### Merkle Tree / Merkle Root

Baumstruktur, die alle Transaktionen eines Blocks paarweise hasht, bis ein einziger Hash übrigbleibt — die Merkle Root im Block Header. Sie erlaubt es, die Zugehörigkeit einer Transaktion zu einem Block zu beweisen, ohne den ganzen Block zu laden (Grundlage von SPV).

### Miniscript

Eine strukturierte Schreibweise für bestimmte Bitcoin-Scripts. Sie macht Ausgabebedingungen für Software analysierbar und für Menschen lesbarer. → [[miniscript-und-liana]]

### MuSig

Verfahren, mehrere Schnorr-Signaturen zu einer einzigen zusammenzufassen. Eine Multisig-Ausgabe sieht dann aus wie eine gewöhnliche Einzelsignatur — kleiner, günstiger, privater. → [[taproot-musig2-frost]]

### Nonce / Extra Nonce

Das 32-Bit-Feld im Block Header, das der Miner variiert, um einen Hash unter dem Schwierigkeitsziel zu finden. Weil 4 Milliarden Werte oft nicht reichen, dient zusätzlich Platz in der Coinbase als «Extra Nonce».

### Opcode

Ein Befehl der Script-Sprache, der Daten auf den Stapel legt oder eine Operation ausführt.

### OP_RETURN

Ein Opcode, der eine nachweislich nicht ausgebbare Ausgabe mit beliebigen Daten erzeugt. Full Nodes müssen sie nicht in der UTXO-Datenbank halten.

### Orphan Block / Stale Block

Ein Stale Block wurde gültig gemint, liegt aber nicht in der längsten Kette, weil ein konkurrierender Block auf gleicher Höhe zuerst verlängert wurde. Ein Orphan Block ist einer, dessen Vorgänger der lokale Knoten noch nicht kennt.

### Output / Input

Eine Transaktion verbraucht Inputs (Verweise auf frühere UTXOs) und erzeugt Outputs. Jeder Output trägt einen Betrag und ein Script, das die Bedingungen fürs spätere Ausgeben festlegt. → [[bitcoin-transaktionsstruktur]]

### Output Script Descriptor

Ein kompaktes, standardisiertes Datenstück, das alle Informationen enthält, um eine bestimmte Menge von Adressen oder Schlüsseln zu erzeugen — robuster als eine lange Adressliste beim Backup und Import.

### PSBT (Partially Signed Bitcoin Transaction)

Portables Format für noch unfertige Transaktionen. Es erlaubt, eine Transaktion zwischen mehreren Geräten oder Parteien zu reichen — etwa zwischen Wallet und Hardware Wallet oder unter Multisig-Teilnehmern.

### RBF (Replace-by-Fee)

Regel, die es dem Absender erlaubt, eine unbestätigte Transaktion durch eine höher bebührte zu ersetzen, die dieselben Eingänge ausgibt. Nützlich, wenn eine Transaktion bei steigenden Gebühren hängen bleibt.

### RIPEMD-160

Kryptografische Hashfunktion mit 160 Bit Ausgabe, in Bitcoin für Adress-Hashes eingesetzt (kombiniert mit SHA-256).

### Schnorr-Signatur

Das mit Taproot (2021) eingeführte Signaturverfahren. Es erlaubt, Signaturen zu aggregieren (MuSig), senkt so Gebühren und verbessert die Privatsphäre komplexer Ausgaben. → [[taproot-musig2-frost]]

### Script (Bitcoin Script)

Bitcoins einfache, stapelbasierte Sprache, die die Ausgabebedingungen von Transaktionen beschreibt. Bewusst nicht Turing-vollständig — keine Schleifen. → [[bitcoin-script-und-output-locks]]

### ScriptPubKey / ScriptSig

Das ScriptPubKey (Locking Script) steht im Output und legt die Bedingungen zum Ausgeben fest; das ScriptSig (Unlocking Script) liefert im Input die Daten, die diese Bedingungen erfüllen.

### SegWit (Segregated Witness)

Protokoll-Upgrade von 2017, das die Signaturdaten («Witness») aus dem alten Transaktionsteil auslagert. Das behob die Transaction Malleability und schuf Platz für mehr Transaktionen pro Block. Umgesetzt als Soft Fork. → [[segregated-witness-segwit]]

### SHA-256

Die von Bitcoin verwendete kryptografische Hashfunktion (256 Bit Ausgabe). Proof of Work und Blockverkettung beruhen auf ihr; Adressen nutzen sie doppelt angewandt.

### SPV (Simplified Payment Verification)

Verfahren, mit dem eine leichte Wallet prüft, ob eine Transaktion in einem Block steht, ohne die ganze Blockchain zu laden — nur anhand der Block-Header und eines Merkle-Beweises.

### Taproot

Das Upgrade von 2021, das komplexe (etwa Multisig-) Ausgaben auf der Kette gleich aussehen lässt wie einfache — mehr Effizienz und Privatsphäre. Basiert auf Schnorr. → [[taproot-musig2-frost]]

### Transaktion (Transaction)

Eine signierte Datenstruktur, die Bitcoin von Eingängen auf neue Ausgänge überträgt. Sie wird im Netz verteilt, von Minern in einen Block aufgenommen und damit dauerhaft. → [[bitcoin-transaktionsstruktur]]

### Transaction Malleability

Die frühere Eigenschaft, dass sich der Hash (die ID) einer Transaktion ändern liess, ohne ihren Inhalt zu ändern — etwa durch Manipulation der Signatur. Für Zahlungskanäle ein Problem; von SegWit behoben.

### Turing-Vollständigkeit

Die Eigenschaft einer Sprache, jedes berechenbare Programm ausführen zu können. Bitcoin Script ist bewusst nicht Turing-vollständig, um das Verhalten von Transaktionen vorhersagbar und sicher zu halten.

### UTXO (Unspent Transaction Output)

Ein noch nicht ausgegebener Transaktionsausgang. Das Guthaben einer Wallet ist die Summe ihrer UTXOs; ausgeben heisst, UTXOs als Eingänge zu verbrauchen und neue zu erzeugen. → [[utxo-modell-und-konsolidierung]]

### Watch-only Wallet

Eine Wallet, die nur die öffentlichen Schlüssel (xpub) kennt: Sie sieht Guthaben und Verlauf und kann unsignierte PSBTs erstellen, aber nichts ausgeben.

### WIF (Wallet Import Format)

Austauschformat für einen einzelnen privaten Schlüssel, mit Prüfsumme und einem Flag, ob ein komprimierter Public Key genutzt wird.

## Related

- [[glossar-allgemein]]
- [[glossar-lightning]]
- [[bitcoin-transaktionsstruktur]]
- [[bitcoin-script-und-output-locks]]
- [[bitcoin-adresstypen]]
- [[hd-wallets-und-schluesselableitung]]

## Open Questions

Keine offenen Punkte. Neue Protokollbegriffe (etwa aus künftigen Soft Forks) kommen hier dazu.
