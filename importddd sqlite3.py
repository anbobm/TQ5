import sqlite3

class User:
    def __init__(self, user_id=None, name=None):
        self._user_id = user_id
        self._name = name

    def __repr__(self):
        return f"User(id={self._user_id}, name='{self._name}')"
    def get_name(self):
        return self._name
    def set_id(self, id):
        self._user_id = id
    def get_id(self):
        return self._user_id

class Post:
    def __init__(self, post_id=None, user_id=None, title=None):
        self._post_id = post_id
        self._user_id = user_id
        self._title = title

    def __repr__(self):
        return f"Post(id={self._post_id}, user_id={self._user_id}, title='{self._title}')"
    def get_title(self):
        return self._title
    def get_user_id(self):
        return self._user_id
    def get_id(self):
        return self._post_id
    def set_id(self, id):
        self._post_id = id 


class Database:
    # legt Verbindung zur DB an und sorgt dann für das anlegen der Tabellen
    def __init__(self, db_name="posts.db"):
        self._db_name = db_name
        self.create_tables()

    # Hilfsmethode, welche die Tabellen erzeugt (IF NOT EXISTS)
    def create_tables(self):
        try:
            connection = sqlite3.connect(self._db_name)
            cur = connection.cursor()
            query = 'create table if not exists user(rowid integer primary key, name varchar(255))'
            cur.execute(query)
            query = 'create table if not exists post(rowid integer primary key, user_id integer, title varchar(255))'
            cur.execute(query)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    # Fügt einen Nutzer zur DB hinzu
    def add_user(self, user: User):
        #try:
            connection = sqlite3.connect(self._db_name)
            cur = connection.cursor()
            insert_values = [user.get_name()]
            print(insert_values)
            query = 'insert into user (name) values (?) returning rowid'
            res = cur.execute(query, insert_values)
            id_tuple = res.fetchone()
            user.set_id(id_tuple[0])
            connection.commit()
            connection.close()
            return True
        #except:
            return False
    # Holt einen Nutzer aus der DB anhand seiner id
    def get_user(self, user_id):
        pass

    # Fügt der DB einen Post hinzu
    def add_post(self, post: Post):
        try:
            connection = sqlite3.connect(self._db_name)
            cur = connection.cursor()
            insert_values = [post.get_user_id(), post.get_title()]
            print(insert_values)
            query = 'insert into post(user_id, title) values (?, ?) returning rowid'
            res = cur.execute(query, insert_values)
            id_tuple = res.fetchone()
            post.set_id(id_tuple[0])
            print(f'PostID: {post.get_id()}')
            connection.commit()
            connection.close()
            return True
        except:
            return False

    # Holt alle Posts die zu einer bestimmten user_id gehören aus der DB
    def get_posts_for_user(self, user_id):
        try:
            connection = sqlite3.connect(self._db_name)
            cur = connection.cursor()
            select_values = [user_id]
            query = 'select * from post where user_id = ?'
            res = cur.execute(query, select_values)
            post_tuples = res.fetchall()
            print('ptuple')
            print(post_tuples)
            connection.close()
            post_list = []
            for post_tuple in post_tuples:
                post = Post(post_tuple[0], post_tuple[1], post_tuple[2])
                post_list.append(post)
            return post_list
        except:
            print('Fehler')
            return False

db = Database()

# Nutzer anlegen
bernd = User(name="Bernd")
db.add_user(bernd)

# zwei Posts für diesen Nutzer anlegen
db.add_post(Post(None, bernd.get_id(), title="Hallo Welt"))
db.add_post(Post(None, bernd.get_id(), title="Mein zweiter Post"))

# Posts anzeigen
print("User:", bernd)
posts = db.get_posts_for_user(bernd.get_id())
print("Posts:", posts)
 