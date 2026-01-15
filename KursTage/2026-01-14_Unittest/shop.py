class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

    def info(self):
        return f"Produkt {self.name} für {self.preis} €"
    
class Lebensmittel(Produkt):
    def __init__(self, name, preis, haltbarkeit):
        super().__init__(name, preis)
        self.haltbarkeit = haltbarkeit

    def info(self):
        return f"{super().info()}, Lebensmittel haltbar bis {self.haltbarkeit}"

class Elektronik(Produkt):
    def __init__(self, name, preis, garantie_dauer):
        super().__init__(name, preis)
        self.garantie_dauer = garantie_dauer
    
    def info(self):
        return f"{super().info()}, Elektronik mit Garantie von {self.garantie_dauer} Jahren"

class Kleidung(Produkt):
    def __init__(self, name, preis, groesse, farbe):
        super().__init__(name, preis)
        self.groesse = groesse
        self.farbe = farbe

    def info(self):
        return f"{super().info()}, Kleidung der Größe {self.groesse} mit Farbe {self.farbe}"

class Warenkorb:
    def __init__(self, produkte = []):
        self.produkte : list[Produkt] = produkte
    
    def hinzufuegen(self, produkt):
        self.produkte.append(produkt)

    def auflisten(self):
        result = ""
        for produkt in self.produkte:
            result += produkt.info() + "\n"
        return result
    
    def gesamtpreis(self):
        sum = 0
        for produkt in self.produkte:
            sum = sum + produkt.preis
        return sum
    
produkte = [
    Lebensmittel("Goldener Apfel", 1000, "2050-01-01"),
    Elektronik("Gaming-PC", 2499, 5)
]

warenkorb = Warenkorb(produkte)

warenkorb.hinzufuegen(Elektronik("C64", 250, 10))
warenkorb.hinzufuegen(Kleidung("Schuhe", 99, "XXL", "schwarz"))

print(warenkorb.auflisten())
print(f"Gesamtpreis: {warenkorb.gesamtpreis()} €")
