# Grokking Bitcoin / Bitcoin begreifen (Kalle Rosenbaum)

**Status:** established
**Themen:** protokoll, buecher
**Last updated:** 2026-07-13
**Sources:** [[Bitcoin-begreifen_Rosenbaum-Herminghaus-DE]]

## Summary

Kalle Rosenbaums technische Einführung, hier in der deutschen Ausgabe „Bitcoin begreifen" (übersetzt von Volker Herminghaus). Das Buch erklärt, wie Bitcoin auf Protokollebene funktioniert, und baut das Verständnis Schicht für Schicht auf — von Hashfunktionen bis Segregated Witness. Es richtet sich an technisch interessierte Leser, die nicht nur wissen wollen *warum*, sondern *wie* Bitcoin arbeitet; jedes Kapitel enthält Übungen.

## Body

### Einordnung

Als Referenz- und Lernbuch gehört „Bitcoin begreifen" neben *Mastering Bitcoin* zur technischen Standardliteratur, ist aber didaktischer angelegt: Konzepte werden mit Diagrammen und einem durchgehenden Beispiel entwickelt, nicht mit Code-Listings. Es ist kein Ideen- oder Ökonomiebuch, weshalb es hier bewusst als Kurzeintrag geführt wird — die Substanz sind die einzelnen technischen Konzepte, die im Wiki eigene Artikel haben.

### Kapitelübersicht

1. Einführung in Bitcoin
2. Kryptografische Hashfunktionen und digitale Signaturen → [[elliptische-kurven-kryptographie]], [[digitale-signaturen-ecdsa]]
3. Adressen → [[bitcoin-adresstypen]]
4. Wallets → [[hd-wallets-und-schluesselableitung]]
5. Transaktionen → [[utxo-modell-und-konsolidierung]]
6. Die Blockchain → [[bitcoin-blockchain-struktur]]
7. Proof of Work (Arbeitsnachweis) → [[bitcoin-mining-und-proof-of-work]]
8. Peer-to-Peer-Netzwerk → [[bitcoin-netzwerk-und-nodes]]
9. Nochmal zurück zu Transaktionen (Script) → [[bitcoin-script-und-output-locks]]
10. Segregated Witness → [[segregated-witness-segwit]]
11. Bitcoin Upgrades (Soft/Hard Forks)

Anhang: Benutzung von `bitcoin-cli`, Lösungen zu den Übungen, Web-Ressourcen.

### Nutzen

Wer die verlinkten Konzeptartikel vertiefen will, findet im Buch die ausführliche, schrittweise Herleitung mit Übungsaufgaben. Für das Wiki dient dieser Eintrag als Zeiger: Er ordnet das Buch ein und verbindet seine Kapitel mit den bestehenden technischen Artikeln.

## Related

- [[mastering-bitcoin]]
- [[utxo-modell-und-konsolidierung]]
- [[segregated-witness-segwit]]
- [[bitcoin-mining-und-proof-of-work]]

## Open Questions

- Wie aktuell ist die Ausgabe bezüglich Taproot und späterer Upgrades, die nach Erscheinen kamen?
