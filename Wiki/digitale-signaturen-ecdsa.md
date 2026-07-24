# Digitale Signaturen (ECDSA)

**Status:** established
**Themen:** protokoll, privacy
**Last updated:** 2026-06-19
**Sources:** [[learnmeabitcoin-beginners-guide-digital-signatures]]

## Summary

Digitale Signaturen in Bitcoin ermöglichen es, den Besitz eines Private Keys zu beweisen, ohne ihn zu enthüllen. Eine Signatur besteht aus zwei Werten (r, s): r ist die x-Koordinate eines zufälligen Punkts auf der elliptischen Kurve, s kombiniert diesen Punkt mit dem Private Key und dem Transaktions-Hash. Weil jede Signatur an den genauen Transaktions-Hash gebunden ist, kann sie nicht in einer anderen Transaktion wiederverwendet werden. Das Verfahren heisst ECDSA (Elliptic Curve Digital Signature Algorithm).

## Body

### Wozu digitale Signaturen?

Wenn jemand Bitcoin ausgeben will, muss er beweisen, dass er den Private Key zur verwendeten Adresse kennt. Den Private Key direkt in die Transaktion zu schreiben wäre gefährlich: Jeder Node im Netzwerk würde ihn sehen — und könnte ihn nutzen, um andere Outputs derselben Adresse zu stehlen.

Die Lösung: Eine digitale Signatur, die mathematisch beweist, dass man den Private Key kennt, ohne ihn preiszugeben.

### Wie eine Signatur erstellt wird

Eine ECDSA-Signatur besteht aus zwei Teilen:

**r (der Zufallsteil):**
1. Eine grosse Zufallszahl `k` generieren
2. Den Generator Point G der elliptischen Kurve mit k multiplizieren: `k × G = Punkt P`
3. Die x-Koordinate dieses Punkts ist `r`

**s (der Signaturteil):**
```
s = (Hash(Transaktion) + r × Private Key) / k
```

Der Hash der Transaktion bindet die Signatur an genau diese eine Transaktion. Der Private Key stellt den mathematischen Zusammenhang mit dem Public Key her. Die Zufallszahl k sorgt dafür, dass jede Signatur einzigartig ist.

Das vollständige Paar `(r, s)` ist die digitale Signatur.

### Warum eine Signatur nicht wiederverwendet werden kann

Der Transaktions-Hash (`Hash(Transaktion)`) ist in der Signatur enthalten. Ändert sich irgendetwas an der Transaktion — Betrag, Empfänger, Inputs — ändert sich der Hash. Eine Signatur, die für Transaktion A erstellt wurde, ist für Transaktion B ungültig.

Das schützt auch gegen Manipulation: Wer eine bestätigte Transaktion nachträglich verändert, macht alle Signaturen ungültig.

### Wie eine Signatur verifiziert wird

Zur Verifikation braucht man: die Signatur `(r, s)`, den Transaktions-Hash und den Public Key.

1. **Punkt 1 berechnen:** `(Hash / s) × G`
2. **Punkt 2 berechnen:** `(r / s) × Public Key`
3. **Summieren:** Punkt 1 + Punkt 2 = Punkt 3
4. **Prüfen:** x-Koordinate von Punkt 3 = r?

Wenn ja → die Signatur ist gültig. Der Ersteller kannte den zum Public Key gehörigen Private Key.

Dieses Verfahren funktioniert wegen der mathematischen Eigenschaften der elliptischen Kurve: Der Public Key ist `Private Key × G`, und das ermöglicht die obige Gleichung zu lösen, ohne den Private Key zu kennen.

### Einmaligkeit der Zufallszahl k

Die Zufallszahl k muss für jede Signatur neu und kryptografisch sicher generiert werden. Wird dieselbe k zweimal verwendet (auch für zwei verschiedene Transaktionen), kann ein Beobachter den Private Key berechnen. Das ist in der Praxis der häufigste Implementierungsfehler bei ECDSA.

### ECDSA vs. Schnorr

Bitcoin verwendete seit Anfang ECDSA. Mit dem Taproot-Upgrade (2021) wurde **Schnorr-Signaturen** eingeführt. Schnorr ist einfacher, effizienter und ermöglicht native Schlüsselaggregation (MuSig2). → [[taproot-musig2-frost]]

## Related

- [[kryptografische-schlussel-und-adressen]]
- [[bitcoin-script-und-output-locks]]
- [[bitcoin-transaktionsstruktur]]
- [[segregated-witness-segwit]]
- [[taproot-musig2-frost]]
- [[anti-klepto-und-supply-chain-sicherheit]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos & Harding)]] ← Buch

## Open Questions

- Wie unterscheidet sich Schnorr mathematisch von ECDSA und warum ist es sicherer gegen bestimmte Angriffe?
- Was genau ist Dark Skippy und wie nutzt es ECDSA-Schwächen aus? → [[anti-klepto-und-supply-chain-sicherheit]]
