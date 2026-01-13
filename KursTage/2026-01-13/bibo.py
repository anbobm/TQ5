class Medium:
    """
    Basisklasse für alle Medien.

    Repräsentiert ein allgemeines Medium mit Titel und Erscheinungsjahr.
    """

    def __init__(self, titel, erscheinungsjahr):
        """
        Initialisiert ein Medium.

        :param titel: Titel des Mediums
        :param erscheinungsjahr: Jahr der Veröffentlichung
        """
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr

    def info(self):
        """
        Gibt eine textuelle Beschreibung des Mediums zurück.

        :return: String mit Titel und Erscheinungsjahr
        """
        return f"Medium: {self.titel} ({self.erscheinungsjahr})"


class Buch(Medium):
    """
    Repräsentiert ein Buch als spezielles Medium.

    Erweitert die Klasse Medium um Autor und Seitenzahl.
    """

    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        """
        Initialisiert ein Buch.

        :param titel: Titel des Buches
        :param erscheinungsjahr: Jahr der Veröffentlichung
        :param autor: Autor des Buches
        :param seitenzahl: Anzahl der Seiten
        """
        super().__init__(titel, erscheinungsjahr)
        self.autor = autor
        self.seitenzahl = seitenzahl

    def info(self):
        """
        Gibt eine detaillierte Beschreibung des Buches zurück.

        :return: String mit Buchinformationen
        """
        basisinfo = super().info()
        return f"{basisinfo}, Typ Buch, Autor: {self.autor}, Seiten: {self.seitenzahl}"


class Dvd(Medium):
    """
    Repräsentiert eine DVD als spezielles Medium.

    Erweitert die Klasse Medium um Spielzeit und Regisseur.
    """

    def __init__(self, titel, erscheinungsjahr, spielzeit, regisseur):
        """
        Initialisiert eine DVD.

        :param titel: Titel der DVD
        :param erscheinungsjahr: Jahr der Veröffentlichung
        :param spielzeit: Spielzeit in Minuten
        :param regisseur: Regisseur des Films
        """
        super().__init__(titel, erscheinungsjahr)
        self.spielzeit = spielzeit
        self.regisseur = regisseur

    def info(self):
        """
        Gibt eine detaillierte Beschreibung der DVD zurück.

        :return: String mit DVD-Informationen
        """
        basisinfo = super().info()
        return f"{basisinfo}, Typ DVD, Spielzeit: {self.spielzeit} Min, Regisseur: {self.regisseur}"


class Bibliothek:
    """
    Verwaltet eine Sammlung von Medien.

    Ermöglicht das Hinzufügen, Entfernen und Auflisten von Medien.
    """

    def __init__(self):
        """
        Initialisiert eine leere Bibliothek.
        """
        self.medien = []

    def hinzufuegen(self, medium):
        """
        Fügt ein Medium zur Bibliothek hinzu.

        :param medium: Ein Objekt vom Typ Medium oder einer Unterklasse
        """
        self.medien.append(medium)

    def entfernen(self, medium):
        """
        Entfernt ein Medium aus der Bibliothek, falls es vorhanden ist.

        :param medium: Das zu entfernende Medium
        """
        if medium in self.medien:
            self.medien.remove(medium)

    def auflisten(self):
        """
        Gibt alle Medien der Bibliothek auf der Konsole aus.
        """
        for m in self.medien:
            print(m.info())
