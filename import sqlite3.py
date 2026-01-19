import sqlite3

class User:
    def __init__(self, user_id=None, name=None):
        pass

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


class Post:
    def __init__(self, post_id=None, user_id=None, title=None):
        pass

    def __repr__(self):
        return f"Post(id={self.id}, user_id={self.user_id}, title='{self.title}')"


class Database:
    # legt Verbindung zur DB an und sorgt dann für das anlegen der Tabellen
    def __init__(self, db_name="posts.db"):
        pass

    # Hilfsmethode, welche die Tabellen erzeugt (IF NOT EXISTS)
    def create_tables(self):
        pass
    
    # Fügt einen Nutzer zur DB hinzu
    def add_user(self, user: User):
        pass

    # Holt einen Nutzer aus der DB anhand seiner id
    def get_user(self, user_id):
        pass

    # Fügt der DB einen Post hinzu
    def add_post(self, post: Post):
        pass

    # Holt alle Posts die zu einer bestimmten user_id gehören aus der DB
    def get_posts_for_user(self, user_id):
        pass



db = Database()

# Nutzer anlegen
bernd = db.add_user(User(name="Bernd"))

# zwei Posts für diesen Nutzer anlegen
db.add_post(Post(user_id=bernd.id, title="Hallo Welt"))
db.add_post(Post(user_id=bernd.id, title="Mein zweiter Post"))

# Posts anzeigen
print("User:", bernd)
posts = db.get_posts_for_user(bernd.id)
print("Posts:", posts)
 