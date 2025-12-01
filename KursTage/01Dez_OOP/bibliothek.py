class Bibliothek:
    def __init__(self):
        self.medien = []

    def hinzufuegen(self, medium):
        self.medien.append(medium)

    def entfernen(self, medium):
        if medium in self.medien:
            self.medien.remove(medium)

    def auflisten(self):
        for medium in self.medien:
            print(medium.info())
