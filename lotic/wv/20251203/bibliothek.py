import sqlite3
import json
import sys
import csv

class DBController:
    def __init__(self):
        pass
    def insert_book(self, book: 'Buch'):
        try:
            connection = sqlite3.connect('biblio.db')
            insertData = book.get_dbinsert_data() 
            cur = connection.cursor()
            query = 'insert into books (title, release_year, author, page_count) values (?, ?, ?, ?)'
            cur.execute(query, insertData)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    def insert_books(self, booklist: list['Buch']):
        try:
            connection = sqlite3.connect('biblio.db')
            insertData = []
            for book in booklist:
                insert_list = book.get_dbinsert_data()
                insertData.append(insert_list)
            cur = connection.cursor()
            query = 'insert into books (title, release_year, author, page_count) values (?, ?, ?, ?)'
            cur.executemany(query, insertData)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    def insert_dvd(self, dvd: 'Dvd'):
        try:
            connection = sqlite3.connect('biblio.db')
            insertData = dvd.get_dbinsert_data() 
            cur = connection.cursor()
            query = 'insert into dvds (title, release_year, regisseur, duration) values (?, ?, ?, ?)'
            cur.execute(query, insertData)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    def insert_dvds(self, dvdlist: list['Dvd']):
        try:
            connection = sqlite3.connect('biblio.db')
            insertData = []
            for dvd in dvdlist:
                insert_list = dvd.get_dbinsert_data()
                insertData.append(insert_list)
            cur = connection.cursor()
            query = 'insert into dvds (title, release_year, regisseur, duration) values (?, ?, ?, ?)'
            cur.executemany(query, insertData)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    def book_list(self):
        try:
            connection = sqlite3.connect('biblio.db')
            cur = connection.cursor()
            query = 'select * from books'
            res = cur.execute(query)
            book_list = res.fetchall()
            connection.close()
            return book_list
        except:
            print('Ein Fehler ist aufgetreten')
            return []
    def dvd_list(self):
        try:
            connection = sqlite3.connect('biblio.db')
            cur = connection.cursor()
            query = 'select * from dvds'
            res = cur.execute(query)
            dvd_list = res.fetchall()
            connection.close()
            return dvd_list
        except:
            print('Ein Fehler ist aufgetreten')
            return []
    def books_search_by_title(self, searchstring):
        search = f'%{searchstring}%'
        try:
            connection = sqlite3.connect('biblio.db')
            cur = connection.cursor()
            query = 'select * from books where title like ?'
            res = cur.execute(query, [search])
            book_list = res.fetchall()
            connection.close()
            return book_list
        except:
            print('Ein Fehler ist aufgetreten')
            return []

class Bibliothek:
    def __init__(self, db_controller, media_list = []):
        self._db_controller = db_controller
        self._media_list = media_list
    def book_list(self, data):
        booklist = db_controller.book_list()
        booksstring = 'ID - Titel - Veröffentlicht - Autor - Seiten\n'
        if len(booklist) == 0:
            return 'Keine Bücher gefunden'
        for book in booklist:
            booksstring += f'{book[0]} - {book[1]} - {book[2]} - {book[3]} - {book[4]}\n'
        return booksstring
    def dvd_list(self, data):
        dvdlist = db_controller.dvd_list()
        dvdsstring = 'ID - Titel - Veröffentlicht - Regisseur - Spieldauer\n'
        if len(dvdlist) == 0:
            return 'Keine DVD gefunden'
        for dvd in dvdlist:
            dvdsstring += f'{dvd[0]} - {dvd[1]} - {dvd[2]} - {dvd[3]} - {dvd[4]}\n'
        return dvdsstring 
    def clear_media_list(self):
        self._media_list = []
        return True
    def add_media(self, media):
        self._media_list.append(media)
        return True
    def add_book(self, book_dict):
        book = Buch(
            book_dict['title'],
            int(book_dict['release_year']),
            book_dict['author'],
            int(book_dict['page_count'])
        )
        db_res = self._db_controller.insert_book(book)
        if db_res:
            return f'Buch mit dem Titel {book_dict['title']} wurde hinzugefügt'
        return 'Ein Fehler ist aufgetreten'
    def add_dvd(self, dvd_dict):
        dvd = Dvd(
            dvd_dict['title'],
            int(dvd_dict['release_year']),
            dvd_dict['regisseur'],
            int(dvd_dict['duration'])
        )
        db_res = self._db_controller.insert_dvd(dvd)
        if db_res:
            return f'Dvd mit dem Titel {dvd_dict['title']} wurde hinzugefügt'
        return 'Ein Fehler ist aufgetreten'
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
    def books_to_dictlist(self):
        booklist = []
        for media in self._media_list:
            if isinstance(media, Buch):
                booklist.append(media)
    def convert_to_dictlist(self):
        dictlist = []
        for media in self._media_list:
            media_dict = {
                'title': media.get_title(),
                'release_year': media.get_release_year(),
                'author': media.get_author(),
                'page_count': media.get_page_count(),
            }
            dictlist.append(media_dict)
        return dictlist
    def list_medias(self):
        for media in self._media_list:
            print(media)
    def csv_import_books(self, data):
        #import_file = open(data.path, 'r', encoding='utf-8')
        import_list = []
        with open(data['path'], encoding = 'utf-8', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                title, release_year, author, page_count = row
                book = Buch(title, release_year, author, page_count)
                import_list.append(book)
        if len(import_list) == 0:
            return 'Kein Buch zum importieren'
        inserted_into_db = self._db_controller.insert_books(import_list)
        if inserted_into_db:
            return f'{len(import_list)} Bücher importiert'
        else:
            return 'Import fehlgeschlagen'
    def csv_import_dvds(self, data):
        #import_file = open(data.path, 'r', encoding='utf-8')
        import_list = []
        with open(data['path'], encoding = 'utf-8', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                title, release_year, regisseur, duration = row
                dvd = Dvd(title, release_year, regisseur, duration)
                import_list.append(dvd)
        if len(import_list) == 0:
            return 'Keine DVD zum importieren'
        inserted_into_db = self._db_controller.insert_dvds(import_list)
        if inserted_into_db:
            return f'{len(import_list)} DVDs importiert'
        else:
            return 'Import fehlgeschlagen'
    def csv_export_books(self, data):
        #import_file = open(data.path, 'r', encoding='utf-8')
        try:
            export_list = self._db_controller.book_list()
            with open(data['path'], 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL
                )
                for book in export_list:
                    book_attr_list = list(book) 
                    book_attr_list.pop(0)
                    writer.writerow(book_attr_list)
            return f'{len(export_list)} Bücher wurden exportiert.'
        except:
            return 'Export fehlgeschlagen.'
    def csv_export_dvds(self, data):
        #TODO WORK HERE
        #import_file = open(data.path, 'r', encoding='utf-8')
        try:
            export_list = self._db_controller.book_list()
            with open(data['path'], 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL
                )
                for book in export_list:
                    book_attr_list = list(book) 
                    book_attr_list.pop(0)
                    writer.writerow(book_attr_list)
            return f'{len(export_list)} Bücher wurden exportiert.'
        except:
            return 'Export fehlgeschlagen.'

        '''
        with open(data['path'], encoding = 'utf-8', newline = '') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                title, release_year, author, page_count = row
                book = Buch(title, release_year, author, page_count)
                import_list.append(book)
        if len(import_list) == 0:
            return 'Kein Buch zum importieren'
        inserted_into_db = self._db_controller.insert_books(import_list)
        if inserted_into_db:
            return f'{len(import_list)} Bücher importiert'
        else:
            return 'Import fehlgeschlagen'
    def import_books_csv(self):
        filename = input('Welche Datei soll importiert werden? ')
        import_file = open(filename, 'r', encoding='utf-8')
        csv_string = import_file.read()
        media_list = csv_string.splitlines()
        for media_string in media_list:
            attribute_list = media_string.split(',')
            title = attribute_list[0]
            release_year = int(attribute_list[1])
            author = attribute_list[2]
            page_count = int(attribute_list[3])
            book = Buch(title, release_year, author, page_count)
            self.add_media(book)
        import_file.close()
        print(f'{len(media_list)} Bücher wurden importiert')
            '''
    def import_dvds_csv(self):
        filename = input('Welche Datei soll importiert werden? ')
        import_file = open(filename, 'r', encoding='utf-8')
        csv_string = import_file.read()
        media_list = csv_string.splitlines()
        for media_string in media_list:
            attribute_list = media_string.split(',')
            title = attribute_list[0]
            release_year = int(attribute_list[1])
            duration = int(attribute_list[2])
            regisseur = attribute_list[3]
            dvd = Dvd(title, release_year, regisseur, duration)
            self.add_media(dvd)
        import_file.close()
        print(f'{len(media_list)} DVDs wurden importiert')
    def export_books_csv(self):
        filename = input('Dateiname? ')
        export_file = open(filename, 'w', encoding='utf-8')
        csv_string = ''
        for media in self._media_list:
            media_string = f'{media.get_title()},{media.get_release_year()},{media.get_author()},{media.get_page_count()}\n'
            csv_string += media_string
        export_file.write(csv_string)
        export_file.close()
    def export_books_json(self):
        filename = input('Dateiname? ')
        export_file = open(filename, 'w')
        dict_list = self.convert_to_dictlist()
        json_string = json.dumps(dict_list)
        export_file.write(json_string)
        print(f'{len(dict_list)} Bücher wurden exportiert')
    def import_books_json(self):
        filename = input('Dateiname? ')
        import_file = open('importme.json')
        json_string = import_file.read()
        media_list = json.load(json_string)
        print(media_list)
    def info(self):
        print('coming soon')

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
    def get_dbinsert_data(self):
        return [self._titel, self._erscheinungsjahr, self._autor, self._seitenzahl]
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
    def get_dbinsert_data(self):
        return [self._titel, self._erscheinungsjahr, self._regisseur, self._spielzeit]
    def get_spielzeit(self):
        return self._spielzeit
    def get_regisseur(self):
        return self._regisseur
    def __str__(self):
        return f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}'
    def info(self):
        print(f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}')

def readBookInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    author = input('Autor: ')
    pages = input('Seitenzahl: ')
    buch = Buch(title, int(release_year), author, int(pages))
    db_controller.insert_book(buch)

def readDVDInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    regisseur = input('Regisseur: ')
    runtime = input('Spielzeit: ')
    dvd = Dvd(title, int(release_year), regisseur, int(runtime))
    db_controller.insert_dvd(dvd)

def removeTitle():
    title = input('Titel: ')
    media_removed = biblio1.remove_media(title)
    if media_removed:
        return print('Medium wurde entfernt')
    return print('Medium konnte nicht entfernt werden')

db_controller = DBController()
biblio1 = Bibliothek(db_controller)

class UIController:
    def __init__(self):
        pass
    def greeting(self):
        print('Willkommen in Lotics Bibliothek')
    def mainmenu(self):
        print('[1]: Medium hinzufügen')
        print('[2]: Liste')
        print('[3]: Suche')
        print('[4]: CSV Import/Export')
        print('[5]: JSON Import/Export')
        print('[h]: Hilfe')
        print('[q]: Beenden')
    def eval_input(self):
        userInput = ''
        while userInput != 'q':
            userInput = input()
            if userInput == '1':
                return self.media_create_menu()
            if userInput == '2':
                return self.media_list_menu()
            if userInput == '4':
                return self.csv_menu()
            elif userInput == 'q':
                return 'quit'
                break
            else:
                print('Ungültige Eingabe')
    def csv_menu(self):
        print('[1] Importiere Bücher')
        print('[2] Importiere DVDs')
        print('[3] Exportiere Bücher')
        print('[4] Exportiere DVDs')
        print('[q] Zurück')
        userInput = ''
        while True:
            userInput = input()
            if userInput == '1':
                print('Importiere Bücher aus CSV Datei')
                path = input('Pfad zu deiner CSV Datei? ')
                return({'exe': 'csv_import_books', 'path': path})
            if userInput == '2':
                print('Importiere DVDs aus CSV Datei')
                path = input('Pfad zu deiner CSV Datei? ')
                return({'exe': 'csv_import_dvds', 'path': path})
            if userInput == '3':
                print('Exportiere Bücher als CSV Datei')
                path = input('Speichern unter? ')
                return({'exe': 'csv_export_books', 'path': path})
            if userInput == 'q':
                return 'back'
            else:
                print('Ungültige Eingabe')
    def media_list_menu(self):
        print('[1] Liste Bücher')
        print('[2] Liste DVDs')
        print('[q] Zurück')
        userInput = ''
        while True:
            userInput = input()
            if userInput == '1':
                return({'exe': 'book_list'})
            if userInput == '2':
                return({'exe': 'dvd_list'})
            if userInput == 'q':
                return 'back'
            else:
                print('Ungültige Eingabe')
    def media_create_menu(self):
        print('[1] Buch hinzufügen')
        print('[2] DVD hinzufügen')
        print('[q] Zurück')
        userInput = ''
        while True:
            userInput = input()
            if userInput == '1':
                return(self.book_create_mask())
            if userInput == '2':
                return(self.dvd_create_mask())
            if userInput == 'q':
                return 'back'
            else:
                print('Ungültige Eingabe')
    def book_create_mask(self):
        title = input('Titel: ')
        release_year = input('Erscheinungsjahr: ')
        author = input('Autor: ')
        page_count = input('Seitenzahl: ')
        response = {
            'exe': 'add_book',
            'title': title,
            'release_year': release_year,
            'author': author,
            'page_count': page_count
        }
        return response
    def dvd_create_mask(self):
        title = input('Titel: ')
        release_year = input('Erscheinungsjahr: ')
        regisseur = input('Regisseur: ')
        duration = input('Spielzeit: ')
        response = {
            'exe': 'add_dvd',
            'title': title,
            'release_year': release_year,
            'regisseur': regisseur,
            'duration': duration
        }
        return response

ui_controller = UIController()
ui_controller.greeting()
ui_controller.mainmenu()

while True:
    ui_response = ui_controller.eval_input()
    if ui_response == 'quit':
        break
    if ui_response == 'back':
        ui_controller.mainmenu()
        continue
    bibmethod = getattr(biblio1, ui_response['exe'])
    bibresponse = bibmethod(ui_response)
    print(bibresponse)
    ui_controller.mainmenu()

