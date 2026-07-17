# PGP und Verschlüsselungspolitik

**Status:** established
**Themen:** protokoll
**Last updated:** 2026-06-09
**Sources:** [[1991_Why I Wrote PGP]], [[2017_Fog of CryptoWar]]

## Summary

Philip Zimmermanns PGP (1991) war die erste breite Implementierung starker Ende-zu-Ende-Verschlüsselung für Privatpersonen — erschienen als direkte Antwort auf einen US-Gesetzentwurf, der Backdoors in Kommunikationssoftware vorgeschrieben hätte. Die Geschichte der Krypto-Kriege zeigt, wie Regierungen wiederholt versucht haben, Verschlüsselung zu kontrollieren, und warum sie bisher gescheitert sind. Bitcoins Zensurresistenz fusst auf denselben kryptographischen Grundlagen, die Zimmermann und die Cypherpunks in den 1990ern erkämpften.

## Body

### Warum Zimmermann PGP veröffentlichte

Der direkte Auslöser war Senate Bill 266 (1991), ein US-Omnibus-Verbrechensgesetz, das in einer unscheinbaren Klausel vorschrieb: Anbieter sicherer Kommunikation und Hardware-Hersteller müssten sicherstellen, dass Regierungsbehörden im Bedarfsfall auf den Klartext jeder Kommunikation zugreifen können.

Zimmermann sah das als Angriff auf eine Grundfreiheit — nicht die Freiheit zu kriminellen Aktivitäten, sondern die natürliche Privatsphäre, die zuvor durch die Physik garantiert war: Ein Brief in einem Umschlag war privat, weil das Öffnen Aufwand erforderte. Mit elektronischer Kommunikation sei dieses "Gesetz der Physik" verschwunden — und ohne aktive Verschlüsselung seien alle E-Mails wie Postkarten, lesbar für jeden mit Netzzugang.

Die Analogie: Wenn alle Briefe auf Postkarten verschickt würden und man plötzlich anfinge, Umschläge zu benutzen, würde man verdächtig wirken. Wenn aber alle Umschläge benutzen, ist niemand verdächtig. Verschlüsselung als gesellschaftliche Norm — nicht als Geheimhaltung — war Zimmermanns Argument.

### Die FBI-Ermittlung gegen Zimmermann

Nach der Veröffentlichung von PGP als Freeware wurde Zimmermann drei Jahre lang vom FBI untersucht — wegen möglichen Verstosses gegen US-Exportkontrollgesetze für Kryptographie. Software mit starker Verschlüsselung galt damals als Rüstungsgut, das nicht ohne Genehmigung exportiert werden durfte. Die Ermittlung wurde 1996 eingestellt.

Das Paradox: Zimmermann hatte PGP im eigenen Land veröffentlicht — andere hatten es ins Ausland hochgeladen. Aber die Ermittlung zeigte, wie ernst die US-Regierung die Kontrolle über Verschlüsselungstechnologie nahm.

### Die CALEA und Wiretapping-Infrastruktur (1994)

Unabhängig von PGP verabschiedete der US-Kongress 1994 den Communications Assistance for Law Enforcement Act (CALEA): Telekommunikationsanbieter mussten "Remote-Wiretapping-Ports" in ihre digitalen Vermittlungsstellen einbauen. FBI-Agenten konnten fortan von Washington aus Telefonleitungen abhören, ohne physischen Zugang zum Netz.

Zimmermanns Argument: Technologische Infrastruktur überlebt politische Systeme. Einmal eine Überwachungsinfrastruktur gebaut, kann ein politischer Klimawechsel diese Infrastruktur missbrauchen lassen. Die Warnung bleibt relevant.

### Erster Krypto-Krieg: Clipper Chip (1993–1996)

Die NSA entwickelte den Clipper-Chip — einen Verschlüsselungschip für Telefone mit eingebautem Key Escrow: Zwei Regierungsbehörden würden je die Hälfte des Schlüssels halten. Die Begründung war "Strafverfolgung", der reale Effekt wäre universelle staatliche Abhörmöglichkeit gewesen.

Die Cypherpunk-Community leistete massiven Widerstand. Matt Blaze fand 1994 eine kryptographische Schwäche im Clipper-Protokoll. Die Initiative scheiterte an einer Kombination aus technischen Problemen, öffentlichem Widerstand und der Erkenntnis, dass ausländische Nutzer und Unternehmen einfach auf andere Verschlüsselung ausweichen würden.

### Zweiter Krypto-Krieg: Post-Snowden (2013–2017)

Nach Snowdens Enthüllungen (2013) begannen Apple und Google, ihre Geräte standardmässig vollständig zu verschlüsseln. FBI-Direktor James Comey reagierte mit der Forderung nach "Going Dark"-Gesetzgebung: Ende-zu-Ende-Verschlüsselung mache Strafverfolgung unmöglich.

Jonathan 'smuggler' Logan analysierte 2017 den wesentlichen Unterschied zum ersten Krypto-Krieg: Regierungen verlangen heute keine technische Backdoor-Spezifikation mehr. Sie formulieren das Ziel ("Terroristen dürfen keine sicheren Kommunikationsräume haben") und überlassen die Lösung dem Markt und der Industrie. Dieser vagere politische Druck ist schwerer zu bekämpfen, weil es keinen Clipper-Chip gibt, dessen kryptographische Schwäche man demonstrieren könnte.

Logans Hauptthese: Die Debatte wird in den Medien als "Sicherheit vs. Privatsphäre" framed — als ob beides echte Güter wären, die abgewogen werden müssten. In Wahrheit führen Backdoors strukturell zu weniger Sicherheit für alle, weil dieselbe Hintertür auch von Angreifern genutzt werden kann.

### Relevanz für Bitcoin

Bitcoin ist kryptographisch mit denselben Mitteln gesichert, die Zimmermann und die Cypherpunks in den 1990ern erkämpften. Elliptische Kurvenkryptographie, Hashing, digitale Signaturen — all das war durch den Export-Streit der 1990er zeitweilig bedroht. Eine Welt, in der starke Kryptographie 1991 verboten worden wäre, wäre eine Welt ohne Bitcoin.

## Related

- [[kryptoanarchismus-und-cypherpunks]]
- [[cypherpunk-manifest]]
- [[opsec-und-privatsphaere]]
- [[anti-klepto-und-supply-chain-sicherheit]]

## Open Questions

- Wie verhält sich die Diskussion über Ende-zu-Ende-Verschlüsselung in der EU nach der Chat Control-Abstimmung?
- Führt die Proliferation von KI-Überwachung zu einem dritten Krypto-Krieg anderer Qualität?
