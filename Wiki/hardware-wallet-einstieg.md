# Hardware-Wallet — Warum und für wen

**Status:** established
**Last updated:** 2026-06-06
**Sources:** [[20200409_wieso-hardware-wallet-bitcoin-de]]

## Summary

Bitcoin besitzen bedeutet, einen privaten Schlüssel besitzen. Wer diesen Schlüssel einer Börse überlässt, besitzt keinen Bitcoin — nur eine Forderung. Wer ihn auf einem vernetzten Computer speichert, riskiert Diebstahl durch Malware. Eine Hardware-Wallet schließt diese Lücke: Sie hält den Schlüssel offline und isoliert, lässt aber trotzdem sichere Transaktionen zu. Für regelmäßige Transaktionen und Beträge, die man nicht verlieren möchte, ist eine Hardware-Wallet der pragmatische Standard.

## Body

### Was es bedeutet, Bitcoin zu besitzen

Bitcoin "besitzen" bedeutet genau: einen privaten Schlüssel besitzen, der über Bitcoin an einer bestimmten Adresse in der Blockchain verfügen kann. Wer diesen Schlüssel kennt — ob Mensch oder Programm — hat volle Kontrolle. Es gibt keinen Kundendienst, keine Rückbuchung, keinen Notfallzugang.

### Die vier Aufbewahrungsoptionen

**Option 1: Bitcoin auf einer Börse lassen**

Einfach und der übliche Einstieg. Das Problem: Die Börse hält den privaten Schlüssel, nicht der Nutzer. Die Börse kann gehackt werden, insolvent gehen oder Abhebungen unter regulatorischem Druck sperren. Börsen sind selten versichert und kaum reguliert. "Not your keys, not your coins."

**Option 2: Software-Wallet**

Der private Schlüssel liegt auf dem Computer oder Smartphone des Nutzers. Das ist besser als Option 1 — aber ein mit dem Internet verbundenes Gerät ist angreifbar. Malware, Sicherheitslücken, Keylogger: Ein Angreifer, der Zugang zum Schlüssel bekommt, kann alle Coins ohne Chance auf Rückholung stehlen. Für tägliche Ausgaben kleiner Beträge akzeptabel, nicht für Ersparnisse.

**Option 3: Hardware-Wallet (empfohlen für grössere Beträge)**

Ein spezialisiertes Gerät speichert den privaten Schlüssel offline und isoliert. Zwei Kernfunktionen: (1) Den Schlüssel vor unberechtigtem Zugriff schützen. (2) Transaktionsdetails auf dem eingebauten Display anzeigen, damit der Nutzer prüfen kann, was er signiert.

Die Wallet-App auf dem Computer hat keine privaten Schlüssel. Sie bereitet Transaktionen vor und schickt sie ans Gerät. Das Gerät zeigt die Details, der Nutzer bestätigt — dann signiert das Gerät und gibt nur die fertige Signatur zurück. Der Schlüssel verlässt das Gerät nie.

**Option 4: Air-Gap-Setup mit dedizierter Hardware**

Das Glacier Protocol und ähnliche Ansätze nutzen Computer ohne Netzwerkverbindung (Netzwerkkarte entfernt) für maximale Isolation. Für die langfristige Aufbewahrung sehr grosser Summen relevant. Erhebliches Fehlerpotential, komplex, für regelmäßige Nutzung ungeeignet.

### Was man nicht tun sollte: Paper Wallets

Paper Wallets (gedruckte Adressen und private Schlüssel) galten früh als sicher, haben sich aber als problematisch erwiesen. Drei Gründe: Es ist schwierig, den Schlüssel ohne Internetkontakt sicher zu generieren. Die eingedruckte Adresse wird oft mehrfach wiederverwendet (schlechte Privatsphäre). Wer eine Transaktion senden will, muss die gesamte Paper Wallet leeren — das ist vielen nicht bewusst.

Vorgenerierte Schlüssel auf Metall-Produkten oder "professionellen Krypto-Banknoten": Hier ist nicht beweisbar, dass der Hersteller keine Kopie des Schlüssels hat.

### Empfohlene Kombination

Für die meisten Nutzer ergibt eine Kombination Sinn:

- **Mobiles Wallet** (Lightning oder On-Chain) auf dem Smartphone für kleine Beträge im Alltag.
- **Hardware-Wallet** für grössere Beträge und regelmäßige Transaktionen.
- **Hardware-Wallet mit Passphrase** für die langfristige Aufbewahrung bedeutender Summen an einem sicheren Ort.

### Worauf es beim Kauf ankommt

Hardware-Wallets unterscheiden sich in Sicherheitsniveau und Trade-offs. Relevant: Secure Chip (physischer Schutz), Open-Source-Firmware (überprüfbar, kein blindes Vertrauen), eigenes Display (Transaktionen verifizierbar), BIP-39-Backup (herstellerunabhängige Wiederherstellung). Jeder Hersteller sollte ein Threat Model veröffentlichen, das erklärt, vor welchen Angriffen das Gerät schützt und vor welchen nicht.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[wallet-backup-strategien]]
- [[optionale-passphrase]]

## Open Questions

- Ab welchem Betrag rechtfertigt sich der Aufwand einer Hardware-Wallet?
