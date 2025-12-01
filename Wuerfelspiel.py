from random import randint

print(" Willkommen beim Würfelspiel! ")

while True:
    # Würfe erzeugen
    w1 = randint(1, 6)
    w2 = randint(1, 6)
    w3 = randint(1, 6)

    # Grundpunkte
    punkte = w1 + w2 + w3

    # Bonus berechnen
    if w1 == w2 == w3:
        bonus = 6      # Dreierpasch
    elif w1 == w2 or w1 == w3 or w2 == w3:
        bonus = 2      # Zweierpasch
    else:
        bonus = 0      # kein Pasch

    # Gesamtpunktzahl
    gesamt = punkte + bonus

    # Ausgabe
    print(f"Wurf: {w1} + {w2} + {w3} = {punkte} Punkte, {bonus} Bonuspunkte => {gesamt} Punkte")

    # Gewinn/Verlust
    if gesamt >= 15:
        print(" Du hast GEWONNEN! ")
    else:
        print(" Du hast verloren…")

    # Wiederholung?
    nochmal = input("\nNochmal spielen? (j/n): ").lower()
    if nochmal != "j":
        print(" Spiel beendet. Danke fürs Spielen!")
        break