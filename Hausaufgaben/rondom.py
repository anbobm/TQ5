# Wir implementieren folgendes Spiel mit Python:
# Mit der random.randint() Methode simulieren wir den Wurf von drei sechsseitigen Würfeln.
# Die Summe der gewürfelten Zahlen ist die erreichte Punktzahl
# Wurf: 4 + 5 + 2 bedeutet 11 Punkte
# Wenn die Augenzahl auf zwei Würfeln identisch ist, erhalten wir zwei Bonuspunkte ("Zweierpasch").
# z.B. Wurf: 4 + 4 + 5 bedeutet 13 Punkte plus 2 Bonuspunkte, also 15 Punkte insgesamt
# Wenn die Augenzahl auf allen drei Würfeln identisch ist, erhalten wir sechs Bonuspunkte ("Dreierpasch").
# z.B. Wurf 1 + 1 + 1 bedeutet 3 Punkte plus 6 Bonuspunkte also 9 Punkte insgesamt
# Die Ausgabe soll alle drei Würfe, deren Summe, die Bonuspunkte und die Gesamtsumme beinhalten, z.B.:
# "Wurf: 1 + 1 + 1 = 3 Punkte, 6 Bonuspunkte => 9 Punkte"
# Wenn die Gesamtsumme mindestens 15 ist, dann hat man das Spiel gewonnen, ansonsten verloren, und
# das soll auch mit ausgegeben werden.
#
# Zusatz: Nach einem Spiel soll der Spieler gefragt werden, ob er noch einmal spielen will,
# dann wird das Ganze wiederholt, ansonsten wird das Programm beendet

# randint() Methode importieren aus dem random Modul:
from random import randint

# Würfel simulieren mit randint(1, 6) - gibt Zufallszahl zwischen 1 und 6 (einschließend) zurück
wurf1 = randint(1, 6)
wurf2 = randint(1, 6)
wurf3 = randint(1, 6)
summe = wurf1 + wurf2 + wurf3
if summe >= 15:
    ergebnis = "gewonnen"