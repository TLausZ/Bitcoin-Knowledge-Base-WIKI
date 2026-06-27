# Transaktionsgebühren und Mempool

**Status:** established
**Last updated:** 2026-06-27
**Sources:** [[20210714_wieso-muss-ich-eine-transaktionsgebuehr-bezahlen-de]], [[20210804_was-ist-eigentlich-eine-utxo-de]], [[waltz-bitcoin-facts]]

## Summary

Bitcoin-Transaktionsgebühren entstehen, weil jeder Block nur begrenzt Platz hat und Miner entscheiden, welche Transaktionen sie aufnehmen. Wer höher zahlt, kommt früher dran. Der Mempool — die Warteschlange unbestätigter Transaktionen — zeigt die aktuelle Gebührenlage in Echtzeit. Transaktionsgröße in vBytes hängt von Adresstyp und Anzahl der UTXOs ab; wer Gebühren sparen will, konsolidiert UTXOs in ruhigen Phasen.

## Body

### Warum gibt es Transaktionsgebühren?

Im Bitcoin-Netzwerk wird alle ~10 Minuten ein Block erzeugt. Jeder Block ist in seiner Größe begrenzt (1 MB Basisgröße, bis zu ~4 MB mit SegWit-Witness). Das ist bewusst so: unbegrenzte Blöcke würden die Blockchain in einen Zustand wachsen lassen, der nur noch mit sehr leistungsstarken Computern betreibbar wäre — und damit die Dezentralisierung gefährden.

Wenn mehr als ~3.000 Transaktionen auf ihre Bestätigung warten, muss der Miner entscheiden, welche er im nächsten Block aufnimmt. Miner sind ökonomisch motiviert: Sie wählen die Transaktionen mit den höchsten Gebühren.

### Wie Gebühren funktionieren

Eine Transaktionsgebühr wird in Satoshi pro virtuellem Byte (sat/vByte) angegeben — nicht als absoluter Betrag. Je größer eine Transaktion (mehr UTXOs als Inputs, mehr Outputs), desto mehr Platz im Block und desto höhere absolute Gebühr bei gleichem sat/vByte-Satz.

Daraus folgt eine direkte Verbindung zur UTXO-Verwaltung: Viele kleine UTXOs = große Transaktionen = höhere Gebühren. Konsolidierung in Niedriggebühren-Phasen ist eine sinnvolle Strategie.

### Der Mempool

Der Mempool (Memory Pool) ist die Warteschlange aller noch nicht bestätigten Transaktionen im Netzwerk. Er spiegelt die aktuelle Nachfrage nach Blockplatz wider und erlaubt eine Einschätzung der angemessenen Gebühr.

Nützliche Mempool-Explorer:
- **mempool.space** — visuelle Darstellung nach Gebührenstufen, Blockvorhersagen
- **jochen-hoenicke.de** — zeitliche Entwicklung des Mempool-Volumens

Das Grundmuster: Alle ~10 Minuten wird ein Block gefunden, die höchstbietenden Transaktionen werden herausgenommen. Im Diagramm ist das als periodischer Einschnitt von oben sichtbar. In Hochlastphasen (starke Preisvolatilität, viele neue Nutzer) füllt sich der Mempool schnell und Gebühren steigen deutlich.

### Entstehungsgeschichte der Gebühren-Schätzung

In den ersten Jahren von Bitcoin waren Transaktionsgebühren hardcodiert — sie wurden mit jeder neuen Softwareversion manuell angepasst, um Marktbedingungen näherungsweise abzubilden. Erst im Februar 2015 enthielt Bitcoin Core 0.10.0 den ersten algorithmischen Fee-Estimator: Er beobachtet, in welchem Block Transaktionen mit bestimmten Gebührensätzen bestätigt wurden, und leitet daraus Vorhersagen ab. Seither hat sich die Methodik deutlich verfeinert, aber das Grundprinzip — empirische Beobachtung statt Hardcode — stammt aus Version 0.10.0. [[waltz-fact-25-bitcoin-core-fee-estimator]]

### Zeitpräferenz und Strategie

Nicht jede Zahlung ist dringend. Wer Zeit hat, kann bei niedrigem sat/vByte-Satz senden und Stunden oder Tage warten. Wer es eilig hat, zahlt mehr.

Moderne Wallets wie die BitBoxApp automatisieren diese Entscheidung: Im Sendeformular wählt man eine Prioritätsstufe (hoch / mittel / niedrig), die App berechnet den passenden sat/vByte-Satz anhand des aktuellen Mempool-Zustands. Manuelle Gebühreneingabe ist als Option in den Einstellungen verfügbar.

### Zusammenhang mit UTXOs

Jede UTXO, die als Input in einer Transaktion verwendet wird, vergrößert diese — und erhöht damit die absolute Gebühr. Viele kleine UTXOs (z.B. durch viele DCA-Käufe) können dazu führen, dass eine spätere Transaktion teuer wird. UTXO-Konsolidierung (mehrere kleine UTXOs zu einer größeren zusammenfassen) in Phasen niedriger Gebühren ist eine gängige Optimierungsstrategie.

## Related

- [[utxo-modell-und-konsolidierung]]
- [[bitcoin-adresstypen]]
- [[konsensregeln-und-mempool-richtlinien]]

## Open Questions

- Wie entwickeln sich Gebühren langfristig, wenn das Block-Subsidy abnimmt und Gebühren die Haupteinnahme der Miner werden?
- Sind Gebühren in Lightning-Kanälen ein ausreichender Ersatz für On-Chain-Gebühren für Miner-Incentives?
