# Bitcoin als Information

**Status:** established
**Last updated:** 2026-06-23
**Sources:** [[aprycot-gigi-konsequenzen-bitcoin-verbot]]

## Summary

Gigi argumentiert, dass ein Bitcoin-Verbot technisch sinnlos ist, weil Bitcoin aus purem Text und Mathematik besteht. Ein privater Schlüssel ist eine 256-Bit-Zahl, die durch 256 Münzwürfe erzeugt werden kann. Eine Transaktion ist eine signierte Nachricht. Mining ist das Raten einer Zahl. Wer Bitcoin verbannt, muss konsequenterweise das Denken selbst kriminalisieren.

## Body

### Bitcoin ist Text, Mathematik, Sprache

Bitcoin braucht keine Spezialausrüstung. Es kann, im Prinzip, mit Stift und Papier betrieben werden. Drei Schritte genügen:

1. Eine Münze 256 Mal werfen → privater Schlüssel
2. Einen Rechenausdruck auswerten → digitale Signatur
3. Eine Nachricht senden → Transaktion

Das ist keine Metapher. Ken Shirriff hat 2014 eine Runde SHA-256 in 16 Minuten 45 Sekunden per Hand berechnet — das entspricht 0,67 Hashes pro Tag. Mining von Hand ist nicht praktikabel, aber möglich. Die gleiche Logik gilt für alle Schichten des Protokolls.

Ein privater Schlüssel ist eine 256-Bit-Zahl. Dargestellt als 24 mnemonische Wörter ist sie im Kopf speicherbar. Keine Geräte, kein Netzwerk, kein Konto — wer die Zahl kennt, hat die Bitcoin.

### Die Konsequenz für Verbote

Wenn ein Staat „anonyme Wallets" verbieten will, muss er konsequent sein:

- Das Erzeugen von Zufallszahlen müsste illegal sein.
- Das Werfen von Münzen oder Würfeln wäre verboten.
- Das Ausdenken einer Folge von 12 Wörtern wäre strafbar.

Da alle Informationen als Zahlen dargestellt werden können, liefe ein vollständiges Bitcoin-Verbot auf das Verbot bestimmter Zahlen hinaus. Das ist kein Gedankenspiel: Es gibt Präzedenzfälle. „Illegale Zahlen" entstanden in den 1990ern, als Verschlüsselungsalgorithmen aus Exportgründen kriminalisiert wurden — konkrete Zahlenfolgen, deren Besitz illegal war. Ebenso gab es „illegale Primzahlen", die DVD-Kopierschutz-Schlüssel kodierten. Die Analogie ist direkt. [[redefreiheit-und-protokolle]]

Ein US-Bundesgericht hat 2000 festgestellt: Kommunikation verliert den verfassungsrechtlichen Schutz als Redefreiheit nicht dadurch, dass sie in Computercode ausgedrückt wird. Mathematische Formeln sind Sprache. Bitcoin-Transaktionen sind Nachrichten. (*Junger v. Daley, 209 F.3d 481, 484*)

### Was eine Transaktion ist

Eine Bitcoin-Transaktion ist eine signierte Nachricht: „Ich, Alice, überweise 21 Sats an Bob." Sie ist Klartext — nichts darin ist verschlüsselt. Sie kann über jeden Kommunikationskanal übertragen werden: Internet, Satellit, Amateurfunk. Der Kanal ist austauschbar; die Information bleibt dieselbe.

Das macht Bitcoin zu einem Nachrichtenprotokoll. Wer das Versenden bestimmter Nachrichten verbieten will, muss den Inhalt kontrollieren, nicht den Kanal — und Information kann auf nahezu unendlich viele Weisen kodiert werden.

### Was Mining ist

Miner raten Zahlen. SHA-256 nimmt eine Eingabe und gibt eine Ausgabe zurück, die unter einem bestimmten Zielwert liegen muss. Das ist keine mysteriöse Technologie. Es ist ineffizient von Hand machbar, effizient mit ASICs — aber dasselbe Prinzip. ASICs zu verbieten stoppt Mining nicht; sie beschleunigen nur, was rechnerisch möglich ist.

### Wallets sind Gedanken

Eine Wallet ist, in ihrem Kern, ein privater Schlüssel — also eine Zahl — und möglicherweise einige Worte im Kopf. Kein externes Gerät, keine Registrierung, kein Nachweis des Wohnsitzes. Das Konzept „nicht-verwahrende Wallet" ist in einem technischen Sinne redundant: jede Wallet, die den privaten Schlüssel hält, ist per Definition selbstverwahrend. Regulatoren, die „nicht-verwahrende Wallets" verbieten wollen, verbieten das Denken. [[bitcoin-sprache-und-terminologie]]

## Related

- [[redefreiheit-und-protokolle]]
- [[bitcoin-regierungsresistenz]]
- [[bitcoin-sprache-und-terminologie]]
- [[bitcoin-digitale-knappheit]]
- [[kryptografische-schlussel-und-adressen]]
- [[cypherpunk-manifest]]

## Open Questions

- Wie verhält sich dieses Argument zu Protokollen, die auf Netzwerkebene blockiert werden können (z.B. IP-Filterung)? Bitcoin kann über Tor, Satellit, Amateurfunk laufen — aber wie robust ist das in der Praxis gegen staatliche Zensur?
- Illegale Zahlen als historischer Präzedenzfall: Sind Gerichte in anderen Ländern der Junger v. Daley-Logik gefolgt, oder ist das ein US-spezifisches Argument?
