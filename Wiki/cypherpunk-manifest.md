# Cypherpunk's Manifesto

**Status:** established
**Themen:** privacy, philosophie, geschichte
**Last updated:** 2026-07-24
**Sources:** [[cypherpunk-manifesto.txt]], [[aprycot-gigi-freiheit-privatsphaere]]

## Summary

Eric Hughes' "A Cypherpunk's Manifesto" (1993) ist der Gründungstext der Cypherpunk-Bewegung. Er definiert Privatsphäre als gesellschaftliche Notwendigkeit im digitalen Zeitalter — nicht als Secrecy, sondern als die Fähigkeit, sich selektiv zu offenbaren. Kryptographie ist das zentrale Werkzeug. Die Kernthese: Privatsphäre muss aktiv gebaut werden, sie kann nicht durch Appelle an Institutionen erkämpft werden. "Cypherpunks write code."

## Body

### Privatsphäre ist nicht Geheimhaltung

Hughes eröffnet mit der Definition, die den ganzen Text trägt:

> Privacy is necessary for an open society in the electronic age. Privacy is not secrecy. A private matter is something one doesn't want the whole world to know, but a secret matter is something one doesn't want anybody to know. Privacy is the power to selectively reveal oneself to the world.

Privatsphäre ist also die Fähigkeit, selektiv zu entscheiden, wem man sich offenbart, nicht Unsichtbarkeit.

Im digitalen Raum ist diese Unterscheidung gefährdet. Elektronische Kommunikation aggregiert Informationen über Individuen auf eine Weise, die ohne Technologie nicht möglich wäre. Hughes begründet, warum Gesetze dagegen der falsche Hebel sind: Wer über eine gemeinsame Interaktion spricht, spricht über die eigene Erinnerung daran, und Redefreiheit steht ihm noch näher als Privatsphäre — «we seek not to restrict any speech at all».

### Privatsphäre erfordert anonyme Transaktionssysteme

Bargeld war das historische anonyme Transaktionssystem. Wer an einer Kassiererin eine Zeitschrift kauft, muss seinen Namen nicht nennen. Bei digitalen Transaktionen ist das anders, und Hughes benennt den Punkt, an dem Privatsphäre kippt:

> When my identity is revealed by the underlying mechanism of the transaction, I have no privacy. I cannot here selectively reveal myself; I must _always_ reveal myself.

Daraus folgt die Forderung, die 15 Jahre später Bitcoins Ausgangspunkt wird:

> Therefore, privacy in an open society requires anonymous transaction systems. Until now, cash has been the primary such system. An anonymous transaction system is not a secret transaction system. An anonymous system empowers individuals to reveal their identity when desired and only when desired; this is the essence of privacy.

### Kryptographie als Werkzeug

Privatsphäre erfordert Kryptographie. Ohne Verschlüsselung ist jede Kommunikation potenziell öffentlich. Hughes fasst beide Richtungen in einem Satzpaar: «To encrypt is to indicate the desire for privacy, and to encrypt with weak cryptography is to indicate not too much desire for privacy.» Umgekehrt braucht es die kryptographische Signatur, um Identität auf Wunsch zu beweisen, wenn das System standardmässig anonym ist.

Warum Institutionen als Garanten ausfallen, begründet er mit ihren Anreizen:

> We cannot expect governments, corporations, or other large, faceless organizations to grant us privacy out of their beneficence. It is to their advantage to speak of us, and we should expect that they will speak.

Der Rest des Absatzes ist die bekannteste Passage über Information selbst: Sie wolle nicht bloss frei sein, sie sehne sich danach; sie dehne sich aus, bis der verfügbare Speicher gefüllt sei. Hughes nennt sie die jüngere, stärkere Cousine des Gerüchts — schneller, mit mehr Augen, mit mehr Wissen und weniger Verständnis.

### "Cypherpunks write code"

Die politische Schlussfolgerung: Privatsphäre muss technisch implementiert werden. Appelle an Datenschutzgesetze greifen zu kurz. Wer Privatsphäre will, muss Software bauen, die sie strukturell unmöglich macht zu verletzen. Das ist der meistzitierte Absatz des Textes:

> Cypherpunks write code. We know that someone has to write software to defend privacy, and since we can't get privacy unless we all do, we're going to write it. We publish our code so that our fellow Cypherpunks may practice and play with it. Our code is free for all to use, worldwide. We don't much care if you don't approve of the software we write. We know that software can't be destroyed and that a widely dispersed system can't be shut down.

Zur Regulierung von Kryptographie zieht Hughes eine territoriale Grenze: Verschlüsselung sei ein privater Akt, der Information dem öffentlichen Raum entzieht, und «even laws against cryptography reach only so far as a nation's border and the arm of its violence».

Der Schluss steht allerdings unter einer Bedingung, die in der Rezeption oft untergeht. Hughes will Privatsphäre als Gesellschaftsvertrag, nicht als Rückzug Einzelner: Sie reiche nur so weit wie die Kooperation der Mitmenschen, deshalb suche man ausdrücklich Fragen und Einwände. Vom eigenen Kurs abbringen lasse man sich davon nicht. Der Text endet mit einem einzelnen Wort, «Onward», und dem Datum 9. März 1993.

### Relevanz für Bitcoin

Satoshi Nakamotos Bitcoin (2009) ist ein direktes Produkt des Cypherpunk-Denkens. Ein elektronisches Peer-to-Peer-Bargeld ohne Mittelsmänner: kein Vertrauen in Institutionen, nur kryptographische Beweise. Der Querverweis ist explizit: Satoshi veröffentlichte das Whitepaper auf der Cypherpunks-Mailingliste.

Bitcoin löst das konkrete Problem, das Hughes beschreibt: digitale Wertübertragung ohne Identitätsoffenbarung durch den Transaktionsmechanismus selbst.

### Von HTTP zu HTTPS: Bitcoin als nächster Schritt

Gigi zieht in einem Essay (Blockzeit 741471) eine strukturelle Analogie zwischen der Entwicklung des Internets und Bitcoin. Das World Wide Web begann 1989 mit HTTP — Klartext, alles offen, für jeden sichtbar. Erst 1994 (SSL durch Netscape) und formal 1999 (RFC 2818 / HTTPS) wurde Verschlüsselung zum Standard. Der Wandel geschah nicht durch politischen Druck, sondern weil ein Protokoll ein besseres ablöste.

Die Konsequenz fehlender Verschlüsselung — PRISM, ECHELON, massenhafte Überwachung — wurde durch Edward Snowdens Enthüllungen sichtbar. HTTPS ist heute so selbstverständlich wie fliessendes Wasser. Der Weg dorthin war langsam und schmerzhaft.

Gigis These: Das Gleiche passiert jetzt bei Finanzdaten. Finanztransaktionen im Klartext — analysierbar von jedem, gebündelt in Datenbanken, abrufbar von Regierungen — entsprechen dem HTTP-Zeitalter. Bitcoin mit den Datenschutzeigenschaften von Lightning wäre das Äquivalent zu HTTPS: kein Vertrauen in Infrastruktur nötig, kein Angriffspunkt für Massenüberwachung. [[aprycot-gigi-freiheit-privatsphaere]]

Gigi verankert das im Recht: Artikel 12 der Allgemeinen Erklärung der Menschenrechte schützt das Privatleben explizit. In der digitalen Welt folgt daraus, dass Verschlüsselung ein Menschenrechtsgebot ist — Grant Gilliam formuliert es so.

Die Länder, in denen dieser Schutz fehlt, sind kein theoretisches Szenario: Kuba, China, Afghanistan, Palästina, Hongkong, Kanada — Journalisten, Dissidenten und Aktivisten wurden in den Monaten vor Gigis Artikel entfernt oder inhaftiert, weil ihr Verhalten überwacht und analysiert werden konnte. Richelieu: „Gebt mir sechs Zeilen, die der aufrichtigste Mensch geschrieben hat, und ich werde etwas finden, um ihn zu hängen." [[aprycot-gigi-freiheit-privatsphaere]]

## Anhang: Volltext des Manifests

Eric Hughes, «A Cypherpunk's Manifesto», 9. März 1993, veröffentlicht auf der Cypherpunks-Mailingliste. Wortlaut aus [[cypherpunk-manifesto.txt]] (Original: activism.net, Spiegel: Nakamoto Institute). Zeilenumbrüche der Plaintext-Fassung sind zu Absätzen zusammengeführt, der Text selbst ist unverändert.

> Privacy is necessary for an open society in the electronic age. Privacy is not secrecy. A private matter is something one doesn't want the whole world to know, but a secret matter is something one doesn't want anybody to know. Privacy is the power to selectively reveal oneself to the world.
>
> If two parties have some sort of dealings, then each has a memory of their interaction. Each party can speak about their own memory of this; how could anyone prevent it? One could pass laws against it, but the freedom of speech, even more than privacy, is fundamental to an open society; we seek not to restrict any speech at all. If many parties speak together in the same forum, each can speak to all the others and aggregate together knowledge about individuals and other parties. The power of electronic communications has enabled such group speech, and it will not go away merely because we might want it to.
>
> Since we desire privacy, we must ensure that each party to a transaction have knowledge only of that which is directly necessary for that transaction. Since any information can be spoken of, we must ensure that we reveal as little as possible. In most cases personal identity is not salient. When I purchase a magazine at a store and hand cash to the clerk, there is no need to know who I am. When I ask my electronic mail provider to send and receive messages, my provider need not know to whom I am speaking or what I am saying or what others are saying to me; my provider only need know how to get the message there and how much I owe them in fees. When my identity is revealed by the underlying mechanism of the transaction, I have no privacy. I cannot here selectively reveal myself; I must _always_ reveal myself.
>
> Therefore, privacy in an open society requires anonymous transaction systems. Until now, cash has been the primary such system. An anonymous transaction system is not a secret transaction system. An anonymous system empowers individuals to reveal their identity when desired and only when desired; this is the essence of privacy.
>
> Privacy in an open society also requires cryptography. If I say something, I want it heard only by those for whom I intend it. If the content of my speech is available to the world, I have no privacy. To encrypt is to indicate the desire for privacy, and to encrypt with weak cryptography is to indicate not too much desire for privacy. Furthermore, to reveal one's identity with assurance when the default is anonymity requires the cryptographic signature.
>
> We cannot expect governments, corporations, or other large, faceless organizations to grant us privacy out of their beneficence. It is to their advantage to speak of us, and we should expect that they will speak. To try to prevent their speech is to fight against the realities of information. Information does not just want to be free, it longs to be free. Information expands to fill the available storage space. Information is Rumor's younger, stronger cousin; Information is fleeter of foot, has more eyes, knows more, and understands less than Rumor.
>
> We must defend our own privacy if we expect to have any. We must come together and create systems which allow anonymous transactions to take place. People have been defending their own privacy for centuries with whispers, darkness, envelopes, closed doors, secret handshakes, and couriers. The technologies of the past did not allow for strong privacy, but electronic technologies do.
>
> We the Cypherpunks are dedicated to building anonymous systems. We are defending our privacy with cryptography, with anonymous mail forwarding systems, with digital signatures, and with electronic money.
>
> Cypherpunks write code. We know that someone has to write software to defend privacy, and since we can't get privacy unless we all do, we're going to write it. We publish our code so that our fellow Cypherpunks may practice and play with it. Our code is free for all to use, worldwide. We don't much care if you don't approve of the software we write. We know that software can't be destroyed and that a widely dispersed system can't be shut down.
>
> Cypherpunks deplore regulations on cryptography, for encryption is fundamentally a private act. The act of encryption, in fact, removes information from the public realm. Even laws against cryptography reach only so far as a nation's border and the arm of its violence. Cryptography will ineluctably spread over the whole globe, and with it the anonymous transactions systems that it makes possible.
>
> For privacy to be widespread it must be part of a social contract. People must come and together deploy these systems for the common good. Privacy only extends so far as the cooperation of one's fellows in society. We the Cypherpunks seek your questions and your concerns and hope we may engage you so that we do not deceive ourselves. We will not, however, be moved out of our course because some may disagree with our goals.
>
> The Cypherpunks are actively engaged in making the networks safer for privacy. Let us proceed together apace.
>
> Onward.
>
> Eric Hughes <hughes@soda.berkeley.edu>
>
> 9 March 1993

## Related

- [[kryptoanarchismus-und-cypherpunks]]
- [[hacker-ethik]]
- [[pgp-und-verschluesselungspolitik]]
- [[digitales-bargeld-und-ecash]]
- [[opsec-und-privatsphaere]]
- [[bitcoin-whitepaper]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[silent-payments]]
- [[biometrie-und-finanzueberwachung]]
- [[bitcoin-als-information]]
- [[bitcoin-humanitaere-anwendungen]]
- [[cbdc-und-digitaler-yuan]]

## Open Questions

- Wie verhalten sich Post-Quantum-Kryptographie und der Cypherpunk-Ansatz?
- Wo liegt die Grenze zwischen Privatsphäre als Grundrecht und legitimen gesellschaftlichen Transparenzanforderungen?
