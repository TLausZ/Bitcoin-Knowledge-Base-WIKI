# Hardware-Wallet Sicherheitsarchitektur

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20250227_worauf-man-beim-kauf-einer-neuen-hardware-wallet-achten-sollte]], [[20260312_warum-vorsichtig-sein-eine-hardware-wallet-nicht-ersetzen-kann-zero-day-schwachstellen-erklärt]], [[20250620_vorstellung-der-bitbox02-nova]], [[20250703_whisper-wie-die-sichere-bluetooth-integration-der-bitbox02-nova-funktioniert]], [[20220419_hardware-wallet-display-pflicht-de]], [[20220118_bitbox-01-2022-maighels-update-de]], [[20210906_was-bedeutet-open-source-de]], [[20210609_secure-chip-open-source-firmware-de]], [[20210317_5-fragen-hardware-wallet-sicherheit-de]], [[20210615_bitboxapp-android-de]]

## Summary

Eine Hardware-Wallet speichert private Schlüssel offline und isoliert sie vom vernetzten Gerät (Computer, Smartphone). Diese Trennung schützt auch gegen Zero-Day-Exploits und Zero-Click-Angriffe, bei denen ein Gerät ohne jede Nutzerinteraktion kompromittiert werden kann. Vier Kernkriterien für gute Hardware-Wallets: eigenes Display, Open-Source-Firmware, Secure Chip, BIP-39-kompatibler Backup-Standard.

## Body

### Warum Hardware-Wallets nötig sind

Smartphones und Computer sind komplexe Systeme mit Millionen Zeilen Code. Selbst gepflegte, aktuelle Geräte können **Zero-Day-Schwachstellen** enthalten — unbekannte Sicherheitslücken, für die noch kein Patch existiert. Solche Lücken können durch **Zero-Click-Exploits** ausgenutzt werden: Der Angreifer schickt speziell präparierte Daten ans Gerät, die beim automatischen Verarbeiten (Push-Benachrichtigung, Messenger-Vorschau) ausgeführt werden — ohne dass der Nutzer überhaupt auf etwas klickt. Das bekannteste Beispiel ist die Pegasus-Spyware, die über iMessage-Schwachstellen installiert wurde.

Eine Hardware-Wallet geht von Beginn an davon aus, dass das verbundene Gerät kompromittiert sein könnte, und isoliert deshalb die privaten Schlüssel. Selbst wenn ein Computer vollständig übernommen wurde, sind die Coins sicher — der Angreifer kann den Computer kontrollieren, aber nicht die Schlüssel.

### Vier Kernkriterien

**1. Eigenes Display**
Das wichtigste Merkmal. Das verbundene Gerät (Computer, Smartphone) muss aus Sicherheitssicht als potenziell kompromittiert gelten. Ohne eigenes Display muss der Nutzer darauf vertrauen, dass das verbundene Gerät die richtigen Transaktionsdetails anzeigt. Ein böswilliges Programm kann optisch wie die authentische Wallet-App aussehen und sich auch so verhalten — aber anstatt die beabsichtigte Empfangsadresse zu erstellen, sendet es der Hardware-Wallet eine Transaktion mit einer anderen Adresse. Da die Wallet ohne Display nicht selbst prüfen kann, was sie signiert, signiert sie blind.

Das Display der Hardware-Wallet ist unabhängig vom Host-Gerät: Es zeigt genau die Daten, die tatsächlich signiert werden, und fordert eine explizite Bestätigung durch den Nutzer (Tastendrücke am Gerät). Kein bösartiges Programm auf dem Computer kann manipulieren, was das Display der Wallet anzeigt.

**BitBox01 als historische Lektion:** Die erste BitBox-Generation hatte kein eigenes Display und nutzte stattdessen eine Smartphone-App als "sicheren Remote-Bildschirm" über einen verschlüsselten Kanal. Dieses System war komplex und hatte einen fundamentalen Schwachpunkt: Wenn der verschlüsselte Kanal zwischen Host-Computer und Smartphone kompromittiert wurde, reichte es aus, nur den Computer anzugreifen, um Transaktionen zu manipulieren. Damit war der Sicherheitsvorteil gegenüber einer reinen Software-Wallet eliminiert. Die BitBox02 wurde deshalb mit einem OLED-Display ausgestattet.

**2. Open-Source-Firmware**
Open-Source bedeutet, der Quellcode ist öffentlich zugänglich und von jedem einsehbar und kompilierbar. Das macht Auditierbarkeit möglich: Sicherheitsforscher, Entwickler und neugierige Nutzer können den Code auf Schwachstellen und bösartige Bestandteile prüfen. Bei einer Hardware-Wallet ist das besonders kritisch — niemand sollte dem Hersteller blind vertrauen müssen.

Das Gegenteil ist "Sicherheit durch Verschleierung" (Security through Obscurity): Der Code ist geheim, deshalb findet ihn niemand. Das funktioniert nur so lange, bis ein motivierter Angreifer ihn trotzdem analysiert. Open-Source-Software gilt allgemein als robuster, weil die Anreize für saubere Architektur und gute Dokumentation höher sind. Fehler werden schneller gefunden und behoben.

Ein direktes Gegenbeispiel: Ledger-Geräte enthalten Closed-Source-Software auf dem Sicherheitschip, weil der Chip-Hersteller keine Veröffentlichung erlaubt. Nutzer müssen dort dem Hersteller vertrauen, dass die kritische Schlüsselverwaltung korrekt implementiert ist.

Reproduzierbare Builds gehen noch weiter: Der Nutzer kann verifizieren, dass die installierte Firmware exakt aus dem veröffentlichten Quellcode kompiliert wurde — gleicher Code ergibt immer dieselbe Binärdatei. Damit kann niemand — auch nicht der Hersteller — heimlich veränderte Firmware ausliefern. Siehe auch [[firmware-verifikation-und-reproduzierbarkeit]].

**3. Secure Chip**
Schützt gegen physische Angriffe. Auch wenn jemand eine Hardware-Wallet findet und stiehlt, soll er die privaten Schlüssel nicht aus dem Gerät auslesen können. Der Secure Chip ist auf kryptografische Operationen spezialisiert und bietet physische Schutzmechanismen (Tamper Detection, Hardware-Zähler für Entsperrversuche).

*Problem:* Secure Chips sind oft proprietär und nicht vollständig Open-Source. Die **Dual-Chip-Architektur** löst das: Eine Open-Source-MCU läuft parallel zum Secure Chip. Dem Secure Chip wird nicht blind vertraut — er wird nur für physischen Schutz genutzt, während die transparente Firmware die Logik übernimmt.

**4. BIP-39-Backup**
Die privaten Schlüssel müssen als Standard-Backup (12 oder 24 englische Wiederherstellungswörter nach BIP-39) gesichert werden können. So ist der Nutzer nicht vom Hersteller abhängig: Jede andere BIP-39-kompatible Wallet kann die Coins wiederherstellen.

### Secure Chip: Wie die Dual-Chip-Architektur funktioniert

Generische Mikrocontroller (MCUs) sind auf Leistung und Kosten optimiert, nicht auf physische Angriffe. Mit spezialisiertem Equipment lässt sich der Inhalt eines MCU-Flash-Speichers direkt auslesen — durch Entkapseln des Chips mit Laser oder Säure. Solche Dienste sind kommerziell verfügbar.

Secure Chips sind auf genau diese Angriffe ausgelegt: Dekapselung, Sondenangriffe, Fehlerinjektion, Spannungs-Glitching, Seitenkanal-Angriffe. Das Problem: Secure Chips laufen mit proprietärem, nicht einsehbarem Code — Closed Source. Das ist ein direkter Widerspruch zur Anforderung an Open-Source-Firmware.

Die **Dual-Chip-Architektur** der BitBox02 löst den Konflikt: Die Open-Source-Firmware läuft auf der MCU. Der Secure Chip übernimmt physischen Schutz, aber erfährt keine Geheimnisse direkt. Dem Secure Chip muss nicht vertraut werden — im schlimmsten Fall (vollständige Kompromittierung des Secure Chips) sinkt die Sicherheit auf das MCU-Only-Niveau, aber die Coins sind weiterhin durch das Gerätepasswort geschützt.

**Was der Secure Chip konkret beiträgt:**

- Der Seed auf der MCU ist mit mehreren Schlüsseln verschlüsselt, darunter einem Schlüssel via Key Derivation Function (KDF) des Secure Chips. Direktes Auslesen des MCU-Flash-Speichers ergibt nutzlosen verschlüsselten Inhalt.
- Entsperrversuche werden verlangsamt — Brute-Force-Angriffe sind nicht mehr praktikabel.
- Zähler für Lifetime-Entsperrungen: Nach ~730.000 Versuchen sperrt der Secure Chip das Gerät permanent. Bei normaler Nutzung (100 Entsperrungen/Tag) entspricht das über 20 Jahren Nutzung — dieser Grenzwert wird in der Praxis nie erreicht.
- Ein echter zusätzlicher Zufallszahlengenerator (dem nicht vertraut werden muss, aber der Entropie beitragen kann).
- Speicherung eines einzigartigen Zertifikatsschlüssels für die kryptografische Authentizitätsprüfung: Die BitBoxApp verifiziert beim Anschluss, dass das Gerät ein Original ist.

**Authentizitätsprüfung im Detail:** Die BitBoxApp schickt beim Verbinden eine Zufallszahl (Challenge) ans Gerät. Das Gerät signiert sie mit dem privaten Zertifikatsschlüssel des Secure Chips und schickt die Signatur zurück. Die App verifiziert den vollständigen Zertifizierungspfad bis zur Shift-Root-CA. Schlägt die Prüfung fehl, zeigt die App eine Warnung.

### Drei Bedrohungstypen und was dagegen schützt

**1. Phishing und Fernangriffe:** Angreifer versuchen über das Internet, auf den Computer oder die Wallet-App zuzugreifen. Da der private Schlüssel das Gerät nie verlässt, nützt ein kompromittierter Computer einem Angreifer nichts — er kann keine Coins stehlen, solange er kein physisches Gerät hat.

**2. Physische Angriffe auf das Gerät:** Jemand stiehlt das Gerät und versucht, den Schlüssel zu extrahieren. Secure Chip und Gerätepasswort machen das erheblich schwieriger. Das Gerät setzt sich nach 10 Fehleingaben zurück. Das Backup muss deshalb physisch separat und sicher aufbewahrt werden.

**3. Supply-Chain-Angriffe:** Ein gefälschtes oder manipuliertes Gerät wird geliefert. Die Authentizitätsprüfung via Zertifikat erkennt ein gefälschtes Gerät. Open-Source-Firmware und reproduzierbare Builds stellen sicher, dass die installierte Firmware der veröffentlichten entspricht.

### Angriff über das Backup-Medium: microSD-Hijacking

Ein spezifischer Angriffsvektor richtet sich nicht gegen die Transaktion, sondern gegen die Initialisierung: Ein Angreifer platziert ein kompromittiertes Backup auf einer microSD-Karte, bevor das Gerät eingerichtet wird. Kombiniert mit einer bösartigen Version der Wallet-App kann das Setup so getarnt werden, dass der Einrichtungsassistent eine neue Wallet zu erstellen scheint — im Hintergrund aber ein vorhandenes Backup wiederherstellt.

Dieser Angriff erfordert physischen Zugang zur microSD vor dem Setup und eine kompromittierte App. Das Display der Hardware-Wallet schützt davor: Ein korrektes Gerät zeigt beim Wiederherstellen eines Backups explizit an, dass es sich um eine Wiederherstellung handelt — nicht um eine Neueinrichtung. Der Nutzer muss das auf dem Gerätedisplay bestätigen. Eine Manipulation durch die App ist damit erkennbar.

### BitBoxApp: Plattformübergreifende Architektur

Die BitBoxApp läuft auf Windows, macOS, Linux und Android aus einer einzigen Codebasis:

- **Go-Backend (Core Tier):** Enthält die gesamte Geschäftslogik — Kommunikation mit der BitBox02, Blockchain-Abfragen, Adressberechnung, Transaktionserstellung. Enthält keine Geheimnisse; private Schlüssel verlassen das Gerät nie.
- **React/Preact-Frontend:** Nur ein View-Layer; alle Berechnungen geschehen im Go-Backend. Läuft in QtWebEngine (Desktop) oder Android WebView (Mobil).

Die Android-Version bietet denselben vollen Funktionsumfang wie die Desktop-App: Einrichtung, Firmware-Updates, Transaktionen senden/empfangen, eigene Node-Verbindung, Tor. Auf Geräten mit USB-C kein Adapter nötig.

Diese Architektur stellt sicher, dass Code-Änderungen und Sicherheitsverbesserungen gleichzeitig auf allen Plattformen wirksam werden.

### Bluetooth und drahtlose Kommunikation

Wenn Hardware-Wallets drahtlos kommunizieren (z.B. Bluetooth für iPhone-Unterstützung), gelten besondere Anforderungen:

- **Isolierter BLE-Chip:** Bluetooth-Chip hat keinen Zugriff auf Flash-Speicher oder Wallet-Geheimnisse
- **Doppelte Verschlüsselung:** Zusätzlich zur BLE-Verschlüsselung bleibt Ende-zu-Ende-Verschlüsselung zwischen App und Firmware aktiv
- **Minimale Reichweite:** Pairing nur in unmittelbarer Nähe möglich
- **USB-Priorität:** Sobald USB verfügbar ist, wird Bluetooth deaktiviert

## Related

- [[wallet-backup-strategien]]
- [[bitbox02-nova]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Wie entwickeln sich die Sicherheitsstandards für Hardware-Wallets mit Bluetooth/NFC?
- Sind EAL6+-zertifizierte Chips ein signifikanter Vorteil gegenüber EAL5+?
