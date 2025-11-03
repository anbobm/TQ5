# Ein Dictionary ist eine Sammlung von Key-Value-Pairs, also von Schlüssel-Wert-Paaren.

# Aufgabe 1: Einfaches Dictionary erstellen
# Erstelle ein Dictionary person mit den Schlüsseln: name, alter und stadt.
# Weise ihm beliebige Werte zu und gib das komplette Dictionary aus: print(person)

person = {
    'name': 'Ben',
    'alter': 28,
    'stadt': 'Berlin'
}

print(person)

# Aufgabe 2: Werte abrufen
# Gegeben ist das Dictionary:
student = {
    "name": "Max",
    "noten": [1, 2, 3, 4],
    "klasse": "10A"
}

# 1. Gib den Namen des Studenten aus.

print(student['name'])

# 2. Gib die Notenliste aus (komplett oder jedes Element einzeln)
notenliste = student["noten"]

for note in notenliste:
    print(f'Note: {note}')

# 3. Berechne die Durchschnittsnote aus der Notenliste.

notenliste = student["noten"]
name_of_students = student["name"]

summe = 0
for note in notenliste:
    summe = summe + note

anzahl = len(notenliste)
durchschnitt = summe / anzahl

print(f"{name_of_students} hat die Durchschnittsnote {durchschnitt} !")

# oder mit Angabe von 2 Nachkommastellen:
print(f"{name_of_students} hat die Durchschnittsnote {durchschnitt:.2} !")


# Aufgabe 3: Werte ändern und hinzufügen
# Ändere das Alter der Person im Dictionary person.

person['alter'] = 71

# Füge einen neuen Schlüssel 'beruf' mit einem selbstgewählten Wert hinzu.
person['beruf'] = 'Rentner' # schreibender Zugriff auf nicht existierende Schlüssel ist okay

# lesender Zugriff auf nicht existierenden Schlüssel würde Fehler erzeugen, z.B.
# postleitzahl = person['postleitzahl']


# Aufgabe 4: Schleife über ein Dictionary
# Gegeben ist das Dictionary:
inventar = {"apfel": 10, "banane": 5, "orange": 8}

# 1. Schreibe eine Schleife, die jede Frucht und die Anzahl ausgibt. Z.B.:

for frucht in inventar: # alle Schlüssel werden durchlaufen
    anzahl = inventar[frucht]
    print(f'{frucht}: {anzahl}')

# oder mit inventar.items(), d.h alle (Schlüssel, Wert) - Paare werden durchlaufen

for frucht, anzahl in inventar.items():
    print(f'{frucht}: {anzahl}')

# 2. Berechne die Gesamtanzahl aller Früchte.
sum = 0
for anzahl in inventar.values():
    sum = sum + anzahl

print(sum)

# Aufgabe 5: Dictionary verschachteln
# Erstelle ein Dictionary schule mit zwei Schülern. Jeder Schüler soll ein weiteres Dictionary sein, das alter und noten enthält.
# Beispiel:
schule = {
    "Max": {"alter": 15, "noten": [1, 2, 3]},
    "Anna": {"alter": 14, "noten": [2, 1, 2]}
}

# 1. Gib das Alter von Max aus.
max = schule["Max"]
alter_von_max = max["alter"]
print(alter_von_max)
# oder direkt:
print(schule["Max"]["alter"])

# 2. Berechne den Durchschnitt der Noten von Anna.

notenliste_anna = schule["Anna"]["noten"]

print(f'Notendurchschnitt von Anna: { sum(notenliste_anna) / len(notenliste_anna) }')

# Aufgabe 6: Dictionary filtern
# Gegeben ist ein Dictionary:
preise = {"apfel": 2, "banane": 1, "kirsche": 3, "orange": 2}
# Erstelle ein neues Dictionary, das nur die Früchte enthält, die 2 Euro kosten oder weniger.

neu = {}

for frucht in preise:
    preis = preise[frucht]

    if preis <= 2:
        neu[frucht] = preis

print(neu)

# oder (fortgeschritten) mit generator expressions:
neu = { frucht : preis for frucht, preis in preise.items() if preis <= 2}
