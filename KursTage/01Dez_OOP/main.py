from buch import Buch
from dvd import Dvd
from bibliothek import Bibliothek

# Bibliothek erstellen
bibo = Bibliothek()

# Medien erstellen
buch1 = Buch("Harry Potter", 1997, "J.K. Rowling", 336)
dvd1 = Dvd("Inception", 2010, 148, "Christopher Nolan")

# Zur Bibliothek hinzufuegen
bibo.hinzufuegen(buch1)
bibo.hinzufuegen(dvd1)

# Auflisten
bibo.auflisten()
