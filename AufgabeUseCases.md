# Aufgabe: Kinoticket-Buchungssystem

## Beschreibung:
Ein Kino möchte ein Online-System einführen, über das Kunden Kinotickets kaufen können.


## Rahmenbedingungen:

### Das System soll Folgendes ermöglichen:

Kunden können aktuelle Filme und Vorführzeiten ansehen.

Kunden können Sitzplätze auswählen und Tickets buchen.

Kunden können ihre Buchung stornieren.

Ein Administrator kann neue Filme und Vorführzeiten hinzufügen oder löschen.


## Unsere Aufgabe:

Identifiziere die Akteure:
(z. B. Kunde, Administrator, Bezahlsystem)# Aufgabe: Kinoticket-Buchungssystem

## Beschreibung:
Ein Kino möchte ein Online-System einführen, über das Kunden Kinotickets kaufen können.


## Rahmenbedingungen:

### Das System soll Folgendes ermöglichen:

Kunden können aktuelle Filme und Vorführzeiten ansehen.

Kunden können Sitzplätze auswählen und Tickets buchen.

Kunden können ihre Buchung stornieren.

Ein Administrator kann neue Filme und Vorführzeiten hinzufügen oder löschen.


## Unsere Aufgabe:

Identifiziere die Akteure:
(z. B. Kunde, Administrator, Bezahlsystem)

Erstelle 1 Use Case:

   * Filmübersicht anzeigen

   * Ticket buchen

   * Buchung stornieren

 *  Film hinzufügen (Admin)# Aufgabe: Kinoticket-Buchungssystem

## Beschreibung:
Ein Kino möchte ein Online-System einführen, über das Kunden Kinotickets kaufen können.


## Rahmenbedingungen:

### Das System soll Folgendes ermöglichen:

Kunden können aktuelle Filme und Vorführzeiten ansehen.

Kunden können Sitzplätze auswählen und Tickets buchen.

Kunden können ihre Buchung stornieren.

Ein Administrator kann neue Filme und Vorführzeiten hinzufügen oder löschen.


## Unsere Aufgabe:

Identifiziere die Akteure:
(z. B. Kunde, Administrator, Bezahlsystem)

Erstelle 1 Use Case:

   * Filmübersicht anzeigen

   * Ticket buchen

   * Buchung stornieren

 *  Film hinzufügen (Admin)

Erstelle 1 Use Case:

   * Filmübersicht anzeigen

   * Ticket buchen

   * Buchung stornieren

 *  Film hinzufügen (Admin)



# 1. Akteure (Actors)

## Akteur | Beschreibung
- **Kunde** – Möchte Filme ansehen, Tickets buchen und Buchungen stornieren.  
- **Administrator** – Verwaltet Filme und Vorführzeiten (hinzufügen, löschen, bearbeiten).  
- **Bezahlsystem (extern)** – Führt Zahlungen für Ticketbuchungen aus.  
- **Kinosystem / Datenbank** – Speichert alle Filme, Vorführungen, Buchungen usw. (internes System).  

---

# 2. Use Cases (Überblick)

## Use Case | Kurzbeschreibung | Beteiligte Akteure
- **Filmübersicht anzeigen** – Kunde sieht aktuelle Filme und Vorführzeiten. → *Kunde*
- **Ticket buchen** – Kunde wählt Film, Sitzplatz und bezahlt Ticket. → *Kunde, Bezahlsystem*  
- **Buchung stornieren** – Kunde storniert ein bereits gekauftes Ticket. → *Kunde*
- **Film hinzufügen** – Administrator fügt neuen Film mit relevanten Daten hinzu. → *Administrator*

---

# 3. Use Case – „Film hinzufügen (Admin)“

## Use Case Name:
**Film hinzufügen**

## Akteur:
**Administrator**

## Ziel:
Ein neuer Film soll im System verfügbar gemacht werden, damit Kunden diesen später sehen und Tickets dafür buchen können.

---

## Vorbedingungen:
- Administrator ist im System angemeldet.  
- Das System ist online und funktionsfähig.  

---

## Nachbedingungen:
- Der neue Film ist in der Filmliste sichtbar.  
- Optional: Eine oder mehrere Vorführzeiten sind dem Film zugeordnet.  

---

## Hauptszenario (Normalablauf):
1. Administrator wählt die Funktion **„Film hinzufügen“** im Admin-Menü.  
2. Das System zeigt ein Formular zur Eingabe der Filmdaten (Titel, Genre, Dauer, Beschreibung, Altersfreigabe, Startdatum, evtl. Bild).  
3. Administrator gibt alle erforderlichen Informationen ein.  
4. Administrator klickt auf **„Speichern“**.  
5. Das System überprüft die Eingaben auf Vollständigkeit und Plausibilität.  
6. Das System speichert den neuen Film in der Datenbank.  
7. Das System zeigt eine Bestätigungsmeldung: **„Film erfolgreich hinzugefügt.“**  
8. Der neue Film erscheint in der Filmübersicht für Kunden.  

---

## Alternativszenarien (Fehlerfälle):
- **a1:** Fehlende Pflichtangaben → Das System zeigt Fehlermeldung: *„Bitte alle Pflichtfelder ausfüllen.“*  
- **a2:** Verbindung zur Datenbank unterbrochen → Das System zeigt Fehlermeldung: *„Film konnte nicht gespeichert werden. Bitte später erneut versuchen.“*  
- **a3:** Film mit gleichem Titel existiert bereits → Das System warnt: *„Film bereits vorhanden. Möchten Sie dennoch fortfahren?“*  

---

## Auslösendes Ereignis:
Administrator möchte einen neuen Film im System anlegen.