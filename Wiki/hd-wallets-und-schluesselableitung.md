# HD-Wallets und Schlüsselableitung

**Status:** established
**Themen:** protokoll, self-custody, privacy
**Last updated:** 2026-06-19
**Sources:** [[20220505_wie-entsteht-bitcoin-adresse-de]], [[20210804_bitbox-08-2021-cristallina-update-de]], [[20240314_wie-die-bitbox02-den-seed-für-die-lightning-wallet-sicher-ableitet]], [[learnmeabitcoin-technical-keys-hd-wallets]], [[learnmeabitcoin-technical-keys-hd-wallets-extended-keys]], [[learnmeabitcoin-technical-keys-hd-wallets-derivation-paths]], [[learnmeabitcoin-technical-keys-hd-wallets-mnemonic-seed]]

## Summary

Eine Bitcoin-Wallet muss theoretisch unbegrenzt viele Adressen erzeugen können — ohne für jede Adresse ein separates Backup anlegen zu müssen. Hierarchisch-deterministische Wallets (HD-Wallets) lösen das: Aus einem einzigen Seed wird nach einem festen Algorithmus ein ganzer Baum von Schlüsseln abgeleitet. Die Ableitung ist deterministisch (gleicher Seed → immer gleiche Schlüssel) und hierarchisch (strukturiert nach einem Pfad). Wer den Seed kennt, kann alle daraus abgeleiteten Schlüssel und Adressen wiederherstellen.

## Body

### Das Problem: Unendlich viele Adressen, eine Sicherung

Datenschutz erfordert, dass bei jedem Empfang eine neue, bisher unbenutzte Bitcoin-Adresse verwendet wird — sonst kann jeder, der eine Transaktion erhält, den gesamten Saldo der Adresse einsehen. Eine Wallet, die z.B. wöchentlich Zahlungen empfängt, braucht im Laufe der Zeit Tausende Adressen.

Ohne HD-Wallets müsste jede Adresse einzeln gesichert werden. Das HD-Prinzip (BIP32) macht stattdessen eine einzige Sicherung — den Seed — für alle jemals erzeugten Adressen ausreichend.

### Von der Seed-Phrase zum privaten Schlüssel

Die Ableitung erfolgt in mehreren Schritten:

**1. Seed-Phrase (BIP39)**

12 oder 24 englische Wörter aus einer standardisierten Wortliste. In Wirklichkeit eine zufällige Bitfolge (128 oder 256 Bit Entropie), die nur als Wörter codiert ist, weil Menschen damit besser umgehen können.

Wichtig: Die Seed-Phrase muss von einem echten Zufallsgenerator erzeugt werden. Selbst ausgedachte Wörter haben typischerweise viel weniger Entropie als echte Zufälligkeit — die Chance einer Kollision mit einer anderen Wallet steigt dramatisch. Die BitBox02 kombiniert mehrere Entropiequellen: eigener Zufallszahlengenerator, Nutzer-Passwort und Desktop-App.

Eine optionale Passphrase (BIP39 Passphrase) wird direkt mit dem Seed vermischt, *bevor* einzelne Schlüssel abgeleitet werden — dadurch entsteht ein komplett anderer Schlüsselbaum.

**2. Ableitungspfad**

Eine "Formel", die vorschreibt, welcher Schlüssel aus dem Seed abgeleitet wird. Das Konzept ähnelt einem Dateipfad: `m/49'/0'/0'/0/0`

Die Bestandteile:
- `m` — Masterkey (direkt aus dem Seed)
- `Zweck'` — welcher Standard (z.B. 49' für SegWit)
- `coin_type'` — welche Kryptowährung (0' = Bitcoin)
- `account'` — separate Konten innerhalb derselben Wallet
- `change` — externe (0) vs. interne Adressen (1, für Wechselgeld)
- `address_index` — die laufende Nummer der Adresse

Moderne Wallets erhöhen nur die letzte Zahl, um neue Adressen zu erzeugen:

```
m/49'/0'/0'/0/0  ← erste Empfangsadresse
m/49'/0'/0'/0/1  ← zweite Empfangsadresse
m/49'/0'/0'/0/2  ← dritte Empfangsadresse
…
```

Da der Pfad keine obere Grenze hat, können praktisch unbegrenzt viele Schlüssel abgeleitet werden.

**3. Privater Schlüssel → öffentlicher Schlüssel → Adresse**

Jeder Ableitungspfad ergibt einen privaten Schlüssel. Aus dem privaten Schlüssel wird der öffentliche Schlüssel berechnet (Einwegfunktion — der Umkehrweg ist rechnerisch unmöglich). Aus dem öffentlichen Schlüssel wird schliesslich die Bitcoin-Adresse gehasht.

Die Bitcoin-Adresse enthält ein Pubkey-Skript, das die Ausgabebedingungen festlegt: Wer die Transaktion signiert, muss beweisen, dass er den privaten Schlüssel besitzt.

### Technische Details: Extended Keys

**Mnemonic Sentence → Seed:** Die 12/24 Wörter (BIP 39) werden per PBKDF2-HMAC-SHA512 mit 2048 Iterationen und dem optionalen Passphrase-Salt in einen 64-Byte-Seed umgewandelt.

**Master Extended Key:** Der Seed wird durch HMAC-SHA512 mit dem festen String "Bitcoin seed" gehasht → 64 Bytes:
- Erste 32 Bytes → Master Private Key
- Letzte 32 Bytes → Master Chain Code (extra geheime Daten, die für Child-Ableitung benötigt werden)

**Extended Keys = Key + Chain Code.** Die 32-Byte-Chain-Code verhindert, dass jemand mit dem Public Key allein weitere Child-Keys ableiten kann. Extended Public Key (xpub) = Public Key + Chain Code; Extended Private Key (xprv) = Private Key + Chain Code.

**Child-Key-Ableitung:**
- **Normal (non-hardened):** HMAC-SHA512(chain_code, public_key || index) → abgeleitet aus xpub möglich
- **Hardened:** HMAC-SHA512(chain_code, `0x00` || private_key || index) → nur aus xprv möglich; sicherer

Hardened Kinder (BIP 32 Notation: `'` oder `h`) beginnen bei Index 2.147.483.648. Bis zu 4.294.967.296 Kinder pro Extended Key.

**Serialisierte Extended Keys (Base58Check):**
- xprv → beginnt mit `xprv`
- xpub → beginnt mit `xpub`
- Encoding: 4 Byte Version + 1 Byte Tiefe + 4 Byte Parent-Fingerprint + 4 Byte Child-Index + 32 Byte Chain-Code + 33 Byte Key = 78 Bytes → Base58Check

### Warum nur der Seed gesichert werden muss

Da die Ableitung deterministisch ist — gleiche Eingaben ergeben immer dieselben Ausgaben — muss die Wallet die abgeleiteten Schlüssel gar nicht dauerhaft speichern. Sie berechnet sie bei Bedarf neu. Wer den Seed kennt und den Standard-Ableitungspfad verwendet, kann auf jeder kompatiblen Wallet alle Bitcoin wiederherstellen.

Das macht die Seed-Phrase zur einzigen kritischen Sicherung. Verliert man das Gerät, verliert man keine Coins — solange die Seed-Phrase erhalten ist.

### Konten: Ein- und Ausblenden, nicht Erstellen und Löschen

Ein häufiges Missverständnis bei Bitcoin-Konten: Man "erstellt" kein neues Konto — man blendet eines ein. Alle Konten und Adressen, die eine Wallet jemals verwenden kann, existieren als potenzielle Ableitungen aus dem Seed schon von Anfang an. Hinzufügen und Entfernen von Konten in einer Wallet-App ist nur Ein- und Ausblenden. Ein einmal deaktiviertes Konto kann jederzeit wieder aktiviert werden — auch in einer anderen Wallet-App.

Für Bitcoin hat jedes Konto einen eigenen Ableitungspfad und damit einen separaten erweiterten öffentlichen Schlüssel (xpub). Wer eine Wallet auf einem anderen Gerät wiederherstellen will, braucht im Grundfall nur den Seed. Für fortgeschrittene Setups (Multisig, externe Tools) kann der xpub pro Konto explizit eingesehen und exportiert werden.

### Adresswiederverwendung vermeiden

Technisch kann eine Bitcoin-Adresse beliebig oft verwendet werden. Datenschutztechnisch ist das aber schlecht: Jeder, der einmal eine Zahlung an diese Adresse schickte, kann seither das vollständige Guthaben beobachten. Moderne Wallets erzeugen daher automatisch eine neue Adresse bei jedem Empfang.

### BIP-85: Deterministische Entropie für Child-Wallets

BIP-85 erweitert das HD-Wallet-Konzept: Statt nur Schlüssel abzuleiten, leitet es vollständige **Child-Seeds** ab — Entropie, die direkt als Seed für eine andere Wallet genutzt werden kann.

Das Verfahren: Die Hardware-Wallet leitet über einen anwendungsspezifischen Pfad einen Child Key ab, hasht ihn (tausende Iterationen) und gibt das Ergebnis als neue Entropie aus. Die Hash-Funktion ist eine Einwegfunktion — aus der abgeleiteten Entropie kann der übergeordnete Seed nicht rekonstruiert werden.

**Praktische Anwendung:** Die BitBoxApp nutzt BIP-85, um den Seed für die eingebettete Lightning-Wallet zu erzeugen. Der Lightning-Seed ist deterministisch aus dem Haupt-Seed abgeleitet, aber gibt diesen nicht preis. Ein einziges Backup der 24 Wörter deckt damit sowohl Cold-Storage-Wallet als auch Lightning-Wallet ab — "einheitliches Backup".

**Wiederherstellung:**
- Gerät vorhanden: BitBox02 anschliessen → Lightning-Wallet wird automatisch abgeleitet
- Neues Gerät: Seed wiederherstellen → Lightning-Wallet erneut ableitbar
- Ohne Hardware-Wallet: Open-Source-Recovery-Tool kann Lightning-Schlüssel direkt aus dem Seed ableiten

Die Schlüsseleigenschaft: Wer die Lightning-Entropie kennt, kann nicht auf den Haupt-Seed schliessen. Die Sicherheitseigenschaften der beiden Wallets bleiben unabhängig voneinander.

## Related

- [[seedphrase-entropie-und-sicherheit]]
- [[wallet-backup-strategien]]
- [[optionale-passphrase]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[opsec-und-privatsphaere]]
- [[skalierung-lightning-ark-statechains]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch

## Open Questions

- Wie verhalten sich verschiedene Ableitungspfade bei der Wallet-Migration (z.B. von Ledger zu BitBox02)?
- Gibt es Risiken, wenn eine Wallet den Ableitungspfad nicht standardkonform implementiert?
