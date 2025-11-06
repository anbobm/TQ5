# Schreibe ein Programm, das mithilfe einer Funktion entscheidet, wie das Wetter ist — basierend auf einer Temperaturangabe.
# Schreibe eine Funktion namens beurteile_temperatur(temp), die eine Temperatur (Zahl) als Parameter bekommt.
# Verwende if / elif / else, um Folgendes zu prüfen:
# Wenn temp unter 10 ist, soll die Funktion "Es ist kalt." zurückgeben.
# Wenn temp zwischen 10 und 25 liegt, soll sie "Es ist angenehm." zurückgeben.
# Wenn temp über 25 ist, soll sie "Es ist heiß." zurückgeben.
# Erstelle eine Liste mit verschiedenen Temperaturen (z. B. [3, 12, 18, 27, 30]).
# Schreibe eine for-Schleife, die jede Temperatur in der Liste überprüft und das Ergebnis der Funktion ausgibt.

# Hinweis: Die Aufgabe ist ungenau formuliert. Es ist z.B. nicht klar,
# zu welchem Temperaturbereich 10 Grad gehört. Kalt oder Angenehm?
# Wir konkretisieren also bei unserer Lösung wie folgt: 10 ist angenehm, 25 ist heiß.
# Das beinflusst, wie genau wir die Bedingungen bei if und elif formulieren.

# Wir definieren hier bereits die Funktion. Wir müssen sie immer definieren, bevor 
# wir sie aufrufen können. Die Reihenfolge ist also wichtig.

def beurteile_temperatur(temp):
    if temp < 10:
        print('Es ist kalt')
    elif temp >= 10 and temp < 25:
        print ('Es ist angenehm.')
    else: # Temperatur ist größer oder gleich 25
        print ('Es ist heiß')

# Unsere Liste mit Temperaturen
temperaturen = [3, 12, 18, 27, 30]

# Alle Temperaturen in der Liste werden durchlaufen
# Für jede Temperatur wird die Funktion beurteile_temperatur() aufgerufen
for temperatur in temperaturen:
    beurteile_temperatur(temperatur)