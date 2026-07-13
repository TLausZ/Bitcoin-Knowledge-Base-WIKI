# Bitcoin-Adresstypen

**Status:** established
**Themen:** grundlagen, protokoll, self-custody
**Last updated:** 2026-06-06
**Sources:** [[20211021_was-sind-bitcoin-adressen-de]], [[20220331_bitbox-03-2022-glaernisch-update-de]], [[20220118_bitbox-01-2022-maighels-update-de]]

## Summary

Bitcoin kennt vier Adresstypen, die historisch nacheinander eingeführt wurden. Alle sind interoperabel — du kannst Bitcoin von jedem Typ an jeden anderen senden. Der Standard hat sich von Legacy (teuer, alt) über P2SH zu Native SegWit (günstigster Standardtyp) und schließlich Taproot (beste Privatsphäre bei komplexen Transaktionen) entwickelt. Ein einziger Seed erzeugt alle Typen.

## Body

### Warum es mehrere Adresstypen gibt

Bitcoin begann 2009 mit einem einfachen Adressformat. Mit wachsender Nutzung entstanden neue Typen, die Transaktionsgrößen — und damit Gebühren — reduzierten und neue Funktionen wie komplexe Ausgabebedingungen und bessere Privatsphäre ermöglichten.

Wichtig: Alle Adressen in einer Wallet werden vom selben Seed abgeleitet. Kein neuer Seed nötig für neue Adresstypen. Wallets wie die BitBox02 speichern alle Typen in einem einzigen "Unified Account".

### Legacy-Adressen (P2PKH)

**Erkennungszeichen:** beginnen mit `1`  
**Beispiel:** `15e15hWo6CShMgbAfo8c2Ykj4C6BLq6Not`

P2PKH (Pay-to-Public-Key-Hash) ist der ursprüngliche Typ aus 2009. Eine Legacy-Adresse ist der Hash des öffentlichen Schlüssels. Sie verbraucht den meisten Platz in einer Transaktion und ist damit der teuerste Typ. Es gibt keinen guten Grund mehr, neue Legacy-Adressen zu verwenden — die neueren Typen sind in jeder Hinsicht besser. Hauptgrund für ihren Verbleib: ältere Wallets, die neuere Formate noch nicht unterstützen.

### Pay-to-Script-Hash (P2SH)

**Erkennungszeichen:** beginnen mit `3`  
**Beispiel:** `35PBEaofpUeH8VnnNSorM1QZsadrZoQp4N`

P2SH enthält nicht den Hash des öffentlichen Schlüssels, sondern den Hash eines Ausgabe-Scripts mit beliebigen Bedingungen — einfach (nur ein Schlüssel darf ausgeben) oder komplex (Multisig, Zeitsperre). Die Bedingungen bleiben dem Absender zunächst verborgen; sie werden nur beim Ausgeben offengelegt. P2SH-Adressen können auch SegWit nutzen (wrapped SegWit). Etwa **26 % günstiger** als Legacy.

### Natives SegWit (P2WPKH / Bech32)

**Erkennungszeichen:** beginnen mit `bc1q`  
**Beispiel:** `bc1q42lja79elem0anu8q8s3h2n687re9jax556pcc`

Native SegWit trennt Signatur und Script vom Transaktionskörper (Witness) — weniger Daten on-chain. Über **38 % günstiger** als Legacy, weitere **16 % günstiger** als P2SH. Aktuell der häufigste Standard und die Standardeinstellung der BitBoxApp. Einige Börsen unterstützen Bech32 noch nicht und verlangen P2SH als Ausweichoption.

### Taproot (P2TR / Bech32m)

**Erkennungszeichen:** beginnen mit `bc1p`  
**Beispiel:** `bc1pmzfrwwndsqmk5yh69yjr5lfgfg4ev8c0tsc06e`

Taproot wurde im November 2021 als Soft Fork aktiviert (Block 709.632). Es kombiniert Schnorr-Signaturen, MAST und Tapscript. Einfache Taproot-Transaktionen sind geringfügig größer als Native SegWit (gebunden an öffentliche Schlüssel statt Public-Key-Hashes), aber bei komplexen Transaktionen (Multisig, Lightning, Vaults) deutlich günstiger und privater: alle Ausgabewege sehen on-chain gleich aus.

Hardware-Wallet-Rollout am Beispiel BitBox02: Senden an bc1p-Adressen ab Januar 2022 (Maighels-Update), Empfangen auf bc1p-Adressen ab März 2022 (Glärnisch-Update, Firmware v9.10.0). Native SegWit blieb der Standard, da viele Wallets Taproot noch nicht unterstützten.

### Zusammenfassung

| Typ | Präfix | Einsparung vs. Legacy | Einführung |
|-----|--------|----------------------|------------|
| Legacy (P2PKH) | `1` | — | 2009 |
| P2SH | `3` | ~26 % | 2012 |
| Native SegWit (P2WPKH) | `bc1q` | ~38 % | 2017 (BIP-141) |
| Taproot (P2TR) | `bc1p` | ähnlich wie SegWit (besser bei komplex) | 2021 |

**Empfehlung:** Native SegWit (`bc1q`) für den Alltag — breiteste Kompatibilität und niedrigste Gebühren bei einfachen Transaktionen. Taproot (`bc1p`) dort, wo Privatsphäre oder komplexe Skripte entscheidend sind.

## Related

- [[taproot-musig2-frost]]
- [[segregated-witness-segwit]]
- [[hd-wallets-und-schluesselableitung]]
- [[utxo-modell-und-konsolidierung]]

## Open Questions

- Wann wird Taproot zum neuen Standard in gängigen Wallets und auf Börsen?
- Wie entwickelt sich die Adoption angesichts von Anti-Klepto-Anforderungen für Schnorr-Signaturen?
