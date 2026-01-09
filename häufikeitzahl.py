daten = [1, 2, 2, 3, 3, 3, 4,4,4,4,7,9,9,9,10,10,10]

haeufigkeiten = {}  

for element in daten:
    if element in haeufigkeiten:
        haeufigkeiten[element] += 1     # schon vorhanden → zähle hoch
    else:
        haeufigkeiten[element] = 1      # neu → starte bei 1

# Ausgabe
for element, anzahl in haeufigkeiten.items():
    print(f"{element} kommt {anzahl}-mal vor")