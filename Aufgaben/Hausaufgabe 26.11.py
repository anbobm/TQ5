class Bankkonto:
    def __init__(self, kontoinhaber):
        self._kontoinhaber = kontoinhaber
        self._kontostand = 0

    def einzahlen(self, betrag):
        if betrag <= 0:
            print("Fehler: Betrag muss Positiv sein.")
            return

        self._kontostand += betrag
        print(f"Es wurden {betrag} Euro eingezahlt. Neuer Kontostand: {self._kontostand} Euro")

    def abheben(self, betrag):
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein.")
            return

        if betrag > self._kontostand:
            print("Fehler: Nicht genügend Guthaben für diese Abhebung.")
            return

        self._kontostand -= betrag
        print(f"Es wurden {betrag} Euro abgehoben. Neuer Kontostand: {self._kontostand} Euro")

    def __str__(self):
        return f"Inhaber: {self._kontoinhaber}, Kontostand: {self._kontostand} Euro"


konto1 = Bankkonto("Alice")
print(konto1)
konto1.einzahlen(100)
print(konto1)
konto1.abheben(30)
print(konto1)
konto1.abheben(200)




