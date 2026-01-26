### Aufgabe 1: Erweiterte Online-Bestellung

Erstellen Sie ein UML-Aktivitätsdiagramm mit zwei Swimlanes (Kunde und Online-Shop), das folgenden Ablauf darstellt:

1. Der Kunde wählt ein Produkt aus.
1. Der Kunde legt das Produkt in den Warenkorb.
1. Der Kunde gibt seine Bestelldaten ein.
1. Der Online-Shop prüft, ob das Produkt auf Lager ist.

    Falls nein:
    1. Der Online-Shop informiert den Kunden über die Nichtverfügbarkeit.
    1. Der Vorgang endet.

    Falls ja:
    * Der Online-Shop prüft die Zahlungsart.
1. Ist die Zahlung erfolgreich?

    Falls ja:
    1. Der Online-Shop bestätigt die Bestellung.
    1. Der Kunde erhält eine Bestellbestätigung.

    Falls nein:
    * Der Online-Shop informiert den Kunden über die fehlgeschlagene Zahlung.

1. Der Vorgang endet.

### Aufgabe 2: Erweiterte Kursanmeldung

Erstellen Sie ein UML-Aktivitätsdiagramm mit zwei Swimlanes (Teilnehmer und Kursverwaltung), das folgenden Ablauf beschreibt:

1. Der Teilnehmer wählt einen Kurs aus.
1. Der Teilnehmer meldet sich für den Kurs an.
1. Die Kursverwaltung prüft, ob noch freie Plätze verfügbar sind.

    Falls nein:

    1. Die Kursverwaltung informiert den Teilnehmer, dass der Kurs ausgebucht ist.
    1. Der Vorgang endet.

    Falls ja:
    1. Die Kursverwaltung prüft, ob die Teilnahmevoraussetzungen erfüllt sind.

1. Sind die Voraussetzungen erfüllt?

    Falls ja:

    1. Die Kursverwaltung bestätigt die Anmeldung.
    1. Der Teilnehmer erhält eine Anmeldebestätigung.

    Falls nein:

    1. Die Kursverwaltung informiert den Teilnehmer über fehlende Voraussetzungen.

1. Der Vorgang endet.