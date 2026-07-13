# Bitcoin-Einsteiger-Onboarding: Von der Börse zur eigenen Wallet

**Status:** established
**Themen:** grundlagen, self-custody, philosophie, adoption, wallets
**Last updated:** 2026-07-05
**Sources:** [[bitcoin-ratgeber_einleitung]], [[bitcoin-ratgeber_kapitel-02-sei-deine-eigene-bank]], [[bitcoin-ratgeber_kapitel-03-von-der-boerse-zur-eigenen-wallet]]

## Summary

Der erste und wichtigste praktische Schritt für einen Bitcoin-Einsteiger ist der Umzug der Coins von der Börse in eine eigene Wallet. Michael Wolfs "Bitcoin-Ratgeber" beschreibt diesen Umzug als konkreten Fünf-Schritte-Ablauf und stellt ein Prinzip in den Mittelpunkt: mit einem kleinen Testbetrag anfangen, die Wiederherstellung prüfen, erst dann größere Summen bewegen. Ein Adressfehler ist nicht rückgängig zu machen, deshalb testet man jeden Schritt, bevor Vertrauen entsteht.

## Body

### Warum der Umzug zuerst kommt

Wer Bitcoin auf einer Börse hält, besitzt einen Schuldschein, keine Bitcoin. Der Kollaps von FTX 2022 machte das für viele konkret: Die Coins existierten, sie gehörten nur jemand anderem. Das Leitmotiv des Ratgebers, "Don't trust, verify", meint auch das Buch selbst — kleine Beträge testen, bevor man mit größeren Summen handelt. Die technische und wirtschaftliche Begründung steht in [[selbstverwahrung-und-boersenrisiken]].

### Der Fünf-Schritte-Ablauf

1. **Wallet einrichten.** Eine empfohlene Wallet laden (Aqua für Smartphones, Sparrow für den Desktop). Beim ersten Start erzeugt die Software automatisch einen Seed.
2. **Seed sofort sichern.** Alle 12 oder 24 Wörter handschriftlich und in richtiger Reihenfolge auf Papier schreiben. Kein Screenshot, kein Foto.
3. **Empfangsadresse kopieren.** In der Wallet auf "Empfangen" gehen, die Adresse (lange Zeichenkette oder QR-Code) kopieren.
4. **Testbetrag senden.** Auf der Börse "Abheben" wählen, die Wallet-Adresse einfügen, einen kleinen Betrag senden (Gegenwert von etwa 10 bis 20 Euro). Adresse doppelt prüfen — erste und letzte sechs Zeichen vergleichen. Auf die Bestätigung warten (10 bis 60 Minuten).
5. **Bestätigung prüfen, Rest überweisen.** Kommt der Testbetrag in der Wallet an, funktioniert der Ablauf. Erst dann schrittweise den Rest übertragen.

### Der Testbetrag als Grundregel

Niemals sofort alles senden. Ein Fehler bei der Adresse ist unumkehrbar, es gibt keine Hotline und keine Stornierung. Der Testbetrag kostet nur eine kleine Gebühr und ein paar Minuten Wartezeit, deckt aber jeden Bedienfehler auf, bevor er teuer wird. Dieselbe Logik gilt für die Wiederherstellung: Die Recovery mit einem kleinen Betrag ausprobieren, bevor größere Summen von ihr abhängen.

### Custodial oder Non-Custodial

Zwei Arten, Bitcoin zu halten, mit einem klaren Trennkriterium — wer hält den Seed.

| Custodial (Börse/Dritter) | Non-Custodial (eigene Wallet) |
|---|---|
| Kein eigener Seed | Eigener Seed, echte Bitcoin |
| Dritter verwahrt die Schlüssel | Man verwahrt selbst |
| Kann sperren oder pleitegehen | Niemand kann die Coins wegnehmen |
| Gut zum Kaufen, schlecht zum Lagern | Richtig für langfristige Verwahrung |

Der Ratgeber fasst das im Bitcoin-Grundsatz "Not your keys, not your coins" zusammen. Zur begrifflichen Vertiefung siehe [[selbstverwahrung-und-boersenrisiken]].

### Wallet-Wahl für den Einstieg

Software-Wallets ("Hot Wallets") sind mit dem Internet verbunden und für kleinere Alltagsbeträge gedacht: Aqua (einfach, iOS und Android) oder Sparrow (Desktop, Open Source, mehr Kontrolle). Hardware-Wallets sind physische Geräte, deren privater Schlüssel das Gerät nie verlässt; der Ratgeber empfiehlt sie ab einigen hundert Euro Bestand und nennt BitBox02, Trezor Safe 7 und Coldcard Mk4. Hardware-Wallets ausschließlich direkt beim Hersteller kaufen, nie über eBay, Amazon oder secondhand — sonst droht ein manipuliertes Gerät. Details in [[hardware-wallet-einstieg]] und [[hardware-wallet-sicherheitsarchitektur]].

### Die ersten Satoshis

Ein Bitcoin besteht aus 100.000.000 Satoshis. Man muss keinen ganzen Bitcoin kaufen; zehn Euro reichen zum Ausprobieren. Beim Kauf empfiehlt der Ratgeber Wege ohne Identitätsnachweis, weil KYC-Daten bei einem Leak Name, Adresse und Bestand verknüpfbar machen. Kaufwege und Sparpläne (DCA) stehen in [[bitcoin-kaufen-und-dca]] und [[no-kyc-bitcoin]].

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-kaufen-und-dca]]
- [[no-kyc-bitcoin]]
- [[hardware-wallet-einstieg]]
- [[wallet-backup-strategien]]
- [[lightning-netzwerk-grundlagen]]

## Open Questions

- Ab welchem Betrag lohnt der Wechsel von Software- auf Hardware-Wallet in der Praxis? (Ratgeber: einige hundert Euro; hardware-wallet-einstieg nennt 500–1.000 €)
