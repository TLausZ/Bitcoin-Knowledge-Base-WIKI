# Bitcoin Seed Cracking: Praktische Angriffsflächen

**Status:** established
**Themen:** self-custody
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-ethereum-wallet-hack]]

## Summary

Alex Waltz gewann 2022 ein öffentliches Seed-Cracking-Bounty für ein Ethereum-Wallet mit 0,1 ETH. Der Angriff dauerte insgesamt 10 Tage, nutzte 16 GPU-Server, schaffte 1 Million Seed-Prüfungen pro Sekunde — und endete mit ~50 $ Gewinn nach Serverkosten. Die Geschichte illustriert, wie robust ein korrekt erzeugter BIP39-Seed ist, aber auch wie schnell ein teilweise kompromittierter Seed crackbar wird.

## Body

### Ausgangssituation: Seed aus Bilderrätseln

Das Bounty bestand aus Fotografien, die Hinweise auf die 12 BIP39-Wörter enthielten. Waltz identifizierte 11 Wörter sicher und hatte für mehrere Positionen mehrere Kandidaten.

Erste Schätzung: ~5 Millionen mögliche Kombinationen aus den Kandidaten. Auf einem M1 Mac (90.000 Seeds/Sekunde) wären das wenige Minuten. Aber das Target-Wallet war nicht dabei → mindestens eine Schätzung war falsch.

### Eskalation: Ein unbekanntes Wort

Mit einem unbekannten Wort auf einer Position steigen die Kombinationen auf 2.048 × Kandidaten der anderen Positionen. Mit allen drei Laptops zusammen (170.000 Seeds/s) wären das Tage. Da das Bounty öffentlich war, liefen andere gleichzeitig.

Lösung: Cloud-GPU-Cluster über [vast.ai](https://vast.ai). 16 Server, zusammen 1.096.000 Seeds/Sekunde. Kosten: ~\$1/Stunde. Erwartet: 11 Stunden.

### Was BTCRecover macht

BTCRecover ist ein Open-Source-Tool, das Wort-Kombinationen für BIP39-Seeds generiert und prüft, ob sie eine gegebene Bitcoin- oder Ethereum-Adresse ableiten. Es nutzt GPU-Parallelisierung über OpenCL. Das macht es sowohl zum Standard-Tool für ehrliche Wallet-Recovery als auch für Bounty-Hunting.

### Ergebnis

11 Stunden Cracking: kein Treffer. Ein nochmaliger Blick auf die Bilder — Wort 8 war nicht „park", sondern „hard" (ein Straßenschild). Mit der korrigierten Kandidatenliste: 4 Minuten später gefunden.

Einnahmen: 0,1 ETH abzüglich Serverkosten und Tool-Donation ≈ \$50. Zeitaufwand: 10 Tage.

### Was das für Seed-Sicherheit bedeutet

Ein vollständig zufälliger 12-Wort-BIP39-Seed hat 128 Bit Entropie (2¹²⁸ Kombinationen). Selbst mit 1 Billion Versuchen pro Sekunde dauert ein Brute-Force-Angriff länger als das Alter des Universums. Das Bounty war crackbar, weil von Anfang an strukturierte Informationen über die Wörter vorlagen: ein Teilkompromiss von ~3 Positionen reduzierte den Suchraum auf Millionen statt 10³⁸.

Ein einzelnes durchgesickertes oder erratenes Wort bei einem 12-Wort-Seed reduziert die Entropie um etwa 11 Bits — von 128 auf ~117. Das klingt harmlos, aber kombiniert mit weiteren schwachen Positionen kann es praktisch angreifbar werden.

## Related

- [[seedphrase-entropie-und-sicherheit]]
- [[bip39-schwache-seeds]]
- [[bitcoin-entropy-rng]]
- [[wallet-backup-strategien]]
- [[hardware-wallet-angriffsvektoren]]

## Open Questions

- Wie sicher ist ein 24-Wort-Seed mit einer starken Passphrase im Vergleich zu einem 12-Wort-Seed ohne?
- Welche Rolle spielen GPU-Cluster für zukünftige Angriffe auf schlecht generierte Seeds?
