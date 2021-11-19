import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
from PyQt5 import uic

class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
       
        model = QSqlTableModel(self, db)
        model.setTable('coffee_info')
        model.select()

        self.coffeDB_tableView.setModel(model)
        self.coffeDB_tableView.move(10, 10)
        self.coffeDB_tableView.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('CoffeeDB')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())