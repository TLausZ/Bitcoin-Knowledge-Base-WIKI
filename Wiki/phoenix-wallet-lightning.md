# Phoenix Wallet und Lightning Network

**Status:** established
**Themen:** protokoll, self-custody, lightning, wallets
**Last updated:** 2026-06-09
**Sources:** [[2026-06-09_phoenix-wallet-faq]]

## Summary

Phoenix ist eine selbstverwahrendes Lightning-Wallet für iOS und Android, entwickelt von ACINQ (Paris). Im Gegensatz zu custodial Lightning-Wallets betreibt Phoenix einen echten Lightning-Node auf dem Gerät des Nutzers — der Nutzer kontrolliert die privaten Schlüssel. Das Trust-Modell ist jedoch "trust-minimized", nicht trustless: ACINQ kennt Zahlungsempfänger und -beträge und stellt die Liquidität bereit. Phoenix automatisiert die technisch komplexen Aspekte von Lightning (Channel-Management, Liquidität, Splicing) vollständig.

## Body

### Architektur: Echter Node, kein Proxy

Phoenix ist kein Custodial-Wallet und kein Proxy zu einem Server-seitigen Node. Die Wallet betreibt einen vollständigen Lightning-Node auf dem Smartphone. Das unterscheidet Phoenix von Wallets wie Wallet of Satoshi (rein custodial) oder Zeus (Remote-Control zu einem externen Node).

Phoenix verbindet sich ausschliesslich mit dem ACINQ-Node und nutzt dessen Liquidität. Das ist keine technische Einschränkung, sondern eine Designentscheidung: Die Zielgruppe sind technisch weniger erfahrene Nutzer, für die ein Multi-Peer-Setup zu komplex wäre.

Anforderungen: iOS 16+ oder Android 8+. Ein Testnet-Modus existiert nur für Android.

### Trust-Modell: Trust-minimized, nicht trustless

Phoenix ist ehrlich über seine Grenzen:

- ACINQ kennt den **Zahlungsempfänger** und den **Betrag** jeder Zahlung
- Aktuell bietet Phoenix keinen Datenschutzvorteil gegenüber custodial Wallets
- Zukünftige Versionen sollen Trampoline Payments mit Blinded Paths implementieren, die ACINQ den Empfänger verbergen

Was Phoenix dagegen nicht ist: ACINQ kann keine Gelder einfrieren oder stehlen. Der Nutzer hält die privaten Schlüssel. Wenn ACINQ verschwindet, schliesst Phoenix die Channels on-chain und der Nutzer kann den Seed in jede BIP39-Wallet importieren.

Die Channel-Eröffnung bei eingehenden Lightning-Zahlungen erfordert Vertrauen bis zur Bestätigung der Funding-Transaktion. Bei on-chain Deposits ist kein Vertrauen nötig, weil Phoenix die Transaktion direkt finanziert.

### Gebührenstruktur

| Operation | Gebühr |
|-----------|--------|
| Lightning senden | 0,4% + 4 sat |
| Lightning empfangen (ausreichend Liquidität) | kostenlos |
| Lightning empfangen (unzureichend Liquidität) | 1% + Mining-Gebühr |
| Liquidität anfordern | 1% + Mining-Gebühr |
| On-chain empfangen | Mining-Gebühr |
| On-chain senden | Mining-Gebühr (nutzerwählbar) |
| Channel-Eröffnung | 1.000 sat |

Das Mindest-Empfangslimit liegt bei 1.000 sat (0,00001 BTC). Kleinere Beträge werden abgelehnt.

### Inbound Liquidity: Das zentrale Konzept

Inbound Liquidity ist die Kapazität auf der ACINQ-Seite des Channels, die bestimmt, wie viel der Nutzer empfangen kann. Ein Channel mit 5.000 sat Guthaben und 25.000 sat Kapazität bedeutet nicht, dass 20.000 sat empfangen werden können — ein Teil ist durch das Lightning-Protokoll gesperrt (für on-chain Gebühren bei Force-Close und als Channel-Reserve auf ACINQ-Seite).

**Automatisches Management**: Phoenix öffnet oder modifiziert (splicet) Channels automatisch, wenn eingehende Zahlungen die verfügbare Liquidität überschreiten. Dies kostet 1% + Mining-Gebühr.

**Liquiditätsreservierung**: Wenn Phoenix Liquidität schafft, reserviert es diese für ein Jahr — ACINQ beansprucht sie in dieser Zeit nicht zurück. Nach einem Jahr kann ACINQ die ungenutzte Liquidität zurückfordern (ohne den Channel zu schliessen oder das Guthaben zu ändern). Aktive Nutzer erleben kein Problem: Bei regelmässiger Nutzung wird die Reservierung automatisch erneuert. Nutzer können jederzeit manuell zusätzliche Liquidität anfordern.

### Swap-in Wallet: On-chain → Lightning

Phoenix verwaltet eine interne "Swap-in Wallet" für on-chain Zahlungen. Wenn Bitcoin an die Phoenix-Adresse geschickt wird, landen sie zuerst in diesem Swap-in Bereich.

Nach 3 Bestätigungen (ca. 30 Minuten) werden die Mittel automatisch in Lightning getauscht (Swap). Bis dahin zeigt die App den Status:
- **Pending**: Wartet auf 3 Bestätigungen
- **Sleeping**: Bestätigt, aber Swap noch nicht ausgeführt (z.B. Mining-Gebühren zu hoch relativ zum Betrag, oder automatisches Channel-Management deaktiviert)

On-chain Adressen werden aus Privacy-Gründen nach jeder Nutzung rotiert. Alle Adressen sind vom Seed ableitbar und werden bei der Wiederherstellung gefunden.

### Wiederherstellung

Wiederherstellung erfolgt durch Import des 12-Wort-Seeds in eine neue Phoenix-Installation. Phoenix scannt dann die Blockchain nach Channels und on-chain Guthaben.

Was nicht wiederhergestellt wird: Zahlungshistorie. Diese ist lokal gespeichert und nicht im Seed enthalten.

Der Seed ist plattformübergreifend kompatibel (Android ↔ iOS). Er ist auch ein Standard-BIP39-Seed und kann in andere Wallets importiert werden — allerdings erfordert der Zugriff auf Lightning-Channel-Guthaben typischerweise das vorherige Schliessen der Channels.

**Einschränkung**: Denselben Seed in zwei gleichzeitig aktiven Phoenix-Instanzen zu nutzen führt zu Channel-Konflikten und möglichen Force-Closes. Ein Seed, eine Instanz.

### Verhältnis zu on-chain Gebühren

Lightning-Zahlungen sind von hohen on-chain Gebühren unabhängig. Betroffen sind nur Operationen, die on-chain Transaktionen erfordern: on-chain Einzahlungen, Channel-Eröffnungen/Splices bei eingehenden Zahlungen, und Force-Closes. In Phasen hoher Mempool-Auslastung können diese Operationen erheblich teurer werden.

### Sicherheitsprinzip: Gelder immer sicher

Ein zentrales Design-Prinzip: Gelder sind nie in Gefahr, auch wenn Operationen fehlschlagen. Hängende ausgehende Zahlungen werden automatisch zurückerstattet. Nach Force-Closes sind Gelder nach Ablauf des Timelocks (typisch 144 Blöcke ≈ 1 Tag) automatisch on-chain verfügbar. ACINQ kann Gelder nicht einfrieren oder entwenden.

Der Zahlungsvorweis (Payment Preimage) dient als Zahlungsnachweis: Wenn der Status "complete" zeigt, wurde die Zahlung definitiv empfangen.

## Related

- [[skalierung-lightning-ark-statechains]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[hardware-wallet-einstieg]]
- [[transaktionsgebuehren-und-mempool]]
- [[hd-wallets-und-schluesselableitung]]
- [[opsec-und-privatsphaere]]

- [[einfuehrung-in-das-lightning-netzwerk|Einführung in das Lightning-Netzwerk (Antonopoulos, Osuntokun & Pickhardt)]] ← Buch

## Open Questions

- Wann werden Trampoline Payments mit Blinded Paths in Phoenix implementiert, um Zahlungsdatenschutz zu verbessern?
- Wie verhält sich Phoenix bei sehr hohen on-chain Gebühren über längere Zeiträume — bleibt die Wallet nutzbar?
- Gibt es Pläne für Multi-Peer-Verbindungen, um die ACINQ-Abhängigkeit zu reduzieren?
- Wie verhalten sich Phoenix-Channels bei Splicing im Vergleich zu traditionellen Channel-Öffnungen hinsichtlich Kosten und Latenz?
