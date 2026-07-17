# Bitcoin Development Philosophy (Kalle & Linnea Rosenbaum)

**Status:** established
**Themen:** protokoll, privacy, philosophie, buecher
**Last updated:** 2026-07-13
**Sources:** [[Bitcoin-Development-Philosophy_Rosenbaum]]

## Summary

Kalle und Linnea Rosenbaum (2024, Konsensus Network) beschreiben nicht, wie Bitcoin technisch funktioniert, sondern nach welchen Werten es entwickelt wird. Das Buch macht die Prinzipien explizit, an denen jede vorgeschlagene Änderung gemessen wird: Dezentralisierung, Vertrauenslosigkeit, Privatsphäre, Fungibilität und das feste Angebot. Daraus erklärt sich, warum Bitcoin so vorsichtig und langsam verändert wird. Das Buch steht unter der freien Lizenz CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/).

## Body

### Dezentralisierung und Zensurresistenz

Das erste und tragende Kapitel trennt zwei Formen der Dezentralisierung: die der Miner und die der Full Nodes. Zensurresistenz, für die Rosenbaums die zentrale Eigenschaft von Bitcoin, hängt an beiden. Fehlt sie, könnte ein Zensor Nutzer zu neuen Regeln zwingen, etwa einer Ausweitung der Geldmenge zu seinem eigenen Vorteil. Ein Nutzer, der Blöcke selbst verifiziert, hat in einem solchen Fall die Wahl, die erzwungene Regel abzulehnen. Deshalb ist der eigene Full Node kein Detail, sondern das Fundament der Selbstverteidigung. Bitcoin ersetzt die Abstimmung von Personen (die eine zentrale Instanz zum Zulassen der Wähler bräuchte) durch eine Abstimmung mit Rechenleistung, die sich ohne Erlaubnis überprüfen lässt.

### Vertrauenslosigkeit

„Don't trust, verify" ist mehr als ein Slogan. Der Wert der Vertrauenslosigkeit bedeutet, dass jeder Nutzer die Regeln selbst durchsetzt, statt einer Autorität zu glauben. Proof-of-Work erlaubt erlaubnisfreie Teilnahme, es gibt keine feste Gruppe, die deine Änderungen zensieren kann. Die Autoren sind ehrlich über den Preis: Dieser Mechanismus ist teuer und seine ökonomischen Annahmen machen ihn im Grunde nur für ein System wie Geld sinnvoll, nicht für beliebige Anwendungen.

### Privatsphäre und Fungibilität

Ein eigener Block behandelt Privatsphäre: was sie bedeutet, warum sie wichtig ist, und der Unterschied zwischen Pseudonymität und echter Anonymität. Die Autoren trennen On-Chain- von Off-Chain-Privatsphäre und verbinden das Thema mit Fungibilität, der Austauschbarkeit einzelner Coins. Fehlende Privatsphäre bedroht Fungibilität, weil markierte oder nachverfolgbare Coins ungleich behandelt werden könnten. Privatsphäre ist damit keine Bequemlichkeit, sondern eine Bedingung dafür, dass Bitcoin als neutrales Geld funktioniert.

### Festes Angebot und das Fee-Modell

Das feste Angebot wird als Wert behandelt, nicht als blosse Zahl. Die Autoren erklären den Übergang vom Block-Subsidy hin zu den Transaktionsgebühren als langfristige Sicherheitsfrage: Wenn die neue Ausgabe versiegt, müssen Gebühren die Miner tragen. Das ist eine offene Designspannung, die das Buch benennt, statt sie zu glätten.

### Upgrades und adversariales Denken

Beim Ändern des Protokolls führen die Autoren das Vokabular ein (Soft Fork, Hard Fork), zeigen die historischen Upgrades und betonen die Risiken jeder Konsensänderung. Der Schlüssel ist adversariales Denken: Man muss annehmen, dass Angreifer existieren, und jede Änderung aus deren Perspektive prüfen. Dieses Denken ist ausdrücklich nicht nur Sache der Experten, weil am Ende die Nutzer über ihre Nodes entscheiden.

### Open Source und die Entwicklungskultur

Ein grosser Teil widmet sich der Frage, wie an Bitcoin überhaupt gearbeitet wird: Softwarepflege, erlaubnisfreie und pseudonyme Mitarbeit, die zentrale Rolle des Code-Review, die schwierige Finanzierung und der „Culture Shock", den neue Entwickler erleben. Wer ohne Erlaubnis beitragen kann, kann auch angreifen, deshalb ist Review die eigentliche Absicherung.

### Skalierung und eine geprägte Kultur

Das Skalierungskapitel erzählt die Geschichte, die Ansätze und den Ernstfall („when shit hits the fan"), inklusive verantwortungsvoller Offenlegung von Sicherheitslücken. Der Begriff „traumatic childhood" fasst die These des Buches zusammen: Die vorsichtige, konservative Kultur der Bitcoin-Entwicklung ist das Ergebnis harter Erfahrungen wie des Blocksize-Kriegs. Wer verstehen will, warum Bitcoin sich nur langsam ändert, findet hier die Begründung.

## Related

- [[blocksize-war]]
- [[grokking-bitcoin]]
- [[soft-fork-und-hard-fork]]
- [[konsensregeln-und-mempool-richtlinien]]
- [[bitcoin-zensurresistenz]]

## Open Questions

- Die konservative Kultur schützt die Kerneigenschaften, kann aber auch nützliche Änderungen blockieren: Wo verläuft die Grenze zwischen Vorsicht und Stillstand?
- Das Fee-Modell nach dem Auslaufen des Subsidy bleibt offen: Reichen Gebühren, um die Sicherheit langfristig zu tragen?
- Wie tragfähig ist die erlaubnisfreie, oft unterfinanzierte Entwicklung, wenn immer mehr wirtschaftlicher Wert von wenigen Reviewern abhängt?
