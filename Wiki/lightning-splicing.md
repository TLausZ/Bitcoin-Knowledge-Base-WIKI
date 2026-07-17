# Lightning Splicing

**Status:** established
**Themen:** lightning, wallets
**Last updated:** 2026-06-09
**Sources:** [[Splices and Liquidity in the Lightning Network]], [[Rebalancing in the Lightning Network_ Circular Payments, Fee Management and Splices]], [[How Splices Impact Lightning Network Fees.md]], [[phoenix-wallet-lightning]]

## Summary

Splicing ist eine Lightning-Network-Technik, die es erlaubt, die Kapazität eines bestehenden Channels on-chain zu erhöhen (Splice-In) oder zu verringern (Splice-Out), ohne den Channel zu schliessen. Im Gegensatz zu Circular Payments und Fee Management — die nur Kapazität umverteilen — kann Splicing die absolute Kapazität des Netzwerks verändern. Es löst das Liquiditätsproblem von Lightning grundlegend: Funds sind nicht mehr "eingesperrt", sondern flexibel nutzbar.

## Body

### Das Liquiditätsproblem vor Splicing

Im klassischen Lightning-Modell gilt: Funds in einem Channel können nicht ausserhalb genutzt werden. Will man Funds aus einem Channel abziehen, muss man den Channel schliessen — mit on-chain Transaktion, Bestätigungszeit und Gebühren. Das führte zur Wahrnehmung, Lightning "sperre" Geld ein.

Splicing ändert das fundamental: Eine Splice-Transaktion modifiziert die Channel-Kapazität on-chain, während der Channel offen bleibt und weiter Payments routen kann.

### Splice-In und Splice-Out

**Splice-In**: On-Chain Bitcoin wird in einen bestehenden Channel hinzugefügt. Die Channel-Kapazität steigt. Nützlich für: Nachfüllen eines depleted Channels, Empfangen einer grossen On-Chain-Zahlung ohne neuen Channel.

**Splice-Out**: Bitcoin wird aus einem bestehenden Channel on-chain ausgezahlt. Die Channel-Kapazität sinkt. Nützlich für: On-Chain-Ausgabe ohne Channel-Close, Rebalancing.

Beide Operationen erfordern eine on-chain Transaktion (Splice-Transaktion), die Confirmation braucht. Während der Bestätigungszeit kann der Channel bereits weiter genutzt werden. Das ist der Kern des Atomic Splice.

### Splicing vs. andere Rebalancing-Strategien

| Methode | Kapazität des Netzwerks | Funktioniert bei wenig Liquidität |
|---------|------------------------|----------------------------------|
| Circular Payments | unverändert | nein |
| Fee Management | unverändert | nein |
| Splices | ändert sich | ja |

Circular Payments und Fee Management verteilen vorhandene Kapazität um. Splicing bringt neue Kapazität ins Netzwerk (Splice-In) oder entzieht sie (Splice-Out). Das macht Splicing bei schlecht vernetzen oder unterfinanzierten Netzwerken zum einzigen funktionierenden Rebalancing-Tool.

### Kosten: Operational vs. Financial

Routing Nodes haben zwei Kostentypen:

**Operational Costs**: Kosten für das Öffnen und Schliessen von Channels (on-chain Gebühren). Je häufiger gesplict wird, desto höher die operationalen Kosten. Optimum: Splice so selten wie möglich.

**Financial Costs**: Kosten für das Eingesperrtsein von Kapital in einem Channel (Opportunitätskosten). Je mehr Kapital im Channel, desto höher die Financial Costs. Optimum: Nur so viel Kapital wie nötig im Channel halten.

Diese beiden Ziele stehen in Spannung: Wenig Splicing = hohe Financial Costs (zu viel Kapital gebunden). Viel Splicing = hohe Operational Costs. Nodes optimieren über Fee-Einnahmen — Fees müssen beide Kostentypen decken.

### Splicing in der Praxis: Phoenix

Phoenix Wallet (ACINQ) nutzt Splicing als primären Mechanismus für Liquiditätsmanagement. Wenn eine eingehende Lightning-Zahlung die verfügbare Inbound Liquidity übersteigt, splicet Phoenix automatisch in den bestehenden Channel hinein — statt einen neuen Channel zu öffnen. Das ist effizienter (ein UTXO statt zwei) und günstiger. Phoenix nennt das "Splice-In bei unzureichender Liquidität" und berechnet dafür 1% + Mining-Gebühr.

### Technische Voraussetzung

Splicing benötigt SegWit (Segregated Witness), weil es Transaction Malleability verhindert. Ohne SegWit könnten Splice-Transaktionen durch Malleability-Angriffe ungültig werden. Taproot verbessert Splicing weiter durch Schnorr-Signaturen und effizientere Multi-Party-Koordination.

## Related

- [[lightning-rebalancing]]
- [[phoenix-wallet-lightning]]
- [[skalierung-lightning-ark-statechains]]
- [[segregated-witness-segwit]]
- [[taproot-musig2-frost]]
- [[transaktionsgebuehren-und-mempool]]

## Open Questions

- Wann wird Splicing im gesamten Lightning-Netzwerk zum Standard — welche Implementierungen unterstützen es schon?
- Wie verhält sich Splicing bei hohen on-chain Gebühren — wird es dann unökonomisch?
- Kann Splicing zusammen mit Channel Factories kombiniert werden, um die on-chain Footprint weiter zu reduzieren?
