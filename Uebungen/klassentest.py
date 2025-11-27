class Auto():
    """ Das ist meine Autoklasse so das ich nicht jedesmal alles aufs Neue Definieren muss"""
    def __init__(self, marke, modell, jahr, türen):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.räder = 4
        self.türen = türen

auto1 = Auto("Volkswagen","Polo", 2000,  2)
auto2 = Auto("Mercedes","Benz", 2018, 2)
print (auto1.marke)