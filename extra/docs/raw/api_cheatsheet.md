Extra_api

Modul: modules/api.py
Klasse: Extra_api

Wichtig:
Alle Api Anfragen müssen im JSON Format erfolgen.

Methoden:
expense_filter(self, data:str) -> str:
delete_expense(self, data: str) -> str:
update_expense(self, data: str) -> str:
insert_expense(self, data: str) -> str:
payment_method_list(self) -> str:
delete_payment_method(self, data:str) -> str:
update_payment_method(self, data:str) -> str:
insert_payment_method(self, data:str) -> str:
subcategory_list(self, data:str) -> str:
parent_category_list(self) -> str:
update_category(self, data: str) -> str:
insert_category(self, data:str) -> str:
create_db(self, data:str) -> str:
switch_db(self, name: str) -> str:
yearly_expense(self, data: str):
plot_monthly_expense(self, data: str):
monthly_expense(self, data: str) -> str:

Erklärungen:
plot_monthly_expense(self, data: str):
Experimentelles Feature. Zeichnet ein Balkendiagramm der Monatlichen Ausgaben.
{'year': 'yyyy', 'order': {field: 'month/amount_sum', asc: True/False}}

yearly_expense(self, data: str):
Optional können sortieroptionen in der folgenden Form übergeben werden:
{field: 'month/amount_sum', asc: True/False}}
Gibt die Summe der Ausgaben von jedem Jahr zurück.

monthly_expense(self, data: str) -> str:
Benötigt das Jahr und Optional Sortieroptionen.
{'year': 'yyyy', 'order': {field: 'month/amount_sum', asc: True/False}}
Gibt eine Liste der Monate zusammen mit der Summe der Ausgaben im JSON
Format zurück.

delete_payment_method(self, data:str) -> str:
Löscht eine payment_method aus der Datenbank.
Benötigt ein Dict im JSON-Format in der Form {'id': int }
Gibt ein Dict des gelöschten Eintrags im JSON-Format zurück.

delete_category(self, data:str) -> str:
Löscht eine category aus der Datenbank.
Benötigt ein Dict im JSON-Format in der Form {'id': int }
Gibt ein Dict des gelöschten Eintrags im JSON-Format zurück.

delete_expense(self, data: str) -> str:
Löscht eine expense aus der Datenbank.
Benötigt ein Dict im JSON-Format in der Form {'id': int }
Gibt ein Dict des gelöschten Eintrags im JSON-Format zurück.

expense_filter(self, data:str) -> str:
Benötigt ein Dict im JSON-Format mit den gewünschten Filter Optionen
filterdict = {
    start_date: yyyy-mm-dd,
    end_date: yyyy-mm-dd,
    min_amount: amount,
    max_amount: amount,
    category_list: [category_id],
    payment_method_list: [payment_method_id],
    order: {'field':'field', asc: True/False}
}
Nicht benötigte Filter können weggelassen oder auf None gesetzt werden.
Gibt eine Liste von Dicts im JSON-Format zurück.

insert_category(self, data:str) -> str:
Legt neue category in der DB an.
Benötigt ein Dict im JSON-Format mit dem Namen der Kategorie und optional
die id der Übergeordneten Kategorie
{
    'name': str
    'parent_category': int
}
Gibt ein Dict der eingefügten category im JSON-Format zurück.

insert_expense(self, data: str) -> str:
Legt neue expense in der DB an.
Benötigt ein Dict im JSON-Format mit amount, date, category als Dict!,
payment_method als Dict! und der note.
{
    'amount': float,
    'date': datumsstring in der form yyyy-mm-dd
    'category': {id: int}
    'payment_method': {id: int}
    'note': {str}
}
Gibt ein Dict der eingefügten expense im JSON-Format zurück.

insert_payment_method(self, data:str) -> str:
Legt neue payment_method in der DB an.
Benötigt ein Dict im JSON-Format mit dem gewünschten Namen
{'name': str }
Gibt ein Dict der eingefügten payment_method im JSON-Format zurück.

parent_category_list(self) -> str:
Gibt eine Liste aller "Hauptkategorien" im JSON-Format zurück.

subcategory_list(self, data:str) -> str:
Benötigt die id einer parent_category.
{id: int}
Gibt eine Liste aller Unterkategorien dieser "Hauptkategorie" zurück

update_category(self, data: str) -> str:
Ändert die gewünschte Kategorie auf die neuen Werte. 
{
    'id': int,
    'name': str,
    'parent_category': int,
}
Gibt bei erfolg True im JSON-Format zurück

update_expense(self, data: str) -> str:
Ändert die gewünschte expense auf die neuen Werte. 
{
    'id': int
    'amount': float,
    'date': datumsstring in der form yyyy-mm-dd
    'category': {id: int}
    'payment_method': {id: int}
    'note': {str}
}
Gibt bei erfolg True im JSON-Format zurück

update_payment_method(self, data:str) -> str:
Ändert die gewünschte payment_method auf die neuen Werte. 
{'id': int, 'name': str }
Gibt bei erfolg True im JSON-Format zurück
