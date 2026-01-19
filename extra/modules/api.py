import json
import csv
from datetime import datetime
from pathlib import Path

from modules.models import Category, Payment_method, Expense
from modules.db import DBController
from modules.plotter import Extra_plotter 

# Type alias for type hints
JSONStr = str

'''
Extra_api
All API calls need to be in JSON
'''

class Extra_api:
    def __init__(self) -> None:
        self._db_controller = DBController()
        self._plotter = Extra_plotter()

    def payment_method_export_csv(self) -> str:
        res = self._db_controller.payment_method_export()
        datestring = datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
        filename = f'paymethod_export_{datestring}.csv'
        try:
            with open(f'exports/{filename}', 'w', newline = '', encoding = 'utf-8') as export_file:
                writer = csv.writer(export_file)
                writer.writerows(res)
            return filename
        except:
            return json.dumps(False)

    def category_export_csv(self) -> str:
        res = self._db_controller.category_export()
        datestring = datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
        filename = f'category_export_{datestring}.csv'
        try:
            with open(f'exports/{filename}', 'w', newline = '', encoding = 'utf-8') as export_file:
                writer = csv.writer(export_file)
                writer.writerows(res)
            return filename
        except:
            return json.dumps(False)

    def expense_export_csv(self) -> str:
        res = self._db_controller.expense_export()
        datestring = datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
        filename = f'expense_export_{datestring}.csv'
        try:
            with open(f'exports/{filename}', 'w', newline = '', encoding = 'utf-8') as export_file:
                writer = csv.writer(export_file)
                writer.writerows(res)
            return filename
        except:
            return json.dumps(False)

    def db_export_json(self) -> str:
        res = self._db_controller.db_export()
        #print(json.dumps(res))

        datestring = datetime.now().strftime('%Y-%m-%dT%H-%M-%SZ')
        filename = f'db_export_{datestring}.json'
        #print(filename)
        try:
            with open(f'exports/{filename}', 'w', encoding='utf-8') as export_file:
                export_file.write(json.dumps(res))
            return filename 
        except:
            return json.dumps(False)

    def category_expense(self, data: str) -> str:
        options = json.loads(data)
        res = self._db_controller.category_expense(options)
        return json.dumps(res)

    def plot_category_expense_png(self, data: str) -> bytes:
        options = json.loads(data)
        expense_json = self.category_expense(data)
        if not expense_json:
            return False
        expense_list = json.loads(expense_json)
        res = self._plotter.category_expense_png(expense_list, options['year'])
        return res

    def plot_monthly_expense_png(self, data: str) -> bytes:
        options = json.loads(data)
        expense_json = self.monthly_expense(data)
        if not expense_json:
            return False
        expense_list = json.loads(expense_json)
        res = self._plotter.monthly_expense_png(expense_list, options['year'])
        return res

    def profile_details(self) -> str:
        res = self._db_controller.profile_details()
        if not res['expense_avg']:
            res['expense_avg'] = 0
        if not res['expense_sum']:
            res['expense_sum'] = 0
        return json.dumps(res)

    def delete_db(self, db_name: str) -> str:
        path = f'databases/{db_name}.db'
        #print(path)
        Path(path).unlink()
        return json.dumps('True')

    def save_config(self, config: str) -> str:
        with open("config/config.json", "w") as config_file:
            config_file.write(config)
        return json.dumps(True)

    def load_config(self) -> str:
        config_json = ''
        with open("config/config.json", "r") as config_file:
            config_json = config_file.read()
        return config_json

    def profile_info(self) -> str:
        path_module = Path("databases")
        # get a list of files with a certain file suffix 
        profiles = list(path_module.glob("*.db"))
        active_profile = self._db_controller.get_dbname()
        profile_list = []
        for profile in profiles:
            profile_list.append(str(profile))
        
        return json.dumps({
            'active': self._db_controller.get_dbname(),
            'profile_list': profile_list
        })


    '''
        'order': {field: 'month/amount_sum', asc: True/False}
    '''
    def yearly_expense(self, data: str) -> str:
        order = json.loads(data)
        res = self._db_controller.yearly_expense(order)
        return json.dumps(res)

    '''
        order is optional. year needs to be provided
        options: {
            'year': 'yyyy',
            'order': {field: 'month/amount_sum', asc: True/False}
        }
        is just plotted to screen for now. Have to think about
        an export format.
    '''

    def plot_monthly_expense(self, data: str):
        options = json.loads(data)
        expense_json = self.monthly_expense(data)
        expense_list = json.loads(expense_json)
        self._plotter.monthly_expense(expense_list, options['year'])

    '''
    order is optional. year needs to be provided
    options: {
        'year': 'yyyy',
        'order': {field: 'month/amount_sum', asc: True/False}
    }
    '''
    def monthly_expense(self, data: str) -> str:
        options = json.loads(data)
        res = self._db_controller.monthly_expense(options)
        return json.dumps(res)
    '''
    switch_db
    switches to the db provided by name.
    Only works if the Database exists.
    Args: {'name': ...}
    '''

    def switch_db(self, data: str) -> str:
        db_info = json.loads(data)
        path = f'databases/{db_info['name']}.db'
        try:
            db_file = open(path, 'r')
            db_file.close()
            res = self._db_controller.switch_db(path)
            return json.dumps(True)
        except:
            return json.dumps(False)

    '''
    create_db
    creates a new db with the given name and
    sets it up with schemas and default categories +
    payment_methods
    {name: ...}
    '''
    def create_db(self, data:str) -> str:
        db_info = json.loads(data)
        #print(db_info)
        path = f'databases/{db_info['name']}.db'
        try:
            db_file = open(path, 'x')
            db_file.close()
            res = self._db_controller.create_new(path)
            return json.dumps({'success': 'db created'})
        except:
            return json.dumps({'error': 'file_exists'})

    '''
        filterdict = {
        start_date: yyyy-mm-dd or None
        end_date: yyyy-mm-dd or None
        min_amount: amount or None
        max_amount: amount or None
        category_list: [category_id]
        payment_method_list: [payment_method_id]
        order: {'field':'field', asc: True/False}
        }
    '''

    def expense_filter(self, data:str) -> str:
        filter_dict = json.loads(data)
        res = self._db_controller.expense_filter(filter_dict)
        expense_dict_list = []
        for expense in res:
            #expense_dict = expense.dict_export()
            expense_dict_list.append(expense.dict_export())
        return json.dumps(expense_dict_list)

    def delete_expense(self, data: str) -> str:
        expense = Expense()
        expense.json_import(data)
        res = self._db_controller.delete_expense(expense)
        return res.json_export()

    def update_expense(self, data: str) -> str:
        expense = Expense()
        expense.json_import(data)
        res = self._db_controller.update_expense(expense)
        return json.dumps(res)

    def insert_expense(self, data: str) -> str:
        expense = Expense()
        expense.json_import(data)
        res = self._db_controller.insert_expense(expense)
        return res.json_export()
        
    '''
    payment_method_list
    Description: Returns a JSON encoded list of every payment_method 
    '''
    def payment_method_list(self) -> str:
        res = self._db_controller.payment_method_list()
        paylist = []
        for payment in res:
            pay = {
                'id': payment.get_id(),
                'name': payment.get_name(),
            }
            paylist.append(pay)
        return json.dumps(paylist)
    '''
    delete_payment_method
    Description: Deletes a payment_method.
    Expects a JSON encoded Dict with id
    Returns the deleted payment_method as JSON. 
    '''
    def delete_payment_method(self, data:str) -> str:
        payment_dict = json.loads(data)
        payment_method = Payment_method(
            payment_dict['id'],
        )
        res = self._db_controller.delete_payment_method(payment_method)
        if not res:
            return json.dumps(res)
        return json.dumps({'id': res.get_id(), 'name': res.get_name()})

    '''
    update_payment_method
    Description: Updates a payment_method.
    Expects a JSON encoded Dict with id and name
    Returns "True" on successful update. 
    '''
    def update_payment_method(self, data:str) -> str:
        payment_dict = json.loads(data)
        payment_method = Payment_method(
            payment_dict['id'],
            payment_dict['name']
        )
        #print(payment_method)
        res = self._db_controller.update_payment_method(payment_method)
        return json.dumps(res)
    '''
    insert_payment_method
    Description: Inserts a new category into the DB.
    Expects a JSON encoded Dict with name and parent_category_id
    Returns the inserted category as JSON
    '''
    def insert_payment_method(self, data:str) -> str:
        payment_dict = json.loads(data)
        payment_method = Payment_method(None, payment_dict['name'])
        res = self._db_controller.insert_payment_method(payment_method)
        return json.dumps({'id': res.get_id(), 'name': res.get_name()})
    '''
    parent_category_list
    Description: Returns a JSON encoded list of every subcategory
    in a category
    '''
    def subcategory_list(self, data:str) -> str:
        cat_dict = json.loads(data)
        res = self._db_controller.find_subcategories(cat_dict['id'])
        catlist = []
        for category in res:
            cat = {
                'id': category.get_id(),
                'name': category.get_name(),
                'parent_id': category.get_parent_category()
            }
            catlist.append(cat)
        return json.dumps(catlist)

    '''
    parent_category_list
    Description: Returns a JSON encoded list of every parent_category 
    '''
    def parent_category_list(self) -> str:
        res = self._db_controller.find_parent_categories()
        catlist = []
        for category in res:
            cat = {
                'id': category.get_id(),
                'name': category.get_name(),
                'parent_id': category.get_parent_category()
            }
            catlist.append(cat)
        return json.dumps(catlist)

    '''
    update_category
    Description: updates category.
    Expects a JSON encoded Dict with id, name and parent_id
    returns True on successful update 
    '''
    def update_category(self, data: str) -> str:
        cat_dict = json.loads(data)
        category = Category(
            cat_dict['id'],
            cat_dict['name'],
            cat_dict['parent_id']
        )
        res = self._db_controller.update_category(category)
        return json.dumps(res)
    '''
    delete_category
    Description: Removes category from DB.
    Only works for categories that do not have a subcategory
    and there can't be expenses in that category
    Expects a JSON encoded Dict with id
    returns the removed category as JSON String
    '''
    def delete_category(self, data:str) -> str:
        cat_dict = json.loads(data)
        category = Category(
            cat_dict['id'],
        )
        res = self._db_controller.delete_category(category)
        if not res:
            return json.dumps(res)
        return res.json_export()

    '''
    insert_category
    Description: Inserts a new category into the DB.
    Expects a JSON encoded Dict with name and parent_category_id
    Returns the inserted category as JSON
    '''
    def insert_category(self, data:str) -> str:
        cat_dict = json.loads(data)
        parent_category = cat_dict.get('parent_category_id')
        category = Category(
            None,
            cat_dict['name'],
            #cat_dict['parent_category_id']
            parent_category
        )
        res = self._db_controller.insert_category(category)
        return res.json_export()

