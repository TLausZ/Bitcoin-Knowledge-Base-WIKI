# Bitcoin Vaults

**Status:** emerging
**Themen:** protokoll, self-custody, lightning
**Last updated:** 2026-06-04
**Sources:** [[20260409_wie-bitcoin-vaults-komfort-mit-sicherheit-verbinden]]

## Summary

Ein Bitcoin Vault ist ein Wallet-Setup, das Auszahlungen verzögert und einen separaten Wiederherstellungspfad vorsieht. Statt Coins sofort ausgeben zu können, startet eine Auszahlung einen Countdown — in dieser Zeit kann der Besitzer die Transaktion noch abbrechen und die Coins in ein sichereres Setup umleiten. Vaults verbessern so die Balance zwischen Alltagskomfort und Hochsicherheit, sind heute aber noch weitgehend auf Covenants angewiesen, die noch nicht in Bitcoin implementiert sind.

## Body

### Das Grunddesign

Ein typischer Bitcoin Vault hat drei Bestandteile:

- **Der Vault selbst:** Die Coins liegen in einem Wallet mit vordefinierten Ausgabebedingungen
- **Auszahlungspfad:** Öffnet den Vault und startet einen Countdown (z.B. 24 Stunden)
- **Wiederherstellungspfad:** Kann jede laufende Auszahlung abbrechen und die Coins in ein sichereres Setup umleiten

Der Schlüssel: Auszahlungspfad und Wiederherstellungspfad können sehr **unterschiedliche Setups** sein. Beispiel: Der Auszahlungspfad nutzt eine einzelne Hardware-Wallet für den Alltag; der Wiederherstellungspfad ist ein 3-von-5-Multisig mit Backups an verschiedenen geografischen Orten.

### Warum das sinnvoll ist

Ein Angreifer, der Zugang zur einfachen Alltagswallet erlangt, kann die Coins nicht sofort stehlen — er müsste den Countdown abwarten. In dieser Zeit kann der legitime Besitzer die Auszahlung über den Wiederherstellungspfad stoppen.

Umgekehrt kann der Besitzer für alltägliche Zahlungen den bequemen Auszahlungspfad nutzen, ohne jedes Mal auf die hochsichere (aber umständliche) Multisig-Konfiguration zurückgreifen zu müssen.

### Kompromisse

**Nachteile:**
- **Überwachung:** Der Countdown hilft nur, wenn der Besitzer den Vorgang rechtzeitig bemerkt
- **Verzögerung:** Legitime Zahlungen dauern länger — die Wartezeit muss eingeplant werden
- **Mehrere Transaktionen:** Jede Auszahlung erfordert mindestens zwei On-Chain-Transaktionen (höhere Gebühren)

**Wann sinnvoll:** Vor allem für Bitcoin, die selten bewegt werden, aber trotzdem nutzbar bleiben sollen — langfristige Ersparnisse, Unternehmensreserven, Familienvermögen, Vererbungsplanung.

### Technische Voraussetzung: Covenants

Bitcoin unterstützt bereits Multisig und Timelocks. Vollständige Vaults brauchen aber mehr: Sie müssen einschränken, **wohin** Coins als nächstes bewegt werden dürfen — nicht nur wann. Dafür sind **Covenants** nötig: Ausgabebedingungen, die Teile einer zukünftigen Transaktion einschränken.

Covenant-Vorschläge für Bitcoin (z.B. CTV, CheckTXHashVerify) sind zum Zeitpunkt des Schreibens noch in der Diskussionsphase. Native Bitcoin Vaults sind daher vorerst eine spannende Idee für die Zukunft. Eingeschränkte Vault-ähnliche Setups sind heute mit vorab signierten Transaktionen und Miniscript möglich.

## Related

- [[skalierung-lightning-ark-statechains]]
- [[taproot-musig2-frost]]
- [[multisig-und-kollaborative-verwahrung]]
- [[bitcoin-covenants]]

## Open Questions

- Werden Covenants (CTV oder ähnliche Proposals) in Bitcoin aktiviert? Wann?
- Welche bestehenden Tools (Miniscript, Liana) können Vault-ähnliche Setups heute schon umsetzen?
