# Firmware-Verifikation und Reproduzierbarkeit

**Status:** established
**Themen:** self-custody, philosophie
**Last updated:** 2026-06-05
**Sources:** [[20230119_bitbox02-firmware-verifizieren-de]]

## Summary

Reproduzierbarkeit ist das Prinzip, dass jeder aus demselben Quellcode dieselbe Binärdatei kompilieren kann — und damit unabhängig überprüfen kann, dass die veröffentlichte Software nur den öffentlichen Code enthält, nichts anderes. Für Hardware-Wallets ist das ein zentrales Sicherheitsversprechen: Ohne reproduzierbare Builds müsste man dem Hersteller vertrauen, dass die Firmware keine versteckten Backdoors enthält. Die BitBox02-Firmware ist reproduzierbar, und die Verifikation ist für jeden Nutzer mit Docker durchführbar.

## Body

### Warum Reproduzierbarkeit entscheidend ist

Open-Source-Code allein reicht nicht aus. Ein Hersteller könnte den sauberen Quellcode veröffentlichen, aber eine kompromittierte Binärdatei ausliefern. Ohne reproduzierbare Builds gibt es keine Möglichkeit, das zu erkennen.

Reproduzierbarkeit schliesst diese Lücke: Wenn andere unabhängig aus demselben Code dieselbe Binärdatei erstellen und die Hashes übereinstimmen, gibt es keine Manipulation. Diese Eigenschaft ist auch in der Kryptografieforschung fundamental — Vertrauen setzt unabhängige Überprüfbarkeit voraus.

### Verifikation der BitBox02-Firmware

Die Schritte im Überblick:

1. **Docker installieren.** Die Kompilierung läuft in einem isolierten Docker-Container, um identische Build-Umgebungen zu garantieren.
2. **Quellcode herunterladen.** Das Firmware-Repository von GitHub als ZIP herunterladen und entpacken.
3. **Kompilieren.** Im Verzeichnis `releases/` den Build-Befehl ausführen:
   - Bitcoin-only: `./build.sh firmware-btc-only/v9.13.1 "make firmware-btc"`
   - Multi-Edition: `./build.sh firmware/v9.13.1 "make firmware"`
4. **Hash berechnen.** Mit `shasum -a 256` den SHA-256-Hash der kompilierten Binärdatei berechnen.
5. **Vergleichen.** Die offizielle Signatur-Datei mit `./describe_signed_firmware.py` auslesen und den Hash vergleichen. Stimmen beide überein, ist die Firmware identisch mit dem öffentlichen Code.

Zusätzlich kann die BitBox02 so konfiguriert werden, dass sie den Firmware-Hash beim Einschalten anzeigt — ein weiterer direkter Vergleichspunkt.

### Community-Bestätigungen

BitBox pflegt im GitHub-Repository eine Liste unabhängiger Community-Bestätigungen: Nutzer, die die Firmware erfolgreich reproduziert haben, können ihre GPG-signierten Bestätigungen einreichen. Das schafft ein dezentrales Netz unabhängiger Verifikationen — ähnlich wie Nodes im Bitcoin-Netzwerk Konsensregeln unabhängig durchsetzen.

### Einordnung

Reproduzierbarkeit allein ist kein vollständiger Schutz. Sie beantwortet die Frage: "Stimmt die Binärdatei mit dem Code überein?" Nicht beantwortet wird: "Ist der Code selbst sicher?" Dafür braucht es Code-Audits und formale Verifikation. Reproduzierbarkeit ist eine notwendige, aber nicht hinreichende Bedingung für sicherheitskritische Software.

Die BitBox02-Firmware kombiniert Reproduzierbarkeit mit Open-Source-Code und externen Sicherheitsaudits.

## Related

- [[anti-klepto-und-supply-chain-sicherheit]]
- [[hardware-wallet-sicherheitsarchitektur]]
- [[bitcoin-only-vs-multi-edition]]
- [[specter-diy]]
- [[bitbox02-features]]

- [[bitcoin-development-philosophy|Bitcoin Development Philosophy (Kalle & Linnea Rosenbaum)]] ← Buch

## Open Questions

- Wie viele unabhängige Nutzer bestätigen aktiv jedes Release?
- Gibt es automatisierte Verifikations-Tools, die den Prozess für Nicht-Entwickler vereinfachen?
