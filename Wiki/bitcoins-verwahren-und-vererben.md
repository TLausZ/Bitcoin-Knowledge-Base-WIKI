# Bitcoins verwahren und vererben (Marc Steiner)

**Status:** established
**Themen:** self-custody, buecher
**Last updated:** 2026-07-13
**Sources:** [[2020_Bitcoins-verwahren-und-vererben_Steiner]]

## Summary

Marc Steiners praktischer Ratgeber (Aprycot Media, 2020, Vorwort von Jonas Schnelli) behandelt eine Lücke, die die meiste Bitcoin-Literatur auslässt: Wie sichert man Coins so, dass sie weder zu Lebzeiten verloren gehen noch nach dem Tod für die Erben unerreichbar werden? Kern des Buches ist der individuelle Nachlassplan; dazu liefert Steiner ein kostenloses Hilfstool. Thomas Lohbeck ist in der Danksagung unter den Gesprächspartnern genannt (im Druck als „Thomas Lobeck").

## Body

### Ausgangsproblem

Bitcoin macht dich zur eigenen Bank, mit der Kehrseite, dass es keine Helpline gibt. Die „Null-Fehler-Toleranz" der Kryptowelt gilt auch beim Vererben: Coins an eine falsche Adresse oder ein verlorener Schlüssel sind in der Regel endgültig weg. Steiners Leitsatz ist der Szene-Klassiker „Nur wer seine Bitcoins selber verwaltet, besitzt Bitcoins". Daraus folgt für ihn: Jeder Bitcoin-Besitzer braucht einen Nachlassplan, und zwar solange er bei klarem Verstand und guter Gesundheit ist.

### Verwahrungs-Entscheidungen (Buch-Logik)

Steiner führt schrittweise durch die Wallet-Typen und leitet daraus ab, was sich fürs Erbe eignet:

- **Custodial vs. non-custodial:** Custodial (Börse/Kryptobank hält die Schlüssel) ist bequem, aber Fremdverwahrung, einfrierbar, hackbar, und beim Erbfall problematisch, weil das Einloggen mit dem Namen des Verstorbenen mancherorts strafbar ist. Fürs Erbe klar abgelehnt.
- **Cold vs. hot storage:** Hot-Wallets (permanent online) nur für Kleinbeträge, „nicht mehr, als du Bargeld in der Brieftasche trägst". Für langfristige Verwahrung und Erbe ausschliesslich Cold Storage.
- **Fazit des Buches:** non-custodial + cold ist die einzige Basis, auf der ein mehrjähriger Nachlassplan aufsetzt.

### Werkzeuge für Sicherung und Vererbung

Das Buch behandelt die gängigen Bausteine und wie sie im Nachlassplan zusammenspielen:

- **Hardware-Wallet** als Cold-Storage-Gerät.
- **Seed-Backup** (12/24 Wörter), möglichst metallgestanzt gegen Feuer/Wasser.
- **Passphrase** als 25. Wort, zusätzlicher Schutz, aber auch zusätzliche Verlustquelle, die im Plan bedacht sein muss.
- **Shamir Secret Sharing**, Aufteilung des Seeds in mehrere Teile, von denen eine Schwelle zur Wiederherstellung genügt.
- **Multisig** als kryptografisches Mehr-Augen-Prinzip, bei dem mehrere Schlüssel für eine Ausgabe nötig sind.
- **Schliessfach/Tresor** zur räumlich getrennten Ablage von Teilgeheimnissen.

### Der Nachlassplan

Das eigentliche Thema ist die Choreografie für den Ernstfall. Steiner betont die zentrale Spannung: Der Plan muss zugänglich genug sein, dass die Erben (für die Bitcoin meist Neuland ist) Schritt für Schritt an die Coins kommen, und zugleich sicher genug, dass niemand zu Lebzeiten das Guthaben abräumt. Beide Fehlrichtungen sind fatal: offen herumliegende Zugangsdaten laden Angreifer ein, zu gut versteckte machen das Erbe unauffindbar.

Praktische Elemente des Plans:

- Eine verständliche Schritt-für-Schritt-Anleitung für Erben, nicht nur die nackten Zugangsdaten.
- Trennung von Geheimnisträgern (z. B. Seed-Teile bei verschiedenen Personen/Orten), damit kein Einzelner allein Zugriff hat.
- Einbindung von Testament und rechtlicher Ebene neben der technischen.
- Steiners kostenloses Hilfstool zur strukturierten Erfassung der eigenen Situation.

Das Buch versteht sich ausdrücklich als Inspirationsquelle und Nachschlagewerk, das an Punkte erinnert, die man selbst übersehen würde, nicht als starre Vorschrift. Steiner ermutigt, auch unkonventionelle Vererbungswege zu prüfen.

## Related

- [[selbstverwahrung-und-boersenrisiken]]
- [[hardware-wallet-einstieg]]
- [[wallet-backup-strategien]]
- [[multisig-und-kollaborative-verwahrung]]
- [[fortego-backup-sicherheit]]
- [[miniscript-und-liana]]
- [[diceware-und-seed-generierung]]

## Open Questions

- Wie viel Redundanz (Shamir/Multisig) ist für einen typischen Privatanleger sinnvoll, bevor die Komplexität selbst zum Verlustrisiko wird?
- Wie hält man einen Nachlassplan über Jahre aktuell, wenn sich Geräte, Wohnorte und Erben ändern?
- Trägt die rechtliche Ebene (Testament) international, oder scheitert der Plan an Jurisdiktionsgrenzen?
