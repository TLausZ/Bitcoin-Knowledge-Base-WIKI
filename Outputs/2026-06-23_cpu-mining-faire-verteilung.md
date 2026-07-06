# Warum waren CPUs entscheidend für eine faire Verteilung der Bitcoin?

**Datum:** 2026-06-23
**Quelle der Frage:** Kommentar zum LinkedIn-Artikel «Woher kamen die 10'000 BTC für zwei Pizzen?»
**Relevante RAW-Quelle:** [[linkedin-Woher kamen die 10000 BTC für zwei Pizzen]]

---

## Frage

Warum waren CPUs entscheidend für eine möglichst faire Verteilung der Bitcoin — und was war mit «fairer Verteilung» überhaupt gemeint?

---

## Antwort

### Was Satoshi mit «fairer Verteilung» meinte

Satoshi verwendete den Begriff für zwei Dinge gleichzeitig: die Verteilung der Coins *und* die Verteilung der Rechenleistung (Hashrate). Beides ist untrennbar verknüpft, weil Mining-Rewards direkt proportional zur eingesetzten Hashrate anfallen — wer mehr Hashrate kontrolliert, bekommt mehr Coins.

Im Bitcoin-Whitepaper steht das Grundprinzip explizit: «one CPU, one vote.» Das Ziel war ein System, an dem möglichst viele Menschen gleichberechtigt teilnehmen können, ohne dass einzelne Akteure einen strukturellen Vorteil haben. Niemand sollte durch bessere Hardware unverhältnismässig viele Coins akkumulieren können.

### Warum CPUs das ermöglichten

Mit einer CPU kann jeder mitmachen, der einen normalen Computer besitzt. Die Hardware ist günstig, überall erhältlich, und die Leistungsunterschiede zwischen den Geräten sind begrenzt. Das Spielfeld ist im Wesentlichen eben.

GPUs kippten genau das. Sie sind für parallele Berechnungen gebaut und beim SHA-256-Hashing (dem Bitcoin-Mining-Algorithmus) etwa 50–100x schneller als CPUs. Laszlo Hanyecz demonstrierte das eindrücklich: Mit seinem GPU-Setup häufte er zwischen April und November 2010 über 81'000 BTC an — fast im Alleingang.

### Das eigentliche Sicherheitsproblem dahinter

Neben der ungleichen Coin-Verteilung gibt es ein strukturelles Netzwerkrisiko: Wer mehr als 50% der gesamten Hashrate kontrolliert, kann Transaktionen zensieren oder doppelt ausgeben (sogenannter 51%-Angriff). Satoshi wollte das Netzwerk so breit verteilt halten, dass kein Einzelner diese Schwelle je realistisch erreicht. CPU-Mining war der Mechanismus dafür — nicht weil CPUs technisch besser sind, sondern weil sie Rechenleistung demokratisieren.

### Die Ironie im Fall Laszlo

Laszlo hatte mit seinem GPU-Miner genau das Problem geschaffen, das Satoshi verhindern wollte. Deshalb kontaktierte Satoshi ihn privat. Und deshalb fühlte Laszlo sich «schuldig», das Projekt zu verschlechtern. Seine Pizza-Käufe und die übrigen ~100'000 BTC, die er 2010 ausgab, waren kein Leichtsinn — sondern der Versuch, Coins aktiv zurück in Umlauf zu bringen und den Schaden zu begrenzen, den seine eigene Erfindung angerichtet hatte.

---

## Offene Fragen

- Hat Satoshis Warnung an Laszlo das GPU-Mining wirklich verzögert — oder hätte es sich ohnehin durchgesetzt?
- Wann genau begann die Gemeinschaft, GPU-Mining als Standard zu akzeptieren, und wie reagierte Satoshi darauf öffentlich?
- Inwiefern beeinflusste diese frühe Erfahrung spätere Proof-of-Work-Algorithmen (z. B. Scrypt bei Litecoin), die explizit GPU-resistent sein sollten?
