import sqlite3

class User:
    def __init__(self, user_id=None, name=None):
        self.id = user_id
        self.name = name

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


class Post:
    def __init__(self, post_id=None, user_id=None, title=None):
        self.id = post_id
        self.user_id = user_id
        self.title = title

    def __repr__(self):
        return f"Post(id={self.id}, user_id={self.user_id}, title='{self.title}')"


class Database:
    # legt Verbindung zur DB an und sorgt dann für das anlegen der Tabellen
    def __init__(self, db_name="posts2.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    # Hilfsmethode, welche die Tabellen erzeugt (IF NOT EXISTS)
    def create_tables(self):
        cur = self.connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
            )
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES Users(id))
            """)
        
    
    # Fügt einen Nutzer zur DB hinzu
    def add_user(self, user: User):
        cur = self.connection.cursor()

        cur.execute("INSERT INTO Users(name) VALUES (?)", (user.name,))
        self.connection.commit()
        user.id = cur.lastrowid
        return user

    # Holt einen Nutzer aus der DB anhand seiner id
    def get_user(self, user_id):
        cur = self.connection.cursor()

        cur.execute("SELECT id, name FROM Users WHERE id = ?", (user_id,))

        # hier könnte man noch Abfangen, dass es die id gar nicht gibt,
        # dann würde fetchone() None zurückgeben
        id, name = cur.fetchone()
        return User(id, name)

    # Fügt der DB einen Post hinzu
    def add_post(self, post: Post):
        cur = self.connection.cursor()

        cur.execute("INSERT into Posts(user_id, title) VALUES (?, ?)", (post.user_id, post.title))
        self.connection.commit()

        post.id = cur.lastrowid
        return post

    # Holt alle Posts die zu einer bestimmten user_id gehören aus der DB
    def get_posts_for_user(self, user_id):
        cur = self.connection.cursor()

        cur.execute("SELECT id, user_id, title FROM Posts WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()

        posts = []
        for row in rows:
            id, user_id, title = row
            posts.append(Post(id, user_id, title))
        return posts


db = Database()

# Nutzer anlegen
bernd = db.add_user(User(name="Bernd"))

# zwei Posts für diessen Nutzer anlegen
db.add_post(Post(user_id=bernd.id, title="Hallo Welt"))
db.add_post(Post(user_id=bernd.id, title="Mein zweiter Post"))

# Posts anzeigen
print("User:", bernd)
posts = db.get_posts_for_user(bernd.id)
print("Posts:", posts)
