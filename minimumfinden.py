def finde_minimum(liste):
    if not liste:
        return None
    min_wert = liste[0]

    for zahl in liste:
        if zahl < min_wert:
            min_wert = zahl
            return min_wert

meine_zahlen = [15, 3, 42, -7, 11]
print(f"Das Minimum ist: {finde_minimum(meine_zahlen)}")