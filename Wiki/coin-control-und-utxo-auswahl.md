# Coin Control und UTXO-Auswahl

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[sparrow-wallet]], [[electrum-wallet]], [[utxo-modell-und-konsolidierung]], [[coinjoin-und-on-chain-privatsphaere]]

## Summary

Coin Control bezeichnet die manuelle Auswahl von UTXOs beim Erstellen einer Transaktion. Statt der Wallet zu überlassen, welche Coins verwendet werden, entscheidet der Nutzer selbst. Das ist keine erweiterte Komfortfunktion, sondern ein Datenschutzwerkzeug: Wer Coins mit unterschiedlicher Herkunft in eine Transaktion mischt, verknüpft deren Historien unwiderruflich.

## Body

### Warum UTXO-Auswahl wichtig ist

Jede Bitcoin-Wallet verwaltet intern eine Liste unverbrauchter Outputs (UTXOs) — nicht einen einzigen Kontostand. Wenn eine Transaktion erstellt wird, müssen eine oder mehrere UTXOs als Input gewählt werden. Welche das sind, ist öffentlich auf der Blockchain sichtbar.

Zwei UTXOs, die in derselben Transaktion als Input erscheinen, signalisieren einem Beobachter: Diese Coins gehören wahrscheinlich demselben Besitzer. Das ist die **Common Input Ownership Heuristic** — die grundlegendste Kettenanalyse-Methode. Coin Control unterläuft diese Heuristik, indem Coins unterschiedlicher Herkunft nie zusammen ausgegeben werden.

### Typische Anwendungsfälle

Coins von einer Exchange (KYC, mit Identitätsbindung) und Coins aus privatem Kauf oder Mining sollten nicht in derselben Transaktion auftauchen. Coin Control verhindert die automatische Vermischung.

Vor einem CoinJoin ist gezieltes Einfrieren von UTXOs sinnvoll — nur die für CoinJoin vorgesehenen Coins werden verwendet, der Rest bleibt unangetastet.

Wer viele kleine UTXOs aus DCA-Käufen akkumuliert hat, kann sie gezielt konsolidieren, wenn die Mempool-Gebühren niedrig sind — ohne dabei UTXOs aus sensiblen Quellen einzubeziehen.

### Umsetzung in gängigen Wallets

**Sparrow Wallet** zeigt alle UTXOs der Wallet direkt an. Beim Erstellen einer Transaktion bietet Sparrow mehrere Coin-Selection-Algorithmen (Branch-and-Bound für minimale Gebühren, manuelle Auswahl). UTXOs können mit Labels versehen werden — eine einmal vergebene Label-Information bleibt auch nach mehreren Ausgaben erhalten. [[sparrow-wallet]]

**Electrum** zeigt UTXOs über „Ansicht → Coins anzeigen". Per Kontextmenü kann ein UTXO direkt ausgegeben oder eingefroren werden. Eingefrorene UTXOs werden bei automatischer Coin-Auswahl ignoriert. [[electrum-wallet]]

**BitBoxApp** bietet Coin Control unter den erweiterten Einstellungen des jeweiligen Kontos. Dort sind alle UTXOs gelistet; einzelne können manuell für die nächste Transaktion ausgewählt werden. Nützlich für gezielte Konsolidierung ohne Privatsphäre-Kompromisse. [[utxo-modell-und-konsolidierung]]

### Verhältnis zu Labels

Coin Control funktioniert besser mit konsequentem UTXO-Labeling. Ohne Labels — wer diesen UTXO mir geschickt hat, aus welchem Kontext er stammt — ist manuelle Auswahl blind. Mit Labels lässt sich gezielt entscheiden. BIP-329 standardisiert Wallet-Labels, sodass sie zwischen Wallets portierbar sind. [[bip-0329]]

### Verhältnis zu CoinJoin

CoinJoin verbessert Privatsphäre durch Vermischung mehrerer Nutzer in einer Transaktion. Coin Control ist eine Vorbereitung dafür: Nur die UTXOs, die in CoinJoin sollen, werden nicht eingefroren. Die anderen bleiben unangetastet. Ohne Coin Control riskiert man, in einem CoinJoin Coins zu verwenden, die man lieber getrennt halten wollte. [[coinjoin-und-on-chain-privatsphaere]]

## Related

- [[utxo-modell-und-konsolidierung]]
- [[coinjoin-und-on-chain-privatsphaere]]
- [[sparrow-wallet]]
- [[bip-0329]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Wie verhält sich automatische Coin-Selection (Branch-and-Bound, FIFO) gegenüber Datenschutz-Heuristiken im Vergleich zu echter manueller Auswahl?
- Gibt es standardisierte UTXO-Freezing-Formate, die zwischen Wallets portierbar wären?
