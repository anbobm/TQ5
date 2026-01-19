Klasse DBController

Beschreibung:
Benutzt das sqlite3 Modul um mit den Datenbanken zu kommunizieren.

Args:
db_name: str
Pfad zur Datenbank. Default: databases/extra.db

Methoden

def payment_method_export(self) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tuplen aller Einträge der payment_method Tabelle zurück.

def category_export(self) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tuplen aller Einträge der category Tabelle zurück.

def expense_export(self) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tuplen aller Einträge der expense Tabelle zurück.

def db_export(self) -> dict{str, list[tuple]}:
Beschreibung:
Gibt ein Dict mit dem Datenbankpfad und Listen von Tuplen aller Einträge in der DB zurück.

def category_expense(self, options: dict) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tuplen zurück. Jeder Tuple besteht aus dem Kategorienamen und der Summe aller Ausgaben in der Kategorie.
Args: options: dict
{year: '2025'}

def profile_details(self) -> dict:
Beschreibung:
Gibt ein Dict mit Informationen über die Datenbank zurück.
Diese Informationen beinhalten: Datenbankpfad, Ältester Eintrag, Neuster Eintrag,
Anzahl der Einträge in der expense Tabelle, Summe aller Ausgaben, Durchschnittliche Ausgabe.

def yearly_expense(self, order: dict[str, bool]) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tupeln mit der Gesammtsumme aller Ausgaben pro Jahr zurück.

def monthly_expense(self, options: dict[str, dict]) -> list[tuple]:
Beschreibung:
Gibt eine Liste von Tuplen mit der Gesamtsumme aller Ausgaben jeden Monats für ein bestimmtes Jahr zurück.

def switch_db(self, path: str) -> str:
Beschreibung:
Ändert die ausgewählte Datenbank

def create_new(self, path: str) -> bool:
Beschreibung:
Legt eine neue Datenbank mit den default payment_method und category tabellen an.

def expense_filter(self, filter: dict) -> list[Expense]:

def delete_expense(self, expense: Expense) -> Expense:

def update_expense(self, expense: Expense) -> bool:

def insert_expense(self, expense: Expense) -> Expense:

def delete_payment_method(self, payment_method: Payment_method) -> Payment_method:

def update_payment_method(self, payment_method: Payment_method) -> bool:

def insert_payment_method(self, payment_method: Payment_method) -> Payment_method:

def payment_method_list(self) -> list[Payment_method]:

def update_category(self, category: Category) -> bool:

def insert_category(self, category: Category) -> Category:

def find_subcategories(self, parent_category_id):

def find_parent_categories(self) -> list[Category]:
