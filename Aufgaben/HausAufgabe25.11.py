from random import randint

def spielrunde():
    # Drei Würfel werfen
    w1 = randint(1, 6)
    w2 = randint(1, 6)
    w3 = randint(1, 6)

    # Grundpunkte (Summe der Würfel)
    summe = w1 + w2 + w3

    # Bonuspunkte berechnen
    bonus = 0

    # Dreierpasch zuerst prüfen (alle drei gleich)
    if w1 == w2 == w3:
        bonus = 6
    # Wenn kein Dreierpasch, dann schauen ob ein Zweierpasch vorliegt
    elif w1 == w2 or w1 == w3 or w2 == w3:
        bonus = 2

    # Gesamtsumme
    gesamt = summe + bonus

    # Ausgabe bauen
    print(f"Wurf: {w1} + {w2} + {w3} = {summe} Punkte, {bonus} Bonuspunkte => {gesamt} Punkte")

    # Gewinn oder Verlust
    if gesamt >= 15:
        print("Du hast gewonnen!")
    else:
        print("Du hast verloren.")

# Hauptschleife
while True:
    spielrunde()

    # Spieler fragen, ob er nochmal will
    nochmal = input("Nochmal spielen? (j/n): ").strip().lower()

    if nochmal != "j":
        print("Dann nicht... Spiel wird beendet.")
        break

