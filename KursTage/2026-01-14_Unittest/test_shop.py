from unittest import TestCase
from shop import Produkt, Lebensmittel, Elektronik, Kleidung, Warenkorb

class TestProdukte(TestCase):

    def test_produkt_info(self):
        p = Produkt("Buch", 12.99)
        self.assertEqual(p.info(), "Produkt Buch für 12.99 €")

    def test_lebensmittel_info(self):
        l = Lebensmittel("Apfel", 0.5, "01.01.2026")
        self.assertEqual(
            l.info(),
            "Produkt Apfel für 0.5 €, Lebensmittel haltbar bis 01.01.2026"
        )

    def test_elektronik_info(self):
        e = Elektronik("Laptop", 999.99, 2)
        self.assertEqual(
            e.info(),
            "Produkt Laptop für 999.99 €, Elektronik mit Garantie von 2 Jahren"
        )

    def test_kleidung_info(self):
        k = Kleidung("T-Shirt", 19.99, "M", "Blau")
        self.assertEqual(
            k.info(),
            "Produkt T-Shirt für 19.99 €, Kleidung der Größe M mit Farbe Blau"
        )


class TestWarenkorb(TestCase):

    def setUp(self):
        self.warenkorb = Warenkorb()
        self.p1 = Produkt("Buch", 10)
        self.p2 = Lebensmittel("Milch", 2, "01.01.2026")

    def test_hinzufuegen(self):
        self.warenkorb.hinzufuegen(self.p1)
        self.assertIn(self.p1, self.warenkorb.produkte)

    def test_gesamtpreis(self):
        self.warenkorb.hinzufuegen(self.p1)
        self.warenkorb.hinzufuegen(self.p2)
        self.assertEqual(self.warenkorb.gesamtpreis(), 12)

    def test_auflisten(self):
        self.warenkorb.hinzufuegen(self.p1)
        self.warenkorb.hinzufuegen(self.p2)

        erwartete_ausgabe = (
            "Produkt Buch für 10 €\n"
            "Produkt Milch für 2 €, Lebensmittel haltbar bis 01.01.2026\n"
        )
        self.assertEqual(self.warenkorb.auflisten(), erwartete_ausgabe)