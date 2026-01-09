# Zahl vom Benutzer einlesen per Input
n = int(input("Gib eine positive ganze Zahl ein: "))

# Sicherstellen, dass n positiv ist 
if n <= 0:
    print("Bitte eine positive ganze Zahl größer als 0 eingeben!")
else:
    print(f"Die Teiler von {n} sind:")

    # Alle Teiler finden und ausgeben
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)