# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from CommonUIUtils import *
from ConnectDB import *


class Ui_AddCourse(object):
    def setupUi(self, AddCourse):
        AddCourse.setObjectName("AddCourse")
        AddCourse.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AddCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 121, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.courseIDLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseIDLabel.setObjectName("courseIDLabel")
        self.verticalLayout.addWidget(self.courseIDLabel)
        self.courseNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.verticalLayout.addWidget(self.courseNameLabel)
        self.semesterLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.semesterLabel.setObjectName("semesterLabel")
        self.verticalLayout.addWidget(self.semesterLabel)
        self.departmentLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.verticalLayout.addWidget(self.departmentLabel)
        self.courseLevelLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseLevelLabel.setObjectName("courseLevelLabel")
        self.verticalLayout.addWidget(self.courseLevelLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 40, 131, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.courseIDLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.courseIDLine.setObjectName("courseIDLine")
        self.verticalLayout_2.addWidget(self.courseIDLine)
        self.couresNameLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.couresNameLine.setObjectName("couresNameLine")
        self.verticalLayout_2.addWidget(self.couresNameLine)
        self.semesterLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.semesterLine.setObjectName("semesterLine")
        self.verticalLayout_2.addWidget(self.semesterLine)
        self.departmentLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.departmentLine.setObjectName("departmentLine")
        self.verticalLayout_2.addWidget(self.departmentLine)
        self.courseLevelBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.courseLevelBox.setObjectName("courseLevelBox")
        self.courseLevelBox.addItem("")
        self.courseLevelBox.addItem("")
        self.verticalLayout_2.addWidget(self.courseLevelBox)
        AddCourse.setCentralWidget(self.centralwidget)

        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(200, 325, 113, 32))
        self.submitButton.setObjectName("Submit")


        self.menubar = QtWidgets.QMenuBar(AddCourse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AddCourse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddCourse)
        self.statusbar.setObjectName("statusbar")
        AddCourse.setStatusBar(self.statusbar)

        self.retranslateUi(AddCourse)
        QtCore.QMetaObject.connectSlotsByName(AddCourse)

        self.submitButton.clicked.connect(lambda: (self.saveValuesToDB()))


    def saveValuesToDB(self):
        try:
            conn = ConnectDB()
            query = "INSERT INTO `Courses` (`CourseID`, `CourseName`, `Semester`, `Department`, `CourseLevel`) " \
                    "VALUES (%s,%s,%s,%s,%s)"

            params = (self.courseIDLine.text(),self.couresNameLine.text(),self.semesterLine.text(),self.departmentLine.text()
                      ,self.courseLevelBox.currentText().__str__())

            conn.execute(query,params)
            CommonUIUtils.showSuccessMessage("Course Added Successfully!!")


        except mysql.connector.IntegrityError as err:
            print("Error:{}".format(err))



    def retranslateUi(self, AddCourse):
        _translate = QtCore.QCoreApplication.translate
        AddCourse.setWindowTitle(_translate("AddCourse", "Add Course"))
        self.courseIDLabel.setText(_translate("AddCourse", "CourseID"))
        self.courseNameLabel.setText(_translate("AddCourse", "CourseName"))
        self.semesterLabel.setText(_translate("AddCourse", "Semester"))
        self.departmentLabel.setText(_translate("AddCourse", "Department"))
        self.courseLevelLabel.setText(_translate("AddCourse", "CourseLevel"))
        self.courseLevelBox.setItemText(0, _translate("AddCourse", "Graduate"))
        self.courseLevelBox.setItemText(1, _translate("AddCourse", "Undergraduate"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCourse = QtWidgets.QMainWindow()
    ui = Ui_AddCourse()
    ui.setupUi(AddCourse)
    AddCourse.show()
    sys.exit(app.exec_())
