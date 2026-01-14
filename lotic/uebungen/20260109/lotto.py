'''
Eine Simulation einer Lotterie
Autor: Timo Röhle
'''

# Eine Liste bestehend aus 6 Zahlen die wir wetten werden.
lottoschein = []

# Eine Liste aus 6 zufälligen Zahlen die unsere Ziehung repräsentiert.
lottoziehung = []

# Bool variable die Überprüft ob wir unseren Lottoschein richtig ausgefüllt haben.
lottoschein_ausgefüllt = False
print('Fülle deinen Lottoschein aus')

while not lottoschein_ausgefüllt:
    benutzer_eingabe = input(f'Bitte Zahl {len(lottoschein)+1} eingeben')
    try:
        zahl = int(benutzer_eingabe)
    except:
        print(Ungültige Eingabe)

