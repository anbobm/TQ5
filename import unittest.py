import unittest
from shop import Produkt, Lebensmittel, Elektronik, Kleidung, Warenkorb

class ProduktTest(unittest.TestCase):
    def setUp(self):
        self.produkt = Produkt('Honig', 4.99)

    def test_constructor(self):
        self.assertEqual(self.produkt.name, 'Honig')
        self.assertEqual(self.produkt.preis, 4.99)

    def test_info(self):
        self.assertEqual(self.produkt.info(), 'Produkt Honig für 4.99 €')

class LebensmittelTest(unittest.TestCase):
    def setUp(self):
        self.lebensmittel = Lebensmittel('Honig', 4.99, '7026-05-10')

    def test_constructor(self):
        self.assertEqual(self.lebensmittel.name, 'Honig')
        self.assertEqual(self.lebensmittel.preis, 4.99)
        self.assertEqual(self.lebensmittel.haltbarkeit, '7026-05-10')

    def test_info(self):
        self.assertEqual(self.lebensmittel.info(), 'Produkt Honig für 4.99 €, Lebensmittel haltbar bis 7026-05-10')

class ElektronikTest(unittest.TestCase):
    def setUp(self):
        self.elektronik = Elektronik('Headset', 49.99, 2)

    def test_constructor(self):
        self.assertEqual(self.elektronik.name, 'Headset')
        self.assertEqual(self.elektronik.preis, 49.99)
        self.assertEqual(self.elektronik.garantie_dauer, 2)

    def test_info(self):
        self.assertEqual(self.elektronik.info(), 'Produkt Headset für 49.99 €, Elektronik mit Garantie von 2 Jahren')


class KleidungTest(unittest.TestCase):
    def setUp(self):
        self.kleidung = Kleidung('T-Shirt', 15.99, 'S', 'Orange')

    def test_constructor(self):
        self.assertEqual(self.kleidung.name, 'T-Shirt')
        self.assertEqual(self.kleidung.preis, 15.99)
        self.assertEqual(self.kleidung.groesse, 'S')
        self.assertEqual(self.kleidung.farbe, 'Orange')

    def test_info(self):
        self.assertEqual(self.kleidung.info(), 'Produkt T-Shirt für 15.99 €, Kleidung der Größe S mit Farbe Orange')

class WarenkorbTest(unittest.TestCase):
    def setUp(self):
        self.lebensmittel = Lebensmittel('Honig', 4.99, '7026-05-10')
        self.elektronik = Elektronik('Headset', 49.99, 2)
        self.kleidung = Kleidung('T-Shirt', 15.99, 'S', 'Orange')
        self.warenkorb = Warenkorb([self.lebensmittel, self.elektronik])

    def test_constructor(self):
        self.assertEqual(self.warenkorb.produkte, [self.lebensmittel, self.elektronik])

    def test_hinzufuegen(self):
        self.warenkorb.hinzufuegen(self.kleidung)
        self.assertIn(self.kleidung, self.warenkorb.produkte)

    def test_auflisten(self):
        self.assertEqual(self.warenkorb.auflisten(), 'Produkt Honig für 4.99 €, Lebensmittel haltbar bis 7026-05-10\nProdukt Headset für 49.99 €, Elektronik mit Garantie von 2 Jahren\n')

    def test_gesamtpreis(self):
        self.assertAlmostEqual(self.warenkorb.gesamtpreis(), 4.99 + 49.99)


if __name__ == "__main__":
    unittest.main()

 