# Digitales Zeitstempel und Hash-Verkettung

**Status:** established
**Themen:** grundlagen, protokoll, geschichte
**Last updated:** 2026-06-17
**Sources:** [[How to time-stamp a digital document]], [[Improving the Efficiency and Reliability of Digital Time-Stamping ]], [[secure-names-bit-strings]], [[secure-timestamping-service]]

## Summary

Digitale Zeitstempel lösen ein fundamentales Problem: Wie beweist man, dass ein Dokument zu einem bestimmten Zeitpunkt existiert hat, ohne einer zentralen Instanz vertrauen zu müssen? Stuart Haber und W. Scott Stornetta entwickelten ab 1991 eine Lösung via Hash-Verkettung — jedes Dokument wird mit dem Hash des vorherigen verknüpft, sodass nachträgliche Änderungen die gesamte Kette ungültig machen. Bayer, Haber und Stornetta (1992) erweiterten das System mit Merkle-Bäumen für effiziente Skalierung. Diese Arbeit ist die direkte strukturelle Vorstufe von Bitcoins Blockchain — Satoshi zitiert Haber & Stornetta dreimal im Whitepaper.

## Body

### Das Problem: Digitale Dokumente sind beliebig veränderbar

Papier-Dokumente haben forensische Eigenschaften — Tinte altert, Papier reißt, nachträgliche Änderungen hinterlassen Spuren. Digitale Dateien haben das nicht: Ein Bit ändern, Timestamp im Dateisystem anpassen, fertig. Das macht es unmöglich, den Erstellungszeitpunkt oder die Unverändertheit digitaler Dokumente nachzuweisen.

Das ist besonders relevant für Patentrechte, Verträge, Urheberrecht — überall, wo der Zeitpunkt der Erstellung entscheidend ist.

### Haber & Stornetta 1991: Die Hash-Kette

Der Kernbeitrag von Haber und Stornetta ("How to Time-Stamp a Digital Document", Journal of Cryptology, 1991):

**Das Grundprinzip:** Um zu belegen, dass Dokument D zum Zeitpunkt T existierte, reicht es nicht, D mit einem Timestamp T zu signieren — eine vertrauenswürdige Stelle könnte rückwirkend falsche Timestamps ausgeben. Die Lösung: D wird mit dem Hash des *vorherigen* signierten Dokuments verknüpft.

```
Block 1: Hash(D1) + Signatur
Block 2: Hash(D2 + Hash(Block1)) + Signatur
Block 3: Hash(D3 + Hash(Block2)) + Signatur
...
```

Jede Änderung an einem Block invalidiert alle nachfolgenden — die gesamte Kette würde nicht mehr stimmen. Wer viele Nutzer in dieselbe Kette einbindet, kann keinen einzelnen Block rückwirkend ändern, ohne dass alle anderen das sofort bemerken.

**Privacy by Design:** Der Timestamping-Service muss den Inhalt der Dokumente nicht kennen — er erhält nur die Hashes. Das Dokument selbst bleibt privat.

### Bayer, Haber & Stornetta 1992: Merkle-Bäume

Das 1991er-Verfahren hat einen Skalierungsproblem: Mit vielen Nutzern wird die Kette sehr lang. Bayer, Haber und Stornetta lösten das 1992 mit Merkle-Bäumen:

```
        Root-Hash
       /          \
   Hash(AB)    Hash(CD)
   /    \      /    \
Hash(A) Hash(B) Hash(C) Hash(D)
```

Statt jedes Dokument sequenziell zu verketten, werden viele Dokumente gleichzeitig in einem Merkle-Baum zusammengefasst. Nur der Wurzel-Hash muss publiziert werden (z.B. in einer Zeitung). Ein einzelnes Dokument kann mit einem kleinen Beweis (dem Merkle-Pfad) verifiziert werden, ohne alle anderen Dokumente zu kennen.

Das reduziert den Speicherbedarf exponentiell und ermöglicht echte Skalierung — tausende Dokumente pro Periode, ein einziger publizierter Hash.

### Der Publikations-Trick: Zeitung als Anker

Eine elegante Lösung für die Frage "Aber woher weiß ich, dass der Timestamping-Service den Timestamp nicht nachträglich geändert hat?": Veröffentliche den Root-Hash jede Woche in einer Zeitung. Zeitungen werden archiviert, gedruckt, verteilt — rückwirkende Änderung ist praktisch unmöglich.

Haber und Stornetta's Firma Surety nutzte diesen Mechanismus tatsächlich: Sie veröffentlichten wöchentlich einen Hash in der New York Times. Der älteste kontinuierliche Blockchain-ähnliche Dienst war damit bereits aktiv, bevor Satoshi Bitcoin veröffentlichte.

### Massias et al.: Minimales Vertrauen

Das belgische TIMESEC-Projekt (Massias, Serret Avila, Quisquater) untersuchte, wie Timestamping-Services mit minimalem Vertrauen implementiert werden können. Zwei Familien:

- **Trusted Third Party**: Klassisch, eine vertrauenswürdige Instanz signiert Timestamps. Problem: Vertrauen.
- **Distributed Trust**: Viele unabhängige Parteien bestätigen, reduziert Vertrauen in einzelne Instanz.

### Haber & Stornetta: Sichere Namen für Bit-Strings

In einem weiteren Paper ("Secure Names for Bit-Strings") entwickelten Haber und Stornetta, wie man Dokumente nach ihrem Inhalt benennt (nicht nach Ort) — inhaltsadressierbare Benennung via Hash. Das Konzept findet sich in Git (Content-Addressed Storage), IPFS und direkt in Bitcoins TXID-Schema wieder.

### Verbindung zu Bitcoin

Satoshi Nakamoto zitiert Haber & Stornetta dreimal im Bitcoin-Whitepaper — öfter als jeden anderen Autoren. Die strukturellen Parallelen sind direkt:

| Haber & Stornetta | Bitcoin |
|---|---|
| Hash-verkettete Dokumente | Hash-verkettete Blöcke |
| Merkle-Baum der Dokumente | Merkle-Baum der Transaktionen |
| Root-Hash in Zeitung | Root-Hash im Block-Header |
| Timestamping-Service | Miner (dezentralisiert) |
| Vertrauen in Service | Proof-of-Work (trustless) |

Der entscheidende Bitcoin-Beitrag: die Dezentralisierung durch Proof-of-Work. Bei Haber & Stornetta gibt es noch einen (vertrauenswürdigen) Timestamping-Service — Bitcoin ersetzt diesen durch den verteilten Konsens aller Miner.

## Related

- [[bitcoin-whitepaper]]
- [[merkle-baeume]]
- [[hashcash]]
- [[digitales-bargeld-und-ecash]]
- [[bitcoin-mining-und-proof-of-work]]

## Open Questions

- Warum ist Surety's ursprünglicher Timestamping-Service (aktiv seit 1995!) so wenig bekannt, obwohl er konzeptuell Bitcoin vorwegnimmt?
- Wie wird SPV (Simplified Payment Verification) durch den Merkle-Pfad-Mechanismus von Bayer et al. ermöglicht?
