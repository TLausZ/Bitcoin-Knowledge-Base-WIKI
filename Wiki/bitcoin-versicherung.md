# Bitcoin-Versicherung für Selbstverwahrung

**Status:** emerging
**Themen:** oekonomie, self-custody
**Last updated:** 2026-06-08
**Sources:** [[20240208_die-erste-versicherung-für-deine-eigenen-bitcoin]], [[20240208_bitbox-02-2024-fletschhorn-update]]

## Summary

Bitsurance ist die erste Versicherung speziell für selbst verwahrte Bitcoin. Sie deckt physische Risiken ab — Raub, Einbruch, Feuer, Erpressung, Naturkatastrophen — die durch Technologie allein nicht addressiert werden können. Die Versicherung erfordert keine Weitergabe privater Schlüssel und ergänzt die digitale Sicherheit einer Hardware-Wallet durch Absicherung gegen analoge Bedrohungen.

## Body

### Das Lücke zwischen digitaler und physischer Sicherheit

Eine Hardware-Wallet schützt gegen digitale Angriffe: Malware, Phishing, Remote-Zugriff, kompromittierte Netzwerke. Gegen physische Bedrohungen bietet sie keinen Schutz. Ein Räuber, der die Hardware-Wallet und das Backup kennt, lässt sich nicht durch Kryptographie abhalten. Fortgeschrittene Lösungen (geografisch verteilte Backups, Multisig mit Notaren) sind wirksam, aber komplex — sie erhöhen die Anforderungen an den Nutzer erheblich.

Eine Versicherung schliesst diese Lücke ohne zusätzliche technische Komplexität.

### Was Bitsurance versichert

- Raub, Einbruch, Vandalismus
- Erpressung (inkl. "$5-Wrench-Attack" — physischer Zwang zur Herausgabe des Seeds)
- Feuer, Wasser, Blitzschlag
- Naturkatastrophen (Erdbeben, Lawinen, Überschwemmungen)

Versichert sind die BitBox02 und die darauf gesicherten Bitcoin. Keine privaten Schlüssel werden weitergegeben — die Versicherung deckt finanzielle Verluste ab wie jede andere Sachversicherung.

### Kein Custody-Risiko

Der entscheidende Unterschied zur Verwahrung bei einer Börse: Der Versicherer hat keinen Zugriff auf die Coins. Wenn ein Schadensfall eintritt, zahlt Bitsurance Fiat-Wert, ohne dass ein privater Schlüssel enthüllt wird. Die Versicherungsbeziehung erzeugt kein Gegenparteirisiko auf die Coins selbst.

### Integration in die BitBoxApp

Die Bitsurance-Partnerschaft wurde mit dem Fletschhorn-Update (Februar 2024) angekündigt und direkt in die BitBoxApp integriert. Keine Datenweitergabe an Bitsurance ohne aktive Anmeldung des Nutzers. Der Abschluss läuft über ein sicheres Web-Widget in der App.

Erstmals verfügbar für Deutschland, danach Schweiz, Österreich, weiteres Europa.

### Einordnung

Bitsurance ist kein Ersatz für gute Sicherheitspraktiken (sichere Backups, geografische Verteilung, OpSec). Es ist eine zusätzliche Ebene für Nutzer, für die physische Risiken ein relevantes Bedrohungsmodell darstellen. Besonders relevant bei höheren Beständen, wenn das Risiko physischer Zwangsmassnahmen realistischer wird.

## Related

- [[hardware-wallet-sicherheitsarchitektur]]
- [[opsec-und-privatsphaere]]
- [[wallet-backup-strategien]]
- [[komplexitaet-ist-keine-sicherheit]]

## Open Questions

- Wie entwickelt sich der Markt für Bitcoin-Selbstverwahrungsversicherungen in Europa?
- Welche Nachweisanforderungen stellt Bitsurance im Schadensfall (ohne private Schlüssel zu enthüllen)?
