# Stablecoins und agentische Zahlungen: Die Stripe-Infrastruktur

**Status:** emerging
**Last updated:** 2026-07-05
**Sources:** [[stripe_sessions2026-Opening remarks and product keynote]]

## Summary

Die Stripe-Sessions-Keynote 2026 zeigt, wie schnell Stablecoin-Rails in die Mainstream-Zahlungsinfrastruktur einziehen. Stripe baut mit Bridge (Orchestrierung), Privy (Wallets) und der eigens mit Paradigm entwickelten Blockchain Tempo einen vollständigen Stack für programmierbares Geld: Streaming-Micropayments für KI-Agenten, Stablecoin-Auszahlungen an 250 Millionen Link-Konsumenten, Treasury-Konten mit Stablecoin-Rails in 100 Ländern. Für die Bitcoin-Perspektive relevant: Hier entsteht ein zentralisiert kontrolliertes, aber global funktionierendes «Internet-Geld», das viele Alltags-Zahlungsprobleme löst, die auch Bitcoin adressiert, allerdings ohne Zensurresistenz und mit Fiat-Bindung.

## Body

### Die These: Agenten zahlen mit Stablecoins

Stripe positioniert Stablecoins als Standardzahlungsmittel für KI-Agenten. Das Argument ist technisch: Karten, ACH, UPI oder Pix können keine Beträge im Subcent-Bereich in Echtzeit und irreversibel abwickeln. Wer Compute pro Token abrechnen will, braucht Geld, das sich im Millisekundentakt in Bruchteilen von Cents bewegen lässt. In der Live-Demo wurde ein «tokens-paid-as-burned»-Geschäftsmodell gezeigt: KI-Agenten verbrennen Tokens, parallel streamen Stablecoin-Micropayments von je drei Tausendstel Cent über die Tempo-Blockchain, sichtbar im Block Explorer.

Ergänzend dazu das Machine Payments Protocol (MPP), ein offener Standard, über den Dienste einem Agenten direkt per HTTP mitteilen, dass und wie zu zahlen ist. Links neues Agenten-Wallet gibt Agenten Zahlungsfähigkeit, ohne Kartendaten offenzulegen; jeder Kauf braucht Nutzerfreigabe.

### Tempo: eine Blockchain nur für Zahlungen

Tempo wird von Stripe und Paradigm inkubiert; CTO ist Georgios Konstantopoulos, zuvor langjähriger Ethereum-Architekt bei Paradigm. Seine Motivation speist sich aus der griechischen Finanzkrise, sein Befund: Die Agenten-Welle wird bestehende Zahlungsinfrastruktur überrollen. Nutzer der Kette sind unter anderem DoorDash (globale Dasher-Auszahlungen), Klarna (eigener Stablecoin «Klarna USD») und Visa; Validatoren betreiben neben Stripe auch Visa und Standard Chartered. Als nächstes Grossthema nennt Konstantopoulos Privacy: Stablecoins im Klartext zu nutzen hält er für untragbar.

### Der Stack darunter

Drei Zukäufe beziehungsweise Beteiligungen bilden Stripes Stablecoin-Fundament: Bridge orchestriert grenzüberschreitende Stablecoin-Bewegungen, Privy liefert Wallets als API, Tempo die Settlement-Schicht. Privys «digital asset accounts» bündeln Zahlungen über Token und Chains, Fiat-On/Off-Ramps, On-Chain-FX, Yield und Custody in einer API. Darauf laufen Ramp, Deel, DoorDash sowie Startups wie Hyperliquid und Chipper Cash.

Die Reichweite ist der eigentliche Punkt:

- Link, Stripes Konsumenten-Netzwerk mit 250 Millionen Nutzern, kann jetzt Stablecoins halten. Firmen zahlen damit an Konsumenten aus, ohne dass diese ein Krypto-Wallet verstehen müssen; Meta nutzt das für Creator-Auszahlungen auf den Philippinen und in Kolumbien.
- Das neue Stripe Treasury führt Dollar, Pfund, Euro und Stablecoins nebeneinander in einem Konto, mit Währungsumtausch auch am Wochenende. Live in 119 Ländern, Stablecoin-Rails in 100, geplant 160 bis Jahresende.
- Das Startup Félix wickelt Überweisungen per WhatsApp ab und trägt dank Stablecoins über 5% des US-Mexiko-Korridors, des grössten Remittance-Korridors der Welt.

### Einordnung aus Bitcoin-Sicht

Die Keynote bestätigt zwei Muster, die in der Knowledge Base wiederkehren. Erstens: Die Nachfrage nach global sofort beweglichem, programmierbarem Geld ist real und gross; Stripe belegt sie mit Zahlen statt Ideologie («not crypto for crypto's sake»). Zweitens: Stablecoins lösen das Bewegungsproblem des Fiat-Geldes, nicht sein Entwertungsproblem. Klarna USD und FDIC-versicherte Treasury-Konten bleiben Dollar-Forderungen mit Emittenten-, Zensur- und Inflationsrisiko, siehe [[geld-staat-und-fiat-monopol]] und [[cbdc-und-digitaler-yuan]] für die Kontrollseite solcher Rails.

Interessant ist die Konvergenz der Probleme: Konstantopoulos benennt Privacy als dringendste Baustelle, dieselbe Debatte führt die Bitcoin-Welt seit Jahren ([[coinjoin-und-on-chain-privatsphaere]], [[silent-payments]]). Und Streaming-Micropayments im Subcent-Bereich sind exakt der Anwendungsfall, für den Lightning konzipiert wurde ([[lightning-netzwerk-grundlagen]], [[skalierung-lightning-ark-statechains]]). Die offene Frage ist, ob zensurresistente Rails gegen die Distributionsmacht eines Zahlungsdienstleisters mit Millionen Händlern bestehen, oder ob sie ein Nischenprodukt für die Fälle bleiben, in denen Neutralität zwingend ist.

## Related

- [[bitcoin-vs-krypto]]
- [[cbdc-und-digitaler-yuan]]
- [[geld-staat-und-fiat-monopol]]
- [[lightning-netzwerk-grundlagen]]
- [[bitcoin-skalierung-und-zahlungen]]
- [[bitcoin-und-ki]]

## Open Questions

- Tempo ist permissioned-nah aufgebaut (Validatoren: Stripe, Visa, Standard Chartered). Wie unterscheidet sich das Vertrauensmodell konkret von einer Datenbank mit mehreren Schreibern?
- Frisst Stablecoin-Adoption Bitcoins Medium-of-Exchange-Anwendungsfall in Schwellenländern (Félix, Meta-Payouts), oder dient sie als Einstiegsrampe?
- Kann Lightning technisch mit Tempo-Streaming-Payments mithalten (Latenz, Kosten, Entwickler-Ergonomie)?
