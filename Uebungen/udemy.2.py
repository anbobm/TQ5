'''
antwort1 = float(input("Wie viel Euro Budge hast du? "))
antwort2 = float(input("Wie viel %  beabsichtigst du von deinem Budge für die Unterkunft auszugeben? "))
antwort3 = float(input("Wie viel %  möchtest du für Essen ausgeben? "))
antwort4 = float(input("Wie viel %  möchtest du für aktivitäten ausgeben? "))

ergebnis1 = antwort1 / antwort2
ergebnis2 = antwort1 / antwort3
ergebnis3 = antwort1 / antwort4
masterergebnis = ergebnis1 + ergebnis2 + ergebnis3

print(f"Du beabsichtigst {masterergebnis}€ für Unterkunft, Verpflegung & Aktivitäten auszugeben ")
'''
try:
    celsiusantwort = int(input("Wie viel Grad in Celsius ist bei ihnen? "))
    frechnung = (celsiusantwort * 9/5) + 32

    print(f"es ist {frechnung} fahrenheit bei ihnen ")

except:
    print("Fehler bei der eingabe")