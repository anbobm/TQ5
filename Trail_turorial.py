# firmenname = "AOL" #variable
# beruf = "IT-FISI" #variable
# weiterbildungsdauer = 6 - 2
# print ("Hallo libes Team von " + firmenname + ", ich möchte gerne in ihrer Firma " + firmenname + " arbeiten. Vielen Dank.")
# print ("Ich habe eine Weiterbildung zum " + beruf + " gemacht, ")
# print (weiterbildungsdauer)

# x = "50" #String (str) Zeichenkette, Buchstaben aber auch Zahlen, Leerstellen oder Sonderzeichen
# print (x)

# x = 50 #Integer (int) Ganzzahl
# print (x)

# x = 50 + 50 #Integer (int) Auch berechenbar
# print (x)

# x = 50.0 #Float (float) in Py immer mit PunktZeichen kein Kommazeichen für NachKommaStelle
# y = 25.5
# print (y)

# x = True Boolean (bool) Wahrheitswerte können nur True oder False
# y = False
# print (y)

# # Index = einzelne Zuordnung der Bestandteile einer Zeichenkette ermöglicht isolierte Ansprache einzelner Buchstaben von Strings
# # Ein Index wird immer in [] eckigen Klammern angegeben !
# x = 'Hallo Welt'
# print (x[6])

# Slicing = Zerlegen/Zerschneiden von Strings > ermöglicht isolieren einzelner Wörter
# x = 'Hallo Welt!!!'
# # Doppelpunkt in der eckingen klammer [_:] Bestimmte Stelle bis Ende [:_] Anfang bis beliebige stelle
# print (x[6:10])

# # Funktion: len () Zählen der Bestandteile im str
# y = 'Dieser Satz ist recht lang. Wie lang ist er?'
# #print(len(y))
# print ('Der String mit der Variable y ist', len(y), 'Zeichen lang.')

# Strings sind unveränderliche Datentypen
# x = 'hallo'
# # Verketten
# x = 'H' +  x[1:] # + Pluszeichen addiert nicht bzw verketten ein großes H ab Index [1:_] bis ende also das kleine h in Variable x wird ersetzt !
# print (x) # Jetzt ergibt es ein groß geschriebenes Hallo

# x = 'Hallo'
# print (x + x + x ) # so sollte es nicht sein
# print (x * 10) # stern zeichen mal x10
# noch effizienter wäre
# print ('hallo' * 10) # nur mit * Wenn + dann 10 in "" also + "10"
# x = 100
# print ('Hallo' + str(x))

# Funktionen für Strings x.upper () in GROSSBUCHSTABEN umwandeln
# x = 'Hallo Welt'
# print(x.upper()) #  Alles groß
# print(x.lower()) #  Alles klein
# print(x.split()) #  einzeln getrennt

# y = 'Hallo Welt, ich, lerne, Python'
# print (y.split(',')) # Split mit Kommazeichen

# x = 'Ich liebe Python Tutotials <3'
# print (x.find('Python')) # x.find Zeigt den ersten Buchstaben
# print (x[x.find('Python'):]) # str slicing [:]

# ZAHLEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#INTEGER Ganzzahlen positiv oder negativ
#FLOAT Gleitkommazahlen Trennzeichen .Punkt beachten

# print (10 + 2) # Plus
# print (10 - 2) # Minus
# print (10 / 2) # Division mit Float Output .0

# print (type(5.0)) # type zeigt Class typ an
# print (type(10 / 2)) # zeigt trotzdem Float weil 5.0

# DIVISION MIT REST = Modulu Operator
# print(10 / 3) # 10 geteilt 3 REST ? in Python mit % Zeichen
# print(10 % 3) # 10 %Modulu 3 rest 1

# print(10 / 2) # 10 geteilt 2 KEIN REST !
# print(10 % 2) # 10 %Modulu 3 rest 0
# print (10** 2) # 10 **HOCH 2
# print(10 ** 0.5) # Wurzel ziehen
# Punkt vor strich
# 2+ 1 * 3
# erst die Klammer mal 3
# (2+1) * 3

# INPUT

# x = input ('Wie ist dein Name?') # Unterbricht ausgabe bis INPUT
# print ('Hallo ' + x) # Hallo + Wie ist dein Name + INPUT in der unteren Terminal Ausgabe !

# y = input ('Wie viel ist dein Gehalt? ')
# x = y * 1.10
# print(x) # FEHLER !!! <<< Wird als Text erkannt ! Erst umwandeln.

# y = int(input ('Wie viel ist dein Gehalt? ')) # Die eingabe also der eigene INPUT wird in INT umgewandelt.
# x = y * 1.10
# print(x)

# ÜBUNG <<<<<<<<<<<<<<<<<<<<<<<<<
# Währungsumrechner EUR > BAHT <<<<<<<<<<<<<<<<<
# Ein Programm das fragt wieviel € hast du ?
# Dann die Eingabe (INPUT) Bsp: 50 €
# Ausgabe in der Konsole = Deine € sind XY BAHT

# euro = float(input('Wie viel Euro has du? '))
# baht = euro * 38.06
# print('Super! Deine ', euro, ' Euro sind ', baht, ' Baht wert.')

# BOOLEAN = Waheitswerte > True oder False immer GROSS SCHREIBEN
# True = 1
# False = 0

# print(type (True)) # mit dem type Befehl checken welcher Class True angehört...
# print(2 > 1)
# print(2 < 1)
# logische Aussagen ABER 
# "="  > Zuweisung von Variablen
# "==" > logische Aussagen (Prüfung)
# print(2 = 1) #NICHT MÖGLICH weil nur Variable Zuweisung
# print(2 == 1)  # mit == MÖGLICH weil Logische Aussage

# WENN DANN ? IF ELSE ! <<<<<<<<<<<<<<<<<

# BEISPIEL: NACH STRECKE, zu Fuss oder Fahrrad ?

# streckeInKm = 2 # Hier kleiner oder größer als 3 Eintragen !
# if streckeInKm < 3:
#     print('Lauf doch zu Fuß!') # Wenn <kleiner als 3
# else:
#     print('Nimm das Fahrrad!') # Wenn >größer als 3

# streckeInKm = 3 # ELIF

# if streckeInKm < 3:
#     print('Lauf doch zu Fuß!')
# elif streckeInKm == 3:
#     print('Strecke ist recht lang')
#     print('Nimm Laufschuhe!')
# else:
#     print('Nimm das Fahrrad!')

# ÜBUNG KINOTICKETS

# alter = int(input('Wie alt bist du?'))

# if alter > 65:
#     print('Rentner zahlen 7.5€')
# elif alter >= 18:
#     print('Erwachsene zahlen 10€')
# else:
#     print('Kinder zahlen 5€')

# 2 VARIABLE + ANZAHL <<<
# alter = int(input('Wie alt bist du?'))
# anzahl = int(input('Wie viele Tickets möchtest du kaufen?'))

# if alter > 65:
#     print(7.5 * anzahl)
# elif alter >= 18:
#     print(10 * anzahl)
# else:
#     print(5 * anzahl)

# LISTEN "list" in [] eckigen Klammern, geordnete und veränderbare Daten <<<<<<<<

# Leere Liste
# leere_liste = []
# print (leere_liste)


# einkaufszettel = ['Eier', 'Trauben', 'Milch', 22] # Liste aus gemischten Datentypen 3x str 1x int
# print(einkaufszettel[2]) # Nach Index 2 also 0,1,2 ist Milch die 2
# print(type(einkaufszettel[2])) # String Funktionen wie Indexing und Slicing sind auch auf Listen möglich
# print((einkaufszettel[2][1])) # Index Kästchen [2] bezieht sich auf Milch und Index Kästchen [1] Das Wor Milch BUCHASTABE mit dem Index [1] = i

# Funktionen für Listen <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# f.append(...)
# f.insert(_;...)
# f.remove(...)
# f.pop() # letzter Eintrag entfernen
# del f[_]
# len(f)
# min(f) #kleinste nach Anzahl der Buchstaben
# max (f) #größte nach Anzahl der Buchstaben

# einkaufszettel = ['Eier', 'Trauben', 'Milch',]
# # print(einkaufszettel)

# einkaufszettel.append('Nüsse')
# print(einkaufszettel)

# einkaufszettel.insert(0, 'Schokolade')
# print(einkaufszettel)

# einkaufszettel.remove('Nüsse')
# print(einkaufszettel)


# einkaufszettel.pop()
# einkaufszettel.pop() #  .pop() Mehrfach hintereinander möglich, Einträge werden von hinten entfernt
# print(einkaufszettel)

# del einkaufszettel[0] # del Befehl löscht den Index, Eintrag 0
# print(einkaufszettel)

# einkaufszettel = ['Eier', 'Trauben', 'Milch',]
# print(len(einkaufszettel)) # Anzahl der Einträge

einkaufszettel = ['Eier', 'Trauben', 'Milch',]
print(einkaufszettel[1:3]) # Slicing
print(einkaufszettel[1:len(einkaufszettel)]) # Länge geht auch