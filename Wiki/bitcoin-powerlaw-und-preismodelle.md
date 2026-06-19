# Bitcoin Power Law und Preismodelle

**Status:** established
**Last updated:** 2026-06-20
**Sources:** [[A Mechanistic Derivation of the Bitcoin Price Power Law_ Network Adoption Dynamics and Generalised Metcalfe Scaling]], [[bitcoin_powerlaw_v4_FINALA]]

## Summary

Der Bitcoin-Preis folgt einem robusten Potenzgesetz in der Zeit: P(t) ∼ t^β mit β = 5.69 ± 0.05 (R² = 0.961, gemessen über 5.696 Tagesbeobachtungen Juli 2010 bis Februar 2026). Entscheidend ist: Der Exponent ist kein freier Parameter, sondern ergibt sich mechanistisch aus zwei unabhängigen Grössen — dem kubischen Adoptionswachstum des Netzwerks und einer Metcalfe-artigen Werteskalierung. Das macht das Modell falsifizierbar und unterscheidet es von blossem Kurvenanpassen.

## Body

### Die zwei Komponenten des Exponenten

Santostasi & Perrenod (2026) zeigen, dass β das Produkt zweier unabhängig messbarer Grössen ist:

**βA = 3.046 ± 0.012** — Adoptionswachstum. Die Anzahl aktiver Bitcoin-Adressen (non-zero balance) wächst kubisch mit der Zeit. Das entspricht dem Spreading-Muster auf heterogenen Scale-Free-Netzwerken, wie es aus Epidemiologie und Technologiediffusion bekannt ist (Sättigungswellen-Mechanismus).

**βM = 1.838 ± 0.031** — Werteskalierung. Der Preis skaliert mit der Nutzerzahl nach einem generalisierten Metcalfe-Gesetz: P ∼ N^βM. Das klassische Metcalfe-Gesetz (Wert ∝ N²) ergibt β_M = 2; der empirisch gemessene Wert liegt darunter, was auf sublineare Netzwerkeffekte hindeutet.

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

## Related

- [[bitcoin-spieltheorie-und-anreize]]
- [[bitcoin-netzwerk-und-nodes]]
- [[bitcoin-geldpolitik-und-21-millionen-limit]]
- [[bitcoin-alles-geteilt-durch-21-millionen]]

## Open Questions

- Hält das kubische Adoptionswachstum auch bei globaler Massenadoption an, oder flacht es mit Marktsättigung ab?
- Wie verhält sich das Modell nach dem letzten Halving (~2140), wenn der Block Subsidy auf null fällt?
- Gibt es vergleichbare Potenzgesetze in anderen dezentralen Netzwerken (Ethereum, anderen L1s)?
