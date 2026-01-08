def berechne_summe(liste):
    gesamt_summe = 0
    for zahl in liste:
        gesamt_summe = gesamt_summe + zahl
    return gesamt_summe

zahlen = [10, 20, 30, 40, -5]
ergebnis = berechne_summe(zahlen)

print(f"Die Summe ist: {ergebnis}")