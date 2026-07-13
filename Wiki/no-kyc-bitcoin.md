# No-KYC Bitcoin kaufen

**Status:** established
**Themen:** protokoll, self-custody, privacy
**Last updated:** 2026-06-25
**Sources:** [[Das Privacy Handbuch_ Ein Ratgeber für digitale Sicherheit und Privatsphäre]], [[opsec-und-privatsphaere]], [[bitcoin-ratgeber_kapitel-03-von-der-boerse-zur-eigenen-wallet]]

## Summary

KYC (Know Your Customer) verknüpft eine Bitcoin-Adresse dauerhaft mit einer staatlich verifizierten Identität. Alle zukünftigen Transaktionen von dieser Adresse bleiben für Blockchain-Überwachungsfirmen, Börsen und Behörden nachverfolgbar. No-KYC-Bitcoin trennt diese Verbindung von Anfang an — durch P2P-Handel, Verdienen oder Tausch gegen Bargeld.

## Body

### Was KYC bedeutet und was es kostet

KYC-Verifikation bei einer Börse erzeugt einen dauerhaften Datensatz: Name, Adresse, Ausweisdokument, verknüpft mit den Bitcoin-Adressen, auf die ausgezahlt wird. Daraus folgen mehrere Risiken:

Erstens Datenlecks. Börsen, die Tausende Kundendatensätze halten, sind attraktive Ziele. Wenn persönliche Daten zusammen mit Bitcoin-Beständen im Darknet landen, betrifft das nicht nur die Privatsphäre, sondern kann die physische Sicherheit gefährden.

Zweitens Blockchain-Überwachung. Firmen wie Chainalysis kaufen Datensätze von Börsen und kombinieren sie mit On-Chain-Analyse. Wenn einmal bekannt ist, welche Adresse zu wem gehört, lässt sich die gesamte Ausgabehistorie rekonstruieren — rückwirkend und vorausschauend.

Drittens staatliche Kontrolle. Behörden können von Börsen Kontoinformationen verlangen, Bitcoin beschlagnahmen lassen oder künftige Dienste sperren.

### Wege zu No-KYC-Bitcoin

**Bitcoin verdienen.** Wer Produkte oder Dienstleistungen anbietet, kann Bitcoin direkt als Zahlung akzeptieren — ohne jede Vermittlerstelle. Das ist der sauberste Weg.

**Kauf gegen Bargeld (persönlich oder auf Meetups).** Bitcoin gegen Scheine, kein Datensatz. Die Herausforderung: einen Verkäufer zu finden. Bitcoin-Meetups in der eigenen Stadt sind ein guter Ausgangspunkt.

**Kauf auf P2P-Börsen.** Online-Plattformen vermitteln Käufer und Verkäufer direkt. Ein Preis-Aufschlag von typischerweise 5 % auf den Marktpreis ist üblich — dieser spiegelt den Wert der fehlenden KYC-Verknüpfung wider. Mit Geduld sind Angebote 1–3 % über Marktpreis findbar.

### P2P-Plattformen im Vergleich (Stand April 2025)

**PeachBitcoin** ([peachbitcoin.com](https://peachbitcoin.com)) — Schweizer Unternehmen, Open-Source-App für Mobilgeräte, gut für Einsteiger. Gebühren bei 200 €: ca. 2,00 €.

**RoboSats** ([robosats.com](https://robosats.com)) — vollständig anonyme Konten (Zufalls-Roboter-Identität), End-zu-End-verschlüsselt, läuft über Tor und Lightning Network. Gebühren bei 200 €: ca. 0,05 €. Derzeit eine der günstigsten und privatsten Optionen.

**Bisq** ([bisq.network](https://bisq.network)) — dezentrale Open-Source-Plattform ohne zentrale Instanz. Benutzeroberfläche ist komplexer als die anderen. Gebühren bei 200 €: ca. 2,30 € plus variable Bitcoin-Transaktionskosten.

**HodlHodl** ([hodlhodl.com](https://hodlhodl.com)) — etablierte P2P-Börse mit vielen Zahlungsoptionen. Bekannt dafür, unter bestimmten Umständen Zahlungs- und Transaktionsdaten weiterzugeben. Gebühren bei 200 €: ca. 1,20 €.

### Zahlungsmethoden bei P2P-Käufen

Bei Überweisungen über Fintech-Banken (Revolut, N26, Wise) sieht der Verkäufer meistens nur einen Kurznamen — keine IBAN, kein vollständiges Profil. Bei klassischen Banküberweisungen mit IBAN sind mehr persönliche Informationen sichtbar. Wenn die Privatsphäre gegenüber dem Verkäufer wichtig ist, sind Fintech-Transfers oder Bargeld besser.

### KYC- und No-KYC-Bitcoin sauber trennen

Wer beides hat — Bitcoin von einer regulierten Börse und No-KYC-Bitcoin — sollte sie nie in derselben On-Chain-Transaktion mischen. Sobald ein KYC-UTXO mit einem No-KYC-UTXO kombiniert wird, verliert Letzterer seinen Privatsphärevorteil. Die Trennung lässt sich durch separate Wallets und eine konsequente Passphrase-Strategie aufrechterhalten: eine Passphrase für die KYC-Coins, eine andere für No-KYC-Coins. Beide teilen dieselben 24 Seed-Wörter, führen aber auf vollständig getrennte Wallets.

Jede empfangene Transaktion sollte sofort mit einem Label versehen werden: Quelle (Börse, P2P, Person), Datum, Zweck. Sparrow Wallet hat dafür eine eigene Labeling-Funktion. Wer weiß, woher seine UTXOs stammen, kann beim Ausgeben bewusste Entscheidungen treffen und vermeidet ungewollte Verknüpfungen.

### Weitere Einsteiger-Optionen (Bitcoin-Ratgeber)

Michael Wolfs "Bitcoin-Ratgeber" nennt für den KYC-freien Einstieg zusätzlich GetBittr (SEPA-Überweisung ohne Ausweis, Auszahlung direkt auf die eigene Wallet), Bisq 2 als aktuelle Desktop-Version und den P2P-Weg Hodl Hodl im Browser. Als laufend gepflegte Übersicht KYC-freier Anbieter verweist er auf das Verzeichnis kycnot.me. Der Ratgeber begründet die Empfehlung mit dem Sicherheitsrisiko von KYC-Leaks: Wird eine Plattform gehackt, sind Name, Adresse und Bestand verknüpfbar — dokumentierte Fälle reichen bis zu gezielten Überfällen und Entführungen.

## Related

- [[opsec-und-privatsphaere]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[coin-control-und-utxo-auswahl]]
- [[sparrow-wallet]]

## Open Questions

- Wie entwickelt sich der regulatorische Druck auf P2P-Börsen in der EU (MiCA)?
- Bleibt RoboSats mit Lightning dauerhaft nutzbar, oder gerät auch dieses Modell ins Visier?
