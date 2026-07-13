# Specter DIY

**Status:** established
**Themen:** self-custody, wallets
**Last updated:** 2026-06-27 (USB-Befehlssatz, SD-Card-Protokoll, offizielle Docs ergänzt)
**Sources:** [[Specter-Hardware-Wallet-Anleitung_v1_0_0]], [[Specter-Shield-Metal-Manual-part_EN_v1_0_0]], [[Specter DIY – Testbericht zur ersten DIY Bitcoin Hardware Wallet]], [[specter-diy-introduction]], [[specter-diy-faq]], [[specter-diy-shopping]], [[specter-diy-assembly]], [[specter-diy-shield]], [[specter-diy-shield-lite]], [[specter-diy-quickstart]], [[specter-diy-communication]], [[specter-diy-roadmap]], [[20220309_bitbox02-multisig-specter-desktop-de]]

## Summary

Specter DIY ist eine Bitcoin-only Hardware-Wallet, die 2018 als Open-Source-DIY-Projekt gegründet wurde und sich durch Air-Gap-Kommunikation via QR-Codes, optionale Smartcard-Speicherung und vollständige Überprüfbarkeit aller Komponenten auszeichnet. Die Hardware basiert auf einem STM32-Entwicklerboard (oder einem vormontierten Gerät von ClavaStack), die Firmware ist MIT-lizenziert und unterstützt reproduzierbare Builds. Seit 2025 liegt das Projekt in den Händen einer Schweizer Non-Profit, der Specter Association.

## Body

### Geschichte und Organisation

CryptoAdvance, gegründet 2018 in München vom Quantenphysiker Stepan Snigirev und Moritz Wietersheim, veröffentlichte die Firmware und Bauanleitung der ersten DIY Hardware Wallet ohne Geschäftsmodell. Parallel entstand Specter Desktop, eine Companion-App für den PC, die als erste Lösung Multisig-Setups und Fullnode-Verbindungen für Normalnutzer zugänglich machte.

2022 kaufte Swan Bitcoin das Startup, entwickelte beide Projekte kaum weiter und setzte das Team für ein Collaborative-Custody-Produkt ein. 2025 übertrug Swan alle Markenrechte und Social-Media-Kanäle ohne Gegenleistung an die neu gegründete Specter Association in der Schweiz — einen Non-Profit-Verein mit aktuell 11 Mitgliedern, der sich durch Spenden finanziert und ehrenamtlich weiterentwickelt wird. Im europäischen Markt vertreibt ClavaStack (München) die Geräte.

### Kernphilosophie: Vertrauen minimieren

Das Designziel ist nicht Komfort, sondern minimales Vertrauen in Hersteller und Lieferkette. Wer die Standardkomponenten (STM32F469I-DISCO Entwicklerboard, Waveshare QR-Scanner) selbst in normalen Elektronikläden kauft, muss keiner Firma beim Zusammenbau vertrauen. Die Einzelkäufe lassen nicht auf den Bau einer Bitcoin-Wallet schließen (Privatsphäre), kein Hersteller weiß vom Zusammenbau (Supply-Chain-Resistenz), und alle Teile sind in Rohform inspizierbar.

Die Firmware ist MIT-lizenziert, vollständig Open-Source auf GitHub, und unterstützt reproduzierbare Builds — jeder kann verifizieren, dass die installierte Binärdatei exakt dem publizierten Quellcode entspricht. Die Embit-Library, die Specter dabei entwickelte, floss in andere DIY-Wallet-Projekte ein (SeedSigner, Krux).

Wer das Gerät fertig montiert bei ClavaStack kauft, gewinnt Komfort, muss dafür aber dem Anbieter vertrauen. Die Tamper-Evident-Verpackung und der Proof-Service auf proof.clavastack.com reduzieren dieses Risiko: Der Hash des Tamper-Evident-Bags wird am Verpackungstag fotografiert, gehasht und auf der Website sowie in der Bitcoin-Blockchain verankert, sodass der Käufer die Herkunft nachprüfen kann.

### Die drei Varianten

**Specter DIY (165 €)** ist die Basisvariante mit 3D-gedrucktem Gehäuse, QR-Scanner und Micro-USB. Kein Akku, kein Secure-Chip. Das Gerät wird primär als reines Signiergerät eingesetzt: Die Seedphrase liegt nur temporär im RAM, wird nach dem Stromtrennen nicht mehr rekonstruierbar und muss bei jeder Nutzung neu eingegeben oder per Seed-QR eingescannt werden. Diese Variante eignet sich für Bastler, die auf jedes proprietäre Bauteil verzichten wollen.

**Specter Shield Lite (190 €)** ergänzt die Basis um einen Smartcard-Slot mit Secure Chip. Zwei Smartcards sind im Lieferumfang. Kein Akku, 3D-gedrucktes Gehäuse. Das Preis-Leistungs-Verhältnis ist das beste der drei Varianten — volle Sicherheitsarchitektur zu einem mit anderen Hardware-Wallets konkurrenzfähigen Preis.

**Specter Shield Metal (399 €)** bietet dasselbe Sicherheitsniveau mit gefrästem Aluminiumgehäuse und integriertem Lithium-Polymer-Akku (3,7 V) — die einzige Variante ohne externe Powerbank. Ladezeit ca. 3,75 Stunden, Akkulaufzeit ca. 4,5 Stunden. Geladen wird ausschließlich über das mitgelieferte Kabel am unteren Port (5 V DC, min. 500 mA); rote LED = lädt, aus = voll. Maße: 13,4 × 6,7 × 2,6 cm, Gewicht 248 g. Lieferumfang: 2 Smartcards (optional getarnt), SD-Karte, 2× Backup Stack Mini für Seedphrase, 5× Tamper-Evident Bags, hochwertiges Stoffmäppchen. Akku nicht selbst wechselbar — eigene Öffnungsversuche erlöschen die Garantie.

| | Specter DIY | Shield Lite | Shield Metal |
|---|---|---|---|
| Preis | 165 € | 190 € | 399 € |
| Gehäuse | 3D-Druck | 3D-Druck | Aluminium |
| Akku | ✗ | ✗ | ✓ |
| Smartcard | ✗ | 2× | 2× |
| QR-Scanner | ✓ | ✓ | ✓ |

### Smartcard-Speicherung

Die optionale Smartcard speichert die Seedphrase verschlüsselt auf einem Secure Chip. Sie muss bei ausgeschaltetem Gerät mit der Chip-Seite nach innen bis zum Anschlag eingesteckt sein. Der PIN schützt den Zugriff; nach 10 Falscheingaben ist die Karte dauerhaft gesperrt. Gerät und Smartcard haben unabhängige PINs — mindestens 6 Stellen werden empfohlen.

Zwei Verschlüsselungsmodi stehen zur Wahl: **Plain Text** ermöglicht die Wiederherstellung auf einem beliebigen anderen Specter-Gerät (mehr Flexibilität, besser als Backup-Karte geeignet). **Encrypted** koppelt die Smartcard an dieses spezifische Gerät; zusätzlich zur Seedphrase werden weitere Wallet-Informationen verschlüsselt (maximale Sicherheit, aber weniger portabel — muss bei Gerätewechsel neu synchronisiert werden).

Ein besonderer Vorteil: Mehrere Smartcards mit verschiedenen Seedphrases und eigenen PINs können mit demselben Gerät genutzt werden. Das ermöglicht saubere Trennung zwischen verschiedenen Wallets (beruflich/privat, verschiedene Familienmitglieder) ohne mehrere Geräte kaufen zu müssen.

### Sicherheitsmodell

#### PIN und Anti-Phishing-Wörter

Beim ersten Start generiert das Gerät ein internes, einzigartiges Geheimnis. Dieses kombiniert sich mit dem eingegebenen PIN zu einem Entschlüsselungsschlüssel für die gespeicherten Bitcoin-Schlüssel. Für jede eingegebene PIN-Ziffer erscheinen am Bildschirm spezifische Wörter — diese sind einzigartig für jede Gerät/Smartcard-Kombination und verändern sich bei manipulierter Firmware, Smartcard oder Hardware. Wer die Anti-Phishing-Wörter kennt und prüft, erkennt jede Manipulation sofort. Beim ersten Start notieren, bei jedem Start überprüfen.

#### Entropie-Generierung

Die Seedphrase-Erzeugung kombiniert mehrere Quellen: den True Random Number Generator (TRNG) des Mikrocontrollers, Touchscreen-Eingaben (Position und Timing in Mikroprozessor-Ticks bei 180 MHz) und optional die eingebauten Mikrofone. Die kombinierte Entropie ist immer besser als jede einzelne Quelle. Alternativ lässt sich die Seedphrase durch Münzwürfe aus der realen Welt erzeugen — prüfbar gegen die BIP-39-Wörterliste, ohne jedem internen Zufallsalgorithmus vertrauen zu müssen.

#### Air-Gap-Kommunikation

Das Gerät kommuniziert nach dem initialen Firmware-Flashen (Micro-USB) ausschließlich über QR-Codes und SD-Karte. USB ist optional, wird aber von Specter nicht empfohlen. Diese Architektur hat zwei Vorteile gegenüber USB: Der genaue Datenaustausch ist für jeden sichtbar und verifizierbar, und die Angriffsfläche (Datenmenge und Kommunikationsfrequenz) wird reduziert.

Der PSBT-Signing-Ablauf läuft so: Die Software-Wallet erstellt eine unsignierte Transaktion, zeigt sie als QR-Code. Das Specter-Gerät scannt, zeigt alle Details auf dem 4-Zoll-Touchscreen (Empfängeradresse, Betrag, In- und Outputs, Locktime, nSequence, Replace-by-Fee), der Nutzer bestätigt. Das Gerät zeigt die signierte Transaktion als QR-Code zurück, die Software-Wallet scannt und broadcastet.

Für die Adressverifizierung wird der QR-Code-Inhalt `bitcoin:<address>?index=<index>` gescannt; das Gerät leitet die Adresse aus allen gespeicherten Wallet-Descriptoren ab und zeigt die passende an — inklusive Wallet-Name und Adressnummer.

Wallets werden per QR mit dem Befehl `addwallet <name>&<descriptor>` importiert. Descriptors folgen dem Bitcoin-Core-Standard, ergänzt um Miniscript-Unterstützung.

Beim PSBT-Signing: Das Gerät sendet nur die globale Transaktion und die Partial Signatures zurück — alle anderen PSBT-Felder werden entfernt, um die QR-Code-Größe zu minimieren. Die Host-Software muss die signierte PSBT mit der ursprünglichen PSBT zusammenführen. Fingerprint `00000000` in der BIP32-Derivation wird durch den echten Geräte-Fingerprint ersetzt, was die Kompatibilität mit Software-Wallets verbessert, die den Fingerprint nicht kennen.

#### USB-Befehlssatz

USB-Kommunikation läuft über menschenlesbare Klartextnachrichten (einfachere Fehlersuche als binäre Protokolle). Jeder Befehl wird mit `\r` oder `\r\n` abgeschlossen:

| Befehl | Funktion |
|---|---|
| `fingerprint` | Hex-Fingerprint des Root-Keys |
| `xpub <derivation>` | xpub am angegebenen Ableitungspfad (z.B. `xpub m/84h/1h/0h`) |
| `sign <psbt>` | Nutzer wird zur Bestätigung des PSBT aufgefordert |
| `showaddr <type> <derivation> [witness_script]` | Zeigt Adresse an; type: `wpkh`, `sh-wpkh`, `pkh`, `sh`, `sh-wsh`, `wsh` |
| `importwallet <name>&<descriptor>` | Nutzer wird zur Bestätigung der neuen Wallet aufgefordert |

USB-Kommunikation ist standardmäßig deaktiviert. Aktivierung unter **Device settings → Communication → USB communication**.

#### SD-Karte

`.psbt`- und `.txt`-Dateien auf der SD-Karte werden identisch zu USB- oder QR-Eingaben verarbeitet — sie können eine Transaktion, einen Wallet-Import-Befehl oder einen Adressverifikationsbefehl enthalten.

#### Firmware-Verifikation und Secure Boot

Firmware-Updates laufen über SD-Karte: `specter_upgrade_vX.X.X.bin` in die SD-Root legen, Gerät einschalten, Bootloader installiert automatisch. Das Gerät installiert nur Updates mit korrekter digitaler Signatur — Stepans PGP-Schlüssel signiert die `sha256.signed.txt`, gegen die der Nutzer den Hash der Binary prüft. Der Secure Boot überprüft Signaturen bei jedem Start; wird fremde Firmware aufgespielt, wird das interne Geheimnis gelöscht, was an den veränderten Anti-Phishing-Wörtern erkennbar ist. Specter ist unter den DIY-Wallets die einzige, die Secure Boot implementiert.

### Kompatible Software-Wallets

Das Gerät ist bewusst so gebaut, dass mehrere Koordinations-Apps verwendbar sind, nicht nur die eigene Specter Desktop App. Kompatibel: Sparrow Wallet (PC), Specter Desktop (PC), Nunchuk (PC/Smartphone), Bitcoin Safe (PC), Blue Wallet (PC/Smartphone), Liana Wallet (PC), Bitcoin Keeper (PC/Smartphone), Bull Bitcoin (Smartphone).

### Emergency Recovery

**Seedphrase verloren:** Risiko hoch. Neue Seedphrase auf neuer (ungenutzter) Smartcard erstellen, Bitcoin mit der alten Smartcard zur neuen Wallet übertragen, alte Smartcard bereinigen.

**Smartcard verloren:** Risiko begrenzt — Angreifer haben nur 10 PIN-Versuche. Wenn kein Zugriff durch Dritte zu befürchten: neue Smartcard mit alter Seedphrase beschreiben. Wenn Risiko besteht: wie bei verlorener Seedphrase vorgehen.

**Gerät verloren:** Risiko gering, wenn Seedphrase nicht im internen Flash gespeichert war. Neues Gerät kaufen, alte Smartcard einstecken — Wallet bleibt identisch. Bei Encrypted-Smartcard: Neusynchronisierung nötig.

**PIN verloren:** Geräte-PIN — 10× falsch eingeben für Factory Reset, dann wie Gerät verloren vorgehen. Smartcard-PIN — neue Smartcard mit alter Seedphrase, alte Smartcard durch 10× Falscheingabe sperren.

### Kritikpunkte

Die Lernkurve ist steil — das Gerät richtet sich explizit an fortgeschrittene Nutzer. Der Micro-USB-Anschluss (statt USB-C) ist ein Komfortmangel. Die Geräte sind groß und schwer verglichen mit anderen Hardware-Wallets. Die günstigeren Varianten im 3D-Druck-Gehäuse wirken wie Prototypen. Wer das Gerät fertig kauft, muss dem Zusammenbauer vertrauen. Die Firmware-Sprache ist englisch, deutschsprachige Tutorials gibt es aber.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[multisig-und-kollaborative-verwahrung]]
- [[sparrow-wallet]]
- [[wallet-backup-strategien]]
- [[firmware-verifikation-und-reproduzierbarkeit]]
- [[hardware-wallet-angriffsvektoren]]

## Open Questions

- Wie entwickelt sich der Secure-Element-Plan für den Specter? (Roadmap nennt es als offenes Thema)
- Wird die Specter Association langfristig genug Spendenvolumen für aktive Entwicklung sichern?
- Miniscript-Unterstützung im Vergleich zu anderen Wallets (Liana, BitBox02 MiniTapscript)?
