# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filesectionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class FileWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 478)
        self.FileSectionWindow = QtWidgets.QWidget(MainWindow)
        self.FileSectionWindow.setObjectName("FileSectionWindow")
        self.widget = QtWidgets.QWidget(self.FileSectionWindow)
        self.widget.setGeometry(QtCore.QRect(20, 60, 631, 291))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.downloadButton = QtWidgets.QPushButton(self.widget)
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout.addWidget(self.downloadButton)
        self.DeleteButton = QtWidgets.QPushButton(self.widget)
        self.DeleteButton.setObjectName("DeleteButton")
        self.verticalLayout.addWidget(self.DeleteButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.FileSectionWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Section"))
        self.addButton.setText(_translate("MainWindow", "Add File"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
