import math

def ist_primzahl(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    eingabe = input("Zahl eingeben (oder 'ende'):")
    if eingabe.lower() == 'ende':
        break

    try:
        zahl = int(eingabe)
        if ist_primzahl(zahl):
            print(f'{zahl} ist eine Primzahl.')
        else:
            print(f'{zahl} ist keine Primzahl.')
    except ValueError:
        print('Bitte eine gültige Ganzzahl eingeben.')