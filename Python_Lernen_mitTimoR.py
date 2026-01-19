import random
# numbers = [8, 5, 2, 9, 6, 3] eckige Klammer bedeutet dass wir eine liste haben

zahlen = input('Bitte 6 nummer eingeben getrennt durch leerzeichen, keine doppelte zahlen:')
# print(zahlen)

listeauszahlenstring = zahlen.split(' ')
listeauszahlen = []
# print(listeauszahlenstring)

# for i in range(0, 6): # 0 bis 6 bedeutet dass die schleife 6 mal sich wiederholt 0, 1, 2, 3, 4, 5 = 6x
    # for schleife immer dann benutzen wenn man es im voraus weisst wie oft die schleife sich wiederholen soll sonst die while schleife benutzen.
    # print(listeauszahlenstring[i])
    # print(type(listeauszahlenstring[i]))
    # listeauszahlen.append(int(listeauszahlenstring[i])) # listenauszahlenstring an die listenauszahlen angehängt und von string ein int erstellt (ganze zahlen)
    
# print(listeauszahlen)

for zahlenstring in listeauszahlenstring:
    listeauszahlen.append(int(zahlenstring))

print(listeauszahlen)

# zufallszahl = random.randint(1, 49) # random.randint erzeugt eine int (ganzzahl) zufällig zwischen 1 - 49
'''listeauszufallszahlen = []
for zähler in range(0, 6):
    zufallszahl = random.randint(1, 49)
    listeauszufallszahlen.append(zufallszahl)
    # print(zufallszahl)
    
print(listeauszufallszahlen)''' # wenn der print aus der schleife geschrieben wird dann wird nur das letzte ergebniss angezeigt, sonst wird alle duruchläufe angezeigt.
lottoziehung_korrekt = False
lottoziehung = []

while not lottoziehung_korrekt:
    zufallszahl = random.randint(1, 49) # zufallszahl wird ausgewählt
 
    if lottoziehung.count(zufallszahl) == 1: # existiert die zahl schon? wenn ja dann continue
        continue                             # wiederholt die While-Schleife bis das  obere if fals ist, dann geht es weiter nach unten
 
    lottoziehung.append(zufallszahl)        # wird die zahl an die liste (lottoziehung) angehängt
    anzahl_gueltige_ziehungen = len(lottoziehung)   # länge der liste (lottoziehung)
    if anzahl_gueltige_ziehungen == 6:      # Die While-Schleife wird wiederholt bis 6 gültigen ziehungen erfolgt sind
        lottoziehung_korrekt = True         # Wunrde 6x die ziehung erfolgreich durchgeführt dann ist die lottoziehung TRUE!

print(lottoziehung)

# listeauszahlen = []

treffer = 0

for zahl in listeauszahlen:        # Eine for-Schleife geht Element (zahl) für Element durch eine Liste (listeauszahlen) und wählt bei jedem Durchgang das aktuell passende Listenelement aus.
    if zahl in lottoziehung:       # überprüft ob das akutelle element (zahl) in der lottozieung vorhanden ist
        treffer = treffer + 1      # wenn das element (zahl) in der lottozieung vorhanden ist, dann wird die variable treffer um 1 erhöht
if treffer < 3:
    print('Sie haben leider kein Gewinn')
if treffer == 3:
    print('Glückwunsch Sie haben 10 €uro Gewonnen!')
if treffer == 4:
    print('Glückwunsch Sie haben 100 €uro Gewonnen!')
if treffer == 5:
    print('Glückwunsch Sie haben 10.000 €uro Gewonnen!')
if treffer == 6:
    print('Glückwunsch Sie haben 1.000.000 €uro Gewonnen!')