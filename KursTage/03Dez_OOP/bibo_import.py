
class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr
 
    def info(self):
        return f"Medium: {self.titel} ({self.erscheinungsjahr})"
 
 
class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self.autor = autor
        self.seitenzahl = seitenzahl
 
    def info(self):
        basisinfo = super().info()
        return f"{basisinfo}, Typ Buch, Autor: {self.autor}, Seiten: {self.seitenzahl}"
 
 
class Dvd(Medium):
    def __init__(self, titel, erscheinungsjahr, spielzeit, regisseur):
        super().__init__(titel, erscheinungsjahr)
        self.spielzeit = spielzeit
        self.regisseur = regisseur
 
    def info(self):
        basisinfo = super().info()
        return f"{basisinfo}, Typ DVD, Spielzeit: {self.spielzeit} Min, Regisseur: {self.regisseur}"
 
 
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

    def importieren(self):
        with open("bücher.txt", encoding="utf-8") as file:
            zeilen = file.read().splitlines()
        for zeile in zeilen:
            # funktioniert nur, wenn innerhalb von Feldern keine speziellen
            # Zeichen wie "," und "\n" auftauchen
            titel, erscheinungsjahr, autor, seitenzahl = zeile.split(",")
            buch = Buch(titel, int(erscheinungsjahr), autor, int(seitenzahl))
            self.hinzufuegen(buch)
        
        with open("dvds.csv", encoding="utf-8") as file:
            zeilen = file.read().splitlines()
        for zeile in zeilen:
            titel, erscheinungsjahr, spielzeit, regisseur = zeile.split(",")
            dvd = Dvd(titel, int(erscheinungsjahr), int(spielzeit), regisseur)
            self.hinzufuegen(dvd)
    
    def seiten(self):
        """Aufsummieren der Seiten aller gespeicherten Bücher

        Diese Methode gibt es hauptsächlich als Test um zu sehen,
        ob beim Import Zahlen als Strings oder als Zahlen interpretiert
        worden sind"""
        seiten = 0
        for medium in self.medien:
            if type(medium) is Buch:
                seiten = seiten + medium.seitenzahl
        return seiten

b1 = Buch("Das Boot", 1977, "Lothar-Günther Buchheim", 603)
d1 = Dvd("Der Spitzname", 2025, 87, "Sönke Wortmann")

bib = Bibliothek()
bib.hinzufuegen(b1)
bib.hinzufuegen(d1)
bib.importieren()
bib.auflisten()
print(bib.seiten())