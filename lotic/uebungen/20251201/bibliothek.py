class Bibliothek:
    def __init__(self, media_list = []):
        self._media_list = media_list

    def add_media(self, media):
        self._media_list.append(media)
        return True
    def find_media_index(self, title):
        for index in range(0, len(self._media_list)):
            if self._media_list[index].get_title() == title:
                return index
        return -1
    def remove_media(self, title):
        index = self.find_media_index(title)
        if index == -1:
            return False
        self._media_list.pop(index)
        return True
    def list_medias(self):
        for media in self._media_list:
            print(media)
    def info(self):
        print('''
Willkommen in Lotics Bibliothek
[1]: Buch hinzufügen
[2]: DVD hinzufügen
[3]: Medium löschen
[4]: Liste
[5]: Beenden
        ''')

class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self._titel = titel
        self._erscheinungsjahr = erscheinungsjahr
    def get_title(self):
        return self._titel
    def get_release_year(self):
        return self._erscheinungsjahr

class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self._autor = autor
        self._seitenzahl = seitenzahl
    def get_author(self):
        return self._autor
    def get_page_count(self):
        return self._seitenzahl
    def __str__(self):
        return f'{self._titel} - {self._erscheinungsjahr} - {self._autor} - {self._seitenzahl}'
    def info(self):
        print(f'{self._titel} - {self._erscheinungsjahr} - {self._autor} - {self._seitenzahl}')


class Dvd(Medium):
    def __init__(self, titel, erscheinungsjahr,  regisseur, spielzeit):
        super().__init__(titel, erscheinungsjahr)
        self._regisseur = regisseur
        self._spielzeit = spielzeit
    def get_spielzeit(self):
        return self._spielzeit
    def get_regisseur(self):
        return self._regisseur
    def __str__(self):
        return f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}'
    def info(self):
        print(f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}')



buch1 = Buch('Momo', 1973, 'Micheal Ende', 250)
dvd1 = Dvd('The hateful eight', 2015, 'Quentin Tarantino', 168)
biblio1 = Bibliothek()
biblio1.add_media(buch1)
biblio1.add_media(dvd1)
biblio1.info()

def readBookInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    author = input('Autor: ')
    pages = input('Seitenzahl: ')
    buch = Buch(title, release_year, author, pages)
    biblio1.add_media(buch)
    print('Buch hinzugefügt')

def readDVDInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    regisseur = input('Regisseur: ')
    runtime = input('Spielzeit: ')
    dvd = Dvd(title, release_year, regisseur, runtime)
    biblio1.add_media(dvd)
    print('DVD hinzugefügt')

def removeTitle():
    title = input('Titel: ')
    media_removed = biblio1.remove_media(title)
    if media_removed:
        return print('Medium wurde entfernt')
    return print('Medium konnte nicht entfernt werden')


def readUserInput():
    userInput = input()
    try:
        userInput = int(userInput)
    except:
        print('Ungültige Eingabe')
        biblio1.info()
        readUserInput()
    if userInput == 1:
        readBookInfo()
        biblio1.info()
        readUserInput()
    elif userInput == 2:
        readDVDInfo()
        biblio1.info()
        readUserInput()
    elif userInput == 3:
        removeTitle()
        biblio1.info()
        readUserInput()
    elif userInput == 4:
        biblio1.list_medias() 
        biblio1.info()
        readUserInput()
    elif userInput == 5:
        return

readUserInput()
'''
print(buch1)
print(dvd1)

print(biblio1.find_media_index('Momo'))

buch1.info()
dvd1.info()
'''
