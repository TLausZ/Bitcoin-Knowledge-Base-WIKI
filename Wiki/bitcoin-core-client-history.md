# Bitcoin Core: Client-Geschichte und Namensfindung

**Status:** established
**Themen:** geschichte
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bitcoin-core-naming-history]], [[alex-waltz-bitcoin-v01-source-code-secrets]], [[alex-waltz-satoshi-alternative-names]], [[alex-waltz-satoshi-november-2008-version]]

## Summary

Was heute als „Bitcoin Core" bekannt ist, hiess ursprünglich schlicht „bitcoin". Der Name wurde erst 2014 nach einer langen Community-Debatte festgelegt. Der Weg dahin — von Satoshis frühen Experimenten über alternative Namen wie Netcoin bis zur ersten Veröffentlichung am 8. Januar 2009 — zeigt, wie provisorisch viele Grundentscheidungen waren, die heute als selbstverständlich gelten.

## Body

### Von Netcoin zu Bitcoin

Einen Tag vor der Registrierung von bitcoin.org meldete Satoshi netcoin.org an. In E-Mails an Adam Back (August 2008) und Wei Dai (August 2008) trug der White-Paper-Entwurf im Dateinamen das Wort „e-cash": `e-cash.pdf`. Der Titel lautete damals „Electronic Cash Without a Trusted Third Party" — kein „Bitcoin" weit und breit.

Der Name „Supercoin" taucht im prä-v0.1-Testcode auf, den Satoshi einer Handvoll Tester schickte. In mindestens einem Kommentar bezeichnet er die Mining-Funktion als SUPERCOIN.

### Was in v0.1 steckte, was nie genutzt wurde

Das ursprüngliche Bitcoin-Client-Release (8. Januar 2009) enthielt mehr als nur den Zahlungsprotokoll-Code:

- Ein unfertiges **Poker-Spiel** im Quellcode
- Ein **eBay-ähnlicher Marktplatz** (inklusive Satoshis Bewertungssystem für Verkäufer)
- Pläne für ein **Escrow-System**, das nie fertiggestellt wurde

Diese Funktionen waren auskommentiert oder unfertig, aber der Code war vorhanden. Satoshi hatte Bitcoin offenbar als eine Art dezentrale Handelsplattform mitgedacht — Zahlungen waren nur ein Teil davon.

### Satoshis November-2008-Version: Die 10 Unterschiede

Bevor Satoshi Bitcoin am 8. Januar 2009 öffentlich lancierte, existierte eine interne Testversion, bekannt als „November 2008 Version". Sie unterschied sich in zehn wesentlichen Punkten vom finalen Bitcoin:

1. **Kein Pre-Mining:** Satoshi startete Mining erst, als andere Peers im Netzwerk waren.
2. **Blockzeit 15 statt 10 Minuten.**
3. **Difficulty-Anpassungsperiode 30 Tage (2.880 Blöcke) statt 14 Tage (2.016 Blöcke).**
4. **1 Million Einheiten pro Bitcoin** statt 100 Millionen Satoshis.
5. **Halving alle 100.000 Blöcke** mit 100 Coins Belohnung, statt alle 210.000 Blöcke mit 50 BTC.
6. **Genesis-Block vom 10. September 2008**, ohne die berühmte Times-Headline.
7. **Blockchain hiess „Timechain"** — das Wort „blockchain" kommt im späteren Code vor.
8. **Keine Coinbase-Reife:** Frisch geminte Coins waren sofort ausgebbar. Die 100-Block-Wartezeit kam erst in der finalen Version.
9. **Minimaler Proof-of-Work** für Tests (Satoshi war allein).
10. **Feste Gebühren** (10.000 Einheiten), statt nutzerkonfigurierbarer Fees.

### Die Namensdebatte 2013/2014

Bis 2013 hiess der Client schlicht „bitcoin". Als Bitcoin als Netzwerk wuchs und weitere Implementierungen entstanden, erkannte die Community, dass eine Unterscheidung zwischen Netzwerk und Client nötig war. Die Debatte lief auf IRC, Reddit und im Bitcoin Foundation Forum.

Vorschläge: Nova, Origo, Bitcoin-Prime, Mercury, CoinTorrent (tatsächlich vorgeschlagen). „Bitcoin Core" wurde von Mike Hearn eingebracht — mit dem Einwand, es klinge zu „offiziell". Da Kernbeitragende ohnehin „Core Developers" genannt wurden, gewann der Name schliesslich.

Am 19. März 2014 erschien **Bitcoin Core 0.9.0**, das erste Release unter diesem Namen.

## Related

- [[bitcoin-fruehgeschichte]]
- [[bitcoin-launch-januar-2009]]
- [[bitcoin-whitepaper]]

## Open Questions

- Warum hat Satoshi das Poker-Spiel und den Marktplatz nie fertiggestellt — Prioritäten oder Bedenken?
- Welche anderen Designentscheidungen zwischen November 2008 und Januar 2009 sind noch nicht dokumentiert?
