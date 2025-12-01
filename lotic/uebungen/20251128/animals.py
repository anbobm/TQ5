class Animal:
    def __init__(self, name, pate):
        self._name = name
        self._pate = pate

    def geraeusch(self, geraeusch):
        print(geraeusch)

    def get_geraeusch(self):
        return self._geraeusch

class Cat(Animal):
    def __init__(self, name, pate, leben):
        super().__init__(name, pate)
        self._geraeusch = 'miau'

garfield = Cat('Garfield', 'Lotic', 9)
garfield.geraeusch(garfield.get_geraeusch())
