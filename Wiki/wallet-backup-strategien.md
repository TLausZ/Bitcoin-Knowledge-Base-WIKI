# Wallet-Backup-Strategien

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20250123_wie-du-backups-deiner-wallet-sicher-erstellst-und-verwahrst]], [[20260226_warum-die-bitbox-dich-nicht-zwingt-deine-seedphrase-aufzuschreiben]], [[20250828_lerne-deine-seedphrase-nicht-auswendig]], [[20210305_bitcoin-backups-grundlagen-fehler-de]], [[20210309_bitcoin-backups-sichern-4-methoden-de]], [[20210524_bitcoin-vererben-erben-de]], [[20210618_steelwallet-bitcoin-backup-ewigkeit-de]]

## Summary

Das Wallet-Backup — die 12 oder 24 Wiederherstellungswörter nach BIP-39 — ist der eigentliche Besitz der Bitcoin, nicht die Hardware-Wallet. Es bleibt dauerhaft gleich und muss offline und sicher aufbewahrt werden. Gängige Backup-Methoden sind Papier, microSD-Karten und Edelstahl, mit unterschiedlichen Trade-offs bei Komfort, Robustheit und Fehleranfälligkeit. Das Backup im Gedächtnis zu halten ist als alleinige Strategie ungeeignet.

## Body

### Bitcoin ist Information

Private Schlüssel sind sehr große Zahlen, bequem als englische Wörter (BIP-39) kodiert. Die Wiederherstellungswörter sind ein Generalschlüssel: Aus ihnen lassen sich alle Konten, Adressen und privaten Schlüssel der Wallet ableiten. Das Backup bleibt immer gleich — man muss es nur einmal sichern.

### Backup-Methoden im Vergleich

**Papier**
Einfach, günstig, keine Technik nötig. Wichtig: richtige Reihenfolge, nummeriert, Bleistift auf qualitätsvollem Papier. Risiken: Wasser, Feuer, Unleserlichkeit über Zeit. Empfehlung: Laminierung oder robuste Backup-Karten.

**MicroSD-Karte**
Die BitBox02 erstellt automatisch ein Backup auf der mitgelieferten microSD-Karte. Vorteile: fehlerfrei, sofort, BIP-39-kompatibel, mehrere Kopien möglich. Nachteile: nicht gut gegen Feuer/Wasser geschützt. Das Backup ist unverschlüsselt — vergleichbar mit analogen Backup-Methoden. Empfehlung: Immer auch ein analoges Backup ergänzen.

**Edelstahl**
Für wachsende Bestände. Gravieren oder Stanzen der Wörter in Edelstahl bietet maximalen Schutz gegen Feuer, Wasser, physische Kraft. Die Steelwallet von Shift Crypto besteht aus Edelstahl und wurde von Jameson Lopp in einem umfassenden Belastungstest mit Bestnote bewertet (Feuer, Wasser, Korrosion, mechanische Kraft). Aufwändiger als Papier, aber in der Langlebigkeit überlegen.

### Was man vermeiden sollte

**Gedächtnis als einzige Methode:** Das menschliche Gedächtnis ist für zufällige 12–24 Wörter ohne Bedeutungskontext ungeeignet. Digitspan-Tests zeigen eine durchschnittliche Kapazität von ~7 Ziffern; 24 Wiederherstellungswörter entsprechen ~80 Ziffern. Zusätzlich besteht immer das Risiko von Unfällen mit Gedächtnisausfall. Als *Ergänzung* zu physischen Backups kann das Auswendiglernen sinnvoll sein (z.B. für Flucht-Szenarien), nie als Hauptstrategie.

**„Don't roll your own crypto":** Selbst ausgedachte Verschlüsselungs- oder Versteckmethoden führen regelmäßig dazu, dass Nutzer sich aus ihrem eigenen Backup aussperren.

### Warum ein Backup dauerhaft gilt (HD-Wallet-Mechanismus)

Moderne Wallets sind "hierarchisch deterministisch" (HD). Alle Adressen, privaten Schlüssel und Konten werden von einem einzigen Geheimnis — dem Seed — deterministisch abgeleitet. "Deterministisch" bedeutet: Aus demselben Seed entstehen immer dieselben Adressen, in derselben Reihenfolge. Nach einer Wiederherstellung berechnet die Wallet einfach alle Adressen neu und fragt die Blockchain nach Transaktionen ab.

Konsequenz: Ein einziges Backup reicht dauerhaft. Man muss es nicht nach jeder Transaktion erneuern.

### Fünf häufige Backup-Fehler

**Fehler 1: Kein Backup erstellen.** Verlust des Geräts ohne Backup = Verlust der Coins. Kein Hersteller, kein Support kann helfen.

**Fehler 2: Glauben, das Backup müsse regelmäßig aktualisiert werden.** Falsch — einmal reicht dauerhaft.

**Fehler 3: Backup auf dem Computer eingeben.** Wer die Wiederherstellungswörter in ein digitales Gerät eingibt, riskiert Diebstahl durch Malware. Auch Screenshots, Cloud-Speicher und Fotos sind tabu. Für Wiederherstellung immer die Hardware-Wallet selbst nutzen (Wörter direkt ans Gerät eingeben).

**Fehler 4: Backup nicht physisch absichern.** Das Backup ist unverschlüsselt. Wer es findet, kann alle Coins stehlen — ohne das Gerät. Die physische Sicherheit des Backups ist wichtiger als die des Geräts. Geeignete Aufbewahrung je nach Betrag: verschlossene Schublade, privater Safe, Bankschliessfach.

**Fehler 5: Backup nicht überprüfen.** Einmal im Jahr verifizieren. Mit der BitBox02: microSD-Karte einstecken und Integrität in der BitBoxApp prüfen.

### Sicherheit erhöhen: vier etablierte Methoden

**Methode 1: Sicherer Aufbewahrungsort.** Backup in versiegeltem Umschlag mit unauffälliger Beschriftung (kein "Bitcoin"). Manipulationssichere Sicherheitstaschen ermöglichen, unbemerkte Zugriffe zu erkennen.

**Methode 2: BIP-39 Passphrase.** Ein zusätzliches Passwort erzeugt eine vollständig neue, unabhängige Wallet. Backup und Passphrase werden getrennt aufbewahrt; beide werden für den Zugriff benötigt. Vorteile: Sehr starker Schutz. Nachteile: Die Passphrase wird nie dauerhaft gespeichert, muss bei jeder Entsperrung eingegeben werden; keine Prüfsumme (ein Tippfehler erzeugt eine leere Wallet); beide Elemente müssen sicher aufbewahrt werden. Empfehlung: Feature für fortgeschrittene Nutzer.

**Methode 3: 2-von-3-Wortaufteilung.** Drei Karten erstellen, von denen jede 16 der 24 Wörter enthält (8 pro Karte fehlen) — so dass je zwei Karten alle 24 Wörter ergeben. An drei verschiedenen Orten aufbewahren. Vorteile: Fehlertoleranz (eine Karte verlieren ist kein Problem), ~80 Bits Entropie pro Karte (nicht durch Brute-Force knackbar). Nicht zu verwechseln mit der unsicheren Methode "12+12": Diese hat zwar ausreichende Entropie, aber keine Fehlertoleranz.

**Methode 4: Multisig.** Mehrere Hardware-Wallets für eine Wallet. Theoretisch am sichersten für grosse Beträge. Wichtig: Das Multisig-Backup muss zusätzlich zu den regulären Seeds auch Unterzeichneranzahl, Skripttyp, Ableitungspfad und alle Extended Public Keys (xpubs) aller Geräte enthalten — und diese müssen auf den Geräten selbst verifiziert werden.

**Warum kein verschlüsseltes Backup?** Die BitBox01 hatte verschlüsselte Backups. Ergebnis: Einige Nutzer vergaßen das Backup-Passwort und verloren dauerhaft Zugang zu ihren Coins. Die Kombination aus Gerätepasswort + Backup-Passwort + optionaler Passphrase ist zu komplex für die meisten Nutzer. Wer eine zweite Sicherheitsebene will, sollte die Passphrase verwenden, nicht Backup-Verschlüsselung.

### Vererbungsplanung

Wenn niemand weiß, dass man Bitcoin besitzt, oder niemand das Backup findet, sind die Coins effektiv verloren. Ein strukturierter Vererbungsplan löst das.

**Der "Brief an meine Lieben"** (nach Pamela Morgan, Autorin von "Cryptoasset Inheritance Planning"): Ein Brief, der keine Geheimnisse enthält, aber erläutert, dass Bitcoin-Vermögen existiert und wo Backups zu finden sind. Niemand, der den Brief liest, kann damit direkt Coins stehlen — aber Erben wissen, was zu tun ist.

**Inventar ohne Geheimnisse:** Notieren, wo Backups aufbewahrt werden — nicht die Beträge (veralten schnell) und nicht die Wörter selbst. Inventar für jedes Wallet: Gerät, App, Ort der Zugangsinformationen.

**Vertrauenswürdige Kontakte:** Mindestens zwei Personen benennen, die Erfahrung mit Bitcoin haben und sich gegenseitig nicht kennen. Beim Zugriff auf das Erbe sollten mindestens zwei dieser Personen anwesend sein und jeden Schritt unabhängig überwachen.

**Komplexität ist der Feind.** Erben sind oft unerfahren. Ein einfaches, gut dokumentiertes Setup ist besser als ein maximal sicheres, das niemand versteht. Shamir's Secret Sharing ist zuverlässig, aber die sichere Wiederherstellung ist anspruchsvoll (komplett offline). Multisig ist sicher, aber fehleranfällig für Unkundige.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[bip-85-child-keys]]
- [[opsec-und-privatsphaere]]
- [[diceware-und-seed-generierung]]
- [[optionale-passphrase]]
- [[multisig-und-kollaborative-verwahrung]]

## Open Questions

- Wie weit verbreitet sind Edelstahl-Backups unter erfahrenen Bitcoin-Nutzern?
- Ab wann lohnt sich Shamir's Secret Sharing gegenüber der einfacheren 2-von-3-Wortaufteilung?
