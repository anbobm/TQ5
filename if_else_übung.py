# is else = wenn dann
'''
größe = 170

#if größe < 180:
   # print('Du bist klein')

if größe > 180:
    print('Du bist groß')
else:
    print('Du bist klein')
'''
'''
ist_frau = False

print(not True) # False
print(not False) # True

if not ist_frau:
    print('Irgendjemand ist weiblich')
else:
    print('Irgendjemand ist männlich')
'''

zahl = 49

if zahl < 10:
    print('Zahl ist kleiner als 10')
elif zahl > 10 and zahl < 20:
    print('Die zahl liegt zwischen 10 und 20')
elif zahl > 20 and zahl < 50:
    print('Zahl liegt zwischen 20 und 50')
else:
    print('Zahl ist größer gleich 50')