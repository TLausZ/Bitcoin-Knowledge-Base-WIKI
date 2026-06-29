# Nostr-Protokoll

**Status:** established
**Last updated:** 2026-06-29
**Sources:** [[The Bitcoin Newsletter #2 - Bitcoin is not speculation.]], [[The Bitcoin Newsletter 14 - How Bitcoin & Nostr foster innovation without institutional credit]], [[Nostr_ The Importance of Censorship-Resistant Communication for Innovation and Human Progress]], [[redefreiheit-und-protokolle]]

## Summary

Nostr (Notes and Other Stuff Transmitted by Relays) ist ein offenes Kommunikationsprotokoll, das auf kryptografischen Schlüsselpaaren basiert statt auf Plattformkonten. Es entstand aus der Bitcoin-Community und wurde von Lightning-Entwickler fiatjaf geschrieben. Die Kernthese: Plattformen können keine echte Redefreiheit gewähren, weil sie Accounts sperren können. Ein Protokoll kann das nicht — wer den privaten Schlüssel hält, kontrolliert seine Identität.

## Body

### Wie Nostr funktioniert

Jede Nostr-Identität ist ein kryptografisches Schlüsselpaar: öffentlicher Schlüssel als Adresse, privater Schlüssel als Authentifizierung. Nachrichten (Notes) werden signiert und an Relay-Server weitergegeben, die sie verbreiten. Jeder kann einen Relay betreiben; kein einzelner Relay ist systemkritisch.

Das Modell ist das Gegenteil von Twitter/X: Dort gehört die Identität der Plattform. Auf Nostr gehört die Identität dem Schlüsselinhaber. Ein gesperrtes Konto auf einer Plattform ist permanent — ein gesperrter Nostr-Schlüssel auf einem Relay kann auf jedem anderen Relay weitergeführt werden. [[The Bitcoin Newsletter #2 - Bitcoin is not speculation.]]

In den ersten Wochen nach breiterer Bekanntheit (Januar 2023) wuchs die Zahl aktiver Accounts auf über 400.000. Edward Snowden postete dazu; Jack Dorsey spendete 14 BTC für die Entwicklung. Heute sind Apps wie Damus (iOS) und Amethyst (Android) die wichtigsten Clients.

### Cashu und Micropayments

Nostr integriert sich mit Lightning-basierten Zahlungen. Die Cashu-Integration erlaubt es, Ecash-Token direkt in Nostr-Nachrichten zu verschicken — ohne Mittler, als einfache Textnachricht. Das verbindet freie Kommunikation mit freiem Geldtransfer in einem einzigen Protokoll-Stack. [[Nostr_ The Importance of Censorship-Resistant Communication for Innovation and Human Progress]]

### Nostr und Innovation ohne institutionellen Kredit

Wankum (TBN #14) macht einen historischen Vergleich: Unter dem Goldstandard konnten Wright Brothers und Benz ihre Erfindungen selbst finanzieren — hartes Geld erlaubte Eigenkapitalbildung ohne Bankkredit. Das Fiat-System zentralisiert Kapitalallokation bei Banken und institutionellen Investoren, die nur Projekte mit Mainstream-Konsens finanzieren.

Bitcoin und Nostr brechen dieses Gatekeeping auf zwei Ebenen: Bitcoin erlaubt Selbstfinanzierung ohne Inflationsverlust. Nostr erlaubt Kommunikation und Koordination ohne zentrale Plattform-Erlaubnis. Zusammen ermöglichen sie Bottom-Up-Innovation, die im Fiat-System strukturell benachteiligt wird.

Das konkrete Beispiel aus TBN #26: Globale Kollaboration — etwa zwischen Entwicklern in Nigeria, El Salvador und den USA — war früher auf Plattformen wie GitHub oder Twitter angewiesen, die in autoritären Kontexten gesperrt werden können. Nostr macht das unmöglich. [[The Bitcoin Newsletter 14 - How Bitcoin & Nostr foster innovation without institutional credit]]

### Verhältnis zu Bitcoin

Gigi formuliert die Verbindung präzise (vgl. `redefreiheit-und-protokolle`): Bitcoin ist freies Geld, Nostr ist freie Kommunikation — beide sind Protokolle, keine Plattformen. Protokolle können keine Konten sperren. Diese Eigenschaft ist nicht verhandelbar, weil sie im Design liegt, nicht in einer Policy.

Die Lightning-Integration verbindet beide: Wer über Nostr kommuniziert, kann gleichzeitig per Lightning bezahlen. Value-for-Value-Modelle (Streaming Sats) werden direkt im Kommunikationsfluss möglich, ohne Zwischenhändler. [[redefreiheit-und-protokolle]]

## Related

- [[redefreiheit-und-protokolle]]
- [[value4value-und-wertaktivierendes-web]]
- [[bitcoin-unternehmens-strategie]]
- [[cypherpunk-manifest]]
- [[kryptoanarchismus-und-cypherpunks]]
- [[lightning-netzwerk-grundlagen]]

## Open Questions

- Wie skaliert Nostr mit stark wachsender Nutzerzahl — welche Relay-Infrastruktur ist tragfähig?
- Inwiefern ist Nostr wirklich zensurresistent, wenn Relays trotzdem filtern können?
- Cashu auf Nostr: Welche Datenschutzeigenschaften hat Ecash im Vergleich zu direkten Lightning-Zahlungen?
