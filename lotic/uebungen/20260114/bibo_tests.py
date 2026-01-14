import unittest
from bibo import Bibliothek, Medium, Dvd, Buch

# test bibo.py

class MediumTest(unittest.TestCase):
    def setUp(self):
        self.medium = Medium("Shogun", 1975)

    def test_constructor_valid(self):
        #medium = Medium("Shogun", 1975)
        self.assertEqual(self.medium.titel, "Shogun")
        self.assertEqual(self.medium.erscheinungsjahr, 1975)

    def test_info(self):
        #medium = Medium("Shogun", 1975)
        self.assertEqual(self.medium.info(), "Medium: Shogun (1975)")  

class BuchTest(unittest.TestCase):
    def setUp(self):
        self.book = Buch('Shogun', 1975, 'James Clavell', 1280)
    def test_constructor_valid(self):
        self.assertEqual(self.book.titel, "Shogun")
        self.assertEqual(self.book.erscheinungsjahr, 1975)
        self.assertEqual(self.book.autor, 'James Clavell')
        self.assertEqual(self.book.seitenzahl, 1280)
    def test_info(self):
        self.assertEqual(self.book.info(), 'Medium: Shogun (1975), Typ Buch, Autor: James Clavell, Seiten: 1280')


class DvdTest(unittest.TestCase):
    def setUp(self):
        self.dvd = Dvd('Fightclub', 1999, 139, 'David Fincher')

    def test_constructor_valid(self):
        #medium = Medium("Shogun", 1975)
        self.assertEqual(self.dvd.titel, "Fightclub")
        self.assertEqual(self.dvd.erscheinungsjahr, 1999)
        self.assertEqual(self.dvd.spielzeit, 139)
        self.assertEqual(self.dvd.regisseur, 'David Fincher')

    def test_info(self):
        self.assertEqual(self.dvd.info(), 'Medium: Fightclub (1999), Typ DVD, Spielzeit: 139 Min, Regisseur: David Fincher')


class BibliotheksTest(unittest.TestCase):
    def setUp(self):
        self.bibliothek = Bibliothek()

    def test_constructor_valid(self):
        self.assertEqual(self.bibliothek.medien, [])

    def test_hinzufuegen(self):
        test_dvd = Dvd('Fightclub', 1999, 139, 'David Fincher')
        self.bibliothek.hinzufuegen(test_dvd)
        #self.assertEqual(self.bibliothek.medien, [test_dvd])
        self.assertIn(test_dvd, self.bibliothek.medien) # schaut ob Element in Liste ist.

    def test_entfernen(self):
        test_dvd = Dvd('Fightclub', 1999, 139, 'David Fincher')
        self.bibliothek.hinzufuegen(test_dvd)
        self.bibliothek.entfernen(test_dvd)
        #self.assertEqual(self.bibliothek.medien, [])
        self.assertNotIn(test_dvd, self.bibliothek.medien) # schaut ob Element nicht in Liste ist.
    
    def test_seiten(self):
        self.bibliothek.hinzufuegen(Buch('Shogun', 1975, 'James Clavell', 1280))
        seiten = self.bibliothek.seiten()
        self.assertEqual(seiten, 1280)


if __name__ == "__main__":
    unittest.main()
