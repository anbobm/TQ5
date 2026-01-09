liste = [10, 20, 30, 40, 50]

# Summe manuell berechnen
summe = 0
for zahl in liste:
    summe += zahl

# Anzahl der Elemente manuell ermitteln
anzahl = 0
for _ in liste:
    anzahl += 1

# Durchschnitt berechnen
if anzahl > 0:  # Schutz vor Division durch 0
    durchschnitt = summe / anzahl
else:
    durchschnitt = 0

print("Durchschnitt:", durchschnitt)