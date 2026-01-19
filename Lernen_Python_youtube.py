
x = 8


print('Hallo Ionut')
print(1 + x)

name = input('Bitte gebe den Name ein: ')

mein_name = 'Ionut Strainescu'
age = '40'
city = 'Nürnberg'

is_woman = False

if is_woman:
    print('Sehr geehrte Frau ' + name + ',')
else:
    print('Sehr geehrter Herr ' + name + ',')

print('')
print('Mein Name ist ' + mein_name + '.')
print('Ich bin ' + age + ' Jahre alt.')
print('Ich komme aus ' + city + '.')
input('Bitte beliebige Taste drücken...')
'''
'''
stundenlohn = input('Bitte gebe deinen Stundenlohn ein: ')
tag = 8 * int(stundenlohn)
monat = tag * 20
jahr = monat * 12

print('Dein Stundenlohn beträgt ' + str(stundenlohn) + '€')
print('Du verdienst ' + str(tag) + ' € pro Tag.')
print('Du verdienst ' + str(monat) + ' € pro Monat.')
print('Du hast ein Jahresgehalt von ' + str(jahr) + ' €.')



for x in range(1, 100):
    print(x)