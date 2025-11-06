import random

class Bankkonto:
    '''
    Clasa cont bancar
    
    Atribute:
        Kontostand: Soldul contului
        Kontoinhaber: Titularul contului
        IBAN: Număr internațional de cont bancar
    
    Metode:
        abrufen: Verificare sold
        einzahlen: Depunere
        automatisches_IBAN: Generare număr IBAN
    
    Beispiele:
        mein_konto = Bankkonto('Nicolas Arevalo Hoelscher')
        mein_konto.einzahlen(300)
        mein_konto.abrufen()
        print(mein_konto.IBAN)
    '''

    def __init__(self, Kontoinhaber):
        '''
        Inițializare cont bancar
        
        Parametri:
            Kontoinhaber (str): Numele titularului de cont
        '''
        self.Kontostand = 0
        self.Kontoinhaber = Kontoinhaber
        self.IBAN = Bankkonto.automatisches_IBAN()

    def automatisches_IBAN():
        '''
        Generare automată număr IBAN
        
        Returnează:
            str: Număr IBAN de 20 de cifre începând cu 'DE'
        '''
        iban = 'DE'
        for zahl in range(0,18):
            iban += str(random.randint(0,9))
        return iban

    def abrufen(self):
        '''
        Afișează soldul curent al contului
        '''
        print(f'Mein Kontostand betraegt: ${self.Kontostand:.2f}')

    def einzahlen(self, betrag):
        '''
        Metodă de depunere
        
        Parametri:
            betrag (float): Suma de depus
            
        Returnează:
            int: -1 dacă suma este negativă, altfel nimic
        '''
        if betrag<0:
            print('Negative Zahlen sind nicht eralubt.')
            return -1
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
