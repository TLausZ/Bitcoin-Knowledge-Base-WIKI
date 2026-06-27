# Mt. Gox

**Status:** established
**Last updated:** 2026-06-27
**Sources:** [[alex-waltz-mtgox-full-story]], [[bitcoin-fruehgeschichte]], [[selbstverwahrung-und-boersenrisiken]]

## Summary

Mt. Gox war von 2010 bis 2014 die dominante Bitcoin-Börse und wickelte zeitweise über 70 % des weltweiten BTC-Handels ab. Am 28. Februar 2014 meldete sie Insolvenz an und gab an, 850.000 Bitcoin verloren zu haben — 750.000 davon Kundengelder. Die offizielle Erklärung (Transaction-Malleability-Angriffe) war eine Halbwahrheit: Forensische Analysen zeigen, dass die Coins schon seit mindestens 2011 systematisch aus dem Hot Wallet abgezogen wurden. Der Fall gilt als das folgenreichste Versagen in der Bitcoin-Geschichte und als stärkstes Argument für Selbstverwahrung.

## Body

### Entstehung und frühe Jahre

Mt. Gox begann 2007 als Handelsbörse für Magic: The Gathering-Karten (*Magic: The Gathering Online eXchange*). Jed McCaleb baute die Plattform 2010 zu einer Bitcoin-Börse um. Im März 2011 verkaufte er sie an Mark Karpelès, als Bitcoin noch bei rund 1 US-Dollar handelte.

Karpelès übernahm damit auch die bekannt schwachen Sicherheitspraktiken der Plattform — in einem Markt, der kurz danach explodieren sollte. Bereits im Juni 2011 kompromittierte ein Angreifer einen Admin-Account, manipulierte den Preis kurz auf $0.01 und stahl ~2.000 BTC. Im Oktober 2011 schickte ein Software-Fehler weitere 2.609 BTC durch ungültige Adressen in den Abgrund. Beide Vorfälle wurden nicht öffentlich kommuniziert. [[alex-waltz-mtgox-full-story]]

### Der Kollaps: Chronologie Februar 2014

**4. Februar 2014.** Community-Tools, die Mt. Gox' öffentliche API überwachten, zeigten 41.390 BTC im Status "BAD Transaction" — bei damaligem Kurs (~$934) rund 38 Millionen US-Dollar. Mt. Gox bestätigte das Problem, sprach von einer technischen Störung bei grossen Transaktionen.

**7. Februar.** Mt. Gox pausierte alle Abhebungen, begründet mit dem erhöhten Transaktionsvolumen, das "die Plattform technisch überfordert" habe. Die Panik begann.

**10. Februar.** Die offizielle Erklärung: Transaction Malleability. Vor dem SegWit-Upgrade konnte ein Angreifer kleine Felder in einer Transaktion verändern, sodass zwei Versionen derselben Transaktion im Netzwerk auftauchten. Nur eine wurde bestätigt, aber Mt. Gox' Software erkannte die "mutierte" Version als Fehler — und sandte die Coins erneut aus. Der Angreifer konnte so mehrfach abheben, während das System dachte, die erste Auszahlung sei nie angekommen.

Das war ein realer Angriffsvektor. Die meisten anderen Dienste hatten ihn längst durch einfache Zusatzprüfungen abgesichert — Mt. Gox nicht. [[alex-waltz-mtgox-full-story]]

**14. Februar.** Kolin Burges (@The_K_meister) flog von London nach Tokio und protestierte vor dem Mt. Gox-Büro mit einem handgeschriebenen Schild: *"Mt.Gox, where is our money?"*

**23. Februar.** CEO Mark Karpelès trat aus der Bitcoin Foundation zurück; der Twitter-Account der Börse wurde geleert.

**24. Februar.** Alle Handelsaktivitäten eingestellt, Website offline.

**28. Februar.** Insolvenzanmeldung beim Tokyoter Gericht. Bestätigt: 850.000 BTC verschwunden.

### Die Malleability-These war eine Halbwahrheit

Ein Paper von Christian Decker und Roger Wattenhofer (26. März 2014) wertete alle Malleability-Angriffe auf das Bitcoin-Netzwerk aus. Ergebnis: Insgesamt waren 302.000 BTC in solchen Angriffen involviert, davon nur 1.811 BTC in Angriffen *vor* dem Abhebungsstopp. 78,64 % dieser Angriffe scheiterten ohnehin.

[Chart: Verlauf der Malleability-Angriffe auf dem Bitcoin-Netzwerk (grüne/blaue Linie) — Original: [X-Thread](https://x.com/raw_avocado/status/2026689179615100981)]

Das lässt ~849.600 BTC ohne Erklärung. Der interne "Crisis Strategy Draft", der am 25. Februar geleakt wurde, enthielt die deutlichere Formulierung: "744.408 BTC waren aufgrund von Malleability-Diebstählen verschwunden, die jahrelang unbemerkt blieben. Der Cold-Storage war durch ein Leck im Hot Wallet geleert worden." [[alex-waltz-mtgox-full-story]]

### Was wirklich passierte: der WizSec-Befund

2015 veröffentlichte WizSec (@wizsecurity) eine forensische Analyse der Mt. Gox-Wallets ([Quelle](https://blog.wizsec.jp/2015/04/the-missing-mtgox-bitcoins.html)). Ihr Befund: Die Coins wurden ab spätestens Ende 2011 kontinuierlich aus dem Hot Wallet abgezogen. Die Methode war simpel, weil interne Transfers zwischen Cold- und Hot-Wallet nicht überwacht wurden.

Schema: Coins aus Cold Storage in den Hot Wallet → von dort an externe Adressen. Niemand kontrollierte, ob diese Abflüsse legitim waren. Jemand mit Systemzugang konnte diesen Prozess unbegrenzt wiederholen.

[Chart: Mt. Gox-Soll (blau) vs. tatsächlich vorhandene BTC (orange) 2011–2014 — Original: [X-Thread](https://x.com/raw_avocado/status/2026689179615100981)]

Mt. Gox war demnach de facto jahrelang insolvent — spätestens ab 2013 waren kaum noch Coins vorhanden. Wer genau die Coins gestohlen hat, ist bis heute nicht rechtskräftig festgestellt. [[alex-waltz-mtgox-full-story]]

### Preischaos in den letzten Tagen

Auch nach dem Abhebungsstopp handelten verzweifelte Nutzer auf Mt. Gox weiter Bitcoin gegen Fiat. Der interne Preis brach auf $130–$133 ein, während Bitcoin auf Bitstamp und BTC-e bei $450–$550 stand. Die Spanne zeigt, wie gering das Vertrauen in die Auszahlung war — und wie viele Nutzer lieber zu jedem Preis raus wollten.

### Karpelès: Verhaftung und Urteil

Am 1. August 2015 wurde Mark Karpelès in Tokio verhaftet. Vorwürfe: Unterschlagung, Vertrauensbruch und Datenmanipulation.

Er verbrachte knapp 11 Monate in U-Haft. Im März 2019 sprach ihn das Tokyoter Bezirksgericht von Unterschlagung und Diebstahl frei, verurteilte ihn aber wegen Fälschung elektronischer Daten (er hatte die scheinbaren Guthaben der Börse um ~33,5 Millionen US-Dollar aufgebläht). Strafe: 2,5 Jahre, vollständig auf Bewährung ausgesetzt. Zusätzliche Haft: keine. [[alex-waltz-mtgox-full-story]]

### Gläubiger-Saga: Stand 2026

Im März 2014 wurden ~200.000 BTC in alten Cold-Storage-Wallets wiedergefunden. Die Auszahlungen an Gläubiger begannen aber erst 2024 ernsthaft. Bis früh 2026 haben rund 19.500 Gläubiger Teilauszahlungen erhalten; tausende warten noch. Die Frist für die letzte Zahlung liegt derzeit bei 31. Oktober 2026 — der Treuhänder hat sie mehrfach verschoben, zuletzt im Oktober 2025. [[alex-waltz-mtgox-full-story]]

### Bedeutung für das Bitcoin-Ökosystem

Mt. Gox war für Jahre die einzige reale Möglichkeit, Bitcoin zu kaufen. Ohne sie hätte sich der Markt kaum so schnell entwickelt. Gleichzeitig machte der Kollaps die Kosten von Drittverwahrung unübersehbar.

Das Proof-of-Keys-Prinzip — "not your keys, not your Bitcoin" — hat in Mt. Gox seinen stärksten historischen Beleg. Wer Coins auf einer Börse lässt, hält eine Forderung, kein Bitcoin. Dieser Unterschied kostet im Ernstfall alles.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-fruehgeschichte]]
- [[segregated-witness-segwit]] (SegWit löste u.a. Transaction Malleability)
- [[hardware-wallet-einstieg]]
- [[bitcoin-skalierung-und-zahlungen]]

## Open Questions

- Wer hat die Coins tatsächlich gestohlen? WizSec deutet auf einen internen Akteur hin, rechtskräftig ist nichts.
- Warum wurden Karpelès' Unterschlagungs-Anklagen fallen gelassen? Die Beweislage war offenbar nicht ausreichend.
- Wie viele der 200.000 wiedergefundenen BTC stammen aus dem ursprünglichen Diebstahl vs. legitimen Cold-Storage-Reserven?
