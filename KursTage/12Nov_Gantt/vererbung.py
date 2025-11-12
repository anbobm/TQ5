class Bank:
    def __init__(self, name:str, adresse:str):
        self.name = name
        self.adresse = adresse
        self.konten = []


class Konto:
    #Alle gemeinsamkeiten hier definieren!
    # Kontostand
    # Kontoinhaber
    # Zinsatz
    # Kundenummer
    # IBAN
    # BIC
    def __init__(self, bankname:str, konstand:float, kontoinhaber:str, zinsatz:float, kundennummer:str, iban:str, bic:str):
        self.bankname = bankname
        self.kontostand = konstand
        self.kontoinhaber = kontoinhaber
        self.zinsatz = zinsatz
        self.kundennummer = kundennummer
        self.iban = iban
        self.bic = bic

    def einzahlen(self, betrag:float):
        self.kontostand += betrag

    def auszahlen(self, betrag:float):
        self.kontostand -= betrag

    def kontostand_anzeigen(self):
        return self.kontostand
    
    def konto_details(self):
        return f"Konto von {self.kontoinhaber}, IBAN: {self.iban}, BIC: {self.bic}, Kontostand: {self.kontostand}, Zinsatz: {self.zinsatz}%, Kundennummer: {self.kundennummer}"


class DebitKonto(Konto):

    def __init__(self, konstand, kontoinhaber, zinsatz, kundennummer, iban, bic):
        super().__init__(konstand, kontoinhaber, zinsatz, kundennummer, iban, bic)

    def auszahlen(self, betrag:float):
        if betrag > self.kontostand:
            print("Auszahlung nicht möglich: Unzureichender Kontostand.")
        else:
            super().auszahlen(betrag)

class KreditKonto(Konto):
    def __init__(self, konstand:float, kontoinhaber:str, zinsatz:float, kundennummer:str, iban:str, bic:str, kreditlimit:float):
        super().__init__(konstand, kontoinhaber, zinsatz, kundennummer, iban, bic)
        self.kreditlimit = kreditlimit

    def auszahlen(self, betrag:float):
        if betrag > self.kontostand + self.kreditlimit:
            print("Auszahlung nicht möglich: Kreditlimit überschritten.")
        else:
            super().auszahlen(betrag)

class SparKonto(Konto):
    def __init__(self, konstand:float, kontoinhaber:str, zinsatz:float, kundennummer:str, iban:str, bic:str):
        super().__init__(konstand, kontoinhaber, zinsatz, kundennummer, iban, bic)
        # Hoeheren Zinsatz fuer SparKonto
        self.zinsatz += 1.0  # Beispiel: 1% hoeherer Zinsatz