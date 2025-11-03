from datetime import datetime, time
from time import sleep

feierabend = time(16)

while True:
    print('Feierabend? ...', end='')
    sleep(1)
    
    jetzt = datetime.now().time()

    if jetzt >= feierabend:
        print('Feierabend!')
        break
    else:
        print('leider noch nicht :(')

    sleep(1)