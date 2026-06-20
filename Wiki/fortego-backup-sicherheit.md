# Fortego: Backup-Sicherheit und Double Responsibility Problem

**Status:** established
**Last updated:** 2026-06-19
**Sources:** [[fortego_Das Double Responsibility Problem]], [[fortego_Die Fortego-Sicherheitsarchitektur]], [[fortego_Seed Phrase_ Die eine Regel, die keine Ausnahme kennt]]

## Summary

Das Double Responsibility Problem beschreibt das strukturelle Dilemma bei Bitcoin-Backups: Ein Seed-Backup muss gleichzeitig auffindbar (Verlustschutz) und unzugänglich (Diebstahlschutz) sein — zwei Anforderungen, die sich direkt widersprechen. Jede zusätzliche Kopie erhöht die Sicherheit gegen Verlust, vergrößert aber die Angriffsfläche. Fortego löst dieses Dilemma durch Trennung von Backup und Zugangsschlüssel (CodeBook): Wer nur eines hat, kann nichts rekonstruieren.

## Body

### Das Double Responsibility Problem

Jeder Bitcoiner mit Selbstverwahrung hat dasselbe Dilemma. Zwei Ängste, eine Quelle:

**Angst 1 — Verlust:** "Wenn das Backup jetzt weg wäre — Feuer, Wasserschaden, Umzug — wären meine Bitcoin weg."

**Angst 2 — Diebstahl:** "Was wenn jemand schon dran war und die Wallet ist leer, bevor ich es merke?"

Der Kern: 12–24 Wörter im Klartext sollen gleichzeitig *auffindbar* und *unsichtbar* sein. Das ist strukturell unmöglich ohne zusätzliche Schicht.

**Mehr Redundanz** senkt Verlustrisiko, vergrößert Angriffsfläche. **Mehr Abschottung** senkt Zugriffsrisiko, erhöht das Risiko, dass das Backup im Notfall oder Erbfall nicht mehr zugänglich ist. Man kann eine Seite verbessern — nur auf Kosten der anderen.

Fortegos Antwort: Das Backup und der Zugangsschlüssel (CodeBook) werden getrennt aufbewahrt. Wer nur das Backup findet, hat die Wörter, aber keinen Schlüssel zu ihrer Rekonstruktion. Wer nur das CodeBook findet, hat den Schlüssel, aber keine Wörter.

### Die Seed-Phrase-Grundregel (absolut)

> Jeder, der nach deiner Seed Phrase fragt, greift dich an.

Kein legitimer Dienst braucht die Seed Phrase — nicht Hardware-Wallet-Hersteller, nicht Exchanges, nicht Support, nicht Recovery-Services. Die Regel hat keine Ausnahmen.

**Typische Angriffsmuster:**
- **Fake-Wallet-Seiten** — sieht aus wie offizielle Download-Seite; enthält Eingabefeld für Recovery Phrase
- **Support-Impersonation** — angeblicher Hersteller-Support kontaktiert Nutzer; bittet um Wörter zur "Verifizierung"
- **Recovery-Scams** — verspricht, verloren gegangene Bitcoin zurückzuholen; verlangt Seed als "Beweis"
- **Browser-Erweiterungen** — legitimate aussehende Wallet-Extension; exfiltriert Seed beim Eingeben

**Was tun wenn kompromittiert:** Sofort alle Bitcoin auf eine neue Wallet (frische Seed Phrase) verschieben, bevor der Angreifer es tut.

### Fortego-Sicherheitsarchitektur

Fortego implementiert eine verwaltete Tresor-Lösung für das CodeBook mit vier technischen Säulen:

**1. Protokollierung (Audit Trail)**
Jede Änderung am CodeBook wird als neuer Eintrag protokolliert — kein stilles Überschreiben oder Löschen. Unbemerkte Manipulation wird damit sichtbar und nachvollziehbar.

**2. Verschlüsselung**
Das CodeBook liegt in Fortegos Systemen nur verschlüsselt vor. Der Entschlüsselungsschlüssel wird nicht im Klartext gespeichert, sondern über einen verwalteten Schlüsseldienst geschützt und nur im Arbeitsspeicher gehalten. Ein kompromittiertes Dateisystem oder Server-Snapshot reicht für Zugriff nicht aus.

**3. Redundante Geo-Backups**
Produktivsystem, Sicherungskopien und Wiederherstellungsweg sind bewusst getrennt. Verschiedene Anbieter, geografisch getrennte Speicherorte. Einzelner Systemausfall betrifft nicht alle Kopien. Sicherungskopien werden regelmäßig technisch verifiziert.

**4. User-controlled Freigabe**
Das CodeBook wird nur auf kontrollierte Anfrage freigegeben. Fortego kann nicht einseitig zugreifen oder freigeben; der Nutzer entscheidet.

### Einordnung im Bitcoin-Backup-Ökosystem

Fortego ist ein verwalteter Dienst — d.h. man vertraut Fortego mit dem CodeBook, ähnlich wie einem kollaborativen Verwahrer. Das ist ein bewusstes Trade-off: Weniger maximale Selbstverwahrung gegen Lösung des Double Responsibility Problems.

Vergleich mit anderen Ansätzen:

| Ansatz | Verlustrisiko | Diebstahlrisiko | Komplexität |
|---|---|---|---|
| Einzige Kopie sicher verwahrt | Hoch | Niedrig | Niedrig |
| Mehrere Kopien verteilt | Niedrig | Hoch | Mittel |
| Passphrase als zweite Schicht | Mittel | Mittel | Mittel |
| Shamir Secret Sharing (SSS) | Niedrig | Niedrig | Hoch |
| Fortego (CodeBook-Trennung) | Niedrig | Niedrig | Mittel |

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[wallet-backup-strategien]]
- [[shamir-secret-sharing]]
- [[opsec-und-privatsphäre]]
- [[biometrie-und-finanzueberwachung]]

## Open Questions

- Wie verhält sich Fortego bei einem Unternehmensausfall — gibt es ein dokumentiertes Recovery-Verfahren ohne Fortego?
- Ist die Trennung von Backup und CodeBook ausreichend, wenn beide beim selben Nutzer physisch nah liegen?
- Wie entwickelt sich der Markt für verwaltete Backup-Dienste in Europa nach MiCA und DSGVO?
