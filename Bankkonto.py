import random
# Diese Variante ist besser!
class Bankkonto:
    # Eigenschaften:
        # Kontostand, Kontoinhaber, IBAN
    # Funktionen/Methoden:
        # Abrufen, Einzahlen, Auszahlen

    #Konstruktor
    def __init__(self, Kontoinhaber):
        self.Kontostand = 0
        self.Kontoinhaber = Kontoinhaber
        self.IBAN = Bankkonto.automatisches_IBAN()

    def automatisches_IBAN():
        iban = 'DE'
        for zahl in range(0,18):
            iban += str(random.randint(0,9))
        return iban

    def abrufen(self):
        print(f'Mein Kontostand betraegt: ${self.Kontostand:.2f}')

    def einzahlen(self, betrag):
        self.Kontostand = self.Kontostand + betrag
        print(f'Nach deine Einzahlung von ${betrag} haben wir folgendes Kontostand: ${self.Kontostand:.2f}')


mein_konto = Bankkonto('Nicolas Arevalo Hoelscher')
mein_konto.einzahlen(300)
mein_konto.einzahlen(9384.56)
mein_konto.einzahlen(19)
mein_konto.einzahlen(546)
print(mein_konto.IBAN)


dein_konto = Bankkonto('Nico Himpele')
dein_konto.einzahlen(234)
print(dein_konto.IBAN)