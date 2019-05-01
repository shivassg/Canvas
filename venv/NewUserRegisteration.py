# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ConnectDB import *
import mysql.connector
from CommonUIUtils import *

class Ui_NewUserRegisteration(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 93, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UBIDLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.UBIDLabel.setObjectName("UBIDLabel")
        self.verticalLayout.addWidget(self.UBIDLabel)
        self.FNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.FNameLabel.setObjectName("FNameLabel")
        self.verticalLayout.addWidget(self.FNameLabel)
        self.LNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.LNameLabel.setObjectName("LNameLabel")

        self.verticalLayout.addWidget(self.LNameLabel)
        self.EmailLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.EmailLabel.setObjectName("EmailLabel")

        self.verticalLayout.addWidget(self.EmailLabel)
        self.PhoneNumberLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PhoneNumberLabel.setObjectName("PhoneNumberLabel")
        self.verticalLayout.addWidget(self.PhoneNumberLabel)

        self.UserTypeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.UserTypeLabel.setObjectName("UserTypeLabel")
        self.verticalLayout.addWidget(self.UserTypeLabel)

        self.DepartmentLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DepartmentLabel.setObjectName("DepartmentLabel")
        self.verticalLayout.addWidget(self.DepartmentLabel)

        self.UsernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.verticalLayout.addWidget(self.UsernameLabel)

        self.PasswordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.verticalLayout.addWidget(self.PasswordLabel)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 50, 160, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.UBIDLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.UBIDLine.setObjectName("UBIDLine")
        self.verticalLayout_2.addWidget(self.UBIDLine)

        self.FNameLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.FNameLine.setObjectName("FNameLine")
        self.verticalLayout_2.addWidget(self.FNameLine)

        self.LNameLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.LNameLine.setObjectName("LNameLine")
        self.verticalLayout_2.addWidget(self.LNameLine)

        self.EmailLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.EmailLine.setObjectName("EmailLine")
        self.verticalLayout_2.addWidget(self.EmailLine)

        self.PhoneNumberLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.PhoneNumberLine.setObjectName("PhoneNumberLine")
        self.verticalLayout_2.addWidget(self.PhoneNumberLine)

        #self.UserTypeLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        #self.UserTypeLine.setObjectName("UserTypeLine")
        #self.verticalLayout_2.addWidget(self.UserTypeLine)

        self.userTypeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.userTypeComboBox.setObjectName("userTypeComboBox")
        self.verticalLayout_2.addWidget(self.userTypeComboBox)
        self.userTypeComboBox.addItem("")
        self.userTypeComboBox.addItem("")
        self.userTypeComboBox.addItem("")


        self.DepartmentLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.DepartmentLine.setObjectName("DepartmentLine")
        self.verticalLayout_2.addWidget(self.DepartmentLine)

        self.UsernameLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.UsernameLine.setObjectName("UsernameLine")
        self.verticalLayout_2.addWidget(self.UsernameLine)

        self.PasswordLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.PasswordLine.setObjectName("PasswordLine")
        self.verticalLayout_2.addWidget(self.PasswordLine)

        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(210, 510, 113, 32))
        self.RegisterButton.setObjectName("RegisterButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.RegisterButton.clicked.connect(lambda: (self.saveValuesToDB()))


    def saveValuesToDB(self):

        try:
            conn = ConnectDB()
            query = "INSERT INTO `users` (`UserID`, `Fname`, `Lname`, `Email`, `PhoneNum`, `UserType`, `Department`, `Username`,`Password`) " \
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            params = (self.UBIDLine.text(),self.FNameLine.text(),self.LNameLine.text(),self.EmailLine.text()
                      ,self.PhoneNumberLine.text(),self.userTypeComboBox.currentText().__str__(),self.DepartmentLine.text(),self.UsernameLine.text(),self.PasswordLine.text())

            conn.execute(query,params)
            CommonUIUtils.showSuccessMessage("User Registered Successfully!!")


        except mysql.connector.IntegrityError as err:
            print("Error:{}".format(err))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New User"))
        self.label.setText(_translate("MainWindow", "New User Registeration"))
        self.UBIDLabel.setText(_translate("MainWindow", "UB ID"))
        self.FNameLabel.setText(_translate("MainWindow", "First Name"))
        self.LNameLabel.setText(_translate("MainWindow", "LastName"))
        self.EmailLabel.setText(_translate("MainWindow", "Email"))
        self.PhoneNumberLabel.setText(_translate("MainWindow", "Phone Number"))
        self.UserTypeLabel.setText(_translate("MainWindow", "User Type"))
        self.userTypeComboBox.setItemText(0, _translate("MainWindow", "Student"))
        self.userTypeComboBox.setItemText(1, _translate("MainWindow", "Professor"))
        self.userTypeComboBox.setItemText(2, _translate("MainWindow", "Admin"))

        self.DepartmentLabel.setText(_translate("MainWindow", "Department"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.RegisterButton.setText(_translate("MainWindow", "Register"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
