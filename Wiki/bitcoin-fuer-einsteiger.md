# Bitcoin für Einsteiger (Marco Bühler)

**Status:** established
**Themen:** grundlagen, protokoll, self-custody, oekonomie, kritik, buecher
**Last updated:** 2026-07-31
**Sources:** [[Bitcoin-fuer-Einsteiger_Buehler]]

## Summary

Deutschsprachiges Einführungsbuch von 2024, geschrieben vom Schweizer YouTuber Marco Bühler («sunny decree»). Es führt in drei Teilen vom Bankensystem über die Technik bis zum Marktverhalten und endet mit einer konkreten Kaufanleitung. Der Bogen ist der klassische Bitcoin-only-Bogen: Fiat-Geld ist konstruktionsbedingt schlecht, hartes Geld setzt sich langfristig durch, Bitcoin ist das erste digitale harte Geld, Altcoins sind Ablenkung, und die praktische Konsequenz heisst regelmässig kaufen und selbst verwahren. Was das Buch von anderen Einsteigertiteln abhebt, ist der zweite Teil: Bühler erklärt Bitcoin entlang des Weges, den eine einzelne Transaktion nimmt, statt entlang einer Begriffsliste. Der dritte Teil ist der schwächste, weil er zugleich Produkte verkauft; immerhin legt Bühler das offen.

## Body

### Einordnung

Das Buch richtet sich an Leute ohne Vorwissen und ist entsprechend gebaut: kurze Kapitel, Parabeln statt Formeln, Zwischenbilanzen, eine «Lernkontrolle» nach dem Technikteil und ein Lexikon am Schluss. Alle Zahlen stehen auf dem Stand März 2024 — Marktkapitalisierung «über 1'000 Milliarden USD», vier abgeschlossene Preiszyklen, die Spot-ETFs gerade zugelassen. Als Fachprüfer nennt die Danksagung unter anderem Christian Decker. Verlag ist Eulogia (Hamburg), das Werk ist urheberrechtlich geschützt, es gibt keine offene Lizenz.

### Teil 1: die Geldfrage

Bühler beginnt nicht bei Bitcoin, sondern bei der Bank. Er listet die Geschäftsfelder einer Universalbank auf und markiert eines davon als das eigentlich strittige: Kreditvergabe erzeugt Buchgeld. Daran hängen die weiteren Kritikpunkte — Fractional Reserve Banking und die Frage, was bei einem Bank Run passiert; die Einlagensicherung von 100'000 Euro oder Franken, bei der ein Sparer mit 250'000 im Ernstfall 150'000 verliert (Zypern 2013 als Beleg); Zahlungen, die eine Bank ohne Vorwarnung zurückhält; und CBDCs als Ausbau genau dieser Kontrolle. Die Genesis-Block-Schlagzeile schliesst das Kapitel.

Die Geldtheorie läuft über eine Insel-Parabel: zwei Gestrandete, Arbeitsteilung, ein Hüttenbauer, dessen Ware nicht direkt tauschbar ist, also braucht es einen Zwischenspeicher. Daraus die drei Funktionen — Wertspeicher, Tauschmittel, Recheneinheit — und die Prüfung, wo Bitcoin steht. Bühlers Antwort ist differenzierter als der Buchtitel erwarten lässt: als Wertspeicher bewährt, als Tauschmittel in fünf von sechs Punkten erfüllt (offen bleibt die allgemeine Akzeptanz), als Recheneinheit noch nicht, weil die Volatilität es nicht zulässt. Er argumentiert, dass die Schwankung mit wachsender Marktkapitalisierung sinkt, und belegt es mit den Drawdowns der vier Zyklen: 94, 86, 84, 78 Prozent.

Die Insel kehrt für den Cantillon-Effekt zurück. Der stärkste Bewohner beansprucht den Strand für sich, sammelt Muscheln und hilft in der Wasserkrise mit zusätzlichen Muscheln aus — worauf der Wasserpreis weiter steigt und die zusätzlichen Muscheln nach der Krise im System bleiben. Das Bild trägt die ganze Geldmengenkritik: Fed-Bilanz um 8 Billionen Dollar, M2 seit 1971 rund vervierzigfacht, Kaufkraftverlust des Dollars von 87 Prozent, dazu Bernholz' Befund einer durchschnittlichen Fiat-Lebensdauer von 27 Jahren. Ökonomisch verortet sich Bühler klar bei der Österreichischen Schule und stellt sie Keynesianismus und MMT gegenüber. Nützlich ist seine Unterscheidung zwischen knapp und begrenzt: Gold und Rolex-Uhren sind knapp, aber die Fördermenge beziehungsweise die Produktion lässt sich hochfahren, sobald der Preis es lohnend macht. Begrenzt sind Land und Bitcoin.

### Teil 2: die Transaktion als roter Faden

Der Technikteil ist der stärkste. Statt Begriffe abzuarbeiten, legt Bühler die sieben Stationen einer Transaktion fest — Wallet, Nodes, Mempool, Miner, Block, Nodes, Blockchain — und hängt jedes Konzept dort auf, wo es im Ablauf gebraucht wird. Vorher stehen zwei Vorbereitungskapitel: Dezentralität als Papier-Beispiel (vier Leute am Tisch, einer führt Buch, dann führen alle Buch und halten ihr Blatt hoch) und Kryptographie, wobei Bühler korrekt anmerkt, dass Bitcoin von den drei Zielen Vertraulichkeit, Integrität und Authentizität nur die letzten beiden nutzt.

Zwei didaktische Griffe bleiben hängen. Erstens die Mining-Übung: Leser sollen drei Beispieltransaktionen plus eine Nonce in einen SHA-256-Generator tippen und die Nonce hochzählen, bis der Hash mit einer Null beginnt — mit dem Hinweis, dass jede weitere Hexadezimalstelle den Aufwand versechzehnfacht. Zweitens die Gebührenerklärung als Auktion um Platz im nächsten Block, ergänzt um den Zweck, den Gebühren jenseits der Miner-Vergütung haben: Spamschutz.

Die Wallet-Typologie ist praktisch brauchbar und für ein Einsteigerbuch ungewöhnlich deutlich in ihren Abratungen — Web-Wallets und Paper-Wallets empfiehlt Bühler ausdrücklich nicht, Multisig hält er für Fortgeschrittene. Beim Seed verweist er auf BIP-39 mit seinen 2'048 Wörtern und der Vier-Buchstaben-Eindeutigkeit, rät aber davon ab, nur diese vier Buchstaben zu notieren, weil ein vollständiges Wort bei Wasserschaden oder unleserlicher Handschrift rekonstruierbar bleibt. Metall statt Papier ist die Empfehlung.

Das Kritikkapitel behandelt Energie, Skalierung, 51 Prozent und Regulierung. Die Energieantwort ist die bekannte: Bitcoin nutzt Energie zweckgebunden, die Vergleiche mit Länderverbräuchen sind willkürlich gewählt, und Miner können als abschaltbare Last ein Netz stabilisieren (Texas). Beim Skalierungsproblem gibt Bühler zu, dass es eines ist, und verweist auf Lightning.

### Teil 3: Markt, Betrug und ein offengelegter Interessenkonflikt

Der dritte Teil beginnt mit einer Betrugstypologie — Tradinggruppen, Pump-and-Dump, Rug-Pulls, Renditeplattformen, MLM, Scam-Börsen, Phishing, vorpräparierte Hardware-Wallets — und fasst sie in zwölf Grundregeln zusammen. Danach die Altcoin-Absage, sortiert nach Typ, mit dem Orakel-Problem als bestem Argument: Sobald eine Blockchain externe Daten aufnimmt, muss man wieder derjenigen Stelle vertrauen, die sie einträgt, womit der Vorteil verfällt.

Für den Umgang mit dem Preis empfiehlt Bühler Sparpläne, Zurückhaltung gegenüber technischer Analyse und emotionsfreies Verhalten in beide Richtungen. Bemerkenswert ist die Offenheit über die eigene Position: Er hält die Wahrscheinlichkeit, dass Bitcoin scheitert, für 0,1 bis 1 Prozent und will trotzdem in einer Hype-Phase einen Teil seiner Position abbauen, aus Diversifikationsgründen. Am Ende stehen Produktempfehlungen, darunter Relai mit einem Gutscheincode auf seinen eigenen Namen und Sygnum mit der Bitte, das Buch beim Onboarding zu erwähnen. Das ist Affiliate-Geschäft, aber im Text sichtbar gemacht.

### Wo das Buch ungenau wird

Drei Stellen sind für die Ablage im Korpus wichtig. Die Fork-Geschichte stimmt nicht: Bühler schreibt, 2017 sei eine Erhöhung der Blockgrösse von 1 auf 2 MB vorgeschlagen, von der Mehrheit abgelehnt worden und daraus sei Bitcoin Cash entstanden. Tatsächlich waren das zwei getrennte Vorgänge — BCH spaltete sich am 1. August 2017 als von Bitmain vorbereitete Hard Fork mit 8-MB-Blöcken ab, während die 2-MB-Hard-Fork Phase zwei des New Yorker Abkommens war und am 8. November 2017 abgesagt wurde (siehe [[blocksize-war]]). Zweitens die Formulierung, Bitcoin sei «zu 100 % fälschungssicher» und ein Schlüsselpaar existiere «bis in die Ewigkeit» — als Einsteigerverkürzung verständlich, aber die kryptographischen Annahmen dahinter sind zeitgebunden (siehe [[bitcoin-und-quantenrisiko]]). Drittens die Behauptung, das Blockchain-Trilemma sei so unlösbar wie ein Perpetuum mobile. Der physikalische Vergleich suggeriert einen Beweis, den es nicht gibt; das Trilemma ist eine Faustregel aus der Praxis, kein Theorem.

## Related

- [[bitcoin-einsteiger-onboarding]]
- [[geld-staat-und-fiat-monopol]]
- [[geldpolitik-und-inflation]]
- [[bitcoin-kaufen-und-dca]]
- [[bitcoin-vs-krypto]]
- [[phishing-und-angriffsmethoden]]
- [[hardware-wallet-einstieg]]
- [[bitcoin-mining-und-proof-of-work]]
- [[transaktionsgebuehren-und-mempool]]
- [[bitcoin-volatilitaet-und-preisfindung]]
- [[blocksize-war]]
- [[das-kleine-bitcoin-buch|Das kleine Bitcoin-Buch]] ← Buch
- [[bitcoin-verstaendlich-erklaert|Bitcoin verständlich erklärt (Hügli/Lanni)]] ← Buch

## Open Questions

- Bühler datiert die Bitcoin-Zyklen auf «exakt vier Jahre» und führt sie auf das Halving zurück. Der Korpus hält dagegen (siehe [[bitcoin-volatilitaet-und-preisfindung]]): Der Supply-Effekt des Halvings ist inzwischen zu klein, um die Preisbewegung zu erklären. Ein Vergleich der beiden Erklärungen wäre ein eigener Artikel wert.
- Die Bitcoin-only-Einsteigerliteratur im Korpus wächst. Eine Gegenüberstellung, welches Buch für welchen Leser taugt, fehlt noch.
