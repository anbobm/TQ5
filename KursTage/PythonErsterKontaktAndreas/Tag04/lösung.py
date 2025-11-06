
# Übungen nur mit if / elif / else
# --------------------------------------

# Aufgabe 1: Notenbewertung
# Schreibe ein Programm, das eine Punktzahl (0–100) einliest und dazu eine Note ausgibt:
# - 90–100 -> „Sehr gut“
# - 75–89 -> „Gut“
# - 50–74 -> „Befriedigend“
# - 30–49 -> „Ausreichend“
# - 0–29 -> „Nicht bestanden“

# Punktzahl einlesen (als String)
punkteString = input('Wie viele Punkte? ')
# String in Ganzzahl umwandeln
punkte = int(punkteString)
# man kann auch beides in einem Schritt tun:
# punkte = int(input('Wie viele Punkte? '))

if punkte >= 90:
    print('Sehr gut')
elif punkte >= 75:
    print('Gut')
elif punkte >= 50:
    print('Befriedigend')
elif punkte >= 30:
    print('Ausreichend')
else: 
    print('Nicht bestanden')

# Man könnte hier auch noch die Fälle behandeln, dass der Nutzer
# unsinnige Punktzahlen wie z.B. > 100 oder < 0 eingibt

# Aufgabe 2: Gerade oder ungerade
# Lies eine Zahl vom Benutzer ein und gib aus, ob sie gerade oder ungerade ist.
# Eine Zahl einlesen geht mit: zahl = int(input('Gib eine Zahl ein: '))
# Das int(...) ist nötig, weil die input(..) Funktion einen String zurückgibt,
# wir aber eine Zahl brauchen.

zahl = int(input('Gib eine Zahl ein: '))

# Zahl ist gerade, d.h. bei der Division mit 2 bleibt der Rest 0
# Der Modulo-Operator % gibt den Rest bei der Division zurück
if zahl % 2 == 0:
    print('Die Zahl ist gerade')
else:
    print('Die Zahl ist ungerade')

# Aufgabe 3: Altersfreigabe
# Frage das Alter einer Person ab und gib aus:
# - Unter 12 -> „Kinderfilm erlaubt“
# - 12–15 -> „Abenteuerfilm erlaubt“
# - 16–17 -> „Actionfilm erlaubt“
# - 18 oder älter -> „Alle Filme erlaubt“

alter = int(input('Wie alt? '))

if alter >= 18:
    print('Alle Filme erlaubt')
elif alter >= 16:
    print('Actionfilm erlaubt')
elif alter >= 12:
    print('Abenteuerfilm erlaubt')
else:
    print('„Kinderfilm erlaubt')


# Übungen nur mit for-Schleifen
# -----------------------------------

# Aufgabe 4: Quadratzahlen
# Erstelle eine Liste mit den Zahlen von 1 bis 10 und gib zu jeder Zahl ihr Quadrat (zahl*zahl) aus.

# Liste von Zahlen erstellen (manuell)
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# oder mit range(...)
# Liste beginnt bei 1, geht bis 11 (11 nicht eingeschlossen)
zahlen = range(1, 11) 

for zahl in zahlen:
    quadrat = zahl * zahl
    print(quadrat)

# Aufgabe 5: Namen begrüßen
# Du hast eine Liste mit Namen: ["Anna", "Ben", "Cem", "Dana"]
# Schreibe eine for-Schleife, die jeden Namen begrüßt.

namen = ['Anna', 'Ben', 'Cem', 'Dana']

for name in namen:
    # mit f-String:
    print(f'Hallo {name}')
    # es ginge z.B. auch:
    # print('Hallo ' + name)

# Aufgabe 6: Zahlen addieren
# Gib die Summe aller Zahlen in einer Liste aus. Beispiel: [3, 7, 2, 8] -> Summe = 20

zahlen = [3, 7, 2, 8]

# hier speichern wir unsere summe ab.
# sie startet bei 0 und dann addieren wir fortlaufend jede einzelne
# zahl der liste dazu
summe = 0

for zahl in zahlen:
    summe = summe + zahl

print(summe)


# Kombinierte Aufgaben (if + for + Liste)
# ----------------------------------------------

# Aufgabe 7: Zahlen filtern
# zahlen = [2, 7, 10, 15, 20, 3, 8]
# Gib nur die Zahlen aus, die größer als 8 sind, und zähle, wie viele das sind.

zahlen = [2, 7, 10, 15, 20, 3, 8]

# variable zum zählen der zahlen größer 8
anzahl = 0

for zahl in zahlen:
    if zahl > 8:
        print(zahl)
        anzahl = anzahl + 1

print(f'Es gab {anzahl} Zahlen, die größer als 8 sind.')

# Aufgabe 8: Einkaufsliste prüfen
# einkauf = ["Apfel", "Milch", "Brot", "Zucker"]
# Frage den Benutzer nach einem Artikel. Prüfe, ob er in der Liste ist.
# Die Benutzerabfrage könnte so aussehen: artikel = input('Welchen Artikel suchst du?')

einkauf = ['Apfel', 'Milch', 'Brot', 'Zucker']

gesucht = input('Welchen Artikel suchst du?')

gefunden = False
for artikel in einkauf:
    if artikel == gesucht:
        gefunden = True
        print(f'Gefunden! Der Artikel {artikel} ist in der Einkaufsliste vorhanden')
        break

if not gefunden:
    print('Artikel nicht gefunden')

# Aufgabe 9: Schulnoten analysieren
# noten = [1, 3, 2, 5, 4, 1, 2]
# Gib jede Note mit Text aus und zähle, wie oft jede Note vorkommt.

noten = [1, 3, 2, 5, 4, 1, 2]

# Zählvariablen für die einzelnen Noten
sehrgut = 0
gut = 0
befriedigend = 0
ausreichend = 0
nichtbestanden = 0

for note in noten:
    if note == 1:
        print('Sehr gut')
        sehrgut = sehrgut + 1
    elif note == 2:
        print('Gut')
        gut = gut + 1
    elif note == 3:
        print('Befriedigend')
        befriedigend = befriedigend + 1
    elif note == 4:
        print('Ausreichend')
        ausreichend = ausreichend + 1
    else: 
        print('Nicht bestanden')
        nichtbestanden = nichtbestanden + 1

print(f'Sehr gut gab es {sehrgut} mal')
print(f'Gut gab es {gut} mal')
print(f'Befriedigend gab es {befriedigend} mal')
print(f'Ausreichend gab es {ausreichend} mal')
print(f'Nicht bestanden gab es {nichtbestanden} mal')


# Bonusaufgabe
# ---------------
# Aufgabe 10: FizzBuzz
# Durchlaufe die Zahlen von 1 bis 30:
# - Wenn Zahl durch 3 teilbar -> „Fizz“
# - Wenn durch 5 teilbar -> „Buzz“
# - Wenn durch 3 und 5 -> „FizzBuzz“
# - Sonst -> die Zahl selbst
# Ob eine Zahl durch 5 teilbar ist, findet man heraus mit zahl % 5
# Ist zahl % 5 gleich 0, dann ist die Zahl durch 5 teilbar, ansonsten nicht.

for zahl in range(1,31):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print('FizzBuzz')
    elif zahl % 3 == 0:
        print('Fizz')
    elif zahl % 5 == 0:
        print('Buzz')
    else:
        print(zahl)

# Alternative:

# for zahl in range(1,31):
#     ausgabe = ''
#     if zahl % 3 == 0:
#         ausgabe = 'Fizz'
#     if zahl % 5 == 0:
#         ausgabe = ausgabe + 'Buzz'
#     if ausgabe == '':
#         ausgabe = zahl
#     print(ausgabe)