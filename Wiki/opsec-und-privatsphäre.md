# OPSEC und Privatsphäre für Bitcoin-Nutzer

**Status:** established
**Last updated:** 2026-06-25 (Pass 53: Passphrase-Strategie, Gerätestapel-Kontext, Steuern DE)
**Sources:** [[20250522_sprich-nicht-über-deine-bitcoin]], [[20211220_bitbox02-bestellen-ohne-adresse-de]], [[20210320_shift-crypto-datenschutz-de]], [[aprycot-gigi-privatsphaere-in-bitcoin.md]], [[Das Privacy Handbuch – Timo Volkov (2025)]]

## Summary

Operational Security (OPSEC) bedeutet für Bitcoin-Nutzer: sorgfältig steuern, welche Informationen über den eigenen Bitcoin-Besitz nach außen dringen. Selbst kleine Details — exakte Beträge, Transaktions-IDs, Adressen — können mit anderen Daten kombiniert werden, um Rückschlüsse auf das Gesamtvermögen zu ziehen. Die größten Risiken entstehen durch unüberlegtes Teilen auf Social Media, unnötige Angeberei und das Preisgeben von Wallet-Strategien in öffentlichen Foren.

## Body

### Privatsphäre ist keine Geheimhaltung

Eric Hughes eröffnete das Cypherpunk's Manifesto (1993) mit der Unterscheidung: „Privatsphäre ist keine Geheimhaltung. Eine private Angelegenheit ist etwas, von dem man nicht will, dass die ganze Welt es weiß, aber eine geheime Angelegenheit ist etwas, von dem man nicht will, dass es irgendjemand weiß." Was man auf der Toilette tut, ist weder illegal noch geheim — aber man schließt die Tür. Dasselbe gilt für Finanzen.

Bitcoin ist bestenfalls pseudonym, nicht anonym. Jede in der Blockchain gespeicherte Transaktion bleibt öffentlich einsehbar, solange Bitcoin existiert. Wer jetzt keine Privatsphäre-Maßnahmen ergreift, riskiert künftige Nachteile — da Blockchain-Analyse mit der Zeit besser, nicht schlechter wird. [[aprycot-gigi-privatsphaere-in-bitcoin.md]]

### Acht Bewährte Praktiken (Gigi / Matt Odell)

Gigi und Matt Odell formulierten 2021 eine priorisierte Liste:

1. **Selbst verwahren** — Not your keys, not your coins. Wer andere für sich verwahren lässt, gibt alle Transaktionsdaten preis.
2. **Keine Adress-Wiederverwendung** — Zerstört die Privatsphäre beider Seiten einer Transaktion.
3. **KYC minimieren** — Verknüpfung der realen Identität mit Bitcoin-Adressen ist schwer rückgängig zu machen. Datenlecks von KYC-Diensten sind häufig. No-KYC-Alternativen existieren (Hodl Hodl, Bisq, Peach).
4. **Dritte minimieren** — „Vertrauenswürdige Dritte sind Sicherheitslücken" (Nick Szabo). Wenn möglich alles selbst betreiben.
5. **Eigenen Node betreiben** — Wer keinen eigenen Node hat, vertraut einem fremden Node. Der fremde Node sieht alle Anfragen.
6. **Lightning für kleine Transaktionen nutzen** — Off-Chain erhöht Privatsphäre mit wenig Aufwand. Onion Routing auf Lightning verbirgt Zahlungspfade.
7. **Keine öffentlichen Block-Explorer** — Adresssuchen verknüpfen Adressen mit IP-Adressen. Alternative: eigenen Block-Explorer auf dem Node betreiben, oder Tor/VPN.
8. **CoinJoin früh und oft** — Da Bitcoin permanent ist: kollaborative Transaktionen (Whirlpool, JoinMarket) verhindern künftige Rückverfolgung.

[[aprycot-gigi-privatsphaere-in-bitcoin.md]]

### Warum Transaktionsdaten privat sind

Bitcoin-Transaktionen sind öffentlich auf der Blockchain. Wer eine Bitcoin-Adresse kennt, kann alle damit verbundenen Transaktionen einsehen. Ein unscheinbarer Social-Media-Post mit einem exakten Kaufbetrag und einer Uhrzeit kann ausreichen, um die Transaktion auf der Blockchain zu identifizieren — und von dort aus das Gesamtvermögen zu rekonstruieren.

Jedes geteilte Detail hinterlässt einen digitalen Fingerabdruck. Vor dem Teilen sollten folgende Fragen gestellt werden:
- Ist diese Information privat, oder kann sie Rückschlüsse auf private Informationen ermöglichen?
- Ist es wirklich nötig, sie in diesem Kontext zu teilen?
- Mit wem teile ich sie — einer vertrauenswürdigen Person oder potenziell der ganzen Welt?
- Kann die Information mit anderen Daten kombiniert werden?

### Angeberei vermeiden

Bitcoin war in den vergangenen Jahren eine außergewöhnlich gute Investition. Das kann den Wunsch wecken, Familie, Freunden oder Fremden davon zu erzählen. Das Problem: Man kann nie vorhersagen, was jemand mit der Information „Ich habe sechsstellige Beträge in Bitcoin" anfängt. Im schlimmsten Fall führt es zu physischen Angriffen oder gezieltem Betrug.

Auch das Teilen mit Bekannten sollte mit Bedacht geschehen — nicht weil man niemandem vertrauen sollte, sondern weil die Entscheidung bewusst getroffen werden sollte.

### Wallet-Strategien allgemein halten

In Bitcoin-Foren oder auf Social Media sollte man nicht über die eigene konkrete Backup-Strategie sprechen. Statt „Ich bewahre meine Seedphrase im Passwort-Manager auf — ist das sicher?" besser: „Welche Methoden zur Aufbewahrung von Seedphrases werden empfohlen?" Kleine sprachliche Änderungen reduzieren den digitalen Fußabdruck erheblich.

### OPSEC im Alltag

Grundlegende OPSEC-Maßnahmen, die sich auf Bitcoin übertragen lassen:
- Passwort-Manager für alle Konten
- Zwei-Faktor-Authentifizierung
- Datenschutzfreundliche Dienste
- Bewusster Umgang mit sensiblen Informationen und deren Empfängern

Auch die Nutzung einer Hardware-Wallet und das sichere Verwahren des Backups gehören zur OPSEC.

### Hardware-Wallet anonym kaufen

Wer keine Spur hinterlassen möchte, dass er eine Hardware-Wallet besitzt, kann das Gerät an eine nicht-persönliche Lieferadresse bestellen. In Deutschland ermöglicht das DHL Packstation oder Postfiliale (mit DHL-Registrierung); in der Schweiz MyPost24-Automaten, PickPost oder Postlagernd (mit Post-Registrierung). Die eigene Wohnadresse erscheint dabei nirgends in den Lieferdaten. Das ist eine verhältnismäßig einfache Maßnahme für Nutzer, die den Besitz einer Hardware-Wallet nicht mit ihrer Hausadresse verknüpfen wollen.

### Datenschutz beim Wallet-Anbieter: Was Shift Crypto sammelt

Selbst ein seriöser Hardware-Wallet-Anbieter sammelt Daten — zum Beispiel die IP-Adresse beim Verbinden mit den eigenen Electrum-Servern. Shift Crypto veröffentlicht seine Datenschutzprinzipien:

- **Electrum-Server:** Shift betreibt eigene Server für die BitBoxApp. Die IP-Adresse der Verbindung ist bekannt, Bitcoin-Adressen werden nicht geloggt. Für vollständige IP-Anonymisierung: eigenen Node oder Tor nutzen (beides direkt in der BitBoxApp konfigurierbar).
- **Webshop:** Bestelldaten werden 30 Tage nach Lieferung gelöscht. Kreditkartenzahlungen laufen über Stripe — Shift speichert keine Kartendaten.
- **Kundensupport:** Ticket-Daten werden 23 Tage nach Schliessen gelöscht.
- **Pakete:** Versand als "Shift Switzerland", Produktbezeichnung "USB Stick" — kein Hinweis auf Bitcoin oder Hardware-Wallet auf der Außenseite.

Der praktische Rat: Wer maximale Privatsphäre will, betreibt einen eigenen Electrum Server oder Bitcoin Full Node und schaltet Tor in der BitBoxApp ein.

### Passphrase-Strategie: KYC und No-KYC trennen

Eine Passphrase (das «25. Wort») erzeugt aus denselben 24 Seed-Wörtern eine vollständig andere Wallet. Wer mehrere Passphrases nutzt, kann damit saubere Trennungen ziehen:

**KYC vs. No-KYC:** Bitcoin von regulierten Börsen landen auf einer Passphrase-Wallet, No-KYC-Bitcoin auf einer anderen. Beide teilen denselben Seed, aber ihre On-Chain-Adressen sind vollständig getrennt — solange man nie UTXOs beider Wallets in derselben Transaktion mischt.

**Wrench-Attack-Schutz (5-Dollar-Schraubenschlüssel-Attacke):** Wer unter physischem Druck steht, kann eine Passphrase für einen kleinen Betrag herausgeben. Der Großteil des Vermögens liegt auf einer anderen Passphrase, die dem Angreifer unbekannt ist.

**Vererbung:** Verschiedene Empfänger können dieselben 24 Wörter erhalten, aber jeder bekommt eine individuelle Passphrase — so hat jeder nur Zugriff auf seinen Teil.

Die Passphrase ist kein Passwort für das Gerät. Sie muss jedes Mal eingegeben werden und muss separat vom Seed gesichert werden — verliert man sie, sind die Coins auf dieser Wallet unwiederbringlich weg.

### Geräte-OPSEC als Voraussetzung für finanzielle Privatsphäre

Bitcoin-Privatsphäre beginnt nicht auf der Blockchain, sondern auf dem Gerät. Ein Windows-PC mit Standard-Browser zeichnet jeden Besuch einer Börsen-Website auf. App Stores protokollieren Wallet-Downloads. Ein kompromittiertes Gerät macht alle On-Chain-Maßnahmen wertlos.

Grundlage für ernsthafte Bitcoin-Privatsphäre: Ein Linux-Betriebssystem (Ubuntu oder ähnlich) oder GrapheneOS auf Android, ein Datenschutz-Browser (LibreWolf oder ähnlich), ein Passwortmanager (Bitwarden) und 2FA für alle Konten. Wer Bitcoin kauft oder verwaltet, sollte das auf einem Gerät tun, das er versteht und kontrolliert.

### Labeling: Jeden UTXO dokumentieren

Jede eingehende Transaktion sollte sofort mit einem Label versehen werden: Herkunft (Börse, Name, P2P-Kauf), Datum, Zweck. Sparrow Wallet hat eine Labeling-Funktion eingebaut. Das ist keine Bürokratie — wer nicht weiß, woher seine UTXOs stammen, kann beim Ausgeben keine fundierten Privatsphäre-Entscheidungen treffen. KYC-UTXOs, die versehentlich mit No-KYC-UTXOs gemischt werden, verlieren ihren Privatsphärevorteil dauerhaft.

### Bitcoin-Steuern in Deutschland (Überblick)

Bitcoin gilt in Deutschland steuerrechtlich als privates Veräußerungsgeschäft. Die wichtigsten Regeln (Stand 2025, kein Steuerberatungsersatz):

Wer Bitcoin länger als ein Jahr hält und dann verkauft, zahlt keine Kapitalertragsteuer — unabhängig vom Gewinn. Wer innerhalb eines Jahres verkauft, versteuert den Gewinn mit dem persönlichen Einkommensteuersatz. Liegt der Gewinn (nicht der Verkaufserlös) unter 600 € pro Kalenderjahr, ist er steuerfrei; wird die Grenze überschritten, muss der gesamte Betrag versteuert werden.

Als Verkauf gilt jede Transaktion, bei der Bitcoin gegen einen Gegenwert getauscht werden — also auch der Kauf eines Produkts mit Bitcoin. Transfers zwischen eigenen Wallets sind keine Veräußerung. Zur Berechnung der Haltefrist wird FIFO angewendet: Die zuerst gekauften Bitcoin gelten als zuerst verkauft.

### Ausnahmen: Wann Transparenz sinnvoll ist

Es gibt Situationen, wo offenes Sprechen über den eigenen Bitcoin-Besitz wichtig ist — vor allem bei der **Vererbungsplanung**. Wenn niemand weiß, dass man Bitcoin besitzt oder wo das Backup liegt, sind die Coins für Erben effektiv verloren.

## Related

- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[regulierung-tofr-aopp]]
- [[no-kyc-bitcoin]]
- [[coinjoin-und-on-chain-privatsphäre]]

## Open Questions

- Wie weit sollte man OPSEC in der Praxis treiben? Wo wird es unverhältnismäßig?
- Welche Steuer-Tools (Blockpit, Koinly) respektieren ihrerseits die Privatsphäre der Nutzerdaten?
