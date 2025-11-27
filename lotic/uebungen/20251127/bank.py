class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontoinhaber = kontoinhaber
        self._kontostand = 0

    def einzahlen(self, betrag):
        if betrag < 0:
            print('Ungültiger Betrag. Vorgang abgebrochen.')
            return False
        self._kontostand += betrag
        return True

    def abheben(self, betrag):
        if betrag < 0:
            print('Ungültiger Betrag. Vorgang abgebrochen.')
            return False
        if betrag > self._kontostand:
            print('Deckung nicht ausreichen.')
            return False
        self._kontostand -= betrag
        return True

    def __str__(self):
        return f'Kontoinhaber: {self._kontoinhaber}\nKontostand: {self._kontostand}'

class Bank:
    def ueberweisen(self, senderKonto, empfaengerKonto, betrag):
        abgehoben = senderKonto.abheben(betrag)
        if abgehoben == False:
            return False
        eingezahlt = empfaengerKonto.einzahlen(betrag)
        if eingezahlt == False:
            return False
        return True

bank = Bank()
kontoBob = Bankkonto('Bob')
kontoBob.einzahlen(100)
kontoAlice = Bankkonto('Alice')
kontoAlice.einzahlen(100)

print('***Konten vor der Ueberweisung***')
print(kontoBob)
print(kontoAlice)
bank.ueberweisen(kontoBob, kontoAlice, 70)
print('***Konten nach der Ueberweisung***')
print(kontoBob)
print(kontoAlice)
bank.ueberweisen(kontoBob, kontoAlice, -70)
