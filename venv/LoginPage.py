# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewUserRegisteration import *
from AdminLogin import *
from ConnectDB import *
from CommonUIUtils import *
from CommonUtils import *

class Ui_LoginPage(object):



    def checkLogin(self, userNameText, passwordText ):
        print("Checking Username and Password")
        conn = ConnectDB()

        checkLogin = CommonUtils.checkLogin(userNameText.text(),passwordText.text())
        if not checkLogin:
            CommonUIUtils.showWarningMessageBox("Incorrect Username or Password")
        else:
            userType = CommonUtils.getUserTypeFromUserName(userNameText.text())
            if userType == 'Admin' :
                firstName = CommonUtils.getFnameFromUserName(userNameText.text())
                self.openAdminLoginWindow(firstName)


    def openAdminLoginWindow(self, firstNameText):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminLoginWindow(firstNameText)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(791, 485)
        LoginPage.setStyleSheet("background-image:url(image.png)")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.Username = QtWidgets.QLabel(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(260, 210, 66, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.Username.sizePolicy().hasHeightForWidth())
        self.Username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(260, 250, 64, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Usernametext = QtWidgets.QLineEdit(self.centralwidget)
        self.Usernametext.setGeometry(QtCore.QRect(330, 210, 125, 21))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Usernametext.sizePolicy().hasHeightForWidth())

        self.Usernametext.setSizePolicy(sizePolicy)
        self.Usernametext.setObjectName("Usernametext")

        self.Passwordtext = QtWidgets.QLineEdit(self.centralwidget)
        self.Passwordtext.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Passwordtext.setGeometry(QtCore.QRect(330, 250, 125, 21))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Passwordtext.sizePolicy().hasHeightForWidth())

        self.Passwordtext.setSizePolicy(sizePolicy)
        self.Passwordtext.setObjectName("Passwordtext")

        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(380, 290, 75, 24))
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(lambda :self.checkLogin(self.Usernametext, self.Passwordtext))
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Canvas Application"))
        self.Username.setText(_translate("LoginPage", "Username"))
        self.Password.setText(_translate("LoginPage", "Password"))
        self.Login.setText(_translate("LoginPage", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
