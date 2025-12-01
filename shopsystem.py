class Artikel:
    def __init__(self, bezeichnung, betrag):
        self.bezeichnung = bezeichnung
        self.betrag = betrag

    def beschreibung(self):
        return f"{self.bezeichnung} - {self.betrag} Euro"

class Nahrungsmittel(Artikel):
    def __init__(self, bezeichnung, betrag, ablauftermin):
        super().__init__(bezeichnung, betrag)
        self.ablauftermin = ablauftermin

    def beschreibung(self):
        return f"{self.bezeichnung} - {self.betrag} Euro (Ablaufdatum: {self.ablauftermin})"

class Technikprodukt(Artikel):
    def __init__(self, bezeichnung, betrag, garantiezeit):
        super().__init__(bezeichnung, betrag)
        self.garantiezeit = garantiezeit

    def beschreibung(self):
        return f"{self.bezeichnung} - {self.betrag} Euro (Garantiezeitraum: {self.garantiezeit} Monate)"

class Bekleidung(Artikel):
    def __init__(self, bezeichnung, betrag, ausführung, farbe):
        super().__init__(bezeichnung, betrag)
        self.ausführung = ausführung
        self.farbe = farbe

    def beschreibung(self):
        return f"{self.bezeichnung} - {self.betrag} Euro (Ausführung: {self.ausführung}, Farbe: {self.farbe})"

class Einkaufswagen:
    def __init__(self):
        self.artikel_liste = []

    def artikel_einfügen(self, artikel):
        self.artikel_liste.append(artikel)

    def berechne_summe(self):
        gesamt = 0
        for artikel in self.artikel_liste:
            gesamt += artikel.betrag
        return gesamt

    def zeige_inhalt(self):
        for position, artikel in enumerate(self.artikel_liste, 1):
            print(f"{position}. {artikel.beschreibung()}")

# Test Auslösen
if __name__ == "__main__":
    
    obst = Nahrungsmittel("Bio-Äpfel", 1.70, "11.11.2025")
    computer = Technikprodukt("Notebook", 832.99, 24)
    pullover = Bekleidung("Wollpullover", 34.44, "XXS", "Grau")

    mein_einkauf = Einkaufswagen()
    mein_einkauf.artikel_einfügen(obst)
    mein_einkauf.artikel_einfügen(computer)
    mein_einkauf.artikel_einfügen(pullover)

    print("Einkaufswagen Inhalt:")
    print("-" * 40)
    mein_einkauf.zeige_inhalt()
    print("-" * 40)
    print(f"Gesamtbetrag: {mein_einkauf.berechne_summe():.2f} Euro")