import math

class form():

def flaeche(self):
        """Berechnet die Fläche der Form."""
        raise NotImplementedError("Methode 'flaeche()' muss in der Unterklasse implementiert werden.")

    def umfang(self):
        """Berechnet den Umfang der Form."""
        raise NotImplementedError("Methode 'umfang()' muss in der Unterklasse implementiert werden.")

class Rechteck(form):
        def __init__(self,breite,höhe):
                self.breite = breite
                self.höhe = höhe

        def fläche(self):
                return self.breite * self.höhe
        
        def umfang(self):
                return 2 * (self.breite + self.höhe)
        
