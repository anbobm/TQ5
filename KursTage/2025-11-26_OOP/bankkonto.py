class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontostand = 0
        self._kontoinhaber = kontoinhaber

    def __str__(self):
        return f"Konto von {self._kontoinhaber} mit Kontostand {self._kontostand}"
    
    def einzahlen(self, betrag):
        if betrag < 0:
            print("Negative Beträge können nicht eingezahlt werden")
            return
        
        self._kontostand += betrag

    def abheben(self, betrag):
        if betrag < 0:
            print("Negative Beträge können nicht abgehoben werden")
            return
        
        if self._kontostand < betrag:
            print("Abheben nicht möglich, Deckung nicht ausreichend")
            return

        self._kontostand -= betrag

konto1 = Bankkonto("Alice")
print(konto1)
konto1.einzahlen(100)
print(konto1)
konto1.abheben(30)
print(konto1)
konto1.abheben(200) # sollte Fehler ausgeben und Abhebung wird nicht durchgeführt
print(konto1)

konto1.einzahlen(-10) # sollte Fehler ausgeben und Einzahlen wird nicht durchgeführt
konto1.abheben(-10) # sollte Fehler ausgeben und Abhebung wird nicht durchgeführt