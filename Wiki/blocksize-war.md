# Der Blocksize-Krieg (2015–2017)

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[blocksizewar]], [[20181114_bitcoinmagazine-when-fork-forks-bitcoin-cash-goes-war]], [[20181116_bitcoinmagazine-one-day-after-bch-hard-fork]], [[20181123_bitcoinmagazine-one-week-later-bitcoin-cash-split]], [[20181201_bitcoinmagazine-bch-hash-war-came-and-went]], [[20181209_bitcoinmagazine-bitcoin-abc-bitmain-ver-suit-bch-split]]

## Summary

Der Blocksize-Krieg war ein zweijähriger Konflikt (2015–2017) darüber, wer die Konsensregeln von Bitcoin kontrolliert. Die Big-Blocker, angeführt von Gavin Andresen, Roger Ver, Jihan Wu und später Jeff Garzik, wollten das 1-MB-Blocklimit per Hard Fork erhöhen, um mehr On-Chain-Transaktionen zu ermöglichen. Die Small-Blocker, darunter Gregory Maxwell, Adam Back, Peter Todd und das Bitcoin-Core-Team, setzten auf Soft Forks, Kapazitätserweiterung durch SegWit und Layer-2-Lösungen wie Lightning. Nach einer Reihe gescheiterter Fork-Versuche (Bitcoin XT, Bitcoin Classic, Bitcoin Unlimited, BTC1/SegWit2x) endete der Krieg am 8. November 2017 mit der bedingungslosen Kapitulation der SegWit2x-Befürworter. SegWit wurde aktiviert, Bitcoin Cash überlebte als Splitter-Coin — und der Konflikt legte den Grundstein für das Prinzip, dass Endnutzer und nicht Miner oder Unternehmen die letzte Entscheidungsgewalt über Bitcoins Protokollregeln haben.

## Body

### Hintergrund: Das 1-MB-Limit

Satoshi Nakamoto hatte das 1-MB-Blocklimit ursprünglich als temporäre Spam-Schutzmaßnahme eingeführt. Mit wachsender Bitcoin-Nutzung ab 2013 füllten sich die Blöcke zusehends, Transaktionsgebühren stiegen, und die Warteschlange im Mempool wurde länger. Diese Entwicklung lieferte den Big-Blockern ihr zentrales Argument: Bitcoin könne kein globales Zahlungssystem werden, wenn es nicht auf höheres On-Chain-Volumen skaliert.

Die Small-Blocker sahen das anders. Für sie war die Dezentralisierung des Netzwerks wichtiger als niedriger Gebühren. Größere Blöcke bedeuten größere Datenmengen, höhere Bandbreitenanforderungen für Nodes, und damit weniger Leute, die einen Full Node betreiben können. Das konzentriere die Netzwerkkontrolle auf wenige große Akteure. Ihr Skalierungsansatz: Kapazität durch technische Verbesserungen des Protokolls (SegWit) steigern und teure On-Chain-Transaktionen in Layer-2-Systeme (Lightning Network) verlagern.

### Die Hauptakteure

**Big-Blocker:** Gavin Andresen war der von Satoshi ernannte Nachfolger als Bitcoin-Chefentwickler und der prominenteste Vertreter der Big-Blocker. Mike Hearn, damals bei Google beschäftigt, arbeitete mit ihm am Bitcoin-XT-Client. Roger Ver ("Bitcoin Jesus"), früher bekannt für seine aggressive Bitcoin-Promotion, wurde zum lautesten öffentlichen Fürsprecher. Jihan Wu, Co-CEO von Bitmain (dem dominierenden ASIC-Hersteller und Mining-Pool-Betreiber), lieferte die Mining-Hashrate. Jeff Garzik und Mike Belshe (BitGo) übernahmen später die Führung im SegWit2x-Projekt. Barry Silbert (Digital Currency Group) koordinierte die Wirtschaftsseite.

**Small-Blocker:** Gregory Maxwell (Blockstream-Mitgründer, Bitcoin-Core-Entwickler) war der intellektuelle Motor. Adam Back (Hashcash-Erfinder, Blockstream-CEO) gab dem Lager öffentliche Sichtbarkeit. Pieter Wuille entwickelte SegWit als technische Lösung. Peter Todd, Luke Dashjr und zahlreiche weitere Core-Entwickler standen auf dieser Seite. "Shaolinfry", ein pseudonymer Entwickler, erfand den UASF (User-Activated Soft Fork).

### Chronologie

**September 2015 — Scaling I, Montreal:** Die erste Scaling-Konferenz. Gregory Maxwell trug den Spitznamen "One Meg Greg" ein und erläuterte die Blockstream-Position. Peter Rizuns "Produktionsquoten"-Argument gegen das Blocklimit sorgte für Schlagzeilen. Die Big-Blocker nannten die Konferenzserie später "Stalling Bitcoin".

**Dezember 2015 — Scaling II, Hongkong:** Pieter Wuille stellte SegWit erstmals vor — einen Soft Fork, der Signaturdaten vom Transaktionskörper trennt, Transaction Malleability behebt und die effektive Kapazität auf etwa 2 MB steigert. Wang Chun von F2Pool war auf dem Mining-Panel vertreten. Roger Ver tauchte hier erstmals als prominente Figur auf. Bitcoin XT war zu diesem Zeitpunkt praktisch tot.

**Januar 2016 — Mikes Abgang:** Mike Hearn veröffentlichte am 14. Januar 2016 einen Blogeintrag, in dem er Bitcoin für gescheitert erklärte. Der Text erschien in der New York Times und schadete dem Ruf der Big-Blocker erheblich. Kurz zuvor waren XT-Nodes unter DDoS-Attacken geraten.

**Februar 2016 — Bitcoin Classic und Hongkong-Abkommen:** Bitcoin Classic erschien am 10. Februar 2016 als Nachfolger von XT mit einer einfacheren 2-MB-Erhöhung. Sein 75%-Aktivierungsfenster war eine strukturelle Schwäche, weil es einen asymmetrischen Wipeout ermöglichte: Die kleine Mining-Minderheit konnte die Hard Fork rückgängig machen, aber der umgekehrte Fall galt nicht. Parallel fand am 20. Februar der "Runde Tisch Hongkong" statt. Bier schildert, wie er uneingeladen erschien und die nächtlichen Verhandlungen bis 4 Uhr früh miterlebte. Jihan Wu forderte, die Hard Fork müsse vor SegWit kommen. Ein Abkommen wurde unterschrieben, war aber rechtlich nicht durchsetzbar.

**Mai 2016 — Faketoshi:** Am 2. Mai 2016 erklärte Craig Wright öffentlich, Satoshi Nakamoto zu sein, und Gavin Andresen bestätigte das. Die angeblichen kryptografischen Beweise erwiesen sich als Betrug: Craig hatte eine bereits existierende Blockchain-Signatur kopiert. Gavin verlor daraufhin seinen Commit-Zugang zum Bitcoin-Repository. Das Faketoshi-Debakel spaltete die Big-Blocker-Community und stärkte die Glaubwürdigkeit der Small-Blocker.

**Juni–Juli 2016 — Die DAO und die Ethereum-Lehre:** Der Hack des Ethereum-DAO-Fonds am 17. Juni 2016 und der anschließende Hard Fork vom 20. Juli führten zu Ethereum Classic — einem Minderheits-Fork mit 5–10% der ursprünglichen Hashrate. Barry Silbert kaufte ETC bei $0,50. Für Bitcoin war das Ereignis ein Wendepunkt: Miner sahen, dass Chain-Splits real und potenziell teuer sind. Das verzögerte neue Fork-Versuche und hielt das Mining-Lager zögerlicher.

**Oktober 2016 — Scaling III, Mailand:** Jihan Wu kündigte öffentlich an, SegWit nicht zu unterstützen. Jake Smith bereiste China, um Miner gegen SegWit zu mobilisieren. Am 1. November erschien Bitcoin Core 0.13.1 mit SegWit-Parametern.

**Ende 2016 bis Frühjahr 2017 — Bitcoin Unlimited:** Bitcoin Unlimited versuchte eine Alternative mit einem komplexen Drei-Parameter-System (MG/EB/AT) für "Emergent Consensus". Das "Sticky Gate" führte zu perverser Anreizstruktur, und der "Median EB"-Angriff war eine bekannte Schwäche. Im März 2017 legte ein DoS-Bug ~600 von 776 BU-Nodes lahm. Jihan drohte, die kleine Block-Chain anzugreifen, und ein angebliches Angriffsbudget von 100 Millionen US-Dollar kursierte.

**März 2017 — Börsen deklarieren:** Am 17. März 2017 erklärten Bitfinex, Kraken, Bitstamp, Poloniex und BitMEX gemeinsam, dass Bitcoin Unlimited kein Bitcoin sei und Replay-Schutz notwendig sei. Am nächsten Tag listete Bitfinex BTU-Futures gegenüber BCC (Bitcoin Cash). BTU kam nie über 20% des Bitcoin-Preises hinaus und verfiel wertlos.

**April 2017 — ASICBoost-Enthüllung:** Am 5. April 2017 veröffentlichte Gregory Maxwell eine E-Mail, die covertés ASICBoost beschrieb: eine 20%-Effizienzsteigerung beim Mining durch Manipulation des Merkle-Root-Feldes. SegWit würde diese Methode inadvertent blockieren. Bitmain bestritt es zunächst, bestätigte aber Tests im Testnet. Gavin Andresen verteidigte Bitmain. Das Patent landete 2018 in einem defensiven Pool; offenes ASICBoost ist heute in über 70% der Blöcke aktiv.

**Februar–April 2017 — Litecoin als Testlauf:** Am 12. Januar 2017 brachte "Shaolinfry" einen SegWit-Client für Litecoin heraus. Am 9. April wurde UASF für Litecoin aktiviert. Jiang Zhuoer versuchte mit Hashrate, SegWit zu blockieren. Am 21. April brachte ein Litecoin-Roundtable einen Kompromiss: SegWit plus Hard Fork wenn 50% Kapazität erreicht. Litecoin aktivierte SegWit im Mai 2017. Das zeigte, dass SegWit in der Praxis funktionierte.

**Februar–Juli 2017 — UASF (BIP 148):** Am 25. Februar 2017 schlug Shaolinfry eine User-Activated Soft Fork vor. Am 12. März wurde BIP 148 veröffentlicht: Ab dem 1. August 2017 würden Nodes, die BIP 148 liefen, Blöcke ohne SegWit-Signaling ablehnen. Gregory Maxwell war dagegen (zu riskant für die Nutzer), Pieter Wuille ebenfalls. Luke Dashjr unterstützte es. Jihan Wu postete ein Jonestown-Foto mit dem Hashtag #UASF. ViaBTC listete UASF-Futures (die wertlos verfielen). Am 14. Juni 2017 kündigte Bitmain einen UAHF (User-Activated Hard Fork) als Gegenmaßnahme an — den Ursprung von Bitcoin Cash — mit 72-stündigem geheimem Mining.

**Mai 2017 — Das New Yorker Abkommen:** Am 22. Mai 2017 versammelten sich auf Einladung von Barry Silbert 58 Unternehmen in New York. Das NYA (New York Agreement) sah zwei Phasen vor: SegWit-Aktivierung über 80% Miner-Signaling (Bit 4) und eine 2-MB-Hard-Fork sechs Monate später. 83,28% der Hashrate unterzeichneten. James Hillards BIP 91 diente als Brücke zwischen NYA-Bit-4 und BIP-148-Bit-1. Jeff Garzik wurde Hauptentwickler von BTC1, dem SegWit2x-Client. BIP 91 wurde am 21. Juli gesperrt, am 26. Juli begann obligatorisches Signaling für Bit 1. SegWit aktivierte bei Block 481.824 am 24. August 2017.

**August 2017 — Bitcoin Cash:** Am 30. Juni 2017 präsentierte Amaury Sechet auf der Arnheim-Konferenz Bitcoin ABC. Am 12. Juli wurde der Client veröffentlicht. Am 17. Juli nannte ViaBTC die Fork "Bitcoin Cash" (BCC/BCH). Erst sechs Tage vor dem Start fügte Ben Delo obligatorischen Replay-Schutz durch, was einen sauberen Split erst ermöglichte. Der letzte gemeinsame Block war 478.559, gemint am 1. August 2017 um 13:16 UTC. Der erste BCH-Block trug die Nachricht "Willkommen auf der Welt, Shuya Yang!" und war 1,9 MB groß (ViaBTC). BCH handelte zunächst bei 10–12% des Bitcoin-Preises.

**September–Oktober 2017 — NYA zerfällt:** Die Unterzeichner begannen das NYA zu verlassen. Bitwala (22. August), F2Pool (31. August), Wayniloans, Vaultoro, surBTC, Crypto Facilities — einer nach dem anderen. Bitfinex und BitMEX erklärten, SegWit2x als alternativen Coin (B2X) zu behandeln und nicht als Bitcoin, unabhängig von der Hashrate. Arthur Hayes von BitMEX nannte ihn "ShitCoin2x". Am 24. Oktober kündigte Jeff Garzik den neuen Altcoin "Metronome" an. Coinbase erklärte zuerst, die bestehende Chain als Bitcoin zu betrachten, ruderte dann zurück und wollte der Chain mit der höchsten kumulierten Schwierigkeit folgen — eine Position, die weder klar noch operativ sinnvoll war.

**Scaling IV, Stanford, 4./5. November 2017:** Praktisch niemand auf der Konferenz unterstützte noch SegWit2x. Bobby Lee, einer der letzten Befürworter, weigerte sich in seiner Rede, das Thema SegWit2x anzusprechen, um Gegenfragen zu vermeiden.

**8. November 2017 — Kapitulation:** Um 16:58 Uhr UTC schickte Mike Belshe eine E-Mail an die SegWit2x-Mailingliste, unterzeichnet von Belshe, Wences Casares, Jihan Wu, Jeff Garzik, Peter Smith und Erik Voorhees. Sie erklärten, Phase zwei des NYA auszusetzen, weil kein ausreichender Konsens erreicht worden sei. Bier markiert diesen Punkt — 816 Tage nach Kriegsbeginn — als Ende der offiziellen Feindseligkeiten. Am 15. November stellte sich heraus, dass der BTC1-Client gravierende Bugs enthielt: Die Hard Fork-Logik griff zwei Blöcke zu früh (Höhe 494.782 statt 494.784). Die SegWit2x-Chain hätte selbst wenn die Kapitulation nicht gekommen wäre aus technischen Gründen nie funktioniert.

### Nebenhandlungsstränge

**Höhle der Löwen:** Joseph Poon enthüllte die Existenz eines geheimen Small-Blocker-Koordinations-Slacks mit 21 Mitgliedern, der für 24/7-PR und Meme-Produktion genutzt wurde. Bram Cohens Bildschirm zeigte versehentlich den Channelnamen "Lions' Den" in einem Video. Bier infiltrierte den Channel und beobachtete, dass beide Seiten identische PR-Taktiken verwendeten.

**ASICBoost im Kontext:** Covertés ASICBoost war für Bitmain ein strategischer Vorteil, den SegWit beseitigt hätte. Das erklärte Jihans hartnäckigen Widerstand gegen SegWit nach Mailand besser als ideologische Überzeugung allein.

**Replay-Schutz als Kernfrage:** Die Weigerung der SegWit2x-Befürworter, Replay-Schutz einzubauen, war für viele Exchanges das entscheidende Ausschlusskriterium. Ohne Replay-Schutz hätte eine Transaktion auf beiden Chains gleichzeitig gültig gewesen — gefährlich für jeden, der beide Coins halten wollte.

### Nachwirkungen und Epilog

Bitcoin Cash stieg nach der SegWit2x-Absage kurzzeitig auf 48% des Bitcoin-Preises (November 2017), fiel dann aber schnell zurück. Bis Anfang 2021 notierte BCH bei etwa 1% des Bitcoin-Preises. Ironischerweise hatte das On-Chain-Volumen auf Bitcoin via SegWit das BCH-Volumen bereits im März 2018 überholt. Bitmain investierte mehr als 888 Millionen US-Dollar in Bitcoin Cash; der Börsengangversuch in Hongkong (August 2018) scheiterte, und das Unternehmen erlitt schwere Verluste.

Im November 2018 spaltete sich Bitcoin Cash ein zweites Mal. Craig Wright und nChain lehnten geplante ABC-Upgrades (CTOR, OP_CHECKDATASIG) ab und veröffentlichten Bitcoin SV (Satoshi's Vision) mit 128-MB-Blöcken. Wright drohte öffentlich mit einem 51%-Angriff auf die ABC-Chain. Sein Lager — CoinGeek, SVPool, BMG Pool — kontrollierte bis zu 70 Prozent der BCH-Hashrate. Der Fork vollzog sich am 15. November 2018 um 18:07 UTC, als Bitcoin.com den ersten ABC-Block fand, den das SV-Netzwerk ablehnte. Die angedrohten 51%-Angriffe blieben aus. Bitcoin ABC konterte mit einem unangekündigten 10-Block-Checkpoint, der tiefe Reorganisationen blockierte. Zwei Wochen nach dem Split erklärte Calvin Ayre den Hash War für beendet und gab den Namen "Bitcoin Cash" sowie das Ticker-Symbol BCH auf. BCHABC handelte bei $150–200, BCHSV bei $75–100. Roger Ver kommentierte: "Die Core-Leute waren früher wirklich gegen jede Art von umstrittener Hard Fork, und ich denke, dass die Angst davor berechtigt ist, denn wir sehen gerade, welchen Schaden eine umstrittene Hard Fork anrichten kann."

### Wer hatte recht?

Bier unterscheidet zwischen zwei Fragen. In der engbegrenzten Frage der Blockgröße: unentschieden. Möglicherweise wäre eine moderate Hard Fork auf 2 MB ein guter pragmatischer Schritt gewesen — wir werden es nie wissen. In der umfassenderen Frage — wer kontrolliert Bitcoins Protokollregeln? — standen die Small-Blocker klar auf der richtigen Seite. Industrie-Meetings können keine Protokollregeln beschließen. Miner können Regeln nicht lockern. Nur Endnutzer und Investoren, die Änderungen durch ihre Node-Wahl und Marktnachfrage gutheißen, können Konsensregeln verändern. Das ist die finanzielle Souveränität, die Bitcoin einzigartig macht.

Bier schließt mit einer Warnung: Der Blocksize-Krieg hat Bitcoin nur Zeit verschafft. Zukünftige Angriffe — wahrscheinlich durch das Finanz- und politische Establishment, mit deutlich mehr Ressourcen — werden eher um Zensurresistenz als um Blockgrößen gehen. Der Ausgang ist ungewiss.

## Related

- [[segregated-witness-segwit]]
- [[soft-fork-und-hard-fork]]
- [[skalierung-lightning-ark-statechains]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[kryptoanarchismus-und-cypherpunks]]
- [[craig-wright-faketoshi]]

## Open Questions

- Hätte eine moderate 2-MB-Hard Fork per breitem Konsens 2015–2016 Bitcoin tatsächlich geschadet?
- Welche Rolle spielte ASICBoost im Vergleich zur ideologischen Überzeugung bei Jihans SegWit-Widerstand?
- Wie wird der nächste große Governance-Konflikt in Bitcoin aussehen — und wer sind dann die Akteure?
- Hätte der UASF (BIP 148) ohne das NYA als Brücke funktioniert, oder wäre er an Miner-Ablehnung gescheitert?
