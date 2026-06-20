# WalletConnect und DApps

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[20240118_mithilfe-von-walletconnect-die-bitboxapp-mit-einer-dapp-verbinden]]

## Summary

WalletConnect ist ein offenes Protokoll, das Browser-basierte dezentrale Anwendungen (DApps) mit Wallets verbindet — per QR-Code oder URI-Scan. Für BitBox02-Nutzer bedeutet das: DApp im Browser, Signierung auf der BitBox02. Die Transaktion verlässt die DApp nie unbestätigt; die Hardware-Wallet verifiziert jeden Schritt.

## Body

### Was WalletConnect ist

WalletConnect leitet Signieranfragen von einer DApp an eine Wallet weiter. Verbindungsaufbau: Die DApp zeigt einen QR-Code; die Wallet scannt ihn oder nimmt die URI entgegen. Nach dem Pairing werden Transaktionsanfragen der DApp direkt in der Wallet-App angezeigt — zur Bestätigung auf dem Hardware-Wallet-Gerät.

Das Protokoll ist plattformübergreifend: Eine mobile App kann sich mit einer Desktop-DApp verbinden.

Ohne WalletConnect war die Nutzung von DApps mit der BitBox02 nur über die Rabby-Browsererweiterung möglich — eine Desktop-only-Lösung. WalletConnect öffnet denselben Workflow für Desktop und Android.

### Verbindungsaufbau (Schritt für Schritt)

1. DApp im Browser öffnen → „Connect" → „WalletConnect" auswählen
2. QR-Code erscheint in der DApp
3. In der BitBoxApp: Ethereum-Konto aufrufen → „WalletConnect" antippen
4. QR-Code scannen oder URI einfügen
5. Verbindung in der BitBoxApp bestätigen

Sobald verbunden, läuft die DApp normal. Wenn eine Transaktion Signierung erfordert, öffnet WalletConnect einen Dialog in der BitBoxApp. Die Transaktionsdetails erscheinen auf der BitBox02 — dort wird bestätigt oder abgelehnt.

### Einschränkungen

WalletConnect in der BitBoxApp unterstützt aktuell nur **Ethereum Mainnet**. Für andere EVM-Netzwerke (Polygon, Arbitrum, BSC usw.) bleibt die Rabby-Browsererweiterung die geeignete Lösung.

Das Feature ist ausschließlich für die **BitBox02 Multi Edition** verfügbar — nicht für die Bitcoin-only Edition. Bitcoin-Transaktionen werden über Lightning oder on-chain abgewickelt, nicht über DApps.

### Sicherheitshinweis

Smart-Contract-Interaktionen können zu dauerhaftem Verlust von Coins führen, wenn der Vertrag Fehler enthält oder die DApp betrügerisch ist. WalletConnect selbst schützt vor Man-in-the-Middle-Angriffen auf die Signing-Anfrage — es kann aber nicht beurteilen, ob eine DApp legitim ist. Nutzung setzt voraus, dass man versteht, was der Smart Contract tut.

## Related

- [[kryptografische-schlussel-und-adressen]]
- [[selbstverwahrung-und-boersenrisiken]]

## Open Questions

- Wann kommt WalletConnect-Support für andere EVM-Netzwerke in der BitBoxApp?
- Gibt es eine Bitcoin-native DApp-Interaktion (z.B. über Taproot-Verträge oder Ordinals), die vergleichbaren Komfort bieten würde?
