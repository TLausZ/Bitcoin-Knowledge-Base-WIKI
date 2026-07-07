# Selbstverwahrung und Börsenrisiken

**Status:** established
**Last updated:** 2026-07-07
**Sources:** [[20230103_wir-feiern-proof-of-keys-de]], [[aprycot-seedor-bitcoin-ist-sicher]], [[aprycot-21bitcoin-custody-einfach-erklaert]], [[20230118_die-bitbox01-ist-am-ende-ihrer-reise-de]], [[20220822_warum-bitcoin-eigenes-wallet-halten-de]], [[20220103_proof-of-keys-bitcoin-de]], [[20210622_warum-bitcoin-nicht-auf-boersen-aufbewahren-de]], [[2025-10-03_Blocktrainer-Bitcoin sicher aufbewahren 2025_ Selbstverwahrung, Wallet und Co.]], [[2025-05-14_Blocktrainer-Bitcoin_ 5 Anfängerfehler, die teuer werden können]], [[Bitcoin ist die Wiederentdeckung des Geldes.md]], [[Die andere Seite der Medaille.md]], [[bitcoin-ratgeber_kapitel-02-sei-deine-eigene-bank]], [[20221115_bmi-ftx-bankrott-de]]

## Summary

Wer Bitcoin auf einer Börse hält, besitzt kein Bitcoin — nur eine Forderung gegen ein Unternehmen. Börsenpleiten (Mt. Gox 2014, FTX 2022), Hacks und willkürliche Kontosperrungen haben das wiederholt bewiesen. Der Proof-of-Keys-Tag am 3. Januar erinnert die Bitcoin-Community jährlich daran, ihre Coins abzuheben und in Selbstverwahrung zu nehmen. Nur wer seinen privaten Schlüssel selbst hält, besitzt Bitcoin im eigentlichen Sinne.

## Body

### Gegenparteirisiko als Grundproblem

Jede Bitcoin-Börse ist eine Gegenpartei. Das bedeutet: Man vertraut darauf, dass sie solvent ist, nicht gehackt wird, Abhebungen erlaubt und nicht unter regulatorischem Druck einfriert. Keines dieser Versprechen ist garantiert.

Das ist keine theoretische Überlegung. Einige dokumentierte Fälle:

- **Mt. Gox (2014):** Damals größte Bitcoin-Börse weltweit. Verlor 650.000 Bitcoin durch einen Hack. Nutzer warteten jahrelang auf Rückerstattung — viele warten noch heute (Stand 2021).
- **QuadrigaCX (2019):** Kanadische Börse verlor ~215 Millionen US-Dollar. Der CEO Gerald Cotton starb angeblich in Indien, und mit ihm die Zugangspasswörter zu den Cold-Wallets — oder so lautete zumindest die offizielle Version. Spätere Untersuchungen legten nahe, dass die Gelder schon länger fehlten.
- **FTX (2022):** Nutzer verloren über 10 Milliarden Dollar, weil ihre Kontoguthaben nicht durch reale Bitcoin-Bestände gedeckt waren.
- **Coinbase (2017):** Frierte Konten von Nutzern ein, die Bitcoin mit Kreditkarten gekauft hatten, wegen Betrugsverdachts — unabhängig von der Schuld der Nutzer.

### KYC als Datenschutzrisiko

Börsen, die eine vollständige Identifikation (KYC — Know Your Customer) verlangen, sammeln eine Verbindung zwischen Identität und Bitcoin-Adressen. Dieser Datensatz hat einen Wert.

Blockchain-Analyse-Firmen (z.B. Chainalysis) kaufen oder erhalten diese Daten und können damit Bitcoin-Transaktionen einzelnen Personen zuordnen. Selbst wenn man die Coins längst von der Börse abgezogen hat, bleibt die Verbindung "diese Person hat Bitcoin besessen" bestehen. Das kann regulatorische, steuerliche oder sicherheitsrelevante Konsequenzen haben.

KYC-light Alternativen wie Relai (Banküberweisung, kein Konto) oder Pocket Bitcoin (Direktkauf in Hardware-Wallet) minimieren diese Datenspur. Für den, dem Privatsphäre wichtig ist, hinterlässt die KYC-Anforderung einer Börse einen dauerhaften Fußabdruck.

### Papier-Bitcoin und Fractional Reserves

Wenn viele Nutzer ihre Bitcoin auf Börsen lagern, können Börsen mehr Bitcoin in ihren Büchern ausweisen, als tatsächlich auf der Blockchain existieren. Diese "Papier-Bitcoin" halten sich nicht an das 21-Millionen-Limit. Eine Börse, die insolvent wird, kann diese Papier-Positionen nicht auszahlen.

Das ist strukturell ähnlich wie ein Banksystem mit Teilreserve (Fractional Reserve Banking) — mit dem Unterschied, dass Bitcoin-Gläubiger keine staatliche Einlagensicherung haben.

Die Analogie zum Papiergold ist direkt: Das geschätzte Verhältnis von physischem Gold zu Papiergold-Ansprüchen (ETFs, Terminkontrakte, Futures) liegt zwischen 1:10 und mehr als 1:200. Die genaue Zahl lässt sich nicht bestimmen, aber die Größenordnung zeigt das strukturelle Problem. Ein überhöhtes Papier-Angebot drückt den Preis des echten Vermögenswerts — und wenn Nachfrage entsteht, die tatsächliche Bestände verlangt, bricht das System ein.

### Proof-of-Keys-Tag

Der Proof-of-Keys Day am **3. Januar** (Jahrestag des ersten Bitcoin-Blocks, des "Genesis-Blocks") wurde 2019 von Trace Mayer ins Leben gerufen. An diesem Tag werden Bitcoiner aufgerufen, ihre Coins von Börsen abzuheben. Das hat zwei Effekte:

1. **Persönlich:** Man bestätigt, dass man noch Zugang zu seinen Coins hat und versteht, wie Selbstverwahrung funktioniert.
2. **Systemisch:** Koordinierte Abhebungen legen solvent erscheinende, aber tatsächlich unterdeckte Börsen offen.

### FTX in Echtzeit: Börsenabflüsse und Proof-of-Reserves-Welle (Wüstenfeld, Nov 2022)

Jan Wüstenfeld dokumentierte in seinem Newsletter unmittelbar nach dem FTX-Kollaps, wie sich das Ereignis on-chain niederschlug. Die realisierten Nettoverluste erreichten am 9. November 2022 rund 1,9 Milliarden Dollar — beträchtlich, aber unter den Werten des LUNA-Crashs (≈2,5 Mrd. am 9. und 11. Mai) und des Celsius-Ereignisses (4,2 Mrd. am 13. Juni). Der Anteil der seit mehr als sechs Monaten unbewegten Bitcoin fiel nur leicht von 81 % auf 79 %; der Bestand, der länger als ein Jahr ruhte, nahm sogar zu. Langfristige Halter saßen die Turbulenzen also aus.

Die für dieses Thema zentrale Beobachtung: Seit Beginn des FTX-Crashs verließen mehr als 200.000 Bitcoin die Börsen — möglicherweise einer der größten wöchentlichen Nettoabflüsse der Bitcoin-Geschichte. Wüstenfeld deutet das als praktische Lektion von «Not your keys, not your coins»: Wer Coins auf einer Börse hält, erfährt erst bei deren Implosion, ob die Bitcoin überhaupt existierten. Zugleich blieben laut seiner Analyse über 2 Millionen Bitcoin auf Börsen liegen.

Als Nebeneffekt kündigten nach dem Disaster mehr Börsen Proof-of-Reserves an. Kraken praktizierte das bereits länger; Huobi, Binance, Crypto.com, Deribit, Kucoin und Okx zogen mit Ankündigungen nach. Wüstenfelds Einordnung: kein Ersatz für Selbstverwahrung, aber ein Anfang, um die Widerstandsfähigkeit des Ökosystems zu verbessern — und ein direkter Bezug zur offenen Frage weiter unten, wie sich Börsensolvenz überhaupt prüfen lässt. [[20221115_bmi-ftx-bankrott-de]]

### Bitcoin als erlaubnisfreies System

Wer Bitcoin auf einer Börse hält, muss um Erlaubnis bitten, um die eigenen Coins zu bewegen. Die Börse kann verweigern — wegen lokaler Gesetze, wegen Betrugsverdachts, oder einfach weil der Markt kollabiert und Abhebungen gesperrt werden. Voyager Digital sperrte im Juli 2022 Handeln und Abhebungen; es war nicht der erste Fall.

Das ist der direkte Widerspruch zu Bitcoins ursprünglichem Versprechen: ein **erlaubnisfreies** Finanzsystem, an dem jeder teilnehmen kann — unabhängig von Herkunft, politischen Ansichten oder Schuldstatus. Dieses Versprechen gilt nur für Nutzer, die ihren Schlüssel selbst halten.

Selbst die Privatsphäre geht verloren: Wer Bitcoin über eine Börse bewegt, hinterlässt dort eine vollständige Transaktionshistorie. Die Börse weiß zu jeder Zeit den genauen Saldo. Je nach Jurisdiktion sind diese Daten regulatorisch abrufbar.

### Was Selbstverwahrung bedeutet

Selbstverwahrung bedeutet: Man hält den privaten Schlüssel selbst. Niemand sonst kann die Coins sperren, einfrieren oder verweigern. Man braucht keine Erlaubnis, um eine Transaktion zu senden.

### Physische Sicherung der Seed Phrase (Edelstahl)

Hardware-Wallets generieren eine Recovery Seed Phrase (12 oder 24 Wörter). Wer diese verliert, verliert seine Bitcoin unwiderruflich. Papier-Backups stoßen schnell an physische Grenzen: Ein Hausbrand, ein Wasserrohrbruch, ausbleichende Tinte oder ein neugieriger Hund machen den Notizzettel unbrauchbar.

Edelstahl ist das überlegene Material für langfristige Seed-Backups. Rostfreier Stahl ist resistent gegen Wasser, Feuer, Korrosion und mechanische Beanspruchung — und übersteht damit Szenarien, die Papier zerstören. Ein Edelstahl-Backup der Seed Phrase ist mit der richtigen Ausrüstung dauerhaft einprägbar.

SEEDOR — ein Schweizer Anbieter von Bitcoin-Backup-Systemen — verdichtet dieses Prinzip auf eine fertige Lösung: Schablone, Prägewerkzeug, Edelstahlscheiben und robuste Kapsel aus derselben Legierung. Das Ergebnis ist ein Backup, das laut Hersteller "Generationen überdauern" kann.

Stan Lee formulierte das Prinzip für eine andere Domäne treffend: "Aus großer Macht folgt große Verantwortung." Selbstverwahrung gibt einem vollständige Kontrolle über sein Bitcoin — aber diese Kontrolle ist nur so gut wie das Backup dahinter.

Quelle: [[aprycot-seedor-bitcoin-ist-sicher]]

Das entspricht auch dem ursprünglichen Versprechen von Bitcoin als dezentrales, zensurresistentes Zahlungsnetz. Wer sein Bitcoin bei einer Börse lässt, nutzt Bitcoin wie eine Bankeinlage — mit all den Risiken, die das impliziert, aber ohne die Sicherheiten, die Banken gesetzlich bieten müssen.

Eine Hardware-Wallet wie die BitBox02 überbrückt den Komfort-Sicherheits-Tradeoff: Sie ermöglicht sichere Selbstverwahrung ohne tiefes technisches Wissen.

### Bitcoin-ETPs und ETFs als Mittelweg

Für Einsteiger, die sich Selbstverwahrung noch nicht zutrauen, sind börsengehandelte Produkte eine Option. Bitcoin-ETPs (in Deutschland: ETNs/ETCs, keine ETFs wegen EU-Diversifikationspflicht) bilden den Kurs 1:1 ab. Wichtig: Sie sind Schuldverschreibungen, kein Sondervermögen. Bei Insolvenz des Emittenten drohen Verluste. Produkte mit "physischer" Bitcoin-Deckung sind sicherer als synthetische.

Der erhebliche Nachteil: Verwaltungsgebühren. BlackRock's europäischer Bitcoin-ETP kostet 0,25 % pro Jahr. Bei 40 Jahren Haltedauer fehlen ~10 % gegenüber direktem Bitcoin-Besitz. Viele europäische ETNs verlangen noch mehr. Für Langzeithalter kein optimales Vehikel.

Ein struktureller Vorteil: Kauf über normalen Aktien-Broker, kein Krypto-Börsenkonto nötig. Für kurzfristigen Exposure oder steuerlich optimierte Strukturen kann das sinnvoll sein. Für die vollständige Kontrolle führt kein Weg an der Selbstverwahrung vorbei.

### BitBox01 als Warnung: Legacy-Geräte und Abhängigkeiten

Auch bei Hardware-Wallets können Support-Abhängigkeiten entstehen. Die BitBox01 verlor 2022/2023 ihre Funktionsfähigkeit, weil externe Tools wie MyEtherWallet die Unterstützung einstellten und der 2FA-Relay-Server abgeschaltet wurde. Nutzer ohne gültiges Backup verloren den Zugang zu ihren Coins.

Das zeigt: Selbstverwahrung erfordert nicht nur das Gerät, sondern ein vollständiges, aktuelles Backup (Seedphrase) — unabhängig von proprietären Services.

### Schlüssel + Node = Wiederentdeckung des Geldes (Gigi)

Gigi formuliert Selbstverwahrung als philosophische Vollständigkeit, nicht nur als Sicherheitstechnik. Bitcoin ist die Wiederentdeckung des Geldes — aber nur dann, wenn man beides hält:

**Private Schlüssel** (kryptographische Seite): Wer keine eigenen Schlüssel hält, besitzt keine Bitcoin, sondern Schuldscheine — einen Kredit gegenüber der Börse. „Wenn dein Geld ein Gegenparteirisiko hat, ist es kein Geld, sondern ein Kredit."

**Full Node** (rechnerische Seite): Wer keinen eigenen Node betreibt, weiß nicht, ob die Bitcoin, die er zu besitzen glaubt, tatsächlich im Netzwerk existieren — und in welchem Netzwerk. Ein Node verifiziert selbst: die 21-Millionen-Grenze, die gültige Chain, den eigenen Kontostand.

Gigi: „Wenn du nicht im Besitz deiner eigenen Schlüssel bist, besitzt du keine Bitcoin, sondern Schuldscheine. Wenn du nicht deinen eigenen Node betreibst, hast du kein Mitspracherecht bei Bitcoin — du bist der Vorstellung eines anderen von Bitcoin verpflichtet." [[Bitcoin ist die Wiederentdeckung des Geldes.md]]

Nur wer beides kombiniert — eigene Schlüssel und eigenen Node — hat Geld wiederentdeckt: etwas, das ihm allein gehört, das kein Gegenparteirisiko hat und dessen Regeln er selbst verifiziert. Das war vor Bitcoin für digitales Geld strukturell unmöglich.

Geld hat nach Gigi keine Rendite, kein Gegenparteirisiko, braucht keine Identität und muss nicht wachsen. Shitcoins und Fiat-Deposits sind keine Alternative, weil sie all diese Eigenschaften verletzen. [[Die andere Seite der Medaille.md]]

### Custodial vs. Non-Custodial — Grundbegriffe (21bitcoin)

Der Unterschied zwischen Custodial- und Non-Custodial-Wallets: Bei Custodial verwahrt eine dritte Partei den privaten Schlüssel; bei Non-Custodial ist der Nutzer selbst Schlüsselinhaber. Der private Schlüssel (12 oder 24 Wörter) ist der einzige Beweis für Eigentum an den Coins — wer ihn teilt oder verliert, verliert seine Bitcoin. Anders als ein Autoschlüssel lässt er sich nicht nachmachen.

Custodial-Wallets haben legitime Anwendungsfälle: einfacher Einstieg, Kundendienst bei Passwort-Verlust, integrierte Handelsfunktionen. Non-Custodial-Wallets erfordern mehr Eigenverantwortung, sind aber die einzige Möglichkeit, Bitcoin tatsächlich zu besitzen.

Hardware-Wallets (z.B. Bitbox, Ledger, Trezor) verbinden beides: Sichere, eigenständige Bitcoin-Wallet auf dedizierter Hardware (USB-ähnliche Geräte), kontrolliert über einen Browser oder eine App. Der private Schlüssel verlässt das Gerät nie.

Eine Übergangs-Lösung für Einsteiger: Custodial-Wallet mit automatischer Übertragung auf eigene Hardware-Wallet sobald ein Schwellwert erreicht wird (z.B. 21bitcoins "Auto-Wallet-Transfer"-Feature). Schrittweise Übernahme der Selbstverwahrung statt Alles-oder-Nichts-Entscheidung.

## Related

- [[bitcoin-kaufen-und-dca]]
- [[wallet-backup-strategien]]
- [[opsec-und-privatsphaere]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[hardware-wallet-migration]]
- [[bitcoin-fehlannahmen]]
- [[eu-regulierung-selbstverwahrung]]

## Open Questions

- Wie kann man die Solvenz einer Börse überprüfen (Proof of Reserves)?
- Welche regulatorischen Entwicklungen ändern die Risikolandschaft für Börsenkunden in der EU?
- Wie entwickelt sich der ETP-Markt in Europa nach MiCA?
