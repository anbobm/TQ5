eingabe = input('Gib eine Zahl ein: ')

try:
    zahl = int(eingabe)
except ValueError:
    print('Das war keine Zahl')

person = {"name": "Paul",
        }

try:
    alter = person["alter"]
except:
    print('Es gab kein Alter')
    alter = 30

def foo(liste):
    if len(liste) == 0:
        return False
    
    erstes = liste[0]

foo([])