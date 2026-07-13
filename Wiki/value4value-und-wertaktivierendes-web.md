# Value4Value und das wertaktivierende Web

**Status:** established
**Themen:** lightning, oekonomie, philosophie
**Last updated:** 2026-06-23
**Sources:** [[Eine Vision für wertaktivierendes Web.md]], [[aprycot-gigi-freiheit-der-werte.md]]

## Summary

Gigi analysiert die strukturellen Defekte des heutigen Internets — Empörungsmaximierung, „Du bist das Produkt"-Modelle, Micropayment-Unmöglichkeit, KYC-Zwang — und führt sie auf eine gemeinsame Ursache zurück: konventionelle Währungen können im Cyberspace nur als Kredit (IOUs) existieren, nicht als Bargeld. Bitcoin und Lightning ermöglichen erstmals digitales Inhabergeld ohne Gegenparteirisiko, was eine neue Ökonomie des Webs ermöglicht, in der Wert direkt zwischen Produzenten und Konsumenten fließt.

## Body

### Die Diagnose: Kaputte Anreize im Web

Das Web leidet an sechs ineinandergreifenden Problemen: kaputte Anreize, technische Begrenzungen, Kredit statt Bargeld, Aufmerksamkeit als Ersatzwährung, fehlende Konsequenzen und Zwangs-Identität.

Charlie Mungers Grundsatz — „Zeigen Sie mir die Anreize und ich werde Ihnen das Ergebnis zeigen" — erklärt das Meiste: Wer Werbeeinnahmen maximiert, muss Empörung maximieren. Wer Nutzerdaten verkauft, muss Nutzer einsperren. Die Plattformen sind nicht moralisch gescheitert; sie folgen rationalen Anreizen in einem kaputten System.

### Das Kredit-Problem

Konventionelle Währungen sind offline Münzen — im Cyberspace können sie nur als IOUs übertragen werden. Ein IOU ist kein Bargeld, sondern Kredit mit Gegenparteirisiko. Gegenparteirisiko erfordert:
- Identitätsverifizierung (KYC)
- Rückbuchungsmechanismen
- Hohe Transaktionsgebühren (Minimum ~$5 damit rentabel)
- Abo-Modelle statt Einzelzahlungen

Satoshi Nakamoto formulierte es 2009: „Ihre massiven Gemeinkosten machen Micropayments unmöglich."

Das ist der Grund, warum kostenlose Plattformen mit Werbung finanziert werden: Nicht weil Werbung das beste Modell ist, sondern weil Einzelzahlungen unter $5 mit konventionellen Zahlungssystemen unwirtschaftlich sind.

### Aufmerksamkeit als Ersatzwährung

Da Micropayments nicht funktionieren, entstand die Aufmerksamkeitsökonomie. Zeit und Aufmerksamkeit sind als Währung jedoch ungeeignet — man kann sie nicht horten. Die Folge: Plattformen konkurrieren um maximale Verweildauer, nicht um maximalen Wert. Nuancen und langsamere Informationen verlieren gegenüber Empörung und Konflikten, die Engagement erzeugen.

Gigi: „Indem wir Aufmerksamkeit als De-facto-Währung im Internet verwenden, zerstören wir Tiefe und Nuancen sowie unsere kollektive Aufmerksamkeitsspanne."

### Bitcoin als Lösung: Digitales Bargeld

Bitcoin ist das erste Geld, das von Natur aus digital ist — kein IOU, kein Kredit, kein Gegenparteirisiko. Das Lightning Network ermöglicht Zahlungen in der Größenordnung von Satoshis (Bruchteile von Cent) nahezu kostenlos und in Echtzeit.

Die Konsequenzen:
- **Geringere Reibung**: Kein KYC, keine Zwischenhändler, kein Konto nötig
- **Peer-to-Peer**: Wie physisches Bargeld — niemand ist zwingend Mittler
- **Neutralität**: Offenes Protokoll, kein Gatekeeper, kein Deplatforming
- **Reale Kosten im Cyberspace**: Spam-Bots werden unrentabel, wenn jede Aktion echte Kosten hat

### Das Value4Value-Modell

Value4Value (V4V) ist das konkrete Anwendungsmodell: Konsumenten senden Wert direkt an Produzenten, proportional zum wahrgenommenen Wert — ohne Mittler, ohne Abo-Zwang.

Podcasting 2.0 ist das erste skalierte Beispiel: Hörer können während eines Podcasts Sats streamen (Value-Streaming), nicht nur nach Abschluss. Die Apps Fountain, Breez und andere implementieren dies. Der „Value Block" im Podcast-Namespace definiert, wie Sats auf Hosts, Gäste und Produzenten aufgeteilt werden.

Weitere Beispiele: Stacker News (Sats statt Upvotes), „Boost"-Mechanismen in neuen Apps, direkte Lightning-Adressen für Autoren.

### Die digitale Knappheit des Produzenten

Gigi löst das Paradox digitaler Güter: JPGs, Blogposts und mp3s können zu Grenzkosten von null kopiert werden — sie sind nicht knapp. Aber die Menschen, die sie erstellen, sind knapp (Zeit, Talent, Energie). V4V trennt den Preis der Datei (null) vom Wert der Person dahinter (von Konsumenten freiwillig bestimmt).

„Wenn es uns gelingt, den Einsatz von Zeit und Aufmerksamkeit als Online-Währung zu reduzieren — werden Lärm und Abhängigkeit reduziert, während Freiheit und echte Signale maximiert werden."

### Das MTX-Problem und das DRM-Paradoxon

Gigi benennt zwei strukturelle Hindernisse, warum digitale Inhalte nicht wie normale Waren verkauft werden können. Das **MTX-Problem** (Mental Transaction Costs): Jede Bezahlschranke erzwingt eine bewusste Kaufentscheidung. Nick Szabo zeigte, dass die psychologischen Kosten dieser Entscheidung selbst bei minimalen Beträgen die Transaktion unattraktiv machen. Bei einem Stundenlohn von 20 USD und zwei Sekunden Überlegung kostet das Nachdenken mehr als der Preis der Transaktion. Flatrates und Abonnements lösen das Problem für stabile Konsumenten — für den Long Tail der Inhalte nicht.

Das **DRM-Paradoxon**: Man kann keine nicht-kopierbaren Informationen erschaffen. Bruce Schneier: „Der Versuch, digitale Dateien unkopierbar zu machen, ist wie der Versuch, Wasser nicht nass zu machen." Gute Inhalte werden immer freigesetzt; schlechte bleiben hinter Paywalls. Das Paradoxon: Bezahlschranken funktionieren nur für qualitativ schlechte Inhalte.

Beide Probleme löst Value-for-Value: Kein Paywall, kein DRM, keine Bezahlentscheidung vorab. Wer einen Wert empfangen hat, gibt freiwillig zurück. Die mentale Transaktionskosten sinken auf null — man entscheidet nicht vor dem Konsum, sondern danach. [[aprycot-gigi-freiheit-der-werte.md]]

### Plattformen vs. Protokolle

Gigi: „Plattformen für freie Meinungsäußerung können nicht existieren. Es kann nur Protokolle der freien Meinungsäußerung geben." Der Mechanismus: Wer Inhalte hosten oder übermitteln kann, wird unter staatlichem Druck zensieren. Selbst aufrichtige Plattformen werden irgendwann zur Zensur gezwungen — durch Haftungsfragen, Werbeabhängigkeit oder politischen Druck.

Plattformen unterliegen Anreizen, die zur Selbstzensur, Deplatforming und Meinungsmanipulation führen — nicht aus Bosheit, sondern aus Survival-Logik: Wer Empörung maximiert, überleben; wer kontrovers ist, verliert Werbeeinnahmen oder Plattform-Zugang. Das evolutionäre Umfeld selektion für Dopaminmaschinen (Gigi: TikTok als „Heroin gemischt mit Crack für den Verstand"). Protokolle — Bitcoin, Nostr, E-Mail, das Web selbst — unterliegen dieser Logik nicht, weil niemand sie kontrolliert. [[aprycot-gigi-freiheit-der-werte.md]]

### Vision des wertaktivierenden Webs

Die Vision (kein einzelnes Produkt, sondern ein Ökosystem offener Protokolle):
- Wert fließt direkt von Konsumenten zu Produzenten, ohne Gatekeeper
- Identität bleibt optional; Reputation entsteht durch kostspielige Signale (Sats statt gefälschte Likes)
- Antisoziales Verhalten wird teuer, ohne Deplatforming
- „Fatten the long tail" — nicht nur Top-Creators profitieren, sondern alle Produzenten im Long Tail
- Aufbau auf offenen Protokollen, nicht auf geschlossenen Plattformen

Satoshi Nakamoto, zitiert im Artikel: „Das Grundproblem der konventionellen Währung ist das Vertrauen, das erforderlich ist, damit sie funktioniert. [...] Ihre massiven Gemeinkosten machen Micropayments unmöglich."

Gigi: „Es ist Tag 2 für das Internet, und es ist an der Zeit, es zu reparieren."

## Related

- [[lightning-netzwerk-grundlagen]]
- [[bitcoin-als-zahlungsmittel]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoin-als-reserve-und-anlagegut]]
- [[proof-of-work-grundlagen]]

## Open Questions

- Wann erreicht V4V eine kritische Masse, die das Aufmerksamkeits-Modell wirklich verdrängt?
- Wie können Produzenten, die weder Bitcoin kennen noch Wallets haben, am einfachsten einsteigen?
- Nostr als Identitätsschicht — reicht das für das „wertaktivierende Web"?
