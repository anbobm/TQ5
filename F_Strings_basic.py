# f-strings Einfürhung

name = 'Timo'
alter = 42

# Wir wollen einen String ausgeben, der beide Variablen enthällt

# Möglichkeit 1 mit + (concat = verbindung von strings)
print('Hallo ich heiße ' + name + ' und bin ' + str(alter) + ' Jahre alt.')

# Möglichkeit 2 mit f-string
print(f'Hallo ich heiße {name} und bin {alter} Jahre alt.')