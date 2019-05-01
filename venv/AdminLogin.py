# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminLogin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewUserRegisteration import *
from addcourse import Ui_AddCourse


class Ui_AdminLoginWindow(object):

    LoggedInUserName =''


    def __init__(self, userNameText):
        Ui_AdminLoginWindow.LoggedInUserName = userNameText

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.newUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.newUserButton.setGeometry(QtCore.QRect(20, 70, 181, 81))
        self.newUserButton.setObjectName("newUserButton")

        self.createCourseButton = QtWidgets.QPushButton(self.centralwidget)
        self.createCourseButton.setGeometry(QtCore.QRect(210, 70, 181, 81))
        self.createCourseButton.setObjectName("createCourseButton")

        self.courseToProfessorButton = QtWidgets.QPushButton(self.centralwidget)
        self.courseToProfessorButton.setGeometry(QtCore.QRect(400, 70, 181, 81))
        self.courseToProfessorButton.setObjectName("courseToProfessorButton")

        self.courseToStudentButton = QtWidgets.QPushButton(self.centralwidget)
        self.courseToStudentButton.setGeometry(QtCore.QRect(590, 70, 181, 81))
        self.courseToStudentButton.setObjectName("courseToStudentButton")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 181, 81))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 200, 31))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.newUserButton.clicked.connect(lambda :(self.newUserWindow()))

        self.createCourseButton.clicked.connect(lambda: (self.addCourseWindow()))


    def addCourseWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddCourse()
        self.ui.setupUi(self.window)
        self.window.show()

    def newUserWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewUserRegisteration()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdminLogin"))
        self.newUserButton.setText(_translate("MainWindow", "New User Registeration"))
        self.createCourseButton.setText(_translate("MainWindow", "Create Course"))
        self.courseToProfessorButton.setText(_translate("MainWindow", "Add Course To Professor"))
        self.courseToStudentButton.setText(_translate("MainWindow", "Add Course To Student"))
        self.pushButton_5.setText(_translate("MainWindow", "Other Options"))
        self.label.setText(_translate("MainWindow", "Welcome "+ Ui_AdminLoginWindow.LoggedInUserName ))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
