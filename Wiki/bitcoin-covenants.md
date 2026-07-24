# Bitcoin Covenants

**Status:** emerging
**Themen:** protokoll, self-custody
**Last updated:** 2026-06-04
**Sources:** [[20240229_was-sind-bitcoin-covenants-ctv-und-checktxhashverify]], [[20260409_wie-bitcoin-vaults-komfort-mit-sicherheit-verbinden]]

## Summary

Covenants sind Ausgabebedingungen in Bitcoin-Transaktionen, die nicht nur einschränken, *ob* Coins ausgegeben werden dürfen, sondern auch *wohin* sie als nächstes fliessen können. Die beiden wichtigsten Vorschläge sind Check Template Verify (CTV) und CheckTXHashVerify. Sie sind noch nicht in Bitcoin aktiviert, würden aber wichtige neue Anwendungen ermöglichen: Vaults, Congestion-Control und Kanal-Fabriken für Lightning.

## Body

### Das Grundprinzip

In herkömmlichem Bitcoin-Script legen Ausgabebedingungen fest, wer Coins ausgeben darf (privater Schlüssel, Multisig, Zeitsperre). Sobald die Bedingung erfüllt ist, können die Coins an beliebige Adressen gesendet werden.

Covenants gehen weiter: Sie schränken ein, **wohin** Bitcoin nach der Ausgabe fliessen können — ähnlich wie ein physischer Vertrag, der vorschreibt, an wen eine Immobilie weiterverkauft werden darf.

### Check Template Verify (CTV)

CTV (BIP-119) erlaubt Ausgabebedingungen, die prüfen, ob die Transaktionsdaten mit einem vorberechneten Hash übereinstimmen. Die Hash-Eingabe umfasst: Inputs, Outputs, Version, Locktime. All das muss beim Erstellen der Adresse bereits feststehen.

Eine CTV-Adresse kann sich also nur auf diese vorberechneten Transaktionen festlegen. Keine rekursiven Covenants möglich.

### CheckTXHashVerify

Ähnlich wie CTV, aber flexibler: Es können selektiv nur bestimmte Teile der Transaktion festgelegt werden (z.B. nur die Empfänger, oder nur die Anzahl der Inputs), andere bleiben frei wählbar.

### Anwendungen

**Vaults:** Coins können nur an eine vorherbestimmte Zwischenadresse gesendet werden, die mit einer Zeitsperre versehen ist. Während der Zeitsperre kann ein Rückruf an die Cold-Storage-Adresse erfolgen. Böswillige Transaktionen können innerhalb eines Zeitfensters „storniert" werden.

**Congestion-Control:** Eine Börse sendet bei hohen Gebühren eine günstige Transaktion mit einem einzigen Output, die sich dazu verpflichtet, später viele Auszahlungen durchzuführen. Günstig heute, Auszahlung bei niedrigeren Gebühren.

**Kanal-Fabriken:** Mehrere Parteien können in einer einzigen On-Chain-Transaktion mehrere Lightning-Kanäle eröffnen, ohne für jeden Kanal eine separate Transaktion zu senden.

### Aktueller Stand

Covenants sind zum Zeitpunkt dieses Artikels Vorschläge ohne konkreten Aktivierungsplan. Sie wären ein Soft Fork. CTV und CheckTXHashVerify ermöglichen keine rekursiven Covenants — ein wichtiger Aspekt für die Community-Diskussion.

## Related

- [[bitcoin-vaults]]
- [[soft-fork-und-hard-fork]]
- [[skalierung-lightning-ark-statechains]]
- [[bitcoin-whitepaper-errata]] ← warum Encumbrances Signatur-Abdeckung brauchen (P2SH-Vorgeschichte)
- [[miniscript-und-liana]]

## Open Questions

- Welcher Covenant-Vorschlag wird aktiviert werden? CTV, CheckTXHashVerify, oder ein anderer?
- Wie lange dauert der Aktivierungsprozess?
- Welche weiteren Anwendungen entstehen durch rekursive vs. nicht-rekursive Covenants?
