# Komplexität ist keine Sicherheit

**Status:** established
**Last updated:** 2026-06-05
**Sources:** [[20231005_komplexitaet-ist-keine-sicherheit]]

## Summary

Ab einem bestimmten Punkt erhöht mehr Sicherheitskomplexität nicht die Sicherheit — sie erhöht das Risiko, die eigenen Coins zu verlieren. Eine gut konfigurierte Single-Signature Hardware-Wallet bietet bereits ein außergewöhnlich hohes Sicherheitsniveau. Multisig, Passphrasen und andere Expertenfunktionen sind sinnvoll, wenn man sie vollständig versteht — aber gefährlich, wenn nicht.

## Body

### Das Sicherheits-Paradoxon der Selbstverwahrung

Die übliche Annahme: Mehr Sicherheitsschichten = mehr Sicherheit. In der Bitcoin-Selbstverwahrung gilt das nur bis zu einem Punkt. Danach dreht sich die Kurve: Jede zusätzliche Schicht erhöht die Wahrscheinlichkeit, den Zugang zu verlieren.

Konkrete Beispiele:
- Eine sehr lange Passphrase — jeder Tippfehler erzeugt eine andere Wallet. Das Risiko eines Fehlers beim Aufschreiben oder Eintippen steigt mit der Länge.
- Multisig ohne tiefes Verständnis — wer den Wallet-Deskriptor oder den xpub eines Cosigners verliert, ist ausgesperrt. Kein Angreifer nötig.

### Der Sweet Spot

Hardware-Wallets lösen das klassische Spannungsverhältnis zwischen Sicherheit und Benutzerfreundlichkeit: Der private Schlüssel verlässt das Gerät nie, Transaktionen werden auf einem verifizierbaren Display bestätigt. Eine Single-Signature Hardware-Wallet mit sauberem Backup ist bereits auf einem Sicherheitsniveau, das die meisten Bedrohungsmodelle abdeckt.

Fortgeschrittene Setups (Multisig, Passphrase, Air-Gap) sind dann sinnvoll, wenn das Bedrohungsmodell es erfordert und man die Mechanismen vollständig versteht — einschließlich aller Verlustrisiken.

### Komplexität als Eintrittsbarriere

Anfänger werden oft zu komplexen Setups gedrängt — mit gut gemeinter Absicht, aber kontraproduktivem Ergebnis. Wer sich aus der eigenen Wallet aussperrt oder frustriert aufgibt und zurück zur Börse wechselt, ist schlechter dran als mit einer einfachen, gut verwahrten Hardware-Wallet.

Expertenfunktionen wie Multisig oder Passphrasen sind als opt-in gedacht, nicht als Standard. Der richtige Zeitpunkt dafür ist, wenn man versteht, was bei einem Fehler passiert — und wie man ihn vermeidet.

### Simplicity is security

Die intuitive Schlussfolgerung ist umgekehrt: Einfachheit ist Sicherheit. Ein Setup, das man vollständig versteht und korrekt ausführen kann, ist sicherer als ein komplexes Setup mit versteckten Fallstricken.

## Related

- [[optionale-passphrase]]
- [[multisig-und-kollaborative-verwahrung]]
- [[wallet-backup-strategien]]
- [[hardware-wallet-sicherheitsarchitektur]]

## Open Questions

- Wie kommuniziert man Komplexitätsrisiken effektiv an Einsteiger, ohne sie zu entmutigen?
- Ab welchem Vermögenswert rechtfertigt ein erweitertes Bedrohungsmodell ein komplexeres Setup?
