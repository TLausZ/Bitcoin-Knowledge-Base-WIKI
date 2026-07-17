# DESIGN.md — Bitcoin-Wiki Visualizer

Corporate Identity der Wiki-Karten in diesem Ordner. Format nach
github.com/google-labs-code/design.md: YAML-Tokens plus Prosa. Die Tokens
sind aus `index.html` extrahiert und gelten als Referenz für alle
weiteren Visualisierungen der Knowledge Base. Tokens haben Vorrang vor
eigenen Annahmen.

## Grundidee

Der Visualizer sieht aus wie eine alte topografische Vermessungskarte:
Sepia-Papier, dünne braune Höhenlinien, zurückhaltende Beschriftung. Eine
einzige Farbfamilie (warme Braun- und Beigetöne), kein reines Schwarz, kein
reines Weiss, keine zweite Akzentfarbe ausser dem wärmeren Rotbraun für
Hervorhebungen. Flächen sind matt und deckend, Tiefe entsteht durch die
Stufen des Geländes selbst, nicht durch Schlagschatten oder Verläufe.
Interface-Elemente (Panel, Titelleiste, Buttons) benutzen dieselbe Palette
wie die Karte, damit sie wie Kartenrand und Legende wirken, nicht wie ein
darübergelegtes UI.

## Tokens

```yaml
color:
  paper:        "#ece2cd"   # Seitenhintergrund, Kartenkörper, Panels
  paper-bright: "#f2ead6"   # Text auf dunklen Flächen
  ink:          "#5c4a34"   # Überschriften, aktive Elemente, Buttons
  ink-soft:     "#6b5a42"   # Listentext, Sekundärtext
  ink-faint:    "#8a7a5e"   # Grundtext, Untertitel, Hinweise
  line:         "rgba(74,58,40,0.68)"    # Höhenlinien, Konturen
  line-shadow:  "rgba(110,92,64,0.07)"   # Bodenschatten der Konturen
  border:       "rgba(110,92,64,0.25)"   # Trennlinien Panel/Titelleiste
  border-strong: "rgba(110,92,64,0.4)"   # Button-Rahmen
  bar:          "rgba(110,92,64,0.18)"   # Gewichtsbalken in der Liste
  accent:       "rgba(150,90,50,0.95)"   # Hover/Auswahl: Gipfelpunkt
  accent-line:  "rgba(120,70,40,0.85)"   # Hover/Auswahl: Verbindungslinie
  accent-box:   "rgba(92,74,52,0.97)"    # Hover/Auswahl: Label-Box

font:
  family: "ui-sans-serif, system-ui, sans-serif"
  size:
    title:    15px   # h1 Titelleiste, Gewicht 600
    base:     13px   # Grundschrift, Zeilenhöhe 1.4
    ui:       12px   # Liste, Untertitel, Buttons, Marker, Link
    label:    11px   # Karten-Labels (Canvas)
  weight:
    normal:   400
    strong:   600    # nur Titel und Namens-Präfixe

radius:
  button: 4px
  pill:   3px        # Link-Anzeige im Kartenbereich

space:
  page:   16px       # Aussenabstand Titelleiste, Link
  panel:  12px       # Innenabstand Panel und Buttons
  row:    3px        # vertikales Padding Listenzeilen

layout:
  topbar-height: 61px
  panel-width:   276px

stroke:
  contour: 0.85px    # Höhenlinien (mal devicePixelRatio)
  shadow:  1px
  leader:  1px       # Label-Verbindungslinien, 1.2px bei Hervorhebung
```

## Farbe

**Ausnahme Screensaver:** `screensaver.html` färbt die Höhenringe
hypsometrisch in Pastelltönen (Palette «Atlas-Klassiker», definiert im
`PALETTES`-Objekt dort; Doku in `SCREENSAVER.md`). Linien, Labels, Papier
und alles Übrige folgen weiterhin den Tokens dieser Datei. Der
interaktive Visualizer (`index.html`) bleibt einfarbig.

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

## Typografie

Systemschrift ohne Ausnahme, keine Webfonts. Vier Grössen genügen; nichts
unter 11px, nichts über 15px. Fett nur für den Kartentitel und
Namens-Präfixe (etwa vor der GitHub-URL). Keine Kursive, keine
Versalien-Überschriften. Beschriftungen auf der Karte sind Kleinschreibung
mit Leerzeichen statt Bindestrichen (Slug-Schreibweise aufgelöst).

## Komponenten

- **Buttons** (Sortierung): 1px-Rahmen `border-strong`, Text `ink`,
  transparenter Grund. Aktiver Zustand invertiert: Grund `ink`, Text
  `paper-bright`. Kein Hover-Effekt auf inaktiven Buttons.
- **Listenzeilen**: Gewicht als linksbündiger Hintergrundbalken (`bar`),
  Score als kleinere, abgeschwächte Zahl. Hover und Auswahl invertieren
  die Zeile wie den aktiven Button.
- **Karten-Labels**: helle halbtransparente Box, dünne Verbindungslinie
  zum Gipfelpunkt mit Knick, wenn die Box an den Rand gedrückt wird.
  Hervorgehoben: dunkle Box, helle Schrift, dickerer Punkt.
- **Link-Anzeige**: Pill auf `paper` mit `radius.pill`, fetter Name als
  Text, nur die URL verlinkt. Verschwindet ohne Auswahl vollständig.

## Bewegung

Keine Animationen und keine Übergänge. Die Karte reagiert unmittelbar auf
Eingaben (Drehen, Zoomen, W/A/S/D); Zustandswechsel wie Hover oder Auswahl
springen ohne Transition. Was sich bewegt, ist immer die Karte selbst,
nie das Interface.

## Sprache im Interface

Deutsch, knapp, Kleinschreibung in Hinweisen («ziehen zum drehen»).
Tastennamen fett. Zahlen im Untertitel kommen aus den Daten und werden
nicht von Hand gepflegt.
