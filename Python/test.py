class Auto:
    def __init__(self,marke,modell,jahr,tueren):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren


auto1 = Auto("Volkswagen","Polo", 2000,  2)
auto2 = Auto("Mercedes", "Benz", 2018, 2,)

print(auto1.marke, auto1.modell, auto1.jahr, auto1.raeder, auto1.tueren)
print(auto2.marke, auto2.modell, auto2.jahr, auto2.raeder, auto2.tueren)



