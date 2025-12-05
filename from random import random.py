from random import random

class Figur:
    def __init__(self, name, leben, angriff):
        self.name = name
        self.leben = leben
        self.angriff = angriff

    def ist_besiegt(self):
        return self.leben <= 0

class Held(Figur):
    def angreifen(self, monster):
        print(f"{self.name} greift {monster.name} an")
        monster.leben = monster.leben - self.angriff
        print(f"{monster.name} hat jetzt {monster.leben} Leben.\n")

class Monster(Figur):
    def angreifen(self, held):
        print(f"{self.name} greift {held.name} an!")
        held.leben = held.leben - self.angriff
        print(f"{held.name} hat jetzt {held.leben} Leben.\n")

held = Held("Arin", 60, 12)

monsterliste = [
    Monster("Goblin", 20, 5),
    Monster("Ork", 35, 8),
    Monster("Drachenjunges", 50, 12)
]

while monsterliste and not held.ist_besiegt():
    print("Monster in der Arena:")
    for i, m in enumerate(monsterliste):
        print(f"{i+1}. {m.name} (Leben: {m.leben})")

    wahl = int(input("Welches Monster soll angegriffen werden? ")) - 1
    ziel = monsterliste[wahl]

    held.angreifen(ziel)

    if ziel.ist_besiegt():
        print(f"{ziel.name} wurde besiegt!\n")

        if random() < 0.2:
            print("Das Monster lässt einen Heiltrank fallen, den du dir einverleibst. Deine Lebenspunkte steigen um 10")
            held.leben = held.leben + 10

        monsterliste.pop(wahl)
        continue

    ziel.angreifen(held)

if held.ist_besiegt():
    print("Der Held wurde besiegt! Spiel vorbei!")
else:
    print("Alle Monster wurden besiegt! Du hast gewonnen!")
 