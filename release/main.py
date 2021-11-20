import sys
import sqlite3
from UI.mainForm import Ui_Form1
from UI.addEditCoffeeForm import Ui_Form2
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QTableWidgetItem
from PyQt5 import uic

class Coffee(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data\\coffee.sqlite')
        db.open()
       
        model = QSqlTableModel(self, db)
        model.setTable('coffee_info')
        model.select()

        self.coffeDB_tableView.setModel(model)
        self.coffeDB_tableView.move(10, 10)
        self.coffeDB_tableView.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('CoffeeDB')
        self.change_btn.move(20, 400)
        self.change_btn.clicked.connect(self.go_to_changer)

    def go_to_changer(self):
        self.hide()
        change_db_ex.show()

class CoffeeChanger(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data\\coffee.sqlite")
        self.load_btn.clicked.connect(self.update_result)
        self.coffeeDB_tableWidget.itemChanged.connect(self.item_changed)
        self.save_btn.clicked.connect(self.save_results)
        self.modified = {}
        self.titles = None
        self.back_btn.clicked.connect(self.back_to_main_form)
        self.put_pushButton.clicked.connect(self.put_results)

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee_info WHERE id=?",
                         (item_id := self.id_spinBox.text(), )).fetchall()
        self.coffeeDB_tableWidget.setRowCount(len(result))
        try:
            self.coffeeDB_tableWidget.setColumnCount(len(result[0]))
        except:
            pass
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.coffeeDB_tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE coffee_info SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                          for key in self.modified.keys()])
            que += "WHERE id = ?"
            cur.execute(que, (self.id_spinBox.text(),))
            self.con.commit()
            self.modified.clear()
    
    def put_results(self):
        data = [self.name_lineEdit.text(), self.roasting_lineEdit.text(),
                self.smashed_lineEdit.text(), self.info_textEdit.toPlainText(), 
                self.cost_lineEdit.text(), self.volume_lineEdit.text()]
        
        for line in data:
            if line == '':
                self.error_lbl.setText('Неверные данные.')
                break
        else:
            con = sqlite3.connect('data\\coffee.sqlite')
            cur = con.cursor()
            cur.execute(f'''INSERT INTO coffee_info(coffee_name,
                        coffee_roasting, smashed_or_completed, taste_info, cost, volume)
                        VALUES("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}",
                               "{data[4]}", "{data[5]}")''')
            con.commit()
            con.close()
    
    def back_to_main_form(self):
        self.hide()
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    change_db_ex = CoffeeChanger()
    ex.show()
    sys.exit(app.exec())