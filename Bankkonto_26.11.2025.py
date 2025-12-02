class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontostand = 0
        self._kontoinhaber = kontoinhaber

    def __str__(self):
        return f'Konto von {self._kontoinhaber} mit Kontostand {self._kontostand}'
    
    def einzahlen(self, betrag):
        self._kontostand += betrag

    def abheben(self, betrag):
        if self._kontostand >= betrag:
            self._kontostand = self._kontostand - betrag   # self._kontostand -= betrag (ist das gleiche)
        else:
            print('Abheben nicht möglich, Deckung nicht ausreichend')
    

konto = Bankkonto('Paul Schmidt')

print(konto)

konto.einzahlen(100)

print(konto)

konto.abheben(200)

print (konto)