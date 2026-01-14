import random


# len = length

def lziehung():
    
    lottoziehung = []
    lottoziehung_korrekt = False

    while not lottoziehung_korrekt:
        zufallszahl = random.randint(1, 49)

        if lottoziehung.count(zufallszahl) == 1:
            continue

        lottoziehung.append(zufallszahl)
        anzahl_gueltige_ziehungen = len(lottoziehung)
        if anzahl_gueltige_ziehungen == 6:
            lottoziehung_korrekt = True
    return lottoziehung

lottoschein = [13, 11, 19, 8, 3, 1]
anzahl_ziehungen = 0
treffer = 0
while True:
    ziehung = lziehung() 
    for element in lottoschein:
        if element in ziehung:
            treffer += 1
    anzahl_ziehungen += 1
    print(f'Ziehung: {anzahl_ziehungen}')
    print(lottoschein)
    print(ziehung)
    print(f'teffer: {treffer}')
    if treffer > 5:
        break
    treffer = 0
