# Regulierung: ToFR, Satoshi-Tests und AOPP

**Status:** established
**Themen:** protokoll, adoption
**Last updated:** 2026-06-06
**Sources:** [[20250109_wie-satoshi-tests-der-selbstverwahrung-schaden-und-warum-aopp-die-lösung-ist]], [[20210804_bitbox-08-2021-cristallina-update-de]]

## Summary

Die EU-„Transfer of Funds Regulation" (ToFR, in Kraft seit Dezember 2024) verpflichtet Broker und Börsen, die Kontrolle über Bitcoin-Adressen ihrer Kunden zu verifizieren. Die gebräuchlichste Methode — Satoshi-Tests (Testtransaktionen) — erzeugt mehrere praktische Probleme für Selbstverwahrende. Das Address Ownership Proof Protocol (AOPP) bietet eine elegantere Lösung, die in der BitBoxApp seit 2021 unterstützt wird.

## Body

### Was die ToFR verlangt

Die Transfer of Funds Regulation (auch „Travel Rule") gilt seit 30. Dezember 2024 in allen EU-Mitgliedstaaten. Ziel: Geldwäsche und kriminelle Aktivitäten mit Kryptowährungen einzudämmen. In der Praxis bedeutet das: Viele Broker und Börsen verlangen einen Nachweis, dass Kunden die Kontrolle über ihre Bitcoin-Adressen haben.

### Satoshi-Tests: Die problematische Standardmethode

Der verbreitetste Ansatz ist der **Satoshi-Test**: Der Nutzer schickt eine kleine Testtransaktion von seiner Wallet an die Börse. Sobald die Transaktion eingeht, gilt die Adresse als verifiziert.

**Drei Kernprobleme:**

1. **Henne-Ei-Problem:** Um eine Testtransaktion zu senden, braucht man Bitcoin. Wer noch keine hat, kann seine Adresse nicht verifizieren, um Bitcoin abzuheben.

2. **Wechseladressen:** Bitcoin-Wallets verwenden automatisch UTXOs für Transaktionen — oft von Wechseladressen, die in der Transaktionshistorie der Wallet nicht als reguläre Adressen auftauchen. Zukünftige Auszahlungen auf diese Wechseladressen wären dann in der App unsichtbar. Lösung: Coin Control in der BitBoxApp verwenden, um manuell einen geeigneten UTXO auszuwählen.

3. **Doppelte Einzahlungen:** Wenn Börsen Satoshi-Tests auch für Einzahlungen verlangen, kann der zu deponierende UTXO durch die Testtransaktion auf eine Wechseladresse wandern — die verifizierte Einzahlungsadresse ist danach leer. Resultat: drei On-Chain-Transaktionen für eine einzige Einzahlung.

Alle Satoshi-Tests schaden ausserdem der Privatsphäre: Da Testtransaktionen Gebühren kosten, werden Nutzer ermutigt, Adressen mehrfach zu verwenden.

### AOPP: Die bessere Lösung

Das **Address Ownership Proof Protocol** (AOPP) automatisiert das Signieren einer Nachricht mit dem privaten Schlüssel der zu verifizierenden Adresse — ohne On-Chain-Transaktion, ohne Gebühren.

Ablauf mit der BitBoxApp:
1. Klick auf „Adresse verifizieren" auf der Börsen-Website
2. BitBoxApp öffnet sich automatisch
3. BitBox02 fordert Bestätigung auf dem Gerät
4. Adresse und Signatur werden automatisch an die Börse übermittelt

AOPP gibt keine privaten Informationen preis — es teilt nur eine Bitcoin-Adresse und die dazugehörige Signatur, die man ohnehin teilen müsste. Die BitBoxApp implementierte AOPP im August 2021 als Teil des Cristallina-Updates — als erste Hardware-Wallet überhaupt, die das Protokoll unterstützte. AOPP wurde zusammen mit 21 Analytics spezifiziert und funktionierte bereits in BlueWallet und Sparrow Wallet, bevor es in Hardware ankam.

### Technische Grenzen aller Verifizierungsmethoden

Aus technischer Sicht kann keine Verifizierungsmethode eindeutig beweisen, *wer* die Kontrolle über eine Wallet hat. Ein Test beweist nur, dass *jemand* den Prozess durchgeführt hat. Kriminelle können die Anfragen an Dritte weiterleiten. Die ToFR ist daher in ihrer Wirksamkeit begrenzt — schafft aber trotzdem Hürden für normale Selbstverwahrende.

## Related

- [[opsec-und-privatsphaere]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[bitcoin-beratung-und-micar]]
- [[bitcoin-etf-und-institutionelle-verwahrung]]

## Open Questions

- Werden weitere Länder ähnliche Regulierungen einführen?
- Wird AOPP von mehr Börsen und Brokern übernommen?
- Wie entwickeln sich die regulatorischen Anforderungen für rein selbstverwahrendes Bitcoin?
