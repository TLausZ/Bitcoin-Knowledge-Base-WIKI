# Das Privacy Handbuch (Timo Volkov)

**Status:** established
**Themen:** privacy, philosophie, buecher
**Last updated:** 2026-07-13
**Sources:** [[Das-Privacy-Handbuch_Volkov]]

## Summary

Timo Volkovs „Privacy Handbuch" ist ein deutschsprachiger Praxis-Ratgeber für digitale Sicherheit und Privatsphäre aus dem Bitcoin-nahen Umfeld. Es ist weniger Theorie- als Umsetzungsbuch: vom Gefahrenmodell über Betriebssystem und Gerät bis zu konkreten Tool-Empfehlungen und aktiven Gegenmassnahmen. Der rote Faden ist digitaler Minimalismus, die Angriffsfläche gar nicht erst entstehen zu lassen.

## Body

### Threat Model zuerst

Volkov beginnt nicht mit Tools, sondern mit dem persönlichen „Threat Model": Wovor genau will ich mich schützen, und vor wem? Ein Journalist, der Quellen schützt, hat andere Anforderungen als jemand, der nur der Werbeindustrie entkommen will. Erst das Gefahrenmodell entscheidet, welche der folgenden Massnahmen sinnvoll sind, Privatsphäre ist kein Alles-oder-nichts, sondern eine Abwägung von Aufwand und Risiko.

### Digitaler Minimalismus

Das Leitprinzip: „Weniger ist mehr." Wer weniger digitale Dienste nutzt, bietet weniger Daten zum Sammeln. Statt Diensten, die sich über zielgerichtete Werbung finanzieren, wählt Volkov Alternativen mit anderem Geschäftsmodell. Der Nebeneffekt ist ein ruhigeres, weniger technologie­dominiertes Leben.

### Fundament: Gerät und Betriebssystem

Privacy-Tools auf einem kompromittierten Gerät sind wertlos, deshalb setzt das Buch beim Unterbau an:

- **Desktop:** Wechsel von Windows/macOS zu Linux (Ubuntu), Hardware-Sicherheit.
- **Anonyme Sitzungen:** Tails (amnesisches Live-System).
- **Smartphone:** GrapheneOS auf Pixel-Geräten, mit Nutzerprofilen, App-Sandboxing, Berechtigungs­kontrolle, Faraday-Taschen, Mikrofon-/Kamera-Management.

### Werkzeug-Stack

Die Kapitel arbeiten einen Baukasten ab, aus dem man je nach Threat Model wählt:

- **Browser & Netz:** LibreWolf, Tor-Browser, VPN, eigener DNS, Vorsicht in öffentlichen WLANs.
- **Zugänge:** starke Passwörter, Passwortmanager, 2FA, verschlüsselte Backups und USB-Sticks.
- **Kommunikation:** E-Mail mit Aliassen, Signal als Messenger, Nostr, PGP; getrennte Telefonnummern/SMS.
- **Datenminimierung:** private Alternativen für Kalender, Kontakte, Notizen und Office; bewusster Umgang mit Social Media, Musik/Podcasts, KI-Diensten.

### Aktive Gegenmassnahmen (OSINT-Abwehr)

Über die Verteidigung hinaus behandelt Volkov offensive Privatsphäre:

- **Aliase/Pseudonyme** für Kontexte, die keinen echten Namen brauchen.
- **Gezielte Falschinformationen** als falsche Fährte, um Profile zu verwässern.
- **„Plant your flag":** bei kritischen Institutionen (Steuer, Behörden) bewusst ein Konto auf den echten Namen anlegen, nicht zur Nutzung, sondern damit kein Betrüger es zuerst tut. Schutz vor Identitätsdiebstahl.
- **Metadaten entfernen**, Informationen gezielt löschen, Wohnadresse schützen, Daten für den Todesfall regeln.

### Bitcoin privat nutzen

Ein eigenes Kapitel überträgt die Prinzipien auf Bitcoin. „Not your keys, not your coins", belegt an Mt. Gox (2014) und FTX (2022), wo Coins in Fremdverwahrung über Nacht verschwanden. Für die Privatsphäre ist die eigene Wallet ebenso zentral: Wer die Verwahrung abgibt, macht seine Transaktionen, Bestände und Adressen für den Verwahrer zum offenen Buch. Selbstverwahrung ist damit sowohl Sicherheits- als auch Privatsphäre-Entscheidung.

## Related

- [[opsec-und-privatsphaere]]
- [[no-kyc-bitcoin]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[bitcoins-verwahren-und-vererben]]
- [[coin-control-und-utxo-auswahl]]
- [[coinjoin-und-on-chain-privatsphaere]]

## Open Questions

- Wo liegt für einen durchschnittlichen Nutzer der Punkt, an dem zusätzlicher Privacy-Aufwand mehr Reibung als Schutz bringt?
- „Gezielte Falschinformationen" als Taktik, wann kippt das von Selbstschutz in problematisches Verhalten (z. B. gegenüber Behörden)?
- Wie schnell veralten die konkreten Tool-Empfehlungen, und welche Prinzipien des Buches bleiben unabhängig von der Tool-Generation gültig?
