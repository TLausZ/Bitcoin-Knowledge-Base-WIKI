# UTXO-Modell und UTXO-Konsolidierung

**Status:** established
**Themen:** privacy
**Last updated:** 2026-06-19
**Sources:** [[20231207_utxo-konsolidierung-bitcoin-gebühren-senken]], [[20210804_was-ist-eigentlich-eine-utxo-de]], [[learnmeabitcoin-beginners-guide-outputs]], [[learnmeabitcoin-beginners-guide-transactions]]

## Summary

Bitcoin verwendet das UTXO-Modell (Unspent Transaction Outputs): Jede Transaktion verbraucht bestehende UTXOs als Inputs und erzeugt neue als Outputs. Transaktionsgebühren hängen direkt von der Anzahl der Inputs ab — wer viele kleine UTXOs hat, zahlt mehr. UTXO-Konsolidierung (Zusammenfassen vieler kleiner UTXOs in wenige grössere) spart zukünftige Gebühren, wenn in Zeiten niedriger Gebühren durchgeführt.

## Body

### Das UTXO-Modell

Bitcoin ähnelt in einem entscheidenden Aspekt eher Bargeld als einem Bankkonto: Eine Wallet fasst empfangene Bitcoin nicht zu einer einzigen Summe zusammen, sondern bewahrt jede eingehende Transaktion separat auf. Jede dieser Einheiten ist ein UTXO — ein "Geldschein" in einem fixen Wert, der der exakten Höhe der eingegangenen Transaktion entspricht.

Jede Transaktion besteht aus:
- **Inputs:** UTXOs (Geldscheine), die ausgegeben werden
- **Outputs:** Neue UTXOs, die entstehen — inkl. Wechselgeld-Output zurück an den Sender

Jeder UTXO hat einen festen Wert, ist an eine Bitcoin-Adresse gebunden und wird durch eine Transaktions-ID eindeutig identifiziert.

### Wie Transaktionsgebühren berechnet werden

`Gebühr = Transaktionsgrösse × Gebührensatz (sat/vByte)`

Die Transaktionsgrösse hängt von der **Anzahl der Inputs** ab. Mehr Inputs = grössere Transaktion = höhere Gebühren. Wer monatlich Bitcoin via DCA kauft, sammelt über Zeit viele kleine UTXOs an — alle zukünftigen Ausgaben werden dadurch teurer.

### Was ist UTXO-Konsolidierung?

Konsolidierung = viele kleine UTXOs in einer Transaktion an sich selbst zusammenfassen → wenige grosse UTXOs entstehen.

**Wann sinnvoll:** In Zeiten niedriger Gebühren (z.B. Wochenenden, Nebensaison) konsolidieren → bei späteren Ausgaben in Hochgebühren-Phasen profitieren, weil weniger Inputs benötigt werden.

Die Konsolidierung selbst kostet Gebühren — aber wenn in einer Phase mit niedrigen Gebühren konsolidiert wird, können die Einsparungen bei späteren Ausgaben diese Kosten leicht übertreffen.

### Privatsphäre-Kompromiss

Alle Inputs einer Konsolidierungstransaktion werden miteinander verknüpft — ein Beobachter kann schliessen, dass alle diese Adressen zum selben Nutzer gehören. Deshalb:

- UTXOs aus verschiedenen Quellen (KYC-Börse vs. KYC-freier Kauf) **separat halten**
- Verschiedene Konten in der BitBoxApp für verschiedene Quellen verwenden

### Coin Control in der BitBoxApp

Über die erweiterte Einstellung „Coin Control" können in der BitBoxApp einzelne UTXOs für eine Transaktion manuell ausgewählt werden. Das ermöglicht gezielte Konsolidierung und bessere Kontrolle über die Privatsphäre.

## Related

- [[coinjoin-und-on-chain-privatsphaere]]
- [[coin-control-und-utxo-auswahl]]
- [[opsec-und-privatsphaere]]
- [[konsensregeln-und-mempool-richtlinien]]

- [[mastering-bitcoin|Mastering Bitcoin (Antonopoulos/Harding)]] ← Buch

## Open Questions

- Wie entwickeln sich Gebühren langfristig, wenn die Block-Subsidy sinkt?
- Welche Wallet-Tools automatisieren UTXO-Management in Zukunft?
