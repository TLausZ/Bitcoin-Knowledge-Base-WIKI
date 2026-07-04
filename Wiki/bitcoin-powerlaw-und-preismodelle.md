# Bitcoin Power Law und Preismodelle

**Status:** established
**Last updated:** 2026-07-04
**Sources:** [[A Mechanistic Derivation of the Bitcoin Price Power Law_ Network Adoption Dynamics and Generalised Metcalfe Scaling]], [[bitcoin_powerlaw_v4_FINALA]], [[Bitcoin_Supply_Demand_Price_Dynamics]], [[Supply_and_Demand_Framework_Bitcoin_Price_Forecasting]], [[20260125_heartmoney-der-bitcoin-fruhling-beginnt]], [[20260510_heartmoney-ein-barenmarkt-fur-ameisen]], [[20260630_heartmoney-bitcoin-angst-und-magie]], [[20251123_heartmoney-ki-hat-keine-traumata]]

## Summary

Der Bitcoin-Preis folgt einem robusten Potenzgesetz in der Zeit: P(t) ∼ t^β mit β = 5.69 ± 0.05 (R² = 0.961, gemessen über 5.696 Tagesbeobachtungen Juli 2010 bis Februar 2026). Entscheidend ist: Der Exponent ist kein freier Parameter, sondern ergibt sich mechanistisch aus zwei unabhängigen Grössen — dem kubischen Adoptionswachstum des Netzwerks und einer Metcalfe-artigen Werteskalierung. Das macht das Modell falsifizierbar und unterscheidet es von blossem Kurvenanpassen.

## Body

### Die zwei Komponenten des Exponenten

Santostasi & Perrenod (2026) zeigen, dass β das Produkt zweier unabhängig messbarer Grössen ist:

**βA = 3.046 ± 0.012:** Adoptionswachstum. Die Anzahl aktiver Bitcoin-Adressen (non-zero balance) wächst kubisch mit der Zeit. Das entspricht dem Spreading-Muster auf heterogenen Scale-Free-Netzwerken, wie es aus Epidemiologie und Technologiediffusion bekannt ist (Sättigungswellen-Mechanismus).

**βM = 1.838 ± 0.031:** Werteskalierung. Der Preis skaliert mit der Nutzerzahl nach einem generalisierten Metcalfe-Gesetz: P ∼ N^βM. Das klassische Metcalfe-Gesetz (Wert ∝ N²) ergibt β_M = 2; der empirisch gemessene Wert liegt darunter, was auf sublineare Netzwerkeffekte hindeutet.

**Kompositionsidentität**: β = βA × βM = 3.046 × 1.838 = 5.60 — übereinstimmend mit dem direkt gemessenen βobs = 5.69 auf 1.6% Abweichung. Diese Übereinstimmung ist der zentrale Befund: Die Preisentwicklung folgt aus der Netzwerkstruktur, nicht aus spekulativer Dynamik.

### Statistische Robustheit

Die lognormalen Residuen vom Power-Law-Fit haben σ = 0.302 dex und keinen säkularen Drift — das Modell ist langzeitstabil. Vier unabhängige Tests bestätigen die Skalierungsinvarianz:

1. Multi-Asset Paar-Ratio-Test
2. Direkter Kollaps-Test: P(λt)/P(t) = λ^β* mit β* = 5.59 aus 5.298 Preisverhältnissen
3. Rollende Temporalanalyse 2011–2026: Median β* = 5.73 ± 0.58, kein struktureller Bruch
4. Sequenzielle Bayes-Analyse: Posterior β ∼ N(5.729, 0.013²) mit schrumpfender Unsicherheit als n^(-1/2)

### Falsifizierbarkeit

Das Modell benennt Bedingungen, unter denen das Power Law brechen würde: wenn Adoption nicht mehr dem kubischen Spreading-Muster folgt (z.B. durch regulatorische Abkoppelung vom globalen Netzwerk) oder wenn die Metcalfe-Skalierung strukturell kollabiert (z.B. durch einen überlegenen Konkurrenten, der Netzwerkeffekte absorbiert). Das macht es wissenschaftlich testbar — im Unterschied zu Stock-to-Flow, das keine mechanistische Grundlage hat.

### Einordnung und Grenzen

Das Power Law beschreibt die Preisentwicklung als deterministischen Ausdruck der Netzwerktopologie. Es erklärt nicht kurzfristige Volatilität, Halving-induzierte Zyklen oder spekulative Überschiessungen — diese erscheinen als Rauschen um den Trend. Das Modell sagt keine spezifischen Zielpreise vorher, sondern einen langfristigen Wachstumspfad, der solange gilt, wie das Netzwerkwachstum dem gemessenen Adoptionsmuster folgt.

### Angebot-Nachfrage-Modelle (Rudd & Porter, 2025)

Neben dem netzwerktheoretischen Power-Law-Ansatz gibt es einen komplementären Bottom-up-Ansatz, der den Preis aus fundamentalen Angebot-Nachfrage-Gleichgewichten ableitet statt aus Netzwerktopologie.

**Rudd & Porter (Journal of Risk and Financial Management, 2025)** entwickeln zwei verbundene Modelle:

*Supply and Demand Framework (Companion Paper)*: Ein Gleichgewichtsrahmen auf Basis von CES-Nachfragefunktion (Constant Elasticity of Substitution) und inelastischem 21M-Angebot. Der Preis entsteht als Market-Clearing-Preis, der von fünf Faktoren bestimmt wird: Marktdemand, Zeitpräferenz der Investoren, Fiat-Auszahlungssensitivität, initiale Liquid Supply, und tägliche Entnahmen aus der Liquid Supply (institutional accumulation).

*Monte Carlo Simulation (Bitcoin Supply, Demand, and Price Dynamics, JRFM 2025)*: Probabilistische Preisszenarien bis 2036. Wichtigste Befunde:
- **50% Wahrscheinlichkeit: BTC > 5,17 Mio. USD bis April 2036** (halving-relative Baseline)
- Typische Szenarien liegen zwischen "wenige Millionen" und "niedrige zweistellige Millionen" — weite Parameter liefern ähnliche Ergebnisse
- Hyperbolische Preispfade (>10× Baseline) konzentrieren sich nur bei Liquid Supply < 2 Mio. BTC + niedriger Auszahlungssensitivität
- **Liquid Supply ist der stärkste Preis-Hebel**: Wenn institutionelle Akkumulation und strategische Reserven BTC aus der Liquid Supply nehmen, steigt der Gleichgewichtspreis stark

Der Unterschied zum Power Law: Das Power-Law-Modell leitet den Preispfad aus der Netzwerkdiffusion ab (deterministisch, topologisch); das Angebot-Nachfrage-Modell leitet ihn aus wirtschaftlichem Gleichgewicht ab (stochastisch, fundamentalseitig). Beide liefern für 2036 Preisbänder im Millionenbereich — ein konsistentes Signal aus unterschiedlichen Methodiken. [[Bitcoin_Supply_Demand_Price_Dynamics]], [[Supply_and_Demand_Framework_Bitcoin_Price_Forecasting]]

### Log-periodisches Zyklusmodell und das Ende des 4-Jahres-Zyklus

Der populäre 4-Jahres-Zyklus (drei grüne Jahre, ein rotes, getaktet durch das Halving) wurde mit dem Jahresabschluss 2025 gebrochen: Statt des erwarteten Hype-Jahres endete 2025 mit −6%, ohne «Uptober» und ohne Blow-off-Top. Stephen Perrenod — Astrophysiker und Co-Autor der mechanistischen Power-Law-Herleitung oben — vertritt dazu die Position, der 4-Jahres-Zyklus habe als sauberes Muster nie existiert. Die Daten deuteten stattdessen auf ein log-periodisches Muster: Die zeitlichen Abstände zwischen den großen Boom-Phasen verdoppeln sich ungefähr mit jeder Iteration. Daraus folgt, dass 2025 keine klassische Hype-Phase brachte und der nächste Haupt-Peak eher um 2027 zu erwarten wäre. [[20260125_heartmoney-der-bitcoin-fruhling-beginnt]]

In dieselbe Richtung argumentieren Michael Saylor und Lyn Alden: Bitcoin werde inzwischen stärker von Kapitalflüssen, Kreditmärkten, globaler Liquidität und Makrobedingungen getrieben als vom Halving-Takt. [[20260510_heartmoney-ein-barenmarkt-fur-ameisen]]

Praxis-Check aus dem Bärenmarkt 2025/26: Im Juni 2026 notierte der Kurs am unteren Power-Law-Band. Die Quelle formuliert das Falsifikationskriterium der Community-Praxis: Würde die untere Unterstützungslinie über mehrere Wochen signifikant unterschritten, wäre das Power Law mit seinen heutigen Parametern zu begraben. Im Mai 2026 hielt das Band (Erholung über 82.000 USD). [[20260630_heartmoney-bitcoin-angst-und-magie]]

Das Modell ist inzwischen auch Anwendungswissen im DACH-Raum: Es dient als Beruhigungsrahmen in Bärenphasen (Einordnungs-Streams von Les Femmes Orange, Erklärvideos), als Timing-Heuristik für kreditfinanzierte Käufe (siehe [[bitcoin-auf-kredit]]) und als Rechenbasis für Renten-Gedankenexperimente («Wie viel Bitcoin reicht in 20 Jahren?») — Letzteres regelmäßig begleitet von Kritik an der Prognosegrundlage. [[20251123_heartmoney-ki-hat-keine-traumata]]

## Related

- [[bitcoin-spieltheorie-und-anreize]]
- [[bitcoin-netzwerk-und-nodes]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-alles-geteilt-durch-21-millionen]]
- [[bitcoin-auf-kredit]]
- [[bitcoin-volatilitaet-und-preisfindung]]

## Open Questions

- Wie verhält sich Perrenods log-periodisches Zyklusmodell formal zur mechanistischen Power-Law-Herleitung (Santostasi & Perrenod)? Die Newsletter-Quelle referiert es nur aus zweiter Hand (Interview/Video) — Primärquelle für RAW gesucht.
- Hält das kubische Adoptionswachstum auch bei globaler Massenadoption an, oder flacht es mit Marktsättigung ab?
- Wie verhält sich das Modell nach dem letzten Halving (~2140), wenn der Block Subsidy auf null fällt?
- Gibt es vergleichbare Potenzgesetze in anderen dezentralen Netzwerken (Ethereum, anderen L1s)?
