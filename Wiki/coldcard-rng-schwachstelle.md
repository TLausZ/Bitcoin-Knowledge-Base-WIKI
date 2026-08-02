# Coldcard RNG-Schwachstelle (2021–2026)

**Status:** established
**Themen:** protokoll, self-custody, wallets
**Last updated:** 2026-08-02
**Sources:** [[2026-07-31_02_coldcard-rng-schwachstelle-wiki]], [[2026-08-02_bitcoinwell_the-coldcard-hack-38m-entropy-failure]], [[2026-08-02_coldcard-watch-dashboard]]

## Summary

Ab Firmware v4.0.0 erzeugte die Bitcoin-Hardware-Wallet Coldcard von Coinkite ihre kryptografischen Geheimnisse nicht mit dem Hardware-Zufallsgenerator des verbauten STM32-Mikrocontrollers, sondern mit einem deterministischen Software-Generator. Ursache war eine Präprozessor-Prüfung, die nur testete, ob ein Makro definiert ist, nicht ob es einen von Null verschiedenen Wert hat. Der Fehler lag seit März 2021 im ausgelieferten Code. Am 30. und 31. Juli 2026 wurden in drei automatisierten Wellen mindestens 1'359 BTC (rund 71 Mio. USD) aus 4'312 verifizierten Adressen abgezogen; noch am ersten Tag veröffentlichten Coinkite ein Advisory und Sicherheitsforscher bei Block eine unabhängige Analyse. Seeds und Schlüssel, die unter betroffener Firmware entstanden, gelten als kompromittiert; ein Firmware-Update repariert sie nicht. Stand: 2. August 2026.

## Body

### Der Fehler

Die Coldcard-Firmware wechselte am 1. März 2021 auf die Kryptobibliothek libngu. Deren Prüfung auf einen verfügbaren Hardware-RNG fragte per Präprozessor ab, ob das Makro `MICROPY_HW_ENABLE_RNG` existiert. In der Board-Konfiguration der Coldcard war es auf `0` gesetzt — definiert, aber abgeschaltet. Die Prüfung wertete die blosse Existenz als Zustimmung, der Aufruf des Hardware-RNG entfiel, und stillschweigend übernahm der in MicroPython enthaltene Yasmarang-Generator die Arbeit.

Dessen Zustand wurde aus drei Werten initialisiert: den unteren 32 Bit der Geräte-UID, kombiniert mit dem SysTick-Zähler, sowie zwei Registern der Echtzeituhr (Tageszeit und Subsekunden). Keiner davon ist kryptografisch geeignet. Die UID ist fest im Chip verankert, von ihren 96 Bit wurden nur 32 genutzt. Der SysTick-Zähler ist periodisch und deckt bei typischer Bootdauer nur etwa 80'000 bis 120'000 Werte ab. Die Uhrenregister korrelieren mit dem Einschaltzeitpunkt und sind teilweise statisch.

### Wieviel Sicherheit bleibt

| Modell | Firmware | Zustand |
|---|---|---|
| Mk1 | alle | nicht betroffen |
| Mk2, Mk3 | bis v3.2.2 | nicht betroffen |
| Mk2, Mk3 | v4.0.0 bis v4.1.9 | vollständig deterministisch, kein Reseed |
| Mk4, Q, Mk5 | ab v5.0.0 | Fallback aktiv, Reseed auf 32 Bit begrenzt |

Massgeblich ist die Firmware-Version zum Zeitpunkt der Schlüsselerzeugung, nicht das Herstellungsdatum.

Zwei Präzisierungen aus dem Abgleich mit Coinkites signiertem Release-Manifest (Coldcard Sweep Watch): Eine Firmware 4.0.0 wurde nie ausgeliefert, die erste Version, auf der jemand einen Seed erzeugen konnte, ist 4.0.1. Und das Coinkite-Advisory begrenzt den Mk3 auf Version 4.1.9, obwohl 2022 noch signierte Mk3-Builds 5.0.1 und 5.0.3 erschienen — ob diese betroffen sind, hat Coinkite nicht gesagt; das Dashboard listet sie vorsorglich als gefährdet. [[2026-08-02_coldcard-watch-dashboard]]

Für Mk2 und Mk3 unter Firmware v4 bleibt ein Suchraum von etwa 2^40,7, wenn die Timer-Werte unbekannt sind, und etwa 2^16,3, wenn sie bekannt sind. Bei bekannter Geräte-UID und bekannter Reihenfolge der RNG-Aufrufe ist die Ausgabe praktisch vorhersagbar. Ab v5.0.0 liefert das Secure Element zwar einen authentifizierten 32-Byte-Wert, davon erreichen aber nur vier Bytes die Reseed-Funktion und ersetzen ein einzelnes 32-Bit-Zustandswort. Der Suchraum liegt damit bei höchstens 2^32 Kandidaten, im Mittel rund 2^31.

Nachgelagertes Hashing hilft dabei nicht. SHA256d erhöht keine Entropie, die eingangsseitig fehlt, und die BIP-39-Prüfsumme trägt ohnehin keine bei; dasselbe Prinzip steht in [[seedphrase-entropie-und-sicherheit]] und [[bip39-schwache-seeds]].

### Was betroffen ist

Der Fehler trifft alles, was auf dem Generator aufbaut: Wallet-Seeds einschliesslich ephemerer, private Schlüssel für Paper Wallets, Seed-XOR-Masken, Schlüssel für Cloning und USB-Verschlüsselung, Key-Teleport-Schlüssel, Web2FA-Secrets und Passwörter für Secure Notes. Kandidaten lassen sich offline gegen bekannte öffentliche Schlüssel oder abgeleitete Adressen prüfen, ohne dass das Gerät je wieder angefasst werden muss.

Eine BIP-39-Passphrase stammt nicht aus dem Generator und bringt eigene Entropie mit. Sie erhöht den Angriffsaufwand um ihre eigene Entropie, multipliziert mit den Kosten von 2'048 PBKDF2-Runden je Kandidatenpaar. Sie schützt aber ausschliesslich BIP-39-Seeds, keine der übrigen betroffenen Funktionen. Die Analyse von Block behandelt Passphrasen nicht. Coinkites Empfehlung ist entsprechend zweistufig: Die Passphrase reduziert die unmittelbare Gefährdung, repariert den Seed aber nicht — auch Passphrase-Nutzer sollen auf einen neuen Seed migrieren. Bei Würfel-Entropie gilt: 50 bis 98 eigene Würfe steuerten mindestens 128 Bit bei, 99 und mehr etwa 256 Bit; wer unter 50 Würfen lag oder sich nicht erinnert, soll migrieren. [[2026-08-02_coldcard-watch-dashboard]]

### Der Diebstahl vom 30./31. Juli 2026

Das On-Chain-Gesamtbild liefert das Live-Dashboard Coldcard Sweep Watch (anonymer Betreiber, Transaktion für Transaktion verifiziert, ausdrücklich als Untergrenze deklariert): mindestens 1'359.18 BTC, rund 71 Mio. USD (bei $62'949/BTC), aus 4'312 bestätigten Adressen in drei Clustern — 1'195 Adressen am 30. Juli (Blöcke 960'183–960'191), 1'126 am 31. Juli (Blöcke 960'345–960'369) und 13 weitere später am selben Tag (Block 960'455). Die letzte verifizierte Drain datiert vom 31. Juli, 08:36:17 UTC. Weil das erste Fenster in US-Zeitzonen auf den Abend des 29. Juli fiel, datieren manche Berichte den Diebstahl auf den 29. Das Dashboard warnt zudem, weitere unentdeckte Cluster anderer Angreifer seien «near certain». [[2026-08-02_coldcard-watch-dashboard]]

Die erste Welle beschreibt Addairs Bericht vom 31. Juli im Detail: Zwischen 01:36 und 01:51 UTC räumte eine automatisierte Operation rund 500 Adressen mit 1'324 UTXOs und etwa 594.5 BTC (~38 Mio. USD) leer, bei Gebühren von nur ~0.044 BTC; 562 BTC flossen in eine einzelne Konsolidierungsadresse. Diese Zahlen sind ein früher Snapshot der ersten Welle — das Dashboard verifizierte im selben Blockfenster später mehr als doppelt so viele Adressen. Die Beute liegt laut Dashboard auf sechs Konsolidierungsadressen; erkannte Bewegungen werden dort Hop für Hop weiterverfolgt (Stand: 2. August 2026).

Das On-Chain-Muster trägt die Signatur der Schwachstelle: ausschliesslich Single-Sig-Adressen, kein Multisig, kein Taproot, Seeds aus den Jahren 2021 bis 2026. Der kleinste Verlust lag bei 0.15 BTC, was auf eine Vorfilterung der Ziele nach Mindestguthaben hindeutet; der Median lag bei 0.41 BTC, der grösste Einzelverlust bei 29.9 BTC. Rob Hamilton (AnchorWatch) diagnostizierte noch am selben Tag «faulty entropy in wallet generation». Auffällig für die Verteidigungsseite: Jede einzige geleerte Wallet war ein Single-Sig-Seed ohne BIP-39-Passphrase. Das deckt sich mit der Analyse oben — die Passphrase ist der eine Input, den der defekte Generator nie erzeugt hat.

Der zeitliche Ablauf der Aufdeckung: Die erste Meldung kam um 13:19 UTC von einem Opfer auf Reddit. Kevin Loaec (Wizardsardine) eskalierte ab 17:35 UTC («This is not a drill»), Jameson Lopp bestätigte auch Teilabflüsse. Coinkite-Gründer NVK erklärte den Vorfall um 18:10 UTC zunächst als geleakte Fremd-Seeds, zog diese Einschätzung aber zurück, als sich das systemische Muster abzeichnete. Bis zum Tagesende folgten das Mk3-Advisory und der Block-Report.

Coinkite lieferte über Nacht einen Hotfix aus: Firmware 5.6.0 für Mk4 und Mk5, 1.5.0Q für die Q. Der Fix schliesst den MicroPython-Fallback explizit aus dem Build aus und ergänzt eine Compile-Zeit-Prüfung, die fehlschlägt, wenn nicht der Hardware-RNG angebunden ist — genau die Prüfung, deren Fehlen den Fehler vier Jahre überleben liess. Der Mk3 ist aus dem Support und erhält keinen Hotfix; seine Besitzer werden auf den Migrationspfad des Advisories verwiesen. Bemerkenswert am Rande: Coinkite geht davon aus, dass der Angreifer den Fehler per AI-Analyse der quelloffenen Firmware fand, und gibt an, wenige Wochen zuvor selbst ein führendes AI-Modell über den eigenen Code laufen gelassen zu haben, ohne dass es den Bug fand.

Der Fall reiht sich in ein wiederkehrendes Muster schwacher Seed-Erzeugung ein: Milk Sad (2023, Zeitstempel als einzige Entropie), Randstorm (Browser-Wallets 2011–2015) und die Ill-Bloom-Disclosure vom Juli 2026 (fünf Wallet-Implementierungen). Vergleiche [[bip39-schwache-seeds]].

### Konsequenz für Betroffene

Ein Update stellt bestehende Geheimnisse nicht wieder her. Wer unter betroffener Firmware Schlüssel erzeugt hat, muss sie ersetzen und die Guthaben auf eine neu erzeugte Wallet transferieren. Ein betroffener Seed bleibt auch dann schwach, wenn er auf ein Gerät eines anderen Herstellers restauriert wird — die Schwäche liegt in den Zahlen, nicht in der Hardware (so auch Trezors Hinweis an eigene Nutzer).

Als Weg, die Abhängigkeit vom geräteinternen Generator zu umgehen, bleibt die externe Erzeugung der Seed-Entropie mit physischen Würfeln (siehe [[diceware-und-seed-generierung]]). Ein Rest an Vertrauen bleibt auch dann bestehen, weil das Gerät den extern erzeugten Seed korrekt übernehmen und speichern muss.

Hardware-Wallets anderer Hersteller laufen mit eigener Firmware und sind von diesem Fehler nicht betroffen. Über die Qualität ihrer eigenen Zufallserzeugung sagt das nichts aus.

### Umfang: der frühere Widerspruch ist aufgelöst

Das erste Security Advisory von Coinkite (30. Juli 2026) adressierte nur Mk3-Besitzer mit Firmware ab v4.0.1, die Analyse von Block führte zusätzlich Mk4, Q und Mk5 auf. Die Folgeereignisse bestätigen die breitere Block-Sicht: Der Hotfix vom 31. Juli gilt genau den Modellen Mk4, Mk5 und Q, und Coinkites eigene Folgeanalyse beziffert deren Restsuchraum als «material improvement», das die 128-Bit-Zielmarke trotzdem verfehlt. Die Fokussierung auf den Mk3 erklärt sich daraus, dass der Diebstahl Mk3-Ära-Wallets traf (dort ist der Suchraum am kleinsten), nicht daraus, dass andere Modelle sauber wären.

Eine Richtigstellung zur kursierenden Zahl «acht Jahre alter Bug»: Der verwundbare MicroPython-Fallback-Code stammt von Mai 2018, er gelangte aber erst mit der libngu-Migration im März 2021 in die Seed-Erzeugung der Coldcard. Betroffene Seeds reichen also gut vier Jahre zurück, nicht acht.

### Zeitleiste

| Datum | Ereignis |
|---|---|
| Januar 2021 | Fehlerhafte Makro-Prüfung in libngu vorhanden |
| 1. März 2021 | Coldcard migriert auf libngu |
| 17. März 2021 | Firmware v4.0.0 mit betroffenem Code veröffentlicht |
| März 2022 | 32-Bit-Reseed-API ergänzt, Fallback bleibt bestehen |
| 30. Juli 2026, 01:36–01:51 UTC | Erste Diebstahlswelle: 1'195 Adressen in den Blöcken 960'183–960'191 (Addairs früher Snapshot: 500 Adressen, 594.5 BTC) |
| 30. Juli 2026, tagsüber | Erste Opfermeldung auf Reddit (13:19 UTC), Community-Diagnose «faulty entropy», Coinkite-Advisory, Block-Report |
| 31. Juli 2026 | Zweite und dritte Welle: 1'126 Adressen (Blöcke 960'345–960'369) und 13 weitere (Block 960'455), letzte Drain 08:36 UTC; Hotfix 5.6.0 (Mk4/Mk5) und 1.5.0Q (Q); Mk3 ohne Support |
| 2. August 2026 | Verifizierte Untergrenze 1'359 BTC aus 4'312 Adressen; Coinkite macht öffentlich, Betroffene direkt per Mail informiert zu haben |

Zwischen Auslieferung und Entdeckung liegen fünf Jahre und vier Monate, obwohl die Firmware quelloffen ist und geprüft werden konnte. Die Reviews bestätigten, dass der korrekte Hardware-TRNG im Binary vorhanden war, prüften aber nie, welche der beiden gleichnamigen Funktionen der Seed-Pfad tatsächlich aufruft — vorhanden ist nicht dasselbe wie verwendet.

## Related

- [[bitcoin-entropy-rng]]
- [[seedphrase-entropie-und-sicherheit]]
- [[bip39-schwache-seeds]]
- [[bitcoin-seed-cracking]]
- [[diceware-und-seed-generierung]]
- [[hardware-wallet-angriffsvektoren]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[hardware-wallet-migration]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[multisig-und-kollaborative-verwahrung]]
- [[optionale-passphrase]]

## Open Questions

- Die Gesamtsumme ist eine deklarierte Untergrenze; das Dashboard hält weitere unentdeckte Cluster anderer Angreifer für «near certain». Die Zahl dürfte weiter steigen.
- Ob die 2022er Mk3-Builds 5.0.1/5.0.3 betroffen sind, hat Coinkite nicht geklärt; das Dashboard listet sie vorsorglich als gefährdet.
- Der Korpus hat keinen Artikel darüber, wie Hardware-Wallet-Firmware unabhängig geprüft wird (reproduzierbare Builds, Audits, Bug-Bounty). Dieser Fall wäre der Anlass, einen anzulegen.
