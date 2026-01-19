import json

class Category:
    def __init__(self, id: int = None, name: str = None, parent_category: int = None) -> None:
        self._id: int = id
        self._name: str = name
        self._parent_category: int = parent_category

    def get_id(self) -> int:
        return self._id

    def get_parent_category(self) -> int:
        return self._parent_category

    def get_name(self) -> str:
        return self._name

    def set_id(self, id: int) -> bool:
        self._id = id
        return True

    def json_import(self, json_str: str) -> None:
        cat_raw = json.loads(json_str)
        self._id = cat_raw.get('id')
        self._name = cat_raw.get('name')
        self._parent_category = cat_raw.get('parent_category')
        return 

    def json_export(self) -> str:
        return json.dumps({'id': self._id, 'name': self._name, 'parent_category': self._parent_category})

    def __str__(self) -> str:
        return f'ID: {self._id} - Name: {self._name} - Parent Category: {self._parent_category}'


class Payment_method:
    def __init__(self, id: int = None, name: str = None):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_id(self, id):
        self._id = id
        return True

    def json_import(self, json_str) -> None:
        pay_raw = json.loads(json_str)
        self._id = pay_raw.get('id')
        self._name = pay_raw.get('name')
        return 

    def json_export(self) -> str:
        return json.dumps({'id': self._id, 'name': self._name})

    def __str__(self):
        return f'ID: {self._id} - Name: {self._name}'


class Expense:
    def __init__(
        self,
        id: int = None,
        amount: float = 0,
        date: str = '',
        category: Category = Category(),
        payment_method: Payment_method = Payment_method(),
        note: str = ''
    ) -> None:
        self._id = id
        self._amount = amount
        self._date = date
        self._category = category
        self._payment_method = payment_method
        self._note = note

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> bool:
        self._id = id
        return True

    def get_amount(self) -> float:
        return self._amount

    def get_date(self) -> str:
        return self._date

    def get_category(self) -> Category:
        return self._category

    def get_payment_method(self) -> Payment_method:
        return self._payment_method

    def get_note(self) -> str:
        return self._note

    def json_import(self, json_str: str) -> None:
        expense_raw = json.loads(json_str)
        category = Category() 
        if expense_raw.get('category'):
            category = Category(
                expense_raw['category'].get('id'),
                expense_raw['category'].get('name'),
                expense_raw['category'].get('parent_catgory')
            )
        payment_method = Payment_method()
        if expense_raw.get('payment_method'):
            payment_method = Payment_method(
                expense_raw['payment_method'].get('id'),
                expense_raw['payment_method'].get('name'),
            )
        self._id = expense_raw.get('id')
        self._amount = expense_raw.get('amount')
        self._date = expense_raw.get('date')
        self._note = expense_raw.get('note')
        self._category = category
        self._payment_method = payment_method
        return

    def json_export(self) -> str:
        export_dict = {
            'id': self._id,
            'amount': self._amount,
            'date': self._date,
            'category': {
                'id': self._category.get_id(),
                'name': self._category.get_name(),
                'parent_category': self._category.get_parent_category()
            },
            'payment_method': {'id': self._payment_method.get_id(), 'name': self._payment_method.get_name()},
            'note': self._note,
        }
        return json.dumps(export_dict)
    def dict_export(self) -> dict:
        export_dict = {
            'id': self._id,
            'amount': self._amount,
            'date': self._date,
            'category': {
                'id': self._category.get_id(),
                'name': self._category.get_name(),
                'parent_category': self._category.get_parent_category()
            },
            'payment_method': {'id': self._payment_method.get_id(), 'name': self._payment_method.get_name()},
            'note': self._note,
        }
        return export_dict
    def __str__(self) -> str:
        return f'id - amount - date - category - payment method - note\n {self._id} - {self._amount} - {self._date} - {self._category.get_name()} - {self._payment_method.get_name()} - {self._note}'


