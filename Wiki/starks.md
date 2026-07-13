# STARKs

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-07-02
**Sources:** [[How STARKs Work_ Part 1]], [[How STARKs Work_ Part 2]], [[How STARKs Work_ Part 3]], [[How STARKs Work_ Part 4]], [[How STARKs Work_ Part 5]], [[How STARKs Work_ Part 6]]

## Summary

STARKs (Scalable Transparent Arguments of Knowledge) sind kryptografische Beweissysteme: Ein Prover verarbeitet eine grosse Menge Transaktionen off-chain und erzeugt einen Validitätsbeweis, den ein Verifier mit minimalem Rechenaufwand prüft. Statt dass jede Node jede Transaktion nachrechnet (wie bei Bitcoin und Ethereum), genügt die Prüfung des Beweises. StarkWare beziffert das Verhältnis so: Der Beweis für 1 Million Transaktionen lässt sich mit dem Rechenaufwand von etwa 6 Transaktionen verifizieren. Die Sicherheit beruht auf Fehlerverstärkung durch Error-Correcting-Codes (Reed-Solomon), Kompression per FRI-Protokoll und einem Merkle-Commitment. Weil STARKs als einzige kryptografische Annahme eine sichere Hashfunktion brauchen, gelten sie als post-quanten-sicher; SNARKs dagegen bauen auf Elliptische-Kurven-Kryptografie, die für Quantencomputer angreifbar ist. Seit 2018 bei StarkWare produktiv im Einsatz, primär im Ethereum-Umfeld.

## Body

### Das Problem: Jeder rechnet alles nach

Dezentrale Blockchains verifizieren jede Interaktion auf jeder Node. Sendet Alice Geld an Bob, prüft jede Node erneut: Hatte Alice genug Guthaben? Stimmt die Signatur? Wurden die Salden korrekt angepasst? Das macht das System sicher und gleichzeitig langsam.

Die Analogie aus der Quelle: 30 Schüler schreiben eine Matheprüfung, aber der korrigierende Lehrer ist möglicherweise bestochen. Wenn deshalb alle anderen Lehrer sämtliche Prüfungen selbst nachkorrigieren, funktioniert das mit 30 Prüfungen gerade noch, mit 3'000 nicht mehr.

### Die Grundidee: Ein Beweis statt Nachrechnen

Im STARK-Protokoll gibt es zwei Rollen:

- Der *Prover* verarbeitet die Transaktionen in einer aufwendigen Berechnung und erzeugt den STARK-Beweis.
- Der *Verifier* ist ein Stück Software, das den Beweis in wenigen Schritten prüft.

Der Prover muss nicht vertrauenswürdig sein. Er kann ein Staat sein, ein Konzern oder ein anonymer Akteur; die Mathematik lässt sich nicht zu seinen Gunsten verbiegen. Der Verifier rechnet keine Transaktionen nach, sondern zieht Stichproben aus dem Beweis. Damit das reicht, ist der Beweis so konstruiert, dass jeder noch so kleine Fehler den gesamten Beweis kontaminiert.

### Schritt 1: Ausführungsschritte und Constraints

Der Prover bündelt einen grossen Batch von Transaktionen und registriert deren Ausführungsschritte als Zahlenfolge: Anfangssaldo des Senders, Anfangssaldo des Empfängers, Transferbetrag, Endsalden usw.

Gültigkeit wird über *Constraints* definiert, Regeln, die jede korrekte Transaktion erfüllen muss. Für einen Transfer von Alice an Bob etwa:

1. Summe der Anfangssalden = Summe der Endsalden (A+B = D+E)
2. Bobs Anfangssaldo plus Betrag = Bobs Endsaldo (B+C = E)
3. Alices Anfangssaldo minus Betrag = Alices Endsaldo (A−C = D)
4. Der Betrag ist positiv und übersteigt Alices Saldo nicht

Die Quelle vergleicht das mit Sudoku: Eine falsche Zahl verletzt sichtbar die Regel ihrer Zeile, Spalte oder ihres Quadrats. Wer schummelt und Bob 1 Token gutschreibt, ohne ihn Alice abzuziehen, verletzt Constraint 1 und 3 zugleich. Der Haken: Die Verletzung zeigt sich nur an genau dieser Stelle der Sequenz. Bei einer Milliarde Ausführungsschritten (1 Million Transaktionen à ~1'000 Schritte) würde eine Stichprobe einen einzelnen Fehler fast sicher verpassen.

### Schritt 2: Daten expandieren, Fehler verstärken

Deshalb wird die Sequenz um redundante Prüfdaten erweitert, eine hochgezüchtete Version der Prüfziffer (wie bei ISBN oder Fahrgestellnummern): Eine Formel über die Hauptziffern liefert eine Kontrollziffer; ein Tippfehler bringt Formel und Kontrollziffer aus dem Takt.

STARKs berechnen viele solcher «Prüfziffern» in gezielten Mustern, etwa die Summe aller Zahlen, jeder dritten Zahl, aller geraden Zahlen, der ersten Hälfte. Technisch ist das ein Error-Correcting-Code, konkret der Reed-Solomon-Code auf Basis von Polynomen niedrigen Grades. Die Idee stammt aus der Informationstheorie der 1940er (Claude Shannon): Codes, die Nachrichten trotz Rauschen korrekt ankommen lassen. Die angehängten Prüfdaten sind deutlich länger als die Transaktionsdaten selbst.

Anschliessend werden Constraints auch auf die Prüfziffern angewendet. Beispiel: Der Eintrag «Summe aller Zahlen» muss dem Eintrag «Summe der ersten Hälfte» plus «Summe der zweiten Hälfte» entsprechen. Über den ganzen Batch hinweg gilt analog: Die Summe aller Anfangssalden von Sendern und Empfängern muss der Summe aller Endsalden entsprechen (a'+b' = d'+e').

Der Effekt: Ein einzelner manipulierter Eintrag zieht sich durch unzählige nachgelagerte Berechnungen. Wer einen Eintrag fälscht, müsste immer mehr weitere Einträge anpassen, um alle Quersummen konsistent zu halten. Für den verwendeten Code lässt sich mathematisch beweisen, dass das nicht gelingt: Fast keine geprüfte Kombination von Prüfziffern geht dann noch auf.

### Schritt 3: Falten mit FRI

Der Beweis ist jetzt extrem lang und wird per «Folding» komprimiert. Jede Faltung erzeugt eine kürzere Sequenz, deren Einträge jeweils 10 Zahlen der vorherigen zusammenfassen: von 1 Milliarde auf 100 Millionen, dann 10 Millionen, nach 8 Faltungen bleiben 10 Zahlen. Das Protokoll heisst FRI (Fast Reed-Solomon IOPP); es halbiert schrittweise den Grad des zugrunde liegenden Polynoms.

Das Falten prüft zugleich die Gültigkeit. Eine ehrlich erzeugte Sequenz bildet ein mathematisches Muster, das die Quelle als «millionendimensionale Schneeflocke» beschreibt. Faltet man dieses Muster, sind am Ende alle 10 Zahlen identisch, egal welches Faltungsmuster gewählt wurde. Der Verifier liest 10 Zahlen und vergleicht sie. Ein Prover, der geschummelt hat (im Text: Darth Vader statt Luke Skywalker), kann das Muster nicht erzeugen; er faltet etwas Deformiertes, und die Endzahlen weichen fast immer voneinander ab.

### Schritt 4: Versiegeln per Merkle-Commitment

Bevor der Verifier Stichproben zieht, muss der Prover sich auf seine Sequenz festlegen, sonst könnte er Einträge nachträglich passend machen. Das Commitment läuft über einen [[merkle-baeume|Merkle-Baum]]: Der Prover committet auf die Zahlenfolge, und beim Auslesen einzelner Einträge lässt sich effizient prüfen, dass sie unverändert sind.

Hier liegt die einzige kryptografische Annahme des ganzen Systems: dass die verwendete Hashfunktion sicher ist. Alles andere ist reine Mathematik ohne Annahmen. Daraus folgt die Post-Quanten-Sicherheit: Hashfunktionen gelten als quantenresistent, während SNARKs auf Elliptische-Kurven-Kryptografie angewiesen sind, die ein Quantencomputer brechen könnte.

Zum Schluss gehen STARK-Beweis und State-Update on-chain. Der On-chain-Verifier prüft den Beweis; ist er gültig, wird der neue Zustand akzeptiert.

### Einordnung

Die Quelle ist eine StarkWare-Publikation und entsprechend werbend im Ton («battle-tested», Buchwerbung des Autors). Die beschriebene Technik läuft seit 2018 produktiv, allerdings im Ethereum-Umfeld (Starknet, zk-Rollups), nicht auf Bitcoin. Für Bitcoin sind STARKs aus zwei Gründen interessant: als möglicher Baustein für Off-chain-Skalierung mit Validitätsbeweisen (vgl. BitVM in [[skalierung-lightning-ark-statechains]], das allerdings optimistisch statt mit Validitätsbeweisen arbeitet) und wegen der Post-Quanten-Eigenschaft, die im Kontext von [[bitcoin-und-quantenrisiko]] relevant ist. Neben Skalierung ermöglichen STARKs auch Privatsphäre: Der Verifier bestätigt Gültigkeit, ohne die zugrunde liegenden Daten zu sehen.

## Related

- [[merkle-baeume]]
- [[bitcoin-und-quantenrisiko]]
- [[skalierung-lightning-ark-statechains]]
- [[bitcoin-skalierung-und-zahlungen]]
- [[double-sha256]]

## Open Questions

- Gibt es ernsthafte Vorschläge, STARK-Validitätsbeweise direkt auf Bitcoin zu verankern (z.B. via BitVM-artige Konstruktionen oder OP_CAT-Covenants)? Die Quelle sagt dazu nichts.
- Wie gross sind STARK-Beweise in der Praxis (Bytes on-chain) und was kostet das Proving rechnerisch? Die Serie bleibt hier qualitativ.
- Abgrenzung STARK vs. SNARK verdient bei Gelegenheit einen eigenen Vergleich mit neutraleren Quellen; die Serie stammt vom STARK-Erfinderumfeld.
