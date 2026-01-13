## Ein Parkhaus-Zutrittssystem steuert die Einfahrtsschranke und prüft Tickets.

Modelliere folgendes System im Zustandsdiagramm.

### Beschreibung des Systems:
* Das System befindet sich im Zustand "Bereit", solange es auf ein Auto wartet.
* Wenn ein Auto ankommt, wechselt das System in den Zustand "Ticket prüfen".
* Das Ticket kann:
  * gültig sein -> System öffnet die Schranke -> Zustand "Schranke offen"
  * ungültig sein -> System zeigt Fehlermeldung -> Zustand "Fehler"
* Nach dem Öffnen der Schranke schließt sie automatisch wieder und das System geht zurück in den Zustand "Bereit".
* Im Fehlerzustand wartet das System auf die Eingabe "Abbrechen".
* Danach kehrt es wieder in den Zustand "Bereit" zurück.

### Zusatzaufgabe:

* Im Zustand "Ticket prüfen" kann das Ticket zusätzlich den Status "unbezahlt" haben.

* Dann zeigt das System "Bitte zuerst bezahlen" und geht in den Zustand "Bezahlen erforderlich".

* Nach erfolgreicher Zahlung darf das Auto einfahren -> zurück zu "Ticket prüfen".