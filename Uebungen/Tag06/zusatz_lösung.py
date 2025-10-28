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
