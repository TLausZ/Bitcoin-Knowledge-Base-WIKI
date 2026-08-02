# Coldcard RNG-Schwachstelle (2021–2026)

**Status:** emerging
**Themen:** protokoll, self-custody, wallets
**Last updated:** 2026-07-31
**Sources:** [[2026-07-31_02_coldcard-rng-schwachstelle-wiki]]

## Summary

Ab Firmware v4.0.0 erzeugte die Bitcoin-Hardware-Wallet Coldcard von Coinkite ihre kryptografischen Geheimnisse nicht mit dem Hardware-Zufallsgenerator des verbauten STM32-Mikrocontrollers, sondern mit einem deterministischen Software-Generator. Ursache war eine Präprozessor-Prüfung, die nur testete, ob ein Makro definiert ist, nicht ob es einen von Null verschiedenen Wert hat. Der Fehler lag seit dem 17. März 2021 im ausgelieferten Code und wurde am 30. Juli 2026 von Sicherheitsforschern bei Block veröffentlicht, nachdem aktive Ausnutzung beobachtet worden war. Seeds und Schlüssel, die unter betroffener Firmware entstanden, gelten als kompromittiert; ein Firmware-Update repariert sie nicht. Stand: 31. Juli 2026.

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

Für Mk2 und Mk3 unter Firmware v4 bleibt ein Suchraum von etwa 2^40,7, wenn die Timer-Werte unbekannt sind, und etwa 2^16,3, wenn sie bekannt sind. Bei bekannter Geräte-UID und bekannter Reihenfolge der RNG-Aufrufe ist die Ausgabe praktisch vorhersagbar. Ab v5.0.0 liefert das Secure Element zwar einen authentifizierten 32-Byte-Wert, davon erreichen aber nur vier Bytes die Reseed-Funktion und ersetzen ein einzelnes 32-Bit-Zustandswort. Der Suchraum liegt damit bei höchstens 2^32 Kandidaten, im Mittel rund 2^31.

Nachgelagertes Hashing hilft dabei nicht. SHA256d erhöht keine Entropie, die eingangsseitig fehlt, und die BIP-39-Prüfsumme trägt ohnehin keine bei; dasselbe Prinzip steht in [[seedphrase-entropie-und-sicherheit]] und [[bip39-schwache-seeds]].

### Was betroffen ist

Der Fehler trifft alles, was auf dem Generator aufbaut: Wallet-Seeds einschliesslich ephemerer, private Schlüssel für Paper Wallets, Seed-XOR-Masken, Schlüssel für Cloning und USB-Verschlüsselung, Key-Teleport-Schlüssel, Web2FA-Secrets und Passwörter für Secure Notes. Kandidaten lassen sich offline gegen bekannte öffentliche Schlüssel oder abgeleitete Adressen prüfen, ohne dass das Gerät je wieder angefasst werden muss.

Eine BIP-39-Passphrase stammt nicht aus dem Generator und bringt eigene Entropie mit. Sie erhöht den Angriffsaufwand um ihre eigene Entropie, multipliziert mit den Kosten von 2'048 PBKDF2-Runden je Kandidatenpaar. Sie schützt aber ausschliesslich BIP-39-Seeds, keine der übrigen betroffenen Funktionen. Die Analyse von Block behandelt Passphrasen nicht.

### Konsequenz für Betroffene

Ein Update stellt bestehende Geheimnisse nicht wieder her. Wer unter betroffener Firmware Schlüssel erzeugt hat, muss sie ersetzen und die Guthaben auf eine neu erzeugte Wallet transferieren.

Als Weg, die Abhängigkeit vom geräteinternen Generator zu umgehen, bleibt die externe Erzeugung der Seed-Entropie mit physischen Würfeln (siehe [[diceware-und-seed-generierung]]). Ein Rest an Vertrauen bleibt auch dann bestehen, weil das Gerät den extern erzeugten Seed korrekt übernehmen und speichern muss.

Hardware-Wallets anderer Hersteller laufen mit eigener Firmware und sind von diesem Fehler nicht betroffen. Über die Qualität ihrer eigenen Zufallserzeugung sagt das nichts aus.

### Offener Widerspruch in der Bewertung

Das Security Advisory von Coinkite vom 30. Juli 2026 adressiert Besitzer eines Mk3 mit Firmware v4.0.1. Die Analyse von Block führt darüber hinaus Mk4, Q und Mk5 als betroffen auf. Hersteller und Forscher stellen den Umfang also unterschiedlich dar. Solange das ungeklärt ist, steht dieser Artikel auf *emerging*.

### Zeitleiste

| Datum | Ereignis |
|---|---|
| Januar 2021 | Fehlerhafte Makro-Prüfung in libngu vorhanden |
| 1. März 2021 | Coldcard migriert auf libngu |
| 17. März 2021 | Firmware v4.0.0 mit betroffenem Code veröffentlicht |
| März 2022 | 32-Bit-Reseed-API ergänzt, Fallback bleibt bestehen |
| 30. Juli 2026 | Veröffentlichung durch Block nach beobachteter Ausnutzung, Stellungnahme von Coinkite |

Zwischen Auslieferung und Entdeckung liegen fünf Jahre und vier Monate, obwohl die Firmware quelloffen ist und geprüft werden konnte.

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

## Open Questions

- Wie viele Guthaben wurden tatsächlich abgezogen? Die Veröffentlichung nennt beobachtete Ausnutzung, aber keine Zahlen.
- Ob und wie Coinkite seine Einschätzung zu Mk4, Q und Mk5 anpasst, ist offen und sollte nachgetragen werden.
- Der Korpus hat keinen Artikel darüber, wie Hardware-Wallet-Firmware unabhängig geprüft wird (reproduzierbare Builds, Audits, Bug-Bounty). Dieser Fall wäre der Anlass, einen anzulegen.
