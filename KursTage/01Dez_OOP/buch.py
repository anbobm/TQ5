from medium import Medium


class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self.autor = autor
        self.seitenzahl = seitenzahl

    def info(self):
        return (
            f"Buch - {self.titel} ({self.erscheinungsjahr}), "
            f"Autor: {self.autor}, Seiten: {self.seitenzahl}"
        )
