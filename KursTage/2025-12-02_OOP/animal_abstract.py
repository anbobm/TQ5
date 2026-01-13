from abc import ABC, abstractmethod

# Klasse Animal soll abstrakt sein, muss daher von ABC (Abstract Base Class) erben
class Animal(ABC):
    # der @abstractmethod decorator macht klar, dass diese Methode abstrakt ist und
    # in einer abgeleiteten Klasse überschrieben werden muss
    @abstractmethod
    def geraeusch():
        pass

class Dog(Animal):
    # hier wird die abstrakte Methode geraeusch() überschrieben
    def geraeusch():
        return "woof!"

# das geht nicht, weil Animal abstrakt ist, ein Objekt kann also nicht davon erzeugt werden
animal = Animal()

# das geht, weil Dog die abstrakten Methoden von Animal überschrieben hat
dog = Dog()
