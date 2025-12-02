class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self.titiel = titel
        self.erscheinungsjahr = erscheinungsjahr

    def info(self):
        rfeturn f'Titel: {self.titel}, Jahr: {self.erscheinungsjahr}'


class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self.autor = autor
        self.seitenzahl = seitenzahl

    def info(self):
        return (f'Buch - Titel: {self.titel}, Jahr: {self.erscheinungsjahr},'
                f'Autor: {self.autor}, Seiten: {self.seitenzahel}')
    
class Dvd(Medium):
    def __init__(self, titel, erscheinungjahr, spielzeit, regisseur):
        super().__init__(titel, erscheinungjahr)
        self. spielzeit = spielzeit
        self. regisseur = regisseur

    def info(self):
        return (f'DVD - Titel: {self.titel}, Jahr: {self.erscheinungsjahr},'
                f'Spielzeit: {self.spielzeit} min, Regisseur: {self.regisseur}')
    

class Bibliothek:
    def __init__(self):
        self.medien = []

    def hinzuguegen(self, medium):
        self.medien.append(medium)

    def entfernen(self, medium):
        if medium in self.medien:
            self.medien.remove(medium)

    def auflisten(self):
        for m in self.medien:
            print(m.info())