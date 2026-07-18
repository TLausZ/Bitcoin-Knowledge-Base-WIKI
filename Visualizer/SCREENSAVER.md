# SCREENSAVER.md — Technische Doku zu screensaver.html

Notizen für die Weiterarbeit in neuen Sitzungen. Stand: 18. Juli 2026.

## Was es ist

`screensaver.html` — eigenständige Seite im Visualizer-Ordner. Zeigt das
Bitcoin-Wiki als Screensaver: pro Karte ein langsamer Orbit plus eine
Kamerafahrt («Überflug»), beide mit demselben orthografischen Renderer
`draw()` und derselben Höhenfärbung (Palette 1, Navy-Meer). Nach jedem
Orbit+Flug-Zyklus wechselt die Insel: Gesamtkarte, dann alle 18
Themenkarten alphabetisch, dann wieder von vorne (18. Juli 2026). Vorbild war der
Idle-Screensaver von turtletoy.net (Output auf Ebenen, langsame
Kamerafahrt, Maus beendet).

Beenden: Mausbewegung (>40 px kumuliert), Klick, Taste, Scroll, Touch →
zurück zur Ursprungsseite via `document.referrer` (same-origin geprüft);
ohne Referrer (Direktaufruf) zur Gesamtkarte `index.html`.

Starten: `index.html` und alle Themenkarten wechseln nach 42 s ohne
Eingabe automatisch zu `screensaver.html` (Idle-Timer am Skriptende von
index.html; build_theme_cards.py patcht den Pfad in den Themenkarten auf
`../screensaver.html`). Ausnahmen:
Mobile-View (max-width 640px) und offenes Lese-Modal — dort wird der Timer
nur neu gestellt. Kein UI auf der Screensaver-Seite selbst: Kartusche und
Zoom/Label-HUD wurden auf User-Wunsch entfernt, sichtbar ist nur der Canvas.

## Kein eigener Datenbestand

Die Seite lädt beim Start alle Karten per `fetch` (Liste `MAPS`: index.html
plus themen/*.html, hartkodiert — neue Themen dort nachtragen!) und parst
je Karte in `parseMap`:

- `PEAKS`: Gesamtkarte `const PEAKS = [...];`, Themenkarten volles Array
  mit Themen-Tags plus `.filter(p => (p.t||[]).includes(THEME))` — der
  Filter wird beim Parsen nachgebaut (`const THEME = "…"` aus der Datei).
- Relief-Parameter aus dem Block `let SEED = ...` bis `let yaw`: SEED,
  BETA, L, ZMAX, BASE, TERW, RIDGE, DBIAS, SPREAD, IRAD, COASTW, BASECUT,
  LIFT. Themenkarten überschreiben die Defaults in einer Zeile anstelle
  des `/*__THEME_CFG__*/`-Markers — darum zählt je Name die LETZTE
  Zuweisung im Block.

Nicht ladbare Karten werden übersprungen (Promise.allSettled). Dadurch ist
der Screensaver automatisch aktuell, wenn `tools/layout_map.py` oder
`build_theme_cards.py` neu bauen. Bricht, falls sich der PEAKS-Zeilenaufbau
ändert. Ohne HTTP (file://) schlägt fetch fehl → Fehlerhinweis im DOM
(#err), Karte über `python3 -m http.server` öffnen.

Die Gelände-Pipeline (mulberry32, fft1d/fft2d, buildEnvelope, computeField,
contour, chainLoops, build, project, peakVisible) ist 1:1 aus index.html
kopiert. Änderungen dort müssen hier nachgezogen werden.

## Ablauf (Timeline in animate)

Konstanten: `ORBIT_DUR=106` (halber Flug, 18. Juli 2026; davor 84),
`CROSS=213` (320/1.5), `NCROSS=1`, `CYCLE=ORBIT_DUR+NCROSS*CROSS` (=319 s),
`FADE=1.5`
(einblenden), `FADEOUT=2.5` (ausblenden), `TRIM=1` (Route läuft ganz durch;
das frühere Kappen galt dem Ego-Renderer mit Meer-Anflug).

- Default (kein mode-Parameter): 106 s Orbit → 1 Überflug à 213 s → dann
  Kartenwechsel auf die nächste Insel (Zyklusnummer modulo Kartenzahl).
  Da yaw eine Funktion der Gesamtzeit ist, zeigt jede Orbit-Phase einen
  anderen Abschnitt der Umrundung.
- Kartenwechsel (`applyMap` + `build()`, 2–4 s Feld-Neubau) passiert exakt
  an der Zyklusgrenze, wo die Blende voll deckt; das Bild friert auf dem
  Meer-Cover ein und die verlorene Zeit wird über `tOff` zurückgegeben,
  damit der neue Zyklus bei u≈0 einblendet. Label-Zustand (`labState`,
  `labGhosts`) wird beim Wechsel geleert. `?mode=flug` / `?mode=orbit`
  bleiben fix auf der Gesamtkarte.
- Jeder Szenenwechsel fadet über ein Meerfarb-Overlay (`SEA_RGB`) am Ende
  von animate. Kein harter Schnitt.
- Start der Seite: immer Fade-in (t0 = Zeit des ersten Frames; nötig, weil
  der Feld-Build 2–4 s frisst und t ab Seitenlade-Zeitpunkt läuft).
- Artikel-Highlight (`tourIdx`): wechselt alle 30 s durch die Top-21-Artikel
  (peaks ist gewichtssortiert), gilt in beiden Modi.
- Label-Fade: Labels laufen über den Helper `drawLabels(entries, dpr)`;
  Erscheinen/Verschwinden blendet über `LABEL_FADE` (0.1 s, Echtzeit, nicht
  speed-skaliert). Zustand in `labState` (Map Artikel-Index → Alpha + letzte
  Geometrie). Springt ein Label auf eine neue Stapelhöhe (>halbe
  Zeilenhöhe/Boxbreite pro Frame), blendet die alte Lage als «Geist»
  (`labGhosts`) aus und die neue frisch ein.

## Ein Renderer, zwei Kameras

`draw()` ist der orthografische Wiki-Renderer: gestapelte
Höhenring-Flächen (loopsByLevel, evenodd, Wände via `wall`), Labels mit
Kollisions-Schub nach oben und Stapel-Bremse (>3 Zeilen über dem Gipfel →
Label entfällt; von 6 auf 3 verschärft am 18. Juli 2026, weil die dichten
BIP-Cluster Label-Türme bauten). Label-Budget: `min(42, max(21, ((zoom-1.10)/2.30)^6 * 439))`
— bis Zoom ~2.5 die Top 21, ab ~2.65 konstant 42 (21/42 als Bitcoin-Zahlen).

### Orbit (`orbitCam`)
- Kamera kreist automatisch: yaw-Periode 400 s, pitch 1.08±0.16 (194 s),
  zoom 2.25±1.15 (302 s, also 1.10–3.40). Inselmitte fixiert (camX=camY=0;
  die frühere Lissajous-Drift wurde auf User-Wunsch entfernt). Der
  Bildanker `anchorY` hängt am Kippwinkel: 0.55 in der Seitenansicht,
  bis 0.47 bei maximaler Draufsicht.
- Ringe gefärbt nach Palette (siehe Höhenfärbung), Hintergrund = Meerfarbe
  (body-Background).

### Überflug (`flyoverCam`, seit 18. Juli 2026)
- Gleicher `draw()`-Aufruf wie im Orbit, inklusive Färbung (18. Juli 2026:
  zuerst ungefärbt als purer index.html-Look via `FLYING`-Flag, dann auf
  User-Wunsch identisch zum Orbit gefärbt — das Flag ist wieder weg).
- Route: quadratische Bezierkurve von Küste zu Küste (R0=R1=1.8, Wegpunkt
  nahe Inselmitte), `camX/camY` fahren sie ab; Routenwahl deterministisch
  pseudozufällig über `mulberry32(fi)`, fi = globaler Überflug-Index.
- yaw fix pro Route (aus demselben rnd-Strom) plus langsame Drehung
  (+0.5 rad über die Route), pitch 1.12±0.04, zoom als Ken-Burns-Verlauf
  1.8 → 3.2 über die Route (überschreibbar per `?zoom=N`), anchorY 0.5.
- Der frühere Ego-Perspektive-Renderer (drawFlight: 190 Tiefenscheiben,
  Painter, Marching-Squares-Höhenlinien, skyY-Silhouette samt
  Apex-Verfeinerung, flightCam, sampleH, peakVisibleP, FBUF, vorgezogenes
  Flug-Ende via tOff/landCols) wurde am 18. Juli 2026 komplett entfernt —
  letzte Fassung in git (Stand compile pass 94). Dort auch die
  Performance-Historie (Zwei-Pass-Fill, 33 → 16.6 ms/Frame).

## Höhenfärbung

Beide Kameras färben die Ringflächen nach Höhenstufe (hypsometrisch,
pastell) — die Färbung sitzt in `draw()`. Standard ist Palette 1 «Meer»: Landfarben des
Atlas-Klassikers (User-Vorlage, 35% Richtung Papierweiss aufgehellt — Grün
→ Gelb → Ocker → Rost → Braunrot → Grau → Weiss) plus Navy-Meer. Die
Paletten 2–6 (sonnig, kühl, sepia-nah, hypsometrisch, Atlas-Klassiker pur)
bleiben als Alternativen im `PALETTES`-Objekt, umschaltbar per `?pal=N`.

- Meerfarbe `SEA_RGB`: Palette 1 helles Navy, sonst Papier.
- Wasser-Hintergrund (18. Juli 2026, nur Palette 1): linearer Verlauf
  nach dem `WATER_STOPS`-Array, reines Blau ohne Warmtöne mit bewusst
  geringem Kontrast (oben → unten: dunkles Navy rgb 52,68,112 →
  rgb 32,46,90 → tiefes Dunkelblau rgb 14,26,66). `paintWater()` zeichnet ihn
  15% überhöht und verschiebt ihn per Pitch vertikal (sanfter Parallax,
  Pitch-Bereich 0.92–1.28 auf den Überstand gemappt): flache Kamera
  zeigt das warme Licht oben, Draufsicht rutscht ins tiefe Blau. Die
  Blende in animate nutzt denselben Hintergrund via globalAlpha.
  Frühere Iterationen (alle verworfen): radialer Verlauf um die
  Inselmitte, berechneter Himmel-Horizont (f·tanθ — schnitt in flachen
  Orbit-Momenten durch die Insel), prozedurale Wellen-Ellipsen, ein
  Aquarell-Wasserbild (wasser.png, Parallax zu stark, gelöscht).
- `ringColor(l)`: Stufe l (1..L) → Farbe, lineare Interpolation über
  Stützpunkte `[t, [r,g,b]]` mit t=l/L. Im Orbit `fillStyle=ringColor(l)`
  pro Ring-Ebene (Wände inklusive), Konturlinien bleiben braun.
- Palette-Leiste (Arbeitswerkzeug): mit `?pal=N` erscheinen rechts 32
  Boxen mit der aktiven Palette; abgeblendet, was nie als Ring erscheint
  (Stufe 32 und alles unter BASECUT, aktuell 1–4). Aktuell deaktiviert:
  der `buildPalette()`-Aufruf im Start-Block ist auskommentiert, Code
  bleibt drin — für Farbarbeit wieder einkommentieren.
- Gezeichnete Ringe: `L=32` Stufen, Konturschleife l=1–31, BASECUT=0.14
  kappt 1–4 → sichtbar sind die Stufen 5–31 (27 Ringe).

## URL-Parameter

- `?pal=N` — Palette 1–6 umschalten und Palette-Leiste einblenden
  (Standard ohne Parameter: Palette 1, keine Leiste; ungültige Werte
  wirken wie kein Parameter).
- `?speed=N` — Zeitraffer (Testen; N beliebig, ohne = 1).
- `?mode=flug` / `?mode=orbit` — Modus fixieren; ohne: Wechsel-Zyklus.
- `?noexit=1` — Exit-Events deaktiviert (Testen mit Mausbewegung).
- `?labels=0` — Labels aus (beide Modi). Andere Werte ohne Wirkung, seit
  überall die Zoom-Rampe gilt.
- `?zoom=N` — friert den Zoom auf N ein (Orbit-Atmung aus, Überflug fix),
  zum Tunen.
- `?pitch=N` — friert die Kameraneigung ein (rad; ~1.55 = Seitenansicht),
  zum Tunen.
- Cache: Chrome cached die Seite heuristisch; beim Testen nach Edits
  Query-Parameter variieren (`&v=2`) oder Hard-Reload.

## Test-Workflow

- Server: `python3 -m http.server 8741` im Visualizer-Ordner (kein PHP auf
  dieser Maschine; Sandbox blockiert den Port-Bind → ohne Sandbox starten).
- Chrome-Screenshots: Seite braucht nach Load 2–4 s für den Feld-Build
  (leeres Papier ist dann kein Bug). Achtung beim Testen mit Browser-Tools:
  ohne `noexit=1` killt jede echte Mausbewegung des Users die Seite → Sprung
  auf index.html.
- Übliche Test-URL: `http://localhost:8741/screensaver.html?speed=8&noexit=1`.

## Bewusste Entscheidungen / History

- User-Vorgaben umgesetzt: Orbit fixiert auf Inselmitte; Fades statt
  Schnitten; Highlight-Wechsel 30 s; zuerst 3 Überflüge pro Zyklus, später
  reduziert auf 1 Überflug mit doppelt langem Orbit davor.
- `LABEL_TOP=21` wie im Original (21 Millionen).
- DESIGN.md gilt: eine Farbfamilie, Systemschrift. Kartusche und HUD wurden
  wieder entfernt — die Seite zeigt nur den Canvas (plus #err-Fallback).
- Ego-Perspektive-Ära (bis 18. Juli 2026, alles in git): eigener
  Flugsimulator-Renderer mit Tiefenscheiben; dort nacheinander entfernt:
  Seitenblick, Banking, Distanz-Skalierung der Labels, Profillinien
  (ersetzt durch skyY-Silhouette), Höhenfärbung mit Himmel/Meer-Verlauf;
  zuletzt Kuppen-Wackeln per Apex-Verfeinerung behoben — dann der ganze
  Renderer auf User-Wunsch («wir rendern wie index.html und fliegen
  drüber») durch die flyoverCam-Kamerafahrt ersetzt.
- Verworfen: `?render=flug` (Perspektiv-Renderer als Orbit) — getestet und
  vom User abgelehnt, der Orbit blieb immer orthografisch.
- Label-Rampe: final hoch 6 mit Untergrenze 21 und Obergrenze 42.

## Offene Ideen

- Überflug vom User abgenommen (18. Juli 2026): «gefällt viel besser,
  ähnelt Ken-Burns-Effekt». Die Parameter (R0/R1=1.8, zoom 1.8→3.2,
  pitch 1.12, yaw-Drehung +0.5 rad, CROSS=213 s) sind erste Setzung und
  bei Bedarf tunbar.
- Entschieden: Der Zyklus bleibt fix Orbit → Flug → Orbit → Flug
  (NCROSS=1, endlos); eine variable Überflug-Anzahl ist ausdrücklich nicht
  gewünscht.
