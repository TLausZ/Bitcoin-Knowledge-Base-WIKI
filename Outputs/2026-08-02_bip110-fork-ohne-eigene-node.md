# BIP110-Fork: Was gilt für mich ohne eigene Node?

**Datum:** 2026-08-02
**Frage (weitergeleitet von Brit):** Bei der BIP110-Fork kann ich als Node-Betreiber wählen, welchem Protokoll ich folge. Was passiert ohne eigene Node? Laufen dann beide Protokolle für mich? Wie entscheide ich, welchem ich folge? Hat das Nachteile, und könnte ich einem Protokoll zugeordnet werden?

## Kurzantwort

Ohne eigene Node folgst du dem Protokoll, das die Node deines Wallet-Anbieters oder deiner Börse durchsetzt. Du erbst deren Wahl. Direkt wählen kannst du nur mit eigener Node; indirekt wählst du über die Wahl des Anbieters. Weil BIP110 eine Soft Fork ist, bleibt das praktische Risiko für Endnutzer klein. Guthaben geht in keinem Fork-Szenario verloren.

## Einordnung: Was BIP110 ist

BIP110 («Reduced Data Temporary Softfork», Dathon Ohm) will die Menge beliebiger Daten begrenzen, die sich in Bitcoin-Transaktionen einbetten lassen. Anlass ist das Ordinals-/Inscriptions-Phänomen. Technisch handelt es sich um eine Soft Fork: Die Regeln werden strenger, und Blöcke nach den neuen Regeln sind auch unter den alten gültig ([[bip-0110]], [[soft-fork-und-hard-fork]]).

Zur Aktivierungslage (Stand: Juli 2026): Die Spezifikation ist seit 25. Juni 2026 «Complete», im Netzwerk aber nicht aktiviert. Bitcoin Core integriert BIP110 nicht; Bitcoin Knots unterstützt es mit manueller Konfiguration. Die Miner-Signalisierung lag im Juli unter 2%, bei einer Schwelle von 55% und einem Mandatory-Signaling-Fenster Anfang August 2026 ([[bip-0110]]; die Zahlen stammen aus Sekundärquellen und sind noch ungeprüft).

## Die eigentliche Antwort

### 1. Ohne Node erbst du die Regeln deines Anbieters

Wer keine eigene Node betreibt, validiert selbst keine Regeln. Das Wallet (bei Software-Wallets meist über die Server des Anbieters) oder die Börse verbindet sich mit einer Node, und deren Software entscheidet, welche Blöcke als gültig gelten. Insofern trifft die Vermutung zu: Man wird faktisch einem Protokoll zugeordnet, nämlich dem des Anbieters. [[soft-fork-und-hard-fork]] hält als Kernkonzept fest, dass die wirtschaftliche Mehrheit (Börsen, Wallet-Anbieter, Nutzer) über ihre Softwarewahl bestimmt, welche Chain «Bitcoin» ist. An dieser Abstimmung nimmt ein Nutzer ohne Node nur vermittelt über seinen Anbieter teil. Dasselbe Argument steht in der Quelle zum 21-Millionen-Limit: Wer auf einer Börse hält, bekommt «whatever rules your custodian decides to follow» ([[bitcoin-geldpolitik-und-21-millionen-limit]]; RAW: 2026-08-02_bitcoinwell_why-21-million-doesnt-move.md).

### 2. Laufen beide Protokolle für mich? Nein.

Solange kein Chainsplit passiert, existiert ohnehin nur eine Chain. Käme es zu einem Split, hätte man Guthaben auf beiden Seiten, weil die eigenen Keys überall gültig bleiben. Sehen und nutzen würde man aber nur die Seite, auf der die Node des eigenen Anbieters steht.

### 3. Wie man ohne Node wählt

Es gibt zwei Hebel. Erstens die Anbieterwahl: Man kann nachfragen oder nachlesen, welche Software das Wallet-Backend oder die Börse fährt (heute praktisch überall Bitcoin Core, ohne BIP110), und bei Bedarf wechseln. Zweitens die eigene Node. Erst damit setzt man die Regeln selbst durch; das bleibt der einzige direkte Weg.

### 4. Nachteile und Risiken

Der Hauptnachteil liegt auf der Grundsatzebene: Ohne Node hat man im Regelwerk keine eigene Stimme. Bei BIP110 dämpft der Soft-Fork-Charakter die praktischen Folgen. BIP110-konforme Blöcke sind auf beiden Seiten gültig, ein dauerhafter Split mit zwei Coins (wie bei der Hard Fork Bitcoin Cash 2017) gilt darum als unwahrscheinliches Szenario; kurzzeitige Splits sind bei umkämpften Soft Forks möglich ([[soft-fork-und-hard-fork]]). Guthaben geht in keinem Fall verloren, weil die Keys auf jeder Chain gelten, die aus der bisherigen hervorgeht. Ein Sonderfall bleibt die Verwahrung auf der Börse: Bei einem Split entscheidet die Börse, welche Seite sie gutschreibt. Mit eigenen Keys behält man den Zugriff auf beide ([[selbstverwahrung-und-boersenrisiken]]).

## Zitierte Artikel und Quellen

- [[bip-0110]] — Inhalt, Status, Aktivierungslage, Spieltheorie, Kritik
- [[soft-fork-und-hard-fork]] — Soft/Hard Fork, MASF/UASF, wirtschaftliche Mehrheit, Chainsplit-Mechanik
- [[bitcoin-geldpolitik-und-21-millionen-limit]] — Nodes als Durchsetzungsmechanismus
- [[selbstverwahrung-und-boersenrisiken]] — Custodial-Risiken
- RAW: `2026-08-02_bitcoinwell_why-21-million-doesnt-move.md` — «If you hold your Bitcoin on an exchange, you don't get a vote on what Bitcoin is.»

## Offene Punkte

- Die Aktivierungszahlen im BIP110-Artikel (55%-Schwelle, unter 2% Signalisierung, Fenster Anfang August 2026) stammen aus Sekundärquellen; die Prüfung steht in den Open Questions von [[bip-0110]].
- Ob das Mandatory-Signaling-Fenster Anfang August 2026 greift, wäre in den nächsten Tagen ein Kandidat für ein Update des BIP110-Artikels.
