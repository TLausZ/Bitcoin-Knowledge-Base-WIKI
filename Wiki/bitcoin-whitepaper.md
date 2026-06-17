# Bitcoin Whitepaper

**Status:** established
**Last updated:** 2026-06-05
**Sources:** [[20081031_bitcoin-whitepaper]]

## Summary

Satoshi Nakamotos neun Seiten von Oktober 2008 definierten ein elektronisches Peer-to-Peer-Zahlungssystem ohne vertrauenswürdige Drittpartei. Das Kernproblem — Double-Spending ohne zentrale Autorität zu verhindern — löst Nakamoto mit einem dezentralen Timestamp-Server, der Transaktionen durch Proof-of-Work in einer unveränderlichen Kette verankert. Das Whitepaper beschreibt UTXO-basierte Transaktionen, den Incentive-Mechanismus für Miner, Simplified Payment Verification (SPV) und ein pseudonymes Privatsphäre-Modell.

## Body

### Das Problem: Double-Spending ohne Trusted Third Party

Online-Zahlungen erforderten bislang Finanzinstitute als Vermittler. Das schafft Rückbuchungsrisiken, Transaktionskosten und Abhängigkeiten. Das Kernproblem der digitalen Währung ist Double-Spending: Eine digitale Münze kann theoretisch kopiert und zweimal ausgegeben werden. Der traditionelle Lösungsweg — eine zentrale Mint, die jede Transaktion prüft — überträgt das Schicksal des gesamten Geldsystems auf eine einzige Instanz.

### Die Lösung: Dezentraler Timestamp-Server

Nakamoto schlägt einen Peer-to-Peer-Timestamp-Server vor. Transaktionen werden öffentlich verbreitet. Nodes sammeln Transaktionen in Blöcken, suchen per Proof-of-Work nach einem gültigen Hash, und verbreiten den fertigen Block. Der längste Chain — die meiste investierte CPU-Arbeit — gilt als die korrekte Geschichte.

**Proof-of-Work:** Nodes suchen eine Nonce, sodass der SHA-256-Hash des Blocks mit einer bestimmten Anzahl Nullbits beginnt. Die Schwierigkeit passt sich alle 2016 Blöcke an, um ~10 Minuten pro Block zu halten. Ein Angreifer müsste mehr CPU-Power als alle ehrlichen Nodes zusammen aufbringen — und das schnell genug, um aufzuholen.

### Transaktionen und das UTXO-Modell

Eine elektronische Münze ist eine Kette digitaler Signaturen. Jeder Eigentümer überträgt die Münze, indem er den Hash der vorherigen Transaktion und den öffentlichen Schlüssel des nächsten Eigentümers signiert. Das Netzwerk prüft, ob die Inputs tatsächlich unausgegeben sind.

Transaktionen können mehrere Inputs (frühere UTXOs) und mehrere Outputs (neue UTXOs, inkl. Wechselgeld) haben.

### Incentive-Mechanismus

Der erste Block-Reward — eine neu geschaffene Münze für den Block-Ersteller — ist die initiale Verteilung ohne zentrale Behörde. Das Modell entspricht Gold-Mining: CPU-Zeit und Strom werden gegen neue Coins getauscht. Langfristig kann die Block-Subsidy vollständig durch Transaktionsgebühren ersetzt werden — was Bitcoin deflationär und inflationsfrei macht.

Der Incentive hält Miner ehrlich: Ein Angreifer mit Mehrheits-CPU-Power würde mehr durch ehrliches Mining verdienen als durch einen Angriff, der das Vertrauen — und damit den Wert seiner eigenen Coins — zerstört.

### Simplified Payment Verification (SPV)

Nutzer ohne Full-Node können Zahlungen verifizieren, indem sie nur Block-Header der längsten Chain halten und den Merkle-Ast zur eigenen Transaktion abfragen. Dies ist sicher, solange ehrliche Nodes das Netzwerk kontrollieren — aber SPV-Clients sind anfälliger gegen Angriffe als Full-Nodes.

### Privatsphäre

Das traditionelle Banking-Modell schützt Privatsphäre durch Zugangsbeschränkung. Bitcoin veröffentlicht alle Transaktionen, schützt Privatsphäre aber durch Pseudonymität: Öffentliche Schlüssel haben keinen Eigentümer-Identifier. Nakamoto empfiehlt, für jede Transaktion ein neues Schlüsselpaar zu verwenden, um Verknüpfungen zu vermeiden.

### Historische Bedeutung

Das Whitepaper wurde am 31. Oktober 2008 — mitten in der Finanzkrise — auf einer Kryptografie-Mailingliste veröffentlicht. Die Genesis Block-Coinbase enthielt den Zeitungsheadline "Chancellor on brink of second bailout for banks" als Timestamp und politisches Statement. Satoshi Nakamoto verschwand 2010 aus der Öffentlichkeit; die Identität ist bis heute unbekannt.

## Related

- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-mining-und-proof-of-work]]
- [[utxo-modell-und-konsolidierung]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[segregated-witness-segwit]]

## Open Questions

- Wie lange bleibt das 51%-Angriffs-Modell mit sinkendem Block-Reward sicher, wenn Mining-Pools sich konzentrieren?
- Inwiefern deckt SPV in der Praxis noch die Sicherheitsannahmen des Whitepapers ab?
