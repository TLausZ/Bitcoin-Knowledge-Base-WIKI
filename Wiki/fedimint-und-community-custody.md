# Fedimint und Community Custody

**Status:** emerging
**Themen:** protokoll, lightning, philosophie
**Last updated:** 2026-06-23
**Sources:** [[aprycot-fedimints-gladstein]], [[digitales-bargeld-und-ecash]]

## Summary

Fedimint ist ein Open-Source-Protokoll, das föderierte chaumische Münzanstalten auf Bitcoin und Lightning ermöglicht. Entwickelt von Eric Sirion, verfolgt es einen dritten Weg zwischen Selbstverwahrung (Hardware-Wallet) und zentralisierter Verwahrung (Börse): eine Gruppe von Hütern — vertraute Personen in der Gemeinschaft — kontrolliert die Gelder gemeinsam per Multisig, während Blindsignaturen sicherstellen, dass die Hüter nicht sehen können, wer innerhalb des Systems Transaktionen durchführt.

## Body

### Das Verwahrungsproblem bei globaler Bitcoin-Adoption

Obi Nwosu, ehemaliger Betreiber der britischen Bitcoin-Börse Coinfloor, sieht Verwahrung als die dritte ungelöste Säule von Bitcoin — neben Geld (Bitcoin-Basisschicht) und Zahlungen (Lightning). Sein Kernargument: Milliarden von Menschen in Schwellenländern werden weder Zugang zu Hardware-Wallets noch zu regulierten Börsen haben. Bei Bitnob, einer Nigeria-fokussierten Bitcoin-App, lösen 80–90% der Nutzer ihre Bitcoin nie aus der verwalteten Umgebung ein. Globale Hyperbitcoinisierung setzt voraus, dass diese Menschen Bitcoin wirklich halten können — nicht nur Ansprüche auf Bitcoin.

In Nigeria werden schätzungsweise 80% aller Finanzdienstleistungen über Gemeinschaftsmechanismen abgewickelt: Tontinen (Côte d'Ivoire), Ekub (Sudan), Sou-Sous (Trinidad und Tobago). Nwosu sieht Fedimint als digitale Fortsetzung dieser Tradition.

### Wie Fedimint funktioniert

Chaumische Blindsignaturen sind der kryptografische Kern. Die Bank (hier: die Fedimint-Hüter) signiert Token, ohne zu wissen, welcher spezifische Token signiert wird — vergleichbar mit einem Bankangestellten, der einen versiegelten Umschlag unterschreibt. Das Ergebnis: Die Hüter wissen, dass Gelder in die Münzanstalt eingegangen und herausgegangen sind, aber sie können einzelne Transaktionen nicht nachverfolgen. [[aprycot-fedimints-gladstein]]

Die Hüter bilden eine Föderation mit Konsensregeln: Eine Mehrheit muss jeder Aktion zustimmen. Ein einzelner Hüter kann keine Gelder stehlen oder einfrieren — im Gegensatz zu einer zentralisierten Börse mit einem Single Point of Failure. Die technische Grundlage baut auf Blockstreams Elements-/Liquid-Technologie auf, die Sirion für gemeinschaftliche Zwecke adaptierte.

Für Wiederherstellung können Nutzer ihre Gelder mit einer Seed-Phrase sichern. Als Alternative kann die Fedimint-App ein verschlüsseltes Backup bei den Hütern hinterlegen: Verliert jemand das Telefon, kann ein Quorum der Hüter den Wiederherstellungsprozess einleiten.

### Lightning-Gateway als globales Netzwerk

Innerhalb einer Fedimint laufen Transaktionen über den Software-eigenen Konsens-Algorithmus — sofort und privat. Der eigentliche Hebel liegt im Lightning-Gateway: ein Dienst, der eingehende und ausgehende Lightning-Transaktionen im Namen der Münzanstalt abwickelt. Damit werden alle Fedimints — tausende, möglicherweise millionen — interoperabel mit dem gesamten Lightning-Netzwerk.

In der Praxis zahlt eine Nutzerin BTC in ihr Fedimint ein, erhält E-Cash-Token in gleicher Höhe, und kann damit sowohl intern (privat, keine On-Chain-Gebühren) als auch extern (über das Gateway, mit Lightning-Geschwindigkeit) zahlen. Der Händler bemerkt keinen Unterschied zu einer gewöhnlichen Lightning-Zahlung.

### Second-Party Custody: zwischen Selbstverwahrung und Börse

Matt Odell beschreibt Fedimint als "Signal für Bitcoin": Signal hat Kompromisse (Telefonnummerpflicht, keine eigenen Server), bietet aber Datenschutz für Dutzende Millionen Nutzer, die sonst auf unverschlüsselte Messenger setzen würden. Fedimint macht denselben Kompromiss: weniger Selbstverwahrung als eine Hardware-Wallet, aber massiv besser als Binance oder Coinbase.

Sirion formuliert den Zielmarkt klar: "Wenn Sie Ihre eigene Hardware-Wallet verwenden und Ihren eigenen Lightning-Knoten betreiben, dann sind Fedimints vielleicht nichts für Sie. Der eigentliche Zielmarkt ist die viel grössere Gruppe von Menschen, die vollständig KYC-geprüfte, verwahrte Lösungen verwenden."

### Risiken

Sirion benennt die wesentlichen Gefahren offen. Ein unkontrolliert wachsendes Fedimint könnte wie Mt. Gox zu einem systemischen Risiko werden, wenn zu viel Kapital an einem Punkt konzentriert ist. Die Konsens-Technologie ist komplex; sie verbindet Bitcoin, Lightning und föderierte Konsensmechanismen — ein heikles Zusammenspiel.

Regulatorisch bleibt offen, ob Fedimint-Hüter in westlichen Rechtssystemen als Geldtransporteure gelten und KYC/AML-Pflichten unterliegen. In autoritären Regimen, wo Bitcoin-Nutzung oft schon verboten ist, stellt das kein zusätzliches Risiko dar.

Kritiker wie Muun-Gründer Dario Sneidermanis sehen in grossen Fedimints dieselben Schwachstellen wie bei Börsen: rechtliche Haftung, Sicherheitsrisiken durch konzentrierte Gelder, operative Anforderungen. Ob der Fedimint-Ansatz diese Probleme wirklich löst oder nur verschiebt, wird sich in der Praxis zeigen.

### Stand 2022

Nwosu, Sirion und Justin Moon gründeten Fedi, ein Unternehmen für die erste mobile Fedimint-Wallet. Die Seed-Runde betrug $4,2 Millionen. Unterstützer sind Blockstream und die Human Rights Foundation. Das Open-Source-Repository liegt auf GitHub; Sirion behält eine beratende Rolle bei Fedi und konzentriert sich auf die Protokollentwicklung.

## Related

- [[digitales-bargeld-und-ecash]]
- [[skalierung-lightning-ark-statechains]]
- [[lightning-netzwerk-grundlagen]]
- [[bitcoin-humanitaere-anwendungen]]
- [[multisig-und-kollaborative-verwahrung]]
- [[shamir-secret-sharing]]

## Open Questions

- Wie hat sich Fedimint seit 2022 entwickelt? Gibt es live-Deployments in Schwellenländern?
- Wie verhält sich Fedimint zu Ark (einem anderen Community-Custody-Ansatz, der 2023 angekündigt wurde)?
- Löst Fedimint das UTXO-Knappheitsproblem für Milliarden von Nutzern, oder entstehen neue Zentralisierungsrisiken durch grosse Gateways?
