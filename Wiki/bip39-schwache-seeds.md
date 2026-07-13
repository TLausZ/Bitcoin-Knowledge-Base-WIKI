# BIP39 Schwache Seeds

**Status:** established
**Themen:** bips, self-custody
**Last updated:** 2026-06-28
**Sources:** [[alex-waltz-bip39-weak-seeds]], [[alex-waltz-electrum-first-deterministic-wallet]]

## Summary

BIP39 erlaubt Mnemonics, bei denen alle Wörter identisch sind — etwa „beef beef beef beef beef beef beef beef beef beef beef beef". Von 184.320 möglichen solcher Einwort-Mnemonics sind exakt 241 technisch gültig (da das letzte Wort die Prüfsumme enthält). Diese Phrasen sollte man nie als echten Seed verwenden; sie demonstrieren aber einen weniger bekannten Aspekt des BIP39-Standards.

## Body

### Wie BIP39 funktioniert

BIP39 kodiert Entropie in 12, 15, 18, 21 oder 24 englische Wörter aus einem festen Wörterbuch von 2.048 Einträgen. Der Prozess: Entropie wird in 11-Bit-Blöcke aufgeteilt, jeder Block wird als Index ins Wörterbuch umgewandelt. Das letzte Wort ist Sonderfall — es enthält die Prüfsumme (Checksum = Entropielänge / 32 Bits, also 4 Bits bei 12 Wörtern, 8 Bits bei 24 Wörtern).

Aus dem Mnemonic wird dann via PBKDF2 (Password-Based Key Derivation Function 2, 2048 Iterationen) ein 512-Bit-Seed berechnet, den Wallets weiterverarbeiten.

### Warum „beef beef beef..." gültig ist

Das Wort „beef" liegt im BIP39-Wörterbuch. Bei 12 gleichen Wörtern müssen die ersten 11 Wörter als Entropie-Blöcke passen, und das 12. Wort muss die Prüfsumme-Bedingung erfüllen. Weil die letzten Bits des 12. Worts aus dem SHA256-Hash der vorangegangenen Bits berechnet werden, ist nicht jede Einwort-Kombination gültig. Von 2.048 möglichen Wörtern bei einem 12-Wort-Mnemonic aus identischen Wörtern erfüllen nur 241 diese Bedingung — darunter „beef" und „valid".

### Warum das ein Problem ist

Solche Mnemonics haben extrem niedrige Entropie. Alle 241 gültigen Einwort-Mnemonics sind bekannt und öffentlich dokumentiert. Wer Bitcoin dorthin schickt, gibt sie faktisch preis — jeder mit dieser Liste kann die Wallets prüfen und Funds stehlen. Das wäre kein Fehler im Protokoll, sondern menschliche Unvorsicht.

### Das tieferliegende BIP39-Problem: Derivationspfade

Ein weniger diskutiertes Problem von BIP39: Die Wörter allein reichen für eine vollständige Wallet-Recovery nicht immer aus. BIP39 kodiert keine Information über den Derivationspfad. Verschiedene Wallets nutzen unterschiedliche Pfade (m/44'/0'/0' für Legacy, m/84'/0'/0' für Native SegWit usw.). Wer die Wörter hat, aber nicht mehr weiss, mit welcher Wallet und welchem Pfad sie erstellt wurden, muss alle gängigen Pfade durchprobieren.

### Electrum-Seeds: Ein überlegenes Design

Electrum hatte dieses Problem früher erkannt. Die originale Electrum-Mnemonic-Implementierung von 2011 (vor BIP39) nutzte ein eigenes 1.626-Wörter-Wörterbuch. Seit Electrum 2.0 (2015) gibt es ein Versioning-System im Seed selbst — die Seed-Phrase kodiert welche Art von Wallet sie öffnet, sodass bei der Recovery keine Mehrdeutigkeit entsteht. Außerdem ist sie unabhängig von einem festen Wörterbuch und kann aktualisiert werden.

BIP39 wurde trotzdem zum De-facto-Standard, da nahezu alle anderen Wallets es adoptiert haben. Das macht BIP39-Seeds interoperabler — aber die fehlenden Derivationspfad-Informationen bleiben ein praktisches Risiko.

## Related

- [[bip-0039]]
- [[seedphrase-entropie-und-sicherheit]]
- [[diceware-und-seed-generierung]]
- [[electrum-wallet]]
- [[hd-wallets-und-schluesselableitung]]

## Open Questions

- Sollte man beim Backup zusätzlich den Derivationspfad und den Wallet-Namen notieren?
- Wie viele Nutzer verloren tatsächlich Funds wegen inkompatibler Derivationspfade?
