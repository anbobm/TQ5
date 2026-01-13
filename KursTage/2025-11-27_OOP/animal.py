class Animal:
    def __init__(self, name, pate):
        self._name = name
        self._pate = pate

    def geräusch(self):
        print("[irgendein Geräusch]")
    
    def __str__(self):
        return f"Tier mit Namen {self._name} und dem Paten {self._pate}"
    
class Dog(Animal):
    def __init__(self, name, pate, rasse):
        super().__init__(name, pate)
        self._rasse = rasse

    def geräusch(self):
        print("Wau wau!")

    def hol_stöckchen(self):
        print(f"{self._name} holt das Stöckchen")

class Cat(Animal):
    def __init__(self, name, pate, leben=7):
        super().__init__(name, pate)
        self._leben = leben
    
    def geräusch(self):
        print("Miau!")
    
    def übergeben(self):
        print(f"{self._name} würgt ein Fellknäuel hoch. Super!")

dog = Dog("Hasso", "Sönke", "Schäferhund")
cat = Cat("Garfield", "Nico")

print(dog)
dog.geräusch()
dog.hol_stöckchen()
print(cat)
cat.geräusch()
cat.übergeben()