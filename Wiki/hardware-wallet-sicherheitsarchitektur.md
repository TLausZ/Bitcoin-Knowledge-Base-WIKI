# Hardware-Wallet Sicherheitsarchitektur

**Status:** established
**Themen:** protokoll, self-custody
**Last updated:** 2026-10-20
**Sources:** [[BitBox02 Bedrohungsmodell]], [[BitBox – Sicherheit auf jeder Ebene]], [[Firmware-Updates im Zeitalter von KI_ Auf dem neuesten Stand zu sein ist wichtiger denn je]], [[BitBox 08.2026 Dixence-Update]], [[20250227_worauf-man-beim-kauf-einer-neuen-hardware-wallet-achten-sollte]], [[20260312_warum-vorsichtig-sein-eine-hardware-wallet-nicht-ersetzen-kann-zero-day-schwachstellen-erklärt]], [[20250620_vorstellung-der-bitbox02-nova]], [[20250703_whisper-wie-die-sichere-bluetooth-integration-der-bitbox02-nova-funktioniert]], [[20220419_hardware-wallet-display-pflicht-de]], [[20220118_bitbox-01-2022-maighels-update-de]], [[20210906_was-bedeutet-open-source-de]], [[20210609_secure-chip-open-source-firmware-de]], [[20210317_5-fragen-hardware-wallet-sicherheit-de]], [[20210615_bitboxapp-android-de]]

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

### Physischer Schutz: Verguss, Sollbruch-Pins, Zähler
Die Herstellerseite zur Sicherheit fasst zusammen, was das Gehäuse und die Chips gegen Angriffe mit dem Gerät in der Hand leisten. Der verschlüsselte Seed auf dem Mikrocontroller braucht drei Geheimnisse: eines auf dem Secure Chip, eines auf dem Mikrocontroller und das Gerätepasswort, das nirgends gespeichert ist. Sollte ein Dieb das Zehn-Versuche-Limit des Mikrocontrollers umgehen, begrenzt ein monotoner Zähler im Secure Chip die Gesamtzahl der Passworteingaben, und die Passwortdehnung verlängert jeden Versuch. Mikrocontroller und Secure Chip sind mit einem Sicherheits-Epoxidharz vergossen, «um invasive Angriffe weiter zu erschweren»; der Secure Chip selbst ist gegen das Extrahieren von Schlüsselmaterial ausgelegt. Die beiden Gehäusehälften sind mit einem Kleber verbunden, der die Pins der oberen Hälfte beim Trennen abbrechen lässt, sodass sich das Gehäuse nicht mehr sauber schliessen lässt; die nötige Kraft hinterlässt zudem sichtbare Spuren aussen. Der Bootloader akzeptiert nur von Shift Crypto signierte Firmware, verhindert Downgrades und den Wechsel zwischen Multi- und Bitcoin-only-Edition und kann den Firmware-Hash vor dem Start anzeigen. Die USB-Verbindung ist mit dem Noise-Protokoll verschlüsselt, Malware auf dem Host sieht nur Chiffrat. Die Firmware wurde von Census Labs geprüft, ein Bug-Bounty-Programm läuft, und das Bedrohungsmodell ist veröffentlicht. Für den Lieferkettenangriff auf Ledger vom Oktober 2026, bei dem ein Mithörer an der Display-Leitung sass, heisst das: Verguss und Sollbruch-Pins erhöhen den Aufwand für einen Umbau und machen ihn sichtbar, ein Ausschluss ist das nicht, und ob die Leitung zwischen Chip und Display unter dem Verguss liegt, sagt die Seite nicht (siehe [[anti-klepto-und-supply-chain-sicherheit]]). [[BitBox – Sicherheit auf jeder Ebene]]

### Das Bedrohungsmodell: was drin ist und was nicht
Shift Crypto veröffentlicht für die BitBox02 ein technisches Bedrohungsmodell (nur auf Englisch). Es schützt gegen Angreifer, die ohne Zwang Coins stehlen, Verluste verursachen oder die Privatsphäre verletzen wollen, ohne das Gerät vorher zu entsperren. Ausserhalb des Modells liegen Denial-of-Service, der Fall, dass ein Angreifer Gerät und Passwort oder das Backup besitzt, und ausdrücklich der Fall, dass der Nutzer ein manipuliertes Gerät mit seinem Passwort entsperrt: «if you unlock a tampered device with your device password, the attacker is likely to succeed. Such targeted attacks are out of scope.» Das Gehäuse ist mit Epoxid auf die Platine geklebt, um Manipulation zu erschweren, und der Nutzer soll das Gerät vor jeder Nutzung auf Spuren prüfen; mit genug Aufwand hält das Modell Evil-Maid-Angriffe für machbar. Ein verlorenes oder gestohlenes Gerät fällt dagegen in den Schutzumfang. Für den Ledger-Lieferkettenangriff von 2026 heisst das: Ein Umbau zwischen Werk und Kunde, den der Nutzer dann einrichtet, ist auch für die BitBox kein Szenario, gegen das der Hersteller Schutz verspricht; die Attestation prüft die Echtheit des Secure-Chip-Schlüssels, nicht das Fehlen angelöteter Bauteile. Der Rat des Modells ist derselbe wie nach dem Ledger-Fall: Wallet immer selbst einrichten, weil ein Mitarbeiter oder Reseller sonst ein Gerät mit bekanntem Seed liefern könnte. [[BitBox02 Bedrohungsmodell]]

Innerhalb des Modells zählt die Seite die Gegenmassnahmen auf. Gegen Firmware-Bugs: Stack-Smashing-Schutz, möglichst viele Speicherbereiche per MPU nicht ausführbar, Booleans als zwei feste Integerwerte, Debug-Schnittstellen ab Werk abgeschaltet, Bootloader schreibgeschützt, Secure Chip unumkehrbar konfiguriert, die volle API erst nach dem Entsperren (nur die Echtheitsprüfung davor). Gegen invasive Angriffe nimmt das Modell an, dass ein Angreifer den Mikrocontroller entkapseln und auslesen oder Bauteile tauschen kann, nachdem der Nutzer das Gerät nicht mehr benutzt; die Kombination aus Passwort, Mikrocontroller-Geheimnis und Secure-Chip-Geheimnis macht den ausgelesenen Seed wertlos, und Mikrocontroller und Secure Chip authentisieren und verschlüsseln ihre Kommunikation mit Werksschlüsseln. Gegen Seitenkanäle setzt BitBox auf Constant-Time-Bibliotheken; die theoretische Schwachstelle über den Stromverbrauch des OLED-Displays ist bei der Nova durch Filterung entschärft. Gegen Evil Maid: Echtheitsprüfung vor jeder Nutzung, dazu merken sich Gerät und App ihre Gegenstelle (bis zu fünf Pairings), ein erneutes Pairing ist ein Warnsignal. Gegen Brute-Force bricht der monotone Zähler des Secure Chips den Chip bei Dauerraten. Auf der Computerseite: Passwort nur am Gerät, Hash und Signatur der BitBoxApp veröffentlicht, USB mit Noise_XX_25519_ChaChaPoly_SHA256 verschlüsselt und per Pairing-Code gegen Man-in-the-Middle gesichert, Warnung vor Clipboard-Hijacking. Auf der Serverseite lädt die App alle Blockheader von Bitcoin und Litecoin und prüft per SPV, dass die Coins existieren; ein eigener Backend-Server macht unabhängig. In der Lieferkette: Entropie der beiden TRNGs könnte vom Chiphersteller hintertürt sein, deshalb die Mischung mit Werkswert, Host-Entropie und Passwort; jede Firmware wird von mehreren Ingenieuren signiert, kein Single Point of Failure; weil Mitarbeiter einen bösartigen Bootloader einschleusen könnten, liefert die Firmware dessen Hash bei der Echtheitsprüfung mit; und falls ein Staat oder eine kriminelle Organisation Shift Crypto zwingt, eine Firmware nur für einen Nutzer zu signieren, lässt sich der Bootloader so einstellen, dass er den Firmware-Hash vor jedem Start zeigt, kombiniert mit deterministischen Builds. Eine Einschränkung nennt das Modell beim Anti-Klepto-Protokoll: Es gilt nur für ECDSA auf secp256k1, nicht für Schnorr-Signaturen, also nicht für Taproot. [[BitBox02 Bedrohungsmodell]]

### Drei Bedrohungstypen und was dagegen schützt

**1. Phishing und Fernangriffe:** Angreifer versuchen über das Internet, auf den Computer oder die Wallet-App zuzugreifen. Da der private Schlüssel das Gerät nie verlässt, nützt ein kompromittierter Computer einem Angreifer nichts — er kann keine Coins stehlen, solange er kein physisches Gerät hat.

**2. Physische Angriffe auf das Gerät:** Jemand stiehlt das Gerät und versucht, den Schlüssel zu extrahieren. Secure Chip und Gerätepasswort machen das erheblich schwieriger. Das Gerät setzt sich nach 10 Fehleingaben zurück. Das Backup muss deshalb physisch separat und sicher aufbewahrt werden.

**3. Supply-Chain-Angriffe:** Ein gefälschtes oder manipuliertes Gerät wird geliefert. Die Authentizitätsprüfung via Zertifikat erkennt ein gefälschtes Gerät. Open-Source-Firmware und reproduzierbare Builds stellen sicher, dass die installierte Firmware der veröffentlichten entspricht.

### Angriff über das Backup-Medium: microSD-Hijacking

Ein spezifischer Angriffsvektor richtet sich nicht gegen die Transaktion, sondern gegen die Initialisierung: Ein Angreifer platziert ein kompromittiertes Backup auf einer microSD-Karte, bevor das Gerät eingerichtet wird. Kombiniert mit einer bösartigen Version der Wallet-App kann das Setup so getarnt werden, dass der Einrichtungsassistent eine neue Wallet zu erstellen scheint — im Hintergrund aber ein vorhandenes Backup wiederherstellt.

Dieser Angriff erfordert physischen Zugang zur microSD vor dem Setup und eine kompromittierte App. Das Display der Hardware-Wallet schützt davor: Ein korrektes Gerät zeigt beim Wiederherstellen eines Backups explizit an, dass es sich um eine Wiederherstellung handelt — nicht um eine Neueinrichtung. Der Nutzer muss das auf dem Gerätedisplay bestätigen. Eine Manipulation durch die App ist damit erkennbar.

### Firmware-Schwachstellen in der Praxis: das Dixence-Update (August 2026)

Wie eine Herstellerreaktion auf gefundene Schwachstellen aussieht, zeigt das BitBox-Update vom 17. August 2026 (Firmware 9.26.5). Bei einer internen Prüfung der gesamten Codebasis, teils unter Einsatz von KI-Modellen, fand das Entwicklerteam drei Sicherheitsprobleme und legte sie offen. Für keines davon gibt es Berichte über eine Ausnutzung oder gestohlene Nutzergelder (Stand: August 2026).

**Bootloader-Schwachstelle**, behoben bereits in Version 9.26.3 (Oeschinen-Update, Juli 2026): Ein Angreifer hätte einen Nutzer dazu bringen können, manipulierte Firmware auf einer echten BitBox02 zu installieren. Voraussetzung wäre ein vorgängig erfolgreicher Phishing-Angriff gewesen, etwa über eine gefälschte BitBoxApp, dazu das Entsperren des Geräts durch den Nutzer. Zuerst intern entdeckt, später unabhängig von einem externen Sicherheitsforscher gemeldet. Die BitBox02 Nova ist wegen des Alters der betroffenen Bootloader-Versionen nicht betroffen; die BitBox02 bis einschliesslich Firmware 9.26.1.

**Speicherverwaltungsfehler der Multi-Edition**, behoben in 9.26.5: Ausnutzbar an einem Gerät, auf dem noch keine Wallet eingerichtet ist und das an einem manipulierten Endgerät hängt. Erfolgreich ausgenutzt hätte er beliebige Codeausführung erlaubt und damit auch das Aufspielen manipulierter Firmware. Die Bitcoin-only Firmware enthält den betroffenen Code nicht. Betroffen: Multi-Edition von BitBox02 und BitBox02 Nova bis einschliesslich 9.26.4.

**Fehler in der Silent-Payments-Implementierung**, behoben in 9.26.5: Ein Angreifer hätte Coins an eine unbeabsichtigte Zahlungsadresse binden können. Direkter Diebstahl war nicht möglich, doch die Wiederherstellung hätte seine Mitwirkung erfordert, was sich für einen Erpressungsversuch eignet. Betroffen: BitBox02 und Nova ab 9.21.0 bis einschliesslich 9.26.4, sofern zusammen mit einem manipulierten Endgerät eine Transaktion an eine Silent-Payment-Adresse erstellt wurde.

Über den Einzelfall hinaus sind zwei Dinge bemerkenswert. Alle drei Angriffe setzen ein manipuliertes Endgerät oder eine gefälschte App voraus; die Hardware-Wallet allein hebelt keiner von ihnen aus. Und BitBox meldet eine Rekordzahl externer Sicherheitsmeldungen, viele davon mit KI-Modellen erzeugt. Firmware aktuell zu halten wird damit zum laufenden Aufwand statt zur einmaligen Einrichtung. [[BitBox 08.2026 Dixence-Update]]

Den Hintergrund liefert ein BitBox-Beitrag vom August 2026: KI-Werkzeuge analysieren grosse Codebasen in Stunden, fuzzen Schnittstellen in grossem Massstab und decken ganze Fehlerklassen auf, die früher Wochen Handarbeit brauchten; Sicherheitsteams, unabhängige Forscher und Bug-Bounty-Teilnehmer setzen sie bereits ein. Das Oeschinen-Update vom Juli 2026 enthielt Korrekturen für eine Reihe von Bugs, die externe Forscher und interne Audits mit KI-Hilfe gefunden hatten. Die Kehrseite: Eine Korrektur schützt erst nach der Installation, und weil Details zu Lücken üblicherweise nach dem Update veröffentlicht werden, läuft auf alter Firmware Code mit bekannten, dokumentierten Problemen. Ein Gerät ist so sicher wie sein letztes Update, und die Spanne zwischen Entdeckung und allgemeinem Verständnis einer Lücke schrumpft. Gegen die Scheu vor dem Update führt der Beitrag drei Schutzebenen an: Nur signierte Firmware wird akzeptiert, der Seed bleibt beim Update unverändert, und das Backup fängt ein fehlgeschlagenes Update ab. Die empfohlene Routine: Gerät herausholen, zuerst auf Updates prüfen, dann erst signieren; Updates nur über offizielle Kanäle, Release Notes lesen, Version danach kontrollieren. In der BitBoxApp zeigt ein roter Punkt auf dem Einstellungssymbol ein verfügbares Update an, die Firmware steckt in der App selbst. Dazu die Warnung, dass Phishing-Kampagnen sicherheitsbezogene Meldungen nutzen, um Angst und Zeitdruck zu erzeugen; kein Hersteller fragt je nach den Wiederherstellungswörtern. [[Firmware-Updates im Zeitalter von KI_ Auf dem neuesten Stand zu sein ist wichtiger denn je]]

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
- [[diceware-und-seed-generierung]]
- [[hardware-wallet-einstieg]]
- [[airgap-und-kommunikationskanaele]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[bitbox02-features]]
- [[bitcoin-entropy-rng]]
- [[bitcoin-kaufen-und-dca]]
- [[bitcoin-only-vs-multi-edition]]
- [[seedphrase-entropie-und-sicherheit]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie entwickeln sich die Sicherheitsstandards für Hardware-Wallets mit Bluetooth/NFC?
- Sind EAL6+-zertifizierte Chips ein signifikanter Vorteil gegenüber EAL5+?
- Liegt bei der BitBox02 die Leitung zwischen Mikrocontroller und Display unter dem Epoxid-Verguss? Das Bedrohungsmodell beantwortet das indirekt: Das Gehäuse ist auf die Platine geklebt, ein Umbau soll sichtbar werden, aber ein manipuliertes Gerät, das der Nutzer entsperrt, liegt ausserhalb des Schutzumfangs. Die Leitung selbst wird nicht genannt.
- Wann bekommt Anti-Klepto eine Schnorr-Variante, damit auch Taproot-Signaturen gegen Nonce-Kanäle geschützt sind?
