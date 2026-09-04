# SHRINCS: hashbasierte Post-Quantum-Signaturen für Bitcoin

**Status:** emerging
**Themen:** protokoll, self-custody
**Last updated:** 2026-09-04
**Sources:** [[Neuer BIP-Entwurf_ SHRINCS – So sollen quantensichere Bitcoin-Signaturen alltagstauglich werden]]

## Summary

SHRINCS ist ein BIP-Entwurf (Stand: August 2026, noch ohne Nummer, Status Draft) für ein hashbasiertes, quantensicheres Signaturverfahren, das speziell für Bitcoin entworfen wurde. Mitautor Jonas Nick nennt es den ersten konkreten Entwurf eines Post-Quantum-Signaturverfahrens für Bitcoin. Die Sicherheit beruht auf SHA-256 statt auf elliptischen Kurven, damit greift Shors Algorithmus nicht. Der Kern des Vorschlags ist die Kombination von zwei Signaturpfaden unter einem 48 Byte grossen Public Key: ein kompakter Stateful-Pfad für den Normalbetrieb und ein grösserer Stateless-Pfad als Rückfall, wenn der Wallet-Zustand nach einer Seed-Wiederherstellung verloren ist. Sighash, Script, Konsens und Aktivierung sind noch nicht spezifiziert; der Entwurf aktiviert nichts.

## Body

### Das Problem: Grösse

Schnorr-Signaturen brauchen 64 Byte. Viele Post-Quantum-Verfahren liefern mehrere Kilobyte pro Signatur. Bei solchen Grössen passen weniger Transaktionen in einen Block, was die Gebühren treibt. Eine Bitcoin-Lösung muss darum zwei Dinge gleichzeitig sein: quantenresistent und kompakt. Das standardisierte hashbasierte Verfahren (im Artikel nicht namentlich genannt) erzeugt 7'856 Byte pro Signatur; SHRINCS kommt im Stateful-Pfad je nach Merkle-Pfad auf 548 bis 4'619 Byte.

### Wie die Signatur funktioniert

Grundbaustein ist die Hashkette: Ein geheimer Zufallswert wird wiederholt mit SHA-256 gehasht, der Endwert ist öffentlich. Von einem veröffentlichten Zwischenwert aus kann jeder bis zum Ende weiterhashen, der Rückweg zum Anfang gilt als praktisch unmöglich.

Der Stateful-Pfad benutzt WOTS+C-Einmalschlüssel mit je 32 parallelen Hashketten und Positionen von 0 bis 15. Aus dem Nachrichtendigest und einem kleinen Suchwert in der Signatur leitet das Verfahren die 32 Kettenpositionen ab. Beim Signieren veröffentlicht die Wallet aus jeder Kette genau einen Zwischenwert; die davor liegenden Werte bleiben geheim. Der Verifizierer leitet dieselben Positionen ab und hasht jeden Wert vorwärts bis zum Kettenende. Die 32 Endwerte bilden den WOTS-Public-Key. Ein Merkle-Pfad in der Signatur führt zur Stateful-Wurzel, die mit dem entsprechenden Teil des 48-Byte-SHRINCS-Public-Keys verglichen wird.

### Warum ein Einmalschlüssel nur einmal signieren darf

Jede Signatur legt Zwischenwerte der Ketten offen. Signiert derselbe WOTS+C-Schlüssel zwei verschiedene Nachrichten, sieht ein Beobachter zusätzliche Kettenstücke. Das gibt nicht zwingend den Hauptschlüssel preis, kann aber genügen, um eine gültige Signatur für eine dritte Nachricht zu konstruieren und die Coins auszugeben.

Deshalb führt die Wallet einen persistenten Counter, der bei 0 beginnt und pro Stateful-Signatur steigt. Aus Counter und Baumstruktur ergibt sich der nächste unbenutzte Slot. Der neue Zählerstand muss dauerhaft gespeichert sein, bevor die Signatur die Wallet verlässt. Er darf nicht aus einem Backup zurückgesetzt werden, und paralleles Signieren mit demselben Schlüssel auf mehreren Geräten ist gefährlich. Der Draft verlangt geschützten, dauerhaften, möglichst rollback-sicheren Speicher.

Das erzeugt ein Backup-Problem: Der Seed lässt sich wiederherstellen, der letzte Counter-Stand steckt nicht darin. Eine wiederhergestellte Wallet mit altem Zählerstand würde Einmalschlüssel erneut verwenden.

### Der Trick: Stateless Recovery

SHRINCS bindet zwei alternative Pfade unter einen Public Key. Eine gültige Signatur aus einem der beiden genügt.

| Pfad | Signaturgrösse | Voraussetzung |
|---|---|---|
| Stateful (Normalbetrieb) | 548 bis 4'619 Byte | zuverlässig gespeicherter Counter |
| Stateless (Rückfall) | immer 5'777 Byte | kein persistenter Zustand |

Ist der Counter verloren, beschädigt oder unsicher, muss die Wallet Stateful-Signaturen verweigern und den Stateless-Pfad nehmen. Nach einer Seed-Wiederherstellung kann sie die Coins über diesen Pfad auf ein neues Schlüsselpaar übertragen, für das dann bei korrekt geführtem Counter wieder der kompakte Pfad gilt. Wie SHRINCS-Schlüssel aus einer Mnemonic abgeleitet werden, ist nicht Teil des Entwurfs.

### Was der Entwurf nicht ist

Der Draft spezifiziert Schlüsselerzeugung, Signieren und Verifizieren und enthält eine ausführbare Referenzimplementierung, die nur der Prüfung der Spezifikation dient. Es fehlen: BIP-Nummer, formaler Sicherheitsbeweis für Konstruktion und Parameter, Sighash-Bildung, Script-Einbindung, Konsens- und Aktivierungsregeln. Nichts wird aktiviert, Schnorr wird nicht ersetzt. Der Beitrag ordnet SHRINCS als ersten konkreten Vorschlag ein, den Kryptografen und Entwickler jetzt testen und kritisieren können.

### Verhältnis zu BIP-360 und BIP-361

Die beiden vorhandenen Post-Quantum-BIPs im Korpus lösen andere Teile des Problems. [[bip-0360]] definiert mit Pay-to-Merkle-Root einen Output-Typ ohne Key-Path, der nur über Script-Path und hashbasierte Commitments ausgegeben wird. [[bip-0361]] beschreibt den Fahrplan zum Abschalten von ECDSA und Schnorr in zwei Phasen. Keiner der beiden legt fest, mit welchem Signaturverfahren quantensichere Outputs künftig autorisiert werden. SHRINCS ist ein Kandidat für genau diese Lücke. Die Quelle stellt diese Verbindung nicht explizit her; sie folgt aus der Arbeitsteilung der drei Entwürfe und bleibt bis zu einer Script-Spezifikation offen.

## Related

- [[bitcoin-und-quantenrisiko]]
- [[bip-0360]]
- [[bip-0361]]
- [[digitale-signaturen-ecdsa]]
- [[taproot-musig2-frost]]
- [[elliptische-kurven-kryptographie]]
- [[kryptografische-schlussel-und-adressen]]
- [[das-privacy-handbuch]] ← Buch (Autor des Beitrags)

## Open Questions

- Welches standardisierte hashbasierte Verfahren meint der Vergleichswert von 7'856 Byte? Der Primärentwurf (github.com/SHRINCS/shrincs-bip) fehlt im Korpus.
- Wie soll der Counter in Hardware-Wallets rollback-sicher gespeichert werden, und was heisst das für Multi-Device-Setups und Multisig?
- Wird SHRINCS als Script-Opcode in P2MR-Leaves (BIP-360) eingebunden oder als eigener Output-Typ?
- Bei welchen Gebühren wird der Stateless-Pfad mit 5'777 Byte für kleine UTXOs unwirtschaftlich?
