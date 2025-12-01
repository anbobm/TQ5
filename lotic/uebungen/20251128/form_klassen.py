import math

class Form:
    def __init__(self, typ):
        self._typ = typ        
    def flaeche(self):
        raise NotImplementedError 
    def umfang(self):
        raise NotImplementedError
    def get_typ(self):
        return self._typ

class Quadrat(Form):
    def __init__(self, typ, seitenlaenge):
        super().__init__(typ)
        self._seitenlaenge = seitenlaenge
    def flaeche(self):
        return self._seitenlaenge * self._seitenlaenge
    def umfang(self):
        return self._seitenlaenge * 4

class Rechteck(Form):
    def __init__(self, typ, a_laenge, b_laenge):
        super().__init__(typ)
        self._a_laenge = a_laenge
        self._b_laenge = b_laenge
    def flaeche(self):
        return self._a_laenge * self._b_laenge
    def umfang(self):
        return (self._a_laenge * 2) + (self._b_laenge * 2)

class Kreis(Form):
    def __init__(self, typ, radius):
        super().__init__(typ)
        self._radius = radius
    def flaeche(self):
        return self._radius * self._radius * math.pi
    def umfang(self):
        return 2 * math.pi * self._radius

class Dreieck(Form):
    def __init__(self, typ, a, b, c):
        super().__init__(typ)
        self._a = a
        self._b = b
        self._c = c
    def flaeche(self):
        halberUmfang = (self._a + self._b + self._c) / 2
        return math.sqrt(halberUmfang * (halberUmfang - self._a) * (halberUmfang - self._b) * (halberUmfang - self._c))
    def umfang(self):
        return self._a + self._b + self._c

dreieck = Dreieck('Dreieck', 4, 13, 15)
print(dreieck.flaeche())
print(dreieck.umfang())

quadrat = Quadrat('Quadrat', 5)
print(quadrat.flaeche())
print(quadrat.umfang())

rechteck = Rechteck('Rechteck', 5, 2)
print(rechteck.flaeche())
print(rechteck.umfang())

kreis = Kreis('Kreis', 10)
print(kreis.flaeche())
print(kreis.umfang())
