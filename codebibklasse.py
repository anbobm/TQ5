class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr

    def info(self):
        return f"{self.titel} ({self.erscheinungsjahr})"


class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self.autor = autor
        self.seitenzahl = seitenzahl

    def info(self):
        return f"Buch: {self.titel}, {self.erscheinungsjahr}, Autor: {self.autor}, Seiten: {self.seitenzahl}"


class Dvd(Medium):
    def __init__(self, titel, erscheinungsjahr, spielzeit, regisseur):
        super().__init__(titel, erscheinungsjahr)
        self.spielzeit = spielzeit
        self.regisseur = regisseur

    def info(self):
        return f"DVD: {self.titel}, {self.erscheinungsjahr}, Spielzeit: {self.spielzeit} Min, Regisseur: {self.regisseur}"


class Bibliothek:
    def __init__(self):
        self.medien = []

    def hinzufuegen(self, medium):
        self.medien.append(medium)

    def entfernen(self, medium):
        if medium in self.medien:
            self.medien.remove(medium)

    def auflisten(self):
        for m in self.medien:
            print(m.info())


#   Test    
if __name__ == "__main__":
    b1 = Buch("Das Boot", 1977, "Lothar-Günther Buchheim", 603)
    d1 = Dvd("Der Spitzname", 2025, 87, "Sönke Wortmann")

    bib = Bibliothek()
    bib.hinzufuegen(b1)
    bib.hinzufuegen(d1)

    bib.auflisten()
