# Phishing und Bitcoin-Angriffsmethoden

**Status:** established
**Themen:** self-custody, mining, kritik
**Last updated:** 2026-07-22
**Sources:** [[20230906_online-sicherheit-betrügerische-e-mails-erkennen]], [[20250911_wie-man-bitcoin-von-anderen-stiehlt]], [[20240627_wie-unser-kundensupport-bitbox-produkte-prägt]], [[20220721_datenleck-activecampaign-de]], [[20250921_heartmoney-von-spatsommer-zu-selbstermachtigung]], [[20250928_heartmoney-menschheit-geduld-bitcoin-in-dieser-reihenfolge]], [[bitcoin-ratgeber_kapitel-05-sicherheit]], [[Die Schwingung passt nicht mehr]]

## Summary

Bitcoin-Angriffe zielen fast immer auf denselben Schwachpunkt: den Nutzer, nicht die Kryptografie. Gefälschte Apps, Address-Spoofing-Malware, Phishing-E-Mails und Keylogger sind die häufigsten Methoden. Gegen alle schützen zwei Grundregeln: Transaktionsdetails immer auf dem Hardware-Wallet-Display verifizieren und Wiederherstellungswörter niemals digital eingeben.

## Body

### Gefälschte Wallet-Apps

Gefälschte Wallet-Software gelangt über manipulierte Suchmaschinenergebnisse, bösartige Links oder als Beilage zu anderer Software auf das Gerät. Sie imitiert das Aussehen und Verhalten echter Anwendungen. Eine gut gemachte Fake-App kann exakt wie das Original wirken — mit subtilen Manipulationen im Hintergrund, etwa beim Austauschen von Adressen oder Beträgen.

**Schutz:** Software nur von der offiziellen Website herunterladen. Keine Suchmaschinen beim Installieren sensibler Software nutzen. Offizielle Seiten als Lesezeichen speichern. Nach dem Download die digitale Signatur oder Prüfsumme verifizieren. Das Display der Hardware-Wallet ist die letzte Sicherheitsbarriere — eine Fake-App kann die dort angezeigten Informationen nicht manipulieren.

### Address Spoofing (Adressmanipulation)

Einer der effektivsten Angriffe. Spezialisierte Malware tauscht im Hintergrund Bitcoin-Adressen aus — die Empfangsadresse, die der Nutzer einfügt, wird durch die Adresse des Angreifers ersetzt. In einem bekannten Supply-Chain-Angriff auf den Node Package Manager (NPM) wurden so ähnlich aussehende Adressen ersetzt; die Malware wurde mehrere Milliarden Mal installiert.

Angreifer optimieren ihre Adressen so, dass sie den ersten und letzten Zeichen der Zieladresse ähneln — wer nur Anfang und Ende prüft, fällt herein.

**Schutz:** Immer die vollständige Empfangsadresse auf dem Hardware-Wallet-Display mit der ursprünglichen Quelle abgleichen. Adressverifikation über unabhängige Kanäle. Payment Requests (SLIP-24) ermöglichen kryptografische Verifikation der Adressauthentizität.

### Phishing-E-Mails

Phishing-E-Mails imitieren offizielle Kommunikation (z.B. von einem Hardware-Wallet-Hersteller) und nutzen psychologische Druckmittel wie Dringlichkeit. Ziel: Den Nutzer auf eine bösartige Website oder zu einer gefälschten App-Version zu locken. Diese könnten dann nach Wiederherstellungswörtern fragen oder Screenshots analysieren.

**Erkennungsmerkmale:** Falsche Absenderadresse (z.B. nicht @bitbox.swiss), schlechte Grammatik, ungewöhnlicher Zeitdruck, direkte Links zu Installationsdateien. Legitime Hersteller fragen **niemals** nach Wiederherstellungswörtern.

2023 wurden zwei betrügerische E-Mails im BitBox-Layout gemeldet. Ein Phishing-Angriff auf BitBox wurde 2024 vom Kundensupport erkannt, bevor Nutzer Schaden nehmen konnten.

### Keylogger

Keylogger zeichnen sämtliche Tastatureingaben auf. Fatal: Die Wiederherstellungswörter auf dem Computer eintippen. Damit hätte ein Angreifer mit Keylogger-Zugang vollständige Kontrolle über die Wallet.

**Schutz:** Wiederherstellungswörter niemals irgendwo digital eingeben — ausschliesslich direkt auf der Hardware-Wallet.

### Phishing nach einem Datenleck

Wenn E-Mail-Adressen durch ein Datenleck bei einem Drittanbieter bekannt werden, haben Angreifer eine wertvolle Ausgangsbasis: Sie kennen den Namen des Nutzers, seine E-Mail-Adresse und unter Umständen den Hinweis, dass er ein Hardware-Wallet besitzt. Das ermöglicht personalisierte, glaubwürdig klingende Phishing-Nachrichten.

Im Juli 2022 gelang einem Angreifer der Zugriff auf E-Mail-Listen des Marketing-Dienstleisters ActiveCampaign — trotz aktivierter Zwei-Faktor-Authentifizierung. Erbeutet wurden Name, E-Mail-Adresse und IP-Adresse von Newsletter-Abonnenten. Kurz danach gab es Berichte über Phishing-E-Mails, die wahrscheinlich auf diesen Daten basierten.

Typische Muster nach einem Datenleck:
- "Dein Konto wurde gesperrt — reaktiviere es mit deinen Wiederherstellungswörtern"
- "Sicherheitsupdate erforderlich — lade die neue BitBoxApp von folgendem Link"
- "Überweisung notwendig, um deine Coins zu sichern"

Alle drei Muster folgen dem gleichen Prinzip: Dringlichkeit erzeugen, den Nutzer zu einer gefährlichen Aktion bewegen. Shift Crypto wird **niemals** nach Wiederherstellungswörtern, Wallet-Backups oder direkten Überweisungen fragen.

**Strukturelles Schutzprinzip:** Seriöse Hardware-Wallet-Hersteller bieten in ihren Sicherheitsmitteilungen nach einem Datenleck immer dasselbe Muster: Kein Handlungsbedarf, keine Links zu Installationsdateien, kein Anlass zur Panik. Jede E-Mail, die das Gegenteil vermittelt, ist mit sehr hoher Wahrscheinlichkeit ein Angriff.

### Rendite- und Mining-Scams (Social-Media-Muster 2025)

Neben den technischen Angriffen oben existiert eine zweite Kategorie, die keinen Code braucht: Anlagebetrug im Bitcoin-Gewand. Das 2025 dokumentierte Muster läuft über Instagram-Direktnachrichten und Mail und verspricht Rendite durch «Bitcoin-Mining» oder Handelsprogramme. Der Ablauf ist immer gleich: hohe Renditen als Köder, der Kunde investiert, sieht (scheinbare) Gewinne, investiert mehr — dann sind Auszahlung und Guthaben eingefroren, das Geld ist weg. Auffällig ist die soziale Verteidigung der Betreiber: Kritiker werden zu «Informations-Calls» eingeladen («man müsse sich doch erst über die Renditechancen informieren»), Warnungen mit Empörung beantwortet.

Der Angriff zielt nicht auf Schlüssel, sondern auf Fremdverwahrungs-Bereitschaft; die Gegenregel ist entsprechend nicht technisch, sondern kategorisch: Wer Bitcoin gegen Renditeversprechen abgibt, hat sie im Betrugsfall verloren («Not your keys, not your coins», [[selbstverwahrung-und-boersenrisiken]]). Historische Referenz für das Muster ist der österreichische Fall Optioment (2017/18, aufgearbeitet von Bitcoin Austria): dieselbe Dramaturgie, damals über Vertriebsstrukturen statt Instagram. Dass sich nur der Kanal ändert und nicht das Schema, macht die Fälle als Lehrmaterial brauchbar. [[20250921_heartmoney-von-spatsommer-zu-selbstermachtigung]], [[20250928_heartmoney-menschheit-geduld-bitcoin-in-dieser-reihenfolge]]

### Identitätsdiebstahl auf Telegram

Eine dritte Betrugskategorie kopiert nicht Wallet-Software, sondern Personen und Gruppen: gefälschte Telegram-Profile und -Gruppen, die bekannte Bitcoin-Stimmen oder Community-Initiativen imitieren — teilweise mit einem Handle, das dem echten Account täuschend ähnlich sieht. Die Fake-Accounts kontaktieren Mitglieder der echten Gruppe im Namen der kopierten Person und bewerben Trading-Kurse oder Investitionsprogramme, die es nie gab. Dokumentiert ist das Muster bei der Frauen-Initiative Les Femmes Orange ([[frauen-und-bitcoin]]) und ihrer Gründerfigur Nicole Nowak: Zahlreiche gefälschte Profile kommunizierten unter ihrem Namen mit echten Gruppenmitgliedern.

**Schutz:** Auf Telegram grundsätzlich nichts kaufen und keinen Investitions- oder Trading-Aufforderungen folgen — seriöse Bitcoin-Persönlichkeiten und -Initiativen verkaufen keine Trading-Kurse über Direktnachrichten. Die echte Gruppe über die offizielle Website verifizieren, gefälschte Profile über die Telegram-Meldefunktion anzeigen. [[Die Schwingung passt nicht mehr]]

### Die zwei unverzichtbaren Grundregeln

Alle Angriffsmethoden haben denselben Gegenpol:

1. **Immer** alle Transaktionsdetails und Empfangsadressen auf dem sicheren Display der Hardware-Wallet verifizieren.
2. Wiederherstellungswörter **niemals** mit jemandem teilen und ausschliesslich direkt auf der Hardware-Wallet eingeben.

Wer diese zwei Regeln befolgt, lässt Angreifern kaum Spielraum.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[opsec-und-privatsphaere]]
- [[payment-requests]]
- [[anti-klepto-und-supply-chain-sicherheit]]
- [[hardware-wallet-angriffsvektoren]]

## Open Questions

- Wie entwickeln sich KI-gestützte Phishing-Methoden (personalisierte, fehlerfreie Fakes)?
- Welche Rolle spielen Passkey/FIDO2-Methoden beim Schutz von Wallet-Software-Downloads?
