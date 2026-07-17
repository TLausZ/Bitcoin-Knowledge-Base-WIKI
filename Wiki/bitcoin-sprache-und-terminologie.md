# Bitcoin: Sprache und Terminologie

**Status:** established
**Themen:** protokoll, philosophie, kritik
**Last updated:** 2026-06-22
**Sources:** [[aprycot-gigi-woerter-in-bitcoin]]

## Summary

Gigi analysiert in einem Essay (Blockzeit 742573), wie die Sprache rund um Bitcoin sowohl intern ungenau als auch extern als Angriffswerkzeug eingesetzt wird. Alle Bitcoin-Begriffe sind Metaphern — und alle Metaphern scheitern an einem Punkt. Interne Terminologie wie „Wallet", „Schlüssel" oder „Adresse" ist nützlich, aber technisch irreführend. Externe Sprache wie „nicht gehostete Wallet" oder „Proof of Stake" ist dagegen bewusst eingesetzt, um Abhängigkeit zu normalisieren und Bitcoin zu diskreditieren.

## Body

### Warum Metaphern in Bitcoin unvermeidlich sind

Bitcoin hat keinen intuitiven Bezugspunkt. „Es gibt nichts, womit man es in Verbindung bringen könnte", schrieb Satoshi. Jede Erklärung setzt Metaphern voraus — Schlüssel, Wallet, Adresse, Mining, Fork, Seed. George Box' Prinzip gilt: „Alle Modelle sind falsch, aber einige sind nützlich." Das Problem entsteht, wenn die Metapher für die Realität gehalten wird. [[aprycot-gigi-woerter-in-bitcoin]]

### Interne Terminologie: wo die Metaphern versagen

**Wallet.** Eine Bitcoin-Wallet enthält keine Bitcoin. Sie verwaltet kryptografische Schlüssel und ermöglicht das Signieren von Transaktionen. Das Guthaben liegt auf der Blockchain, nicht im Gerät. Präzisere Begriffe entstehen bereits: Hardware Wallets werden zunehmend als „Signaturgeräte" bezeichnet; Multi-Sig-Konstrukte heissen „Tresore". Gigi hofft, den Oberbegriff „Wallet" langfristig aufzugeben.

**Schlüssel.** In der physischen Welt öffnet ein Schlüssel Schlösser. Ein Bitcoin-Private-Key unterschreibt Nachrichten — er ist eher ein Stift als ein Schlüssel. Er ist reine Information: geheime Daten, die niemand ausser dem Eigentümer kennen sollte. Wer diese Information hat, hat die Bitcoin. Die Darstellung als Wortliste (Seed Phrase) macht die Informationsnatur sichtbar: 24 Wörter = Zugang zu allen davon abgeleiteten Schlüsseln und Adressen.

**Adresse.** Luke DasJr hat BIP 179 verfasst, dessen einziger Zweck ist, den Begriff „Adresse" durch „Rechnung" (Invoice) zu ersetzen. Der Grund: Bitcoin-Transaktionen haben keine Absenderadresse. Das Konzept einer „Von-Adresse" ist eine Heuristik, kein Protokollmerkmal. Eine Transaktion enthält nur Skripte — Anforderungen und Lösungen für Anforderungen. Der Invoice-Begriff ist in Lightning bereits Standard und technisch akkurater.

**Münzen.** Das Protokoll kennt keine „Coins". Es gibt nur Sats und ausgabefähige Transaktionsausgaben (UTXOs). „Ein Bitcoin" ist eine Konvention: 100 Millionen Sats. Peter van Valkenburgh: „Erstens gibt es keine Bitcoins. Sie existieren nicht. Es gibt Hauptbucheinträge in einem gemeinsam genutzten Hauptbuch. Sie existieren an keinem physischen Ort." [[aprycot-gigi-woerter-in-bitcoin]]

### Linguistische Angriffe

**„Nicht gehostete Wallet."** Der Begriff impliziert, dass eine Wallet normalerweise „gehostet" sein sollte — und dass das Fehlen des Hostings ein Manko ist. Tatsächlich ist eine selbst verwaltete Wallet der Normalzustand. „Die Cloud ist der Computer von jemand anderem" — eine „gehostete Wallet" ist die Wallet von jemand anderem. Die richtige Framing-Frage: Wer kann auf das Geld zugreifen? Wer kann sperren? Gigi schlägt „unabhängige Wallet" oder „Freiheits-Wallet" vor; das Gegenteil wäre ein „Depotdienst", bei dem man nur einen Erlaubnisschein hält, keine echten Bitcoin. Dass 12 Wörter auswendig lernen regulierbar sein soll, bezeichnet Gigi als „sehr, sehr, (sehr!) dummes Gesetz".

**#ChangeTheCode.** Die Kampagne von Greenpeace, Bitcoin auf Proof of Stake umzustellen, wurde von Chris Larsen finanziert — dem Gründer von Ripple (XRP). Bitcoin ist freie Open-Source-Software unter MIT-Lizenz. Jeder kann den Code ändern, ohne um Erlaubnis zu fragen. Niemand ist gezwungen, die Änderung zu übernehmen. Die Kampagne erklärt sich durch das, was sie angreift: Proof-of-Work ist der Grund, warum permissionslose, zentralisierungsresistente Systeme wie Bitcoin überhaupt funktionieren.

**„Proof of Stake."** Gigi listet, was PoS im Vergleich zu PoW fehlt: kein objektiver Wahrheitsmechanismus, keine objektive Zeit, keine zufällige Auswahl, keine faire Ausgabe, keine externen Kosten, keine Betriebskosten — und es zentralisiert sich im Zeitverlauf. PoW hat das Zeitproblem in dezentralen Systemen gelöst, das Problem der fairen Ausgabe und das Problem der unfälschbaren Kostspieligkeit. PoS löst keines davon. Gigi fasst zusammen: PoS heisst im Grunde „vertrau mir einfach, Bruder". [[aprycot-gigi-woerter-in-bitcoin]]

### Warum Terminologie politisch ist

Die Zuweisung folgt der Wahrnehmung, die öffentliche Politik folgt der Wahrnehmung. Wer Bitcoin als „Waffe" oder „Verschwendung" oder „unkontrollierbares Schwarzgeld" bezeichnet, formt die Regulierungsdebatte. Wer Bitcoin als elektronisches Bargeld bezeichnet — permissionsfrei, überprüfbar, eigenverantwortlich — framt es anders.

Gigi schliesst: In einer Welt voller Euphemismen ist es an sich rebellisch, Dinge beim richtigen Namen zu nennen. Die beste Antwort auf schlechte Terminologie sind präzise Begriffe und das Verständnis, warum Metaphern versagen.

## Related

- [[bitcoin-vs-krypto]]
- [[proof-of-stake-kritik]]
- [[selbstverwahrung-und-boersenrisiken]]
- [[hd-wallets-und-schluesselableitung]]
- [[bitcoin-adresstypen]]
- [[bitcoin-regierungsresistenz]]
- [[redefreiheit-und-protokolle]]

## Open Questions

- Wann und ob sich „Signaturgerät" als Standardbegriff für Hardware Wallets durchsetzt.
- Wie sich die Terminologie in regulatorischen Texten entwickelt — folgen sie dem Industrie-Framing oder etablieren sie eigenständige Definitionen?
- BIP 179 ist noch nicht aktiviert; wie wahrscheinlich ist eine tatsächliche Umbenennung von „Adresse" zu „Rechnung" auf der Basisschicht?
