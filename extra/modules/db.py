from modules.models import Category, Payment_method, Expense
import sqlite3
import json

class DBController:
    def __init__(self, db_name: str = 'databases/extra.db') -> None:
        self._db_name = db_name

    def payment_method_export(self) -> list[tuple]:
        query = '''
            select * from payment_method
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        payment_method_list = res.fetchall()
        return payment_method_list

    def category_export(self) -> list[tuple]:
        query = '''
            select * from category
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        category_list = res.fetchall()
        connection.close()
        return category_list
 
    def expense_export(self) -> list[tuple]:
        query = '''
            select * from expense
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        return res.fetchall()
 
    def db_export(self) -> dict[str, list[tuple]]:
        query = '''
            select * from expense
        '''
        export_dict = {
            'db': self.get_dbname(),
        }
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        export_dict['expense_table'] = res.fetchall() 

        query = '''
            select * from category 
        '''
        cur = connection.cursor()
        res = cur.execute(query)
        export_dict['category_table'] = res.fetchall() 
 
        query = '''
            select * from payment_method
        '''
        cur = connection.cursor()
        res = cur.execute(query)
        export_dict['payment_method_table'] = res.fetchall() 
        connection.close()
        return export_dict
    '''
        options: {
            year: year,
        }
    '''
    def category_expense(self, options: dict) -> list[tuple]:
        query = '''
            select
              sum(expense.amount),
              category.name
            from expense
            join category on category.id = expense.category_id
            where strftime('%Y', expense.date) = ?
            group by category.id
            order by 1;
        '''

        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, [options['year']])
        expense_list = res.fetchall() 
        connection.close()
        return expense_list

    def profile_details(self) -> dict[str, float, int]:
        query = '''
            select 
              sum(expense.amount),
              avg(expense.amount),
              count(expense.id)
            from expense
        '''

        profile_details = {'db': self.get_dbname()}
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query).fetchone()
        #print(res)
        sum, avg, count = res
        profile_details['expense_sum'] = sum
        profile_details['expense_avg'] = avg
        profile_details['expense_count'] = count 

        query = '''
            select 
              expense.date
            from expense
            order by expense.date
        '''

        res = cur.execute(query).fetchone()
        if res:
            profile_details['oldest_entry'] = res[0]
        else:
            profile_details['oldest_entry'] = 'Noch keine Einträge vorhanden.' 

        query = '''
            select 
              expense.date
            from expense
            order by expense.date desc
        '''

        res = cur.execute(query).fetchone()
        if res:
            profile_details['newest_entry'] = res[0]
        else:
            profile_details['newest_entry'] = 'Noch keine Einträge vorhanden.' 
        connection.close()
        return profile_details

    '''
        'order': {field: 'month/amount_sum', asc: True/False}
    '''
    def yearly_expense(self, order: dict[str, bool]) -> list[tuple]:
        query = '''
            select
              sum(expense.amount) as amount_sum,
              strftime('%Y', expense.date) as year 
            from expense
            group by strftime('%Y', expense.date)
        '''

        if order.get('field'):
            query += f' order by {order['field']}'
            if not order.get('asc'):
                query += ' desc'
        else:
            query += ' order by year'

        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        expense_list = res.fetchall() 
        connection.close()
        return expense_list


    '''
        order is optional. year needs to be provided
        options: {
            'year': 'yyyy',
            'order': {field: 'month/amount_sum', asc: True/False}
        }
    '''
    def monthly_expense(self, options: dict[str, dict]) -> list:
        query = '''
            select
              sum(expense.amount) as amount_sum,
              strftime('%m', expense.date) as month
            from expense
            where strftime('%Y', expense.date) = ?
            group by strftime('%m', expense.date)
        '''

        if options.get('order'):
            query += f' order by {options['order']['field']}'
            if not options['order'].get('asc'):
                query += ' desc'
        else:
            query += ' order by month'

        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, [options['year']])
        expense_list = res.fetchall() 
        connection.close()
        return expense_list

    def switch_db(self, path: str) -> str:
        self._db_name = path
        return self._db_name

    def create_new(self, path: str) -> bool:
        connection = sqlite3.connect(path)
        try:
            # Create Schema
            with open(
                'assets/schema_definition.sql',
                'r',
                encoding ='utf-8'
            ) as schema_file:
                connection.executescript(schema_file.read())

            # Insert default categories 
            with open(
                'assets/default_categories.sql',
                'r',
                encoding ='utf-8'
            ) as category_file:
                connection.executescript(category_file.read())

            # Insert default payment_methods 
            with open(
                'assets/default_payment_methods.sql',
                'r',
                encoding ='utf-8'
            ) as payment_methods_file:
                connection.executescript(payment_methods_file.read())
            connection.close()
            return True
        except:
            return False

    def expense_filter(self, filter: dict[str, list]) -> list[Expense]:
        query = '''
            select
              expense.id,
              expense.amount,
              expense.date,
              expense.notes,
              category.id as category_id,
              category.name as category_name,
              category.parent_category as category_parent,
              payment_method.id as payment_method_id,
              payment_method.name as payment_method_name
            from expense
            join category on expense.category_id = category.id
            join payment_method on expense.payment_method_id = payment_method.id
            where 1=1
        '''

        filter_data = []
        if filter.get('start_date'):
            query += ' and expense.date >= ?'
            filter_data.append(filter['start_date'])
        if filter.get('end_date'):
            query += ' and expense.date <= ?'
            filter_data.append(filter['end_date'])
        if filter.get('min_amount'):
            query += ' and expense.amount >= ?'
            filter_data.append(filter['min_amount'])
        if filter.get('max_amount'):
            query += ' and expense.amount <= ?'
            filter_data.append(filter['max_amount'])
        if filter.get('category_list'):
            if len(filter['category_list']) == 0:
                return 
            qmarks = len(filter['category_list']) * '?, '
            qmarks = qmarks[:-2]
            query += f' and expense.category_id in ({qmarks})'
            for category_id in filter['category_list']:
                filter_data.append(category_id)
        if filter.get('payment_method_list'):
            if len(filter['payment_method_list']) == 0:
                return 
            qmarks = len(filter['payment_method_list']) * '?, '
            qmarks = qmarks[:-2]
            query += f' and payment_method_id in ({qmarks})'
            for payment_method_id in filter['payment_method_list']:
                filter_data.append(payment_method_id)
        if filter.get('order'):
            query += f' order by {filter['order']['field']}'
            #filter_data.append(filter['order']['field'])
            if not filter['order']['asc']:
                query += ' desc'

        #print(query)
        #print(filter_data)
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, filter_data)
        expense_list_raw = res.fetchall()
        expense_list = []
        for expense_tuple in expense_list_raw:
            id, amount, date, notes, category_id, category_name, category_parent, payment_id, payment_name = expense_tuple
            category = Category(category_id, category_name, category_parent)
            payment = Payment_method(payment_id, payment_name)
            expense_list.append(Expense(id, amount, date, category, payment, notes))
        return expense_list

    def delete_expense(self, expense: Expense) -> Expense:
        query = '''
            delete from expense where id = ? returning *
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        res = cur.execute(query, [expense.get_id()])
        expense_tuple = res.fetchone()
        id, amount, date, category_id, payment_id, notes, reccuring = expense_tuple
        query = '''
            select * from category where id = ?
        '''
        res = cur.execute(query, [category_id])
        category_tuple = res.fetchone()
        category_id, category_parent, category_name = category_tuple
        category = Category(category_id, category_name, category_parent)
        query = '''
            select * from payment_method where id = ?
        '''
        res = cur.execute(query, [payment_id])
        payment_tuple = res.fetchone()
        payment_id, payment_name = payment_tuple
        payment_method = Payment_method(payment_id, payment_name)
        connection.commit()
        connection.close()
        return Expense(id, amount, date, category, payment_method, notes)

    def update_expense(self, expense: Expense) -> bool:
        query = '''
            update expense
              set amount = ?, date = ?, category_id = ?, payment_method_id = ?, notes = ?
            where id = ?
        '''
        update_data = [
            expense.get_amount(),
            expense.get_date(),
            expense.get_category().get_id(),
            expense.get_payment_method().get_id(),
            expense.get_note(),
            expense.get_id()
        ]
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        res = cur.execute(query, update_data)
        connection.commit()
        connection.close()
        return True

    def insert_expense(self, expense: Expense) -> Expense:
        query = ''' 
            insert into expense (amount, date, category_id, payment_method_id, notes)
            values (?, ?, ?, ?, ?) returning id
        '''
        insert_data = [
            expense.get_amount(),
            expense.get_date(),
            expense.get_category().get_id(),
            expense.get_payment_method().get_id(),
            expense.get_note()
        ]
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        res = cur.execute(query, insert_data)
        id_tuple = res.fetchone()
        expense_id = id_tuple[0]
        connection.commit()

        query = '''
            select
              expense.id,
              expense.amount,
              expense.date,
              expense.notes,
              category.id as category_id,
              category.name as category_name,
              category.parent_category as category_parent,
              payment_method.id as payment_method_id,
              payment_method.name as payment_method_name
            from expense
            join category on expense.category_id = category.id
            join payment_method on expense.payment_method_id = payment_method.id
            where expense.id = ?
        '''

        res = cur.execute(query, [expense_id])
        expense_tuple = res.fetchone()
        #print(expense_tuple)

        id, amount, date, notes, category_id, category_name, category_parent, payment_id, payment_name = expense_tuple
        category = Category(category_id, category_name, category_parent)
        payment = Payment_method(payment_id, payment_name)
        return Expense(id, amount, date, category, payment, notes)

    def delete_payment_method(self, payment_method: Payment_method) -> Payment_method:
        query = ''' 
            delete from payment_method where id = ? returning * 
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        try:
            res = cur.execute(query, [payment_method.get_id()])
            id, name = res.fetchone()
            connection.commit()
            return Payment_method(id, name)
        except:
            return False
        finally:
            connection.close()

    def update_payment_method(self, payment_method: Payment_method) -> bool:
        query = ''' 
            update payment_method set name = ? where id = ? 
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, [payment_method.get_name(), payment_method.get_id()])
        connection.commit()
        connection.close()
        return True

    def insert_payment_method(self, payment_method: Payment_method) -> Payment_method:
        query = ''' 
            insert into payment_method (name) values (?) returning * 
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, [payment_method.get_name()])
        id, name = res.fetchone()
        connection.commit()
        connection.close()
        return Payment_method(id, name)

    def payment_method_list(self) -> list[Payment_method]:
        query = ''' 
            select * from payment_method order by name 
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        payment_list_raw = res.fetchall()
        payment_methods = []
        for payment_tuple in payment_list_raw:
            id, name = payment_tuple
            payment_method = Payment_method(id, name)
            payment_methods.append(payment_method)
        connection.close()
        return payment_methods

    def update_category(self, category: Category) -> bool:
        query = ''' 
            update category
            set name = ?, parent_category = ?
            where id = ?
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        res = cur.execute(query, [category.get_name(), category.get_parent_category(), category.get_id()])
        connection.commit()
        connection.close()
        return True

    def insert_category(self, category: Category) -> Category:
        query = '''
            insert into category (name, parent_category) values (?, ?) returning id, name, parent_category
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        res = cur.execute(query, [category.get_name(), category.get_parent_category()])
        id, name, parent_category = res.fetchone()
        connection.commit()
        connection.close()
        return Category(id, name, parent_category)

    def find_subcategories(self, parent_category_id):
        query = '''
            select
              id,
              name,
              parent_category
            from
              category
            where parent_category = ? 
            order by name
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query, [parent_category_id])
        category_list_raw = res.fetchall()
        category_list = []
        for category_raw in category_list_raw:
            id, name, parent_category = category_raw
            category = Category(id, name, parent_category)
            category_list.append(category)
        connection.close()
        return category_list

    def find_parent_categories(self) -> list[Category]:
        query = '''
            select
              id,
              name
            from
              category
            where parent_category is null
            order by name
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        res = cur.execute(query)
        category_list_raw = res.fetchall()
        category_list = []
        for category_raw in category_list_raw:
            id, name = category_raw
            category = Category(id, name)
            category_list.append(category)
        connection.close()
        return category_list

    def delete_category(self, category: Category) -> Category:
        query = ''' 
            delete from category where id = ? returning *
        '''
        connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        try:
            res = cur.execute(query, [category.get_id()])
            id, parent_category, name = res.fetchone()
            connection.commit()
            return Category(id, name, parent_category)
        except:
            return False
        finally:
            connection.close()

    def import_payment_methods(self):
        connection = sqlite3.connect('databases/demo.db')
        #connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        payment_json = ''
        with open("./assets/payment_methods.json") as file:
            payment_json = file.read()
            
        payment_dict = json.loads(payment_json)
        payment_list = payment_dict['payment_methods']
        insert_list = []
        for pay in payment_list:
            insert_list.append([pay])
        query = ''' 
            insert into payment_method (name) values (?) 
        '''
        res = cur.executemany(query, insert_list)
        connection.commit()
        connection.close()
        return True

    def import_categories(self) -> bool:
        connection = sqlite3.connect('databases/demo.db')
        #connection = sqlite3.connect(self._db_name)
        cur = connection.cursor()
        categories_json = ''
        with open("./assets/categories.json") as file:
            categories_json = file.read()
            
        category_dict = json.loads(categories_json)
        category_list = category_dict['categories']
        #print(category_list)
        category_query = ''' 
            insert into category (name) values (?) returning id 
        '''
        subcategory_query = ''' 
            insert into category (name, parent_category) values (?, ?)
        '''
        for category in category_list:
            res = cur.execute(category_query, [category['name']])
            id_tuple = res.fetchone()
            subcategory_list = []
            for subcategory_name in category['subcategories']:
                subcategory_list.append([subcategory_name, id_tuple[0]])
            #print(subcategory_list)
            res = cur.executemany(subcategory_query, subcategory_list)
        connection.commit()
        connection.close()
        return True
    def get_dbname(self):
        return self._db_name
