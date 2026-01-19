import sys
import json
from pathlib import Path
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QStackedWidget,
    QLabel, QListWidget, QTextEdit, QLineEdit, QComboBox, QPushButton,
    QDateEdit, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtGui import (
    QAction, QPixmap, 
    QDoubleValidator, QIntValidator
)
from PySide6.QtCore import QSize, Qt, QDate, QLocale
from modules.api import Extra_api
xtra_api = Extra_api()

colors = {'red': '#bd2a2a', 'green': '#16A34A', 'blue': '#3b82f6'}

class ExpenseTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self._expense_list = []
        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)
        top_label = QLabel('<b>Ausgaben</b>')
        grid.addWidget(top_label, 0, 0, 1, 2)
        self.expense_table = QTableWidget(0, 7)
        self.expense_table.setHorizontalHeaderLabels(["Betrag", "Datum", "Kategorie", "Bezahlm.", "🗉", '🖉', '✖'])
        self.expense_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.expense_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.expense_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.expense_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.expense_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.expense_table.horizontalHeader().resizeSection(4, 25)
        self.expense_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.expense_table.horizontalHeader().resizeSection(5, 25)
        self.expense_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)
        self.expense_table.horizontalHeader().resizeSection(6, 25)
        #self.expense_table.cellClicked.connect(self.click_expense_table_cell)
        grid.addWidget(self.expense_table, 1, 0, 1, 2)

        self.sum_label = QLabel('<b>Summe:</b>')
        #self.sum_label.setMaximumHeight(20)
        grid.addWidget(self.sum_label, 2, 0, 1, 2)
        self.note_display = QTextEdit(self)
        self.note_display.setReadOnly(True)
        self.note_display.setFixedHeight(65)
        self.note_display.setPlaceholderText('Keine Notiz')
        grid.addWidget(self.note_display, 3, 0, 1, 2)
        grid.setRowStretch(0, 0)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 0)
        grid.setRowStretch(3, 0)

        self.setLayout(grid)

    def confirm_delete(self, title="Sicher?", text="Möchten Sie fortfahren?") -> bool:
        delete_alert = QMessageBox()
        delete_alert.setWindowTitle(title)
        delete_alert.setText(text)
        delete_alert.setIcon(QMessageBox.Warning)
        yes = delete_alert.addButton(QMessageBox.Yes)
        yes.setText('Löschen')
        no  = delete_alert.addButton(QMessageBox.No)
        no.setText('Abbrechen')
        delete_alert.setDefaultButton(QMessageBox.No)
        result = delete_alert.exec()
        return result == QMessageBox.Yes

    def render_table(self, expense_list):
        #self._expense_list = expense_list
        self.expense_table.clearContents()
        self.expense_table.setRowCount(0)
        amount_sum = 0
        for i in range(0, len(expense_list)):
            amount_sum += expense_list[i]['amount']
            row = self.expense_table.rowCount()
            self.expense_table.insertRow(row)
            amount_item = QTableWidgetItem(f'{expense_list[i]['amount']:.2f}€')
            amount_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.expense_table.setItem(
                row,
                0,
                amount_item 
            )
            date_item = QTableWidgetItem(expense_list[i]['date'])
            date_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.expense_table.setItem(
                row,
                1,
                date_item
            )
            self.expense_table.setItem(
                row,
                2,
                QTableWidgetItem(expense_list[i]['category']['name'])
            )
            self.expense_table.setItem(
                row,
                3,
                QTableWidgetItem(expense_list[i]['payment_method']['name'])
            )
            note_item = QTableWidgetItem('')
            if expense_list[i]['note'] != '':
                note_item.setText('🗉')
            note_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            note_item.setData(Qt.UserRole, {'note': expense_list[i]['note']})
            self.expense_table.setItem(
                row,
                4,
                note_item
            )
            edit_item = QTableWidgetItem('🖉')
            edit_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            edit_item.setData(Qt.UserRole, {'edit': expense_list[i]})
            self.expense_table.setItem(
                row,
                5,
                edit_item
            )
            delete_item = QTableWidgetItem('✖')
            delete_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            delete_item.setData(Qt.UserRole, {'delete': expense_list[i]})
            self.expense_table.setItem(
                row,
                6,
                delete_item
            )
        self.sum_label.setText(f'Summe: {amount_sum:.2f}€')
  
class ExpenseFilterForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Ausgabenfilter</b>'), 0, 0, 1, 2)

        validator = QDoubleValidator(0.00, 1_000_000.00, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        # At testing I had problems that validator sometime wants dots and sometimes wants commas.
        # So we set local to english to force dots.
        validator.setLocale(QLocale(QLocale.English))

        grid.addWidget(QLabel("Betrag (min):"), 1, 0, alignment=Qt.AlignRight)
        self.minamount_input = QLineEdit()
        self.minamount_input.setValidator(validator)
        grid.addWidget(self.minamount_input, 1, 1)

        grid.addWidget(QLabel("Betrag (max):"), 2, 0, alignment=Qt.AlignRight)
        self.maxamount_input = QLineEdit()
        self.maxamount_input.setValidator(validator)
        grid.addWidget(self.maxamount_input, 2, 1)

        grid.addWidget(QLabel("Start-Datum:"), 3, 0, alignment=Qt.AlignRight)
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDisplayFormat("dd.MM.yyyy")
        self.start_date_edit.setDate(QDate.currentDate())
        grid.addWidget(self.start_date_edit, 3, 1)

        grid.addWidget(QLabel("Ende-Datum:"), 4, 0, alignment=Qt.AlignRight)
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDisplayFormat("dd.MM.yyyy")
        self.end_date_edit.setDate(QDate.currentDate())
        grid.addWidget(self.end_date_edit, 4, 1)

        grid.addWidget(QLabel("Sortieren nach:"), 5, 0, alignment=Qt.AlignRight)
        self.combo_orderby = QComboBox()
        self.combo_orderby.addItem('Betrag absteigend', {'field': 'amount', 'asc': False})
        self.combo_orderby.addItem('Betrag aufsteigend', {'field': 'amount', 'asc': True})
        self.combo_orderby.addItem('Datum absteigend', {'field': 'date', 'asc': False})
        self.combo_orderby.addItem('Datum aufsteigend', {'field': 'date', 'asc': True})
        grid.addWidget(self.combo_orderby, 5, 1)

        self.btn_search_expense = QPushButton("Zeige Ausgaben")
        grid.addWidget(self.btn_search_expense, 6, 0, 1, 2)

        grid.setRowStretch(5, 1)
        self.setLayout(grid)

    def search_expense(self):
        parsed_min_amount = 0
        parsed_max_amount = 0
        try:
            parsed_min_amount = float(self.minamount_input.text())
        except:
            parsed_min_amount = -1

        try:
            parsed_max_amount = float(self.maxamount_input.text())
        except:
            parsed_max_amount = -1

        filter_dict = {
            'start_date': self.start_date_edit.date().toString('yyyy-MM-dd'),
            'end_date': self.end_date_edit.date().toString('yyyy-MM-dd'),
            'order': self.combo_orderby.currentData(),
        }

        if parsed_min_amount >= 0:
            filter_dict['min_amount'] = parsed_min_amount
        if parsed_max_amount > 0:
            filter_dict['max_amount'] = parsed_max_amount
        res = xtra_api.expense_filter(json.dumps(filter_dict))
        return json.loads(res) 

class ExpenseUpdateForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Ausgabe Bearbeiten</b>'), 0, 0, 1, 2)

        grid.addWidget(QLabel("Betrag:"), 1, 0, alignment=Qt.AlignRight)
        self.amount_input = QLineEdit()

        validator = QDoubleValidator(0.00, 1_000_000.00, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        # At testing I had problems that validator sometime wants dots and sometimes wants commas.
        # So we set local to english to force dots.
        validator.setLocale(QLocale(QLocale.English))

        self.amount_input.setValidator(validator)
        grid.addWidget(self.amount_input, 1, 1)

        # Category Dropdown
        #categories = xtra_api.parent_category_list()
        #category_list = json.loads(categories)
        grid.addWidget(QLabel("Kategorie:"), 2, 0, alignment=Qt.AlignRight)
        self.combo_category = QComboBox()
        #for category in category_list:
        #    self.combo_category.addItem(category['name'], category['id'])

        grid.addWidget(self.combo_category, 2, 1)

        #subcategories = xtra_api.subcategory_list(
        #    json.dumps({'id': self.combo_category.currentData()})
        #)
        #subcategory_list = json.loads(subcategories)
        grid.addWidget(QLabel("Unterkategorie:"), 3, 0, alignment=Qt.AlignRight)
        self.combo_subcategory = QComboBox()
        #for subcategory in subcategory_list:
        #    self.combo_subcategory.addItem(subcategory['name'], subcategory['id'])

        grid.addWidget(self.combo_subcategory, 3, 1)

        # Payment_methods Dropdown
        #payment_methods = xtra_api.payment_method_list()
        #payment_method_list = json.loads(payment_methods)
        grid.addWidget(QLabel("Bezahlmethode:"), 4, 0, alignment=Qt.AlignRight)
        self.combo_payment = QComboBox()
        #for payment in payment_method_list:
        #    self.combo_payment.addItem(payment['name'], payment['id'])
        grid.addWidget(self.combo_payment, 4, 1)

        grid.addWidget(QLabel("Datum:"), 5, 0, alignment=Qt.AlignRight)
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setDate(QDate.currentDate())
        grid.addWidget(self.date_edit, 5, 1)

        grid.addWidget(QLabel("Notiz:"), 6, 0, alignment=Qt.AlignRight)

        self.note_input = QTextEdit()
        grid.addWidget(self.note_input, 6, 1)

        self.btn_update_expense = QPushButton("Speichern")
        grid.addWidget(self.btn_update_expense, 7, 0, 1, 2)
        #self.btn_save_expense.clicked.connect(self.save_expense)
        self.btn_abort_update = QPushButton("Abbrechen")
        grid.addWidget(self.btn_abort_update, 8, 0, 1, 2)

        self.id_input = QLineEdit()
        grid.addWidget(self.id_input, 8, 0, 1, 2)
        self.id_input.hide()
        grid.setRowStretch(5, 1)
        self.setLayout(grid)

    def change_parent_category(self, index):
        self.combo_subcategory.clear()
        parent_category = self.combo_category.currentData()
        subcategory_list = json.loads(xtra_api.subcategory_list(json.dumps({'id': parent_category['id']})))
        for subcategory in subcategory_list:
            self.combo_subcategory.addItem(subcategory['name'], subcategory)

class ProfileDetails(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        profile_info = json.loads(xtra_api.profile_info())
        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Profil Details</b>'), 0, 0, 1, 2)
        #profile_details = json.loads(xtra_api.profile_details())
        #print(profile_details)

        self.detail_list = QListWidget()
        grid.addWidget(self.detail_list, 1, 0, 1, 2)
        self.update_detail_list()
        self.setLayout(grid)

    def update_detail_list(self) -> None:
        self.detail_list.clear()
        profile_details = json.loads(xtra_api.profile_details())
        self.detail_list.addItem(f'Datenbank: {profile_details['db']}')
        self.detail_list.addItem(f'Einträge: {profile_details['expense_count']}')
        self.detail_list.addItem(f'Ausgabensumme: {profile_details['expense_sum']}€')
        self.detail_list.addItem(f'Ausgaben Ø : {profile_details['expense_avg']:.2f}€')
        self.detail_list.addItem(f'Ältester Eintrag : {profile_details['oldest_entry']}')
        self.detail_list.addItem(f'Neuster Eintrag : {profile_details['newest_entry']}')
 
class ProfileForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Profil Manager</b>'), 0, 0, 1, 2)
        self.setLayout(grid)
       
        grid.addWidget(QLabel("Profile:"), 1, 0, 1, 1, alignment=Qt.AlignRight)
        self.combo_profile = QComboBox()
        self.init_combo_profile()
        grid.addWidget(self.combo_profile, 1, 1, 1, 1)

        grid.addWidget(QLabel("Profil-Name:"), 2, 0, alignment=Qt.AlignRight)
        self.profile_name_input = QLineEdit()
        grid.addWidget(self.profile_name_input, 2, 1, 1, 1)

        self.btn_switch_profile = QPushButton("Profil laden")
        grid.addWidget(self.btn_switch_profile, 3, 0, 1, 2)
 
        self.btn_create_profile = QPushButton("Profil erstellen")
        grid.addWidget(self.btn_create_profile, 4, 0, 1, 2)
 
        self.btn_delete_profile = QPushButton("Profil löschen")
        grid.addWidget(self.btn_delete_profile, 5, 0, 1, 2)
        self.btn_close_menu = QPushButton("Zurück")
        grid.addWidget(self.btn_close_menu, 6, 0, 1, 2)

        grid.setRowStretch(7, 1)
        self.setLayout(grid)

    def init_combo_profile(self) -> None:
        self.profile_info = json.loads(xtra_api.profile_info())
        profile_index = 0
        for index, db_path in enumerate(self.profile_info['profile_list']):
            if db_path == self.profile_info['active']:
                profile_index = index
            path_obj = Path(db_path)
            profile_name = path_obj.stem
            #This approach does not work under windows...
            #path_list = db_path.split('/')
            #profile_name = path_list[1][:-3]
            self.combo_profile.addItem(profile_name, db_path)
        self.combo_profile.setCurrentIndex(profile_index)

    def change_parent_category(self, index):
        self.combo_subcategory.clear()
        parent_category = self.combo_category.currentData()
        subcategory_list = json.loads(xtra_api.subcategory_list(json.dumps({'id': parent_category['id']})))
        for subcategory in subcategory_list:
            self.combo_subcategory.addItem(subcategory['name'], subcategory)


'''
ExpenseInsertForm
Description: Form for adding a new Expense
'''

class ExpenseInsertForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Neue Ausgabe</b>'), 0, 0, 1, 2)

        grid.addWidget(QLabel("Betrag:"), 1, 0, alignment=Qt.AlignRight)
        self.amount_input = QLineEdit()

        validator = QDoubleValidator(0.00, 1_000_000.00, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        # At testing I had problems that validator sometime wants dots and sometimes wants commas.
        # So we set local to english to force dots.
        validator.setLocale(QLocale(QLocale.English))

        self.amount_input.setValidator(validator)
        grid.addWidget(self.amount_input, 1, 1)

        # Category Dropdown
        grid.addWidget(QLabel("Kategorie:"), 2, 0, alignment=Qt.AlignRight)
        self.combo_category = QComboBox()
        grid.addWidget(self.combo_category, 2, 1)

        # Sub-Category Dropdown
        grid.addWidget(QLabel("Sub-Kategorie:"), 3, 0, alignment=Qt.AlignRight)
        self.combo_subcategory = QComboBox()
        grid.addWidget(self.combo_subcategory, 3, 1)

        # Payment Dropdown
        grid.addWidget(QLabel("Bezahlmethode:"), 4, 0, alignment=Qt.AlignRight)
        self.combo_payment = QComboBox()
        grid.addWidget(self.combo_payment, 4, 1)

        grid.addWidget(QLabel("Datum:"), 5, 0, alignment=Qt.AlignRight)
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setDate(QDate.currentDate())
        grid.addWidget(self.date_edit, 5, 1)

        grid.addWidget(QLabel("Notiz:"), 6, 0, alignment=Qt.AlignRight)

        self.note_input = QTextEdit()
        grid.addWidget(self.note_input, 6, 1)

        self.btn_save_expense = QPushButton("Speichern")
        self.btn_save_expense.clicked.connect(self.save_expense)
        grid.addWidget(self.btn_save_expense, 7, 0, 1, 2)

        grid.setRowStretch(5, 1)
        self.setLayout(grid)

    def change_parent_category(self, index) -> None:
        self.combo_subcategory.clear()
        parent_category = self.combo_category.currentData()
        subcategory_list = json.loads(xtra_api.subcategory_list(json.dumps({'id': parent_category['id']})))
        for subcategory in subcategory_list:
            self.combo_subcategory.addItem(subcategory['name'], subcategory)

    def save_expense(self) -> bool:
        parsed_amount = 0
        try:
            parsed_amount = float(self.amount_input.text())
        except:
            QMessageBox.information(self, "Warnung", "Bitte geben sie einen gültigen Betrag ein.")
            return False
        expense_dict = {
            'amount': parsed_amount,
            'category': self.combo_subcategory.currentData(),
            'payment_method': self.combo_payment.currentData(),
            'date': self.date_edit.date().toString('yyyy-MM-dd'),
            'note': self.note_input.toPlainText()
        }

        # Normaly the Expense belongs to a subcategory. Unless there is
        # no subcategory then it belongs to the main category
        if not expense_dict['category']:
            expense_dict['category'] = self.combo_category.currentData()
        res = xtra_api.insert_expense(json.dumps(expense_dict))
        inserted_expense = json.loads(res)
        #print(inserted_expense)
        amount = inserted_expense['amount']
        date = datetime.strptime(inserted_expense['date'], '%Y-%m-%d').strftime('%d.%m.%Y')
        category = inserted_expense['category']['name']
        QMessageBox.information(self, "Erfolg", f"Ausgabe über {amount:.2f} vom {date} in der Kategorie {category} wurde gespeichert")
        return True

class DiagramScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Diagramm</b>'), 0, 0, 1, 2)
        self.image_label = QLabel()
        grid.addWidget(self.image_label, 1, 0, 1, 2)
        grid.setRowStretch(1, 1)
        self.setLayout(grid)
    def pixmap_image(self, png_bytes: bytes) -> None:
        pixmap = QPixmap()
        pixmap.loadFromData(png_bytes, format="PNG")
        self.image_label.setPixmap(pixmap)

class SettingsScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid = QGridLayout()
        self.grid.setContentsMargins(8, 8, 8, 8)
        self.grid.setHorizontalSpacing(10)
        self.grid.setVerticalSpacing(6)

        self.grid.addWidget(QLabel('<h2>Einstellungen Hilfe</h2>'), 0, 0, 1, 1)
        #grid.addWidget(QLabel('Coming Soon...'), 1, 0, 1, 2)
        #self.grid.setRowStretch(2, 1)
        self.setLayout(self.grid)

        self.setting_stack = QStackedWidget()
        self.grid.addWidget(self.setting_stack, 1, 0)

        self.category_settings_container = QWidget()
        self.category_settings_layout = QGridLayout(self.category_settings_container)
        self.setting_stack.addWidget(self.category_settings_container)
        category_help_label = QLabel()
        category_help_label.setWordWrap(True)
        category_help_label.setText('<h3>Kategorie Einstellungen</h3>Hier können Kategorien erstellt, umbenannt oder gelöscht werden.<h4>Kategorie erstellen</h4>In das Feld mit der Bezeichnung <b>Kategoriename</b> den gewünschten Namen eintragen<br>und auf den Knopf <b>Kategorie erstellen</b> klicken.<h4>Kategorie umbennenen</h4>Die gewünschte Kategorie aus dem Dropdownmenü auswählen,<br>den neuen Namen in des Feld Kategorienamen eintragen und auf den Knopf <b>Kategorie umbennenen</b> klicken.<h4>Kategorie löschen</h4>Gewünschte Kategorie aus dem Dropdownmenü auswählen<br> und auf den Knopf <b>Kategorie löschen</b> klicken.<br><b>Funktioniert nur bei Kategorien, die keine Unterkategorie haben</b>.<h4>Sub-Kategorie anlegen</h4>Im Dropdownmenü <b>Kategorien</b> die gewünschte Hauptkategorie auswählen, anschließend im Feld <b>Sub-Kategorie Name</b> den Namen der neuen Kategorie eintragen und mit einem Klick auf den Knopf <b>Subkategorie anlegen</b> bestätigen.<h4>Subkategorie umbennen</h4>Die gewünschte Subkategorie mithilfe der Dropdownmenüs auswählen, den neuen Namen im Feld <b>Sub-Kategorie name</b> eintragen und mit einem Klick auf den Knopf <b>Subkategorie umbennen</b> bestätigen.<h4>Subkategorie löschen</h4> Die zu löschende Subkategorie mithilfe der Dropdownmenüs auswählen und anschließend mit einem Klick auf den Knopf <b>Subkategorie löschen</b> bestätigen. <b>Wichtig: Funktioniert nur bei Subkategorien denen noch keine Ausgabe zugeordnet ist.</b>')

        self.category_settings_layout.addWidget(category_help_label, 0, 0)
        self.category_settings_layout.setRowStretch(1, 1)

        self.payment_settings_container = QWidget()
        self.payment_settings_layout = QGridLayout(self.payment_settings_container)
        self.setting_stack.addWidget(self.payment_settings_container)
        payment_help_label = QLabel()
        payment_help_label.setWordWrap(True)
        payment_help_label.setText('<h3>Bezahlmethoden Einstellungen</h3>Hier können Bezahlmethoden erstellt, umbenannt oder gelöscht werden.<h4>Bezahlmethode erstellen</h4>Namen der neuen Bezahlmethode im Feld <b>Bezahlmethoden Bez</b> eintragen und mit einem Klick auf den Knopf <b>Bezahlmethode anlegen</b> bestätigen.<h4>Bezahlmethode umebennenen</h4>Gewünschte Bezahlmethode im Dropdownmenü auswählen, den neuen Namen in dem Feld <b>Bezahlmethoden Bez.</b> eintragen und mit einem Klick auf den Knopf <b>Bezahlmethode umbennen</b> bestätigen.<h4>Bezahlmethode löschen</h4>Gewünschte Bezahlmethode aus dem Dropdownmenü auswählen und mit einem Klick auf den Knopf <b>Bezahlmethode löschen</b> bestätigen.<b>Wichtig: Funktioniert nur mit Bezahlmethoden, denen noch keine Ausgabe zugeordnet ist.</b>')
 
        self.payment_settings_layout.addWidget(payment_help_label, 0, 0)
        self.payment_settings_layout.setRowStretch(1, 1)

        self.export_settings_container = QWidget()
        self.export_settings_layout = QGridLayout(self.export_settings_container)
        self.setting_stack.addWidget(self.export_settings_container)
        export_help_label = QLabel()
        export_help_label.setWordWrap(True)
        export_help_label.setText('<h3>Daten Export</h3>Hier können die Datenbank oder einzelne Tabellen in unterschiedliche Formate exportiert werden.<h4>Export DB -> JSON</h4>Exportiert den gesammten Inhalt der Datenbank als JSON-String<h4>Export Ausgaben -> CSV</h4>Exportiert die Tabelle <b>expense</b> als CSV Datei.<h4>Export Kategorien -> CSV</h4>Exportiert die Tabelle <b>category</b> als CSV Datei.<h4>Export Bezahlmethoden</h4> Exportiert die Tabelle <b>payment_method</b> als CSV Datei.') 
        self.export_settings_layout.addWidget(export_help_label, 0, 0)
        self.export_settings_layout.setRowStretch(1, 1)

class SettingForm(QWidget):
    def __init__(self, setting_screen: SettingsScreen, parent=None):
        super().__init__(parent)

        self.setting_screen = setting_screen

        self.grid = QGridLayout()
        self.grid.setContentsMargins(8, 8, 8, 8)
        self.grid.setHorizontalSpacing(10)
        self.grid.setVerticalSpacing(6)

        self.settings_menu_container = QWidget()
        self.settings_menu_layout = QGridLayout(self.settings_menu_container)
        self.grid.addWidget(self.settings_menu_container, 0, 0, 1, 1)

        self.settings_menu_layout.addWidget(QLabel('<b>Einstellungen</b>'), 0, 0, 1, 2)

        self.btn_category_settings = QPushButton("Kategorien bearbeiten")
        self.settings_menu_layout.addWidget(self.btn_category_settings , 1, 0, 1, 2)
        self.btn_category_settings.clicked.connect(self.show_category_settings)

        self.btn_payment_settings = QPushButton("Bezahlmethoden bearbeiten")
        self.settings_menu_layout.addWidget(self.btn_payment_settings , 2, 0, 1, 2)
        self.btn_payment_settings.clicked.connect(self.show_payment_settings)

        self.btn_export_settings = QPushButton("Daten Exportieren")
        self.settings_menu_layout.addWidget(self.btn_export_settings, 3, 0, 1, 2)
        self.btn_export_settings.clicked.connect(self.show_export_settings)

        self.setting_stack = QStackedWidget()
        self.grid.addWidget(self.setting_stack, 4, 0)
        self.category_settings_container = QWidget()
        self.category_settings_layout = QGridLayout(self.category_settings_container)
        self.setting_stack.addWidget(self.category_settings_container)
        
        self.category_settings_layout.addWidget(QLabel('<b>Kategorien bearbeiten</b>'), 0, 0)
        self.category_settings_layout.addWidget(QLabel('Kategorien'), 1, 0, alignment=Qt.AlignRight)
        self.combo_category = QComboBox()
        self.category_settings_layout.addWidget(self.combo_category, 1, 1, 1, 1)
        self.category_settings_layout.addWidget(QLabel('Kategorie-Name'), 2, 0, alignment=Qt.AlignRight)
        self.category_name_input = QLineEdit()
        self.category_settings_layout.addWidget(self.category_name_input, 2, 1, 1, 1)
        self.btn_create_category = QPushButton("Kategorie anlegen")
        self.category_settings_layout.addWidget(self.btn_create_category, 3, 0, 1, 2)
        self.btn_update_category = QPushButton("Kategorie umbennenen")
        self.category_settings_layout.addWidget(self.btn_update_category, 4, 0, 1, 2)
        self.btn_delete_category = QPushButton("Kategorie löschen")
        self.category_settings_layout.addWidget(self.btn_delete_category, 5, 0, 1, 2)
 
        self.category_settings_layout.addWidget(QLabel('Sub-Kategorien'), 6, 0, 1, 1, alignment=Qt.AlignRight)
        self.combo_subcategory = QComboBox()
        self.category_settings_layout.addWidget(self.combo_subcategory, 6, 1, 1, 1)
        self.category_settings_layout.addWidget(QLabel('Sub-Kategorie Name'), 7, 0, alignment=Qt.AlignRight)
        self.subcategory_name_input = QLineEdit()
        self.category_settings_layout.addWidget(self.subcategory_name_input, 7, 1, 1, 1)
        self.btn_create_subcategory = QPushButton("Sub-Kategorie anlegen")
        self.category_settings_layout.addWidget(self.btn_create_subcategory, 8, 0, 1, 2)
        self.btn_update_subcategory = QPushButton("Sub-Kategorie umbennenen")
        self.category_settings_layout.addWidget(self.btn_update_subcategory, 9, 0, 1, 2)
        self.btn_delete_subcategory = QPushButton("Sub-Kategorie löschen")
        self.category_settings_layout.addWidget(self.btn_delete_subcategory, 10, 0, 1, 2)

        self.payment_settings_container = QWidget()
        self.payment_settings_layout = QGridLayout(self.payment_settings_container )
        self.setting_stack.addWidget(self.payment_settings_container)
 
        self.payment_settings_layout.addWidget(QLabel('<b>Bezahlmethoden bearbeiten</b>'), 0, 0)
        self.payment_settings_layout.addWidget(QLabel('Bezahlmethoden'), 1, 0, 1, 1, alignment=Qt.AlignRight)
        self.combo_payment = QComboBox()
        self.payment_settings_layout.addWidget(self.combo_payment, 1, 1, 1, 1)
        self.payment_settings_layout.addWidget(QLabel('Bezahlmethode Bez.'), 2, 0, alignment=Qt.AlignRight)
        self.payment_name_input = QLineEdit()
        self.payment_settings_layout.addWidget(self.payment_name_input, 2, 1, 1, 1)
        self.btn_create_payment = QPushButton("Bezahlmethode anlegen")
        self.payment_settings_layout.addWidget(self.btn_create_payment , 3, 0, 1, 2)
        self.btn_update_payment = QPushButton("Bezahlmethode umbennenen")
        self.payment_settings_layout.addWidget(self.btn_update_payment, 4, 0, 1, 2)
        self.btn_delete_payment = QPushButton("Bezahlmethode löschen")
        self.payment_settings_layout.addWidget(self.btn_delete_payment , 5, 0, 1, 2)
        self.payment_settings_layout.setRowStretch(6, 1)

        self.export_settings_container = QWidget()
        self.export_settings_layout = QGridLayout(self.export_settings_container )
        self.setting_stack.addWidget(self.export_settings_container)

        self.export_settings_layout.addWidget(QLabel('<b>Daten Exportieren</b>'), 0, 0)
        self.btn_export_db_json = QPushButton("Export DB -> JSON")
        self.export_settings_layout.addWidget(self.btn_export_db_json, 1, 0, 1, 2)
        self.btn_export_exp_csv = QPushButton("Export Ausgaben -> CSV")
        self.export_settings_layout.addWidget(self.btn_export_exp_csv, 2, 0, 1, 2)
        self.btn_export_cat_csv = QPushButton("Export Kategorien -> CSV")
        self.export_settings_layout.addWidget(self.btn_export_cat_csv, 3, 0, 1, 2)
        self.btn_export_pay_csv = QPushButton("Export Bezahlmethoden -> CSV")
        self.export_settings_layout.addWidget(self.btn_export_pay_csv, 4, 0, 1, 2)
        self.export_settings_layout.setRowStretch(5, 1)

        self.setLayout(self.grid)
        self.grid.setRowStretch(5, 1)
        self.btn_export_db_json.clicked.connect(self.db_export_json)
        self.btn_export_exp_csv.clicked.connect(self.exp_export_csv)
        self.btn_export_cat_csv.clicked.connect(self.cat_export_csv)
        self.btn_export_pay_csv.clicked.connect(self.pay_export_csv)

    def change_parent_category(self, index) -> None:
        self.combo_subcategory.clear()
        parent_category = self.combo_category.currentData()
        subcategory_list = json.loads(xtra_api.subcategory_list(json.dumps({'id': parent_category['id']})))
        for subcategory in subcategory_list:
            self.combo_subcategory.addItem(subcategory['name'], subcategory)

    def show_category_settings(self) -> None:
        self.setting_stack.setCurrentIndex(0)
        self.setting_screen.setting_stack.setCurrentIndex(0)

    def show_payment_settings(self) -> None:
        self.setting_stack.setCurrentIndex(1)
        self.setting_screen.setting_stack.setCurrentIndex(1)

    def show_export_settings(self) -> None:
        self.setting_stack.setCurrentIndex(2)
        self.setting_screen.setting_stack.setCurrentIndex(2)

    def db_export_json(self) -> bool:
        res = xtra_api.db_export_json()
        if res:
            QMessageBox.information(self, "Export Erfolgreich", f'Dein Export liegt unter\nEXTRAVERZEICHNIS/exports/{res} für dich bereit.')
            return True
        QMessageBox.warning(self, "Export Fehlgeschlagen", f'Dein Export ist leider Fehlgeschlagen.')
        return False

    def exp_export_csv(self) -> bool:
        res = xtra_api.expense_export_csv()
        if res:
            QMessageBox.information(self, "Export Erfolgreich", f'Dein Export liegt unter\nEXTRAVERZEICHNIS/exports/{res} für dich bereit.')
            return True
        QMessageBox.warning(self, "Export Fehlgeschlagen", f'Dein Export ist leider Fehlgeschlagen.')
        return False

    def cat_export_csv(self) -> bool:
        res = xtra_api.category_export_csv()
        if res:
            QMessageBox.information(self, "Export Erfolgreich", f'Dein Export liegt unter\nEXTRAVERZEICHNIS/exports/{res} für dich bereit.')
            return True
        QMessageBox.warning(self, "Export Fehlgeschlagen", f'Dein Export ist leider Fehlgeschlagen.')
        return False

    def pay_export_csv(self) -> bool:
        res = xtra_api.payment_method_export_csv()
        if res:
            QMessageBox.information(self, "Export Erfolgreich", f'Dein Export liegt unter EXTRAVERZEICHNIS/exports{res} für dich bereit.')
            return True
        QMessageBox.warning(self, "Export Fehlgeschlagen", f'Dein Export ist leider Fehlgeschlagen.')
        return False

class StatForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #profile_info = json.loads(xtra_api.profile_info())
        grid = QGridLayout()
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(6)

        grid.addWidget(QLabel('<b>Statistiken</b>'), 0, 0, 1, 2)

        grid.addWidget(QLabel('Jahr:'), 1, 0, 1, 1)
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText('yyyy')
        validator = QIntValidator(1000, 3000, self.year_input)
        self.year_input.setValidator(validator)
        grid.addWidget(self.year_input, 1, 1, 1, 1)
        self.btn_sum_per_month = QPushButton("Ausgaben/Monat")
        grid.addWidget(self.btn_sum_per_month, 2, 0, 1, 2)
        self.btn_sum_per_category = QPushButton("Ausgaben/Kategorie")
        grid.addWidget(self.btn_sum_per_category, 3, 0, 1, 2)
        grid.setRowStretch(4, 1)
        self.setLayout(grid)
    def plot_category_expense_bars(self) -> bytes:
        year = self.year_input.text()
        res = xtra_api.plot_category_expense_png(json.dumps({'year': year}))
        return res
    def plot_monthly_expense_bars(self) -> bytes:
        year = self.year_input.text()
        res = xtra_api.plot_monthly_expense_png(json.dumps({'year': year}))
        return res

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Extra - A simple expense tracker")
        self.resize(1200, 800)
        self.config_dict = json.loads(xtra_api.load_config())
        xtra_api.switch_db(json.dumps({'name': self.config_dict['active_profile']}))

        toolbar = self.addToolBar('main_toolbar')
        toolbar.setIconSize(QSize(16, 16))

        expense_action = QAction("Ausgaben", self)
        expense_action.triggered.connect(self.main_screen)
        toolbar.addAction(expense_action)

        profile_action = QAction("Profil", self)
        profile_action.triggered.connect(self.profile_screen)
        toolbar.addAction(profile_action)

        settings_action = QAction("Einstellungen", self)
        settings_action.triggered.connect(self.setting_screen)
        toolbar.addAction(settings_action)

        stats_action = QAction("Statistik", self)
        stats_action.triggered.connect(self.stat_screen)
        toolbar.addAction(stats_action)

        about_act = QAction("Über", self)
        about_act.triggered.connect(self.about)
        toolbar.addAction(about_act)

        self.setStatusBar(QWidget().parentWidget())  # leere Statusbar-Placeholder
        self.statusBar().showMessage(f'Profil: {self.config_dict['active_profile']}')
        # Zentrales Widget und Haupt-Grid
        central = QWidget()
        grid = QGridLayout(central)
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setSpacing(10)

        self.left_stack = QStackedWidget()
        self.right_stack = QStackedWidget()

        grid.addWidget(self.left_stack, 0, 0)
        grid.addWidget(self.right_stack, 0, 1)

        self.left_main_container = QWidget()
        self.left_main_layout = QGridLayout(self.left_main_container)

        self.expense_insert_form = ExpenseInsertForm()
        self.expense_update_form = ExpenseUpdateForm()
        self.expense_filter_form = ExpenseFilterForm()

        # Update and Insert Form Share the same spot. Visibility needs to
        # be toggled.
        self.expense_update_form.hide()

        self.left_main_layout.addWidget(self.expense_insert_form, 0, 0)
        self.left_main_layout.addWidget(self.expense_update_form, 0, 0)
        self.left_main_layout.addWidget(self.expense_filter_form, 1, 0)
        self.left_stack.addWidget(self.left_main_container)

        self.right_main_container = QWidget()
        self.right_main_layout = QGridLayout(self.right_main_container)
        self.expense_table = ExpenseTable()
        self.right_main_layout.addWidget(self.expense_table, 0, 0)
        self.right_stack.addWidget(self.right_main_container)

        self.left_profile_container = QWidget()
        self.left_profile_layout = QGridLayout(self.left_profile_container)
        self.profile_form = ProfileForm()
        self.left_profile_layout.addWidget(self.profile_form, 0, 0)
        self.left_stack.addWidget(self.left_profile_container)

        self.right_profile_container = QWidget()
        self.right_profile_layout = QGridLayout(self.right_profile_container)
        self.profile_details = ProfileDetails()
        self.right_profile_layout.addWidget(self.profile_details, 0, 0)
        self.right_stack.addWidget(self.right_profile_container)

        self.left_stats_container = QWidget()
        self.left_stats_layout = QGridLayout(self.left_stats_container)
        self.stat_form = StatForm()
        self.left_stats_layout.addWidget(self.stat_form, 0, 0)
        self.left_stack.addWidget(self.left_stats_container)

        self.right_stats_container = QWidget()
        self.right_stats_layout = QGridLayout(self.right_stats_container)
        self.diagram_screen = DiagramScreen()
        self.right_stats_layout.addWidget(self.diagram_screen, 0, 0)
        self.right_stack.addWidget(self.right_stats_container)

        self.right_settings_container = QWidget()
        self.right_settings_layout = QGridLayout(self.right_settings_container)
        self.settings_screen = SettingsScreen()
        self.right_settings_layout.addWidget(self.settings_screen, 0, 0)
        self.right_stack.addWidget(self.right_settings_container)

        self.left_settings_container = QWidget()
        self.left_settings_layout = QGridLayout(self.left_settings_container)
        self.settings_form = SettingForm(self.settings_screen)
        self.left_settings_layout.addWidget(self.settings_form, 0, 0)
        self.left_stack.addWidget(self.left_settings_container)

        # Buttons - Profile related
        self.profile_form.btn_switch_profile.clicked.connect(self.switch_profile)
        self.profile_form.btn_create_profile.clicked.connect(self.create_profile)
        self.profile_form.btn_delete_profile.clicked.connect(self.delete_profile)
        self.profile_form.btn_close_menu.clicked.connect(self.main_screen)

        # Buttons - Settings related
        self.settings_form.btn_create_category.clicked.connect(self.create_category)
        self.settings_form.btn_create_subcategory.clicked.connect(self.create_subcategory)
        self.settings_form.btn_create_payment.clicked.connect(self.create_payment_method)
        self.settings_form.btn_delete_payment.clicked.connect(self.delete_payment_method)
        self.settings_form.btn_delete_category.clicked.connect(self.delete_category)
        self.settings_form.btn_delete_subcategory.clicked.connect(self.delete_subcategory)
        self.settings_form.btn_update_payment.clicked.connect(self.update_payment_method)
        self.settings_form.btn_update_category.clicked.connect(self.update_category)
        self.settings_form.btn_update_subcategory.clicked.connect(self.update_subcategory)

        # Buttons - Expense Filter related 
        self.expense_filter_form.btn_search_expense.clicked.connect(self.get_expense_list)

        # Interactive Table Cells
        self.expense_table.expense_table.cellClicked.connect(self.click_expense_table_cell)

        # Update Form Buttons
        self.expense_update_form.btn_abort_update.clicked.connect(self.abort_expense_update)
        self.expense_update_form.btn_update_expense.clicked.connect(self.update_expense)

        # Diagram Buttons
        self.stat_form.btn_sum_per_month.clicked.connect(self.draw_sum_per_month)
        self.stat_form.btn_sum_per_category.clicked.connect(self.draw_sum_per_category)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 3)
        self.setCentralWidget(central)
        self.init_comboboxes()

    def draw_sum_per_category(self) -> bool:
        #print(self.stat_form.year_input.text())
        if not self.stat_form.year_input.hasAcceptableInput() or self.stat_form.year_input.text() == '':
            QMessageBox.warning(self, 'Warnung', 'Bitte geben sie ein gültiges Jahr ein. Format: yyyy')
            return False
        res = self.stat_form.plot_category_expense_bars()
        if not res:
            QMessageBox.warning(self, 'Warnung', 'Keine Daten in diesem Jahr vorhanden.')
            return False
        self.diagram_screen.pixmap_image(res)
        return True

    def draw_sum_per_month(self) -> bool:
        if not self.stat_form.year_input.hasAcceptableInput() or self.stat_form.year_input.text() == '':
            QMessageBox.warning(self, 'Warnung', 'Bitte geben sie ein gültiges Jahr ein. Format: yyyy')
            return False
        res = self.stat_form.plot_monthly_expense_bars()
        if not res:
            QMessageBox.warning(self, 'Warnung', 'Keine Daten in diesem Jahr vorhanden.')
            return False
        self.diagram_screen.pixmap_image(res)
        return True
 
    def about(self) -> None:
        QMessageBox.information(self, "Extra - A simple Expense Tracker", f'Behalte die Übersicht über deine Ausgaben.\nVon: Oguzhan Karaca, Marzieh Rayatzadeh und Timo Röhle')

    def update_subcategory(self) -> bool:
        subcategory = self.settings_form.combo_subcategory.currentData()
        subcategory_name = self.settings_form.subcategory_name_input.text()
        if subcategory_name == '':
            QMessageBox.warning(self, "Ungültiger Name", f'Bitte geben sie einen gültigen Namen für diese Kategorie ein.')
            return False
        confirmation = self.confirmation_dialog('Kategorie umbennenen', f'Die Kategorie {subcategory['name']} wird umbenannt in {subcategory_name} sind sie sicher?')
        if not confirmation:
            return False
        res = xtra_api.update_category(json.dumps({'id': subcategory['id'], 'name': subcategory_name, 'parent_id': subcategory['parent_id']}))
        if json.loads(res):
            QMessageBox.information(self, "Kategorie umbenannt", f'Die Kategorie {subcategory['name']} wurde umbennant in {subcategory_name}')
        self.settings_form.subcategory_name_input.setText('')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def update_category(self) -> bool:
        category = self.settings_form.combo_category.currentData()
        category_name = self.settings_form.category_name_input.text()
        if category_name == '':
            QMessageBox.warning(self, "Ungültiger Name", f'Bitte geben sie einen gültigen Namen für diese Kategorie ein.')
            return False
        confirmation = self.confirmation_dialog('Kategorie umbennenen', f'Die Kategorie {category['name']} wird umbenannt in {category_name} sind sie sicher?')
        if not confirmation:
            return False
        res = xtra_api.update_category(json.dumps({'id': category['id'], 'name': category_name, 'parent_id': category['parent_id']}))
        if json.loads(res):
            QMessageBox.information(self, "Kategorie umbenannt", f'Die Kategorie {category['name']} wurde umbennant in {category_name}')
        self.settings_form.category_name_input.setText('')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def update_payment_method(self) -> bool:
        payment = self.settings_form.combo_payment.currentData()
        payment_name = self.settings_form.payment_name_input.text()
        if payment_name == '':
            QMessageBox.warning(self, "Ungültiger Name", f'Bitte geben sie einen gültigen Namen für diese Bezahlmethode ein.')
            return False
        confirmation = self.confirmation_dialog('Bezahlmethode umbennenen', f'Die Bezahlmethode {payment['name']} wird umbenannt in {payment_name} sind sie sicher?')
        if not confirmation:
            return False
        res = xtra_api.update_payment_method(json.dumps({'id': payment['id'], 'name': payment_name}))
        if json.loads(res):
            QMessageBox.information(self, "Bezahlmethode umbennant", f'Die Bezahlmethode {payment['name']} wurde umbennant in {payment_name}')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def delete_subcategory(self) -> bool:
        subcategory = self.settings_form.combo_subcategory.currentData()
        #print(subcategory)
        confirmation = self.confirmation_dialog('Kategorie löschen', f'Sind sie sicher, dass sie die Kategorie {subcategory['name']} löschen möchten? Diese Aktion kann nicht rückgängig gemacht werden.')
        if not confirmation:
            return False
        res = json.loads(xtra_api.delete_category(json.dumps({'id': subcategory['id']})))
        if not res:
            QMessageBox.warning(self, "Löschen Fehlgeschlagen", f'Die Kategorie {subcategory['name']} konnte nicht gelöscht werden. Bitte stellen sie sicher, das diese Kategorie keine Ausgaben oder Unterkategorie zugeordnet sind.')
            return False
        QMessageBox.information(self, "Kategorie gelöscht", f'Die Die Kategorie {subcategory['name']} wurde gelöscht.')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def delete_category(self) -> bool:
        category = self.settings_form.combo_category.currentData()
        #print(category)
        confirmation = self.confirmation_dialog('Kategorie löschen', f'Sind sie sicher, dass sie die Kategorie {category['name']} löschen möchten? Diese Aktion kann nicht rückgängig gemacht werden.')
        if not confirmation:
            return False
        res = json.loads(xtra_api.delete_category(json.dumps({'id': category['id']})))
        if not res:
            QMessageBox.warning(self, "Löschen Fehlgeschlagen", f'Die Kategorie {category['name']} konnte nicht gelöscht werden. Bitte stellen sie sicher, das diese Kategorie keine Ausgaben oder Unterkategorie zugeordnet sind.')
            return False
        QMessageBox.information(self, "Kategorie gelöscht", f'Die Die Kategorie {category['name']} wurde gelöscht.')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def delete_payment_method(self) -> bool:
        payment = self.settings_form.combo_payment.currentData()
        confirmation = self.confirmation_dialog('Bezahlmethode löschen', f'Sind sie sicher, dass sie die Bezahlmethode {payment['name']} löschen möchten? Diese Aktion kann nicht rückgängig gemacht werden.')
        if not confirmation:
            return False
        res = json.loads(xtra_api.delete_payment_method(json.dumps({'id': payment['id']})))
        if not res:
            QMessageBox.warning(self, "Löschen Fehlgeschlagen", f'Die Bezahlmethode {payment['name']} konnte nicht gelöscht werden. Bitte stellen sie sicher, das keine Ausgaben dieser Bezahlmethode zugeordnet sind.')
            return False
        QMessageBox.information(self, "Bezahlmethode gelöscht", f'Die Bezahlmethode {payment['name']} wurde gelöscht.')
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def create_payment_method(self) -> bool:
        payment_name = self.settings_form.payment_name_input.text()
        if payment_name == '':
            QMessageBox.warning(self, "Ungültiger Name", 'Bitte geben sie einen gültigen Namen für die neue Bezahlmethode ein.')
            return False
        res = xtra_api.insert_payment_method(json.dumps({'name': payment_name}))
        QMessageBox.information(self, "Neue Bezahlmethode angelegt", f'Eine neue Bezahlmethode mit dem Namen: {payment_name} wurde angelegt.')
        self.settings_form.payment_name_input.setText('')
        payment_methods = xtra_api.payment_method_list()
        payment_method_list = json.loads(payment_methods)
        self.disconnect_category_combo()
        self.init_comboboxes()
        return True

    def create_subcategory(self):
        subcategory_name = self.settings_form.subcategory_name_input.text()
        if subcategory_name == '':
            QMessageBox.warning(self, "Ungültiger Name", 'Bitte geben sie einen gültigen Kategorienamen an.')
            return False
        parent_category = self.settings_form.combo_category.currentData()
        create_cat = {
            'name': subcategory_name,
            'parent_category_id': parent_category['id']
        }
        res = xtra_api.insert_category(json.dumps(create_cat))
        res_dict = json.loads(res)
        QMessageBox.information(self, "Neue SubKategorie erstellt", f'In der Kategorie {parent_category['name']} wurde die neue Sub-Kategorie {subcategory_name} erstellt.')
        self.settings_form.subcategory_name_input.setText('')
        self.disconnect_category_combo()
        self.init_comboboxes()

    def create_category(self):
        category_name = self.settings_form.category_name_input.text()
        if category_name == '':
            QMessageBox.warning(self, "Ungültiger Name", 'Bitte geben sie einen gültigen Kategorienamen an.')
            return False
        res = xtra_api.insert_category(json.dumps({'name': category_name}))
        #inserted_category = json.loads(res)
        self.disconnect_category_combo()
        self.init_comboboxes()
        QMessageBox.information(self, "Neue Kategorie angelegt", f'Eine neue Kategorie mit dem Namen: {category_name} wurde angelegt.')
        self.settings_form.category_name_input.setText('')

    def confirmation_dialog(self, title="Sicher?", text="Möchten Sie fortfahren?") -> bool:
        delete_alert = QMessageBox()
        delete_alert.setWindowTitle(title)
        delete_alert.setText(text)
        delete_alert.setIcon(QMessageBox.Warning)
        yes = delete_alert.addButton(QMessageBox.Yes)
        yes.setText('Fortfahren')
        no = delete_alert.addButton(QMessageBox.No)
        no.setText('Abbrechen')
        delete_alert.setDefaultButton(QMessageBox.No)
        result = delete_alert.exec()
        return result == QMessageBox.Yes

    def delete_profile(self) -> bool:
        config_dict = json.loads(xtra_api.load_config())

        profile = self.profile_form.combo_profile.currentText()
        if config_dict['active_profile'] == profile:
            QMessageBox.warning(self, "Warnung", f"Profil {profile} ist gerade aktiv und kann nicht gelöscht werden. Sie können nur Profile löschen die im Augenblick nicht aktiv sind.")
            return False

        confirmation = self.confirmation_dialog('Profil löschen', f'Profil {profile} wird unwiderbringlich gelöscht. Sind sie sicher?')
        if not confirmation:
            return False

        res = xtra_api.delete_db(profile)
        if json.loads(res):
            QMessageBox.information(self, "Profil gelöscht", f"Profil {profile} wurde gelöscht")
            combo_index = self.profile_form.combo_profile.findText(profile)
            if combo_index > -1:
                self.profile_form.combo_profile.removeItem(combo_index)
        return True

    def create_profile(self):
        profile_name = self.profile_form.profile_name_input.text()
        # TODO
        # For the demo this is good enough. But here should be more checks to make sure,
        # the profile_name is valid.
        if profile_name == '':
            QMessageBox.warning(self, "Warnung", "Bitte gib einen gültigen Profilnamen ein")
            return False
        res = xtra_api.create_db(json.dumps({'name': profile_name}))
        res_dict = json.loads(res)
        if res_dict['success'] == 'db created':
            QMessageBox.information(self, "Neues Profil erstellt", f"Neues Profil {profile_name} wurde erstellt.")
            self.profile_form.combo_profile.addItem(profile_name, f'databases/{profile_name}')

    def disconnect_category_combo(self) -> None:
        self.expense_insert_form.combo_category.currentIndexChanged.disconnect()
        self.expense_update_form.combo_category.currentIndexChanged.disconnect()
        self.settings_form.combo_category.currentIndexChanged.disconnect()

    def init_comboboxes(self) -> None:
        self.expense_insert_form.combo_category.clear()
        self.expense_insert_form.combo_subcategory.clear()
        self.expense_insert_form.combo_payment.clear()
        self.expense_update_form.combo_category.clear()
        self.expense_update_form.combo_subcategory.clear()
        self.expense_update_form.combo_payment.clear()
        self.settings_form.combo_category.clear()
        self.settings_form.combo_subcategory.clear()
        self.settings_form.combo_payment.clear()
        parent_category_list = json.loads(xtra_api.parent_category_list())
        for parent_category in parent_category_list:
            self.expense_insert_form.combo_category.addItem(parent_category['name'], parent_category)
            self.expense_update_form.combo_category.addItem(parent_category['name'], parent_category)
            self.settings_form.combo_category.addItem(parent_category['name'], parent_category)
        choosen_category = self.settings_form.combo_category.currentData()
        subcategory_list = json.loads(xtra_api.subcategory_list(json.dumps({'id': choosen_category['id']})))
        for subcategory in subcategory_list:
            self.expense_insert_form.combo_subcategory.addItem(subcategory['name'], subcategory)
            self.expense_update_form.combo_subcategory.addItem(subcategory['name'], subcategory)
            self.settings_form.combo_subcategory.addItem(subcategory['name'], subcategory)
        payment_method_list = json.loads(xtra_api.payment_method_list())
        for payment_method in payment_method_list:
            self.expense_insert_form.combo_payment.addItem(payment_method['name'], payment_method)
            self.expense_update_form.combo_payment.addItem(payment_method['name'], payment_method)
            self.settings_form.combo_payment.addItem(payment_method['name'], payment_method)
        self.settings_form.combo_category.currentIndexChanged.connect(self.settings_form.change_parent_category)
        self.expense_insert_form.combo_category.currentIndexChanged.connect(self.expense_insert_form.change_parent_category)
        self.expense_update_form.combo_category.currentIndexChanged.connect(self.expense_update_form.change_parent_category)

    def switch_profile(self) -> None:
        self.config_dict['active_profile'] = self.profile_form.combo_profile.currentText()
        self.statusBar().showMessage(f'Profil: {self.config_dict['active_profile']}')
        xtra_api.switch_db(json.dumps({'name': self.config_dict['active_profile']}))
        xtra_api.save_config(json.dumps(self.config_dict))
        self.disconnect_category_combo()
        self.init_comboboxes()
        self.profile_details.update_detail_list()

    def main_screen(self) -> None:
        self.left_stack.setCurrentIndex(0)
        self.right_stack.setCurrentIndex(0)

    def profile_screen(self) -> None:
        self.left_stack.setCurrentIndex(1)
        self.right_stack.setCurrentIndex(1)

    def stat_screen(self) -> None:
        self.left_stack.setCurrentIndex(2)
        self.right_stack.setCurrentIndex(2)

    def setting_screen(self) -> None:
        self.left_stack.setCurrentIndex(3)
        self.right_stack.setCurrentIndex(3)

    def abort_expense_update(self) -> None:
        self.expense_update_form.hide()
        self.expense_insert_form.show()

    def get_expense_list(self) -> None:
        res = self.expense_filter_form.search_expense()
        self.expense_table.render_table(res)

    def click_expense_table_cell(self, row, column) -> None:
        cell = self.expense_table.expense_table.item(row, column)
        cell_data = cell.data(Qt.UserRole)
        if column == 4:
            note = cell_data.get('note')
            self.expense_table.note_display.setText(note)
        if column == 5:
            self.expense_insert_form.hide()
            self.expense_update_form.show()
            self.init_update_inputs(cell_data['edit'])
        if column == 6:
            delitem = cell_data.get('delete')
            confirm_title = 'Ausgabe löschen?'
            confirm_text = f'Soll die Ausgabe vom {delitem['date']} aus der Kategorie {delitem['category']['name']} wirklick permanent gelöscht werden?'
            delete_confirmed = self.confirmation_dialog(confirm_title, confirm_text)
            if not delete_confirmed:
                return False
            delete_res = xtra_api.delete_expense(json.dumps(delitem))
            # TODO: HANDLE ERROR and DELETE CONFIRMATION HERE.
            self.expense_table.expense_table.removeRow(row)

    def init_update_inputs(self, data) -> None:
        combo_category = self.expense_update_form.combo_category
        category_data = self.expense_update_form.combo_category.currentData()
        cat_index = -1
        for i in range(combo_category.count()):
            combo_data = combo_category.itemData(i)
            if combo_data['id'] == data['category']['parent_category']:
                cat_index = i
                break
        #print(cat_index)
        combo_category.setCurrentIndex(cat_index)

        combo_subcategory = self.expense_update_form.combo_subcategory
        subcat_index = -1
        for i in range(combo_category.count()):
            combo_data = combo_subcategory.itemData(i)
            if combo_data['id'] == data['category']['id']:
                subcat_index = i
                break
        combo_subcategory.setCurrentIndex(subcat_index)

        combo_payment = self.expense_update_form.combo_payment
        payment_index = -1
        for i in range(combo_payment.count()):
            combo_data = combo_payment.itemData(i)
            if combo_data['id'] == data['payment_method']['id']:
                payment_index = i
                break
        combo_payment.setCurrentIndex(payment_index)

        self.expense_update_form.id_input.setText(str(data['id']))
        self.expense_update_form.amount_input.setText(str(data['amount']))
        self.expense_update_form.note_input.setText(data['note'])
        self.expense_update_form.date_edit.setDate(QDate.fromString(data['date'], 'yyyy-MM-dd'))

    def update_expense(self) -> None:
        parsed_amount = 0
        parsed_id = int(self.expense_update_form.id_input.text())
        try:
            parsed_amount = float(self.expense_update_form.amount_input.text())
        except:
            QMessageBox.information(self, "Warnung", "Bitte geben sie einen gültigen Betrag ein.")
            return False
        combo_subcategory = self.expense_update_form.combo_subcategory
        combo_category = self.expense_update_form.combo_category
        combo_payment = self.expense_update_form.combo_payment
        expense_dict = {
            'id': parsed_id,
            'amount': parsed_amount,
            'category': combo_subcategory.currentData(),
            'payment_method': combo_payment.currentData(),
            'date': self.expense_update_form.date_edit.date().toString('yyyy-MM-dd'),
            'note': self.expense_update_form.note_input.toPlainText()
        }

        # Normaly the Expense belongs to a subcategory. Unless there is
        # no subcategory then it belongs to the main category
        if not expense_dict['category']:
            expense_dict['category'] = combo_category.currentData()
        res = xtra_api.update_expense(json.dumps(expense_dict))
        expense_updated = json.loads(res)
        if expense_updated:
            QMessageBox.information(self, "Erfolg", f"Ausgabe wurde erfolgreich geändert")
            self.expense_update_form.hide()
            self.expense_insert_form.show()
            self.get_expense_list()

def start_ui():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
