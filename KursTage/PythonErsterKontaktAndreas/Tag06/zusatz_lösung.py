# Zusatzaufgabe: Palindrome

# Ein Palindrom ist eine Zeichenfolge, welche
# vorwärts und rückwärts gelesen gleich ist.
# Beispiele:
# 'lagerregal'
# 'anna'
# 'madam'
# 'racecar'
# 'xyzyx'
# '012343210'
# '--------[]--------'
# 'aabaa'

# Schreibe ein Programm welches herausfindet,
# ob ein bestimmter String ein Palindrom ist.
# Der String kann fest vorgegeben sein, oder vom 
# Nutzer eingegeben. Z.B.

teststring = 'lagerregal'

palindrom = True
laenge = len(teststring)
for i in range(laenge // 2):
    if teststring[i] != teststring[laenge - 1 - i]:
        palindrom = False

if palindrom:
    print('Palindrom!')
else:
    print('Kein Palindrom')


# Alternative Lösung mit string-umkehrung

def umgekehrt(str):
    r = ''
    for s in str:
        r = s + r

    return r

if teststring == umgekehrt(teststring):
    print('Palindrom')
else:
    print('Kein Palindrom')


# "clevere" Lösung mittels slices [::]

# slice: gibt eine Teilliste zurück
# liste[start:stop:step] gibt liste zurück, aber
# nur von start-index bis stop-index (exklusive stop-index)
# mit schrittgröße step
# [::-1] bedeutet von anfang bis ende aber rückwärts (-1)

if teststring == teststring[::-1]:
    print('Palindrom')
else:
    print('kein Palindrom')