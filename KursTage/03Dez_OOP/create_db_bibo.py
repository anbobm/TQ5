from sqlite3 import connect

connection = connect("bibo.db")
cur = connection.cursor()

cur.execute("""
            create table if not exists bücher(
                titel TEXT,
                erscheinungsjahr INTEGER,
                autor TEXT,
                seitenzahl INTEGER
            )
            """)

bücher = [
    ("Das Boot",1973,"Lothar-Günther Buchheim",603),
    ("Harry Potter and the Philosopher's Stone",1997,"J.K. Rowling",223)
]

cur.executemany("""
            insert into bücher
            values(?, ?, ?, ?)
            """, bücher)
connection.commit()