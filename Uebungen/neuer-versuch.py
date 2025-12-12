class konto():
    def __init__(self,kontonummer,kontostand=0.00):
        self.kontonummer = kontonummer

    def auszahlen(self, betrag):
        if betrag < self.kontostand:
            self._kontosatand = self.kontostand - betrag
            print("Ihr Aktueller Kontostand ist nun " + str(self.kontostand))
            return
        else:
            print("Auszahlung nicht möglich. Nicht genügend Deckung.")
            return

    def einzahlen(self, betrag1):
        self._kontostand = self.kontostand + betrag1
        print("Ihr Aktueller Kontostand ist nun " + self.kontostand)
        return

    def info(self):
        print("Ihr aktueller kontostand ist " + self.kontostand)
        return
    
class girokonto(konto):
    def __init__(self,kontonummer,kontostand=0.00, überbeziehungsrahmen=1000):
        self.kontonummer = kontonummer
    
    def überziehung(self,betrag):
        if self.kontostand < betrag:
            kontostand-=betrag
            print("Ihr akuteller Kontostand ist "+str(kontostand))

class sparkonto(konto):
    def __init__(self, kontonummer,kontostand=0.00,zinssatz=0.01):
        self.kontonummer=kontonummer
    
    def zinsrechnung(self):
        self.kontostand * zinssatz
