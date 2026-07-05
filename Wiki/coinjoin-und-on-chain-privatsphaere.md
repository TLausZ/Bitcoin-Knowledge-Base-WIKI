# CoinJoin und On-Chain-Privatsphäre

**Status:** established
**Last updated:** 2026-06-25 (Pass 53: CoinJoin-Rechtslage + Lightning/Liquid-Swaps)
**Sources:** [[20240508_was-ist-eigentlich-ein-coinjoin]], [[20240606_payment-codes-bitcoin-adressen-privat-austauschen]], [[sparrowwallet-Spending Privately]], [[Das Privacy Handbuch_ Ein Ratgeber für digitale Sicherheit und Privatsphäre]], [[alex-waltz-joinmarket]]

## Summary

Bitcoin ist nicht anonym — alle Transaktionen sind öffentlich und dauerhaft einsehbar. Wenn Adressen einmal mit einer Identität verknüpft sind, können alle damit verbundenen Transaktionen rückverfolgt werden. CoinJoin ist eine Technik, bei der mehrere Nutzer ihre Bitcoin gemeinsam in einer Transaktion mit gleichen Output-Beträgen ausgeben — dadurch kann nicht mehr zugeordnet werden, welcher Input zu welchem Output gehört.

## Body

### Warum Bitcoin keine Privatsphäre garantiert

Mehrere technische Eigenschaften von Bitcoin verschlechtern die Privatsphäre:

- **Verknüpfte Inputs:** Wenn mehrere Inputs in einer Transaktion zusammengefasst werden, werden die zugehörigen Adressen miteinander verknüpft
- **Wechselgeld-Outputs:** Das Wechselgeld einer Transaktion verbindet frühere und spätere Transaktionen
- **Adress-Wiederverwendung:** Erlaubt es, alle Zahlungen an eine Person zu verfolgen

Selbst bei konsequenter Nutzung neuer Empfangsadressen (wie in der BitBoxApp) können UTXOs durch spätere gemeinsame Ausgabe miteinander verknüpft werden.

### Wie CoinJoin funktioniert

Mehrere Nutzer kombinieren ihre Inputs in einer einzigen Transaktion. Das entscheidende Element: **Alle Outputs haben denselben Betrag** — z.B. je 0,1 BTC. Dadurch ist es unmöglich zu bestimmen, welcher Input zu welchem Output gehört.

**Beispiel:** Alice (0,12 BTC) und Bob (0,13 BTC) machen einen CoinJoin. Beide erhalten einen Output von 0,1 BTC. Das restliche Wechselgeld (0,02 BTC und 0,03 BTC) bleibt zuordenbar — diese werden als **„Doxxic Change"** bezeichnet.

In der Praxis nehmen hunderte oder tausende Nutzer gleichzeitig teil. Die Privatsphäre wächst mit der Teilnehmerzahl exponentiell.

### Vertrauenslos, aber koordiniert

Anders als bei zentralisierten Mixing-Diensten behalten Nutzer beim CoinJoin die Kontrolle über ihre Schlüssel. Ein Koordinierungsservice (früher: Samourai Whirlpool, Wasabi Wallet) tauscht nur Nachrichten aus — er kann die Coins nicht stehlen. Das macht CoinJoin vertrauenslos.

### Stonewall: Fake Coinjoin ohne Koordinator

Sparrow Wallet implementiert «Stonewall» — eine Transaktion, die ein Nutzer allein erstellt, aber extern wie ein Zwei-Personen-Coinjoin aussieht. Für Beobachter von aussen gibt es keine Möglichkeit, festzustellen, ob es sich um einen echten oder einen Fake-Coinjoin handelt. Voraussetzung: Das Wallet muss mehr als doppelt so viel Saldo haben wie der Zahlbetrag (um zwei Input-Sets zu simulieren). Stonewall funktioniert mit Hardware-Wallets und benötigt keinen Koordinierungsserver — daher 2024 weiterhin vollständig nutzbar. [[sparrowwallet-Spending Privately]]

### Aktuelle Lage (2024)

Im April 2024 wurden Samourai Whirlpool beschlagnahmt und die Gründer verhaftet. zkSNACKs stellte den Wasabi Wallet CoinJoin-Koordinierungsservice ein. Beide Implementierungen sind Open-Source und könnten weitergenutzt werden. Alternative: **JoinMarket** (dezentral, kein zentraler Koordinator).

### CoinJoin und rechtliche Risiken (Stand 2024)

Im April 2024 wurden die Samourai-Wallet-Gründer in den USA verhaftet — Vorwurf: nicht lizenziertes Geldtransfergeschäft und Beihilfe zur Geldwäsche. Kurz darauf schloss zkSNACKs den Wasabi-Wallet-Koordinierungsservice und blockierte US-Nutzer. Wasabi wurde später vom Gründer vollständig eingestellt.

CoinJoin selbst ist nicht illegal. Aber zentrale Koordinierungsserver können als Geldtransmitter eingestuft werden — und deren Betreiber haftbar gemacht werden. Wer CoinJoin nutzt, sollte wissen, dass manche Börsen oder Dienste Wallets mit CoinJoin-Vorgeschichte ablehnen oder markieren.

JoinMarket bleibt als dezentrale Alternative ohne zentralen Koordinator verfügbar, erfordert aber mehr technisches Know-how. Mehr Details: [[joinmarket]].

### JoinMarket: Maker/Taker und Fidelity Bonds

JoinMarket löst das Koordinationsproblem über ein Marktmodell. **Maker** stellen Liquidität bereit, inserieren im Order Book und kassieren eine Gebühr fürs Warten. **Taker** zahlen die Gebühr und joinen sofort. Das Ergebnis ist ein System, das immer Liquidität bereitstellt, weil jemand dafür bezahlt wird zu warten.

Gegen Sybil-Angriffe (ein Angreifer füllt den Markt mit Fake-Makers) schützen **Fidelity Bonds**: Maker können Bitcoin on-chain per Timelock sperren und diesen Bond neben dem CoinJoin-Angebot annoncieren. Die Sperre ist trustless (Coins bleiben beim Maker), aber die verlorene Liquidität der Zeit ist ein echter Opferpreis. Taker bevorzugen Maker mit Fidelity Bond — womit der Angriff exponentiell teurer wird, je mehr Fake-Slots ein Angreifer kaufen will. Das Konzept wurde 2013 von Peter Todd entwickelt.

### Lightning- und Liquid-Swaps als Alternative zu CoinJoin

Wer die rechtlichen Risiken von CoinJoin vermeiden will, kann stattdessen Swaps zwischen Netzwerken nutzen: On-Chain-Bitcoin werden ins Lightning Network oder das Liquid Network übertragen, dort weiterbewegt und zurückgetauscht. Der Transaktionsfluss ist für Außenstehende damit nicht mehr nachvollziehbar — ohne dass der Vorgang wie ein CoinJoin aussieht.

**Boltz** ([boltz.exchange](https://boltz.exchange)) — non-kustodialer Dienst für Swaps zwischen Lightning, Liquid und Bitcoin-Mainchain. Unterstützt private, schnelle Atomic Swaps.

**FixedFloat** ([ff.io](https://ff.io)) — Instant-Tauschdienst für Lightning- und On-Chain-Swaps mit einfacher Benutzeroberfläche.

**Aqua Wallet** (App) — non-custodial Wallet speziell für das Liquid Network, unterstützt Liquid-Bitcoin und Lightning.

Das Lightning Network bietet strukturelle Privatsphäre: Transaktionen werden über mehrere Nodes geroutet (ähnlich Tor — Onion Routing), einzelne Zahlungsbeträge sind für Außenstehende nicht sichtbar, und abgeschlossene Kanäle hinterlassen keine dauerhaften Aufzeichnungen der einzelnen Zahlungen.

Liquid bietet zusätzlich *Confidential Transactions* — der Betrag ist verschlüsselt und nur für die beiden Transaktionspartner sichtbar.

### Privatsphäre nach einem CoinJoin

Nach einem CoinJoin sollte man die Coin Selection (welche UTXOs für eine Transaktion verwendet werden) weiterhin im Auge behalten. Das Mischen von CoinJoin-Outputs mit unvermischten UTXOs hebt die gewonnene Privatsphäre auf.

## Related

- [[coin-control-und-utxo-auswahl]]
- [[silent-payments]]
- [[payment-codes-und-adressaustausch]]
- [[opsec-und-privatsphaere]]

## Open Questions

- Wie entwickeln sich dezentrale CoinJoin-Protokolle (JoinMarket) nach den Verhaftungen 2024?
- Welche Rolle spielen Silent Payments und Taproot für zukünftige Privatsphäre-Verbesserungen?
