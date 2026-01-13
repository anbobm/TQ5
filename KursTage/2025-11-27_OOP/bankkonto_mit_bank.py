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
            return False
        
        if self._kontostand < betrag:
            print("Abheben nicht möglich, Deckung nicht ausreichend")
            return False

        self._kontostand -= betrag
        return True

class Bank:
    def überweisen(self, konto1, konto2, betrag):
        erfolg = konto1.abheben(betrag)

        if not erfolg:
            return False
        
        konto2.einzahlen(betrag)
        return True

bank = Bank()

alice = Bankkonto("Alice")
alice.einzahlen(100)
bob = Bankkonto("Bob")

bank.überweisen(alice, bob, 50)