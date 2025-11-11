# Gegeben ist folgende Liste von Früchten:

liste = [
    'Apfel',
    'Wassermelone',
    'Birne',
    'Heidelbeere',
    'Birne',
    'Birne',
    'Kirsche',
    'Birne',
    'Kirsche',
    'Birne',
    'Kirsche',
    'Heidelbeere',
    'Birne',
    'Birne',
    'Wassermelone'
]

# Wir suchen nun nach einer bestimmten Frucht, z.B.

gesucht = 'Birne'

# Zähle nun mit einer for-Schleife, wie oft diese Frucht
# in der Liste vorkommt.

anzahl = 0

for element in liste:
    if element == gesucht:
        anzahl = anzahl + 1

print(f'Das gesucht Element {gesucht} war {anzahl} mal in der Liste.')


# Und anschließend nochmal das gleiche, aber mit einer
# while-Schleife (auch wenn man in dieser Situation
# eigentlich keine while-Schleife einsetzen sollte; wir
# machen das hier nur zum Üben)

anzahl = 0
index = 0
while index < len(liste):
    if liste[index] == gesucht:
        anzahl += 1
    index += 1
print(anzahl)


print('Anzahl: ' + str(anzahl))
print('Anzahl: ', anzahl)
# 'Anzahl: ' + str(anzahl)