# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.coffeDB_tableView = QtWidgets.QTableView(Form)
        self.coffeDB_tableView.setGeometry(QtCore.QRect(10, 100, 381, 192))
        self.coffeDB_tableView.setObjectName("coffeDB_tableView")
        self.change_btn = QtWidgets.QPushButton(Form)
        self.change_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.change_btn.setObjectName("change_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.change_btn.setText(_translate("Form", "изменить"))
