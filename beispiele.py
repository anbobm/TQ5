# Unterscheidung des Alters

alter = 17 # festes alter, oder benutzer eingeben lassen:
alter = int(input('Wie alt bist du? '))

# fallunterscheidung
if alter >= 18:
    print('Du bist volljährig')
else:
    print('Du bist minderjährig')


# Notenberechnung

punkte = 85 # feste punktzahl, oder benutzer eingeben lassen:
punkte = int(input('Wie viele Punkte hast du erreicht? '))

# fallunterscheidung mit mehreren fällen.
# genau einer der fälle wird auf jeden fall ausgeführt.
if punkte >= 90:
    print('Sehr gut')
elif punkte >= 75:
    print('Gut')
elif punkte >= 60:
    print('Befriedigend')
else: 
    print('Ausreichend')


# Listendefinition
countries = ['Deutschland', 'Frankfreich', 'Polen']

# index von listen
zahlen = [
    1,      # das 0-te Element
    0,      # das 1-te Element
    -4,     # das 2-te Element
    12,     # das 3-te Element
    3413,   # das 4-te Element
    -28432, # das 5-te Element
    7       # das 6-te Element
]           #     ^ der Index

# zugriff auf listenelement mittels index-operator:
zahlen[4]

# Range

# range(5) == [0,1,2,3,4]
# range(10) == [0,1,2,3,4,5,6,7,8,9]
# range(100) == [0,1,2,3,4,5,6,7,.................,97,98,99]
# range(11,20,3) == [11,14,17]


# f-Strings 
name = 'Bernd'
wetter = 'regnerisch'
begruessung = 'Hallo ' + name # == 'Hallo Bernd'
begruessung = f'Hallo {name}, das Wetter ist heute {wetter}!' # Hallo Bernd, das Wetter ist heute regnerisch
begruessung = 'Hallo ' + str(name) + ', das Wetter ist heute ' + str(wetter) + '!'

s1 = 'foo'
s2 = 'bar'
v = s1 + s2
v = f'{s1}{s2}'


# Schleifen

# durchlauf einer liste mittels einer for-Schleife
for country in countries:
    # f-Strings f'...' anstelle von String-Verkettung 'abc' + 'def'
    ausgabe = f'Das aktuelle Land ist {country}'
    print(ausgabe)

# while-Schleife
eingabe = ''

while eingabe != 'ja':
    print('Hallo!')
    eingabe = input('Beenden? ')

# Alle Zahlen >= 0 addieren, aber mit einer while-Schleife (s.u. für for-schleife)

zahlen = [1, 0, -4, 12, 3413, -28432, 7]         

index = 0
laenge = len(zahlen)
sum = 0

while index < laenge:
    zahl = zahlen[index]
    if zahl >= 0:
        sum += zahl
    index += 1

print(sum)

# normalerweise würde man das mit einer for-Schleife machen:

zahlen = [1, 0, -4, 12, 3413, -28432, 7]
sum = 0
for zahl in zahlen:
    if zahl >= 0:
        sum += zahl

print(sum)

# Scope von Variablen

x = 'cool' # globale variable

def function():
    y = 3 # lokale variable (lokal bezogen auf die Funktion "function")

    print(x) # hier wird die globale Variable x ausgeben

    global x
    x = 'mega'  # würde ich diese Zuweisung ohne vorheriges "global x" tun
                # dann würde eine lokale Variable "x" angelegt, und die 
                # globale Variable "x" hätte weiterhin den inhalt "cool"

function()
print(x)


# return-Anweisung
# return beendet eine Funktion an dieser Stelle. Der Programmfluss
# kehrt an die Stelle des Aufrufs der Funktion zurück.

def fun(a):
    if a == 0:
        return
    print(f'{a} ist ungleich null') # wird nicht ausgeführt wenn a gleich 0 ist

fun(0) # keine Ausgabe
fun(3) # 3 ist ungleich null

# Funktion die pr+ft, ob zahl gerade ist

def gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False
    

# 'kombinierte Zuweisungsoperatoren' (engl. augmented assign operators
# oder in-place operators)
i = 0   # kein in-place operatur, nur um i zu definieren

i = i + 1
i +=    1

i = i - 1
i -=    1

i = i * 1
i *=    1

i = i / 1
i /=    1

i = i % 1
i %=    1