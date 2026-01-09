def liste_rechts_rotieren(zahlen):
    if len(zahlen) <= 1:
        return zahlen[:]  # Kopie zurückgeben bei 0 oder 1 Element
    
    # Neue Liste erstellen
    rotiert = []
    # Zuerst das letzte Element anhängen
    rotiert.append(zahlen[-1])
    # Dann alle außer dem letzten
    for i in range(len(zahlen) - 1):
        rotiert.append(zahlen[i])
    
    return rotiert

# Test
liste = [1, 2, 3, 4]
print(liste_rechts_rotieren(liste))  # Ausgabe: [4, 1, 2, 3]