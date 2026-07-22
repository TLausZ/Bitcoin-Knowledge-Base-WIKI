# Bitcoin Core Relay-Statement (2025)

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-07-22
**Sources:** [[Bitcoin Core development and transaction relay policy]]

## Summary

Am 6. Juni 2025 veröffentlichten 31 Bitcoin-Core-Beitragende auf bitcoincore.org eine gemeinsame Erklärung zum Verhältnis von Core-Entwicklung und Transaction-Relay-Policy. Kern der Position: Relay-Regeln dürfen der Abwehr von Denial-of-Service-Angriffen und der Gebührenschätzung dienen, sollen aber nicht das Weiterreichen von Transaktionen unterbinden, die anhaltende wirtschaftliche Nachfrage haben und zuverlässig in Blöcke gelangen. Das Statement ist die Antwort der Maintainer auf die Filter- und Datenspeicher-Debatte und bildet den Gegenpol zu Vorschlägen wie [[bip-0110]], die unerwünschte Nutzung über strengere Konsens- oder Relay-Regeln zurückdrängen wollen.

## Body

### Anlass

Das Statement steht im Kontext der seit 2023 laufenden Auseinandersetzung um nicht-finanzielle Daten in Bitcoin-Blöcken und die Frage, ob Node-Software solche Transaktionen über Relay-Filter zurückhalten soll (siehe [[op-return-und-datenspeicherung]]). Die Core-Beitragenden legen darin offen, nach welchen Grundsätzen sie über die Aufnahme- und Weiterleitungsregeln der Software entscheiden.

### Zwei Grundprinzipien

**Nutzer definieren das Netzwerk.** Bitcoin werde durch seine Nutzer bestimmt, die frei wählen, welche Software sie fahren und welche Policy sie durchsetzen. Core-Beitragende seien nicht in der Position, das vorzuschreiben. Sichtbar werde das an der langjährigen Praxis, kein Auto-Update einzubauen: Niemand kann Änderungen einseitig an die Nutzer ausrollen, jede Aktualisierung verlangt die aktive Entscheidung, eine neue Version — oder andere Software — zu installieren. Die Freiheit, beliebige Software zu betreiben, sei der wichtigste Schutz des Netzwerks gegen Zwang.

**Relay-Policy hat eine Grenze.** Als Entwickler sähen sie sich verantwortlich, die Software für ihren Zweck — Validieren und Weiterreichen von Blöcken und Transaktionen — möglichst effizient und verlässlich zu machen. Dazu gehörten Regeln gegen DoS-Angriffe und zur Gebührenbewertung, aber nicht das Blockieren von Transaktionen mit anhaltender wirtschaftlicher Nachfrage, die verlässlich in Blöcke aufgenommen werden.

### Die drei Ziele des Transaction Relay

Die Erklärung nennt drei Zwecke, an denen sich Relay-Regeln messen lassen sollen:

- **Vorhersagen, was gemined wird** — Grundlage für Gebührenschätzung, Fee-Bumping und viele DoS-Schutzstrategien in der Node-Software.
- **Blockpropagation beschleunigen** für Transaktionen, die voraussichtlich in den nächsten Block kommen. Geringere Latenz verhindert, dass grosse Miner unfaire Vorteile gewinnen.
- **Miner über gebührenzahlende Transaktionen informieren**, damit sie nicht auf Out-of-band-Einreichungswege angewiesen sind, die die Mining-Dezentralisierung untergraben.

Daraus folgt der zentrale Satz der Erklärung: «Knowingly refusing to relay transactions that miners would include in blocks anyway forces users into alternate communication channels, undermining the above goals.» Filter, die ohnehin block-fähige Transaktionen zurückhalten, treiben Nutzer also in direkte Miner-Kanäle und arbeiten damit gegen die eigenen Ziele.

### Historische Grenzen von Aufnahmeregeln

Die Beitragenden räumen ein, dass Aufnahmeregeln in der Vergangenheit wirksam waren, um ineffiziente Blockplatz-Nutzung zu entmutigen — solange das billig war. Das funktioniere aber nur, solange Nutzer und Miner mit den Alternativen zufrieden seien. Sobald sich ein wirtschaftlich tragfähiger Anwendungsfall entwickle, der mit den Policy-Regeln kollidiert, könnten Nutzer und Miner direkt zusammenarbeiten und jeden externen Beschränkungsversuch umgehen. Genau diese Möglichkeit sei ein wichtiger Teil von Bitcoins Zensurresistenz; Node-Software mit bevorzugtem Peering habe zudem gezeigt, dass sich die Filter der grossen Mehrheit der Nodes relativ leicht umgehen lassen. Realistischer sei es daher, wenn die Node-Software eine treffende Vorstellung davon anstrebt, was im nächsten Block landet, statt sich zwischen einwilligende Transaktionsersteller und Miner zu stellen.

### Keine Billigung, aber Akzeptanz

Ausdrücklich grenzt sich die Erklärung von einer Wertung ab: «This is not endorsing or condoning non-financial data usage, but accepting that as a censorship-resistant system, Bitcoin can and will be used for use cases not everyone agrees on.» Die Position sei nicht von allen Nutzern und Entwicklern geteilt; die Beitragenden hielten sie aber für im Interesse Bitcoins und wollten Aufnahmeregeln weiter an dessen langfristiger Gesundheit und am rationalen Eigeninteresse der Miner ausrichten — inklusive konkreter technischer Gründe wie Upgrade-Sicherheit, effizienter Blockbau und Schutz vor Node-DoS.

### Signatoren

Unterzeichnet ist das Statement von 31 Beitragenden, darunter mehrere langjährige Maintainer und Protokollentwickler: Pieter Wuille, Gloria Zhao, Ava Chow, Antoine Poinsot, Anthony Towns, Murch (Mark Erhardt), Sergi Delgado, Gregory Sanders, Sebastian Falbesoner und Matthew Zipkin. Die namentliche Zeichnung macht es zu einer Positionsbestimmung einzelner Entwickler, nicht zu einer formalen Protokolländerung: Das Statement ändert keine Regel, sondern erklärt die Grundsätze hinter künftigen Policy-Entscheidungen.

### Einordnung: Gegenpol zu BIP 110

Das Relay-Statement markiert die eine Seite der Datenspeicher-Debatte 2025/2026. Die Gegenseite formuliert sich in [[bip-0110]], das arbiträre Daten über einen temporären Softfork auf Konsensebene begrenzen will. quietNaN bringt die Lagerbildung auf den Punkt: Das «Core-Lager» halte die Verhinderung von Datennutzung für technisch unmöglich, das «BIP-110-Lager» versuche sie dennoch. Michael Saylors [[bip-0110|«110 Reasons»]] argumentiert in dieselbe Richtung wie das Statement — Relay- und Mining-Policy sowie der Gebührenmarkt statt Konsenszwang. Die Debatte schliesst an die Grundfrage des [[blocksize-war]] an: Wer bestimmt, welche gültigen Transaktionen Bitcoin verarbeitet?

## Related

- [[bip-0110]]
- [[op-return-und-datenspeicherung]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[transaktionsgebuehren-und-mempool]]
- [[bitcoin-netzwerk-und-nodes]]
- [[blocksize-war]]
- [[bitcoin-commons-und-governance]]

## Open Questions

- Wie hat sich die Filter-Debatte nach der Lockerung der data-carrier-Policy in Bitcoin Core 30.0 entwickelt?
- Verändert der Aufstieg alternativer Node-Software mit strengeren Filtern (z. B. Bitcoin Knots) das Relay-Gleichgewicht im Netzwerk?
