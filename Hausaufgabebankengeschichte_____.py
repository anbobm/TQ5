"""Aufgabe 3
In einer Banksoftware sollen zwei verschiedene Kontotypen mittels Klassen abgebildet werden. Alle Bankkonten haben die Methode Attribute Kontonummer und Kontostand und die Methoden einzahlen(betrag), auszahlen(betrag) und eine Methode info(), welche Informationen zum Konto ausgibt.
Sparkonto
•	hat einen Zinssatz, dieser wird mit zinsen_gutschreiben() auf das Guthaben angewendet und der Kontostand entsprechend erhöht
•	abheben(betrag) darf nur erfolgreich sein, wenn der Kontostand dafür ausreicht, er darf also nicht negativ werden
Girokonto
•	hat einen Überziehungsrahmen
•	abheben(betrag) darf nur innerhalb des Überziehungsrahmens erfolgreich sein, der Kontostand darf also höchstens bis zum Überziehungsrahmen negativ sein, wenn also z.B. Überziehungsrahmen 1000 € ist, dann darf der Kontostand -1000 € sein, aber nicht niedriger
Schreib im Anschluss ein Programm um diese zwei Kontoarten als Objekte anzulegen und deren Methoden zu testen.

"""
class Konto:
    def __init__(self, kontonummer):
        self._kontonummer=kontonummer
        self._kontostand=0

    def einzahlen(self, betrag):
        self._kontostand=self._kontostand+betrag
        

    def auszahlen(self, betrag):
        if self._kontostand>betrag:
            self._kontostand=self._konstand-betrag
        else:
            print("Mog ich nicht")

    def info(self):
        print (f"bla bla {self._kontonummer}, bla bla bla {self._kontostand}")


class Sparkonto(Konto):
    def __init__(self, kontonummer, zinssatz):
        super().__init__(kontonummer)
        self._zinssatz=zinssatz

    def zinsengutschreiben(self):
        self._kontostand=(self._kontostand*self._zinssatz/100)+self._kontostand

class Girokonto(Konto):
    def __init__(self, kontonummer,überziehungsrahmen):
        super().__init__(kontonummer)
        self._überziehungsrahmen=überziehungsrahmen
    
    def auszahlen(self, betrag):
        if betrag>self._kontostand+self._überziehungsrahmen:
            print("Mog ich nicht")
        else:
            self._kontostand=self._konstand-betrag            

objekt1=Konto(666)
objekt1.info()

objekt2=Sparkonto(99999,100)
objekt2.einzahlen(2222)
objekt2.info()
objekt2.zinsengutschreiben()
objekt2.info()





