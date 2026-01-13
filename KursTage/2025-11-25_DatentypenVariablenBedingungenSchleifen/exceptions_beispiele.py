# Fehler bei Typumwandlung, z.b. String in Integer mit der int(...)-Funktion

eingabe = input('Gib eine Zahl ein: ')
try:
    zahl = int(eingabe)
except ValueError:
    print('Das war keine Zahl')


# Fehler beim Zugriff auf einen Schlüssel, der im Dictionary nicht existiert:

person = {
    "name": "Paul",
    "adresse": "Dorfstraße 1, 01234 Dorf"
}

try:
    alter = person["alter"]
except:
    print('Kein Alter angegeben, setze auf 30')
    alter = 30


# Fehler beim Zugriff auf Dateien, z.B.
# wenn foo.txt nicht existiert gibt es einen FileNotFoundError

try:
    datei = open("foo.txt")
except FileNotFoundError:
    print("Datei foo.txt nicht gefunden")
