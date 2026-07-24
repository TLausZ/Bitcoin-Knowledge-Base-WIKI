# Hashcash und Proof-of-Work

**Status:** established
**Themen:** grundlagen, protokoll, mining, geschichte
**Last updated:** 2026-06-17
**Sources:** [[hashcash]], [[bitcoin-whitepaper]]

## Summary

Hashcash ist ein Proof-of-Work-Mechanismus von Adam Back (1997/2002), der ursprünglich gegen E-Mail-Spam entwickelt wurde: Wer eine E-Mail sendet, muss einen Hash berechnen, der eine bestimmte Anzahl führender Nullbits hat — was CPU-Zeit kostet, aber trivial zu verifizieren ist. Satoshi Nakamoto zitiert Back direkt im Bitcoin-Whitepaper und verwendet dasselbe Prinzip für Bitcoin-Mining. Hashcash ist damit die unmittelbare technische Vorstufe von Bitcoins Proof-of-Work-Konsensus.

## Body

### Das Grundprinzip: Asymmetrische Arbeit

Das Kernproblem, das Hashcash löst: Wie kann man verlangen, dass jemand echte Arbeit geleistet hat, ohne eine zentrale Instanz zu brauchen, die das überprüft?

Hashcash löst das elegant: Man fordert, dass der SHA-1-Hash einer Nachricht (plus Nonce) mit einer bestimmten Anzahl Nullbits beginnt. Da Hash-Funktionen deterministisch aber nicht umkehrbar sind, muss man solange verschiedene Nonces probieren, bis eine passt. Das Finden des richtigen Nonce kostet viel CPU-Zeit — das Verifizieren dagegen kostet einen einzigen Hash-Aufruf.

```
Beispiel (vereinfacht):
SHA1("adam@cypherspace.org:1303030600:randonnee") = 0000001a4c3...
                                                      ^^^^ führende Nullbits = Arbeit bewiesen
```

Je mehr führende Nullbits gefordert werden, desto schwieriger die Aufgabe — die Schwierigkeit ist fein einstellbar.

### Ursprung: Anti-Spam (1997)

Back schlug Hashcash 1997 auf der Cypherpunk-Mailingliste als Spam-Schutz vor. Jede ausgehende E-Mail müsste einen Hashcash-Token im Header tragen. Ein Mensch sendet wenige E-Mails — der Rechenaufwand pro Mail ist vernachlässigbar. Ein Spammer, der Millionen Mails verschickt, hätte dagegen einen prohibitiven Rechenaufwand.

Das Prinzip ist nicht neu: Dwork und Naor hatten 1992 eine ähnliche Idee für Anti-Spam formuliert, aber Back entwickelte das erste praktisch einsetzbare System.

### Eigenschaften der Kostenfunktion

Eine gute Proof-of-Work-Kostenfunktion muss:
- **Parametrierbar teuer**: Schwierigkeit einstellbar (z.B. durch Anzahl geforderter Nullbits)
- **Effizient verifizierbar**: Verifikation in einem Hash-Aufruf
- **Nicht delegierbar**: Arbeit muss jedes Mal neu geleistet werden (kein Caching)
- **Zustandslos**: Kein Server muss den Fortschritt kennen

Hashcash erfüllt alle vier — und ist damit ein allgemeines Werkzeug, nicht nur für E-Mail.

### Von Hashcash zu Bitcoin-Mining

Satoshi übernahm das Hashcash-Prinzip für Bitcoin fast unverändert, erweiterte es aber entscheidend:

| | Hashcash | Bitcoin Mining |
|---|---|---|
| Hash-Funktion | SHA-1 | SHA-256 (doppelt) |
| Ziel | Bestimmte Anzahl Nullbits | Hash < Zielwert (difficulty target) |
| Schwierigkeit | Fix pro E-Mail | Automatisch angepasst (alle 2016 Blöcke) |
| Anreiz | Keiner | Block Reward + Gebühren |
| Koordination | Keiner | Globaler Konsens über längste Chain |

Der entscheidende Unterschied: Bitcoin fügt wirtschaftliche Anreize hinzu und nutzt den PoW als Koordinationsmechanismus — nicht nur als Spam-Filter.

### Bedeutung für Bitcoin

Hashcash ist einer von drei direkten technischen Vorläufern, die Satoshi im Whitepaper zitiert:
- **Hashcash** (Back, 1997/2002) → Proof-of-Work
- **b-money** (Wei Dai, 1998) → dezentrales digitales Geld
- **Haber & Stornetta** (1991/1992) → Hash-verkettete Blöcke / Timestamping

Back war auch aktiv in der Entwicklung von Bitcoin involviert und korrespondierte mit Satoshi vor der Veröffentlichung des Whitepapers. Er ist heute CEO von Blockstream.

## Related

- [[bitcoin-whitepaper]]
- [[bitcoin-mining-und-proof-of-work]]
- [[digitales-bargeld-und-ecash]]
- [[kryptoanarchismus-und-cypherpunks]]
- [[digitales-zeitstempel]]
- [[bitcoin-digitale-knappheit]]

## Open Questions

- Warum wechselte Satoshi von SHA-1 zu doppelt-SHA-256 — reine Sicherheit oder andere Gründe?
- Hätte Hashcash als Spam-Filter Erfolg gehabt, wenn es früher bekannt geworden wäre, bevor Spam-Filter effektiv wurden?
