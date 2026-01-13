class Bankkonto:
    def __init__(self, kontonummer):
        self._kontonummer = kontonummer
        self._kontostand = 0
    
    def einzahlen(self, betrag):
        self._kontostand = self._kontostand + betrag

    def auszahlen(self, betrag):
        pass

    def info(self):
        print(f"Kontonummer {self._kontonummer}, Kontostand {self._kontostand:.2f}")

class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, zinssatz):
        super().__init__(kontonummer)
        self._zinssatz = zinssatz
    
    def zinsen_gutschreiben(self):
        zinsen = self._kontostand * self._zinssatz
        self._kontostand = round(self._kontostand + zinsen, 2)

    def auszahlen(self, betrag):
        if self._kontostand - betrag < 0:
            return
        
        self._kontostand = self._kontostand - betrag

class Girokonto(Bankkonto):
    def __init__(self, kontonummer, dispo):
        super().__init__(kontonummer)
        self._dispo = dispo

    def auszahlen(self, betrag):
        if self._kontostand + self._dispo < betrag:
            return
        
        self._kontostand = self._kontostand - betrag

konto = Girokonto("DE824612874126", 10)
konto.info()
konto.einzahlen(50)
konto.info()
konto.auszahlen(30)
konto.info()
konto.auszahlen(50)
konto.info()
konto.auszahlen(30)
konto.info()
konto.auszahlen(0.01)
konto.info()

sparkonto = Sparkonto("DE28974974", 0.03)
sparkonto.einzahlen(100)
sparkonto.auszahlen(50)
sparkonto.auszahlen(100)
sparkonto.zinsen_gutschreiben()
sparkonto.info()