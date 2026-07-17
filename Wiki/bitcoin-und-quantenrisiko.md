# Bitcoin und Quantenrisiko

**Status:** established
**Themen:** protokoll, self-custody
**Last updated:** 2026-07-17
**Sources:** [[Bitcoin and Quantum Risk_ What Actually Matters]], [[core-lightning-26-06]], [[bip-0451]], [[2025-11-20_Charles Edwards - Bitcoin's Headwinds and the Quantum Threat]], [[2026-07-04_Bitcoin Is Cheap. But Is It Cheap Enough]]

## Summary

Quantencomputer könnten theoretisch die elliptische Kurven-Kryptographie (ECDSA) brechen, auf der Bitcoin-Adressen basieren. Das Risiko ist real, aber falsch eingeordnet: Kryptografisch relevante Quantencomputer existieren heute nicht, der Angriff wäre selektiv statt global, und Bitcoin hat einen funktionierenden Upgrade-Mechanismus. Der häufigste Fehler im öffentlichen Diskurs ist der Sprung von "Quantencomputer werden irgendwann mächtig" direkt zu "Bitcoin ist kaputt". Dabei wird der einzige relevante Teil übersprungen: ob solche Systeme tatsächlich gebaut, skaliert und gegen reale Ziele eingesetzt werden können.

## Body

### Der wichtigste Unterschied: Theorie und Praxis

Eine theoretische Möglichkeit ist kein praktischer Angriff. Das klingt trivial, wird aber im öffentlichen Diskurs konstant verwechselt.

Auf einem ausreichend grossen Quantencomputer kann Shors Algorithmus aus einem öffentlichen Schlüssel den privaten Schlüssel berechnen und damit ECDSA brechen. Die theoretischen Grundlagen dafür sind seit 1994 bekannt. Was sich seither kaum verändert hat: die Hardware.

Für einen kryptografisch relevanten Angriff auf ECDSA-256 sind schätzungsweise 2.000 bis 4.000 fehlerkorrigierte logische Qubits nötig. Fehlerkorrektur erfordert je nach Verfahren 10x bis 1.000x mehr physische Qubits. IBMs beste Systeme (2024: 433 physische Qubits) sind davon noch weit entfernt. Konsensschätzungen der Kryptographie-Gemeinschaft sehen einen ernsthaften Angriff frühestens in 10 bis 30 Jahren. Wankum (TBN #37) formuliert es direkt: "As of today, that remains far from practical reality." [[Bitcoin and Quantum Risk_ What Actually Matters]]

### Bitcoin ist nicht das einzige Ziel

Wenn Quantencomputer jemals ECDSA brechen könnten, wäre Bitcoin nicht der einzige betroffene Bereich. Dieselbe kryptografische Grundlage schützt Bankinfrastruktur, Militärkommunikation und Internet-TLS. Ein Angriff auf Bitcoin wäre gleichzeitig ein Angriff auf praktisch alle digitalen Systeme der Gegenwart.

Das ändert den Risikorahmen grundlegend. Quantencomputing ist ein Problem für die gesamte digitale Infrastruktur, nicht für Bitcoin allein. Der Druck zur Lösung würde aus allen Branchen gleichzeitig kommen. [[Bitcoin and Quantum Risk_ What Actually Matters]]

### Wo das Risiko tatsächlich liegt

Bitcoin-Adressen sind zweistufig geschützt: erst durch SHA-256/RIPEMD-160 (Hashing des Public Keys zur Adresse), dann durch ECDSA (Signatur mit privatem Schlüssel beim Ausgeben).

Shors Algorithmus greift die zweite Schicht an, kann aber nur dann angewandt werden, wenn der öffentliche Schlüssel bekannt ist. Das ist nur in zwei Situationen der Fall.

**P2PK-Adressen** (älteres Format, Satoshis frühe Transaktionen): Der öffentliche Schlüssel ist direkt in der Adresse gespeichert und dauerhaft sichtbar. Schätzungsweise 1 bis 2 Millionen BTC liegen in solchen Adressen. Sie sind die logischen Erstziele eines Quantenangriffs.

**Bereits ausgegebene Adressen**: Wer eine Adresse bereits für eine Ausgabe genutzt hat, hat dabei seinen öffentlichen Schlüssel auf der Blockchain hinterlassen. Das ist einer der Hauptgründe, warum Bitcoin-Adressen nicht wiederverwendet werden sollten.

Native SegWit (bc1q) und Taproot-Adressen (bc1p) zeigen nur einen Hash des öffentlichen Schlüssels. Ein Quantencomputer müsste erst diesen Hash umkehren (SHA-256 via Grovers Algorithmus, der das Problem quadratisch beschleunigt, bei 256-Bit-Hash aber immer noch 2^128 Operationen erfordert) und dann ECDSA brechen. Zwei aufeinanderfolgende Angriffe, nicht einer.

Für unverwendete moderne Adressen gilt zusätzlich: Der öffentliche Schlüssel wird erst sichtbar, wenn eine Transaktion gesendet wird. Ein Angreifer müsste im Zeitfenster zwischen Broadcast und Bestätigung (Minuten bis Stunden) den ECDSA-Angriff abschliessen. Mit heutiger Quantenhardware ausgeschlossen. [[Bitcoin and Quantum Risk_ What Actually Matters]]

BIP-451 (Dust UTXO Disposal Protocol, 2026) adressiert einen verwandten Punkt: Das Ausgeben von Dust-UTXOs offenbart den öffentlichen Schlüssel der betroffenen Adresse. Bei einer Adresse, die danach weiter genutzt wird, entsteht so eine potenzielle Schwachstelle für die Zukunft. [[bip-0451]]

### Bitcoin kann upgraden: BIP-361

Bitcoin ist kein statisches System. Es hat kryptografische Upgrades bereits mehrfach durchgeführt: P2SH (2012), SegWit (2017), Taproot/Schnorr (2021). Quantenresistente Signaturen sind der nächste logische Schritt.

Bitcoin-Entwickler haben 2026 einen konkreten Migrationspfad vorgeschlagen: BIP-361. Der Plan umfasst drei Elemente: Einführung eines neuen Adresstyps mit quantenresistenten Signaturen (Kandidaten sind Lattice-basierte Verfahren wie CRYSTALS-Dilithium und Hash-basierte wie XMSS), aktive Migration der Coins durch Nutzer in diese neuen Adressen analog zum SegWit-Übergang, sowie das mögliche Einfrieren von Legacy-Coins in alten P2PK-Formaten, um den Anreiz für einen Quantenangriff zu eliminieren.

Das erfordert gesellschaftliche Koordination und Vorlaufzeit. Genau dafür ist der lange Zeithorizont des Quantenrisikos hilfreich: Die Community kann sich vorbereiten, bevor die Bedrohung real wird.

Core Lightning 26.06 (Juni 2026) enthielt erste experimentelle Quantum-Resistant Channel-Funktionalität als frühen Schritt in diese Richtung. [[core-lightning-26-06]]

### Eine aggressivere Zeitschätzung (Charles Edwards)

Nicht alle Stimmen teilen den 10-bis-30-Jahre-Konsens. Der Marktanalyst Charles Edwards (Capriole) vertritt in Pascal Hüglis Less-Noise-More-Signal-Podcast eine deutlich kürzere Frist: Quantencomputer könnten die elliptische Kurven-Kryptographie in zwei bis zehn Jahren brechen, mit vier bis fünf Jahren als wahrscheinlichstem Fenster. Er stützt sich dabei auf Einschätzungen aus dem Quanten-Umfeld, verweist auf Jameson Lopp und auf McKinsey-Berichte und zählt die Bedrohung zu den Gegenwinden für Bitcoin. [[2025-11-20_Charles Edwards - Bitcoin's Headwinds and the Quantum Threat]]

Die Schätzung liegt am aggressiven Rand des Spektrums und ist die eines Markt-Analysten, nicht der Kryptographie-Community; sie liegt zudem nur als Podcast-Zusammenfassung vor. Als Datenpunkt ist sie dennoch nützlich: Selbst wenn man das kürzere Fenster ernst nimmt, verschiebt es die Dringlichkeit des Migrationspfads (BIP-361), ohne die Grundlogik zu ändern — entscheidend bleibt, ob Bitcoin rechtzeitig auf quantenresistente Signaturen umstellt. Gästeüberblick in [[bitcoin-marktkommentar-lnms]]. In einer Hausanalyse vom Juli 2026 schärft Hügli mit Edwards den ökonomischen Kern des Arguments: Nicht der Angriff selbst, sondern die ungelöste Unsicherheit ist das Problem. Grosse Kapitalgeber können ein unaufgelöstes Tail-Risiko nicht «underwriten» und reduzieren im Zweifel ihr Engagement — der Quanten-Overhang wirkt so als Kapitalbremse, lange bevor ein realer Angriff möglich wäre. [[2026-07-04_Bitcoin Is Cheap. But Is It Cheap Enough]]

### Das falsche mentale Modell

Viele Bedenken gegen Bitcoin basieren auf dem Rahmen "Wenn ein Risiko existiert, ist das System ungültig." Das ist die falsche Prüfung.

Wankum formuliert es als Gegenfrage: Wenn theoretisches Quantenrisiko ausreicht, um Bitcoin abzulehnen, müssen dieselben Kriterien auch Bankkonten, Zahlungsinfrastruktur und Cloud-Infrastruktur ablehnen, da all das auf denselben kryptografischen Grundlagen beruht.

Die relevante Prüfung lautet: Kann das System sich anpassen, und sind die Anreize dazu stark genug?

Bitcoin besteht diese Prüfung aus einem strukturellen Grund. Es ist open-source und dezentralisiert, und alle Beteiligten (Nutzer, Entwickler, Miner, Unternehmen) haben einen direkten ökonomischen Anreiz, die Integrität des Systems zu erhalten. Ein zentralisiertes System wartet auf eine Entscheidung einer Institution. Bitcoin wartet auf Konsens unter Tausenden von Akteuren mit gleichgerichteten Interessen. [[Bitcoin and Quantum Risk_ What Actually Matters]]

### Was Anfänger wissen müssen

Für jemanden, der heute Bitcoin kauft und verwahrt: Das Risiko ist nicht null, aber für normale Nutzer mit modernen Adressformaten (bc1q, bc1p) und ohne Adressenwiederverwendung heute nicht relevant.

Das Zeitfenster bis zu einem ernsthaften Quantenangriff ist lang genug, dass Bitcoin-Entwickler Gegenmassnahmen entwickeln und einsetzen können, und das tun sie bereits.

Die eigentliche Frage ist, ob Bitcoin vor einem Quantenangriff upgraden kann. Die Antwort ist ja, aus denselben Gründen, aus denen SegWit und Taproot möglich waren: Der Konsens entsteht, wenn die Notwendigkeit klar genug ist.

## Related

- [[elliptische-kurven-kryptographie]]
- [[taproot-musig2-frost]]
- [[bitcoin-regierungsresistenz]]
- [[bitcoin-antifragilitaet]]
- [[core-lightning-26-06]]
- [[bitcoin-adresstypen]]
- [[kryptografische-schlussel-und-adressen]]
- [[starks]]
- [[bitcoin-marktkommentar-lnms]]

## Open Questions

- Ab welchem Qubit-Stand sollte die Bitcoin-Community ernsthaft mit einem Post-Quantum-Soft-Fork beginnen?
- Welches Post-Quantum-Signaturverfahren ist für Bitcoin am besten geeignet (Signaturgrösse, Kompatibilität, Sicherheitsniveau)?
- Was passiert mit Satoshis P2PK-Coins: Werden sie als Teil von BIP-361 eingefroren, und ist das ein sinnvoller Präzedenzfall?
- Wie verändert sich das Dust-UTXO-Risiko, wenn Quantencomputer den Zeitrahmen für Public-Key-Angriffe verkürzen?
