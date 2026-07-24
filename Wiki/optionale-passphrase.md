# Optionale Passphrase (BIP-39)

**Status:** established
**Themen:** self-custody
**Last updated:** 2026-06-06
**Sources:** [[20240411_warum-backups-auf-microsd-karten-nicht-verschlüsselt-werden-sollten]], [[20250123_wie-du-backups-deiner-wallet-sicher-erstellst-und-verwahrst]], [[20231005_komplexität-ist-keine-sicherheit]], [[20230216_optionale-passphrase-vorteile-und-risiken-de]], [[20211130_bitbox-11-2021-planura-update-de]]

## Summary

Die optionale Passphrase (BIP-39) ist ein zusätzliches Wort oder ein Satz, der zur Seedphrase hinzugefügt wird und eine komplett neue Wallet ableitet. Jede Passphrase ergibt eine andere, gültige Wallet — es gibt kein falsches Ergebnis, was eine stille Plausible Deniability ermöglicht. Die Passphrase ist bewusst nicht im microSD-Backup gespeichert, da sie als zweiter unabhängiger Faktor fungiert. Sie sollte nur von Nutzern verwendet werden, die ihre Funktionsweise vollständig verstehen.

## Body

### Was die Passphrase leistet

Die Passphrase erweitert die Standard-Seedphrase (12 oder 24 Wörter) um ein weiteres Element. Das Ergebnis ist eine vollständig neue, unabhängige Wallet. Wer nur die Seedphrase hat, sieht nur die Standard-Wallet ohne Passphrase — die eigentliche Wallet bleibt unsichtbar. Dieser Mechanismus heisst Plausible Deniability: Man kann die Existenz der Passphrase-geschützten Wallet glaubhaft leugnen.

### Warum microSD-Backups nicht verschlüsselt werden

Die BitBox01 (erste Generation) speicherte Backups verschlüsselt mit einem Passwort. Das führte zu zahlreichen Support-Fällen, weil Nutzer das Passwort vergessen hatten und damit den Wallet-Zugang verloren.

Die BitBox02 löst das Problem anders: Das microSD-Backup bleibt unverschlüsselt — wie ein Papier-Backup. Die Sicherheitsebene kommt durch den physisch sicheren Aufbewahrungsort der Karte, nicht durch Verschlüsselung. Wer eine zweite Sicherheitsschicht möchte, verwendet die standardisierte Passphrase. Der entscheidende Vorteil: Die Passphrase ist BIP-39-kompatibel und mit jeder anderen kompatiblen Wallet wiederherstellbar. Eine proprietäre microSD-Verschlüsselung würde eine Abhängigkeit von einer spezifischen Implementierung schaffen.

### Risiken und Fallstricke

Die Passphrase ist das Einfachste der Welt, um sich selbst aus der Wallet auszusperren. Häufige Fehler:

- **Tippfehler:** Gross/Kleinschreibung und Leerzeichen zählen. Eine falsch aufgeschriebene Passphrase ergibt eine andere Wallet mit leerem Saldo, ohne Fehlermeldung.
- **Verlust:** Wenn die Passphrase verloren geht, gibt es keine Wiederherstellung. Sie ist bewusst nirgends gespeichert.
- **Komplexität ohne Verständnis:** Wer nicht versteht, dass jede Passphrase eine gültige Wallet erzeugt, kann seinen eigenen Fehler nicht erkennen.

Lange Passphrasen sind nicht automatisch sicherer — das Risiko, sie falsch aufzuschreiben oder zu vergessen, steigt exponentiell mit der Länge.

### Duress-Wallets (Plausible Deniability unter Druck)

Da jede Passphrase eine andere, gültige Wallet erzeugt, lassen sich mehrere Passphrasen gleichzeitig betreiben. Eine typische Konfiguration:

- **Passphrase A** → Hauptwallet mit dem echten Guthaben
- **Passphrase B** → Duress-Wallet mit einem kleineren Betrag

Im Fall eines physischen Angriffs ("5-Dollar-Wrench-Attack") oder einer Grenzkontrolle gibt man Passphrase B ein. Der Angreifer sieht eine scheinbar plausible Wallet mit echten Coins — nicht aber die eigentliche Hauptwallet. Da es keine "falsche" Passphrase gibt, kann er nicht prüfen, ob es noch eine andere Wallet gibt.

Diese Funktion ist nur wirksam, wenn die Duress-Wallet glaubwürdig aussieht (d.h. tatsächlich etwas Guthaben enthält) und wenn die eigentliche Passphrase nirgends sichtbar gespeichert ist.

### Wann sinnvoll, wann nicht

Die Passphrase ist ein Expertenwerkzeug. Eine gut konfigurierte Single-Signature Hardware-Wallet ohne Passphrase bietet bereits ein aussergewöhnlich hohes Sicherheitsniveau. Die Passphrase empfiehlt sich in spezifischen Szenarien: wenn die physische Sicherheit des Backups kompromittiert sein könnte, oder wenn Plausible Deniability gewünscht wird (z.B. bei Grenzkontrollen oder Erpressungsszenarien).

### UX-Verbesserung: Mehr Kontext bei der Aktivierung

Ab dem Planura-Update (November 2021) zeigt die BitBoxApp beim Aktivieren der optionalen Passphrase deutlich mehr Kontext — einen "Minikurs" —, der die Funktionsweise, Vor- und Nachteile klar erklärt. Hintergrund: Die Funktion hat das Potenzial, Nutzer dauerhaft aus ihrer Wallet auszusperren. Sie wird deshalb nur für fortgeschrittene Nutzer empfohlen, und die App warnt explizit, dass die Passphrase mit zusätzlichen Backup-Pflichten verbunden ist. Diese UX-Verbesserung folgt der Beobachtung, dass Nutzer die Konsequenzen der Passphrase ohne ausreichende Warnung unterschätzten.

### Backup der Passphrase

Da die Passphrase getrennt von der Seedphrase existiert, muss sie getrennt gesichert werden — aber nicht am gleichen Ort. Wer beides zusammen aufbewahrt, hat keinen zweiten Faktor mehr, sondern einen einzigen Angriffspunkt.

## Related

- [[wallet-backup-strategien]]
- [[seedphrase-entropie-und-sicherheit]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[komplexitaet-ist-keine-sicherheit]]
- [[hardware-wallet-einstieg]]
- [[bitcoin-vererbung]]

- [[bitcoins-verwahren-und-vererben|Bitcoins verwahren und vererben (Marc Steiner)]] ← Buch

## Open Questions

- Wie entwickeln sich Standards für Passphrase-Backup (z.B. getrennte Stahl-Sicherung)?
- Gibt es sinnvolle Werkzeuge zur Passphrase-Verifikation ohne Seed-Exposition?
