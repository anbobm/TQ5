class Produkt:
    def __init__(self, name, preis):
        self._name = name
        self._preis = preis

    def info(self):
        return f"Produkt {self._name} für {self._preis} €"
    
class Lebensmittel(Produkt):
    def __init__(self, name, preis, haltbarkeit):
        super().__init__(name, preis)
        self._haltbarkeit = haltbarkeit

    def info(self):
        return f"{super().info()}, Lebensmittel haltbar bis {self._haltbarkeit}"

class Elektronik(Produkt):
    def __init__(self, name, preis, garantie_dauer):
        super().__init__(name, preis)
        self._garantie_dauer = garantie_dauer
    
    def info(self):
        return f"{super().info()}, Elektronik mit Garantie von {self._garantie_dauer} Jahren"

class Kleidung(Produkt):
    def __init__(self, name, preis, groesse, farbe):
        super().__init__(name, preis)
        self._groesse = groesse
        self._farbe = farbe

    def info(self):
        return f"{super().info()}, Kleidung der Größe {self._groesse} mit Farbe {self._farbe}"

class Warenkorb:
    def __init__(self, produkte = []):
        self._produkte : list[Produkt] = produkte
    
    def hinzufuegen(self, produkt):
        self._produkte.append(produkt)

    def auflisten(self):
        for produkt in self._produkte:
            print(produkt.info())
    
    def gesamtpreis(self):
        sum = 0
        for produkt in self._produkte:
            sum = sum + produkt._preis
        return sum
    
    def speichern(self):
        with open("warenkorb.txt", "w", encoding="utf-8") as file:
            for produkt in self._produkte:
                file.write(f"{produkt._name},{produkt._preis}\n")
    
produkte = [
    Lebensmittel("Goldener Apfel", 1000, "2050-01-01"),
    Elektronik("Gaming-PC", 2499, 5)
]

warenkorb = Warenkorb(produkte)

warenkorb.hinzufuegen(Elektronik("C64", 250, 10))
warenkorb.hinzufuegen(Kleidung("Schuhe", 99, "XXL", "schwarz"))

warenkorb.auflisten()
print(f"Gesamtpreis: {warenkorb.gesamtpreis()} €")

warenkorb.speichern()