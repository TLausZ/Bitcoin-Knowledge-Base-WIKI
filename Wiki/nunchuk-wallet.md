# Nunchuk Wallet

**Status:** established
**Last updated:** 2026-06-09
**Sources:** [[2026-06-09_nunchuk-faq]], [[The Definitive Guide to Bitcoin Inheritance (2026)]], [[Recover a Miniscript wallet with Bitcoin Core (2026)]], [[Recover a Nunchuk Wallet with Sparrow (2026)]]

## Summary

Nunchuk ist eine Bitcoin-only Multisig-Wallet für iOS, Android und Desktop, die auf offenen Standards (BIP39, BSMS, Miniscript) aufbaut. Das Kernmerkmal: Im Assisted-Multisig-Modus hat das Smartphone keine Signing-Berechtigung — es ist reines Watch-Only-Interface, alle Schlüssel sind kalt. Nunchuk bietet zwei Inheritance-Protokolle (on-chain autonom via Miniscript, off-chain flexibel via Plattform) und ist von Haus aus interoperabel mit Sparrow und Bitcoin Core.

## Body

### Architektur: Assisted Multisig

Im bezahlten Plan ("Honey Badger", "Premier") läuft Nunchuk im **Assisted Multisig**-Modus:
- Das Smartphone hat **keine** Hot Keys — es ist Watch-Only
- Alle Schlüssel sind kalt (Hardware Wallets)
- Das Smartphone koordiniert Transaktionen (PSBTs), signiert aber selbst nicht
- Wallet-Wechsel erfordert keine Seed-Migration

Im kostenlosen Plan können Hot Keys auf dem Gerät erstellt werden — weniger sicher, aber ohne Hardware-Wallet nutzbar.

### Datenschutz

Nunchuk sammelt nur E-Mail-Adressen. Kein Name, keine Adresse, keine KYC. Datenlöschung über "Account Settings > Delete Account". Zusätzliche Privacy-Features: End-to-End-verschlüsselte Nachrichten, Primary Key Accounts, Inheritance-Plan ohne Identitätsnachweis.

### Interoperabilität: BSMS und offene Standards

Nunchuk nutzt BSMS (Bitcoin Secure Multisig Setup) für Wallet-Beschreibungen. Das bedeutet:

- **Recovery mit Sparrow**: BSMS-Datei + Schlüssel-Backups → Sparrow erkennt die Multisig-Konfiguration
- **Recovery mit Bitcoin Core**: Miniscript-Descriptors werden direkt von Bitcoin Core verstanden
- Keine proprietären Formate — kein Lock-in zu Nunchuk

### Inheritance: The Sovereignty Paradox

Das "Sovereignty Paradox": Bitcoin bietet echte digitale Souveränität ("Not your keys, not your coins"), aber das schafft ein Vererbungsproblem:

- Schlüssel jetzt teilen → erhöhtes Diebstahlsrisiko zu Lebzeiten
- Schlüssel zu gut verstecken → Erben finden sie nicht
- Firmen vertrauen → Gegenparteirisiko und potenzielle staatliche Eingriffe

Nunchuk löst das mit zwei Protokollen:

**On-Chain (Autonomous) Protocol**:
- Timelock wird direkt vom Bitcoin-Netzwerk via Miniscript durchgesetzt
- Ausführung ist autonom — funktioniert auch wenn Nunchuk nicht mehr existiert
- Parameter sind nach Einrichtung unveränderlich
- Empfehlung: langer Timelock (5–10 Jahre), da Änderungen Wallet-Migration erfordern
- Recovery: Seed Phrase des Inheritance Key genügt

**Off-Chain (Flexible) Protocol**:
- Timelock wird von Nunchuk-Plattform durchgesetzt
- Datum kann jederzeit ohne Fund-Migration geändert werden
- Empfehlung: Rolling-Short-Timelock (1–3 Jahre, jährlich verlängern)
- Recovery: Backup Password (entschlüsselt Key-Backup auf Plattform)

**Kosten**:
- Einrichtung im Honey Badger / Premier Plan inkludiert
- Smooth Path (geführte Vererbung): kostenlos solange Abo aktiv; 0,3% bei abgelaufenem Abo
- Failsafe (autonome Recovery): immer kostenlos (nur Bitcoin-Netzwerk-Gebühren)

### Recovery ohne Nunchuk

**Miniscript + Bitcoin Core**:
1. BSMS-Datei exportieren
2. Bitcoin Core mit Miniscript-Support starten
3. Descriptor importieren — Bitcoin Core erkennt alle UTXOs

**Multisig + Sparrow**:
1. BSMS-Datei in Sparrow importieren
2. Alle Hardware-Wallet-Schlüssel anschließen
3. Sparrow rekonstruiert die Multisig-Wallet vollständig

Beides funktioniert unabhängig von Nunchuk-Servern.

### Hardware-Wallet-Unterstützung

Nunchuk unterstützt gängige Hardware Wallets für Multisig-Setups. Neue Gerätetypen werden nach Qualitätsprüfung ergänzt. Iron Hand ist als einzelne Wallet solid, für generationelles Vermögen empfiehlt Nunchuk Honey Badger (höhere Sicherheitskonfiguration + Inheritance).

## Related

- [[multisig-und-kollaborative-verwahrung]]
- [[miniscript-und-liana]]
- [[bitcoin-vererbung]]
- [[sparrow-wallet]]
- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Wie verhält sich Nunchuk bei einem Unternehmensausfall im Off-Chain-Protokoll — gibt es ein öffentlich dokumentiertes Recovery-Verfahren?
- Welche Miniscript-Konstrukte nutzt Nunchuk intern für das On-Chain-Protokoll?
- Ist der Nunchuk-Code vollständig open source, oder nur der Client?
