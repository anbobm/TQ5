class Auto:
    def __init__(self, marke, baujahr):
        self._marke = marke
        self._baujahr = baujahr
    
    def get_marke(self):
        return self._marke
    
    def get_baujahr(self):
        return self._baujahr
    
    def zusammenfassen(self):
        print(f"Auto der Marke {self._marke}, Baujahr {self._baujahr}")

auto1 = Auto("Opel", 2000)
auto2 = Auto("BMW", 1950)

auto1.zusammenfassen()
auto2.zusammenfassen()
