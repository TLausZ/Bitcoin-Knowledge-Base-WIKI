# Miniscript und zeitlich gesperrte Wiederherstellungsschlüssel

**Status:** established
**Themen:** protokoll, self-custody, philosophie, wallets
**Last updated:** 2026-07-05
**Sources:** [[20231109_erkunde-bitcoin-miniscript-mit-liana-und-der-bitbox02]], [[20241023_bitbox-10-2024-lugano-update]], [[20230323_bitcoin-miniscript-verstehen-teil-3]], [[20230302_bitcoin-miniscript-verstehen-teil-2-de]], [[20230216_bitcoin-miniscript-verstehen-teil-1-de]], [[20260315_heartmoney-ein-tag-der-alles-verandert]]

## Summary

Miniscript ist eine strukturierte Sprache für Bitcoin-Script, die komplexe Ausgabebedingungen vereinfacht. Eine besonders nützliche Anwendung sind zeitlich gesperrte Wiederherstellungsschlüssel: Ein Backup-Schlüssel, der erst nach einer definierten Zeit (z.B. 2 Jahre) ausgeben kann, kann an vertrauenswürdige Personen weitergegeben werden, ohne Diebstahlrisiko. Die Wallet Liana implementiert dieses Konzept mit BitBox02-Integration.

## Body

### Das Problem mit mehreren Backups

Mehrere Backups erhöhen die Redundanz, aber auch das Risiko, dass ein Backup gefunden und gestohlen wird. Jedes Backup gibt sofortigen vollständigen Zugriff auf alle Coins. Einem Freund ein Backup anzuvertrauen ist potenziell gefährlich.

### Zeitlich gesperrte Wiederherstellungsschlüssel

Mit Miniscript kann ein Backup-Schlüssel erstellt werden, der erst nach einem definierten Zeitraum ausgeben kann. Der Nutzer:
- Hält den primären Schlüssel (kann jederzeit ausgeben)
- Verteilt Backup-Schlüssel an Vertrauenspersonen oder lagert sie entfernt
- Backup-Schlüssel können die Coins erst nach Ablauf der Zeitsperre ausgeben

Falls der primäre Schlüssel verloren geht, wartet man bis die Zeitsperre abläuft und holt dann einen Backup-Schlüssel zurück.

**Mehrere Backup-Schlüssel mit unterschiedlichen Sperrzeiten** sind möglich — z.B. ein Backup bei einem Notar (3 Jahre) und eines bei einem Familienmitglied (1 Jahr).

### Zeitbeschränkungen zurücksetzen

Die Zeitbeschränkung ist an das Datum der letzten Einzahlung gebunden. Um zu verhindern, dass die Backup-Schlüssel irgendwann ausgeben könnten, muss das Guthaben vor Ablauf der Zeitsperre durch eine Refresh-Transaktion (an sich selbst) neu gestellt werden. Liana warnt rechtzeitig davor.

### Wallet-Deskriptor

Komplexe Wallets werden durch einen **Wallet-Deskriptor** beschrieben — eine Datei, die alle Schlüssel und Ausgabebedingungen enthält. Der Deskriptor muss Teil aller Backups sein; ohne ihn ist die Wallet nicht wiederherstellbar. Er enthält keine privaten Schlüssel, aber alle öffentlichen Schlüssel — wer den Deskriptor hat, kann Guthaben und Transaktionshistorie einsehen.

### MiniTapscript

Mit dem Lugano-Update (Oktober 2024) unterstützt die BitBox02 **MiniTapscript** — Miniscript auf Taproot. Durch Taproot wird beim Ausgeben nur der tatsächlich verwendete Pfad offengelegt. Bei Standardausgaben über den primären Schlüssel sieht die Transaktion aus wie jede normale Taproot-Transaktion → bessere Privatsphäre und geringere Gebühren bei komplexen Setups.

### Technische Grundlage: Parser und Typsystem

Miniscript hat ein formales Typsystem, das jeden Ausdruck klassifiziert: **B** (Base, eigenständiger Script-Ausdruck), **V** (Verify, muss in Verify-Kontext stehen), **K** (Key, gibt Schlüssel zurück), **W** (Wrapped, zweites Element in and_v). Modifier wie `z` (zero-arg) oder `d` (dissatisfiable) kommen hinzu. Diese Regeln ermöglichen automatische Validierung und Kompilierung.

Ein Miniscript-Parser kann alle möglichen Spending Conditions eines Ausdrucks extrahieren — ohne die Logik manuell zu analysieren. Für `thresh(2, pk(A), pk(B), pk(C))` erkennt der Parser automatisch alle sechs möglichen 2-von-3-Kombinationen. Zeitbasierte Bedingungen (Timelocks) erscheinen als eigene Pfade mit Aktivierungszeitpunkt.

Diese maschinenlesbare Analyse ist die Grundlage dafür, dass Wallet-Software wie Liana die relevanten Informationen — welche Schlüssel jetzt ausgeben können, welche erst nach Zeitsperre — zuverlässig anzeigen kann.

### Liana Wallet

[Liana](https://wizardsardine.com/liana/) (von Wizardsardine) implementiert Miniscript-Wallets mit zeitlich gesperrten Wiederherstellungsschlüsseln. Kompatibel mit der BitBox02. Erfordert eine eigene Bitcoin-Node.

### Ankunft in der Community-Praxis (2026)

Liana wird inzwischen auf deutschsprachigen Community-Events in Workshops vermittelt (dokumentiert: Les-Femmes-Orange-Event München, März 2026). Der dort betonte Anwendungsfall ist die Vererbung: Der Besitzer gibt jederzeit selbst aus; stirbt er oder verliert den Zugriff, übernimmt nach Ablauf des Timelocks ein zuvor definierter zweiter Schlüssel. Damit adressiert ein einziges Setup die zwei grössten Selbstverwahrungsrisiken, eigenen Zugangsverlust und die Weitergabe im Erbfall — die Vermittlung folgt also genau der Backup-Logik dieses Artikels, verpackt sie aber als Nachlassplanung. Als Kombination wird Liana (regelt, wer wann zugreifen kann) plus Hardware-Wallet (schützt die Schlüssel) empfohlen. Praktische Hürde neben der Node-Anforderung: Die Software gab es Anfang 2026 nur auf Englisch; die Übersetzung lief. [[20260315_heartmoney-ein-tag-der-alles-verandert]]

## Related

- [[multisig-und-kollaborative-verwahrung]]
- [[bitcoin-covenants]]
- [[wallet-backup-strategien]]
- [[bitcoin-etf-und-institutionelle-verwahrung]]
- [[nunchuk-wallet]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie entwickelt sich die Nutzung von Liana und ähnlichen Wallets in der Praxis?
- Wann vereinfacht sich die Node-Anforderung für Endnutzer?
