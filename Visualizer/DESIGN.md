---
version: alpha
name: Bitcoin-Wiki Visualizer
description: >
  Corporate Identity der Wiki-Karten in diesem Ordner. Format nach
  github.com/google-labs-code/design.md. Die Tokens sind aus index.html
  extrahiert und gelten als Referenz für alle weiteren Visualisierungen
  der Knowledge Base. Tokens haben Vorrang vor eigenen Annahmen.
omitted:
  - Elevation & Depth
colors:
  primary: "{colors.ink}"
  paper: "#ece2cd"                      # Seitenhintergrund, Kartenkörper, Panels
  paper-bright: "#f2ead6"               # Text auf dunklen Flächen
  ink: "#5c4a34"                        # Überschriften, aktive Elemente, Buttons
  ink-soft: "#6b5a42"                   # Listentext, Sekundärtext
  ink-faint: "#8a7a5e"                  # Grundtext, Untertitel, Hinweise
  line: "rgba(74,58,40,0.68)"           # Höhenlinien, Konturen
  line-shadow: "rgba(110,92,64,0.07)"   # Bodenschatten der Konturen
  border: "rgba(110,92,64,0.25)"        # Trennlinien Panel/Titelleiste
  border-strong: "rgba(110,92,64,0.4)"  # Button-Rahmen
  bar: "rgba(110,92,64,0.18)"           # Gewichtsbalken in der Liste
  accent: "rgba(150,90,50,0.95)"        # Hover/Auswahl: Gipfelpunkt
  accent-line: "rgba(120,70,40,0.85)"   # Hover/Auswahl: Verbindungslinie
  accent-box: "rgba(92,74,52,0.97)"     # Hover/Auswahl: Label-Box
typography:
  title:                                # h1 Titelleiste
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
  base:                                 # Grundschrift
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
  ui:                                   # Liste, Untertitel, Buttons, Marker, Link
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
  label:                                # Karten-Labels (Canvas)
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
rounded:
  button: 4px
  pill: 3px                             # Link-Anzeige im Kartenbereich
  nav-pill: 19px                        # Lese-Navigation, voll gerundet bei 38px Höhe
spacing:
  page: 16px                            # Aussenabstand Titelleiste, Link
  panel: 12px                           # Innenabstand Panel und Buttons
  control: 8px                          # Abstand benachbarter Steuer-Knöpfe (Lese-Navigation)
  row: 3px                              # vertikales Padding Listenzeilen
components:
  sort-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.button}"
    padding: "{spacing.panel}"
  read-nav-pill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper-bright}"
    typography: "{typography.ui}"
    rounded: "{rounded.nav-pill}"
    height: 38px
    width: 96px
  link-pill:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.pill}"
---

## Overview

Der Visualizer sieht aus wie eine alte topografische Vermessungskarte:
Sepia-Papier, dünne braune Höhenlinien, zurückhaltende Beschriftung. Eine
einzige Farbfamilie (warme Braun- und Beigetöne), kein reines Schwarz, kein
reines Weiss, keine zweite Akzentfarbe ausser dem wärmeren Rotbraun für
Hervorhebungen. Flächen sind matt und deckend, Tiefe entsteht durch die
Stufen des Geländes selbst, nicht durch Schlagschatten oder Verläufe.
Interface-Elemente (Panel, Titelleiste, Buttons) benutzen dieselbe Palette
wie die Karte, damit sie wie Kartenrand und Legende wirken, nicht wie ein
darübergelegtes UI.

## Colors

Alle Farben stammen aus einer Familie. `paper` ist die einzige
Flächenfarbe; Panel, Titelleiste und Kartenkörper unterscheiden sich nicht
im Ton, sondern nur durch Trennlinien (`border`). Text staffelt sich über
drei Braunstufen von `ink` (wichtig) bis `ink-faint` (beiläufig).
Hervorhebung kippt das Schema: dunkle Box (`accent-box`), helle Schrift
(`paper-bright`). Das wärmere Rotbraun (`accent`) markiert ausschliesslich
den aktiven Gipfel und seine Linie, sonst nichts.

Transparenzen sind Teil der Palette: Linien und Rahmen sind nie voll
deckend, nur Flächen sind es. Neue Elemente sollen eher eine bestehende
Alpha-Stufe wiederverwenden als eine neue einführen.

**Ausnahme Screensaver:** `screensaver.html` färbt die Höhenringe
hypsometrisch in Pastelltönen (Palette «Atlas-Klassiker», definiert im
`PALETTES`-Objekt dort; Doku in `SCREENSAVER.md`). Linien, Labels, Papier
und alles Übrige folgen weiterhin den Tokens dieser Datei. Der
interaktive Visualizer (`index.html`) bleibt einfarbig.

## Typography

Systemschrift ohne Ausnahme, keine Webfonts. Vier Grössen genügen; nichts
unter 11px, nichts über 15px. Fett (600) nur für den Kartentitel und
Namens-Präfixe (etwa vor der GitHub-URL). Keine Kursive, keine
Versalien-Überschriften. Beschriftungen auf der Karte sind Kleinschreibung
mit Leerzeichen statt Bindestrichen (Slug-Schreibweise aufgelöst).

## Layout

Feste Masse ausserhalb des Token-Schemas:

- Titelleiste: 61px hoch
- Panel: 276px breit
- Strichstärken: Höhenlinien 0.85px (mal devicePixelRatio), Bodenschatten
  1px, Label-Verbindungslinien 1px (1.2px bei Hervorhebung)

Abstände folgen der `spacing`-Skala: `page` für Aussenabstände von
Titelleiste und Link, `panel` für Innenabstände von Panel und Buttons,
`control` zwischen benachbarten Steuer-Knöpfen, `row` als vertikales
Padding der Listenzeilen.

## Shapes

Kleine Radien, keine weichen Karten-Ecken: Buttons 4px, die Link-Pill 3px.
Einzige Ausnahme sind die voll gerundeten Pills der Lese-Navigation
(19px bei 38px Höhe). Es gibt keine Schatten und keine Verläufe — Tiefe
entsteht allein durch die Höhenstufen des Geländes (deshalb ist der
Abschnitt «Elevation & Depth» bewusst ausgelassen).

## Components

- **Buttons** (Sortierung, `sort-button`): 1px-Rahmen `border-strong`,
  Text `ink`, transparenter Grund. Aktiver Zustand invertiert: Grund
  `ink`, Text `paper-bright`. Kein Hover-Effekt auf inaktiven Buttons.
- **Lese-Navigation** (`read-nav-pill`, Modal-Kopf, «‹ Zurück» /
  «Weiter ›»): solide Pills, Grund `ink`, Text `paper-bright`, voll
  gerundet (38px hoch). Beide gleich breit (`min-width` 96px, zentriert),
  damit sie beim Ein- und Ausblenden nicht springen; `spacing.control`
  dazwischen. «Weiter» erscheint nur, wenn ein zurückgelassener Artikel
  voraus liegt. Eigener Stil, nicht der der Sortier-Buttons.
- **Listenzeilen**: Gewicht als linksbündiger Hintergrundbalken (`bar`),
  Score als kleinere, abgeschwächte Zahl. Hover und Auswahl invertieren
  die Zeile wie den aktiven Button.
- **Karten-Labels**: helle halbtransparente Box, dünne Verbindungslinie
  zum Gipfelpunkt mit Knick, wenn die Box an den Rand gedrückt wird.
  Hervorgehoben: dunkle Box, helle Schrift, dickerer Punkt.
- **Link-Anzeige** (`link-pill`): Pill auf `paper` mit `rounded.pill`,
  fetter Name als Text, nur die URL verlinkt. Verschwindet ohne Auswahl
  vollständig.

## Do's and Don'ts

- Keine Animationen und keine Übergänge. Die Karte reagiert unmittelbar
  auf Eingaben (Drehen, Zoomen, W/A/S/D); Zustandswechsel wie Hover oder
  Auswahl springen ohne Transition. Was sich bewegt, ist immer die Karte
  selbst, nie das Interface.
- Interface-Sprache: Deutsch, knapp, Kleinschreibung in Hinweisen
  («ziehen zum drehen»). Tastennamen fett.
- Zahlen im Untertitel kommen aus den Daten und werden nicht von Hand
  gepflegt.
- Keine neuen Alpha-Stufen, keine zweite Akzentfarbe, keine Webfonts,
  keine Schatten.
