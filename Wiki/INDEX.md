# Bitcoin KB — Wiki Index

Alle Artikel alphabetisch. Stand: 2026-06-20 (nach Compile-Pass 32: neuer Artikel bitcoin-als-inflationsschutz, 98 Artikel total)

| Artikel | Status | Beschreibung |
|---------|--------|-------------|
| [[airgap-und-kommunikationskanaele]] | established | Airgap = Kommunikationskanal-Wahl, kein Sicherheitsvorteil; alle 11 bekannten HW-Wallet-Exploits 2020-2021 wären durch Airgap nicht verhindert worden; "keine Kommunikation" hat echten Wert, "air-gapped communication" nicht |
| [[anti-klepto-und-supply-chain-sicherheit]] | established | Anti-Klepto (Nonce-Schutz gegen Seed-Extraktion); Dark Skippy (2 Signaturen = 12 Wörter); Supply-Chain-Attestation (Challenge-Response); Evil-Maid-Angriff; RAM-Seed-Verschlüsselung |
| [[biometrie-und-finanzueberwachung]] | established | Biometrische Bankdaten: echte vs. behauptete Motive (Betrug vs. Kundenbindung/Überwachung); behavioral Biometrics überlegen; Vietnam/China/Indien/EU-Parallelen; Chilling Effect auf Grundrechte; Bitcoin als identitätsfreie Alternative |
| [[bitcoin-fehlannahmen]] | established | 10 häufige Missverständnisse widerlegt: kein Nutzen, zu langsam, kein innerer Wert, Nullsumme, Verbots-Risiko, zu spät, Umwelt, Quantencomputer, Altcoins, Skalierung |
| [[bitcoin-als-inflationsschutz]] | emerging | Strukturell (21M-Limit, kein Cantillon-Effekt) + empirisch (3%+ BTC schützt konsistent 2018–2024, RDF-Analyse); Gold-Vergleich; kurzfristig schwacher, langfristig konsistenter Schutz; Volatilitätsvorbehalt |
| [[bitcoin-als-strategische-reserve]] | emerging | Bitcoin als Staatsfonds-Asset: El Salvador/Bhutan/USA-Precedenz; Best Practices Custody/Governance; kontrafaktische RDF-Analyse 2018–2024 (3%+ BTC schützt real gegen Inflation); Timing-Risiken |
| [[bitcoin-powerlaw-und-preismodelle]] | established | Power Law (β=5.69, mechanistisch); Angebot-Nachfrage-Modell Rudd & Porter (JRFM 2025): 50% Wahrscheinlichkeit >5,17 Mio. USD bis April 2036; Liquid Supply als Schlüsselhebel |
| [[blocksize-war]] | established | Der Blocksize-Krieg 2015–2017: Big-Blocker vs. Small-Blocker; Bitcoin XT → Classic → Unlimited → BTC1/SegWit2x; UASF, NYA, BIP 91; SegWit-Aktivierung Aug 2017; Bitcoin Cash; Small-Blocker-Sieg Nov 2017 |
| [[bitcoin-mining-umwelt]] | established | Bitcoin Mining und Umwelt: 87,5% peer-reviewed Papers positiv; 4 Mechanismen (Demand Response, Curtailment, Methan, Abwärme); Texas $18Mrd. Einsparung; Finnland District Heating; Cambridge 2025: 52,4% nachhaltige Energie; Wandel von 2021→2025 |
| [[bitcoin-kaufen-und-dca]] | established | Kaufwege (P2P: Hodl Hodl/Bisq/Peach; ATM; OTC); DCA; Direktkauf in Hardware-Wallet (Pocket Bitcoin, Relai); KYC-light; Timing-Paradox; Anfängerfehler |
| [[bitcoin-versicherung]] | emerging | Bitsurance: erste Versicherung für selbst verwahrte Bitcoin; Schutz gegen physische Risiken (Raub, Feuer, Erpressung, Naturkatastrophen); kein Custody-Risiko |
| [[bitcoin-rechtliche-angriffe]] | established | Rechtsstreit als Angriff auf Bitcoin; Craig Wright vs. Hodlonaut (Norwegen, Sieg Oktober 2022); OpenSats Legal Defense Fund; Shift Crypto Spende $10k |
| [[craig-wright-faketoshi]] | established | Craig Wright: Faketoshi-Behauptung 2016, BCH Hash War 2018, juristische Offensive (Hodlonaut/McCormack/Kleiman/Tulip Trading), COPA v. Wright 2024 (Urteil: nicht Satoshi, Dokumente gefälscht) |
| [[fortego-backup-sicherheit]] | established | Double Responsibility Problem (Verlust vs. Diebstahl); Fortego CodeBook-Trennung; absolute Seed-Phrase-Regel; Sicherheitsarchitektur (Protokollierung, Verschlüsselung, Geo-Backup); Vergleich Backup-Ansätze |
| [[firmware-verifikation-und-reproduzierbarkeit]] | established | Reproduzierbare Builds: selber Code → selbe Binärdatei; Docker-Kompilierung; Hash-Vergleich; Community-Bestätigungen |
| [[bitcoin-whitepaper]] | established | Satoshi Nakamotos Original-Whitepaper: Double-Spend-Problem, PoW, UTXO-Modell, SPV, Incentive-Mechanismus |
| [[satoshi-ankuendigung-2009]] | established | Satoshi auf P2P Foundation (2009-02-11): erste öffentliche Ankündigung; "crypto proof instead of trust"; "distributed timestamp server"; Wei Dai kommentiert; Verbindung zur Cypherpunk-Tradition |
| [[bip-329-wallet-labels]] | emerging | BIP-329 Standard für portierbare Wallet-Labels zwischen verschiedenen Softwares |
| [[bip-85-child-keys]] | emerging | Aus einem Backup mehrere unabhängige Wallets ableiten — Hot Wallets, Geschenke, Passwörter |
| [[bitcoin-adresstypen]] | established | Legacy P2PKH (1...), P2SH (3...), Native SegWit P2WPKH (bc1q, ~38% günstiger, Standard), Taproot P2TR (bc1p); alle interoperabel; ein Seed für alle Typen |
| [[bitcoin-blockchain-struktur]] | established | Blockchain als geteilte Datei aller Transaktionen; Block-Header (Version, Previous Block, Merkle Root, Time, Target, Nonce); Sicherheit durch Hash-Verkettung; Kandidatenblock; lokale Speicherpfade und blk*.dat-Format |
| [[bitcoin-netzwerk-und-nodes]] | established | P2P-Netzwerk aus Nodes; drei Jobs (Regeln, Weitergabe, Blockchain speichern); Mempool; offen für alle; Dezentralisierung als Kernmerkmal; eigener Node = kein Vertrauen nötig |
| [[bitcoin-datenformate]] | established | Hexadezimal, Bytes, Little-Endian, Natural vs. Reverse Byte Order (TXIDs/Block-Hashes), CompactSize |
| [[bitcoin-script-und-output-locks]] | established | Stack-Sprache; alle 10 Standard-Script-Typen: P2PK, P2PKH, P2MS, P2SH, OP_RETURN, P2WPKH, P2WSH, P2TR, P2SH-P2WPKH, P2SH-P2WSH; Script-Limits |
| [[elliptische-kurven-kryptographie]] | established | secp256k1 (y²=x³+7); EC-Mathematik (Double/Add/Multiply); ECDSA (Sign/Verify, DER, Nonce-Sicherheit); Schnorr-Signaturen (BIP 340, x-only Keys, Tagged Hashes, Batch-Verify); SHA-256/RIPEMD-160 Hash-Funktionen |
| [[bitcoin-transaktionsstruktur]] | established | Transaktion = Inputs + Outputs + Unlocking Code; Output-System (keine Konten, sondern Geldscheine); Wechselgeld-Output; Coinbase-Transaktion; implizite Gebühr; Mempool → Block |
| [[bitcoin-covenants]] | emerging | CTV und CheckTXHashVerify: Ausgabebedingungen, die auch Zieladressen einschränken; Anwendungen: Vaults, Congestion-Control, Kanal-Fabriken |
| [[bitcoin-geldpolitik-und-21-millionen-limit]] | established | Wie das 21-Mio-Limit durch Code und dezentrale Nodes durchgesetzt wird |
| [[bitcoin-mining-und-proof-of-work]] | established | Mining als Würfelspiel mit SHA-256-Hashfunktionen; Proof of Work als Sicherheitsmechanismus |
| [[bitcoin-only-vs-multi-edition]] | established | Bitcoin-only (~25% weniger Code) vs. Multi (Altcoins, U2F); gleiche Hardware, unwiderrufliche Firmware-Wahl |
| [[bitcoin-vaults]] | emerging | Verzögerte Auszahlungen + Wiederherstellungspfad; benötigt Covenants für vollständige Umsetzung |
| [[bitbox02-nova]] | established | BitBox02 Nova: iPhone-Support via Whisper/BLE, EAL6+ Chip, OLED-Glasdisplay |
| [[coin-control-und-utxo-auswahl]] | established | Manuelle UTXO-Auswahl als Datenschutzwerkzeug; Common Input Ownership Heuristic; CoinJoin-Vorbereitung; Umsetzung in Sparrow, Electrum, BitBoxApp |
| [[coinjoin-und-on-chain-privatsphäre]] | established | CoinJoin: gleiche Output-Beträge machen Transaktionen unzuordenbar; Samourai/Wasabi-Situation 2024 |
| [[cypherpunk-manifest]] | established | Eric Hughes (1993): Privatsphäre als Grundrecht im digitalen Raum; Kryptographie als einziges wirksames Werkzeug; "Cypherpunks write code"; Vorläufer von Bitcoin |
| [[kryptoanarchismus-und-cypherpunks]] | established | Cypherpunk-Bewegung 1986–2022: Hacker-Ethik, Timothy Mays Kryptoanarchismus, Barlow-Deklaration, PGP, Krypto-Kriege; direkte Vorgeschichte von Bitcoin |
| [[hacker-ethik]] | emerging | Loyd Blankenship "The Conscience of a Hacker" (1986): Neugier als Triebkraft; Unterförderung durch Schulsystem; klassenlose Online-Gemeinschaften; Phrack-Magazin |
| [[pgp-und-verschluesselungspolitik]] | established | Philip Zimmermann / PGP (1991): Warum PGP geschrieben wurde; Clipper Chip; CALEA; erster und zweiter Krypto-Krieg; Verschlüsselung als politisches Grundrecht |
| [[digitale-signaturen-ecdsa]] | established | ECDSA-Grundprinzip; r (Zufallspunkt auf elliptischer Kurve) + s (Private Key + Transaktions-Hash); Bindung an Transaktionsdaten verhindert Replay; Verifikation ohne Private Key; Einmaligkeit von k; Schnorr als Nachfolger |
| [[digitales-bargeld-und-ecash]] | established | Chaums eCash (1989), Hal Finneys Analyse (1994), Wei Dais b-money (1998), Van Valkenburghs "geheimes Recht auf Bargeld" (2017); digitales Bargeld vor Bitcoin; dezentrales Geld als Lösung |
| [[digitales-zeitstempel]] | established | Haber & Stornetta (1991): Hash-verkettete Dokumente; Bayer/Haber/Stornetta (1992): Merkle-Bäume für Timestamping; Massias et al.: minimales Vertrauen; direkte strukturelle Vorstufe der Bitcoin-Blockchain; Satoshi zitiert Haber & Stornetta 3× im Whitepaper |
| [[bitcoin-vererbung]] | established | Marc Steiner (2020): Nachlassplan-Struktur (2 Schichten), 8 Musterabläufe (#1 Grundvariante bis #8 2-von-3-Multisig), Materialien (Laserdrucker, Spezialpapier, Metall-Seed-Speicher), Erben-Erstanleitung, rechtliche Absicherung CH/DE/AT |
| [[ideal-money-und-bitcoin]] | speculative | John Nashs "Ideal Money"-Konzept; Bitcoin als mögliche Realisierung; Praxeologie der Privatsphäre (Mises/Hayek); österreichische Ökonomik und Bitcoin |
| [[bitcoin-geld-als-fiktion-und-paradigmenwechsel]] | established | Svanholm 2020: Piaget Akkommodation; Geld als intersubjektive Fiktion; Bitcoin-Knappheit objektiv prüfbar; Fiat als monetäres Krebsgeschwür; Hyperbitcoinisierung |
| [[bitcoin-spieltheorie-und-anreize]] | established | Svanholm & de Wolf 2024: Spieltheorie, Prisoner's Dilemma, katallaktischer vs. biologischer Wettbewerb; Bitcoin als Anreizinversion des Fiat-Systems; Freedom Footprint |
| [[bitcoin-alles-geteilt-durch-21-millionen]] | established | Svanholm 2022: Geschichte des Geldes; Cantillon-Effekt; ∞/21M-Formel; Knappheit in Geld = Überfluss im Rest; Creative Destruction und Hyperbitcoinisierung |
| [[praxeologie-und-oesterreichische-oekonomik]] | established | Svanholm 2023: Praxeologie als A-priori-Wissenschaft; Handlungs-Axiom; subjektive Wertlehre; Grenznutzen; Zeitpräferenz; Cantillon-Effekt; Katallaktik; Bitcoin als konsistentes Geld |
| [[phoenix-wallet-lightning]] | established | ACINQ Phoenix (2026 FAQ): Echter Lightning-Node auf Smartphone; Trust-minimized (nicht trustless); Inbound Liquidity; Swap-in Wallet; 0,4%+4sat Sendegebühr; BIP39-Seed-Wiederherstellung |
| [[wallet-of-satoshi]] | established | WoS FAQ (2026): Custodial vs. Self-Custodial Modi; Lightning Address; E-Mail-Backup (custodial) vs. Seed (self-custodial); Regionsverfügbarkeit; einfachste Lightning-Wallet |
| [[bitblik]] | established | bitblik FAQ (2026): BLIK–Bitcoin Bridge; Lightning Hold-Invoice Escrow; non-custodial P2P; kein KYC; FOSS; kein App Store; ~2 min Settlement; Polen |
| [[muun-wallet]] | established | Muun (2019–2021): non-custodial Lightning+On-Chain; Emergency Kit (Output Descriptors); Submarine Swaps; LND-basiert; warum Mnemonic allein nicht reicht; Taproot-Upgrade |
| [[lightning-splicing]] | established | Splicing in Lightning: Splice-In/Out; Channel-Kapazität ändern ohne Close; Operational vs. Financial Costs; Vergleich mit Circular Payments und Fee Management; Phoenix-Praxis |
| [[lightning-rebalancing]] | established | Lightning Rebalancing: Channel-Imbalance durch Routing; 3 Strategien (Circular Payments, Fee Management, Splices); Intermediate vs. Edge Node |
| [[nunchuk-wallet]] | established | Nunchuk (2025/2026): Bitcoin-only Assisted Multisig (phone watch-only); BSMS-Interoperabilität; 2 Inheritance-Protokolle (On-Chain Miniscript autonom, Off-Chain flexibel); Recovery mit Sparrow/Bitcoin Core |
| [[core-lightning-26-06]] | established | CLN 26.06 (2026-06-04): xpay als Standard; Quantum-Resistant Channels; bwatch-Architektur für Block-Processing; Splicing-Fixes; graceful Shutdown; BOLT12-Proofs |
| [[lightning-netzwerk-grundlagen]] | established | Zahlungskanäle, lokale/Remote-Balance, Inbound-Kapazitätsproblem, HTLCs, Onion Routing; Eigenbetrieb vs. LSP; Submarine Swaps |
| [[lightning-address-datenschutz]] | established | Lightning Address Datenschutz: LNURL-Server-Sichtbarkeit; Spark-Doxxing via Routing Hints (reneaaron Tool); permanente Kennung in Invoices; Gegenmaßnahmen (BOLT12, self-hosted) |
| [[diceware-und-seed-generierung]] | established | Eigenen Bitcoin-Seed mit Casino-Würfeln erzeugen; BitBox02 berechnet gültiges 24. Wort; BIP-39-kompatibel; Akt persönlicher Souveränität ohne Gerätevertrauen für Entropie |
| [[electrum-wallet]] | established | Electrum: Setup mit BitBox02, Server-Wahl (eigener EPS empfohlen), Adressformate, Ableitungspfade, Coin Control, RBF, Pay-to-many, Watch-only, Tor-Integration |
| [[eu-regulierung-selbstverwahrung]] | established | EU-AML schließt Non-Custodial-Wallets ausdrücklich aus; Selbstverwahrung technisch uneinschränkbar |
| [[hd-wallets-und-schluesselableitung]] | established | BIP32/BIP39: Seed → Ableitungspfad (m/49'/0'/0'/0/n) → privater Schlüssel → öffentlicher Schlüssel → Adresse; nur Seed sichern nötig |
| [[kryptografische-schlussel-und-adressen]] | established | Private Key (256-Bit-Zufallszahl, 2^256 mögliche Werte), Public Key (elliptische Kurven-Multiplikation, Trapdoor-Funktion, compressed Format), Adresse (Hash des Public Keys, Base58Check); Einwegkette; Verlust = permanent |
| [[hardware-wallet-angriffsvektoren]] | established | 5 Angriffe via Host-Gerät: Change-Output, Passphrase-Relay, Cosigner-Manipulation, überhöhte Gebühr, Isolations-Bypass |
| [[hardware-wallet-einstieg]] | established | Warum Hardware-Wallet: 4 Optionen (Börse, Software-Wallet, HW-Wallet, Air-Gap); "not your keys, not your coins"; Paper Wallets unsicher; empfohlene Kombination |
| [[hardware-wallet-migration]] | established | Migration Ledger/Trezor→BitBox02; SLIP-39 (20 Wörter) ≠ BIP-39; zwei Migrationswege; Passphrase-Übertragung |
| [[hardware-wallet-sicherheitsarchitektur]] | established | Display, Open-Source, Secure Chip, BIP-39; Dual-Chip-Architektur; Drei Bedrohungstypen; BitBoxApp-Plattformarchitektur (Go + React) |
| [[komplexität-ist-keine-sicherheit]] | established | Mehr Komplexität ≠ mehr Sicherheit; Sweet Spot: Single-Sig HW-Wallet; Expertentools nur mit vollem Verständnis |
| [[konsensregeln-und-mempool-richtlinien]] | established | Konsensregeln (netzwerkweit, unveränderlich) vs. Mempool-Richtlinien (lokal, konfigurierbar) |
| [[miniscript-und-liana]] | established | Zeitlich gesperrte Wiederherstellungsschlüssel mit Miniscript; Liana Wallet + MiniTapscript; Go-Parser-Typsystem |
| [[multisig-und-kollaborative-verwahrung]] | established | m-von-n Multisig, Fallstricke (xpubs, Cosigner), kollaborative Verwahrung (Unchained) |
| [[op-return-und-datenspeicherung]] | established | OP_RETURN erklärt; 80-Byte-Limit als Mempool-Richtlinie; Datenspeicherungsdebatte 2025 |
| [[opsec-und-privatsphäre]] | established | OPSEC für Bitcoin-Nutzer; Shift Crypto Datenschutzprinzipien (IP-Anonymisierung, 30-Tage Webshop, diskrete Pakete); Beträge nicht teilen; anonym kaufen |
| [[optionale-passphrase]] | established | BIP-39 Passphrase: zweiter Faktor, Plausible Deniability; bewusst nicht auf microSD gespeichert |
| [[payment-codes-und-adressaustausch]] | emerging | BIP-47 PayNyms vs. Silent Payments: statische Adressen mit Privatsphäre |
| [[payment-requests]] | established | SLIP-24: Börsen-Adressen kryptografisch auf Hardware-Wallet verifizieren; verhindert Address Spoofing |
| [[phishing-und-angriffsmethoden]] | established | Fake-Apps, Address Spoofing, Phishing-E-Mails, Keylogger — Angriffsmethoden und Gegenmaßnahmen |
| [[regulierung-tofr-aopp]] | established | EU ToFR / Travel Rule; Satoshi-Test-Probleme; AOPP als bessere Adressverifizierung |
| [[selbstverwahrung-und-boersenrisiken]] | established | Proof-of-Keys-Tag; Börsenrisiken (Mt.Gox, QuadrigaCX, FTX, Papier-Bitcoin); KYC als Datenschutzrisiko (Chainalysis); nur eigene Keys = echte Bitcoin |
| [[seedphrase-entropie-und-sicherheit]] | established | 2^256 Möglichkeiten ≈ Atome im Universum; Risiken schwacher Zufallsgeneratoren; BitBox02 Entropiequellen; Diceware als Alternative |
| [[silent-payments]] | emerging | BIP-352: statische Adressen ohne Privatsphäre-Verlust via ECDH; DLEQ-Beweise für Hardware-Wallets |
| [[skalierung-lightning-ark-statechains]] | emerging | Lightning (Kuriere), Ark (Zug mit VTXOs), Statechains (Eigentum übertragen ohne Bewegung) |
| [[segregated-witness-segwit]] | established | BIP-141: Witness-Trennung, Malleability-Fix, Block Weight, P2WPKH/P2WSH, Lightning-Voraussetzung |
| [[shamir-secret-sharing]] | established | k-of-n Geheimnis-Aufteilung via Polynom-Mathematik; warum 1 Share nichts verrät; Unterschied zu Multisig; FROST als Weiterentwicklung ohne Rekonstruktions-Risiko; SLIP-39 als Bitcoin-Anwendung |
| [[hashcash]] | established | Adam Back (1997/2002): CPU-Kostenfunktion / Proof-of-Work gegen Spam; SHA-1-Hash mit führenden Nullbits; asymmetrisch: Finden teuer, Verifizieren trivial; direkte technische Vorstufe von Bitcoin-Mining; im Whitepaper zitiert |
| [[merkle-baeume]] | established | Merkle (1980) + Bayer/Haber/Stornetta (1992): Baumstruktur aus Hashes; Root repräsentiert alle Blätter kryptografisch; Bitcoin Transaction Merkle Tree; SPV-Beweis mit log(n) Hashes; Grundlage für Taproot/MAST |
| [[mining-schwierigkeit]] | established | Difficulty passt sich alle 2016 Blöcke an (Formel: erwartet/tatsächlich × aktuelle Difficulty); max Faktor ×4 pro Periode; Target = MaxTarget / Difficulty; Ziel: 10-Minuten-Blockzeit; Hex-Darstellung; bitcoin-cli getdifficulty |
| [[szabo-geldursprung]] | established | Nick Szabo "Shelling Out" (2002): Evolutionäre Ursprünge des Geldes — Collectibles vor 75.000 Jahren; 6 Geldattribute; Kooperationsprobleme die Geld löst; Bitcoin als digitale Realisierung; "Advances in Distributed Security" (2003): Byzantine Generals, Threshold-Systeme |
| [[soft-fork-und-hard-fork]] | established | Hard Fork (Regeln entfernen) vs. Soft Fork (Regeln hinzufügen); Kompatibilität und Chainsplits |
| [[sparrow-wallet]] | established | Sparrow Wallet: UTXO-Transparenz, Coin Selection, Pay-to-many, Multisig; "cold-storage sweating"; Server-Wahl (Public/Bitcoin Core/Electrum/BitBox-Server) |
| [[taproot-musig2-frost]] | established | Taproot (Soft Fork 2021): Schnorr, MAST, Key-Path/Script-Path; MuSig2 (n-von-n Aggregation); FROST (Threshold-Signaturen) |
| [[transaktionsgebuehren-und-mempool]] | established | Blockgröße (begrenzt), Miner-Incentive (sat/vByte), Mempool (mempool.space/jochen-hoenicke.de), Priorität-Auswahl in BitBoxApp; Zusammenhang mit UTXO-Konsolidierung |
| [[utxo-modell-und-konsolidierung]] | established | UTXO-Modell erklärt; Gebührenberechnung; UTXO-Konsolidierung in Niedriggebühren-Phasen |
| [[wallet-backup-strategien]] | established | HD-Wallet-Mechanismus (einmal = dauerhaft); 5 häufige Fehler; 4 Sicherungsmethoden (Passphrase, 2-von-3, Multisig); Steelwallet; Vererbungsplanung |
| [[walletconnect-und-dapps]] | established | WalletConnect-Protokoll (QR-Pairing); BitBoxApp-DApp-Integration; nur Ethereum Mainnet + Multi Edition; Sicherheitshinweise bei Smart-Contract-Interaktion |

| [[wie-funktioniert-bitcoin]] | established | Bitcoin als Programm + Netzwerk; Double-Spend-Problem; Blockchain als geteiltes Kassenbuch; Mining-Sicherheit; Longest-Chain-Regel; UTXOs; kryptografische Schlüssel — Gesamtüberblick für Einsteiger |

*88 Artikel, basierend auf 353 RAW-Quellen (inkl. 6 EPUBs aus Svanholm/Steiner/Rosenbaum).*
