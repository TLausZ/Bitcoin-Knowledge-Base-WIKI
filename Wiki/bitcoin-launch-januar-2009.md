# Bitcoin-Launch Januar 2009: Forensische Frühgeschichte

**Status:** established
**Themen:** grundlagen, protokoll, geschichte, satoshi
**Last updated:** 2026-06-27
**Sources:** [[1stbitcoinminer-com_transcriptions.md]]

## Summary

Alex Waltz hat in einer fünfmonatigen forensischen Untersuchung die ersten 170 Blöcke der Bitcoin-Blockchain analysiert und dabei mehrere bisher unbekannte Fakten über Bitcoins Launch herausgearbeitet. Zentrale Erkenntnis: Hal Finney verpasste den Launch, war nicht der zweite Node im Netzwerk, und die beiden anderen Nodes, die bei Hals Beitritt bereits online waren, gehörten wahrscheinlich beide Satoshi Nakamoto. Das Netzwerk hielt in den ersten 170 Blöcken acht Mal an — einmal für 24 Stunden.

## Body

### Die Ausgangsfrage

Die Annahme, Hal Finney sei der zweite Teilnehmer im Bitcoin-Netzwerk nach Satoshi gewesen, galt jahrelang als gesichertes Wissen. Sie stützte sich auf: Hals frühe Antworten auf Satoshis E-Mails, seinen SourceForge-Eintrag als einziger Entwickler neben Satoshi, und seinen Tweet vom 11. Januar 2009 — „Running bitcoin". Keine dieser Quellen enthielt jedoch einen direkten Beweis. Alex Waltz wollte genau diesen Beweis finden.

### Chronologie der ersten Tage

Satoshi kündigte Bitcoin v0.1 am 8. Januar 2009 (19:27 UTC) auf der Cryptography Mailing List an. Noch am selben Abend schrieb er Hal Finney privat. Hal antwortete, er werde sich das am Wochenende anschauen.

Am 10. Januar 2009 (19:13 UTC) postete Hal auf SourceForge: Bitcoin v0.1 sei bei ihm abgestürzt. Er hängte seine `debug.log`-Datei an.

Diese Datei enthält die entscheidenden Beweise:

**Beweis 1: Block 49 als letzter bekannter Block.** Hals Node hatte beim Crash die Hashes der Blöcke 1–49 empfangen. Das bedeutet: Als Hal zum ersten Mal Bitcoin startete, existierten bereits mindestens 49 Blöcke. Der Network-Launch war somit schon vorbei.

**Beweis 2: Zwei andere Nodes im IRC-Channel.** Der frühe Bitcoin-Client nutzte den IRC-Channel `#bitcoin` auf Freenode zur Peer-Discovery. Hals `debug.log` zeigt, dass beim Verbinden bereits drei Teilnehmer im Channel waren:
- `uCeSAaG6R9Qidrs` — Hals eigene Node (IP 207.71.226.132, bekannt als finney.org)
- `x93428606` — eine Node hinter Tor (non-routable, daher zufälliger Username mit `x`-Präfix)
- `@u4rfwoe8g3w5Tai` — der Channel-Operator (clearnet-IP 68.164.57.219), zu dem Hals Node dann eine Verbindung aufbaut

Hals Node war also die dritte Node im Channel, nicht die zweite. Die Frage blieb: Wer betrieb die anderen beiden?

### Satoshis Clearnet-IP im Debug-Log

Die IP 68.164.57.219 (des Channel-Operators) ist öffentlich. Waltz verweist darauf, dass andere Forscher (Lopp, whoissatoshi) diese IP bereits als Satoshis IP identifiziert hatten. Der Channel-Operator zu diesem frühen Zeitpunkt war mit sehr hoher Wahrscheinlichkeit Satoshi selbst.

### Der Tor-Node: ebenfalls Satoshi?

Das ist die zentrale Frage der Untersuchung. Waltz argumentiert mit mehreren Belegen:

**Netzwerk-Halts und ExtraNonce.** Der frühe Bitcoin-Client implementierte den ExtraNonce so, dass er nur beim Neustart der Software auf 0 zurückgesetzt wurde. Dadurch hinterlässt jeder Mining-Betrieb eine Art Uptime-Fingerabdruck in der Blockchain. Waltz analysierte die ExtraNonce-Werte der ersten 183 Blöcke und fand, dass jeder signifikante Zeitabstand zwischen Blöcken mit einem ExtraNonce-Reset zusammenfiel — was auf denselben Miner hindeutet, der seinen Client neu startete.

Die Zeitabstände, die als Netzwerk-Halts gewertet werden können:
| Blocks | Dauer |
|--------|-------|
| 14 → 15 | 24h 12m 37s |
| 27 → 28 | 8h 34m 44s |
| 78 → 79 | 2h 45m 14s |
| 162 → 163 | 2h 54m 13s |
| 168 → 169 | 3h 42m 22s |

Bei der ursprünglichen Schwierigkeit von 1 wäre ein moderner PC von 2009 in der Lage gewesen, alle paar Stunden einen Block zu finden. Solche langen Pausen sind statistisch ohne Netzwerkstillstand nicht erklärbar.

**Satoshis E-Mail vom 12. Januar.** In einer E-Mail an Hal schrieb Satoshi (12. Januar 2009, 16:41 UTC): *„Unfortunately, I can't receive incoming connections from where I am."* Tor-Nodes können keine eingehenden Verbindungen akzeptieren — genau wie die `x93428606`-Node. Diese Formulierung ist konsistent damit, dass Satoshi zu diesem Zeitpunkt hinter Tor operierte.

**Dustins Parallelerfahrung.** Dustin Trammell lief in denselben Bug (fehlgeschlagene Broadcasts bei v0.1.0). Wer zu dieser Zeit sonst noch im Netzwerk war und denselben Bug hatte, hätte keine Blöcke zur Chain beitragen können — was die hohe Konzentration von Blöcken bei einem einzigen Miner erklärt.

### Hal Finneys tatsächliche Mining-Aktivität

Aus dem Forbes-Artikel von 2014 (Andy Greenberg, mit einem Screenshot von Hals Wallet) geht hervor, dass Hals erste erfolgreich abgebaute Block **Block 78** war (11. Januar 2009, 01:00 UTC). Die Wallet zeigt außerdem die 10-BTC-Transaktion von Satoshi (Block 170) und mehrere spätere selbst geminte Blöcke ab dem 10. Januar.

Hal twitterte um 03:33 UTC am 11. Januar — zu diesem Zeitpunkt lief bei ihm Bitcoin v0.1.1, das Satoshi ihm kurz zuvor geschickt hatte.

### Dustin Trammell: wahrscheinlich vor Hal im Netzwerk

Dustin Trammell (@druidian) ist ein bekannter früher Bitcoiner. Er lud die Software sofort nach der Ankündigung herunter — behauptete aber, nicht gewusst zu haben, dass Mining standardmäßig deaktiviert war. Deshalb begann er erst vier bis fünf Tage nach dem Launch zu minen.

Sein erster bestätigter Block: **Block 309** (13. Januar 2009, 09:38 UTC). Die kryptografische Eigentumsbeweise für die Adresse `1627A2DbCtVVykWVJmdQz2ERwkw4uiEL22` hat er 2021 öffentlich vorgelegt und in Bitcoin Core verifiziert.

Er berichtet außerdem von vier frühen Blöcken, die er am 11. Januar gemint hatte, die aber nie bestätigt wurden — eine direkte Folge des Bugs in Bitcoin v0.1.0 (fehlender Broadcast wegen blockiertem Kommunikations-Thread, behoben in v0.1.3). Satoshi bestätigte diesen Bug in seiner E-Mail an Dustin.

Dustins eigene Einschätzung: Als er den Client startete, war anfangs nur eine andere Node verbunden (die er für Satoshis Node hielt). Erst nach einigen Stunden kamen weitere Verbindungen. Das deckt sich mit dem Befund, dass die Tor-Node keine eingehenden Verbindungen annehmen konnte.

### Block 170: Die erste Bitcoin-Transaktion

Block 170 (12. Januar 2009, 03:30 UTC) enthält die erste Nicht-Coinbase-Transaktion der Bitcoin-Geschichte: Satoshi Nakamoto sendete Hal Finney 10 BTC. Zu diesem Zeitpunkt lief bei Hal Bitcoin v0.1.3 — die erste stabile Version.

### Das Mining-Default-Problem

Satoshi hatte Mining im Client standardmäßig ausgeschaltet. Er wollte vermutlich verhindern, dass Nutzer beim ersten Start eine hohe CPU-Auslastung sehen und die Software sofort wieder schließen. Diese Entscheidung hatte weitreichende Folgen: Viele frühe Interessenten wie Dustin Trammell liefen zwar die Software, trugen aber zunächst keine Blöcke zur Chain bei.

### Fazit der Untersuchung

Waltz kommt zu folgenden gesicherten Schlüssen:
- Hal Finney war nicht die zweite Node nach Satoshi — er kam erst bei Block 49 dazu.
- Die beiden anderen Nodes bei Hals Eintritt gehörten wahrscheinlich beide Satoshi.
- Das Netzwerk stand in den ersten 170 Blöcken achtmal still, davon einmal für 24 Stunden.
- Hals erster bestätigter geminter Block ist Block 78; Dustins erster ist Block 309.
- Dustin lief sehr wahrscheinlich vor Hal im Netzwerk, kann aber nicht mit derselben Sicherheit verifiziert werden.

Waltz betont, dass diese Befunde Hals Bedeutung für Bitcoin nicht schmälern. Ohne seine aktive Teilnahme — Bug-Reports, E-Mail-Austausch mit Satoshi, Node-Betrieb — wäre Bitcoin in den ersten Tagen möglicherweise still eingeschlafen.

## Related

- [[bitcoin-fruehgeschichte]]
- [[bitcoin-whitepaper]]
- [[satoshi-ankuendigung-2009]]
- [[bitcoin-mining-und-proof-of-work]]
- [[kryptoanarchismus-und-cypherpunks]]
- [[digitales-zeitstempel]]

## Open Questions

- Wer war hinter dem Tor-Node (x93428606)? Waltz vermutet Satoshi mit hoher Überzeugung, beweisen lässt es sich nicht.
- Hatte Dustin tatsächlich vier Blöcke am 11. Januar gemint, die nie bestätigt wurden? Die E-Mail-Korrespondenz mit Satoshi macht es plausibel, aber die Blöcke selbst sind nicht in der Chain.
- Gibt es weitere frühe Teilnehmer, die nie publik wurden? Mining war off by default, also wären sie keine sichtbaren Spuren hinterlassen haben.
- Warum verbanden sich weder Satoshis Clearnet-Node noch die Tor-Node mit Dustins Node? Waltz lässt diese Frage offen.
