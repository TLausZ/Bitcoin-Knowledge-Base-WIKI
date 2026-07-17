# SCREENSAVER.md — Technische Doku zu screensaver.html

Notizen für die Weiterarbeit in neuen Sitzungen. Stand: 17. Juli 2026.

## Was es ist

`screensaver.html` — eigenständige Seite im Visualizer-Ordner. Zeigt die
Gesamtkarte des Bitcoin-Wikis als Screensaver: abwechselnd ein langsamer
Orbit um die Insel (Look des Original-Visualizers) und Ego-Perspektive-
Überflüge wie im Flugsimulator. Vorbild war der Idle-Screensaver von
turtletoy.net (Output auf Ebenen, langsame Kamerafahrt, Maus beendet).

Beenden: Mausbewegung (>40 px kumuliert), Klick, Taste, Scroll, Touch →
`location.replace('index.html')`.

Starten: `index.html` wechselt nach 42 s ohne Eingabe automatisch zu
`screensaver.html` (Idle-Timer am Skriptende von index.html). Ausnahmen:
Mobile-View (max-width 640px) und offenes Lese-Modal — dort wird der Timer
nur neu gestellt. Kein UI auf der Screensaver-Seite selbst: Kartusche und
Zoom/Label-HUD wurden auf User-Wunsch entfernt, sichtbar ist nur der Canvas.

## Kein eigener Datenbestand

Die Seite lädt zur Laufzeit `index.html` per `fetch` und extrahiert per Regex:

- `PEAKS` (Zeile `const PEAKS = [...]`) — JSON.parse-bar.
- Die Relief-Parameter aus dem Block `let SEED = ...` bis zum Marker
  `/*__THEME_CFG__*/`: SEED, BETA, L, ZMAX, BASE, TERW, RIDGE, DBIAS,
  SPREAD, IRAD, COASTW, BASECUT, LIFT (Zuweisung per `eval`).

Dadurch ist der Screensaver automatisch aktuell, wenn `tools/layout_map.py`
die Karte neu baut. Bricht, falls sich in index.html der PEAKS-Zeilenaufbau
oder der Marker ändert. Ohne HTTP (file://) schlägt fetch fehl → Fehlerhinweis
im DOM (#err), Karte über `python3 -m http.server` öffnen.

Die Gelände-Pipeline (mulberry32, fft1d/fft2d, buildEnvelope, computeField,
contour, chainLoops, build, project, peakVisible) ist 1:1 aus index.html
kopiert. Änderungen dort müssen hier nachgezogen werden.

## Ablauf (Timeline in animate)

Konstanten: `ORBIT_DUR=84` (verdoppelt von 42, 17. Juli 2026), `CROSS=213`
(320/1.5, Flug 1.5x schneller), `NCROSS=1`, `CYCLE=ORBIT_DUR+NCROSS*CROSS`
(=297 s), `FADE=1.5` (einblenden),
`FADEOUT=2.5` (ausblenden), `TRIM=(CROSS-28)/CROSS` (gleicher Routen-Endpunkt
wie die vom User bestätigten 42 s bei CROSS=320).

- Default (kein mode-Parameter): 84 s Orbit → 1 Überflug à 213 s → wieder
  Orbit. Da yaw eine Funktion der Gesamtzeit ist, zeigt jede Orbit-Phase
  einen anderen Abschnitt der Umrundung.
- Jeder Szenenwechsel (auch Überflug→Überflug) fadet über Papierfarbe
  (`rgba(236,226,205,α)`-Overlay am Ende von animate). Kein harter Schnitt.
- Start der Seite: immer Fade-in (t0 = Zeit des ersten Frames; nötig, weil
  der Feld-Build 2–4 s frisst und t ab Seitenlade-Zeitpunkt läuft).
- `TRIM` kappt die Flugroute vor dem Ende. Der Routen-Endpunkt wurde bei
  CROSS=320 iterativ auf −42 s eingestellt (15→25→35→40→42) und bei jeder
  Tempoänderung als FRAKTION beibehalten (bei CROSS=213 sind das −28 s).
  Bei Änderungen an CROSS die Sekundenzahl entsprechend mitskalieren.
- Vorgezogenes Flug-Ende (17. Juli 2026): `drawFlight` zählt pro Frame die
  Spalten mit sichtbarem Land (`landCols`, via skyY). Ist 2 s lang kein Land
  mehr im Bild (Hysterese; zusätzlich muss vorher >30 s Land sichtbar gewesen
  sein), addiert `flightPhase` die Restzeit auf `tOff` und springt damit
  direkt an den Fade-out-Punkt (`CROSS-FADEOUT`). Grund: Die Insel verschwindet
  je nach Route zwischen ~160 und ~210 s unter dem Bildrand (gemessen über
  14 Routen), ein fixer früherer Schnitt passt wegen der Streuung nicht.
  Der Sprung ist unsichtbar (fade=1, nur leeres Papier im Bild). `tOff`
  verschiebt die gesamte Zeitachse (`t=now*SPEED+tOff`), Orbit-yaw und
  tourIdx springen mit — egal, beides zyklisch.
- Artikel-Highlight (`tourIdx`): wechselt alle 30 s durch die Top-21-Artikel
  (peaks ist gewichtssortiert), gilt in beiden Modi.
- Label-Fade: beide Renderer zeichnen Labels über den gemeinsamen Helper
  `drawLabels(entries, dpr)`; Erscheinen/Verschwinden blendet über
  `LABEL_FADE` (0.1 s, Echtzeit, nicht speed-skaliert). Zustand in
  `labState` (Map Artikel-Index → Alpha + letzte Geometrie). Springt ein
  Label auf eine neue Stapelhöhe (>halbe Zeilenhöhe/Boxbreite pro Frame),
  blendet die alte Lage als «Geist» (`labGhosts`) aus und die neue frisch ein.

## Zwei Renderer

### Orbit (`orbitCam` + `draw`)
Orthografisch, identisch zum Wiki-Look: Schattenebene, gestapelte
Höhenlinien-Ringe (loopsByLevel, evenodd), Labels mit Kollisions-Schub nach
oben. Unterschiede zu index.html:
- Kamera kreist automatisch: yaw-Periode 400 s, pitch 1.08±0.16 (194 s),
  zoom 2.25±1.15 (302 s, also 1.10–3.40). Inselmitte fixiert (camX=camY=0;
  die frühere Lissajous-Drift wurde auf User-Wunsch entfernt). Der
  Bildanker `anchorY` hängt am Kippwinkel: 0.55 in der Seitenansicht,
  bis 0.47 bei maximaler Draufsicht (Insel rückt hoch, damit der untere
  Rand im Bild bleibt; Stärke = der Faktor 0.08 in orbitCam).
- Label-Budget: `min(42, max(21, ((zoom-1.10)/2.30)^6 * 439))` — bis Zoom
  ~2.5 die Top 21, kurzer Anstieg, ab Zoom ~2.65 konstant 42 (21/42 als
  Bitcoin-Zahlen). Verworfen: linear und hoch 4 bis 439 (beide zu viele),
  quadratisch (`21*(zoom/1.25)^2`, Kommentar im Code).
- Stapel-Bremse: Labels, die >6 Zeilen über den Gipfel geschoben würden,
  entfallen (verhindert Label-Türme mit langen Leitlinien).

### Flug (`flightCam` + `drawFlight`)
Echte Ego-Perspektive, eigener Renderer (die Konturring-Malerei nach Höhe
funktioniert nur aus steiler Draufsicht; in Bodennähe braucht Verdeckung
eine Tiefensortierung):
- Klassisches Depth-Slice-Verfahren: 190 Tiefenscheiben (zNear 0.18 bis
  zFar 7.0, geometrische Staffelung), von fern nach nah gemalt. Jede Scheibe:
  Höhenprofil via `sampleH` (bilinear aus `field`), gefüllt (Painter: nah
  übermalt fern), ferne Linien blasser. Meer (= BASECUT-Ebene) bleibt
  leeres Papier.
- Zwei Pässe seit 17. Juli 2026 (Performance): Pass 1 sampelt alle Profile
  nah→fern in wiederverwendete Puffer (`FBUF`) und führt pro Scheibe den
  unteren Fill-Rand mit (`EV` = min-y aller näheren Scheiben). Pass 2 malt
  fern→nah, füllt aber nur noch das sichtbare Band (Profil bis EV+10px)
  statt bis zum Bildrand. Vorher wurde der Bildschirm ~100× übermalt —
  das war der Löwenanteil der Frame-Zeit, mit Höhenfärbung doppelt teuer.
  Gemessen (M-Serie, 1280×659 css, mode=flug, pal=1): vorher Ø 33 ms
  (~30 fps, p95 67 ms), nachher Ø 16.6 ms (stabile 60 fps, p95 17 ms) —
  schneller als der alte Renderer sogar ohne Färbung (Ø 21 ms).
  Nachbesserung gleichentags, zweiteilig: (a) der untere Fill-Rand nimmt
  pro Spalte das Maximum aus EV[c-1..c+1], nicht nur EV[c] — kreuzen sich
  Kanten näherer Scheiben steil zwischen zwei Spalten, blieben sonst Keile
  offen. (b) Überlappung von 2 auf 10 px erhöht — an steilen Zacken-
  Segmenten deckte 2 px die AA-Kanten nicht satt ab, Papier flimmerte
  durch (Fills wirkten leicht transparent). Weiche Gradient-Stops als
  Alternative getestet und verworfen: User will die harten Farbstufen.
  Mit 10 px weiterhin stabile 60 fps.
- Höhenlinien-Look wie im Wiki: pro Scheiben-Band (Zelle = 2 Spalten × 2
  Scheiben) Marching Squares über die 32 Höhenstufen (`ZMAX/L`), Schnittpunkte
  in Bildkoordinaten interpoliert, direkt nach dem Fill der näheren Scheibe
  gestrichelt — nähere Fills übermalen verdeckte Segmente. Die horizontalen
  Scheiben-Profillinien laufen nur noch dezent mit (alpha×0.3) als
  Silhouetten-Kante. Kosten: ~3.6 ms/Frame (gemessen).
- Kamera: `fc={x,y,z,hx,hy,horizon}`. Route pro Überflug: quadratische
  Bezierkurve, Start R0=4.3 (weit draussen überm Meer), Wegpunkt nahe
  Inselmitte, Exit R1=2.4 (direkt hinter der Küste). Routenwahl deterministisch
  pseudozufällig über `mulberry32(fi)`, fi = globaler Überflug-Index.
- Blick immer geradeaus (Flugrichtung = Bezier-Ableitung). Kein Seitenblick
  mehr (war drin, auf User-Wunsch entfernt).
- Flughöhe: max(0.46, Gelände+0.15), sanft nachgeführt, am Segmentstart hart
  gesetzt. Horizont bei 0.30·H mit leichtem Wogen. Brennweite fl=H*1.15.
- Kein Banking mehr (auf User-Wunsch entfernt, 17. Juli 2026): `roll` bleibt
  im Flug 0, der Horizont waagrecht. Die Canvas-Rotations-Hooks in
  drawFlight und draw sind noch da, falls es je zurückkommt.
- Labels: perspektivisch projiziert, Schrift skaliert mit 1/Distanz
  (0.85–1.5×), Verdeckung per 3D-Sichtstrahl (`peakVisibleP`), Budget 84
  (früher 28, auf User-Wunsch verdreifacht), gleiche Stapel-Bremse.

## Höhenfärbung (17. Juli 2026)

Beide Renderer färben die Ringe nach Höhenstufe (hypsometrisch, pastell).
Standard ist Palette 1 «Meer»: Landfarben des Atlas-Klassikers
(User-Vorlage, 35% Richtung Papierweiss aufgehellt — Grün → Gelb → Ocker →
Rost → Braunrot → Grau → Weiss) plus Navy-Meer und Himmel. Die Paletten
2–6 (sonnig, kühl, sepia-nah, hypsometrisch, Atlas-Klassiker pur mit
Papier-Hintergrund = früherer Standard) bleiben als Alternativen im
`PALETTES`-Objekt gespeichert, umschaltbar per `?pal=N`.

Meer und Himmel (nur Palette 1, also auch ohne `?pal`-Parameter):

- Meerfarbe `SEA_RGB` helles Navy statt Papier — Hintergrund,
  Flug-Gradient unterhalb Ring 5 und Blendfarbe hängen an dieser
  Konstante, die Insel liegt sichtbar im Meer.
- Im Flugmodus ist der Hintergrund zweigeteilt (`SKY`-Konstante):
  Himmel-Verlauf oberhalb von `horizonY` (tiefes Blau → Teal → Creme,
  Vintage-Bildvorlage), Meer darunter — sonst gäbe es ohne Horizontlinie
  keine Tiefenwirkung.
- Das Meer ist tiefengestaffelt (`seaMix`): nah `SEA_RGB`, am Horizont
  `SEA_FAR_RGB` (dunkles Navy); die Scheiben-Gradients mischen pro
  Scheibe über k/(SLICES−1). Das Hintergrundband hinter den Scheiben ist
  flach im dunkelsten Ton (`seaMix(1)`) — Verlaufsvarianten (linear und
  log-perspektivisch) erzeugten an der Naht zur fernsten Scheibe einen
  sichtbaren Balken unter dem Horizont.

Mit `?pal=2…6` bleibt der Hintergrund einfarbig Papier.

- `ringColor(l)`: Stufe l (1..L) → Farbe, lineare Interpolation über
  Stützpunkte `[t, [r,g,b]]` mit t=l/L.
- Orbit: `fillStyle=ringColor(l)` pro Ring-Ebene (Wände inklusive),
  Konturlinien bleiben braun.
- Flug: pro Tiefenscheibe ein linearer Gradient mit harten Stufen — die
  Bildhöhe ist pro Scheibe linear zur Geländehöhe, darum stimmen die
  Bänder exakt mit dem Orbit überein. Küstenband unter Ring 5 und Meer
  bekommen die Meerfarbe `SEA` (Palette 1: helles Navy, sonst Papier). Alle
  Scheiben-Gradients werden EINMAL vorberechnet
  (`buildGrads`; Länge fl·(ZMAX−seaZ)/zc ist zeitlich konstant, ungültig
  nur bei Resize) und pro Frame bloss vertikal verschoben (translate).
  Verworfen nach Messung: Gradients pro Frame neu bauen (+12 ms) und ein
  einziger Gradient unter scale()-Transform (+29 ms, verlässt den
  schnellen Render-Pfad).
- Palette-Leiste (Arbeitswerkzeug): mit `?pal=N` erscheinen rechts 32
  Boxen (oben Stufe 32), beschriftet 1–32, mit der aktiven Palette;
  abgeblendet, was nie als Ring erscheint (Stufe 32 und alles unter
  BASECUT, aktuell 1–4). Ohne `?pal` keine Leiste. Aktuell deaktiviert:
  der `buildPalette()`-Aufruf im Start-Block ist auskommentiert, Code
  (CSS `#pal`, div, Funktion) bleibt drin — für Farbarbeit wieder
  einkommentieren.
- Gezeichnete Ringe: `L=32` Stufen, Konturschleife l=1–31, BASECUT=0.14
  kappt 1–4 → sichtbar sind die Stufen 5–31 (27 Ringe).

## URL-Parameter

- `?pal=N` — Palette 1–6 umschalten und Palette-Leiste einblenden
  (Standard ohne Parameter: Palette 1, keine Leiste; ungültige Werte
  wirken wie kein Parameter).

- `?speed=N` — Zeitraffer (Testen; N beliebig, ohne = 1).
- `?mode=flug` / `?mode=orbit` — Modus fixieren; ohne: Wechsel-Zyklus.
- `?noexit=1` — Exit-Events deaktiviert (Testen mit Mausbewegung).
- `?labels=N` — Label-Maximum im FLUG (statt 84). Im Orbit ohne Wirkung,
  seit dort die Zoom-Rampe gilt.
- `?zoom=N` — friert den Orbit-Zoom auf N ein (keine Atmung), zum Tunen.
- Verworfen: `?render=flug` (Perspektiv-Renderer als Orbit) — getestet und
  vom User abgelehnt, Orbit bleibt orthografisch.
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

- User-Vorgaben umgesetzt: Orbit fixiert auf Inselmitte; Flug nur geradeaus;
  Start weit ausserhalb; Fades statt Schnitten; Flug 8× langsamer, Orbit 2×
  langsamer als die erste Fassung; Highlight-Wechsel 30 s; Routenende −40 s;
  zuerst 3 Überflüge pro Zyklus, später reduziert auf 1 Überflug mit
  doppelt langem Orbit davor (400 s).
- `LABEL_TOP=21` wie im Original (21 Millionen).
- DESIGN.md gilt: eine Farbfamilie, Systemschrift. Kartusche und HUD wurden
  wieder entfernt — die Seite zeigt nur den Canvas (plus #err-Fallback).
- Flugmodus rendert seit dem Höhenlinien-Umbau OHNE die horizontalen
  Scheiben-Profillinien (testweise entfernt, User zufrieden). Dafür gibt es
  eine Silhouettenkante: pro Spalte wird die oberste Landkante über alle
  Scheiben mitgeführt (`skyY`) und am Schluss als eine Linie gestrichen.
- Label-Rampe: final hoch 6 mit Untergrenze 21 und Obergrenze 42.

## Offene Ideen

Keine. Entschieden: Der Zyklus bleibt fix Orbit → Flug → Orbit → Flug
(NCROSS=1, endlos); eine variable Überflug-Anzahl ist ausdrücklich nicht
gewünscht. Früher erledigte Ideen: Idle-Trigger in index.html (42 s);
Höhenlinien-Look im Flugmodus (Marching Squares auf Tiefenscheiben);
Silhouettenkante im Flugmodus (skyY-Envelope).
