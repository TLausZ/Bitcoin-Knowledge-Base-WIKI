# EU-Regulierung und Bitcoin-Selbstverwahrung

**Status:** established
**Themen:** self-custody, adoption
**Last updated:** 2026-06-05
**Sources:** [[20240328_was-bedeuten-künftige-eu-regulierungen-für-bitbox-kunden]], [[20250109_wie-satoshi-tests-der-selbstverwahrung-schaden-und-warum-aopp-die-lösung-ist]]

## Summary

Die EU-Geldwäscheregulierungen betreffen hauptsächlich Börsen und Finanzdienstleister — nicht Non-Custodial-Wallet-Hersteller oder deren Nutzer. Das EU-Gesetz schließt Anbieter von Hardware und Software selbst gehosteter Wallets ausdrücklich aus. Selbstverwahrung bleibt legal und technisch uneinschränkbar. Die eigentliche Bedrohung für Selbstverwahrer kommt von Börsenseite: Travel Rule und Satoshi-Tests.

## Body

### Was das EU-AML-Gesetz regelt

Die EU hat Geldwäschebekämpfungsregeln (AML) beschlossen, die hauptsächlich Bargeldzahlungen einschränken und Finanzinstitute regulieren. Einige Regeln betreffen Kryptowährungsdienstleister wie Börsen und Broker. Für Non-Custodial-Wallets gilt:

- Hardware- und Software-Anbieter selbst gehosteter Wallets sind **ausdrücklich ausgenommen**
- Non-Custodial-Wallets und Peer-to-Peer-Transaktionen werden weder verboten noch direkt reguliert
- Die Bargeld-Obergrenzen erstrecken sich nicht auf Bitcoin-Transaktionen

### Warum Selbstverwahrung nicht einschränkbar ist

Selbst in einem restriktiveren regulatorischen Umfeld kann Bitcoin-Selbstverwahrung nicht wirksam eingeschränkt werden — aus technischen Gründen. Bitcoin-Transaktionen sind direkte Peer-to-Peer-Transfers ohne zentrale Schnittstelle, die reguliert werden könnte. Ein Hardware-Wallet-Hersteller hat keine Kontrolle darüber, welche Transaktionen seine Nutzer durchführen.

Die BitBoxApp kann auf eine eigene Full-Node oder die Node eines Freundes umgestellt werden. Mit Open-Source-Software wie Sparrow Wallet oder Electrum kann die BitBox02 völlig unabhängig von Herstellerservern genutzt werden.

### Datensparsamkeit als Grundprinzip

BitBox erhebt minimale Daten und anonymisiert Bestelldaten nach 30 Tagen. Bestellungen können an Packstationen oder Postfilialen geliefert werden. Die App enthält keine Tracker (verifiziert durch Exodus Privacy). Das Unternehmen hat technisch keine Möglichkeit, die Coin-Nutzung seiner Nutzer einzuschränken oder zu überwachen.

### Travel Rule und Satoshi-Tests bei Börsen

Während Selbstverwahrung selbst unreguliert bleibt, schreiben die Travel Rule und die EU-Transferverordnung (ToFR) Börsen vor, beim Abheben in nicht-verwaltete Wallets die Wallet-Inhaberschaft zu verifizieren. Börsen nutzen dafür häufig den sogenannten Satoshi-Test: eine winzige Testabhebung, deren genauen Betrag der Nutzer zurückmelden muss.

Das Problem: Der Satoshi-Test ist auf technischer Ebene nicht schlüssig. Der genaue Betrag einer Transaktion ist öffentlich auf der Blockchain einsehbar — jeder, der die Adresse kennt, kann den Betrag ablesen. Außerdem entstehen bei Wechselgeld-Outputs Abweichungen, die zu falschen Negativergebnissen führen können.

AOPP (Address Ownership Proof Protocol) ist eine sauberere Alternative: Die Wallet signiert eine Nachricht mit dem privaten Schlüssel der Bitcoin-Adresse, was den Eigentümernachweis kryptografisch beweist, ohne Testbeträge zu überweisen. Allerdings haben mehrere Schweizer Hardware-Wallet-Hersteller AOPP nach Nutzerprotesten 2022 wieder entfernt — die Debatte über datenschutzkonforme Adressverifikation ist nicht abgeschlossen.

## Related

- [[regulierung-tofr-aopp]]
- [[opsec-und-privatsphaere]]
- [[hardware-wallet-sicherheitsarchitektur]]

- [[bitcoin-unabhaengigkeit-neu-gedacht|Bitcoin – Unabhängigkeit neu gedacht (Knut Svanholm)]] ← Buch

## Open Questions

- Wie werden EU-MiCA und AML-Regeln in der Praxis auf Exchanges durchgesetzt?
- Werden Satoshi-Tests langfristig durch AOPP oder ähnliche kryptografische Methoden ersetzt?
- Wie entwickelt sich die Regulierung in der Schweiz (ausserhalb der EU)?
