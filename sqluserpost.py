import sqlite3
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
    @classmethod
    def from_row(cls, r): return cls(r["id"], r["name"])
@dataclass
class Post:
    id: int
    user_id: int
    title: str
    @classmethod
    def from_row(cls, r): return cls(r["id"], r["user_id"], r["title"])
class DB:
    def __init__(self, name="posts.db"):
        self.name = name
        with self.conn() as c:
            c.executescript("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INT NOT NULL,
                title TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE);
            """)

    def conn(self):
        c = sqlite3.connect(self.name)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA foreign_keys=ON")
        return c

    def add_user(self, name):
        with self.conn() as c:
            cur = c.execute("INSERT INTO users(name) VALUES(?)", (name,))
            return User(cur.lastrowid, name)

    def all_users(self):
        with self.conn() as c:
            return [User.from_row(r) for r in c.execute("SELECT * FROM users")]

    def add_post(self, uid, title):
        with self.conn() as c:
            cur = c.execute("INSERT INTO posts(user_id,title) VALUES(?,?)",
                            (uid, title))
            return Post(cur.lastrowid, uid, title)

    def posts_by_user(self, uid):
        with self.conn() as c:
            return [Post.from_row(r) for r in
                    c.execute("SELECT * FROM posts WHERE user_id=?", (uid,))]

    def all_posts_join(self):
        with self.conn() as c:
            q = """SELECT p.id post_id, p.title, u.id user_id, u.name 
                   FROM posts p JOIN users u ON p.user_id=u.id"""
            return [dict(r) for r in c.execute(q)]

    def delete_user(self, uid):
        with self.conn() as c:
            return c.execute("DELETE FROM users WHERE id=?", (uid,)).rowcount
def menu():
    print("""
1 User anlegen
2 Post anlegen
3 alle User anzeigen
4 Posts eines Users
5 alle Posts anzeigen
6 User löschen
0 Ende
""")

def main():
    db = DB()
    while True:
        menu()
        ch = input("Auswahl: ")
        if ch == "1":
            print(db.add_user(input("Name: ")))
        elif ch == "2":
            print(db.add_post(int(input("User-ID: ")), input("Titel: ")))
        elif ch == "3":
            for u in db.all_users(): print(u)
        elif ch == "4":
            for p in db.posts_by_user(int(input("User-ID: "))): print(p)
        elif ch == "5":
            for p in db.all_posts_join(): print(p)
        elif ch == "6":
            print("Gelöscht:", db.delete_user(int(input("User-ID: "))))
        elif ch == "0":
            break

if __name__ == "__main__":
    main()