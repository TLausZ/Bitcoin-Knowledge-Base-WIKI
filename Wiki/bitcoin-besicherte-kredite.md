# Bitcoin-besicherte Kredite und Buy-Borrow-Die

**Status:** established
**Last updated:** 2026-07-04
**Sources:** [[20260421_heartmoney-von-bitcoin-leben-geht-das-wirklich]], [[20251026_heartmoney-bitcoin-auf-kredit-lohnt-sich-das]], [[20260412_heartmoney-bitcoin-proton-iran]], [[20260510_heartmoney-ein-barenmarkt-fur-ameisen]], [[20260630_heartmoney-bitcoin-angst-und-magie]]

## Summary

Bei Bitcoin-besicherten Krediten wird Bitcoin als Pfand hinterlegt, um Fiat-Liquidität zu erhalten, ohne zu verkaufen. Die zentrale Steuerungsgröße ist der Beleihungsgrad (LTV): Fällt der Kurs, steigt der LTV, es drohen Margin Calls und ab einer Schwelle die Zwangsliquidierung der hinterlegten Bitcoin. Die Strategie «Buy, Borrow, Die» — vom Bestand leben, ohne je zu verkaufen — funktioniert rechnerisch, aber nur mit großem Bestand, niedrigem LTV, hohen Liquiditätsreserven und Disziplin. Nowaks Kernbefund: Selbst ein konservatives Setup garantiert keinen gleichmäßigen Cashflow. Nach einem starken Kursrückgang kann der Entnahmespielraum jahrelang verschwinden. Nicht liquidiert zu werden und davon leben zu können sind zwei verschiedene Dinge.

## Body

### Prinzip und Anbieterlandschaft

Ein Bitcoin-besicherter Kredit ist technisch ein Pfandkredit: Bitcoin dient als Sicherheit, ausgezahlt wird Fiat (Euro, Franken). Keine Bonitätsprüfung im klassischen Sinn, die Sicherheit ersetzt die Schufa-Auskunft. Zwei Verwahrmodelle unterscheiden die Anbieter grundlegend:

- **Custody-Modell:** Die Plattform verwahrt die Bitcoin selbst. Bequem, aber volle Kontrollabgabe und Gegenparteirisiko.
- **Escrow-Modell:** Treuhänderische Verwahrung, meist per Multisig, bei der keine Partei allein Zugriff hat. Beispiel Firefish: P2P-Marktplatz, bei dem die Bitcoin in einem Escrow direkt auf der Blockchain liegen und vom Anbieter nicht weiterverliehen werden können; Zinsen bilden sich marktbasiert zwischen Kreditnehmern und Kreditgebern.

Daneben existieren KYC-freie Nischenangebote (Lendasat). Die Laufzeiten sind oft kurz — häufig maximal 24 Monate —, was das Timing-Risiko erhöht, weil kaum Zeit bleibt, Kursrückgänge auszusitzen. Im Oktober 2025 kündigte die Volksbank Raiffeisenbank Bayern Mitte mit dem Broker 21bitcoin ein reguliertes Bitcoin-besichertes Kreditprodukt an — sie wäre die erste Bank in Deutschland, die Bitcoin als Kreditsicherheit anerkennt. [[20251026_heartmoney-bitcoin-auf-kredit-lohnt-sich-das]], [[20260510_heartmoney-ein-barenmarkt-fur-ameisen]]

### LTV: die zentrale Kennzahl

Der Loan-to-Value setzt Kreditbetrag und aktuellen Wert der Sicherheit ins Verhältnis. Beispiel: 120.000 € Bitcoin hinterlegt, 60.000 € Kredit aufgenommen → 50% LTV. Steigt der Kurs, sinkt der LTV und der Puffer wächst; fällt der Kurs, steigt der LTV. Fällt der Bitcoin-Preis im Beispiel von 60.000 € auf 45.000 €, springt der LTV von 50% auf 67%.

Die Firefish-Mechanik (Stand der Quelle, April 2026): Margin-Call-Stufen bei 73%, 79% und 86% LTV — der Kreditnehmer muss Bitcoin nachschießen oder zurückzahlen. Bei 95% LTV erfolgt die Liquidierung; im Beispiel wäre das bei einem Kurs von knapp 31.600 € der Fall. Nicht der Kreditbetrag allein bestimmt das Risiko, sondern das Verhältnis zum schwankenden Wert der Sicherheit. [[20260421_heartmoney-von-bitcoin-leben-geht-das-wirklich]]

### Buy, Borrow, Die

Die Strategie stammt aus dem US-Immobilienmarkt: Vermögenswert kaufen, langfristig halten, bei Geldbedarf beleihen statt verkaufen. Zwei Vorteile übertragen sich auf Bitcoin: Der Bestand bleibt investiert (künftige Wertsteigerung geht nicht verloren), und es wird kein steuerlicher Verkauf ausgelöst — in Deutschland relevant wegen der Ein-Jahres-Haltefrist, in Österreich seit 2022 wegen der 27,5%-Besteuerung ohnehin anders gelagert.

Das Modell steht auf fünf Annahmen, die alle gleichzeitig halten müssen: (1) Bitcoin wächst langfristig stärker als Kreditzins und Gebühren; (2) niedriger Start-LTV; (3) Margin Calls können im Ernstfall bedient werden; (4) Kreditgeber/Verwahrer fällt nicht aus; (5) Steuer- und Regulierungsrahmen bleibt nicht zum Nachteil verändert.

### Rechenbeispiel 1: konstantes Wachstum

Parameter: 2 BTC als Sicherheit (120.000 € bei Kurs 60.000 €), 50% Start-LTV, 60.000 € Kredit, 25% Bitcoin-Wachstum p.a., 10% Kreditzins p.a. Ergebnis: Der LTV sinkt stetig — nach einem Jahr ~44%, nach fünf Jahren ~26,4%, nach zehn ~13,9%. Bei konstantem Ziel-LTV von 50% entsteht zusätzlicher Kreditspielraum: 9.000 € nach einem Jahr, ~86.500 € nach fünf, über 403.100 € nach zehn Jahren.

Der häufigste Denkfehler liegt hier: Nicht der kumulierte Spielraum ist entnehmbar, sondern nur sein jährlicher Zuwachs — im Modell 9.000 € im ersten, ~27.800 € im fünften, ~97.600 € im zehnten Jahr. Wer den Vorjahresspielraum bereits genutzt hat, kann nur den Neuzuwachs entnehmen.

Zwei Realitätschecks: 50% LTV ist eher aggressiv; für bullische Phasen nennt die Quelle 5–15%, sonst etwa 20% als konservativ. Und die Größenordnung: Wer schon im ersten Jahr 50.000 € bei 20% LTV entnehmen will, braucht über 1,6 Millionen Euro Collateral. Buy-Borrow-Die ist kein Trick für kleine Bestände, sondern ein Modell für die Phase nach erfolgreichem Vermögensaufbau. [[20260421_heartmoney-von-bitcoin-leben-geht-das-wirklich]], [[20260412_heartmoney-bitcoin-proton-iran]]

### Rechenbeispiel 2: volatiler Verlauf

Konservativer Start: 120.000 € Collateral, 20% LTV, 24.000 € Kredit. Fiktiver Kurspfad: +100% im ersten Jahr, +150% im zweiten — der LTV fällt auf 4,8%, die neu entnehmbare Liquidität steigt auf über 69.000 €. Dann −75% im dritten Jahr: Der LTV springt auf 21,3%. Keine Liquidierungsgefahr, aber der Ziel-LTV von 20% ist überschritten — der zusätzliche Kreditspielraum wird negativ, in diesem Jahr ist keine Entnahme möglich, ohne das Risikoprofil aufzugeben.

Daraus folgt die zentrale Unterscheidung: Ein niedriger LTV schützt vor der Liquidierung, garantiert aber keinen gleichmäßigen Cashflow. «Überleben» und «davon leben» sind verschiedene Aussagen. Die öffentliche Debatte dreht sich fast ausschließlich um das Liquidierungsrisiko und übersieht das Entnahmerisiko.

### Fünf Risiken

1. **Marktpreisrisiko:** Bitcoin muss dauerhaft stärker wachsen als die Kreditkosten; kurzfristig kann Entnahmespielraum vollständig verschwinden.
2. **Disziplinrisiko:** In der Theorie startet jeder konservativ, in der Praxis wird der LTV schöngerechnet.
3. **Fehlende Liquiditätsreserven:** Margin Calls erfordern sofortige Liquidität; hieran scheitern die meisten realen Fälle.
4. **Gegenparteirisiko:** Bleibt auch beim Escrow-Modell bestehen, ist dort aber reduziert.
5. **Regulierungsrisiko:** Haltefrist-Debatte in Deutschland; Österreich als Präzedenzfall für die Abschaffung steuerlicher Vorteile.

Ein dokumentierter Praxisfall zur Fallhöhe: Auf der BTC Prague im Juni 2026 — mitten im Bärenmarkt — berichtete ein Kreditnehmer, dass seine Reserven zur Bedienung der Margin Calls zur Neige gingen und die Liquidierung drohte. Die Quelle zieht daraus die Konsequenz, dass LTV, Liquidierung, Margin Calls und Liquiditätsreserven vor Abschluss verstanden sein müssen. [[20260630_heartmoney-bitcoin-angst-und-magie]]

### Einordnung: Aufbau- vs. Entnahmephase

Wer sich noch im Vermögensaufbau befindet, für den ist das Modell nicht gedacht — dort gilt kaufen, halten, Geduld. Als grobe Orientierung zitiert die Quelle den US-YouTuber Brad Long: Unter etwa 1 Million USD Nettovermögen ist man in der Aufbauphase; erst darüber werden Entnahmestrategien wie Buy-Borrow-Die realistisch. Ein blinder Fleck der Community-Debatte: Viele diskutieren Entnahmestrategien, obwohl sie mitten in der Akkumulation stehen. Anwendungsfälle jenseits der Entnahme existieren — etwa Alltagsleben auf dem Bitcoin-Standard mit Krediten als Fiat-Brücke (Fallbeispiel Markus Turm) —, bleiben aber Nische. [[20260510_heartmoney-ein-barenmarkt-fur-ameisen]]

## Related

- [[bitcoin-auf-kredit]]
- [[bitcoin-und-immobilien]]
- [[bitcoin-unternehmens-strategie]]
- [[bitcoin-volatilitaet-und-preisfindung]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-entfinanzialisierung]]

## Open Questions

- Firefish-Parameter (Margin-Call-Stufen, Liquidierungsschwelle) sind zeitgebunden (Stand April 2026) — bei Nutzung aktuell prüfen.
- Wie ist das Volksbank/21bitcoin-Kreditprodukt konkret ausgestaltet (LTV-Grenzen, Verwahrung, Zins)? Ankündigung Okt 2025, Produktdetails ausstehend.
- KYC-freie Anbieter (Lendasat): Funktionsweise und Risiken ungeprüft, nur als Erwähnung belegt.
- Spannung zur These der [[bitcoin-entfinanzialisierung]]: Bitcoin soll vom Zwang befreien, «Geld arbeiten zu lassen» — Buy-Borrow-Die refinanzialisiert den Bestand. Verträgt sich das konzeptionell?
