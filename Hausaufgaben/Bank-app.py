class konto():
    def __init__(self,ibahn):
        self.kontostand = 0.00
        self.ibahn = ibahn
    
    def __str__(self):
        f"Ihr Aktueller Kontostand ist  {self.kontostand}"
        return

    def notenough(self, betrag):
        if betrag < self.kontostand:
            print("Auszahlung ungültig zu Niedriger Kontostand")
            return
    
    def einzahlen(self,betrag1):
        self.kontostand+=betrag1

class sparkonto(konto):
    def __init__(self,ibahn, kontostand=0, zinsatz=0.01):
        super().__init__(ibahn, kontostand)
        self.zinssatz = zinssatz

    def auszahlen(self,betrag):
        if self.kontostand > betrag:
            self.kontostand+betrag
        else: 
            print("Auszahlung abgelehnt: ihr kontostand von {kontostand} ist zu niedrig")
    
    def zinsplus(self):
        zinsen = self.kontostand * self.zinssatz
        print("Ihre zinsen wurden gutgeschrieben")

class Girokonto(konto):
    def __init__(self, ibahn, kontostand=0, ueberziehungsrahmen=1000):
        super().__init__(ibahn, kontostand)
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
spk = sparkonto("SPK123", 500, 0.02)
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