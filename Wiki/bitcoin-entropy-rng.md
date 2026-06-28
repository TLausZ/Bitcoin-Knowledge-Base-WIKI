# Bitcoin Entropie und Zufallszahlen

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-quantum-rng-bitcoin-entropy]]

## Summary

Die Sicherheit eines Bitcoin-Wallets steht und fällt mit der Qualität der Entropie, die beim Erzeugen des privaten Schlüssels genutzt wird. Schlechte Zufallszahlen sind einer der häufigsten Angriffsvektoren. Alex Waltz demonstrierte 2021, dass sich physikalisch echte Zufälligkeit — radioaktiver Zerfall — in Bitcoin-Seeds übersetzen lässt.

## Body

### Warum echter Zufall schwer ist

Computer sind deterministische Maschinen. Pseudorandom Number Generators (PRNGs) erzeugen Zahlen aus einem Startwert (Seed) mit mathematischen Funktionen — deterministisch und reproduzierbar. Für kryptografische Anwendungen braucht man Entropie aus physikalischen Quellen (Tastaturanschläge, Maustiming, Festplattenrauschen). Selbst Würfel und Münzwürfe sind streng genommen deterministisch — nur schwer zu messen.

Radioaktiver Zerfall hingegen ist nach aktuellem physikalischem Verständnis intrinsisch nicht-deterministisch: Wann genau ein Atomkern zerfällt, ist prinzipiell unvorhersagbar.

### Der selbstgebaute Quantum-RNG

Alex Waltz extrahierte Americium-241 aus einem Rauchmelder (Halbwertszeit 432,2 Jahre) und verbannte es mit einem Geigerzähler und einem Raspberry Pi. Der Geigerzähler produziert bei jedem detektierten Teilchen einen Piepton; die Zeitabstände zwischen diesen Tönen sind das eigentliche Zufallssignal.

Für ein Bit Entropie werden vier aufeinanderfolgende Partikel gemessen: Ist die Zeit zwischen Partikel 1 und 2 größer als zwischen 3 und 4, ergibt das eine `1` — sonst eine `0`. Sind beide Abstände gleich, wird das Paar verworfen (von-Neumann-Debias). Ein Python-Skript verarbeitet die Daten direkt zu BIP39-Seeds.

Praktisch: ~6 Partikelzerfälle pro Sekunde → ~2,8 Minuten für einen 24-Wort-BIP39-Seed.

### Limitierungen

Der Geigerzähler hat eine Totzeit von ~150 µs — in diesem Fenster detektiert er keine Zerfälle, was eine systematische Verzerrung einführt. Audacity auf dem Raspberry Pi verlor gelegentlich Datenpunkte. Für einen formalen Nachweis der Zufälligkeit (z.B. mit Diehard-Tests) wären mindestens 6 Monate kontinuierliche Datensammlung nötig.

Der Vergleich von ~2 Wochen Daten (112 GB Rohaufnahmen, 159 KB verarbeitete Entropie) mit dem `ent`-Tool ergab ein „OKish" Bild — visuell zufällig, aber kein formaler Beweis.

### Praktische Implikationen

Der Aufwand zeigt, wie ernst das Entropie-Problem zu nehmen ist. Für die meisten Nutzer ist der Hardware-Wallet-TRNG (True Random Number Generator) die vernünftigere Wahl — ein guter TRNG kombiniert mehrere physikalische Quellen und ist auditiert. Selbst Würfeln mit einem fairen Würfel (Diceware) ist für die meisten Anwendungsfälle ausreichend.

Der interessante Aspekt des Projekts liegt weniger in der praktischen Empfehlung als in der Demonstration: Entropie ist ein physikalisches Phänomen, und ihr Ursprung lässt sich bis auf die Quantenebene zurückverfolgen.

## Related

- [[seedphrase-entropie-und-sicherheit]]
- [[diceware-und-seed-generierung]]
- [[bip39-schwache-seeds]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Sind kommerzielle TRNGs in Hardware-Wallets auditiert genug, oder sollte man zusätzliche externe Entropie einmischen?
- Wie anfällig sind Software-Wallets für schlechte PRNG-Implementierungen auf mobilen Betriebssystemen?
