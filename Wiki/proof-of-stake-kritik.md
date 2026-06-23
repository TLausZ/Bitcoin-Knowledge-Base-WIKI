# Proof-of-Stake: Sicherheitsprobleme und Worst-Case-Versagen

**Status:** established
**Last updated:** 2026-06-22
**Sources:** [[aprycot-nguyen-pos-falsche-denkweise]], [[aprycot-nguyen-pos-private-schluessel-faelschungssicher]]

## Summary

Hugo Nguyen analysiert in zwei Artikeln (2018), warum Proof-of-Stake in Worst-Case-Szenarien fundamental schlechter abschneidet als Proof-of-Work. Der Kern: PoS-Protokolle lösen Netzwerkpartitionen und Schlüsselangriffe nicht deterministisch, während PoW einen objektiven Maßstab für Fork-Auflösung bietet. Die entscheidende Erkenntnis: Die eigentliche Kerninnovation von Bitcoin ist nicht Zufall oder Anreizdesign, sondern *fälschungssichere Kostspieligkeit* (unforgeable costliness) — ein Konzept, das PoS-Designer systematisch ignorieren.

## Body

### Die Ingenieursperspektive und ihre blinden Flecken

Software für kritische Infrastruktur muss mit extremen Worst-Case-Szenarien umgehen. Flugzeuge, Kernreaktoren, Brücken — in diesen Bereichen ist Ingenieurspraxis auf katastrophale Ausfälle ausgerichtet, auch wenn die Wahrscheinlichkeit gering erscheint. Bitcoin ist als Basis des globalen Zahlungssystems potenziell sicherheitskritischer als fast alle existierende Software.

Nguyen kritisiert, dass PoS-Forscher diese Denkweise nicht anwenden. Sie optimieren für durchschnittliche Fälle, nicht für Extrema. Die Challenger-Katastrophe (1986) illustriert das Problem: NASA schätzte die Versagenswahrscheinlichkeit auf 1:100.000 — die tatsächliche lag bei etwa 1:100. Eine tausendfache Fehlkalkulation, weil Ingenieure nicht systematisch für das Schlimmste entwarfen. [[aprycot-nguyen-pos-falsche-denkweise]]

### Worst-Case 1 und 2: Netzwerkpartition

**Szenario: Das Netzwerk fällt aus und startet neu.** In PoW-Systemen löst sich der Konflikt automatisch: Alle Knoten wählen die Chain mit der akkumulierten Arbeit (longest chain). Das Verhalten ist deterministisch, keine menschliche Intervention nötig. In PoS gibt es keinen objektiven Maßstab. Welche der entstehenden Chains ist "richtiger"? Das Protokoll weiß es nicht. Das Ergebnis kann dauerhafter Split sein.

**Szenario: Teile des Netzwerks werden isoliert.** BGP-Hijacking durch staatliche Akteure ist technisch demonstriert (Türkei 2014 gegen Twitter, Chinas Great Firewall). Bei PoW: isolierte Partitionen schürfen weiter, aber nach Reconnect entscheidet die akkumulierte Arbeit. Bei PoS: isolierte Partitionen können keine forks fehlerfrei auflösen, weil kein physisches Gewicht die Auswahl bestimmt.

Das Grundproblem: PoW-Blöcke haben physisches Gewicht durch aufgewandte Energie. PoS-Blöcke bestehen aus Nullen und Einsen ohne inhärente Kostspieligkeit. Ohne Kosten lassen sich Blöcke fälschen — das "Scheingewicht" eines PoS-Blocks ist subjektiv und manipulierbar. [[aprycot-nguyen-pos-falsche-denkweise]]

### Worst-Case 3: Angriffe auf private Schlüssel

**Alte Schlüssel (Nothing-at-Stake):** In frühen PoS-Varianten konnten Validatoren, die ihre Coins längst verkauft hatten, trotzdem an Validierung teilnehmen. Jemand, der alte Schlüssel erwirbt, kann damit die Geschichte umschreiben — ohne Kosten, weil kein Mining nötig. Neuere PoS-Versionen verwenden "dynamische Validierung", wodurch alte Schlüsselinhaber ihr Recht verlieren. Aber neu gestartete oder lange offline gebliebene Nodes bleiben anfällig: Sie können nicht feststellen, ob jemand seine Coins zwischenzeitlich verkauft hat.

**Neue Schlüssel (1/3-Schwelle):** Ein Angreifer mit Schlüsseln, die 1/3 des Stakes kontrollieren, kann zwei gleichwertige Blöcke gleicher Höhe erzeugen. Kein Rest des Netzwerks kann feststellen, welcher "echter" ist. Bei PoS-Protokollen wie Tendermint oder Casper führt das zum Protokollstopp: Kein Block kann mehr als finalisiert gelten, das System friert ein. [[aprycot-nguyen-pos-private-schluessel-faelschungssicher]]

**Staking-Rate und reale Angriffsschwelle:** Diese 1/3-Grenze gilt für *aktiv stakende* Coins. Wenn nur 50% der Coins staken, braucht ein Angreifer nur 1/6 des Gesamtangebots. Bei 25% Beteiligung nur 1/12. Da Vermögensverteilung Potenzgesetzen folgt, ist dieser Schwellenwert für wenige reiche Akteure erreichbar. Je niedriger die Staking-Rate, desto bedrohlicher.

Dazu kommt: Staking-Schlüssel müssen dauerhaft online sein, um Transaktionen zu signieren. Diese permanente Konnektivität erhöht die Angriffsfläche für Hacks drastisch.

**PoW im Vergleich:** Wer die Mehrheits-Hashrate erlangt, kann Doppelausgaben versuchen — muss aber weiterhin Mining-Kosten zahlen. Die Erlangung der Mehrheits-Hashrate gibt dem Angreifer keine unbegrenzte Macht; er muss für jeden Angriff real zahlen. Bei PoS gewährt Mehrheitsstaking unbegrenzte Macht kostenlos. PoW bietet zwei Schutzschichten: Kontrolle erlangen *und* Geld für Angriffe ausgeben. PoS bietet nur eine.

### Die drei Zutaten der Kerninnovation

Nguyen identifiziert drei Komponenten, die Bitcoin zusammen einzigartig machen:

1. **Zufall** — kryptografische Zufallsauswahl des nächsten Block-Produzenten
2. **Fälschungssichere Kostspieligkeit** (unforgeable costliness) — Blöcke kosten echte physische Ressourcen
3. **Anreize** — Spieltheorie, die ehrliches Verhalten profitabler macht als Angriff

PoS-Designs fokussieren auf (1) und (3). DFINITY war obsessiv über Zufall, Ethereum Casper über Anreizsysteme ("Kryptoökonomie"). Komponente (2) fehlt in beiden — und das ist keine Kleinigkeit.

Fälschungssichere Kostspieligkeit ist der Teil, der in keine einzelne akademische Disziplin passt. Sie verbindet Physik, Evolutionspsychologie (Nick Szabos Forschung über Sammlerstücke und Geldursprung), Ökonomie und Archäologie. Gerade weil sie interdisziplinär ist, wird sie übersehen. [[aprycot-nguyen-pos-private-schluessel-faelschungssicher]]

Das Argument in einem Satz: Ohne fälschungssichere Kostspieligkeit hat ein digitaler Block kein echtes Gewicht. Ein Block aus Nullen und Einsen, der nichts kostet, kann reproduziert, gefälscht und manipuliert werden. Was das Gewicht eines PoW-Blocks ausmacht, ist die direkte, prüfbare Verbindung zwischen dem Block-Hash und der aufgewandten Energie.

### Konkrete PoS-Implementierungen im Vergleich

**Tendermint:** Gibt offen zu, dass das Protokoll bei einem 1/3-Angriff stoppt. Lösung: Validatoren sollen sich "koordinieren" und extern entscheiden, welcher Fork gilt. Das ist keine Protokolleigenschaft, sondern ein Aufruf zu manueller menschlicher Intervention — unvereinbar mit dem Ziel automatisierter, skalierbarer Finanzinfrastruktur.

**Ethereum Casper:** Kann ebenfalls bei 1/3-Kontrolle durch einen Gegner einfrieren. Das "Inaktivitätsleck" bestraft offline gehende Validatoren — aber das öffnet einen neuen Angriffsvektor: Ein Angreifer kann ehrliche Validatoren per DDoS offline zwingen und sie gleichzeitig bestrafen, um die Staking-Rate zu senken und die Angriffsschwelle weiter abzusenken.

**DFINITY:** Verwendet zufällig gewichtete Validatoren ("Random Beacon"), aber das Gewicht ist subjektiv. Nodes, die über die Zufälligkeit uneinig sind, haben keine Möglichkeit, objektiv zu entscheiden. Ein Angreifer mit 1/3 der Validatoren kann in bestimmten Teilmengen überrepräsentiert sein und mehr als 1/3 der Gewichtung kontrollieren.

## Related

- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-vs-krypto]]
- [[bitcoin-digitale-knappheit]]
- [[hashcash]]

## Open Questions

- Löst Ethereums Transition zu PoS (Merge, 2022) die Worst-Case-Probleme — oder verlagert sie sie nur?
- Gibt es empirische Daten zu tatsächlichen PoS-Netzwerkausfällen, die Nguyens Argumente bestätigen oder widerlegen?
- Kann "nichts auf dem Spiel" (nothing-at-stake) durch Slashing vollständig eliminiert werden, oder bleiben Residualrisiken?
