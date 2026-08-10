# Defending Bitcoin

**Status:** established
**Themen:** protokoll, privacy, mining, self-custody, adoption, buecher
**Last updated:** 2026-08-10
**Sources:** [[2026_Defending-Bitcoin_deWolf]]

## Summary

Luke de Wolf (2026, Foreword: Mikko Hyppönen) überträgt die Sicherheitslogik industrieller Kontrollsysteme auf Bitcoin. Die These: Bitcoin funktioniert bereits als kritische Infrastruktur und verdient dieselbe verteidigende Ernsthaftigkeit wie Stromnetze und Pipelines. Das Buch analysiert Bitcoins Bedrohungslage systematisch mit dem ISA/IEC-62443-Framework und dem Purdue-Modell, von Exchange-Kollapsen bis Quantencomputern. Der Volltext ist frei lesbar auf [defendingbitcoin.com/reader](https://defendingbitcoin.com/reader); die Print-Ausgabe erschien am 31. Mai 2026.

## Body

De Wolf ist ICS-Cybersecurity-Berater (CISSP/GICSP, über zehn Jahre in der Öl- und Gasindustrie Kanadas, heute Finnland) und zugleich Bitcoin-Maximalist, Co-Host der Bitcoin Infinity Show und Co-Autor von [[bitcoin-inverse-of-clown-world]]. Das Buch richtet sich nach dem Vorbild von ICS-Security-Kursen an zwei Publika zugleich: Bitcoiner, die Cybersecurity lernen wollen, und Sicherheitsprofis, die Bitcoin nicht kennen. Teil I (Kapitel 1 bis 5) baut darum beide Fundamente auf, bevor Teil II (Kapitel 6 bis 15) die eigentliche Bedrohungsanalyse liefert.

Das Scharnier ist Kapitel 5. Bitcoin erfüllt die US-Definition kritischer Infrastruktur (NSM-22) schon heute: Hunderte Millionen Halter, Settlement-Finalität, die den Legacy-Rails überlegen ist, und auf Protokollebene kein nennenswerter Ausfall seit dem Chain Fork vom März 2013. Mining-Anlagen sind faktisch ICS-Umgebungen, auf die sich das Purdue-Modell direkt anwenden lässt (Level 0 = Hash-Berechnung bis Level 4+ = Enterprise-Schicht, wo auch Exchanges sitzen). Die zentrale Anpassung: 62443 kennt keinen Asset Owner für ein System, das niemandem gehört. De Wolfs Antwort ist das Leitmotiv des Buchs: «If you hold Bitcoin, you are your own asset owner» — der Nutzer ist Operator, Verteidiger und Auditor in einem.

Teil II organisiert die Threats in drei eskalierende Layer, jedes Kapitel mit Likelihood/Impact-Einschätzung (fünfstufig, Stand Anfang 2026) und Controls, die auf Security Levels (SL 1 bis 3+) und die 62443-Foundational-Requirements gemappt sind:

- Layer 1, Individuum (Kap. 6–8): Exchange-Kollapse von Mt. Gox bis FTX und Bybit ([[selbstverwahrung-und-boersenrisiken]]), Private-Key-Sicherheit von Seed-Phrase bis [[multisig-und-kollaborative-verwahrung]], Privacy und physische Angriffe ([[opsec-und-privatsphaere]]).
- Layer 2, Netzwerk (Kap. 9–12): [[bitcoin-mining-dezentralisierung]] (Template-Souveränität, Stratum V2, DATUM), Eclipse-Angriffe und Software-Bugs auf Node-Ebene ([[bitcoin-netzwerk-und-nodes]], [[bip-0324]]), die Spam-Debatte um Inscriptions und [[op-return-und-datenspeicherung]], Entwickler-Governance ([[bitcoin-commons-und-governance]]).
- Layer 3, extern und systemisch (Kap. 13–15): Regulierung und Debanking ([[bitcoin-rechtliche-angriffe]]), Strom- und Internetausfälle bis zu Tail-Risks wie Sonnenstürmen, schliesslich [[bitcoin-und-quantenrisiko]] und AI ([[bitcoin-mining-und-ki-rechenzentren]]).

Der rote Faden durch alle Layer ist Privacy als Sicherheitskontrolle statt politischer Haltung: Wer nicht als Halter bekannt ist, wird nicht zum Ziel, darum kehren Adress-Hygiene, [[coinjoin-und-on-chain-privatsphaere]] und [[no-kyc-bitcoin]] in fast jedem Kapitel wieder. Die Conclusion verdichtet alle Controls in eine Referenztabelle nach SL und FR; die SL-1-Stufe (Hardware-Wallet, Stahl-Backup, eigene Node, Tor, tiefes Profil) deckt nach de Wolf die grosse Mehrheit realer Bedrohungen ab.

Das Buch bezieht Stellung, wo die Community streitet. In der Spam-Debatte wertet de Wolf Arbitrary Data als Availability-Schwachstelle (36% des Blockspace Ende 2025, UTXO-Set von ~5 auf über 10 GB verdoppelt), hält Content-Type-Filtering nicht für Zensur und empfiehlt explizit Bitcoin Knots trotz Single-Maintainer-Risiko. Die Governance-Analyse benennt Konzentration beim Namen: fünf Core-Maintainer (Stand Februar 2026), Funding-Dominanz von Chaincode und Brink, die OP_RETURN-PR #32406 als Fallstudie gescheiterten Change-Managements ([[bitcoin-core-relay-statement]], [[blocksize-war]] als historischer Gegenbeweis, dass Nutzer Capture abwehren können). Beim Quantenrisiko rechnet er mit ~1.72 Mio. BTC in dauerhaft exponierten P2PK-Adressen und einem Migrationspfad von grob sieben Jahren (Chaincode-Schätzung), weshalb Vorbereitung heute beginnt; Taproot gilt aus Quantensicht als Rückschritt. Bei AI liegt die Gefahr in der Asymmetrie «Production scales with AI. Review doesn't.»

Den Schluss trägt eine Warnung statt einer Beruhigung: Bitcoins Antifragilität ist nicht im Protokoll eingebaut, sondern die Summe der Entscheidungen seiner Teilnehmer. Die einzige Bedrohung mit existenziellem Potenzial ist Massen-Komplazenz. Gerahmt wird das Ganze in nordischer Mythologie: Der Drache Níðhöggr nagt permanent am Weltenbaum Yggdrasil, und der Baum steht nur, weil er schneller nachwächst, als der Drache frisst.

## Related

- [[bitcoin-zensurresistenz]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[phishing-und-angriffsmethoden]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[eu-regulierung-selbstverwahrung]]
- [[bip-0110]]
- [[lightning-netzwerk-grundlagen]]
- [[bitcoin-mining-und-proof-of-work]]
- [[mining-schwierigkeit]]
- [[der-bitcoin-standard]] ← Buch
- [[softwar]] ← Buch

## Open Questions

- Die Likelihood/Impact-Ratings sind erklärtermassen informierte Urteile des Autors (Stand Anfang 2026), keine Messwerte; das Buch kündigt eine laufend aktualisierte Threat/Control-Datenbank auf der Website an (Companion), die als spätere Quelle taugen könnte.
- Einzelne Zahlen stammen aus Einzelquellen, etwa das AntPool-Template-Sharing über nominell getrennte Pools (Mempool.guide) und der Bitcoin-Reorg vom März 2026 um Block 941'881 als möglicher Selfish-Mining-Fall — im Buch selbst als umstritten markiert.
- Appendizes 1–3 der Print-Ausgabe sind in der Web-Edition nicht enthalten (online nur Glossare 4 und 5); Inhalt unbekannt.
