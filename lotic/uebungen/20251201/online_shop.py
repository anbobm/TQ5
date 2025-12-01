'''
Author: Timo Roehle
Last Change: 01.12.2025
'''

class Produkt:
    def __init__(self, name: str, preis: float):
        self._name = name
        self._preis = preis
    def get_price(self):
        return self._preis
    def info(self):
        return f'{self._name} - {self._preis}'

class Lebensmittel(Produkt):
    def __init__(self, name: str, preis: float, mhd: str):
        super().__init__(name, preis)
        self._mhd = mhd # Mindesthaltbarkeitsdatum
    def info(self):
        return super().info() + f' - MHD: {self._mhd}'


class Elektronik(Produkt):
    def __init__(self, name: str, preis: float, garantie_dauer: int):
        super().__init__(name, preis)
        self._garantie_dauer = garantie_dauer
    def info(self):
        return super().info() + f' - Garantie: {self._garantie_dauer} millisekunden :D'


class Kleidung(Produkt):
    def __init__(self, name: str, preis: float, groesse: str, farbe: str):
        super().__init__(name, preis)
        self._groesse = groesse
        self._farbe = farbe
    def info(self):
        return super().info() + f' - Groesse: {self._groesse} - Farbe: {self._farbe}'

class Warenkorb:
    def __init__(self):
        self._products: list[Produkt] = []
    def hinzufuegen(self, product: Produkt):
        self._products.append(product)
    def gesamtpreis(self):
        sum = 0
        for product in self._products:
            sum += product.get_price()
        return sum
    def auflisten(self):
        for product in self._products:
            print(product.info())

# Some Tests

donut = Lebensmittel('Donut', 1.99, '03-12-2025')
fernseher = Elektronik('Fernseher', 999.99, '31536000000')
lederjacke = Kleidung('Lederjacke', 199.99, 'S', 'Schwarz')

warenkorb = Warenkorb()
warenkorb.hinzufuegen(donut)
warenkorb.hinzufuegen(fernseher)
warenkorb.hinzufuegen(lederjacke)
warenkorb.auflisten()
print(f'Gesamtpreis: {warenkorb.gesamtpreis()}')
