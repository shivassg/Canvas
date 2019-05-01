# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'professorUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from ConnectDB import ConnectDB
import mysql.connector
from CommonUIUtils import *
from CommonUtils import *


class Ui_ProfessorLoginWindow(object):

    LoggedInUserName = ''

    def __init__(self, userNameText):
        Ui_ProfessorLoginWindow.LoggedInUserName = userNameText

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 50, 691, 371))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardWidget = QtWidgets.QListWidget(self.widget)
        self.dashboardWidget.setObjectName("dashboardWidget")
        self.verticalLayout.addWidget(self.dashboardWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filesButton = QtWidgets.QPushButton(self.widget)
        self.filesButton.setObjectName("filesButton")
        self.horizontalLayout.addWidget(self.filesButton)
        self.peopleButton = QtWidgets.QPushButton(self.widget)
        self.peopleButton.setObjectName("peopleButton")
        self.horizontalLayout.addWidget(self.peopleButton)
        self.assignmentButton = QtWidgets.QPushButton(self.widget)
        self.assignmentButton.setObjectName("assignmentButton")
        self.horizontalLayout.addWidget(self.assignmentButton)
        self.gradeButton = QtWidgets.QPushButton(self.widget)
        self.gradeButton.setObjectName("gradeButton")
        self.horizontalLayout.addWidget(self.gradeButton)
        self.announcementButton = QtWidgets.QPushButton(self.widget)
        self.announcementButton.setObjectName("announcementButton")
        self.horizontalLayout.addWidget(self.announcementButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.dashboardLabel = QtWidgets.QLabel(self.centralwidget)
        self.dashboardLabel.setGeometry(QtCore.QRect(30, 20, 91, 31))
        self.dashboardLabel.setObjectName("dashboardLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addDashboardCourses()

        self.filesButton.clicked.connect(lambda: (self.openFileSection()))

        self.peopleButton.clicked.connect(lambda: (self.openPeopleSection()))

        self.assignmentButton.clicked.connect(lambda: (self.openAssignmentSection()))

        self.gradeButton.clicked.connect(lambda: (self.openGradeSection()))

        self.announcementButton.clicked.connect(lambda: (self.openAnnouncementSection()))

    def openAnnouncementSection(self):
        courseID = self.getSelectedRowCourseID()
        print(courseID)

    def openAssignmentSection(self):
        courseID = self.getSelectedRowCourseID()
        print(courseID)


    def openPeopleSection(self):
        courseID = self.getSelectedRowCourseID()
        print(courseID)


    def openFileSection(self):

        courseID = self.getSelectedRowCourseID()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminLoginWindow(firstNameText)
        self.ui.setupUi(self.window)
        self.window.show()

    def getSelectedRowCourseID(self):
        row = self.dashboardWidget.currentRow()
        selectedItem = (self.dashboardWidget.item(row)).text()
        selectedItemList = selectedItem.split()
        courseID = CommonUtils.getCourseIDFromNumberAndSemester(selectedItemList[0], selectedItemList[2])
        return courseID

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Professor Login"))
        self.filesButton.setText(_translate("MainWindow", "Files Section"))
        self.peopleButton.setText(_translate("MainWindow", "People Section"))
        self.assignmentButton.setText(_translate("MainWindow", "Assignment Section"))
        self.gradeButton.setText(_translate("MainWindow", "Grade Section"))
        self.announcementButton.setText(_translate("MainWindow", "Announcement"))
        self.dashboardLabel.setText(_translate("MainWindow", "Dashboard:"))

    def addDashboardCourses(self):
        conn = ConnectDB()
        userID = CommonUtils.getUserIDfromUserName(Ui_ProfessorLoginWindow.LoggedInUserName)
        query = "Select CourseID, Semester from course_professor_table where ProfessorID=%s"
        params = (userID,)
        courseIDWithSemesterList = conn.query(query,params)
        courseIDList = [courseID[0] for courseID in courseIDWithSemesterList]
        '''couresNameList = []
        couresNumberList =[]

        for courseID in courseIDList:
            couresNameList.append(CommonUtils.getCourseNameFromCourseID(courseID))
            couresNumberList.append(CommonUtils.getCourseNumberFromCourseID(courseID))'''

        courseNumberAndNameList=[]
        for couresID in courseIDList:
            courseNumberAndNameList.append(CommonUtils.getCourseNumberNameYearFromCourseID(couresID) )

        print(courseNumberAndNameList)

        courseTuple=()
        for courseIDAndName in courseNumberAndNameList:
            courseTuple = [x for x in courseIDAndName]
            courseNumber = courseTuple[0][0]
            courseName = courseTuple[0][1]
            courseYear = courseTuple[0][2]

            self.dashboardWidget.addItem( courseNumber +" "+ courseName+ " "+ courseYear)

        self.dashboardWidget.setCurrentRow(0)


        '''
        if not couresNameList:
            print("Empty List")

        for courseName in couresNameList:
            for couresNumber in couresNumberList:
                self.dashboardWidget.addItem(couresNumber + courseName)

        print(couresNameList)'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfessorLoginWindow("sganesan")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
