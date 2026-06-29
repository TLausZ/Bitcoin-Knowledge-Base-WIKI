# JoinMarket

**Status:** established
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-joinmarket]]

## Summary

JoinMarket ist eine dezentrale, nicht-verwahrerische CoinJoin-Implementierung. Im Gegensatz zu Samourai Whirlpool oder Wasabi gibt es keinen zentralen Koordinator — stattdessen löst ein Markt das Koordinationsproblem: Wer warten kann, bietet Liquidität an (Maker) und kassiert eine Gebühr; wer sofort mixen will, zahlt sie (Taker).

## Body

### Warum CoinJoin eine Koordination braucht

Mehrere Parteien müssen zur gleichen Zeit, am gleichen Ort, mit dem gleichen Betrag bereit sein. Frühere CoinJoin-Projekte scheiterten genau daran: Sie benötigten einen zentralen Koordinator und erzwangen Wartezeiten. JoinMarket löste das 2013, als Chris Belcher das Maker/Taker-Modell vorschlug.

### Wie das Maker/Taker-Modell funktioniert

**Maker** annoncieren öffentlich, dass sie X Bitcoin zum CoinJoin bereitstellen und verlangen dafür eine Gebühr. Sie warten im Order Book. **Taker** kommen, zahlen die Gebühr und CoinJoinen sofort.

Das Ergebnis: Es gibt immer genug Liquidität, weil ehrliche Maker dafür bezahlt werden zu warten. In der Praxis übersteigt das Angebot die Nachfrage deutlich. Maker-Gebühren sind minimal (\<1 %), manche Taker zahlen nur die Mining-Gebühren.

### Technische Basis: Warum es funktioniert

Drei Eigenschaften von Bitcoin-Transaktionen machen trustloses CoinJoin möglich:

Inputs können von verschiedenen Parteien stammen — es gibt keine erzwungene Verknüpfung zwischen Input-Eigentümer und Transaktion. Außerdem sind Bitcoin-Transaktionen atomar: Alle Signaturen müssen gültig sein, sonst ist die TX ungültig. Weil jeder Input die gesamte TX mitunterzeichnet, sind die Outputs damit „eingefroren" — niemand kann sie heimlich ändern. Und da Satoshis auf Protokollebene fungibel sind (UTXOs hingegen nicht), lässt sich durch gleiche Output-Beträge die Zuordnung effektiv verschleiern.

### Fidelity Bonds: Sybil-Schutz ohne Identität

Das offensichtliche Problem bei einem anonymen, dezentralen System: Ein Angreifer kann die meisten Maker-Slots mit Scheinaccounts füllen und so den CoinJoin deanonymisieren. Die Lösung stammt von Peter Todd (2013) und basiert auf dem Zeitwert von Geld.

Ein Maker kann Bitcoins zeitgesperrt hinterlegen — nicht an einen Dritten, sondern on-chain via Timelocks. Die Coins bleiben in seinem Besitz, aber sie sind für die Laufzeit unbrauchbar. Da Geld heute mehr wert ist als Geld morgen, ist das eine verifiable Opferung. Ein Angreifer müsste diesen Opfer-Betrag für alle gefakten Maker-Slots multipliziert aufbringen — was exponentiell teurer wird. Taker sehen im Order Book, welche Maker einen Fidelity Bond haben, und bevorzugen sie.

Die Formel berücksichtigt sowohl Betrag als auch Laufzeit, sodass kleine Bonds über lange Zeit und große Bonds kurzer Zeit vergleichbar sind. Bonds verlieren nach Ablauf an Wert, was ehrliche Maker dazu anhält, kontinuierlich neue Bonds zu hinterlegen statt zu splitten.

### JAM: Benutzeroberfläche

JoinMarket ist technisch anspruchsvoll, aber die JAM-Weboberfläche (jam.app) macht es zugänglich — ein Browser-UI, das auf einem eigenen Node läuft. JAM ist auf RaspiBlitz, Umbrel, Citadel, MYNODE und RaspiBolt verfügbar.

### Grenzen

CoinJoin löst kein Problem vollständig: Wer CoinJoin-Outputs mit nicht-gemixten UTXOs zusammenführt, hebt den Datenschutzgewinn auf. Coin Control danach ist ebenso wichtig wie der CoinJoin selbst. Maker müssen ihre Coins in einer Hot Wallet halten, was ein Kompromiss ist.

## Related

- [[coinjoin-und-on-chain-privatsphaere]]
- [[coin-control-und-utxo-auswahl]]
- [[utxo-modell-und-konsolidierung]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Wie entwickelt sich JoinMarket nach den Strafverfolgungen gegen Samourai/Wasabi — mehr Adoption?
- Können Fidelity Bonds das Sybil-Problem vollständig lösen oder nur verteuern?
