# Bitcoin als Allmende: Governance und Rehypothecation

**Status:** established
**Themen:** philosophie
**Last updated:** 2026-06-22
**Sources:** [[aprycot-nur-die-staerksten-7-fazit-anhaenge]]

## Summary

Allen Farrington und Big Al wenden in Teil 7 von "Only the Strong Survive" Elinor Ostroms Theorie der gemeinsamen Ressourcen (Allmende) auf Bitcoin und Ethereum an. Das Ergebnis ist klar: Bitcoin erfüllt Ostroms Gestaltungsprinzipien für stabile Gemeinschaftsgüter ausgezeichnet; Ethereum, besonders nach dem Übergang zu Proof-of-Stake, erfüllt sie schlecht. Im Anhang folgt eine algebraische Analyse der Rehypothecation, die zeigt, warum DeFi-Systeme mit Unterbesicherung strukturell instabil sind.

## Body

### Ist Geld ein öffentliches Gut?

Die Behauptung, Bitcoin "privatisiere" ein öffentliches Gut, setzt voraus, dass Geld ein öffentliches Gut ist. George Selgin widerspricht der BIZ: Das Argument, Geld sei ein öffentliches Gut, ist ein Debatten-Stopper — ein magisches Wort, das verhindert, dass das staatliche Geldmonopol verteidigt werden muss.

Elinor Ostrom liefert die präzisere Kategorisierung: Geld ist eine gemeinsame Ressource (Allmende). Eine Allmende hat hohe Ausschlusskosten (ähnlich wie ein öffentliches Gut), ist aber subtrahierbar — wenn Alice Geld druckt, hat Bob seine Münzen nicht verloren, aber sein Geld ist entwertet worden. Der Konsens, den die Münzen repräsentieren, wurde verwässert. Das ist Subtraktion im institutionellen Sinne.

Ostroms Hauptthese: Viele Allmenden können ohne staatliches Eingreifen stabil verwaltet werden — durch effektive Gemeinschaften, Beziehungen und Anreize.

### Die acht Gestaltungsprinzipien

Ostrom identifizierte acht Merkmale stabiler Allmende-Governance. Die Bewertung von Bitcoin und Ethereum:

**I — Klar definierte Grenzen:** Bitcoin ja: unveränderlicher Emissionsplan, kryptografisch durchgesetzte Eigentumsrechte. Ethereum eingeschränkt: ständige Protokollanpassungen verwischen die Grenzen.

**II — Übereinstimmung mit lokalen Bedingungen:** Für globales Geld weitgehend irrelevant.

**III — Kollektive Entscheidungsfindung:** Bitcoin verlangt nahezu vollständigen Nutzer-Konsens für Regeländerungen — eine Änderung ohne diese Zustimmung spaltet die Chain. Ethereum hat klare Autorität bei wenigen Kernentwicklern und Investoren; mit PoS ist die Entscheidungsgewalt noch konzentrierter bei grossen Stakern.

**IV — Rechenschaftspflichtige Monitore:** Bitcoin ist hier wahrscheinlich die am besten konzipierte Allmende der Geschichte. Jeder kann ohne Kosten das Verhalten der "Anreigner" (Miner, potenzielle Inflationierer) überprüfen — ein Full Node reicht. Ethereum: theoretisch möglich, aber die grosse Datenstruktur und die Abhängigkeit von Drittinfrastruktur machen unabhängige Verifikation praktisch schwierig.

**V — Abgestufte Sanktionen:** Bitcoin: regelwidriges Verhalten (ungültige Blöcke) wird sofort und automatisch abgestraft — kein Komitee, kein Ermessen. Ethereum ähnlich, aber Regeländerungen benötigen weniger Konsens.

**VI — Kostengünstige Konfliktlösung:** Bitcoin: Thermodynamik und Mathematik als Schiedsrichter. Ethereum: Konfliktlösung hängt von wenigen mächtigen Personen ab — Vitalik Buterin als faktischer Entscheidungsträger ist keine stabile Governance-Struktur.

**VII — Keine Anfechtung durch externe Behörden:** Bitcoin strukturell unangreifbar durch Dezentralisierung. Ethereum: fragwürdig, da validating Nodes mehrheitlich in wenigen zentralisierten Rechenzentren laufen.

**VIII — Mehrebenen-Organisation:** Beide ja, wobei Bitcoin als robusteres Fundament für höhere Schichten dient. [[aprycot-nur-die-staerksten-7-fazit-anhaenge]]

### Die Konsequenz für das Governance-Argument

Das Gegenargument lautet: Ethereum und Altcoins haben technische Schwächen, gleichen diese aber durch überlegene soziale und Governance-Eigenschaften aus. Ostroms Analyse widerlegt das. Nicht nur sind die Governance-Eigenschaften von Kryptowährungen nicht besser — sie sind nach einem der rigorosesten analytischen Rahmen dafür deutlich schlechter. Dezentralisierung ist kein Luxus, sondern die Voraussetzung für stabile Allmende-Governance.

### Algebra der Rehypothecation

Rehypothecation bezeichnet die Praxis, dieselbe Sicherheit mehrfach als Grundlage für neue Vermögenswerte zu verwenden — ein Mechanismus, der im traditionellen Finanzsystem und im DeFi-Raum verbreitet ist.

Beispiel mit 50 % Überbesicherung (150 % Besicherungsquote): Um 100 Dollar an neuen Vermögenswerten zu prägen, werden 150 Dollar als Sicherheit benötigt. Werden die 100 Dollar als neue Sicherheit eingesetzt, können daraus weitere 67 Dollar entstehen (100 × 100/150), dann weitere 44 Dollar, und so weiter. Die Grenze dieser geometrischen Reihe:

> $100 × Σ(2/3)^n = $100 × 3 = $300

Mit einer Besicherungsquote von x% ist k = (100%/x%), und das Maximum ausstehender synthetischer Vermögenswerte = $100 × k/(k-1).

Kritischer Punkt: Bei genau 100 % Besicherung divergiert die Summe — unendlich viele Iterationen erzeugen unbegrenzte synthetische Vermögenswerte aus einer endlichen Basis. Jede Besicherungsquote unter 200 % führt dazu, dass der Gesamtwert der Ausgabe nach vollständiger Rehypothecation die ursprüngliche Sicherheit übersteigt. Bei 175 % sind es nach drei Iterationen bereits mehr als die ursprüngliche Sicherheit, das Maximum liegt bei 233 Dollar.

Der Punkt bei 200 % Besicherung ist der Gleichgewichtspunkt: bei y = 2 (200 %) ist f(y) = y. Mehr als das schützt. Weniger destabilisiert.

DeFi-Systeme mit Besicherungsquoten unter 200 % sind damit strukturell anfällig für Kaskadenliquidationen, sobald Preisschwankungen eintreten — ein algebraisch beschreibbares Systemrisiko, das nichts mit dem jeweiligen Protokolldesign zu tun hat.

## Related

- [[bitcoin-schichtenarchitektur]]
- [[bitcoin-vs-krypto]]
- [[oesterreichische-kapital-und-geldtheorie]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-fehlannahmen]]

## Open Questions

- Hat das PoS-Ethereum nach der Merge-Transition die Governance weiter zentralisiert (Lido-Stake-Konzentration)?
- Wie verhält sich Ostroms Rahmen zu Bitcoin-Mining-Pools — sind sie eine Governance-Schwäche?
- Gibt es DeFi-Protokolle, die über 200 % Besicherung dauerhaft halten?
