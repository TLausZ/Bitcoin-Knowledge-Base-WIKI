# Satoshi Zitate

**Status:** established
**Themen:** privacy, mining, oekonomie, geschichte, satoshi, zitate
**Last updated:** 2026-07-11
**Sources:** [[the-quotable-satoshi]]

## Summary

Satoshi Nakamotos öffentliche Schriften passen in ein schmales Zeitfenster: das Whitepaper vom 31. Oktober 2008, gut zwei Monate Diskussion auf der Cryptography Mailing List, einige Posts auf der P2P Foundation und die BitcoinTalk-Beiträge von November 2009 bis Dezember 2010. Danach zog er sich zurück. Das Satoshi Nakamoto Institute hat aus diesem Material die aussagekräftigsten Passagen in seiner Sammlung *The Quotable Satoshi* nach Themen geordnet. Dieser Artikel synthetisiert sie und ordnet sie ein: das Vertrauensproblem als Ausgangspunkt, Proof-of-Work als Antwort auf Double-Spending und das Byzantine Generals' Problem, Nakamotos Denken über Knappheit und Deflation, seine Erwartungen an Nodes, Gebühren, Privatsphäre und Mining, und die wenigen Sätze, die etwas über Motiv und Person verraten. Alle Zitate stehen verbatim in [[the-quotable-satoshi]] mit direktem Link zu jeder Fundstelle.

## Body

### Die vier Quellen

Nakamotos Aussagen stammen aus vier Kontexten, und der Ton verschiebt sich mit jedem. Das Whitepaper ist knapp und formell. Auf der Cryptography Mailing List (Oktober 2008 bis Januar 2009) verteidigt er das Design gegen erfahrene Kryptografen und geht auf technische Einwände ein. Auf der P2P Foundation (ab Februar 2009) erklärt er Bitcoin einem breiteren Publikum und formuliert die politische Motivation offener. Auf BitcoinTalk (November 2009 bis Dezember 2010) beantwortet er Nutzerfragen, diskutiert Ökonomie und trifft Produktentscheidungen bis hin zum Logo.

Der Genesis Block trägt eine Zeitungsschlagzeile in der Coinbase: *«The Times 03/Jan/2009 Chancellor on brink of second bailout for banks»*. Sie datiert den Block und benennt zugleich das Problem, gegen das Bitcoin antritt. Ausführlich in [[bitcoin-whitepaper]] und [[bitcoin-fruehgeschichte]].

### Das Vertrauensproblem

Nakamoto rahmte Bitcoin nicht als Zahlungstechnik, sondern als Antwort auf ein Vertrauensproblem. Auf der P2P Foundation steht der Satz, den er am schärfsten formulierte:

> The root problem with conventional currency is all the trust that's required to make it work. The central bank must be trusted not to debase the currency, but the history of fiat currencies is full of breaches of that trust.

([P2P Foundation, 11.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/1/))

Banken behandelte er nicht als teuer, sondern als strukturell riskant:

> Banks must be trusted to hold our money and transfer it electronically, but they lend it out in waves of credit bubbles with barely a fraction in reserve. We have to trust them with our privacy, trust them not to let identity thieves drain our accounts. Their massive overhead costs make micropayments impossible.

([P2P Foundation, 11.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/1/))

Die Analogie, die zeigt, worauf er hinauswollte, ist die starke Verschlüsselung. Vor ihr mussten Nutzer dem Systemadministrator vertrauen; danach galt Sicherheit per Physik statt per Versprechen:

> Then strong encryption became available to the masses, and trust was no longer required. Data could be secured in a way that was physically impossible for others to access, no matter for what reason, no matter how good the excuse, no matter what.

([P2P Foundation, 11.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/1/))

Siehe [[bitcoin-monetaere-deckung-und-sicherheit]] und [[satoshi-ankuendigung-2009]].

### Trusted Third Parties und Rückbuchbarkeit

Das Whitepaper beginnt mit dem Kostenproblem der Vermittler. Nakamotos Punkt ist, dass Rückbuchbarkeit kein Feature, sondern eine strukturelle Last ist:

> Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes. The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions [...] With the possibility of reversal, the need for trust spreads.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Die Alternative fasst er in einem Satz, der später oft zitiert wurde:

> What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Bemerkenswert früh betonte er Open Source als Teil der vertrauensfreien Architektur: «Being open source means anyone can independently review the code. If it was closed source, nobody could verify the security.» ([BitcoinTalk, 10.12.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/17/))

### Double-Spending: das eigentliche Problem

Das technische Kernproblem war, Double-Spending ohne zentrale Instanz zu verhindern. Die übliche Lösung, eine vertrauenswürdige Prägeanstalt, führt zurück zur Bank:

> The problem with this solution is that the fate of the entire money system depends on the company running the mint, with every transaction having to go through them, just like a bank.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Bitcoins Ansatz nutzt stattdessen ein Netzwerk, das die erste Ausgabe einer Münze bezeugt:

> Bitcoin's solution is to use a peer-to-peer network to check for double-spending. In a nutshell, the network works like a distributed timestamp server, stamping the first transaction to spend a coin. It takes advantage of the nature of information being easy to spread but hard to stifle.

([P2P Foundation, 11.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/1/))

Gegen die Sorge, das Netzwerk müsse aktiv nach Betrügern fahnden, stellte er klar, dass es nur entscheidet, welche Ausgabe gilt:

> We're not "on the lookout" for double spends to sound the alarm and catch the cheater. We merely adjudicate which one of the spends is valid. [...] within a few blocks, one of the spends becomes valid and the others become invalid.

([Cryptography Mailing List, 17.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/13/))

Vertiefung in [[bitcoin-mining-und-proof-of-work]] und [[bitcoin-whitepaper]].

### Proof-of-Work und das Byzantine Generals' Problem

Proof-of-Work ist bei Nakamoto zugleich ein Abstimmungsmechanismus, der das Sybil-Problem umgeht:

> The proof-of-work also solves the problem of determining representation in majority decision making. If the majority were based on one-IP-address-one-vote, it could be subverted by anyone able to allocate many IPs. Proof-of-work is essentially one-CPU-one-vote.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Auf einen Einwand hin erklärte er die Kette als Lösung des Byzantine Generals' Problem. Das Bild: Generäle, die einen Angriffszeitpunkt abstimmen müssen, ohne einander vertrauen zu können, einigen sich, indem jeder Rechenarbeit in einen Hash steckt, der die Zeit enthält.

> After two hours, one attack time should be hashed by a chain of 12 proofs-of-work. Every general, just by verifying the difficulty of the proof-of-work chain, can estimate how much parallel CPU power per hour was expended on it [...] The proof-of-work chain is how all the synchronisation, distributed database and global view problems you've asked about are solved.

([Cryptography Mailing List, 13.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/11/))

Den Kern brachte er andernorts auf einen Satz: «The proof-of-work chain is the solution to the synchronisation problem, and to knowing what the globally shared view is without having to trust anyone.» ([09.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/8/)) Und knapper noch: «The credential that establishes someone as real is the ability to supply CPU power.» ([17.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/14/))

Eine Eigenschaft, die für leichte Clients zählt, hob er 2010 hervor:

> Proof-of-work has the nice property that it can be relayed through untrusted middlemen. We don't have to worry about a chain of custody of communication. It doesn't matter who tells you a longest chain, the proof-of-work speaks for itself.

([BitcoinTalk, 07.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/327/))

### Konsens: die längste Kette

Warum immer die längste Kette gilt, begründete Nakamoto mit dem Problem, dass frühere Zeugen spätere Teilnehmer nicht überzeugen können:

> We can't have subfactions of nodes that cling to one branch that they think was first [...] The CPU power proof-of-work vote must have the final say. The only way for everyone to stay on the same page is to believe that the longest chain is always the valid one, no matter what.

([Cryptography Mailing List, 09.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/6/))

Das gilt für ihn ohne Ausnahme, auch bei tiefen Reorganisationen: «There is no way for the software to automatically know if one chain is better than another except by the greatest proof-of-work. In the design it was necessary for it to switch to a longer chain no matter how far back it has to go.» ([16.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/394/))

Genau genommen zählt nicht die Länge, sondern die kumulierte Arbeit. Vertiefung in [[bitcoin-mining-und-proof-of-work]] und im KB-Artikel zu Chainwork.

### Der Incentive-Mechanismus

Der Block-Reward löst für Nakamoto zwei Aufgaben zugleich: initiale Verteilung und Anreiz zur Ehrlichkeit. Den Vergleich zum Goldschürfen zog er schon im Whitepaper:

> The steady addition of a constant of amount of new coins is analogous to gold miners expending resources to add gold to circulation. In our case, it is CPU time and electricity that is expended.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Warum ein Angreifer mit Übermacht meist trotzdem ehrlich mint, formulierte er als Kosten-Nutzen-Rechnung:

> He ought to find it more profitable to play by the rules, such rules that favour him with more new coins than everyone else combined, than to undermine the system and the validity of his own wealth.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Den Übergang von der Subvention zu den Gebühren plante er von Anfang an ein: «Once a predetermined number of coins have entered circulation, the incentive can transition entirely to transaction fees and be completely inflation free.» ([Whitepaper](https://nakamotoinstitute.org/library/bitcoin/))

### Knappheit, Deflation und das 21-Millionen-Limit

Beim v0.1-Release nannte Nakamoto die konkreten Zahlen: 21 Millionen, Halbierung alle vier Jahre, danach Gebühren. Den Deflationseffekt stellte er ausdrücklich gegen das Gelddrucken:

> Since the effective circulation is reduced, all the remaining coins are worth slightly more. It's the opposite of when a government prints money and the value of existing money goes down.

([BitcoinTalk, 10.12.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/17/))

Verlorene Coins waren für ihn kein Verlust für das System: «Lost coins only make everyone else's coins worth slightly more. Think of it as a donation to everyone.» ([21.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/131/))

Das Angebotsmodell verglich er mit einem Edelmetall, bei dem die Menge feststeht und der Wert sich bewegt:

> Instead of the supply changing to keep the value the same, the supply is predetermined and the value changes. As the number of users grows, the value per coin increases. It has the potential for a positive feedback loop.

([P2P Foundation, 18.02.2009](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/3/))

Auf die Frage nach der fehlenden Zentralbank antwortete er, Software könne den realen Wert der Dinge nicht kennen, und genau deshalb sei das Angebot vorgegeben statt gesteuert. Weiter in [[bitcoin-geldpolitik-und-21-millionen-limit]] und [[bitcoin-digitale-knappheit]].

### Das Metall-Gedankenexperiment

Nakamotos meistzitierte Passage zur Werttheorie ist ein Gedankenexperiment. Es war seine Antwort auf den Einwand, Bitcoin verletze Mises' Regressionstheorem, das Geld einen ursprünglichen Gebrauchswert abverlangt.

> As a thought experiment, imagine there was a base metal as scarce as gold but with the following properties: boring grey in colour, not a good conductor of electricity, not particularly strong [...] not useful for any practical or ornamental purpose ... and one special, magical property: can be transported over a communications channel. If it somehow acquired any value at all for whatever reason, then anyone wanting to transfer wealth over a long distance could buy some, transmit it, and have the recipient sell it.

([BitcoinTalk, 27.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/428/))

Er zweifelte selbst an der reinen Lehre, dass Geld intrinsischen Wert braucht: «But if there were nothing in the world with intrinsic value that could be used as money, only scarce but no intrinsic value, I think people would still take up something.» Zur Assetklasse war er im selben Monat knapp: «More like a collectible or commodity.» ([27.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/427/)) Anschluss in [[bitcoin-absolute-knappheit]] und [[ideal-money-und-bitcoin]].

### Bootstrapping und die selbsterfüllende Prophezeiung

Wie ein Geld ohne Anfangswert startet, beschäftigte Nakamoto. Seine bekannteste Antwort ist zugleich die früheste dokumentierte Kaufempfehlung:

> It might make sense just to get some in case it catches on. If enough people think the same way, that becomes a self fulfilling prophecy.

([Cryptography Mailing List, 17.01.2009](https://satoshi.nakamotoinstitute.org/emails/cryptography/17/))

Er sah die Adoption an einer Schwelle: «I'm sure that in 20 years there will either be very large transaction volume or no volume.» ([14.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/57/)) Zur Preisbildung dachte er in Erwartungswerten: «A rational market price for something that is expected to increase in value will already reflect the present value of the expected future increases.» ([21.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/65/))

### Nodes, Server-Farmen und SPV

Nakamoto rechnete nicht damit, dass jeder Nutzer einen Full Node betreibt. Schon in der zweiten Mailing-List-Antwort skizzierte er eine Konsolidierung:

> At first, most users would run network nodes, but as the network grows beyond a certain point, it would be left more and more to specialists with server farms of specialized hardware.

([Cryptography Mailing List, 02.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/2/))

2010 nannte er eine Obergrenze und trennte Nodes von Nutzern:

> I anticipate there will never be more than 100K nodes, probably less. It will reach an equilibrium where it's not worth it for more nodes to join in. The rest will be lightweight clients, which could be millions.

([BitcoinTalk, 14.07.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/188/))

> The current system where every user is a network node is not the intended configuration for large scale. That would be like every Usenet user runs their own NNTP server.

([BitcoinTalk, 29.07.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/287/))

Für die Masse plante er Simplified Payment Verification. Wichtig war ihm, dass ein leichter Client Zahlungen selbst prüfen kann, statt einem Node zu vertrauen: «It does not need to trust a node to verify payments, it can still verify them itself.» ([14.07.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/188/)) Diese Sicht steht in Spannung zum heutigen Dezentralisierungs-Ideal, siehe [[bitcoin-netzwerk-und-nodes]].

### Skalierung

Zur Datenlast war Nakamoto optimistisch und verwies auf fallende Kosten:

> Whatever size micropayments you need will eventually be practical. I think in 5 or 10 years, the bandwidth and storage will seem trivial.

([BitcoinTalk, 05.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/318/))

Zugleich sah er Bitcoin nicht für beliebig kleine Micropayments: «it doesn't claim to be practical for arbitrarily small micropayments.» ([04.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/317/)) Die Gebührenschwelle wollte er als «circuit breaker» niedrig halten und bei Bedarf anheben. Berührt [[bitcoin-skalierung-und-zahlungen]].

### Gebühren

Nakamoto plante die Gebühren als langfristigen Ersatz für die schrumpfende Subvention:

> In a few decades when the reward gets too small, the transaction fee will become the main compensation for nodes.

([BitcoinTalk, 14.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/57/))

Freitransaktionen wollte er nie ganz abschaffen: «I don't think the threshold should ever be 0. We should always allow at least some free transactions.» ([07.09.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/439/)) Ob Gebühren allein die Netzwerksicherheit tragen können, ist bis heute offen, siehe die Diskussion in [[bitcoin-mining-und-proof-of-work]].

### Mining und Energie

Den Energieeinwand beantwortete Nakamoto zweimal ausführlich. Einmal mit dem Gold-Vergleich:

> Gold mining is a waste, but that waste is far less than the utility of having gold available as a medium of exchange. [...] The utility of the exchanges made possible by Bitcoin will far exceed the cost of electricity used. Therefore, not having Bitcoin would be the net waste.

([BitcoinTalk, 07.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/327/))

Einmal mit dem Heiz-Argument, das die spätere Standortdiskussion vorwegnimmt:

> Bitcoin generation should end up where it's cheapest. Maybe that will be in cold climates where there's electric heat, where it would be essentially free.

([BitcoinTalk, 09.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/337/))

Zur Difficulty-Mechanik hielt er fest, dass schnellere Maschinen den Gesamtausstoß nicht erhöhen: «The average total coins generated across the network per day stays the same. Faster machines just get a larger share.» ([12.12.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/20/)) Vertiefung in [[bitcoin-mining-narrativ-und-kritik]] und [[bitcoin-mining-energiequellen]].

### GPU-Wettrüsten

Bemerkenswert früh warnte Nakamoto vor der Aufrüstung der Mining-Hardware und appellierte an die Gemeinschaft:

> We should have a gentleman's agreement to postpone the GPU arms race as long as we can for the good of the network. It's much easer to get new users up to speed if they don't have to worry about GPU drivers and compatibility. It's nice how anyone with just a CPU can compete fairly equally right now.

([BitcoinTalk, 12.12.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/20/))

Der Appell hielt nicht lange; GPUs, dann FPGAs, dann ASICs verdrängten CPU-Mining bis 2013. Verlauf in [[bitcoin-mining-und-proof-of-work]].

### Privatsphäre und Verschlüsselung

Nakamotos Privatsphäre-Modell ist pseudonym, nicht anonym: alle Transaktionen öffentlich, aber die Schlüssel ohne Namensbezug.

> The public can see that someone is sending an amount to someone else, but without information linking the transaction to anyone. This is similar to the level of information released by stock exchanges, where the time and size of individual trades, the "tape", is made public, but without telling who the parties were.

([Whitepaper, 31.10.2008](https://nakamotoinstitute.org/library/bitcoin/))

Die praktische Empfehlung war Adress-Hygiene: «For greater privacy, it's best to use bitcoin addresses only once.» ([25.11.2009](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/11/)) Für stärkere Absicherung riet er zu Tor: «If you're serious about privacy, TOR is an advisable precaution.» ([06.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/45/)) Zu Zero-Knowledge-Proofs blieb er skeptisch: «It's hard to think of how to apply zero-knowledge-proofs in this case.» Zur Verschlüsselung selbst war er zuversichtlich: «SHA-256 is very strong. [...] It can last several decades unless there's some massive breakthrough attack.» ([14.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/119/)) Anschluss in [[coinjoin-und-on-chain-privatsphaere]].

### Transaktionstypen und Script

Dass Bitcoin mehr als einfache Zahlungen erlaubt, war für Nakamoto von Anfang an eingeplant. Da die Kernarchitektur mit v0.1 feststand, musste sie alle Fälle vorsehen:

> The design supports a tremendous variety of possible transaction types that I designed years ago. Escrow transactions, bonded contracts, third party arbitration, multi-party signature, etc. [...] but they all had to be designed at the beginning to make sure they would be possible later.

([BitcoinTalk, 17.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/126/))

Die Lösung, um nicht jeden Fall einzeln zu verdrahten, war Script: «The solution was script, which generalizes the problem so transacting parties can describe their transaction as a predicate that the node network evaluates.» ([17.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/126/))

### Finalität und Bestätigungen

Bitcoin-Finalität ist probabilistisch, und Nakamoto sagte das offen. Empfänger sollen warten, bevor sie liefern:

> The receiver of a payment must wait an hour or so before believing that it's valid. The network will resolve any possible double-spend races by then.

([Cryptography Mailing List, 11.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/10/))

Im Vergleich zu bestehenden Systemen sah er das als schnell an: «Paper cheques can bounce up to a week or two later. Credit card transactions can be contested up to 60 to 180 days later. Bitcoin transactions can be sufficiently irreversible in an hour or two.» ([11.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/10/)) Zu unbestätigten Zahlungen war er unmissverständlich: «0/unconfirmed transactions are very much second class citizens.» ([30.09.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/464/))

### Motive: Freiheit und Politik

Nakamoto äußerte sich sparsam zu Motiven, aber deutlich. Auf der Mailing List:

> Yes, but we can win a major battle in the arms race and gain a new territory of freedom for several years.

([Cryptography Mailing List, 07.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/4/))

> It's very attractive to the libertarian viewpoint if we can explain it properly. I'm better with code than with words though.

([Cryptography Mailing List, 13.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/12/))

Zur Zensurresistenz verwies er auf dezentrale Netzwerke, die staatlichem Druck standhalten: «Governments are good at cutting off the heads of a centrally controlled networks like Napster, but pure P2P networks like Gnutella and Tor seem to be holding their own.» ([07.11.2008](https://satoshi.nakamotoinstitute.org/emails/cryptography/4/)) Kontext in [[bitcoin-regierungsresistenz]] und [[kryptoanarchismus-und-cypherpunks]].

### WikiLeaks

Als WikiLeaks Ende 2010 begann, Bitcoin als Spendenkanal zu erwägen, bat Nakamoto ausdrücklich darum, es zu lassen. Das Projekt sei zu jung für diese Art Aufmerksamkeit:

> The project needs to grow gradually so the software can be strengthened along the way. I make this appeal to WikiLeaks not to try to use Bitcoin. Bitcoin is a small beta community in its infancy.

([BitcoinTalk, 05.12.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/523/))

Sechs Tage später, sein vorletzter dokumentierter Forenpost: «It would have been nice to get this attention in any other context. WikiLeaks has kicked the hornet's nest, and the swarm is headed towards us.» ([11.12.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/542/)) Kurz darauf zog er sich zurück.

### Persönlichkeit und Humor

Zwischen den technischen Antworten scheint gelegentlich der Ton durch. Über die Schwierigkeit, Bitcoin zu erklären: «Writing a description for this thing for general audiences is bloody hard. There's nothing to relate it to.» ([05.07.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/167/)) In der Escrow-Debatte griff er zu einem Bild: «Imagine if gold turned to lead when stolen. If the thief gives it back, it turns to gold again.» ([11.08.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/340/)) Über Adressen: «It doesn't hurt anyone, so generate all you want.» ([16.05.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/98/)) Beim Logo fragte er schlicht in die Runde: «How does everyone feel about the B symbol with the two lines through the outside? Can we live with that as our logo?» ([26.02.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/83/))

### Identität und Abgang

Über die eigene Person gab Nakamoto fast nichts preis. Zur Entstehungszeit verriet er nur: «Since 2007. [...] Much more of the work was designing than coding.» ([18.06.2010](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/127/)) Die letzte im Institut gelistete Äußerung stammt von 2014, nachdem *Newsweek* Dorian Nakamoto als Erfinder benannt hatte:

> I am not Dorian Nakamoto.

([P2P Foundation, 07.03.2014](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/4/))

Zur Person, zum Abgang und zu späteren Identitätsbehauptungen siehe [[bitcoin-whitepaper]] und [[craig-wright-faketoshi]].

## Related

- [[the-quotable-satoshi]]
- [[bitcoin-whitepaper]]
- [[satoshi-ankuendigung-2009]]
- [[bitcoin-mining-und-proof-of-work]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-netzwerk-und-nodes]]
- [[bitcoin-absolute-knappheit]]
- [[bitcoin-mining-energiequellen]]
- [[bitcoin-regierungsresistenz]]
- [[zitate]]

## Open Questions

- Wie ist Nakamotos Node-Konsolidierungs-Sicht («never more than 100K nodes») mit dem heutigen Ideal maximaler Node-Dezentralisierung zu vereinbaren?
- War die WikiLeaks-Bitte ein taktisches Zeitproblem oder Ausdruck einer grundsätzlichen Haltung zur Anwendung?
- Wie viel von Nakamotos Skalierungsplan (SPV, Server-Farmen, kleine Node-Zahl) ist durch Lightning und moderne Full-Node-Praxis überholt?
- Nakamotos Skepsis zur Deutbarkeit des Regressionstheorems: Hat sich die österreichische Debatte seither auf eine Antwort zubewegt?
