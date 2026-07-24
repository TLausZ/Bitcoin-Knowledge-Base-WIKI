# Shamir Secret Sharing

**Status:** established
**Themen:** protokoll, self-custody
**Last updated:** 2026-07-05
**Sources:** [[202606_Shamir Secret Sharing-BitcoinDevs]], [[Vorlage für «Poor Man Shamir's Secret Sharing Scheme»]], [[20251130_heartmoney-schau-hin-der-tiger-greift-an]]

## Summary

Shamir Secret Sharing (SSS) ist ein kryptografisches Verfahren, mit dem ein Geheimnis (z.B. eine Seed-Phrase) auf mehrere Anteile (Shares) aufgeteilt werden kann, sodass erst eine Mindestanzahl davon das Original rekonstruiert — mit weniger Shares erfährt man buchstäblich nichts. Der mathematische Trick: Das Geheimnis wird als Konstante in ein Polynom eingebettet, und jeder Share ist ein Punkt auf diesem Polynom. Weil zwei Punkte genau eine Gerade definieren (bei Threshold 2), reicht ein einzelner Punkt nicht aus — unendlich viele Geraden laufen durch ihn. In Bitcoin kommt SSS als Grundlage von FROST zum Einsatz.

## Body

### Das Grundproblem

Eine Seed-Phrase ist zu wichtig, um sie nur einmal zu sichern — aber mehr Kopien bedeuten mehr Diebstahlrisiko. SSS löst diesen Widerspruch: Statt mehrerer vollständiger Kopien gibt es mehrere unvollständige Shares, von denen jeder einzeln nutzlos ist.

### k-of-n Threshold

Die Stärke von SSS liegt in der frei wählbaren Schwelle:

- **2-of-3**: Ein Share kann verloren gehen — mit 2 verbleibenden ist Rekonstruktion möglich
- **5-of-5**: Zwei Shares können verloren gehen — robuster gegen Verlust
- **4-of-7**: Drei Shares können verloren gehen — maximale Redundanz

Das Threshold-Schema ist entscheidend: Ein einzelner Share verrät **mathematisch nichts** über das Geheimnis, solange die Schwelle nicht erreicht ist. Das unterscheidet SSS von einfacher Aufteilung (wo jede Hälfte Informationen enthält).

### Die Polynom-Mathematik

**Schritt 1: Threshold wählen.** Angenommen: 2-of-3 (k=2, n=3).

**Schritt 2: Geheimnis in ein Polynom einbetten.**  
Das Polynom hat Grad k−1. Für k=2 ist das eine Gerade:

```
f(x) = a₀ + a₁·x
```

Das Geheimnis wird als Konstante `a₀` gesetzt:

```
a₀ = 1234  (das Geheimnis)
a₁ = 5     (zufällig gewählt)
f(x) = 1234 + 5x
```

**Schritt 3: Shares berechnen.**  
Für jeden der n Teilnehmer wird ein Punkt berechnet:

```
f(1) = 1234 + 5·1 = 1239  → Share von Teilnehmer 1
f(2) = 1234 + 5·2 = 1244  → Share von Teilnehmer 2
f(3) = 1234 + 5·3 = 1249  → Share von Teilnehmer 3
```

**Schritt 4: Rekonstruktion.**  
Zwei Punkte bestimmen eindeutig eine Gerade. Mit den Punkten (1, 1239) und (2, 1244) lässt sich die Gerade rekonstruieren — und ihr Schnittpunkt mit x=0 ist `f(0) = a₀ = 1234`, das Geheimnis.

### Warum 1 Share nichts verrät

Durch einen einzelnen Punkt (z.B. (1, 1239)) laufen unendlich viele Geraden — jede mit einem anderen y-Achsenabschnitt. Ohne den zweiten Punkt ist jedes beliebige Geheimnis gleichwahrscheinlich. Mathematisch gesehen: Der Informationsgehalt eines einzelnen Shares ist Null.

Das ist der Kern der Sicherheitsgarantie — und was SSS von einfacher Aufteilung unterscheidet. Halbiert man eine Seed-Phrase und gibt jedem Hälfte, enthält jede Hälfte echte Information. Bei SSS enthält ein Share unterhalb der Schwelle keine.

### Poor Man's Shamir — Papier-Variante ohne Software

Marc Steiner beschreibt im Buch «Bitcoins verwahren und vererben» (und als Web-Artikel, 2020) eine rein papierbasierte Annäherung an SSS, die ohne Software oder Hardware-Wallet auskommt.

Das Prinzip: Eine 24-Wort-Seed-Phrase wird auf drei Karten so verteilt, dass jede Karte genau 16 Wörter trägt (8 Positionen bleiben leer). Die Verteilung ist symmetrisch:

- Wörter 1–8 stehen auf Karte A und B, nicht auf C
- Wörter 9–16 stehen auf Karte A und C, nicht auf B
- Wörter 17–24 stehen auf Karte B und C, nicht auf A

Jede beliebige Kombination aus zwei Karten ergibt alle 24 Wörter. Eine einzelne Karte lässt 8 Wörter im Dunkeln — und 2048⁸ ≈ 2⁸⁸ mögliche Kombinationen sind auch 2025 nicht in vertretbarer Zeit bruteforce-bar.

**Wichtige Einschränkungen:**

Das ist kein echtes SSS. Beim mathematischen SSS ist ein Share unterhalb der Schwelle informationstheoretisch nutzlos — er verrät buchstäblich nichts. Bei Steiners Variante enthält eine gestohlene Karte 16 echte Wörter; ein Angreifer kennt damit ⅔ der Phrase. Die Sicherheit beruht allein auf der Rechenunmöglichkeit, 8 BIP39-Wörter zu erraten — nicht auf einer Informationsgarantie.

Steiner warnt selbst, dass die Sicherheit mit steigender Rechenleistung zu hinterfragen ist.

Stärken des Ansatzes: keine Software, kein Gerät, keine digitale Angriffsfläche. Für Menschen, die keine technische Infrastruktur aufbauen wollen, ist es ein praktikabler Einstieg — solange die 8-Wort-Sicherheitsmarge dem eigenen Risikoprofil entspricht. [[Vorlage für «Poor Man Shamir's Secret Sharing Scheme»]]

Das Schema wird inzwischen auch in der deutschsprachigen Einsteiger-Bildung vermittelt (Nowak, 2025), dort verbunden mit der Empfehlung, (fast) immer 24 statt 12 Wörter zu verwenden — die 8-Wort-Marge des Poor-Man-Schemas existiert nur bei 24 Wörtern. Aus demselben Kontext stammt ein oft übersehener Praxishinweis zur Lagerung: Wer seine Seedphrase in einem externen Bankschliessfach deponiert, ist über die Schliessfachversicherung in der Regel nur für den Materialwert des Trägers gedeckt (die Stahlplatte, nicht die Coins dahinter). Das Schliessfach schützt also physisch, ersetzt aber keine Redundanz — geht der Inhalt verloren, gibt es keinen Ausgleich. [[20251130_heartmoney-schau-hin-der-tiger-greift-an]]

### Unterschied zu Multisig

| | Shamir Secret Sharing | Bitcoin Multisig |
|---|---|---|
| Ebene | Kryptografisch (Geheimnis-Aufteilung) | On-Chain (mehrere Schlüssel) |
| Bitcoin sieht | Normale Single-Sig-Transaktion | m-of-n Ausgabebedingung |
| Rekonstruktion | Am Rekonstruktionsort (Sicherheitsrisiko) | Jeder Schlüssel signiert separat |
| Standard | SLIP-39 (Trezor), SLIP-39 Advanced | BIP-11, P2SH, P2WSH |

Bei Multisig werden mehrere unabhängige Schlüssel verwendet — das Geheimnis verlässt nie die einzelnen Geräte. Bei SSS muss das Geheimnis zur Rekonstruktion an einem Ort zusammengeführt werden, was ein kurzzeitiges Risiko darstellt.

### Anwendung in Bitcoin: FROST

FROST (*Flexible Round-Optimized Schnorr Threshold*) ist die entscheidende Weiterentwicklung: Es kombiniert SSS mit Schnorr-Signaturen so, dass das Geheimnis **nie** vollständig rekonstruiert werden muss. Stattdessen erzeugt jeder Share-Inhaber einen Teil der Signatur, und die Teile werden aggregiert — das Private Key bleibt verteilt. Das schliesst das Rekonstruktions-Sicherheitsleck von klassischem SSS.

SLIP-39 (verwendet von Trezor für Seed-Backup) ist dagegen klassisches SSS: Die Shares müssen zur Rekonstruktion der Seed-Phrase zusammengebracht werden.

## Related

- [[taproot-musig2-frost]]
- [[multisig-und-kollaborative-verwahrung]]
- [[wallet-backup-strategien]]
- [[seedphrase-entropie-und-sicherheit]]
- [[optionale-passphrase]]
- [[fortego-backup-sicherheit]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wann wird FROST in gängigen Hardware-Wallets (BitBox02, Coldcard, Ledger) verfügbar?
- Wie verhält sich SLIP-39 (Trezor SSS) zu BIP-39 + Passphrase in der Praxis — welches ist robuster gegen Verlust und Diebstahl?
- Gibt es sichere Implementierungen von SSS für den Alltagseinsatz (ohne FROST) die das Rekonstruktions-Problem adressieren?
