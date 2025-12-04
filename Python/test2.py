from math import pi, sqrt


class Form:
    def flaeche(self):
        raise NotImplementedError

    def umfang(self):
        raise NotImplementedError


class Rechteck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe

    def flaeche(self):
        return self._breite * self._hoehe

    def umfang(self):
        return self._breite + self._hoehe

    def __str__(self):
        return f"Rechteck {self._breite} x {self._hoehe}, Umfang: {self.umfang()}, Fläche: {self.flaeche()}"


class Kreis(Form):
    def __init__(self, radius):
        self._radius = radius

    def flaeche(self):
        return pi * self._radius ** 2

    def umfang(self):
        return 2 * pi * self._radius

    def __str__(self):
        return f"Kreis mit Radius {self._radius}, Umfang: {self.umfang()}, Fläche: {self.flaeche()}"


class Quadrat(Rechteck):
    def __init__(self, breite):
        super().__init__(breite, breite)

    def __str__(self):
        return f"Quadrat mit Kantenlänge {self._breite}, Umfang: {self.umfang()}, Fläche: {self.flaeche()}"


class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe

    def flaeche(self):
        return self._breite * self._hoehe / 2

    def umfang(self):
        return self._breite + self._hoehe + sqrt(self._breite ** 2 + self._hoehe ** 2)

    def __str__(self):
        return f"Dreieck, Umfang: {self.umfang()}, Fläche: {self.flaeche()}"


rechteck = Rechteck(3, 4)
print(rechteck)

kreis = Kreis(10)
print(kreis)

quadrat = Quadrat(5)
print(quadrat)

dreieck = RechtwinkligesDreieck(3, 4)
print(dreieck)


def flaechen(formen: list[Form]):
    for form in formen:
        print(form.flaeche())


flaechen([rechteck, kreis, quadrat, dreieck])

## Das wirft Fehler weil in der Basisklasse nicht implementiert
# form = Form()
# form.flaeche()
