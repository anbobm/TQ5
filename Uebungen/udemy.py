'''Aufgabe 1'''
my_name = "Patrick Schirmer"
print("Hallo ich heiße " + my_name)


'''Aufgabe 2'''
text = "Python Macht Spaß"

länge = len(text)
print(f"der text {text} ist {länge} lang")


'''Aufgabe 3'''
number = 42
word = "test"
decimal_number = 10.5

print("Die Variable Number hat den datentyp " + str(type(number)) + 
      " Die Variable Word hat den Datentyp " + str(type(word)) + 
      " Die variable decimal_number hat den datentyp " + str(type(decimal_number)))


''' Aufgabe 4'''
number_string = "100"
ergebnis = int(number_string) + 100
print(ergebnis)


'''Aufgabe 5'''
number_one = "100"
number_two = "5.5"

ergebnis2 = int(number_one) / float(number_two)
print(ergebnis2)