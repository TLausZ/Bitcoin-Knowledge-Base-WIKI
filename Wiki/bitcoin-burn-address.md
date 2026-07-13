# Bitcoin Burn Address

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bitcoin-burn-address]]

## Summary

Eine Burn Address ist eine Bitcoin-Adresse, zu der niemand den privaten Schlüssel besitzt — Coins die dorthin geschickt werden, sind dauerhaft verloren. Die bekannteste ist `1111111111111111111114oLvT2`, die heute mehrere hundert Millionen Dollar enthält; kein privater Schlüssel dazu existiert oder kann existieren.

## Body

### Wie eine Bitcoin-Adresse entsteht

Vom privaten Schlüssel (eine zufällige Zahl) wird per Elliptischer-Kurven-Multiplikation ein öffentlicher Schlüssel abgeleitet — ein Einwegprozess. Der öffentliche Schlüssel wird dann gehasht (RIPEMD-160 nach SHA-256), eine Versionsnummer vorangestellt, eine Prüfsumme angehängt, und das Ganze in Base58 kodiert.

Base58 ist das normale alphanumerische Alphabet (62 Zeichen) minus die leicht verwechselbaren Zeichen `0`, `O`, `l` und `I` — macht 58. So lässt sich eine Adresse auch handschriftlich kopieren, ohne Fehler zu riskieren.

Wichtig: Adressen existieren nicht auf der Blockchain. Bitcoin-Nodes arbeiten intern mit Scripts und Public Keys — die Adresse ist eine menschenlesbare Darstellung davon, die Wallets erzeugen.

### Warum `1111...4oLvT2` eine Burn Address ist

Die 1er-Adresse entspricht einem öffentlichen Schlüssel, der aus einer privaten Zahl von 0 abgeleitet wäre — ein mathematisch unmöglicher Ausgangspunkt. Niemand hat den privaten Schlüssel dazu, weil es ihn nicht geben kann. Das ist der Unterschied zur Adresse des Bitcoin-Genesiblocks, wo Satoshi technisch einen privaten Schlüssel haben könnte, aber vermutlich keine Absicht hatte, je auszugeben.

Der Schlüsselgedanke: Der Raum möglicher Bitcoin-Adressen ist so groß (~2¹⁶⁰ für P2PKH), dass das zufällige Finden eines passenden privaten Schlüssels für eine fremde Adresse genauso unwahrscheinlich ist wie für die eigene. Burn Addresses sind keine besonders gesicherten Adressen — es gibt einfach keinen Schlüssel, weil die Adresse nicht aus einem generiert wurde.

### Was mit den Coins dort passiert

Gar nichts. Sie sitzen dort für immer, unveränderlich in der Blockchain verankert. Weil niemand die Ausgabebedingung erfüllen kann, können sie nie ausgegeben werden. Für das Gesamtangebot von 21 Millionen sind bewusst geburnte Coins effektiv deflationary — sie reduzieren das zirkulierende Angebot dauerhaft.

Die bekannte `1111...4oLvT2`-Adresse enthält hauptsächlich Coins, die von Projekten absichtlich dorthin geschickt wurden (z.B. als Token-Ausgabemechanismus auf anderen Protokollen, die Bitcoin-Adressen nutzen). Ein Teil stammt von frühen Fehlern.

### Prüfsumme: Warum Tippfehler selten Funds vernichten

Bitcoin-Adressen enthalten eine Prüfsumme (die letzten Bytes werden aus dem Hash des restlichen Inhalts berechnet). Wallets prüfen diese vor dem Senden. Eine zufällig falsch eingetippte Adresse schlägt daher mit hoher Wahrscheinlichkeit fehl, anstatt Coins an eine falsche Adresse zu schicken.

## Related

- [[kryptografische-schlussel-und-adressen]]
- [[bitcoin-transaktionsstruktur]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-script-und-output-locks]]

## Open Questions

- Wie viel Bitcoin liegt insgesamt in unausgebbaren Adressen (Satoshi-Wallets, Burn Addresses, verlorene Keys)?
