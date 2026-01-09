def zweitgroesste(zahlen):
    if len(zahlen) < 2:
        return None  # oder raise ValueError("Liste muss mindestens 2 Elemente haben")
    
    # Initialisierung mit den ersten zwei Elementen
    if zahlen[0] > zahlen[1]:
        groesste = zahlen[0]
        zweitgroesste = zahlen[1]
    else:
        groesste = zahlen[1]
        zweitgroesste = zahlen[0]
    
    # Rest der Liste durchgehen
    for zahl in zahlen[2:]:
        if zahl > groesste:
            zweitgroesste = groesste      # bisherige größte wird zweitgrößte
            groesste = zahl
        elif zahl > zweitgroesste and zahl < groesste:
            zweitgroesste = zahl
        # Sonderfall: wenn zahl == groesste → ignorieren (bleibt zweitgrößte unverändert)
    
    # Falls alle Zahlen gleich sind → zweitgrößte bleibt None
    if zweitgroesste == groesste:
        return None
    
    return zweitgroesste


# Testfälle
testlisten = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],   # → 8
    [10, 10, 10, 10],                 # → None
    [7, 7, 3, 7],                     # → 3
    [42],                             # → None
    [5, 3],                           # → 3
    [-1, -5, -2, -10],                # → -2
]

for lst in testlisten:
    erg = zweitgroesste(lst)
    print(f"Liste: {lst}  →  Zweitgrößte: {erg}")