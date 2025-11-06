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

# Schreibe ein Programm welches herausfindet,
# ob ein bestimmter String ein Palindrom ist.
# Der String kann fest vorgegeben sein, oder vom 
# Nutzer eingegeben. Z.B.

teststring = 'lagerregal'

# Auf einzelne Zeichen eines Strings kann mit []
# zugegriffen werden, was wir von Listen kennen

erstes_zeichen = teststring[0] # erstes_zeichen ist dann 'l'

laenge = len(teststring)
letzerIndex = laenge - 1
palindrom = True

for index in range(laenge // 2):
    if teststring[index] != teststring[letzerIndex - index]:
        palindrom = False

if palindrom:
    print('Es ist ein Palindrom')
else:
    print('Es ist kein Palindrom')


# Alternative mit Funktionen
def is_palindrome(str):
    laenge = len(str)
    letzerIndex = laenge - 1
    for index in range(laenge):
        if str[index] != str[letzerIndex - index]:
            return False
    return True

print(is_palindrome('xxyxx'))

# Alternative mit String-Umkehrung

teststring = 'lagerregal'

def umgekehrt(str):
    r = ''
    for s in str:
        r = s + r

    return r

umgekehrt('abcdef')

if teststring == umgekehrt(teststring):
    print('Palindrom')
else:
    print('Kein Palindrom')