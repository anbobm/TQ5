class Bankkonto:
    def __init__(self, kontonummer, kontostand=0):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag} € eingezahlt.")
        else:
            print("Fehler: Betrag muss positiv sein.")

    def auszahlen(self, betrag):
        """Wird in Unterklassen überschrieben."""
        raise NotImplementedError

    def info(self):
        print(f"Kontonummer: {self.kontonummer}")
        print(f"Kontostand: {self.kontostand:.2f} €")


class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, kontostand=0, zinssatz=0.01):
        super().__init__(kontonummer, kontostand)
        self.zinssatz = zinssatz

    def auszahlen(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
            print(f"{betrag} € abgehoben.")
        else:
            print("Auszahlung abgelehnt: Kontostand reicht nicht aus.")

    def zinsen_gutschreiben(self):
        zinsen = self.kontostand * self.zinssatz
        self.kontostand += zinsen
        print(f"Zinsen gutgeschrieben: {zinsen:.2f} €")


class Girokonto(Bankkonto):
    def __init__(self, kontonummer, kontostand=0, ueberziehungsrahmen=1000):
        super().__init__(kontonummer, kontostand)
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def auszahlen(self, betrag):
        if self.kontostand - betrag >= -self.ueberziehungsrahmen:
            self.kontostand -= betrag
            print(f"{betrag} € abgehoben.")
        else:
            print("Auszahlung abgelehnt: Überziehungsrahmen überschritten.")


# ----------------------------------------
# Testprogramm
# ----------------------------------------
print("=== Sparkonto Test ===")
spk = Sparkonto("SPK123", 500, 0.02)
spk.info()
spk.einzahlen(200)
spk.auszahlen(100)
spk.zinsen_gutschreiben()
spk.auszahlen(700)  # sollte fehlschlagen
spk.info()

print("\n=== Girokonto Test ===")
gk = Girokonto("GIR456", 300, 1000)
gk.info()
gk.einzahlen(150)
gk.auszahlen(600)
gk.auszahlen(1000)  # im Rahmen möglich
gk.auszahlen(200)   # sollte fehlschlagen
gk.info()