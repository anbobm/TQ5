import random   # Für Zufallsereignisse wie kritische Treffer oder Heiltrank-Drops

# ---------------------------------------------------------
# KLASSENDEFINITION: HELD
# ---------------------------------------------------------
class Held:
    def __init__(self, name, leben, angriff):
        # Grundattribute des Helden
        self.name = name
        self.leben = leben
        self.angriff = angriff

    def angreifen(self, monster):
        # Held fügt dem Monster Schaden in Höhe seiner Angriffskraft zu
        schaden = self.angriff
        monster.leben -= schaden
        print(f"{self.name} greift {monster.name} an und verursacht {schaden} Schaden!")

    def ist_besiegt(self):
        # Held gilt als besiegt, wenn seine Lebenspunkte 0 oder weniger sind
        return self.leben <= 0


# ---------------------------------------------------------
# KLASSENDEFINITION: MONSTER
# ---------------------------------------------------------
class Monster:
    def __init__(self, name, leben, angriff):
        # Grundattribute des Monsters
        self.name = name
        self.leben = leben
        self.angriff = angriff

    def angreifen(self, held):
        # Monster entscheidet zufällig, ob es kritisch angreift
        # random.random() gibt eine Zahl zwischen 0 und 1 zurück
        if random.random() < 0.2:  # 20 % Chance für kritischen Treffer
            schaden = self.angriff * 2
            print(f" Kritischer Treffer von {self.name}!")
        else:
            schaden = self.angriff

        # Schaden wird vom Heldenleben abgezogen
        held.leben -= schaden
        print(f"{self.name} greift {held.name} an und verursacht {schaden} Schaden!")

    def ist_besiegt(self):
        # Monster gilt als besiegt, wenn seine Lebenspunkte 0 oder weniger sind
        return self.leben <= 0

    def drop_heiltrank(self):
        # Monster hat eine 30%ige Chance, einen Heiltrank fallen zu lassen
        return random.random() < 0.3


# ---------------------------------------------------------
# SPIELINITIALISIERUNG
# ---------------------------------------------------------

# Erzeuge Held
held = Held("Arthos", 50, 12)

# Erzeuge Liste von Monstern
monster_liste = [
    Monster("Goblin", 30, 5),
    Monster("Ork", 40, 8),
    Monster("Skelett", 25, 6)
]

heiltraenke = 0   # Anzahl verfügbarer Heiltränke

print("Das Abenteuer beginnt!")
print(f"Held {held.name} hat {held.leben} Leben und {held.angriff} Angriff.\n")

# ---------------------------------------------------------
# HAUPTSCHLEIFE DES SPIELS
# ---------------------------------------------------------
# Die Schleife läuft, solange der Held lebt UND noch mindestens ein Monster lebt
while not held.ist_besiegt() and any(not m.ist_besiegt() for m in monster_liste):

    # Liste der noch lebenden Monster anzeigen
    print("\nMonster in der Nähe:")
    for i, m in enumerate(monster_liste):
        if not m.ist_besiegt():
            print(f"{i+1}. {m.name} (Leben: {m.leben})")

    # Spieler wählt ein Monster aus
    wahl = int(input("Wähle ein Monster aus (Nummer eingeben): ")) - 1
    monster = monster_liste[wahl]

    print("\n--- Runde ---")

    # Held greift das gewählte Monster an
    held.angreifen(monster)

    # Prüfen, ob das Monster nach dem Angriff besiegt ist
    if monster.ist_besiegt():
        print(f"{monster.name} wurde besiegt!")

        # Prüfen, ob das Monster einen Heiltrank fallen lässt
        if monster.drop_heiltrank():
            heiltraenke += 1
            print(f"{monster.name} hat einen Heiltrank fallen lassen! (Heiltränke: {heiltraenke})")

        # Zur nächsten Kampfrunde springen
        continue

    # Monster greift zurück, wenn es noch lebt
    monster.angreifen(held)

    # Held kann Heiltrank nutzen, wenn wenig Leben übrig ist
    if held.leben < 20 and heiltraenke > 0:
        nutze = input("Möchtest du einen Heiltrank benutzen? (j/n): ")
        if nutze.lower() == "j":
            heiltraenke -= 1
            heilung = random.randint(10, 25)  # Zufällige Heilmenge
            held.leben += heilung
            print(f"{held.name} benutzt einen Heiltrank und heilt {heilung} Leben! (Aktuell: {held.leben})")

    print(f"{held.name}: {held.leben} Leben")

# ---------------------------------------------------------
# SPIELENDE
# ---------------------------------------------------------

print("\n============================")

if held.ist_besiegt():
    print("Der Held wurde besiegt... ")
else:
    print("Alle Monster wurden besiegt!  Sieg!")

print("============================")

