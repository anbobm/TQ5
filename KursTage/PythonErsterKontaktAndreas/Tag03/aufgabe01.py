
# Definiert euch eine Liste von ganzen Zahlen (um die 5 Stück).
# Diese Liste soll durchlaufen werden.
# Wenn die Zahl kleiner als 5 ist, soll ausgegeben werden "Die Zahl ... ist klein".
# Wenn die Zahl kleiner als 10 ist, soll ausgegeben werden "Die Zahl ... ist mittelgroß".
# Wenn die Zahl größer als 10 ist, soll ausgegeben werden "Die Zahl ... ist groß".
# Zusatzaufgabe:
# Gebt am Schluss eine Zusammenfassung aus, wie viele kleine, mittelgroße und große Zahlen in der Liste waren.

def klein_gross():
    klein = 0
    mittel = 0
    gross = 0

    for zahl in range(100):
        # Reparatur mit if-elif-else
        if zahl < 5:
            klein = klein + 1
            print(f'Die Zahl {zahl} ist klein')
        elif zahl < 10:
            mittel = mittel + 1
            print(f'Die Zahl {zahl} ist mittelgroß')
        else:
            gross = gross + 1
            print(f'Die Zahl {zahl} ist groß')

    print('Zusammenfassung')
    print(f'Es gab {klein} kleine Zahlen')
    print(f'Es gab {mittel} mittelgroße Zahlen')
    print(f'Es gab {gross} große Zahlen')
