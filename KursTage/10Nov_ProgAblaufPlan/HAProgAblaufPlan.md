# Programmablaufplan

## Aufgabe 1 Beschreibung:

Ein Programm soll von einem Benutzer mehrere Zahlen einlesen und anschließend

* die größte Zahl,

* die kleinste Zahl

* und den Durchschnitt
berechnen und ausgeben.

Zuerst wird eingegeben, wie viele Zahlen verarbeitet werden sollen. Dann werden die Zahlen nacheinander eingelesen und ausgewertet.

### Pseudocode:

```python
EINGABE anzahl
summe := 0
i := 1

EINGABE zahl
groesste := zahl
kleinste := zahl
summe := summe + zahl
i := i + 1

SOLANGE i <= anzahl WIEDERHOLE
    EINGABE zahl
    summe := summe + zahl

    WENN zahl > groesste DANN
        groesste := zahl
    ENDE WENN

    WENN zahl < kleinste DANN
        kleinste := zahl
    ENDE WENN

    i := i + 1
ENDE SOLANGE

durchschnitt := summe / anzahl

AUSGABE "Größte Zahl: ", groesste
AUSGABE "Kleinste Zahl: ", kleinste
AUSGABE "Durchschnitt: ", durchschnitt
```

==============================================

## Aufgabe 2 Beschreibung:

Ein Programm soll die Durchschnittsnote einer Klasse berechnen.

Zuerst wird eingegeben, wie viele Schüler bewertet werden sollen.

Dann gibt der Benutzer für jeden Schüler eine Note (zwischen 1 und 6) ein.

Am Ende wird der Durchschnitt berechnet und eine Bewertung ausgegeben:

1. Durchschnitt < 2 → „Sehr gut“

2. Durchschnitt < 3 → „Gut“

3. Durchschnitt < 4 → „Befriedigend“

4. Sonst → „Verbesserungswürdig“

### Pseudocode:

```python
EINGABE anzahl_schueler
summe := 0
i := 1

SOLANGE i <= anzahl_schueler WIEDERHOLE
    EINGABE note
    summe := summe + note
    i := i + 1
ENDE SOLANGE

durchschnitt := summe / anzahl_schueler

WENN durchschnitt < 2 DANN
    AUSGABE "Sehr gut"
SONST WENN durchschnitt < 3 DANN
    AUSGABE "Gut"
SONST WENN durchschnitt < 4 DANN
    AUSGABE "Befriedigend"
SONST
    AUSGABE "Verbesserungswürdig"
ENDE WENN
```