import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

DB_PATH = "lager.db"

# -----------------------------
# Datenbank-Schicht
# -----------------------------
class InventoryDB:
    def __init__(self, path: str = DB_PATH):
        self.conn = sqlite3.connect(path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._init_schema()

    def _init_schema(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                qty INTEGER NOT NULL DEFAULT 0
            );
            """
        )
        self.conn.commit()

        # Falls die Tabelle leer ist, drei Beispielprodukte anlegen
        cur = self.conn.execute("SELECT COUNT(*) FROM products;")
        (count,) = cur.fetchone()
        if count == 0:
            self.conn.executemany(
                "INSERT INTO products(name, qty) VALUES(?, ?);",
                [("Apfel", 10), ("Banane", 15), ("Karotte", 7)],
            )
            self.conn.commit()

    # CRUD
    def list_products(self):
        cur = self.conn.execute("SELECT id, name, qty FROM products ORDER BY name ASC;")
        return cur.fetchall()

    def get_product_by_name(self, name: str):
        cur = self.conn.execute("SELECT id, name, qty FROM products WHERE name = ?;", (name,))
        return cur.fetchone()

    def add_product(self, name: str, qty: int = 0):
        self.conn.execute("INSERT INTO products(name, qty) VALUES(?, ?);", (name, qty))
        self.conn.commit()

    def delete_product(self, name: str):
        self.conn.execute("DELETE FROM products WHERE name = ?;", (name,))
        self.conn.commit()

    def set_qty(self, name: str, qty: int):
        self.conn.execute("UPDATE products SET qty = ? WHERE name = ?;", (qty, name))
        self.conn.commit()

    def adjust_qty(self, name: str, delta: int):
        cur = self.conn.execute("SELECT qty FROM products WHERE name = ?;", (name,))
        row = cur.fetchone()
        if row is None:
            raise ValueError("Produkt nicht gefunden")
        new_qty = row[0] + delta
        if new_qty < 0:
            raise ValueError("Achtung: Bestand kann nicht negativ werden")
        self.conn.execute("UPDATE products SET qty = ? WHERE name = ?;", (new_qty, name))
        self.conn.commit()
        return new_qty


# -----------------------------
# GUI-Schicht (Tkinter)
# -----------------------------
class InventoryApp(ttk.Frame):
    def __init__(self, master, db: InventoryDB):
        super().__init__(master)
        self.db = db
        self.master.title("Lagerverwaltung – Mini")
        self.master.geometry("680x420")
        self.master.minsize(640, 380)

        self._build_ui()
        self._populate_products()

    def _build_ui(self):
        # Top-Bar: Produktauswahl + Bestand
        top = ttk.Frame(self)
        top.pack(fill=tk.X, padx=12, pady=12)

        ttk.Label(top, text="Produkt:").pack(side=tk.LEFT)
        self.product_var = tk.StringVar()
        self.product_box = ttk.Combobox(top, textvariable=self.product_var, state="readonly", width=24)
        self.product_box.pack(side=tk.LEFT, padx=(6, 12))
        self.product_box.bind("<<ComboboxSelected>>", self._on_select_product)

        self.qty_var = tk.StringVar(value="Bestand: –")
        self.qty_label = ttk.Label(top, textvariable=self.qty_var, font=("", 10, "bold"))
        self.qty_label.pack(side=tk.LEFT)

        ttk.Button(top, text="Aktualisieren", command=self._refresh_view).pack(side=tk.RIGHT)

        # Mittelbereich: Anpassung
        mid = ttk.LabelFrame(self, text="Bestand anpassen")
        mid.pack(fill=tk.X, padx=12, pady=(0, 12))

        ttk.Label(mid, text="Menge:").grid(row=0, column=0, padx=8, pady=8, sticky=tk.W)
        self.amount_var = tk.StringVar(value="1")
        self.amount_entry = ttk.Entry(mid, textvariable=self.amount_var, width=10)
        self.amount_entry.grid(row=0, column=1, padx=8, pady=8, sticky=tk.W)

        ttk.Button(mid, text="+ Hinzufügen", command=lambda: self._change_stock(+1)).grid(row=0, column=2, padx=8, pady=8)
        ttk.Button(mid, text="- Entnehmen", command=lambda: self._change_stock(-1)).grid(row=0, column=3, padx=8, pady=8)

        # Rechts: Produktaktionen
        ttk.Button(mid, text="Neues Produkt…", command=self._add_product_dialog).grid(row=0, column=4, padx=8, pady=8)
        ttk.Button(mid, text="Produkt löschen", command=self._delete_selected_product).grid(row=0, column=5, padx=8, pady=8)

        # Tabelle: gesamte Übersicht
        table_frame = ttk.LabelFrame(self, text="Gesamter Bestand")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        self.tree = ttk.Treeview(table_frame, columns=("name", "qty"), show="headings")
        self.tree.heading("name", text="Produkt")
        self.tree.heading("qty", text="Menge")
        self.tree.column("name", width=240, anchor=tk.W)
        self.tree.column("qty", width=80, anchor=tk.E)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Statusleiste
        self.status_var = tk.StringVar(value="Bereit.")
        status = ttk.Label(self, textvariable=self.status_var, anchor=tk.W)
        status.pack(fill=tk.X, padx=12, pady=(0, 8))

        # Style-Feinschliff
        self.pack(fill=tk.BOTH, expand=True)
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

    def _populate_products(self):
        products = self.db.list_products()
        names = [p[1] for p in products]
        self.product_box["values"] = names
        if names and not self.product_var.get():
            self.product_box.current(0)
        self._refresh_view()

    def _on_select_product(self, event=None):
        self._update_current_qty()

    def _current_product_name(self):
        name = self.product_var.get()
        if not name:
            messagebox.showinfo("Hinweis", "Bitte zuerst ein Produkt auswählen.")
        return name

    def _parse_amount(self):
        try:
            val = int(self.amount_var.get())
            if val <= 0:
                raise ValueError
            return val
        except Exception:
            messagebox.showerror("Fehler", "Bitte eine positive ganze Zahl eingeben.")
            return None

    def _change_stock(self, sign: int):
        name = self._current_product_name()
        if not name:
            return
        amount = self._parse_amount()
        if amount is None:
            return
        try:
            new_qty = self.db.adjust_qty(name, sign * amount)
            self.status_var.set(f"Bestand von '{name}' auf {new_qty} aktualisiert.")
            self._refresh_view()
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def _add_product_dialog(self):
        name = simpledialog.askstring("Neues Produkt", "Name des Produkts:")
        if not name:
            return
        try:
            initial_qty_str = simpledialog.askstring("Neues Produkt", "Startmenge (ganzzahlig, optional):", initialvalue="0")
            initial_qty = int(initial_qty_str) if initial_qty_str else 0
            if initial_qty < 0:
                raise ValueError
            self.db.add_product(name.strip(), initial_qty)
            self.status_var.set(f"Produkt '{name}' angelegt.")
            self._populate_products()
            # Direkt auswählen
            self.product_var.set(name.strip())
            self._update_current_qty()
        except sqlite3.IntegrityError:
            messagebox.showerror("Fehler", "Produktname bereits vorhanden.")
        except ValueError:
            messagebox.showerror("Fehler", "Ungültige Startmenge.")

    def _delete_selected_product(self):
        name = self._current_product_name()
        if not name:
            return
        if messagebox.askyesno("Löschen bestätigen", f"Soll '{name}' wirklich gelöscht werden?"):
            self.db.delete_product(name)
            self.status_var.set(f"Produkt '{name}' gelöscht.")
            self.product_var.set("")
            self._populate_products()

    def _update_current_qty(self):
        name = self.product_var.get()
        if not name:
            self.qty_var.set("Bestand: –")
            return
        row = self.db.get_product_by_name(name)
        if row:
            self.qty_var.set(f"Bestand: {row[2]}")
        else:
            self.qty_var.set("Bestand: –")

    def _refresh_view(self):
        # Tabelle neu befüllen
        for item in self.tree.get_children():
            self.tree.delete(item)
        for _id, name, qty in self.db.list_products():
            self.tree.insert("", tk.END, values=(name, qty))
        self._update_current_qty()


def main():
    db = InventoryDB(DB_PATH)
    root = tk.Tk()
    app = InventoryApp(root, db)
    root.mainloop()


if __name__ == "__main__":
    main()
