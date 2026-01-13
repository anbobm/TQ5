class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt
    
    def jahresgehalt(self):
        return self.gehalt * 12
    
    def info(self):
        return f"Der Mitarbeiter {self.name} verdient {self.jahresgehalt()} € im Jahr."
    
class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, bonus):
        super().__init__(name, gehalt)
        self.bonus = bonus
    
    def jahresgehalt(self):
        return super().jahresgehalt() + self.bonus

class Entwickler(Mitarbeiter):
    def __init__(self, name, gehalt, programmiersprache):
        super().__init__(name, gehalt)
        self.programmiersprache = programmiersprache

    def info(self):
        return f"{super().info()} Programmiert in {self.programmiersprache}"

mitarbeiter1 = Mitarbeiter("Paul", 4000)
mitarbeiter2 = Mitarbeiter("Maria", 5000)
manager = Manager("Eva", 7000, 10000)
entwickler = Entwickler("Peter", 6000, "C#")

print(mitarbeiter1.info())
print(mitarbeiter2.info())
print(manager.info())
print(entwickler.info())