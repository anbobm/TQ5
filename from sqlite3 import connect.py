from sqlite3 import connect

# Verbindung zur Datenbank
connection = connect("database.db")

# Cursor anlegen (braucht man um SQL befehle auszuführen)
cur = connection.cursor()

# Nutzer nach Daten zu "Student" fragen
vorname = input("Vorname: ")
nachname = input("Nachname: ")
email = input("Email: ")

# Datensatz hinzufügen
cur.execute("insert into students values (?, ?, ?)", (vorname, nachname, email))
# ein insert startet automatisch eine Transaktion (in default-Einstellungen)
# danach muss also ein commit folgen
connection.commit()

# Datensatz abfragen
vorname = input("Nach welchem Vornamen suchen? ")
# nach select ist kein commit nötig. man beachte dass parameter als Tupel
# übergeben werden, auch wenn es nur einer ist
cur.execute("select vorname, email from students where vorname = ?", (vorname,))

# Alle Datensätze des Resultats holen
studenten = cur.fetchall()

# erhaltene Datensätze durchlaufen
for student in studenten:
    vorname, email = student

    print(f"Vorname:  {vorname}, Email: {email}")