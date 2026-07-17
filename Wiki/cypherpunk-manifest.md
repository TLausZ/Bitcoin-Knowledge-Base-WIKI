# Cypherpunk's Manifesto

**Status:** established
**Themen:** privacy, philosophie, geschichte
**Last updated:** 2026-06-22
**Sources:** [[cypherpunk-manifesto.txt]], [[aprycot-gigi-freiheit-privatsphaere]]

## Summary

Eric Hughes' "A Cypherpunk's Manifesto" (1993) ist der Gründungstext der Cypherpunk-Bewegung. Er definiert Privatsphäre als gesellschaftliche Notwendigkeit im digitalen Zeitalter — nicht als Secrecy, sondern als die Fähigkeit, sich selektiv zu offenbaren. Kryptographie ist das zentrale Werkzeug. Die Kernthese: Privatsphäre muss aktiv gebaut werden, sie kann nicht durch Appelle an Institutionen erkämpft werden. "Cypherpunks write code."

## Body

### Privatsphäre ist nicht Geheimhaltung

Hughes unterscheidet klar: Privatsphäre ist, was man nicht der ganzen Welt mitteilen will. Geheimhaltung ist, was man niemandem mitteilen will. Privatsphäre ist die Fähigkeit, selektiv zu entscheiden, wem man sich offenbart — nicht Unsichtbarkeit.

Im digitalen Raum ist diese Unterscheidung gefährdet. Elektronische Kommunikation aggregiert Informationen über Individuen auf eine Weise, die ohne Technologie nicht möglich wäre.

### Privatsphäre erfordert anonyme Transaktionssysteme

Bargeld war das historische anonyme Transaktionssystem. Wer an einer Kassiererin eine Zeitschrift kauft, muss seinen Namen nicht nennen. Bei digitalen Transaktionen ist das anders: Der Mechanismus enthüllt oft automatisch Identität.

Das Gegenmodell: Systeme, bei denen Identität nur dann enthüllt wird, wenn der Nutzer es will. Das ist der Kern digitaler Privatsphäre — nicht Anonymität per se, sondern Kontrolle über die eigene Enthüllung.

### Kryptographie als Werkzeug

Privatsphäre erfordert Kryptographie. Ohne Verschlüsselung ist jede Kommunikation potenziell öffentlich. Die kryptografische Signatur ermöglicht es umgekehrt, Identität auf Wunsch zu beweisen, wenn das System standardmässig anonym ist.

Hughes' Konsequenz: Privatsphäre kann nicht durch gesetzliche Regulierung gesichert werden — Regierungen, Unternehmen und andere Institutionen haben strukturelle Interessen an der Enthüllung von Informationen. Vertrauen auf Institutionen reicht nicht aus.

### "Cypherpunks write code"

Die politische Schlussfolgerung: Privatsphäre muss technisch implementiert werden. Appelle an Datenschutzgesetze greifen zu kurz. Wer Privatsphäre will, muss Software bauen, die sie strukturell unmöglich macht zu verletzen: kein Vertrauen nötig, weil kein Vertrauen möglich ist.

"We don't much care if you don't approve of the software we write." — Hughes' Aussage ist radikal: Privatsphäre durch Technologie ist kein Angriff auf die Gesellschaft, sondern ihre Voraussetzung.

### Relevanz für Bitcoin

Satoshi Nakamotos Bitcoin (2009) ist ein direktes Produkt des Cypherpunk-Denkens. Ein elektronisches Peer-to-Peer-Bargeld ohne Mittelsmänner: kein Vertrauen in Institutionen, nur kryptographische Beweise. Der Querverweis ist explizit: Satoshi veröffentlichte das Whitepaper auf der Cypherpunks-Mailingliste.

Bitcoin löst das konkrete Problem, das Hughes beschreibt: digitale Wertübertragung ohne Identitätsoffenbarung durch den Transaktionsmechanismus selbst.

### Von HTTP zu HTTPS: Bitcoin als nächster Schritt

Gigi zieht in einem Essay (Blockzeit 741471) eine strukturelle Analogie zwischen der Entwicklung des Internets und Bitcoin. Das World Wide Web begann 1989 mit HTTP — Klartext, alles offen, für jeden sichtbar. Erst 1994 (SSL durch Netscape) und formal 1999 (RFC 2818 / HTTPS) wurde Verschlüsselung zum Standard. Der Wandel geschah nicht durch politischen Druck, sondern weil ein Protokoll ein besseres ablöste.

Die Konsequenz fehlender Verschlüsselung — PRISM, ECHELON, massenhafte Überwachung — wurde durch Edward Snowdens Enthüllungen sichtbar. HTTPS ist heute so selbstverständlich wie fliessendes Wasser. Der Weg dorthin war langsam und schmerzhaft.

Gigis These: Das Gleiche passiert jetzt bei Finanzdaten. Finanztransaktionen im Klartext — analysierbar von jedem, gebündelt in Datenbanken, abrufbar von Regierungen — entsprechen dem HTTP-Zeitalter. Bitcoin mit den Datenschutzeigenschaften von Lightning wäre das Äquivalent zu HTTPS: kein Vertrauen in Infrastruktur nötig, kein Angriffspunkt für Massenüberwachung. [[aprycot-gigi-freiheit-privatsphaere]]

Gigi verankert das im Recht: Artikel 12 der Allgemeinen Erklärung der Menschenrechte schützt das Privatleben explizit. In der digitalen Welt folgt daraus, dass Verschlüsselung ein Menschenrechtsgebot ist — Grant Gilliam formuliert es so.

Die Länder, in denen dieser Schutz fehlt, sind kein theoretisches Szenario: Kuba, China, Afghanistan, Palästina, Hongkong, Kanada — Journalisten, Dissidenten und Aktivisten wurden in den Monaten vor Gigis Artikel entfernt oder inhaftiert, weil ihr Verhalten überwacht und analysiert werden konnte. Richelieu: „Gebt mir sechs Zeilen, die der aufrichtigste Mensch geschrieben hat, und ich werde etwas finden, um ihn zu hängen." [[aprycot-gigi-freiheit-privatsphaere]]

## Related

- [[kryptoanarchismus-und-cypherpunks]]
- [[hacker-ethik]]
- [[pgp-und-verschluesselungspolitik]]
- [[digitales-bargeld-und-ecash]]
- [[opsec-und-privatsphaere]]
- [[bitcoin-whitepaper]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[silent-payments]]

## Open Questions

- Wie verhalten sich Post-Quantum-Kryptographie und der Cypherpunk-Ansatz?
- Wo liegt die Grenze zwischen Privatsphäre als Grundrecht und legitimen gesellschaftlichen Transparenzanforderungen?
