# Monsterarena
Erstelle ein kleines Textspiel, in dem ein Held gegen mehrere Monster kämpft.

### Klassen:
- Held (Attribute: name, leben, angriff, Methoden: `angreifen(self, monster)`, `ist_besiegt() : bool`)
- Monster (Attribute: name, leben, angriff, Methoden: `angreifen(self, held)`, `ist_besiegt() : bool`)
- Attribute können public sein und `angreifen()` modifiziert das übergebene Objekt (Monster/Held) direkt

### Ablauf:
Lege einen Held und eine Liste von Monstern an. Anschließend:
1. Held wählt ein Monster aus.
1. Held greift an.
1. Monster greift zurück an, falls es noch lebt.
1. Wieder von vorn. Schleife endet, wenn Held oder alle Monster besiegt sind.

### Erweiterungen:
- Monster wählen zufällig, ob sie normal oder kritisch angreifen. (Modul `random`)
- Monster droppen zufällig Heiltränke, die Lebenspunkte des Helden auffüllen