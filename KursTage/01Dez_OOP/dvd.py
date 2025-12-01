from medium import Medium


class Dvd(Medium):
    def __init__(self, titel, erscheinungsjahr, spieldauer, regisseur):
        super().__init__(titel, erscheinungsjahr)
        self.spieldauer = spieldauer
        self.regisseur = regisseur

    def info(self):
        return (
            f"DVD - {self.titel} ({self.erscheinungsjahr}), "
            f"Spieldauer: {self.spieldauer} min, "
            f"Regisseur: {self.regisseur}"
        )
