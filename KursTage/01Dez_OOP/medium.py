class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr

    def info(self):
        return f"Titel: {self.titel}, Jahr: {self.erscheinungsjahr}"
