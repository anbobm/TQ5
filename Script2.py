name = input('Bitte gebe den Name ein: ')

mein_name = 'Ionut Strainescu'
age = '40'
city = 'Nürnberg'

is_woman = False

if is_woman:
    print('Sehr geehrte Frau ' + name + ',')
    print(f'Sehr geehrte Frau {name},') # kommt das gleiche ergebniss raus wie zeile 10 (f-string) er gibt aus genau so wie du geschrieben hast mit alle leerzeichen
else:
    print('Sehr geehrter Herr ' + name + ',')

print('')
print('Mein Name ist ' + mein_name + '.')
print('Ich bin ' + age + ' Jahre alt.')
print('Ich komme aus ' + city + '.')
input('Bitte beliebige Taste drücken...')