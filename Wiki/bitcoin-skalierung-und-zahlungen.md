# Bitcoin: Skalierung und Zahlungen

**Status:** established
**Last updated:** 2026-06-23
**Sources:** [[aprycot-parker-lewis-bitcoin-nicht-zu-langsam]]

## Summary

Der Vergleich Bitcoin vs. Visa setzt eine falsche Konkurrenz voraus. Bitcoin konkurriert nicht mit Zahlungsnetzwerken, sondern mit der Federal Reserve als Währungsemittent und Abrechnungsschicht. Die digitale Knappheit ist Bitcoins 0-zu-1-Innovation (Thiel); Zahlungsskalierung ist ein 1-zu-n-Problem, das darauf aufbaut. Die begrenzte Blockkapazität ist kein Fehler, sondern das Fundament des Gebührenmarkts, der das feste Angebot langfristig sichert.

## Body

### Der falsche Vergleich: Bitcoin ≠ Visa

Visa verarbeitet ~4.000 Transaktionen/Sekunde, das Bitcoin-Basisnetzwerk schafft ~4,6 Transaktionen/Sekunde. Dieser Vergleich klingt vernichtend. Er ist auch vollständig irrelevant.

Visa ist ein Technologieunternehmen mit 17.000 Mitarbeitern. Es hilft, Dollar zu bewegen — ist aber nicht der Dollar. Bitcoin hat keine Mitarbeiter. Es ist Währungsemittent und Abwicklungsschicht zugleich, so wie die Federal Reserve der Abwicklungsmechanismus des Dollarsystems ist. Den richtigen Vergleich zieht Lewis so: Bitcoin gegen die New York Fed — nicht Bitcoin gegen Visa. Auf dieser Ebene sieht Bitcoin wie ein Ferrari aus: globale Endabrechnung alle ~10 Minuten, rund um die Uhr, ohne Genehmigung, ohne Schließzeiten. [[aprycot-parker-lewis-bitcoin-nicht-zu-langsam]]

### Digitale Knappheit: Das 0-zu-1-Problem

Peter Thiels Unterscheidung: 0 zu 1 ist eine Erfindung die zuvor nicht existierte. 1 zu n ist Skalierung des Bestehenden. Bitcoin ist 0 zu 1, weil es digitale Knappheit erschafft — ein Gut, das wirklich nicht beliebig kopiert werden kann. Das gab es nie zuvor.

Vor Bitcoin konnte jede digitale Datei beliebig kopiert werden. Bitcoin löste das Double-Spend-Problem ohne vertrauenswürdige dritte Partei. Diese Leistung ist außergewöhnlich. Im Vergleich dazu ist das Problem "wie machen wir Bitcoin-Zahlungen schneller?" ein ingenieurstechnisches 1-zu-n-Problem. Es ist lösbar; es muss nur noch nicht heute vollständig gelöst sein.

Die Schlussfolgerung ist logisch: Wenn menschlicher Einfallsreichtum das schwierigere Problem (digitale Knappheit) lösen konnte, wird er das einfachere Problem (Zahlungsskalierung) ebenfalls lösen. [[aprycot-parker-lewis-bitcoin-nicht-zu-langsam]]

### Warum begrenzte Blockkapazität kein Fehler ist

Bitcoin-Blöcke sind bewusst kapazitätsbegrenzt. Warum? Die Kausalkette:

**Feste Blockkapazität → Knappheit im Blockraum → Gebührenmarkt → Langzeitfinanzierung der Miner → festes Angebot bleibt vertretbar**

Miner werden heute hauptsächlich durch neue Bitcoin (Blocksubvention) bezahlt. Diese Subvention wird alle vier Jahre halbiert (Halvening) und läuft etwa im Jahr 2140 auf null aus. Danach müssen Transaktionsgebühren die Miner vergüten. Ohne Blockraumknappheit gäbe es keinen Wettbewerb um Blockplatz — und ohne Wettbewerb keine nennenswerten Gebühren. Das hieße: das feste Angebot wäre langfristig nicht absicherbar.

Blockraumknappheit ist also nicht Schwäche, sondern Schutz des wichtigsten Merkmals: der Zuverlässigkeit von 21 Millionen Bitcoin. [[aprycot-parker-lewis-bitcoin-nicht-zu-langsam]]

### Skalierung ist ein 1-zu-n-Problem: Lightning und Layer 2

Das Lightning-Netzwerk ist das bekannteste Beispiel für 1-zu-n-Skalierung auf Bitcoin. Es schafft bidirektionale Zahlungskanäle zwischen Teilnehmern, die Transaktionen sofort und günstig abrechnen — mit finaler Bitcoin-Abrechnung on-chain bei Kanalöffnung und -schließung.

Lewis' Einschätzung: Lightning ist erst der Anfang. Der wirtschaftliche Anreiz, auf Bitcoin aufzubauen, zieht Entwickler und Kapital an; der Wettbewerb wird bessere Lösungen produzieren. Der wichtige Punkt: Diese Innovationen müssen innerhalb der bestehenden Konsensregeln funktionieren oder breiten Konsens für Regeländerungen erreichen — was das Fundament schützt.

Bitcoin konkurriert auf der Basisschicht mit Gold und dem Dollar als Wertspeicher. Zahlungsnetzwerke wie Lightning konkurrieren mit Visa und Mastercard. Diese Schichtenstruktur ist analog zum bestehenden System: Fed (Basisschicht) + Geschäftsbanken + Visa/Mastercard (Zahlungsschicht). Bitcoin macht die Basisschicht offener, vertrauensloser und unmanipulierbar. [[aprycot-parker-lewis-bitcoin-nicht-zu-langsam]]

## Related

- [[bitcoin-zensurresistenz]]
- [[bitcoin-digitale-knappheit]]
- [[bitcoin-nicht-kopierbar]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-netzwerk-und-nodes]]
- [[lightning-netzwerk]]

## Open Questions

- Ab welchem Adoptionsniveau sind Transaktionsgebühren allein ausreichend, um die Mining-Sicherheit zu finanzieren?
- Wie verändert Lightning-Adoption die On-Chain-Gebührenstruktur und damit die Mining-Ökonomie?
